#!/usr/bin/env python3
"""Blind A/B behavioral gate for the Sandler integration cases R031-R041.

Compares the existing five-file full control plane with the promoted
REASONING_KERNEL.md while keeping specialist doctrine, semantic routing,
model, effort and isolation identical.

The harness supports both the complete Phase 6 suite and explicit targeted
reruns (for example R033,R041) when the merge-gate impact analysis proves that
a correction is local. Full and kernel always run on the exact same case set.
"""

from __future__ import annotations

import argparse
import json
import os
from pathlib import Path
import subprocess
import sys

import run_hierarchical_retriever_prototype_a_host as base
import run_architecture_holdout_ab_host as ab


ROOT = Path(__file__).resolve().parents[1]
PHASE6 = ROOT / "evals" / "routing" / "cases_phase6.jsonl"
FULL_ARCH = "sandler_a3_full"
KERNEL_ARCH = "sandler_a3_kernel"
DEFAULT_WORKDIR = Path("/tmp/formalife-sandler-integration-ab")
EXPECTED_BRANCH = "integrate-sandler-v1"
ALL_CASE_IDS = tuple(f"R{i:03d}" for i in range(31, 42))
SELECTED_CASE_IDS = ALL_CASE_IDS

# Preserve the local branch guard, while allowing the verified detached merge
# ref used by GitHub Actions for this exact PR head branch. A detached local
# checkout still fails because the GitHub PR environment variables are absent.
base.EXPECTED_BRANCH = EXPECTED_BRANCH
_ORIGINAL_GOUT = base.gout


def _integration_gout(repo: Path, *args: str) -> str:
    value = _ORIGINAL_GOUT(repo, *args)
    if args == ("branch", "--show-current") and value == "":
        if (
            os.environ.get("GITHUB_ACTIONS") == "true"
            and os.environ.get("GITHUB_HEAD_REF") == EXPECTED_BRANCH
        ):
            return EXPECTED_BRANCH
    return value


base.gout = _integration_gout

# Reuse the holdout machinery with the current promoted kernel, not the old
# pre-promotion draft used by the historical architecture holdout.
ab.FULL_ARCH = FULL_ARCH
ab.KERNEL_ARCH = KERNEL_ARCH
ab.KERNEL = ROOT / "REASONING_KERNEL.md"


def parse_cases(raw: str | None) -> tuple[str, ...]:
    if raw is None or not raw.strip():
        return ALL_CASE_IDS
    ids = tuple(dict.fromkeys(part.strip().upper() for part in raw.split(",") if part.strip()))
    if not ids:
        raise SystemExit("--cases must contain at least one case id")
    invalid = [cid for cid in ids if cid not in ALL_CASE_IDS]
    if invalid:
        raise SystemExit(f"invalid Phase 6 case ids: {invalid}; allowed={list(ALL_CASE_IDS)}")
    return ids


def load_phase6() -> list[dict]:
    rows = ab.load_jsonl(PHASE6)
    all_rows: dict[str, dict] = {}
    for row in rows:
        cid = row.get("id")
        if not isinstance(cid, str) or not cid.startswith("R"):
            raise SystemExit(f"invalid Phase 6 case id: {cid!r}")
        if cid in all_rows:
            raise SystemExit(f"duplicate Phase 6 case id: {cid}")
        all_rows[cid] = row

    actual_all = set(all_rows)
    expected_all = set(ALL_CASE_IDS)
    if actual_all != expected_all:
        raise SystemExit(
            "Phase 6 case set mismatch: "
            f"missing={sorted(expected_all - actual_all)} extra={sorted(actual_all - expected_all)}"
        )

    out: list[dict] = []
    for cid in SELECTED_CASE_IDS:
        row = all_rows[cid]
        out.append(
            {
                "case_id": cid,
                "title": row.get("title"),
                "case_type": row.get("case_type"),
                "prompt": row.get("prompt"),
            }
        )
    return out


# All reused A/B functions resolve this name at runtime.
ab.sanitized_holdout = load_phase6


def validate_setup(base_dir: Path) -> int:
    report: dict[str, dict] = {}
    expected_count = len(SELECTED_CASE_IDS)
    for variant in ("full", "kernel"):
        workdir = base_dir / variant
        _repo, arch, _branch, sha, prompts, root = ab.prepare_workspace(variant, workdir)
        if len(prompts) != expected_count:
            raise SystemExit(
                f"{variant}: expected {expected_count} selected Phase 6 cases, got {len(prompts)}"
            )
        if [row.get("case_id") for row in prompts] != list(SELECTED_CASE_IDS):
            raise SystemExit(
                f"{variant}: selected cases/order mismatch: "
                f"{[row.get('case_id') for row in prompts]} != {list(SELECTED_CASE_IDS)}"
            )
        forbidden_prompt_fields = {
            "required_nodes",
            "required_checks",
            "forbidden_shortcuts",
            "expected_behavior",
            "provenance_checks",
            "required_semantic_units",
            "optional_semantic_units",
        }
        for row in prompts:
            leaked = forbidden_prompt_fields & row.keys()
            if leaked:
                raise SystemExit(f"{variant}/{row.get('case_id')}: leaked gold fields {sorted(leaked)}")
        if any((root / name).exists() for name in ("evals", "reviews", "STATUS.md")):
            raise SystemExit(f"{variant}: forbidden gold/review material in sterile workspace")
        report[variant] = {
            "architecture": arch,
            "commit_sha": sha,
            "cases": len(prompts),
            "case_ids": list(SELECTED_CASE_IDS),
            "fixed_control_chars": ab.fixed_control_chars(variant, root),
            "workspace": str(root),
        }

    fchars = report["full"]["fixed_control_chars"]
    kchars = report["kernel"]["fixed_control_chars"]
    ratio = kchars / fchars if fchars else 0.0
    base_dir.mkdir(parents=True, exist_ok=True)
    (base_dir / "setup-validation.json").write_text(
        json.dumps(
            {
                "variants": report,
                "selected_case_ids": list(SELECTED_CASE_IDS),
                "kernel_to_full_control_ratio": ratio,
            },
            indent=2,
        )
        + "\n",
        encoding="utf-8",
    )
    print("SANDLER INTEGRATION A/B SETUP: PASS")
    print(f"cases_per_variant={expected_count}")
    print("case_ids=" + ",".join(SELECTED_CASE_IDS))
    print(f"full_fixed_control_chars={fchars}")
    print(f"kernel_fixed_control_chars={kchars}")
    print(f"kernel_to_full_control_ratio={ratio:.3f}")
    print("codex_calls=0")
    return 0


def run_variant(variant: str, workdir: Path) -> int:
    rc = ab.run_variant(variant, workdir)
    if rc:
        return rc
    trace = workdir / "holdout-trace.jsonl"
    score = workdir / "semantic-score.json"
    base.run(
        [
            sys.executable,
            "scripts/score_semantic_routing_run.py",
            "--trace",
            str(trace),
            "--json-out",
            str(score),
        ],
        ROOT,
    )
    return 0


def blind_bundle(base_dir: Path) -> None:
    ab.blind_bundle(base_dir)
    src_bundle = base_dir / "holdout-blind-answer-bundle.jsonl"
    src_mapping = base_dir / "holdout-blind-mapping.json"
    (base_dir / "sandler-blind-answer-bundle.jsonl").write_text(
        src_bundle.read_text(encoding="utf-8"), encoding="utf-8"
    )
    (base_dir / "sandler-blind-mapping.json").write_text(
        src_mapping.read_text(encoding="utf-8"), encoding="utf-8"
    )


def score_summary(path: Path, arch: str) -> dict:
    payload = json.loads(path.read_text(encoding="utf-8"))
    return payload["summary"][arch]


def orchestrate(base_dir: Path) -> int:
    base_dir.mkdir(parents=True, exist_ok=True)
    script = Path(__file__).resolve()
    selected_arg = ",".join(SELECTED_CASE_IDS)
    for variant in ("full", "kernel"):
        proc = subprocess.run(
            [
                sys.executable,
                str(script),
                "--internal-variant",
                variant,
                "--cases",
                selected_arg,
                "--workdir",
                str(base_dir / variant),
            ],
            cwd=ROOT,
        )
        if proc.returncode:
            return 2

    blind_bundle(base_dir)
    full = score_summary(base_dir / "full" / "semantic-score.json", FULL_ARCH)
    kernel = score_summary(base_dir / "kernel" / "semantic-score.json", KERNEL_ARCH)
    summary = {
        "selected_case_ids": list(SELECTED_CASE_IDS),
        "full": full,
        "kernel": kernel,
    }
    (base_dir / "semantic-ab-summary.json").write_text(
        json.dumps(summary, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )

    count = len(SELECTED_CASE_IDS)
    print("\n==============================================")
    print("SANDLER INTEGRATION A/B — TRACE GENERATION COMPLETE")
    print("==============================================")
    print(f"Cases per architecture: {count}")
    print("Case ids: " + ",".join(SELECTED_CASE_IDS))
    print(f"Codex calls total: {count * 2}")
    print(
        "Full semantic verified recall="
        f"{full['mean_verified_semantic_recall']:.4f} "
        "precision="
        f"{full['mean_verified_semantic_precision']:.4f} "
        "full_recall_cases="
        f"{full['cases_full_verified_recall']}/{full['cases']}"
    )
    print(
        "Kernel semantic verified recall="
        f"{kernel['mean_verified_semantic_recall']:.4f} "
        "precision="
        f"{kernel['mean_verified_semantic_precision']:.4f} "
        "full_recall_cases="
        f"{kernel['cases_full_verified_recall']}/{kernel['cases']}"
    )
    print("Blind answer bundle:", base_dir / "sandler-blind-answer-bundle.jsonl")
    print("Blind mapping (DO NOT REVEAL BEFORE JUDGMENT):", base_dir / "sandler-blind-mapping.json")
    print("Semantic A/B summary:", base_dir / "semantic-ab-summary.json")
    print("Judge answers against the selected Phase 6 checks before revealing the mapping.")
    return 0


def main() -> int:
    global SELECTED_CASE_IDS

    ap = argparse.ArgumentParser()
    ap.add_argument("--workdir", type=Path, default=DEFAULT_WORKDIR)
    ap.add_argument("--validate-only", action="store_true")
    ap.add_argument(
        "--cases",
        help="Comma-separated Phase 6 case ids. Default: full R031-R041 suite.",
    )
    ap.add_argument("--internal-variant", choices=("full", "kernel"), help=argparse.SUPPRESS)
    args = ap.parse_args()

    SELECTED_CASE_IDS = parse_cases(args.cases)

    if args.validate_only and args.internal_variant:
        raise SystemExit("use --validate-only or --internal-variant, not both")
    if args.validate_only:
        return validate_setup(args.workdir)
    if args.internal_variant:
        return run_variant(args.internal_variant, args.workdir)
    return orchestrate(args.workdir)


if __name__ == "__main__":
    raise SystemExit(main())
