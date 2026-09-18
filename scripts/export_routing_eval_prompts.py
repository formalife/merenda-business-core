#!/usr/bin/env python3
"""Export prompt-only routing eval records for uncontaminated behavioral runs.

Gold routing fields stay in evals/routing/cases*.jsonl and must not be exposed
to the model under test.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EVAL_DIR = ROOT / "evals" / "routing"


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--out", type=Path, required=True)
    args = parser.parse_args()

    rows = []
    seen = set()
    for path in sorted(EVAL_DIR.glob("cases*.jsonl")):
        for lineno, raw in enumerate(path.read_text(encoding="utf-8").splitlines(), start=1):
            if not raw.strip():
                continue
            row = json.loads(raw)
            case_id = row["id"]
            if case_id in seen:
                raise ValueError(f"duplicate case id: {case_id}")
            seen.add(case_id)
            rows.append({
                "case_id": case_id,
                "title": row["title"],
                "case_type": row["case_type"],
                "prompt": row["prompt"],
            })

    args.out.parent.mkdir(parents=True, exist_ok=True)
    with args.out.open("w", encoding="utf-8") as handle:
        for row in rows:
            handle.write(json.dumps(row, ensure_ascii=False) + "\n")

    print(f"EXPORTED {len(rows)} sanitized routing prompts to {args.out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
