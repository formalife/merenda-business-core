#!/usr/bin/env python3
"""Measure static addressability of gold routing nodes.

This is NOT a behavioral eval. It compares explicit node coverage in the current
Decision Router with the draft Retrieval Map coverage linked to gold cases.
The result is useful for architecture diagnosis only.
"""

from __future__ import annotations

import json
from pathlib import Path
import re
from statistics import mean

ROOT = Path(__file__).resolve().parents[1]
ROUTER = ROOT / "merenda" / "DECISION_ROUTER.md"
EVAL_DIR = ROOT / "evals" / "routing"
MAP_DIR = ROOT / "reviews" / "drafts"

PATH_RE = re.compile(r"(?<![A-Za-z0-9_./-])((?:\.\./)?(?:[A-Za-z0-9_À-ÿ.-]+/)+[A-Za-z0-9_À-ÿ.-]+\.md)")


def gold_cases() -> dict[str, dict]:
    rows = {}
    for path in sorted(EVAL_DIR.glob("cases*.jsonl")):
        for raw in path.read_text(encoding="utf-8").splitlines():
            if not raw.strip():
                continue
            row = json.loads(raw)
            rows[row["id"]] = row
    return rows


def normalize_router_path(raw: str) -> str:
    raw = raw.removeprefix("../")
    if raw.startswith("merenda/") or raw.startswith("LAYER1_") or raw.startswith("FORMALIFE_"):
        return raw
    return "merenda/" + raw


def router_nodes() -> set[str]:
    text = ROUTER.read_text(encoding="utf-8")
    return {normalize_router_path(p) for p in PATH_RE.findall(text)}


def map_nodes_by_case() -> dict[str, set[str]]:
    out: dict[str, set[str]] = {}
    for path in sorted(MAP_DIR.glob("DOCTRINE_RETRIEVAL_MAP_V1_*.json")):
        payload = json.loads(path.read_text(encoding="utf-8"))
        for row in payload:
            canonical = row.get("canonical", {}).get("path")
            if not isinstance(canonical, str):
                continue
            for case_id in row.get("eval_cases", []):
                if isinstance(case_id, str):
                    out.setdefault(case_id, set()).add(canonical)
    return out


def recall(required: set[str], available: set[str]) -> float:
    return len(required & available) / len(required) if required else 1.0


def main() -> int:
    gold = gold_cases()
    current = router_nodes()
    mapped = map_nodes_by_case()

    rows = []
    for case_id, case in sorted(gold.items()):
        required = set(case["required_nodes"])
        current_recall = recall(required, current)
        map_recall = recall(required, mapped.get(case_id, set()))
        combined_recall = recall(required, current | mapped.get(case_id, set()))
        rows.append({
            "case_id": case_id,
            "required_count": len(required),
            "current_router_direct_recall": current_recall,
            "map_direct_recall": map_recall,
            "combined_direct_recall": combined_recall,
            "current_misses": sorted(required - current),
            "combined_misses": sorted(required - (current | mapped.get(case_id, set()))),
        })

    summary = {
        "cases": len(rows),
        "router_explicit_node_refs": len(current),
        "mean_current_router_direct_recall": mean(r["current_router_direct_recall"] for r in rows),
        "mean_map_direct_recall": mean(r["map_direct_recall"] for r in rows),
        "mean_combined_direct_recall": mean(r["combined_direct_recall"] for r in rows),
        "cases_with_current_router_full_direct_recall": sum(r["current_router_direct_recall"] == 1.0 for r in rows),
        "cases_with_combined_full_direct_recall": sum(r["combined_direct_recall"] == 1.0 for r in rows),
    }

    print(json.dumps({"summary": summary, "cases": rows}, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
