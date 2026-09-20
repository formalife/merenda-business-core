#!/usr/bin/env python3
from __future__ import annotations

import argparse
import copy
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MAP_DIR = ROOT / "reviews" / "drafts"
SUPPLEMENT = MAP_DIR / "SEMANTIC_UNIT_SUPPLEMENT_V2.json"
RUNTIME_PATCH = MAP_DIR / "SEMANTIC_RUNTIME_PATCH_V3.json"

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


def append_unique(items: list, additions: list) -> list:
    out = list(items)
    for addition in additions:
        if addition not in out:
            out.append(addition)
    return out


def apply_runtime_patches(registry: list[dict]) -> tuple[list[dict], int]:
    patched = [copy.deepcopy(row) for row in registry]
    by_id = {row["id"]: row for row in patched}
    if not RUNTIME_PATCH.exists():
        return patched, 0

    patch_rows = json.loads(RUNTIME_PATCH.read_text(encoding="utf-8"))
    if not isinstance(patch_rows, list):
        raise SystemExit(f"runtime patch must contain a list: {RUNTIME_PATCH}")

    applied = 0
    for patch in patch_rows:
        if not isinstance(patch, dict) or not isinstance(patch.get("id"), str):
            raise SystemExit("runtime patch entries require string id")
        sid = patch["id"]
        if sid not in by_id:
            raise SystemExit(f"runtime patch references unknown semantic id: {sid}")
        row = by_id[sid]
        for field in ("must_read_with", "related"):
            additions = patch.get(f"{field}_add", [])
            if not isinstance(additions, list):
                raise SystemExit(f"{sid}: {field}_add must be a list")
            if field == "must_read_with":
                for item in additions:
                    if not isinstance(item, dict) or not isinstance(item.get("id"), str):
                        raise SystemExit(f"{sid}: invalid must_read_with patch item")
                    if item["id"] not in by_id:
                        raise SystemExit(f"{sid}: must_read_with references unknown id {item['id']}")
            else:
                for item in additions:
                    if not isinstance(item, str) or item not in by_id:
                        raise SystemExit(f"{sid}: related patch references unknown id {item!r}")
            row[field] = append_unique(row.get(field, []), additions)
        applied += 1
    return sorted(patched, key=lambda x: x["id"]), applied


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

    source_registry = load_registry()
    registry, applied_patches = apply_runtime_patches(source_registry)
    lines = [
        "id\tkind\tlabel\tcanonical_for\tupstream",
        *[compact_line(entry) for entry in registry],
    ]
    compact_text = "\n".join(lines) + "\n"
    entries = {entry["id"]: runtime_entry(entry) for entry in registry}
    output = {
        "schema_version": "2.1",
        "runtime_rule": "compact index may be preloaded; full entries are addressable and fetched selectively",
        "gold_linkage_exposed": False,
        "runtime_patch_applied": RUNTIME_PATCH.name if applied_patches else None,
        "runtime_patch_count": applied_patches,
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
        f"units={len(registry)} patches={applied_patches} source_chars={source_chars} "
        f"compact_chars={compact_chars} compact_ratio={ratio:.3f} "
        f"json={args.json_out} txt={args.txt_out}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
