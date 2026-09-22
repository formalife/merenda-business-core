#!/usr/bin/env python3
"""Validate Doctrine/Retrieval Map shards and semantic supplement.

Checks structure, canonical paths/anchors, cross-file graph references,
provenance classes, and links to routing eval cases. Reports eval coverage
without treating incomplete draft coverage as a failure yet.
"""

from __future__ import annotations

import json
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
MAP_DIR = ROOT / "reviews" / "drafts"
EVAL_DIR = ROOT / "evals" / "routing"
SUPPLEMENT = MAP_DIR / "SEMANTIC_UNIT_SUPPLEMENT_V2.json"

REQUIRED = {
    "id", "label", "status", "canonical", "kind", "canonical_for",
    "use_when", "not_sufficient_for", "upstream", "must_read_with",
    "evidence_required", "provenance", "supersession", "related", "eval_cases",
}

LIST_FIELDS = {
    "canonical_for", "use_when", "not_sufficient_for", "upstream",
    "must_read_with", "evidence_required", "related", "eval_cases",
}

KINDS = {
    "gate", "diagnostic_dimension", "causal_dependency", "decision_rule",
    "process", "metric", "exception", "temporal_caveat", "provenance_caveat",
}
STATUSES = {"current", "historical", "superseded", "conditional", "draft"}
PROVENANCE = {"MERENDA_PRIMARY", "ASSIMILATED", "SYNTHESIS"}
HEADING_RE = re.compile(r"^(#{1,6})\s+(.+?)\s*$")


def map_files() -> list[Path]:
    files = sorted(MAP_DIR.glob("DOCTRINE_RETRIEVAL_MAP_V1_*.json"))
    if SUPPLEMENT.exists():
        files.append(SUPPLEMENT)
    return files


def githubish_anchor(text: str) -> str:
    text = text.strip().lower()
    text = re.sub(r"[`*_~]", "", text)
    text = re.sub(r"[^\w\- àèéìòù]", "", text, flags=re.UNICODE)
    text = re.sub(r"\s+", "-", text)
    return text.strip("-")


def anchors_for(path: Path) -> set[str]:
    anchors = set()
    for line in path.read_text(encoding="utf-8").splitlines():
        m = HEADING_RE.match(line)
        if m:
            anchors.add(githubish_anchor(m.group(2)))
    return anchors


def load_eval_ids() -> set[str]:
    ids = set()
    for path in sorted(EVAL_DIR.glob("cases*.jsonl")):
        for raw in path.read_text(encoding="utf-8").splitlines():
            if not raw.strip():
                continue
            try:
                row = json.loads(raw)
            except json.JSONDecodeError:
                continue
            if isinstance(row, dict) and isinstance(row.get("id"), str):
                ids.add(row["id"])
    return ids


def load_map_rows(errors: list[str]) -> list[dict]:
    files = map_files()
    if not files:
        errors.append(f"No retrieval map files found under {MAP_DIR.relative_to(ROOT)}")
        return []

    rows: list[dict] = []
    for path in files:
        try:
            payload = json.loads(path.read_text(encoding="utf-8"))
        except json.JSONDecodeError as exc:
            errors.append(f"{path.name}: invalid JSON: {exc}")
            continue
        if not isinstance(payload, list) or not payload:
            errors.append(f"{path.name}: must contain a non-empty JSON array")
            continue
        for index, row in enumerate(payload, start=1):
            if isinstance(row, dict):
                tagged = dict(row)
                tagged["__source_file"] = path.name
                rows.append(tagged)
            else:
                errors.append(f"{path.name}:{index}: entry must be an object")
    return rows


def main() -> int:
    errors: list[str] = []
    rows = load_map_rows(errors)
    valid_evals = load_eval_ids()
    ids: set[str] = set()
    covered_evals: set[str] = set()

    for index, row in enumerate(rows, start=1):
        source_file = row.get("__source_file", "<unknown>")
        entry_id = str(row.get("id", f"<{source_file}:{index}>"))
        public_keys = set(row) - {"__source_file"}
        missing = sorted(REQUIRED - public_keys)
        if missing:
            errors.append(f"{entry_id}: missing fields: {', '.join(missing)}")
            continue

        if entry_id in ids:
            errors.append(f"Duplicate id across map files: {entry_id}")
        ids.add(entry_id)

        if row["status"] not in STATUSES:
            errors.append(f"{entry_id}: invalid status {row['status']}")
        if row["kind"] not in KINDS:
            errors.append(f"{entry_id}: invalid kind {row['kind']}")

        for field in LIST_FIELDS:
            if not isinstance(row[field], list):
                errors.append(f"{entry_id}: {field} must be a list")

        canonical = row["canonical"]
        if not isinstance(canonical, dict) or not isinstance(canonical.get("path"), str):
            errors.append(f"{entry_id}: canonical must contain a path string")
        else:
            path = ROOT / canonical["path"]
            if not path.exists():
                errors.append(f"{entry_id}: missing canonical path {canonical['path']}")
            else:
                anchor = canonical.get("anchor")
                if anchor is not None:
                    if not isinstance(anchor, str) or not anchor.strip():
                        errors.append(f"{entry_id}: anchor must be null or non-empty string")
                    elif anchor not in anchors_for(path):
                        errors.append(
                            f"{entry_id}: anchor not found in {canonical['path']}: {anchor}"
                        )

        provenance = row["provenance"]
        if not isinstance(provenance, dict) or provenance.get("class") not in PROVENANCE:
            errors.append(f"{entry_id}: invalid provenance class")

        supersession = row["supersession"]
        if not isinstance(supersession, dict):
            errors.append(f"{entry_id}: supersession must be an object")
        else:
            for field in ("supersedes", "superseded_by"):
                if not isinstance(supersession.get(field), list):
                    errors.append(f"{entry_id}: supersession.{field} must be a list")

        cases = row["eval_cases"] if isinstance(row["eval_cases"], list) else []
        if not cases:
            errors.append(f"{entry_id}: must be exercised by at least one eval case")
        for case_id in cases:
            if case_id not in valid_evals:
                errors.append(f"{entry_id}: unknown eval case {case_id}")
            else:
                covered_evals.add(case_id)

    # Cross-file references are checked only after all IDs are known.
    for row in rows:
        if not isinstance(row, dict) or "id" not in row:
            continue
        entry_id = str(row["id"])
        refs: list[tuple[str, str]] = []
        if isinstance(row.get("upstream"), list):
            refs.extend(("upstream", ref) for ref in row["upstream"] if isinstance(ref, str))
        if isinstance(row.get("related"), list):
            refs.extend(("related", ref) for ref in row["related"] if isinstance(ref, str))
        if isinstance(row.get("must_read_with"), list):
            for item in row["must_read_with"]:
                if not isinstance(item, dict) or not isinstance(item.get("id"), str):
                    errors.append(f"{entry_id}: invalid must_read_with entry")
                    continue
                refs.append(("must_read_with", item["id"]))
                if not isinstance(item.get("when"), str) or not item["when"].strip():
                    errors.append(f"{entry_id}: must_read_with entry needs non-empty when")

        for relation, ref in refs:
            if ref not in ids:
                errors.append(f"{entry_id}: {relation} references unknown map id {ref}")
            if ref == entry_id:
                errors.append(f"{entry_id}: {relation} cannot self-reference")

    if errors:
        print("RETRIEVAL MAP VALIDATION: FAIL")
        for error in errors:
            print(f"- {error}")
        return 1

    total_evals = len(valid_evals)
    coverage = (len(covered_evals) / total_evals * 100.0) if total_evals else 0.0
    missing_evals = sorted(valid_evals - covered_evals)
    files = ", ".join(path.name for path in map_files())
    print(
        f"RETRIEVAL MAP VALIDATION: PASS ({len(rows)} entries across {files}; "
        f"eval coverage {len(covered_evals)}/{total_evals} = {coverage:.1f}%)"
    )
    if missing_evals:
        print("DRAFT MAP COVERAGE GAPS: " + ", ".join(missing_evals))
    return 0


if __name__ == "__main__":
    sys.exit(main())
