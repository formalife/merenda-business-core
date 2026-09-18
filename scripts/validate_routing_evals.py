#!/usr/bin/env python3
"""Validate the routing/retrieval eval suite without external dependencies."""

from __future__ import annotations

import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
CASES = ROOT / "evals" / "routing" / "cases.jsonl"

REQUIRED_FIELDS = {
    "id",
    "title",
    "prompt",
    "case_type",
    "required_nodes",
    "optional_nodes",
    "required_checks",
    "forbidden_shortcuts",
    "expected_behavior",
    "provenance_checks",
    "notes",
}

LIST_FIELDS = {
    "required_nodes",
    "optional_nodes",
    "required_checks",
    "forbidden_shortcuts",
    "provenance_checks",
}


def validate() -> list[str]:
    errors: list[str] = []

    if not CASES.exists():
        return [f"Missing eval file: {CASES.relative_to(ROOT)}"]

    seen_ids: set[str] = set()
    rows = []

    for lineno, raw in enumerate(CASES.read_text(encoding="utf-8").splitlines(), start=1):
        if not raw.strip():
            continue
        try:
            row = json.loads(raw)
        except json.JSONDecodeError as exc:
            errors.append(f"Line {lineno}: invalid JSON: {exc}")
            continue

        if not isinstance(row, dict):
            errors.append(f"Line {lineno}: record must be a JSON object")
            continue

        rows.append(row)
        case_id = str(row.get("id", f"<line-{lineno}>"))

        missing = sorted(REQUIRED_FIELDS - set(row))
        if missing:
            errors.append(f"{case_id}: missing fields: {', '.join(missing)}")
            continue

        if case_id in seen_ids:
            errors.append(f"Duplicate case id: {case_id}")
        seen_ids.add(case_id)

        if not case_id.startswith("R") or not case_id[1:].isdigit():
            errors.append(f"{case_id}: id must match R<number>")

        for field in LIST_FIELDS:
            value = row[field]
            if not isinstance(value, list):
                errors.append(f"{case_id}: {field} must be a list")

        if not isinstance(row["expected_behavior"], str) or not row["expected_behavior"].strip():
            errors.append(f"{case_id}: expected_behavior must be non-empty text")

        for field in ("required_nodes", "optional_nodes"):
            value = row[field]
            if not isinstance(value, list):
                continue
            for path_str in value:
                if not isinstance(path_str, str) or not path_str.strip():
                    errors.append(f"{case_id}: invalid path in {field}")
                    continue
                path = ROOT / path_str
                if not path.exists():
                    errors.append(f"{case_id}: missing repository path: {path_str}")

        if not row["required_nodes"]:
            errors.append(f"{case_id}: at least one required_node is required")
        if not row["required_checks"]:
            errors.append(f"{case_id}: at least one required_check is required")
        if not row["forbidden_shortcuts"]:
            errors.append(f"{case_id}: at least one forbidden_shortcut is required")

    if not rows:
        errors.append("No eval cases found")

    return errors


def main() -> int:
    errors = validate()
    if errors:
        print("ROUTING EVAL VALIDATION: FAIL")
        for error in errors:
            print(f"- {error}")
        return 1

    count = sum(1 for line in CASES.read_text(encoding="utf-8").splitlines() if line.strip())
    print(f"ROUTING EVAL VALIDATION: PASS ({count} cases)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
