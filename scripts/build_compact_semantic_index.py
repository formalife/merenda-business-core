#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MAP_DIR = ROOT / "reviews" / "drafts"
SUPPLEMENT = MAP_DIR / "SEMANTIC_UNIT_SUPPLEMENT_V2.json"

RUNTIME_FIELDS = (
    "id",
    "label",
    "status",
    "canonical",
    "kind",
    "canonical_for",
    "use_when",
    "not_sufficient_for",
    "upstream",
    "must_read_with",
    "evidence_required",
    "provenance",
    "supersession",
    "related",
)


def load_registry() -> list[dict]:
    rows: list[dict] = []
    paths = sorted(MAP_DIR.glob("DOCTRINE_RETRIEVAL_MAP_V1_*.json")) + [SUPPLEMENT]
    for path in paths:
        data = json.loads(path.read_text(encoding="utf-8"))
        if not isinstance(data, list):
            raise SystemExit(f"registry file must contain a list: {path}")
        rows.extend(data)
    ids = [r["id"] for r in rows]
    if len(ids) != len(set(ids)):
        raise SystemExit("duplicate semantic ids in combined registry")
    return sorted(rows, key=lambda x: x["id"])


def runtime_entry(entry: dict) -> dict:
    # eval_cases is intentionally excluded: runtime retrieval must never see gold linkage.
    return {field: entry.get(field) for field in RUNTIME_FIELDS if field in entry}


def compact_line(entry: dict) -> str:
    canonical_for = ",".join(entry.get("canonical_for", [])) or "-"
    upstream = ",".join(entry.get("upstream", [])) or "-"
    return "\t".join(
        [
            entry["id"],
            entry.get("kind", "-"),
            entry.get("label", "-"),
            canonical_for,
            upstream,
        ]
    )


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--json-out", type=Path, default=Path("/tmp/formalife-semantic-index-v2.json"))
    ap.add_argument("--txt-out", type=Path, default=Path("/tmp/formalife-semantic-index-v2.txt"))
    args = ap.parse_args()

    registry = load_registry()
    lines = [
        "id\tkind\tlabel\tcanonical_for\tupstream",
        *[compact_line(entry) for entry in registry],
    ]
    compact_text = "\n".join(lines) + "\n"
    entries = {entry["id"]: runtime_entry(entry) for entry in registry}
    output = {
        "schema_version": "2.0",
        "runtime_rule": "compact index may be preloaded; full entries are addressable and fetched selectively",
        "gold_linkage_exposed": False,
        "compact_index_text": compact_text,
        "entries": entries,
    }

    args.json_out.parent.mkdir(parents=True, exist_ok=True)
    args.txt_out.parent.mkdir(parents=True, exist_ok=True)
    args.json_out.write_text(json.dumps(output, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    args.txt_out.write_text(compact_text, encoding="utf-8")

    source_chars = sum(
        len(json.dumps(entry, ensure_ascii=False, separators=(",", ":"))) for entry in registry
    )
    compact_chars = len(compact_text)
    ratio = compact_chars / source_chars if source_chars else 0.0
    print(
        "COMPACT SEMANTIC INDEX: PASS "
        f"units={len(registry)} source_chars={source_chars} compact_chars={compact_chars} "
        f"compact_ratio={ratio:.3f} json={args.json_out} txt={args.txt_out}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
