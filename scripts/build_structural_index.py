#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
import re
from dataclasses import dataclass, field
from pathlib import Path
from typing import Iterable

HEADING_RE = re.compile(r"^(#{1,6})\s+(.+?)\s*$")
FENCE_RE = re.compile(r"^\s*(```+|~~~+)")


def slug(text: str) -> str:
    text = text.strip().lower()
    text = re.sub(r"[^\w\s\-]", "", text, flags=re.UNICODE)
    text = re.sub(r"\s+", "-", text)
    return re.sub(r"-+", "-", text).strip("-")


def stable_doc_id(path: str) -> str:
    digest = hashlib.sha1(path.encode("utf-8")).hexdigest()[:10]
    return f"DOC.{digest}"


@dataclass
class Heading:
    title: str
    level: int
    anchor: str
    occurrence: int
    line_start: int
    line_end_direct: int = 0
    line_end_subtree: int = 0
    parent_index: int | None = None
    children_indices: list[int] = field(default_factory=list)
    heading_path: list[str] = field(default_factory=list)


def parse_headings(lines: list[str]) -> list[Heading]:
    headings: list[Heading] = []
    occurrence_counts: dict[str, int] = {}
    stack: list[int] = []
    fence_marker: str | None = None

    for i, line in enumerate(lines, start=1):
        fm = FENCE_RE.match(line)
        if fm:
            marker = fm.group(1)[0]
            if fence_marker is None:
                fence_marker = marker
            elif marker == fence_marker:
                fence_marker = None
            continue
        if fence_marker is not None:
            continue

        m = HEADING_RE.match(line)
        if not m:
            continue
        level = len(m.group(1))
        title = m.group(2).strip()
        anchor = slug(title)
        occurrence_counts[anchor] = occurrence_counts.get(anchor, 0) + 1
        occurrence = occurrence_counts[anchor]

        while stack and headings[stack[-1]].level >= level:
            stack.pop()
        parent_index = stack[-1] if stack else None
        heading_path = [headings[idx].title for idx in stack] + [title]
        h = Heading(
            title=title,
            level=level,
            anchor=anchor,
            occurrence=occurrence,
            line_start=i,
            parent_index=parent_index,
            heading_path=heading_path,
        )
        headings.append(h)
        idx = len(headings) - 1
        if parent_index is not None:
            headings[parent_index].children_indices.append(idx)
        stack.append(idx)

    total_lines = len(lines)
    for idx, h in enumerate(headings):
        next_heading_line = headings[idx + 1].line_start if idx + 1 < len(headings) else total_lines + 1
        h.line_end_direct = max(h.line_start, next_heading_line - 1)

        subtree_end = total_lines
        for nxt in headings[idx + 1 :]:
            if nxt.level <= h.level:
                subtree_end = nxt.line_start - 1
                break
        h.line_end_subtree = max(h.line_start, subtree_end)

    return headings


def slice_text(lines: list[str], start: int, end: int) -> str:
    if not lines or start <= 0 or end < start:
        return ""
    return "\n".join(lines[start - 1 : end])


def structural_id(path: str, h: Heading) -> str:
    suffix = f"@{h.occurrence}" if h.occurrence > 1 else ""
    return f"SEC:{path}#{h.anchor}{suffix}"


def iter_markdown(root: Path) -> Iterable[Path]:
    yield from sorted(p for p in root.rglob("*.md") if p.is_file())


def validate_index(index: dict) -> None:
    ids: set[str] = set()
    sections_by_id: dict[str, dict] = {}
    counted = 0

    for doc in index["documents"]:
        if not doc["path"].startswith("merenda/"):
            raise ValueError(f"unexpected document path: {doc['path']}")
        for section in doc["sections"]:
            sid = section["structural_id"]
            if sid in ids:
                raise ValueError(f"duplicate structural_id: {sid}")
            ids.add(sid)
            sections_by_id[sid] = section
            counted += 1
            if section["line_start"] > section["line_end_direct"]:
                raise ValueError(f"invalid direct range: {sid}")
            if section["line_end_direct"] > section["line_end_subtree"]:
                raise ValueError(f"direct range exceeds subtree: {sid}")
            if len(section["heading_path"]) < 1:
                raise ValueError(f"empty heading path: {sid}")

    if counted != index["section_count"]:
        raise ValueError("section_count mismatch")

    for sid, section in sections_by_id.items():
        parent = section["parent_structural_id"]
        if parent is not None:
            if parent not in sections_by_id:
                raise ValueError(f"missing parent for {sid}: {parent}")
            if sid not in sections_by_id[parent]["children_structural_ids"]:
                raise ValueError(f"parent/child mismatch: {sid} -> {parent}")
            p = sections_by_id[parent]
            if not (p["line_start"] <= section["line_start"] <= section["line_end_subtree"] <= p["line_end_subtree"]):
                raise ValueError(f"child range outside parent subtree: {sid}")
        for child in section["children_structural_ids"]:
            if child not in sections_by_id:
                raise ValueError(f"missing child for {sid}: {child}")
            if sections_by_id[child]["parent_structural_id"] != sid:
                raise ValueError(f"child/parent mismatch: {sid} -> {child}")


def build(repo: Path) -> dict:
    merenda = repo / "merenda"
    if not merenda.is_dir():
        raise SystemExit(f"missing merenda directory: {merenda}")

    documents = []
    total_sections = 0
    for path in iter_markdown(merenda):
        rel = path.relative_to(repo).as_posix()
        raw = path.read_text(encoding="utf-8")
        lines = raw.splitlines()
        headings = parse_headings(lines)
        ids = [structural_id(rel, h) for h in headings]

        sections = []
        for idx, h in enumerate(headings):
            direct_text = slice_text(lines, h.line_start, h.line_end_direct)
            subtree_text = slice_text(lines, h.line_start, h.line_end_subtree)
            sections.append(
                {
                    "structural_id": ids[idx],
                    "path": rel,
                    "anchor": h.anchor,
                    "anchor_occurrence": h.occurrence,
                    "heading": h.title,
                    "level": h.level,
                    "heading_path": h.heading_path,
                    "parent_structural_id": ids[h.parent_index] if h.parent_index is not None else None,
                    "children_structural_ids": [ids[x] for x in h.children_indices],
                    "line_start": h.line_start,
                    "line_end_direct": h.line_end_direct,
                    "line_end_subtree": h.line_end_subtree,
                    "direct_chars": len(direct_text),
                    "subtree_chars": len(subtree_text),
                    "direct_words": len(direct_text.split()),
                    "subtree_words": len(subtree_text.split()),
                }
            )
        total_sections += len(sections)
        documents.append(
            {
                "document_id": stable_doc_id(rel),
                "path": rel,
                "kind": "routing" if path.name in {"DECISION_ROUTER.md", "INDEX.md"} or path.name == "README.md" else "canonical_or_supporting",
                "bytes": len(raw.encode("utf-8")),
                "chars": len(raw),
                "lines": len(lines),
                "words": len(raw.split()),
                "root_structural_ids": [ids[i] for i, h in enumerate(headings) if h.parent_index is None],
                "sections": sections,
            }
        )

    index = {
        "schema_version": "1.1",
        "source_root": "merenda/",
        "generation": "deterministic-markdown-structure-only",
        "document_count": len(documents),
        "section_count": total_sections,
        "documents": documents,
    }
    validate_index(index)
    return index


def render_md(index: dict) -> str:
    docs = index["documents"]
    total_bytes = sum(d["bytes"] for d in docs)
    total_words = sum(d["words"] for d in docs)
    largest = sorted(docs, key=lambda d: d["bytes"], reverse=True)[:15]
    deepest = sorted(
        (
            (s["level"], d["path"], s["structural_id"], " / ".join(s["heading_path"]))
            for d in docs
            for s in d["sections"]
        ),
        reverse=True,
    )[:15]

    out = [
        "# Structural Index — Mechanical Summary",
        "",
        "Generated deterministically from Markdown structure. Fenced-code headings are ignored. No doctrine interpretation is included.",
        "",
        f"- Schema: **{index['schema_version']}**",
        f"- Documents: **{len(docs)}**",
        f"- Structural sections: **{index['section_count']}**",
        f"- Total bytes: **{total_bytes}**",
        f"- Total words: **{total_words}**",
        "",
        "## Largest documents",
        "",
        "| Path | Bytes | Sections | Words |",
        "|---|---:|---:|---:|",
    ]
    for d in largest:
        out.append(f"| `{d['path']}` | {d['bytes']} | {len(d['sections'])} | {d['words']} |")

    out += ["", "## Deepest heading paths", "", "| Level | Path | Structural ID | Heading path |", "|---:|---|---|---|"]
    for level, path, sid, hpath in deepest:
        out.append(f"| {level} | `{path}` | `{sid}` | {hpath.replace('|', '\\|')} |")

    out += [
        "",
        "## Runtime intent",
        "",
        "This index is a generated structural layer only. It can support section discovery, parent/child expansion and context accounting. It must not be used as a substitute for curated decision-routing metadata or canonical doctrine.",
        "",
    ]
    return "\n".join(out)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--repo", type=Path, default=Path.cwd())
    ap.add_argument("--json-out", type=Path)
    ap.add_argument("--md-out", type=Path)
    args = ap.parse_args()

    repo = args.repo.resolve()
    index = build(repo)

    if args.json_out:
        args.json_out.parent.mkdir(parents=True, exist_ok=True)
        args.json_out.write_text(json.dumps(index, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    if args.md_out:
        args.md_out.parent.mkdir(parents=True, exist_ok=True)
        args.md_out.write_text(render_md(index), encoding="utf-8")
    if not args.json_out and not args.md_out:
        print(json.dumps(index, ensure_ascii=False, indent=2))
    else:
        print(f"STRUCTURAL INDEX: PASS documents={index['document_count']} sections={index['section_count']} schema={index['schema_version']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
