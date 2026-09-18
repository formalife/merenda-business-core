#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EVAL_DIR = ROOT / "evals" / "routing"
MAP_DIR = ROOT / "reviews" / "drafts"


def load_cases() -> list[dict]:
    rows: list[dict] = []
    for path in sorted(EVAL_DIR.glob("cases*.jsonl")):
        for raw in path.read_text(encoding="utf-8").splitlines():
            if raw.strip():
                rows.append(json.loads(raw))
    ids = [r["id"] for r in rows]
    if len(ids) != len(set(ids)):
        raise SystemExit("duplicate case ids")
    return rows


def load_map_entries() -> list[dict]:
    rows: list[dict] = []
    for path in sorted(MAP_DIR.glob("DOCTRINE_RETRIEVAL_MAP_V1_*.json")):
        data = json.loads(path.read_text(encoding="utf-8"))
        if not isinstance(data, list):
            raise SystemExit(f"map shard is not a list: {path}")
        rows.extend(data)
    ids = [r["id"] for r in rows]
    if len(ids) != len(set(ids)):
        raise SystemExit("duplicate semantic ids across retrieval map shards")
    return rows


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument(
        "--out",
        type=Path,
        default=Path("/tmp/formalife-semantic-gold-v2-draft.jsonl"),
    )
    args = ap.parse_args()

    cases = load_cases()
    entries = load_map_entries()
    by_case: dict[str, list[dict]] = defaultdict(list)
    for entry in entries:
        for case_id in entry.get("eval_cases", []):
            by_case[case_id].append(entry)

    out_rows = []
    for case in cases:
        cid = case["id"]
        candidates = sorted(by_case.get(cid, []), key=lambda x: x["id"])
        out_rows.append(
            {
                "case_id": cid,
                "title": case.get("title"),
                "review_status": "DRAFT_NEEDS_MANUAL_REVIEW",
                "candidate_semantic_units_from_map_links": [
                    {
                        "id": e["id"],
                        "kind": e.get("kind"),
                        "canonical": e.get("canonical"),
                        "upstream": e.get("upstream", []),
                        "must_read_with": e.get("must_read_with", []),
                    }
                    for e in candidates
                ],
                "required_semantic_units": [],
                "optional_semantic_units": [],
                "required_expansions": [],
                "required_checks": case.get("required_checks", []),
                "forbidden_shortcuts": case.get("forbidden_shortcuts", []),
                "legacy_required_nodes": case.get("required_nodes", []),
                "legacy_optional_nodes": case.get("optional_nodes", []),
                "review_note": (
                    "Candidates are migration hints only. Do not copy them into required_semantic_units "
                    "without checking required_checks and canonical doctrine."
                ),
            }
        )

    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(
        "".join(json.dumps(r, ensure_ascii=False) + "\n" for r in out_rows),
        encoding="utf-8",
    )
    linked = sum(bool(r["candidate_semantic_units_from_map_links"]) for r in out_rows)
    print(
        f"SEMANTIC GOLD DRAFT: PASS cases={len(out_rows)} cases_with_map_candidates={linked} out={args.out}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
