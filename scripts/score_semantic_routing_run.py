#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from pathlib import Path
from statistics import mean

ROOT = Path(__file__).resolve().parents[1]
GOLD = ROOT / "evals" / "routing" / "semantic_gold_v2.jsonl"


def load_gold() -> dict[str, dict]:
    out: dict[str, dict] = {}
    for raw in GOLD.read_text(encoding="utf-8").splitlines():
        if not raw.strip():
            continue
        row = json.loads(raw)
        cid = row["case_id"]
        if cid in out:
            raise ValueError(f"duplicate gold case: {cid}")
        out[cid] = row
    return out


def load_traces(path: Path) -> list[dict]:
    rows: list[dict] = []
    seen: set[tuple[str, str]] = set()
    for lineno, raw in enumerate(path.read_text(encoding="utf-8").splitlines(), start=1):
        if not raw.strip():
            continue
        row = json.loads(raw)
        key = (row.get("case_id"), row.get("architecture"))
        if not all(isinstance(x, str) for x in key):
            raise ValueError(f"{path}:{lineno}: missing case_id/architecture")
        if key in seen:
            raise ValueError(f"{path}:{lineno}: duplicate trace {key}")
        seen.add(key)
        rows.append(row)
    return rows


def as_set(row: dict, field: str) -> set[str]:
    value = row.get(field, [])
    if not isinstance(value, list) or not all(isinstance(x, str) for x in value):
        raise ValueError(f"{row.get('case_id')}: {field} must be list[str]")
    return set(value)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--trace", type=Path, required=True)
    ap.add_argument("--json-out", type=Path)
    args = ap.parse_args()

    try:
        gold = load_gold()
        traces = load_traces(args.trace)
    except (ValueError, json.JSONDecodeError) as exc:
        raise SystemExit(str(exc))

    scored = []
    errors: list[str] = []
    for trace in traces:
        cid = trace["case_id"]
        arch = trace["architecture"]
        if cid not in gold:
            errors.append(f"unknown case in trace: {cid}")
            continue
        g = gold[cid]
        required = set(g["required_semantic_units"])
        optional = set(g["optional_semantic_units"])
        relevant = required | optional
        try:
            selected = as_set(trace, "selected_semantic_units")
            verified_raw = as_set(trace, "verified_semantic_units")
        except ValueError as exc:
            errors.append(str(exc))
            continue

        # Recall is allowed to benefit from any canonical semantic exposure,
        # including structural discovery. Precision, however, must score focused
        # routing choices rather than semantic units passively exposed by mandatory
        # bootstrap reads. Therefore the precision denominator is restricted to
        # semantic IDs that were explicitly selected and then canonically verified.
        verified_focused = verified_raw & selected
        verified_passive = verified_raw - selected

        selected_hits = selected & required
        verified_hits = verified_raw & required
        selected_relevant = selected & relevant
        focused_verified_relevant = verified_focused & relevant
        stats = trace.get("retrieval_stats", {})
        if not isinstance(stats, dict):
            stats = {}

        scored.append(
            {
                "case_id": cid,
                "architecture": arch,
                "required_semantic_units": sorted(required),
                "selected_semantic_recall": len(selected_hits) / len(required) if required else 1.0,
                "verified_semantic_recall": len(verified_hits) / len(required) if required else 1.0,
                "selected_semantic_precision": len(selected_relevant) / len(selected) if selected else 0.0,
                "verified_semantic_precision": (
                    len(focused_verified_relevant) / len(verified_focused) if verified_focused else 0.0
                ),
                "required_selected": sorted(selected_hits),
                "required_verified": sorted(verified_hits),
                "required_missed": sorted(required - verified_raw),
                "over_selected": sorted(selected - relevant),
                "over_verified": sorted(verified_focused - relevant),
                "passive_verified": sorted(verified_passive),
                "selected_count": len(selected),
                "verified_count": len(verified_focused),
                "verified_count_raw": len(verified_raw),
                "passive_verified_count": len(verified_passive),
                "full_node_reads": int(stats.get("full_node_reads", 0) or 0),
                "section_reads": int(stats.get("section_reads", 0) or 0),
                "semantic_entry_reads": int(stats.get("semantic_entry_reads", 0) or 0),
                "structural_searches": int(stats.get("structural_searches", 0) or 0),
            }
        )

    if errors:
        print("SEMANTIC ROUTING SCORE: FAIL")
        for error in errors:
            print(f"- {error}")
        return 1

    by_arch: dict[str, list[dict]] = {}
    for row in scored:
        by_arch.setdefault(row["architecture"], []).append(row)

    summary = {}
    for arch, rows in sorted(by_arch.items()):
        summary[arch] = {
            "cases": len(rows),
            "mean_selected_semantic_recall": mean(r["selected_semantic_recall"] for r in rows),
            "mean_verified_semantic_recall": mean(r["verified_semantic_recall"] for r in rows),
            "mean_selected_semantic_precision": mean(r["selected_semantic_precision"] for r in rows),
            "mean_verified_semantic_precision": mean(r["verified_semantic_precision"] for r in rows),
            "cases_full_verified_recall": sum(r["verified_semantic_recall"] == 1.0 for r in rows),
            "total_over_selected": sum(len(r["over_selected"]) for r in rows),
            "total_over_verified": sum(len(r["over_verified"]) for r in rows),
            "total_passive_verified": sum(r["passive_verified_count"] for r in rows),
            "total_full_node_reads": sum(r["full_node_reads"] for r in rows),
            "total_section_reads": sum(r["section_reads"] for r in rows),
            "total_semantic_entry_reads": sum(r["semantic_entry_reads"] for r in rows),
            "total_structural_searches": sum(r["structural_searches"] for r in rows),
        }

    output = {
        "metric_definition": {
            "verified_semantic_recall": "required units canonically exposed by focused semantic retrieval or structural discovery",
            "verified_semantic_precision": "precision over semantic units explicitly selected and then canonically verified; passive bootstrap exposure excluded",
            "passive_verified": "canonically exposed semantic units not explicitly selected; reported separately and excluded from precision denominator",
        },
        "summary": summary,
        "cases": scored,
    }
    print(json.dumps(output, ensure_ascii=False, indent=2))
    if args.json_out:
        args.json_out.parent.mkdir(parents=True, exist_ok=True)
        args.json_out.write_text(json.dumps(output, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
