#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import os
import secrets
import shutil
import subprocess
import sys
from pathlib import Path

import run_hierarchical_retriever_prototype_a_host as base
import run_hierarchical_retriever_prototype_a3_host  # noqa: F401  # appends A3 discipline to base.COMMON

ROOT = Path(__file__).resolve().parents[1]
HOLDOUT = ROOT / "evals" / "routing" / "holdout_v1.jsonl"
KERNEL = ROOT / "reviews" / "drafts" / "COMPACT_REASONING_KERNEL_V1.md"
FULL_ARCH = "holdout_a3_full"
KERNEL_ARCH = "holdout_a3_kernel"
A3_COMMON = base.COMMON
ORIGINAL_PREP = base.prep
ORIGINAL_STERILE = base.sterile
ORIGINAL_CONTROL = set(base.CONTROL)


def load_jsonl(path: Path) -> list[dict]:
    rows: list[dict] = []
    for lineno, raw in enumerate(path.read_text(encoding="utf-8").splitlines(), start=1):
        if not raw.strip():
            continue
        row = json.loads(raw)
        if not isinstance(row, dict):
            raise SystemExit(f"{path}:{lineno}: expected object")
        rows.append(row)
    return rows


def sanitized_holdout() -> list[dict]:
    rows = load_jsonl(HOLDOUT)
    out: list[dict] = []
    seen: set[str] = set()
    for row in rows:
        cid = row.get("id")
        if not isinstance(cid, str) or not cid.startswith("H"):
            raise SystemExit(f"invalid holdout id: {cid!r}")
        if cid in seen:
            raise SystemExit(f"duplicate holdout id: {cid}")
        seen.add(cid)
        out.append(
            {
                "case_id": cid,
                "title": row.get("title"),
                "case_type": row.get("case_type"),
                "prompt": row.get("prompt"),
            }
        )
    if len(out) != 6:
        raise SystemExit(f"holdout v1 must contain exactly 6 cases; got {len(out)}")
    return out


def common_for(arch: str, kernel: bool) -> str:
    text = A3_COMMON
    text = text.replace("ARCHITETTURA=prototype_a.", f"ARCHITETTURA={arch}.")
    text = text.replace('"architecture":"prototype_a"', f'"architecture":"{arch}"')
    if kernel:
        start_marker = "CONTROL PLANE FISSO — devi leggere prima integralmente:"
        start = text.find(start_marker)
        if start < 0:
            raise SystemExit("cannot locate full control-plane block in A3 prompt")
        end = text.find("\n\nARCHITETTURA=", start)
        if end < 0:
            raise SystemExit("cannot locate architecture marker after control-plane block")
        replacement = (
            "REASONING KERNEL FISSO — devi leggere prima integralmente:\n"
            "- REASONING_KERNEL.md\n\n"
            "Il kernel è una sintesi sperimentale del control plane. Non sostituisce la doctrine specialistica: "
            "quando una decisione è materiale, recupera comunque le semantic unit/sezioni canoniche pertinenti."
        )
        text = text[:start] + replacement + text[end:]
    return text


def prep_holdout(repo: Path, workdir: Path) -> tuple[str, str, list[dict], Path, Path]:
    branch, sha, _ignored, sem_json, struct_json = ORIGINAL_PREP(repo, workdir)
    prompts = sanitized_holdout()
    prompt_path = workdir / "routing-prompts.jsonl"
    prompt_path.write_text(
        "".join(json.dumps(row, ensure_ascii=False) + "\n" for row in prompts),
        encoding="utf-8",
    )
    return branch, sha, prompts, sem_json, struct_json


def sterile_kernel(repo: Path, dest: Path, sem_json: Path, struct_json: Path) -> None:
    if dest.exists():
        shutil.rmtree(dest)
    dest.mkdir(parents=True)
    shutil.copytree(repo / "merenda", dest / "merenda")
    shutil.copy2(KERNEL, dest / "REASONING_KERNEL.md")
    retr = dest / ".retrieval"
    retr.mkdir()
    shutil.copy2(sem_json, retr / "semantic-index-v2.json")
    shutil.copy2(struct_json, retr / "structural-index.json")
    (dest / "EVAL_READER.py").write_text(base.READER, encoding="utf-8")
    os.chmod(dest / "EVAL_READER.py", 0o755)
    for forbidden in (dest / "evals", dest / "reviews", dest / "STATUS.md"):
        if forbidden.exists():
            raise SystemExit(f"forbidden material leaked into kernel workspace: {forbidden}")


def configure_variant(variant: str):
    if variant == "full":
        arch = FULL_ARCH
        base.ARCH = arch
        base.COMMON = common_for(arch, kernel=False)
        base.CONTROL = set(ORIGINAL_CONTROL)
        return arch, ORIGINAL_STERILE
    if variant == "kernel":
        arch = KERNEL_ARCH
        base.ARCH = arch
        base.COMMON = common_for(arch, kernel=True)
        base.CONTROL = {"REASONING_KERNEL.md"}
        return arch, sterile_kernel
    raise SystemExit(f"unknown variant: {variant}")


def prepare_workspace(variant: str, workdir: Path):
    repo = Path.cwd().resolve()
    arch, sterile_fn = configure_variant(variant)
    branch, sha, prompts, sem_json, struct_json = prep_holdout(repo, workdir)
    root = workdir / f"workspace-{arch}"
    sterile_fn(repo, root, sem_json, struct_json)
    return repo, arch, branch, sha, prompts, root


def fixed_control_chars(variant: str, root: Path) -> int:
    if variant == "kernel":
        return len((root / "REASONING_KERNEL.md").read_text(encoding="utf-8"))
    return sum(len((root / rel).read_text(encoding="utf-8")) for rel in sorted(ORIGINAL_CONTROL))


def validate_setup(base_dir: Path) -> int:
    report: dict[str, dict] = {}
    for variant in ("full", "kernel"):
        workdir = base_dir / variant
        _repo, arch, _branch, sha, prompts, root = prepare_workspace(variant, workdir)
        forbidden_prompt_fields = {
            "required_nodes",
            "required_checks",
            "forbidden_shortcuts",
            "expected_behavior",
            "provenance_checks",
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
            "fixed_control_chars": fixed_control_chars(variant, root),
            "workspace": str(root),
        }

    fchars = report["full"]["fixed_control_chars"]
    kchars = report["kernel"]["fixed_control_chars"]
    ratio = kchars / fchars if fchars else 0.0
    (base_dir / "holdout-setup-validation.json").write_text(
        json.dumps({"variants": report, "kernel_to_full_control_ratio": ratio}, indent=2) + "\n",
        encoding="utf-8",
    )
    print("ARCHITECTURE HOLDOUT SETUP: PASS")
    print("cases_per_variant=6")
    print(f"full_fixed_control_chars={fchars}")
    print(f"kernel_fixed_control_chars={kchars}")
    print(f"kernel_to_full_control_ratio={ratio:.3f}")
    print("codex_calls=0")
    return 0


def run_variant(variant: str, workdir: Path) -> int:
    _repo, arch, branch, sha, prompts, root = prepare_workspace(variant, workdir)

    metadata = {
        "repository": "formalife/merenda-business-core",
        "branch": branch,
        "commit_sha": sha,
        "model": base.MODEL,
        "reasoning_effort": base.EFFORT,
        "architecture": arch,
        "cases": [p["case_id"] for p in prompts],
        "holdout": "v1",
        "isolation": "fresh codex exec process per case; holdout gold physically absent from sterile workspace",
        "gold_exposure": "absent; only case id/title/type/prompt exported",
        "bootstrap": "five canonical full control-plane files" if variant == "full" else "COMPACT_REASONING_KERNEL_V1 only",
    }
    workdir.mkdir(parents=True, exist_ok=True)
    (workdir / "metadata.json").write_text(json.dumps(metadata, indent=2) + "\n", encoding="utf-8")

    traces: list[dict] = []
    try:
        for case in prompts:
            traces.append(base.one(root, case, workdir))
    except Exception as exc:
        print(f"\nHOLDOUT {variant.upper()} STOPPED: {exc}", file=sys.stderr)
        return 2

    trace_path = workdir / "holdout-trace.jsonl"
    base.write_jsonl(trace_path, traces)
    ctx = base.context_summary(traces)
    (workdir / "holdout-context-summary.json").write_text(
        json.dumps({arch: ctx}, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )

    print("\n==============================================")
    print(f"ARCHITECTURE HOLDOUT {variant.upper()} — PASS")
    print("==============================================")
    print("Commit testato:", sha)
    print("Cases:", len(traces))
    print(
        "Context mean chars="
        f"{ctx['mean_operation_chars']:.0f} "
        "routing_metadata="
        f"{ctx['mean_category_chars']['routing_metadata']:.0f} "
        "structural_metadata="
        f"{ctx['mean_category_chars']['structural_metadata']:.0f} "
        "specialist_doctrine="
        f"{ctx['mean_category_chars']['specialist_doctrine']:.0f} "
        "control_plane="
        f"{ctx['mean_category_chars']['control_plane']:.0f}"
    )
    print("Output locale:", workdir)
    print("No holdout judgment executed.")
    return 0


def blind_bundle(base_dir: Path) -> None:
    prompts = {r["case_id"]: r for r in sanitized_holdout()}
    full_rows = {r["case_id"]: r for r in load_jsonl(base_dir / "full" / "holdout-trace.jsonl")}
    kernel_rows = {r["case_id"]: r for r in load_jsonl(base_dir / "kernel" / "holdout-trace.jsonl")}
    case_ids = sorted(prompts)
    if set(full_rows) != set(case_ids) or set(kernel_rows) != set(case_ids):
        raise SystemExit("holdout trace set mismatch")

    mapping_path = base_dir / "holdout-blind-mapping.json"
    bundle_path = base_dir / "holdout-blind-answer-bundle.jsonl"
    if mapping_path.exists():
        mapping = json.loads(mapping_path.read_text(encoding="utf-8"))
    else:
        mapping = {"cases": {}}
        for cid in case_ids:
            if secrets.randbits(1):
                mapping["cases"][cid] = {"A": FULL_ARCH, "B": KERNEL_ARCH}
            else:
                mapping["cases"][cid] = {"A": KERNEL_ARCH, "B": FULL_ARCH}
        mapping_path.write_text(json.dumps(mapping, indent=2) + "\n", encoding="utf-8")

    rows: list[dict] = []
    for cid in case_ids:
        variants = {FULL_ARCH: full_rows[cid], KERNEL_ARCH: kernel_rows[cid]}
        labels = mapping["cases"][cid]
        row = {
            "case_id": cid,
            "title": prompts[cid].get("title"),
            "case_type": prompts[cid].get("case_type"),
            "prompt": prompts[cid].get("prompt"),
        }
        for label in ("A", "B"):
            trace = variants[labels[label]]
            row[label] = {
                "classification": trace.get("classification", []),
                "decision_level": trace.get("decision_level"),
                "answer": trace.get("answer"),
            }
        rows.append(row)
    base.write_jsonl(bundle_path, rows)


def orchestrate(base_dir: Path) -> int:
    if subprocess.run(
        [sys.executable, __file__, "--internal-variant", "full", "--workdir", str(base_dir / "full")],
        cwd=Path.cwd(),
    ).returncode:
        return 2
    if subprocess.run(
        [sys.executable, __file__, "--internal-variant", "kernel", "--workdir", str(base_dir / "kernel")],
        cwd=Path.cwd(),
    ).returncode:
        return 2
    blind_bundle(base_dir)

    summaries = {}
    for variant, arch in (("full", FULL_ARCH), ("kernel", KERNEL_ARCH)):
        data = json.loads((base_dir / variant / "holdout-context-summary.json").read_text(encoding="utf-8"))[arch]
        summaries[variant] = data
    (base_dir / "holdout-ab-context-summary.json").write_text(
        json.dumps(summaries, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )

    full = summaries["full"]
    kernel = summaries["kernel"]
    fchars = full["mean_operation_chars"]
    kchars = kernel["mean_operation_chars"]
    delta = (kchars - fchars) / fchars if fchars else 0.0
    print("\n==============================================")
    print("ARCHITECTURE HOLDOUT A/B — COMPLETE")
    print("==============================================")
    print("Cases per architecture: 6")
    print("Codex calls total: 12")
    print(f"Full bootstrap mean chars: {fchars:.0f}")
    print(f"Kernel bootstrap mean chars: {kchars:.0f}")
    print(f"Kernel total-context delta: {delta:+.1%}")
    print("Blind answer bundle:", base_dir / "holdout-blind-answer-bundle.jsonl")
    print("Blind mapping (DO NOT UPLOAD YET):", base_dir / "holdout-blind-mapping.json")
    print("Judge blind answers before revealing mapping or retrieval traces.")
    return 0


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--workdir", type=Path, default=Path("/tmp/formalife-architecture-holdout-ab"))
    ap.add_argument("--validate-only", action="store_true", help="Build and verify both sterile variants without Codex calls.")
    ap.add_argument("--internal-variant", choices=("full", "kernel"), help=argparse.SUPPRESS)
    args = ap.parse_args()
    if args.validate_only and args.internal_variant:
        raise SystemExit("use --validate-only or --internal-variant, not both")
    if args.validate_only:
        return validate_setup(args.workdir)
    if args.internal_variant:
        return run_variant(args.internal_variant, args.workdir)
    return orchestrate(args.workdir)


if __name__ == "__main__":
    raise SystemExit(main())
