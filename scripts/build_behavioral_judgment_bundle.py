#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
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


def sanitized_trace(trace: dict) -> dict:
    return {
        "case_id": trace.get("case_id"),
        "retrieved_nodes": trace.get("retrieved_nodes", []),
        "retrieved_sections": trace.get("retrieved_sections", []),
        "classification": trace.get("classification", []),
        "decision_level": trace.get("decision_level"),
        "answer": trace.get("answer"),
        "trace_notes": trace.get("trace_notes"),
    }


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


def blank_judgment(case_id: str, blind_label: str) -> dict:
    return {
        "case_id": case_id,
        "architecture": blind_label,
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


def blind_order(case_id: str) -> tuple[str, str]:
    first = hashlib.sha256(case_id.encode("utf-8")).digest()[0]
    return ARCHS if first % 2 == 0 else tuple(reversed(ARCHS))


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
    ap.add_argument(
        "--mapping-out",
        type=Path,
        default=Path("/tmp/formalife-routing-judgment-mapping.json"),
        help="Keep separate from the reviewer until judgments are frozen.",
    )
    args = ap.parse_args()

    baseline = args.baseline_dir.resolve()
    gold = load_gold()
    rows = []
    mapping: dict[str, dict[str, str]] = {}

    for case in gold:
        cid = case["id"]
        traces = {arch: load_trace(baseline, arch, cid) for arch in ARCHS}
        ordered_archs = blind_order(cid)
        labels = {"A": ordered_archs[0], "B": ordered_archs[1]}
        mapping[cid] = labels

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
                    blind_label: {
                        "trace": sanitized_trace(traces[real_arch]),
                        "deterministic_diff": deterministic_diff(case, traces[real_arch]),
                        "judgment_template": blank_judgment(cid, blind_label),
                    }
                    for blind_label, real_arch in labels.items()
                },
                "allowed_failure_categories": list(FAILURE_CATEGORIES),
            }
        )

    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.mapping_out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(
        "".join(json.dumps(row, ensure_ascii=False) + "\n" for row in rows),
        encoding="utf-8",
    )
    args.mapping_out.write_text(
        json.dumps(
            {
                "warning": "Do not expose this mapping to the reviewer until judgments are frozen.",
                "mapping": mapping,
            },
            ensure_ascii=False,
            indent=2,
        )
        + "\n",
        encoding="utf-8",
    )
    print(
        f"JUDGMENT BUNDLE: PASS cases={len(rows)} out={args.out} "
        f"mapping={args.mapping_out}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
