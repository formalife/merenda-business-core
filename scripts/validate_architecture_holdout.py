#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
HOLDOUT = ROOT / "evals" / "routing" / "holdout_v1.jsonl"
STANDARD = [
    ROOT / "evals" / "routing" / "cases.jsonl",
    ROOT / "evals" / "routing" / "cases_phase2.jsonl",
    ROOT / "evals" / "routing" / "cases_phase3.jsonl",
]
REQUIRED = {
    "id",
    "title",
    "prompt",
    "case_type",
    "required_nodes",
    "required_checks",
    "forbidden_shortcuts",
    "expected_behavior",
    "provenance_checks",
    "notes",
}


def load(path: Path) -> list[dict]:
    rows: list[dict] = []
    for lineno, raw in enumerate(path.read_text(encoding="utf-8").splitlines(), start=1):
        if not raw.strip():
            continue
        try:
            row = json.loads(raw)
        except json.JSONDecodeError as exc:
            raise SystemExit(f"{path}:{lineno}: invalid JSON") from exc
        if not isinstance(row, dict):
            raise SystemExit(f"{path}:{lineno}: expected object")
        rows.append(row)
    return rows


def main() -> int:
    rows = load(HOLDOUT)
    if len(rows) != 6:
        raise SystemExit(f"holdout_v1 must contain exactly 6 cases; got {len(rows)}")

    standard_ids: set[str] = set()
    for path in STANDARD:
        for row in load(path):
            cid = row.get("id")
            if isinstance(cid, str):
                standard_ids.add(cid)

    seen: set[str] = set()
    errors: list[str] = []
    for row in rows:
        cid = row.get("id")
        missing = REQUIRED - row.keys()
        if missing:
            errors.append(f"{cid}: missing fields {sorted(missing)}")
            continue
        if not isinstance(cid, str) or not cid.startswith("H"):
            errors.append(f"invalid holdout id {cid!r}")
            continue
        if cid in seen:
            errors.append(f"duplicate id {cid}")
        seen.add(cid)
        if cid in standard_ids:
            errors.append(f"{cid}: overlaps development suite")
        if not isinstance(row["prompt"], str) or not row["prompt"].strip():
            errors.append(f"{cid}: empty prompt")
        for field in ("required_nodes", "required_checks", "forbidden_shortcuts", "provenance_checks"):
            value = row[field]
            if not isinstance(value, list) or not all(isinstance(x, str) and x.strip() for x in value):
                errors.append(f"{cid}: {field} must be non-empty strings list (provenance may be empty)")
        if not row["required_checks"]:
            errors.append(f"{cid}: requires at least one required check")
        for rel in row["required_nodes"]:
            path = ROOT / rel
            if not path.is_file():
                errors.append(f"{cid}: missing required node {rel}")

    if errors:
        print("ARCHITECTURE HOLDOUT: FAIL")
        for error in errors:
            print("-", error)
        return 1

    print(
        "ARCHITECTURE HOLDOUT: PASS "
        f"cases={len(rows)} checks={sum(len(r['required_checks']) for r in rows)} "
        f"standard_overlap=0"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
