#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from pathlib import Path

SMOKE_CASES = {"R002", "R008", "R019", "R020", "R027", "R030"}


def load_jsonl(path: Path) -> list[dict]:
    if not path.is_file():
        raise SystemExit(f"missing file: {path}")
    rows: list[dict] = []
    for lineno, raw in enumerate(path.read_text(encoding="utf-8").splitlines(), start=1):
        if not raw.strip():
            continue
        try:
            row = json.loads(raw)
        except json.JSONDecodeError as exc:
            raise SystemExit(f"{path}:{lineno}: invalid JSON") from exc
        if not isinstance(row, dict):
            raise SystemExit(f"{path}:{lineno}: expected JSON object")
        rows.append(row)
    return rows


def write_jsonl(path: Path, rows: list[dict]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        "".join(json.dumps(row, ensure_ascii=False) + "\n" for row in rows),
        encoding="utf-8",
    )


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument(
        "--workdir",
        type=Path,
        default=Path("/tmp/formalife-hierarchical-prototype-a"),
    )
    ap.add_argument(
        "--answer-out",
        type=Path,
        default=Path("/tmp/formalife-prototype-a-answer-judgment-bundle.jsonl"),
    )
    ap.add_argument(
        "--debug-out",
        type=Path,
        default=Path("/tmp/formalife-prototype-a-retrieval-debug-bundle.jsonl"),
    )
    ap.add_argument(
        "--case",
        action="append",
        dest="cases",
        help="Expected case ID. Repeat for a focused non-smoke run. Omit for the canonical six-case smoke bundle.",
    )
    args = ap.parse_args()

    trace_path = args.workdir / "prototype-a-trace.jsonl"
    prompt_path = args.workdir / "routing-prompts.jsonl"
    metadata_path = args.workdir / "metadata.json"

    traces = load_jsonl(trace_path)
    prompts = load_jsonl(prompt_path)
    if not metadata_path.is_file():
        raise SystemExit(f"missing file: {metadata_path}")
    metadata = json.loads(metadata_path.read_text(encoding="utf-8"))

    expected_cases = set(args.cases) if args.cases else set(SMOKE_CASES)
    if not expected_cases:
        raise SystemExit("expected case set cannot be empty")
    if not args.cases and metadata.get("smoke") is not True:
        raise SystemExit("workdir metadata does not identify the canonical smoke run")
    if metadata.get("gold_exposure") is None:
        raise SystemExit("workdir metadata missing gold_exposure")

    metadata_cases = metadata.get("cases")
    if not isinstance(metadata_cases, list) or set(metadata_cases) != expected_cases:
        raise SystemExit(
            f"metadata case mismatch: got={sorted(metadata_cases or [])} expected={sorted(expected_cases)}"
        )

    prompt_by_id = {row.get("case_id"): row for row in prompts}
    trace_by_id = {row.get("case_id"): row for row in traces}
    if set(trace_by_id) != expected_cases:
        raise SystemExit(
            f"unexpected trace cases: got={sorted(trace_by_id)} expected={sorted(expected_cases)}"
        )

    expected_arch = metadata.get("architecture")
    if not isinstance(expected_arch, str):
        raise SystemExit("workdir metadata missing architecture")

    answer_rows: list[dict] = []
    debug_rows: list[dict] = []
    for cid in sorted(expected_cases):
        trace = trace_by_id[cid]
        prompt = prompt_by_id.get(cid)
        if not prompt:
            raise SystemExit(f"missing sanitized prompt for {cid}")
        if trace.get("architecture") != expected_arch:
            raise SystemExit(
                f"{cid}: unexpected architecture {trace.get('architecture')!r}; expected {expected_arch!r}"
            )

        # Answer-only bundle deliberately excludes semantic IDs, retrieval paths,
        # context stats, scores, gold and trace notes. Judge this first.
        answer_rows.append(
            {
                "case_id": cid,
                "title": prompt.get("title"),
                "case_type": prompt.get("case_type"),
                "prompt": prompt.get("prompt"),
                "classification": trace.get("classification", []),
                "decision_level": trace.get("decision_level"),
                "answer": trace.get("answer"),
            }
        )

        # Keep retrieval/debug material separate until answer judgment is frozen.
        debug_rows.append(
            {
                "case_id": cid,
                "architecture": trace.get("architecture"),
                "retrieved_nodes": trace.get("retrieved_nodes", []),
                "retrieved_sections": trace.get("retrieved_sections", []),
                "selected_semantic_units": trace.get("selected_semantic_units", []),
                "verified_semantic_units": trace.get("verified_semantic_units", []),
                "retrieval_stats": trace.get("retrieval_stats", {}),
                "context_stats": trace.get("context_stats", {}),
                "trace_notes": trace.get("trace_notes", ""),
            }
        )

    write_jsonl(args.answer_out, answer_rows)
    write_jsonl(args.debug_out, debug_rows)

    print("PROTOTYPE JUDGMENT BUNDLE: PASS")
    print("tested_commit:", metadata.get("commit_sha"))
    print("architecture:", expected_arch)
    print("cases:", len(answer_rows), ",".join(sorted(expected_cases)))
    print("answer_bundle:", args.answer_out)
    print("debug_bundle:", args.debug_out)
    print("UPLOAD ONLY THE ANSWER BUNDLE UNTIL JUDGMENT IS FROZEN")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
