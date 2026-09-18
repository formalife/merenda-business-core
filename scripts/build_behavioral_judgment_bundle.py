#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ARCHS = ("current", "current_plus_map")
FAILURE_CATEGORIES = (
    "ROUTING_MISS",
    "DISCOVERY_MISS",
    "EXPANSION_MISS",
    "OVER_RETRIEVAL_DILUTION",
    "CORRECT_RETRIEVAL_BAD_SYNTHESIS",
    "GOLD_TOO_COARSE",
    "MAP_SUPPRESSION",
    "BOOTSTRAP_DILUTION",
    "PROVENANCE_FAILURE",
)


def load_gold() -> list[dict]:
    rows: list[dict] = []
    for path in sorted((ROOT / "evals" / "routing").glob("cases*.jsonl")):
        for line in path.read_text(encoding="utf-8").splitlines():
            if line.strip():
                rows.append(json.loads(line))
    ids = [r["id"] for r in rows]
    if len(ids) != len(set(ids)):
        raise SystemExit("duplicate case ids in gold suite")
    return rows


def load_trace(baseline: Path, arch: str, case_id: str) -> dict:
    path = baseline / "traces" / arch / f"{case_id}.json"
    if not path.is_file():
        raise SystemExit(f"missing frozen trace: {path}")
    row = json.loads(path.read_text(encoding="utf-8"))
    if row.get("case_id") != case_id or row.get("architecture") != arch:
        raise SystemExit(f"trace identity mismatch: {path}")
    return row


def deterministic_diff(gold: dict, trace: dict) -> dict:
    required = list(gold.get("required_nodes", []))
    optional = list(gold.get("optional_nodes", []))
    retrieved = list(trace.get("retrieved_nodes", []))
    relevant = set(required) | set(optional)
    return {
        "missing_required_nodes": [x for x in required if x not in retrieved],
        "retrieved_required_nodes": [x for x in required if x in retrieved],
        "retrieved_optional_nodes": [x for x in optional if x in retrieved],
        "over_retrieved_nodes": [x for x in retrieved if x not in relevant],
        "retrieved_sections": trace.get("retrieved_sections", []),
    }


def blank_judgment(case_id: str, arch: str) -> dict:
    return {
        "case_id": case_id,
        "architecture": arch,
        "satisfied_check_indices": [],
        "triggered_forbidden_shortcut_indices": [],
        "provenance_error": False,
        "unsupported_inference": False,
        "premature_tactic": False,
        "founder_accommodation_failure": False,
        "failure_categories": [],
        "material_failure": False,
        "notes": "",
    }


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument(
        "--baseline-dir",
        type=Path,
        default=Path("/tmp/formalife-routing-baseline"),
        help="Directory containing frozen baseline traces.",
    )
    ap.add_argument(
        "--out",
        type=Path,
        default=Path("/tmp/formalife-routing-judgment-bundle.jsonl"),
    )
    args = ap.parse_args()

    baseline = args.baseline_dir.resolve()
    gold = load_gold()
    rows = []
    for case in gold:
        cid = case["id"]
        traces = {arch: load_trace(baseline, arch, cid) for arch in ARCHS}
        rows.append(
            {
                "case_id": cid,
                "title": case.get("title"),
                "case_type": case.get("case_type"),
                "prompt": case.get("prompt"),
                "gold": {
                    "required_nodes": case.get("required_nodes", []),
                    "optional_nodes": case.get("optional_nodes", []),
                    "required_checks": case.get("required_checks", []),
                    "forbidden_shortcuts": case.get("forbidden_shortcuts", []),
                    "expected_behavior": case.get("expected_behavior"),
                    "provenance_checks": case.get("provenance_checks", []),
                    "notes": case.get("notes"),
                },
                "architectures": {
                    arch: {
                        "trace": traces[arch],
                        "deterministic_diff": deterministic_diff(case, traces[arch]),
                        "judgment_template": blank_judgment(cid, arch),
                    }
                    for arch in ARCHS
                },
                "allowed_failure_categories": list(FAILURE_CATEGORIES),
            }
        )

    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(
        "".join(json.dumps(row, ensure_ascii=False) + "\n" for row in rows),
        encoding="utf-8",
    )
    print(f"JUDGMENT BUNDLE: PASS cases={len(rows)} out={args.out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
