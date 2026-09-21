#!/usr/bin/env python3
"""Validate the routing/retrieval eval suite without external dependencies."""

from __future__ import annotations

import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
EVAL_DIR = ROOT / "evals" / "routing"

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


def case_files() -> list[Path]:
    return sorted(EVAL_DIR.glob("cases*.jsonl"))


def validate() -> tuple[list[str], int]:
    errors: list[str] = []
    files = case_files()

    if not files:
        return [f"No eval files found under {EVAL_DIR.relative_to(ROOT)}"], 0

    seen_ids: set[str] = set()
    total_rows = 0

    for cases in files:
        file_rows = 0
        for lineno, raw in enumerate(cases.read_text(encoding="utf-8").splitlines(), start=1):
            if not raw.strip():
                continue
            try:
                row = json.loads(raw)
            except json.JSONDecodeError as exc:
                errors.append(f"{cases.name}:{lineno}: invalid JSON: {exc}")
                continue

            if not isinstance(row, dict):
                errors.append(f"{cases.name}:{lineno}: record must be a JSON object")
                continue

            file_rows += 1
            total_rows += 1
            case_id = str(row.get("id", f"<{cases.name}:{lineno}>"))

            missing = sorted(REQUIRED_FIELDS - set(row))
            if missing:
                errors.append(f"{case_id}: missing fields: {', '.join(missing)}")
                continue

            if case_id in seen_ids:
                errors.append(f"Duplicate case id across eval files: {case_id}")
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

        if file_rows == 0:
            errors.append(f"{cases.name}: contains no eval cases")

    return errors, total_rows


def main() -> int:
    errors, count = validate()
    if errors:
        print("ROUTING EVAL VALIDATION: FAIL")
        for error in errors:
            print(f"- {error}")
        return 1

    files = ", ".join(path.name for path in case_files())
    print(f"ROUTING EVAL VALIDATION: PASS ({count} cases across {files})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
