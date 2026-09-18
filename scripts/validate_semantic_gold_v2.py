#!/usr/bin/env python3
from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EVAL_DIR = ROOT / "evals" / "routing"
MAP_DIR = ROOT / "reviews" / "drafts"
SUPPLEMENT = MAP_DIR / "SEMANTIC_UNIT_SUPPLEMENT_V2.json"
GOLD = EVAL_DIR / "semantic_gold_v2.jsonl"
HEADING_RE = re.compile(r"^(#{1,6})\s+(.+?)\s*$")
PROVENANCE = {"MERENDA_PRIMARY", "ASSIMILATED", "SYNTHESIS"}


def slug(text: str) -> str:
    text = text.strip().lower()
    text = re.sub(r"[^\w\s\-]", "", text, flags=re.UNICODE)
    text = re.sub(r"\s+", "-", text)
    return re.sub(r"-+", "-", text).strip("-")


def headings(path: Path) -> set[str]:
    found: set[str] = set()
    fenced = False
    for line in path.read_text(encoding="utf-8").splitlines():
        if line.lstrip().startswith("```"):
            fenced = not fenced
            continue
        if fenced:
            continue
        m = HEADING_RE.match(line)
        if m:
            found.add(slug(m.group(2)))
    return found


def load_cases() -> dict[str, dict]:
    out: dict[str, dict] = {}
    for path in sorted(EVAL_DIR.glob("cases*.jsonl")):
        for raw in path.read_text(encoding="utf-8").splitlines():
            if not raw.strip():
                continue
            row = json.loads(raw)
            cid = row["id"]
            if cid in out:
                raise ValueError(f"duplicate case id: {cid}")
            out[cid] = row
    return out


def load_registry() -> dict[str, dict]:
    entries: dict[str, dict] = {}
    paths = sorted(MAP_DIR.glob("DOCTRINE_RETRIEVAL_MAP_V1_*.json")) + [SUPPLEMENT]
    for path in paths:
        data = json.loads(path.read_text(encoding="utf-8"))
        if not isinstance(data, list):
            raise ValueError(f"registry file must contain a list: {path}")
        for row in data:
            sid = row.get("id")
            if not isinstance(sid, str) or not sid:
                raise ValueError(f"semantic unit without id in {path}")
            if sid in entries:
                raise ValueError(f"duplicate semantic id: {sid}")
            entries[sid] = row
    return entries


def load_gold() -> dict[str, dict]:
    out: dict[str, dict] = {}
    for lineno, raw in enumerate(GOLD.read_text(encoding="utf-8").splitlines(), start=1):
        if not raw.strip():
            continue
        row = json.loads(raw)
        cid = row.get("case_id")
        if not isinstance(cid, str) or not cid:
            raise ValueError(f"{GOLD}:{lineno}: missing case_id")
        if cid in out:
            raise ValueError(f"duplicate semantic gold case: {cid}")
        out[cid] = row
    return out


def main() -> int:
    errors: list[str] = []
    try:
        cases = load_cases()
        registry = load_registry()
        gold = load_gold()
    except (ValueError, json.JSONDecodeError) as exc:
        raise SystemExit(str(exc))

    if set(gold) != set(cases):
        for cid in sorted(set(cases) - set(gold)):
            errors.append(f"missing semantic gold case: {cid}")
        for cid in sorted(set(gold) - set(cases)):
            errors.append(f"semantic gold references unknown case: {cid}")

    referenced: set[str] = set()
    for cid, row in sorted(gold.items()):
        if row.get("review_status") != "MANUALLY_REVIEWED":
            errors.append(f"{cid}: review_status must be MANUALLY_REVIEWED")
        required = row.get("required_semantic_units")
        optional = row.get("optional_semantic_units")
        expansions = row.get("required_expansions")
        if not isinstance(required, list) or not required or not all(isinstance(x, str) for x in required):
            errors.append(f"{cid}: required_semantic_units must be non-empty list[str]")
            continue
        if not isinstance(optional, list) or not all(isinstance(x, str) for x in optional):
            errors.append(f"{cid}: optional_semantic_units must be list[str]")
            continue
        if len(required) != len(set(required)) or len(optional) != len(set(optional)):
            errors.append(f"{cid}: duplicate semantic ids inside gold record")
        overlap = set(required) & set(optional)
        if overlap:
            errors.append(f"{cid}: required/optional overlap: {sorted(overlap)}")
        for sid in required + optional:
            referenced.add(sid)
            if sid not in registry:
                errors.append(f"{cid}: unknown semantic id: {sid}")
        if not isinstance(expansions, list):
            errors.append(f"{cid}: required_expansions must be a list")
        else:
            for expansion in expansions:
                if not isinstance(expansion, dict):
                    errors.append(f"{cid}: expansion must be object")
                    continue
                sid = expansion.get("semantic_id")
                if sid not in required:
                    errors.append(f"{cid}: expansion semantic_id must be required: {sid}")

    for sid, entry in sorted(registry.items()):
        canonical = entry.get("canonical")
        if not isinstance(canonical, dict):
            errors.append(f"{sid}: canonical missing")
            continue
        rel = canonical.get("path")
        anchor = canonical.get("anchor")
        if not isinstance(rel, str) or not rel:
            errors.append(f"{sid}: canonical.path missing")
            continue
        path = ROOT / rel
        if not path.is_file():
            errors.append(f"{sid}: canonical path not found: {rel}")
        elif anchor is not None:
            if not isinstance(anchor, str) or not anchor:
                errors.append(f"{sid}: canonical.anchor must be string or null")
            elif anchor not in headings(path):
                errors.append(f"{sid}: canonical anchor not found: {rel}#{anchor}")
        provenance = entry.get("provenance")
        if not isinstance(provenance, dict) or provenance.get("class") not in PROVENANCE:
            errors.append(f"{sid}: invalid provenance")
        for field in ("upstream", "related"):
            refs = entry.get(field, [])
            if not isinstance(refs, list) or not all(isinstance(x, str) for x in refs):
                errors.append(f"{sid}: {field} must be list[str]")
                continue
            for ref in refs:
                if ref not in registry:
                    errors.append(f"{sid}: broken {field} ref: {ref}")
        companions = entry.get("must_read_with", [])
        if not isinstance(companions, list):
            errors.append(f"{sid}: must_read_with must be a list")
        else:
            for item in companions:
                if not isinstance(item, dict) or item.get("id") not in registry:
                    errors.append(f"{sid}: broken must_read_with ref: {item}")

    if errors:
        print("SEMANTIC GOLD V2: FAIL")
        for error in errors:
            print(f"- {error}")
        return 1

    print(
        "SEMANTIC GOLD V2: PASS "
        f"cases={len(gold)} registry_units={len(registry)} referenced_units={len(referenced)}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
