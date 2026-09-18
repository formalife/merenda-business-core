#!/usr/bin/env python3
"""Score routing eval traces against gold cases.

Deterministic metrics only: required node recall, relevant retrieval precision,
over-retrieval, and optional judgment fields when provided.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
import sys
from statistics import mean

ROOT = Path(__file__).resolve().parents[1]
EVAL_DIR = ROOT / "evals" / "routing"


def load_gold() -> dict[str, dict]:
    gold: dict[str, dict] = {}
    for path in sorted(EVAL_DIR.glob("cases*.jsonl")):
        for lineno, raw in enumerate(path.read_text(encoding="utf-8").splitlines(), start=1):
            if not raw.strip():
                continue
            row = json.loads(raw)
            case_id = row["id"]
            if case_id in gold:
                raise ValueError(f"duplicate gold case {case_id}")
            gold[case_id] = row
    return gold


def load_jsonl(path: Path) -> dict[tuple[str, str], dict]:
    rows: dict[tuple[str, str], dict] = {}
    for lineno, raw in enumerate(path.read_text(encoding="utf-8").splitlines(), start=1):
        if not raw.strip():
            continue
        row = json.loads(raw)
        case_id = row.get("case_id")
        architecture = row.get("architecture")
        if not isinstance(case_id, str) or not isinstance(architecture, str):
            raise ValueError(f"{path}:{lineno}: case_id and architecture are required strings")
        key = (case_id, architecture)
        if key in rows:
            raise ValueError(f"{path}:{lineno}: duplicate record {key}")
        rows[key] = row
    return rows


def safe_indices(value, limit: int) -> set[int]:
    if not isinstance(value, list):
        return set()
    out = set()
    for item in value:
        if isinstance(item, int) and 0 <= item < limit:
            out.add(item)
    return out


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--trace", type=Path, required=True)
    parser.add_argument("--judgment", type=Path)
    parser.add_argument("--json-out", type=Path)
    args = parser.parse_args()

    gold = load_gold()
    traces = load_jsonl(args.trace)
    judgments = load_jsonl(args.judgment) if args.judgment else {}

    errors: list[str] = []
    scored = []

    for (case_id, architecture), trace in sorted(traces.items()):
        if case_id not in gold:
            errors.append(f"trace references unknown case {case_id}")
            continue
        case = gold[case_id]
        retrieved = trace.get("retrieved_nodes", [])
        if not isinstance(retrieved, list) or not all(isinstance(x, str) for x in retrieved):
            errors.append(f"{case_id}/{architecture}: retrieved_nodes must be list[str]")
            continue

        required = set(case["required_nodes"])
        optional = set(case["optional_nodes"])
        retrieved_set = set(retrieved)
        relevant = required | optional

        required_hits = required & retrieved_set
        relevant_hits = relevant & retrieved_set
        over = retrieved_set - relevant

        node_recall = len(required_hits) / len(required) if required else 1.0
        precision = len(relevant_hits) / len(retrieved_set) if retrieved_set else 0.0

        record = {
            "case_id": case_id,
            "architecture": architecture,
            "required_node_recall": node_recall,
            "relevant_retrieval_precision": precision,
            "required_nodes_hit": sorted(required_hits),
            "required_nodes_missed": sorted(required - retrieved_set),
            "over_retrieved_nodes": sorted(over),
            "retrieved_node_count": len(retrieved_set),
        }

        judgment = judgments.get((case_id, architecture))
        if judgment:
            checks = safe_indices(judgment.get("satisfied_check_indices"), len(case["required_checks"]))
            shortcuts = safe_indices(
                judgment.get("triggered_forbidden_shortcut_indices"),
                len(case["forbidden_shortcuts"]),
            )
            record.update({
                "required_check_recall": len(checks) / len(case["required_checks"]) if case["required_checks"] else 1.0,
                "forbidden_shortcut_rate": len(shortcuts) / len(case["forbidden_shortcuts"]) if case["forbidden_shortcuts"] else 0.0,
                "provenance_error": bool(judgment.get("provenance_error", False)),
                "unsupported_inference": bool(judgment.get("unsupported_inference", False)),
                "premature_tactic": bool(judgment.get("premature_tactic", False)),
                "founder_accommodation_failure": bool(judgment.get("founder_accommodation_failure", False)),
            })

        scored.append(record)

    if errors:
        print("ROUTING RUN SCORE: FAIL")
        for error in errors:
            print(f"- {error}")
        return 1

    by_arch: dict[str, list[dict]] = {}
    for row in scored:
        by_arch.setdefault(row["architecture"], []).append(row)

    summary = {}
    for architecture, rows in sorted(by_arch.items()):
        item = {
            "cases": len(rows),
            "mean_required_node_recall": mean(r["required_node_recall"] for r in rows),
            "mean_relevant_retrieval_precision": mean(r["relevant_retrieval_precision"] for r in rows),
            "total_over_retrieved_nodes": sum(len(r["over_retrieved_nodes"]) for r in rows),
        }
        judged = [r for r in rows if "required_check_recall" in r]
        if judged:
            item.update({
                "judged_cases": len(judged),
                "mean_required_check_recall": mean(r["required_check_recall"] for r in judged),
                "mean_forbidden_shortcut_rate": mean(r["forbidden_shortcut_rate"] for r in judged),
                "provenance_error_rate": mean(float(r["provenance_error"]) for r in judged),
                "unsupported_inference_rate": mean(float(r["unsupported_inference"]) for r in judged),
                "premature_tactic_rate": mean(float(r["premature_tactic"]) for r in judged),
                "founder_accommodation_failure_rate": mean(float(r["founder_accommodation_failure"]) for r in judged),
            })
        summary[architecture] = item

    output = {"summary": summary, "cases": scored}
    print(json.dumps(output, ensure_ascii=False, indent=2))
    if args.json_out:
        args.json_out.parent.mkdir(parents=True, exist_ok=True)
        args.json_out.write_text(json.dumps(output, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return 0


if __name__ == "__main__":
    sys.exit(main())
