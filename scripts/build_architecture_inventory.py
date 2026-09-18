#!/usr/bin/env python3
"""Build a mechanical inventory of the canonical Merenda doctrine layer.

The output is descriptive, not doctrinal: it inventories files, headings, links,
size, and routing visibility so semantic review can identify retrieval blind spots.
No external dependencies are required.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
import re
from collections import Counter, defaultdict

ROOT = Path(__file__).resolve().parents[1]
MERENDA = ROOT / "merenda"

CONTROL_FILES = [
    MERENDA / "INDEX.md",
    MERENDA / "DECISION_ROUTER.md",
    MERENDA / "00_fondamenti" / "sistema-operativo-merenda.md",
]

HEADING_RE = re.compile(r"^(#{1,6})\s+(.+?)\s*$")
LINK_RE = re.compile(r"\[[^\]]*\]\(([^)]+)\)")


def normalize_text(value: str) -> str:
    value = value.lower()
    value = re.sub(r"[`*_~]", "", value)
    value = re.sub(r"[^a-z0-9àèéìòù]+", " ", value)
    return re.sub(r"\s+", " ", value).strip()


def githubish_anchor(text: str) -> str:
    text = text.strip().lower()
    text = re.sub(r"[`*_~]", "", text)
    text = re.sub(r"[^\w\- àèéìòù]", "", text, flags=re.UNICODE)
    text = re.sub(r"\s+", "-", text)
    return text.strip("-")


def resolve_local_link(source: Path, raw: str) -> tuple[str | None, str | None]:
    raw = raw.strip()
    if not raw or "://" in raw or raw.startswith("mailto:"):
        return None, None
    if raw.startswith("#"):
        return source.relative_to(ROOT).as_posix(), raw[1:]

    target, _, anchor = raw.partition("#")
    if not target:
        target_path = source
    else:
        target_path = (source.parent / target).resolve()
    try:
        rel = target_path.relative_to(ROOT.resolve()).as_posix()
    except ValueError:
        return None, None
    return rel, anchor or None


def load_control_text() -> dict[str, str]:
    out = {}
    for path in CONTROL_FILES:
        if path.exists():
            out[path.relative_to(ROOT).as_posix()] = normalize_text(path.read_text(encoding="utf-8"))
    return out


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--json-out", type=Path, required=True)
    parser.add_argument("--md-out", type=Path, required=True)
    args = parser.parse_args()

    md_files = sorted(MERENDA.rglob("*.md"))
    rel_files = [p.relative_to(ROOT).as_posix() for p in md_files]
    file_set = set(rel_files)
    control_text = load_control_text()

    incoming: Counter[str] = Counter()
    outgoing: dict[str, list[dict]] = defaultdict(list)
    rows = []

    for path in md_files:
        rel = path.relative_to(ROOT).as_posix()
        text = path.read_text(encoding="utf-8")
        lines = text.splitlines()
        headings = []
        local_links = []

        for line_no, line in enumerate(lines, start=1):
            hm = HEADING_RE.match(line)
            if hm:
                title = hm.group(2).strip()
                headings.append(
                    {
                        "level": len(hm.group(1)),
                        "title": title,
                        "anchor": githubish_anchor(title),
                        "line": line_no,
                    }
                )

            for raw_target in LINK_RE.findall(line):
                target_file, anchor = resolve_local_link(path, raw_target)
                if not target_file:
                    continue
                local_links.append(
                    {
                        "raw": raw_target,
                        "target": target_file,
                        "anchor": anchor,
                        "line": line_no,
                        "target_exists": target_file in file_set or (ROOT / target_file).exists(),
                    }
                )
                if target_file in file_set and target_file != rel:
                    incoming[target_file] += 1
                    outgoing[rel].append({"target": target_file, "anchor": anchor})

        section_readme = path.parent / "README.md"
        section_readme_text = (
            normalize_text(section_readme.read_text(encoding="utf-8"))
            if section_readme.exists()
            else ""
        )
        basename_label = normalize_text(path.stem.replace("-", " "))
        readme_visible = path.name == "README.md" or basename_label in section_readme_text
        router_visible = basename_label in control_text.get("merenda/DECISION_ROUTER.md", "")
        index_visible = basename_label in control_text.get("merenda/INDEX.md", "")
        system_visible = basename_label in control_text.get(
            "merenda/00_fondamenti/sistema-operativo-merenda.md", ""
        )

        hidden_headings = []
        control_union = " ".join(control_text.values()) + " " + section_readme_text
        for heading in headings:
            if heading["level"] == 1:
                continue
            norm = normalize_text(heading["title"])
            # Only flag reasonably specific headings; short generic headings create noise.
            if len(norm) >= 22 and norm not in control_union:
                hidden_headings.append(heading)

        rows.append(
            {
                "path": rel,
                "bytes": path.stat().st_size,
                "lines": len(lines),
                "heading_count": len(headings),
                "headings": headings,
                "local_link_count": len(local_links),
                "local_links": local_links,
                "incoming_links": 0,  # filled after full scan
                "routing_visibility": {
                    "section_readme": readme_visible,
                    "index": index_visible,
                    "decision_router": router_visible,
                    "system_operativo": system_visible,
                },
                "hidden_heading_candidates": hidden_headings,
            }
        )

    by_path = {row["path"]: row for row in rows}
    for path, count in incoming.items():
        by_path[path]["incoming_links"] = count

    canonical_rows = [
        row for row in rows
        if not row["path"].endswith("/README.md")
        and row["path"] not in {"merenda/INDEX.md", "merenda/DECISION_ROUTER.md"}
    ]

    largest = sorted(canonical_rows, key=lambda r: r["bytes"], reverse=True)[:15]
    no_incoming = [r for r in canonical_rows if r["incoming_links"] == 0]
    low_visibility = [
        r for r in canonical_rows
        if not any(r["routing_visibility"].values())
    ]
    hidden = sorted(
        (
            {"path": r["path"], **h}
            for r in canonical_rows
            for h in r["hidden_heading_candidates"]
        ),
        key=lambda x: (x["path"], x["line"]),
    )

    broken_links = [
        {"source": r["path"], **link}
        for r in rows
        for link in r["local_links"]
        if not link["target_exists"]
    ]

    inventory = {
        "generated_from": "repository checkout",
        "scope": "merenda/**/*.md",
        "summary": {
            "markdown_files": len(rows),
            "canonical_non_readme_files": len(canonical_rows),
            "total_bytes": sum(r["bytes"] for r in rows),
            "broken_local_links": len(broken_links),
            "files_without_incoming_links": len(no_incoming),
            "files_with_no_routing_visibility": len(low_visibility),
            "hidden_heading_candidates": len(hidden),
        },
        "largest_files": [
            {"path": r["path"], "bytes": r["bytes"], "lines": r["lines"], "headings": r["heading_count"]}
            for r in largest
        ],
        "files_without_incoming_links": [r["path"] for r in no_incoming],
        "files_with_no_routing_visibility": [r["path"] for r in low_visibility],
        "hidden_heading_candidates": hidden,
        "broken_local_links": broken_links,
        "files": rows,
    }

    args.json_out.parent.mkdir(parents=True, exist_ok=True)
    args.md_out.parent.mkdir(parents=True, exist_ok=True)
    args.json_out.write_text(json.dumps(inventory, ensure_ascii=False, indent=2), encoding="utf-8")

    md = []
    md.append("# Architecture Inventory — Mechanical Report")
    md.append("")
    md.append("Questo report è meccanico: segnala pattern da sottoporre a review semantica, non decide la dottrina.")
    md.append("")
    md.append("## Summary")
    for key, value in inventory["summary"].items():
        md.append(f"- **{key}:** {value}")
    md.append("")
    md.append("## Largest canonical files")
    md.append("")
    md.append("| File | Bytes | Lines | Headings |")
    md.append("|---|---:|---:|---:|")
    for r in largest:
        md.append(f"| `{r['path']}` | {r['bytes']} | {r['lines']} | {r['heading_count']} |")
    md.append("")
    md.append("## Files with no incoming canonical links")
    md.append("")
    for r in no_incoming:
        md.append(f"- `{r['path']}`")
    md.append("")
    md.append("## Files with no routing visibility")
    md.append("")
    for r in low_visibility:
        md.append(f"- `{r['path']}`")
    md.append("")
    md.append("## Hidden heading candidates")
    md.append("")
    for item in hidden:
        md.append(f"- `{item['path']}#{item['anchor']}` — {item['title']}")
    md.append("")
    if broken_links:
        md.append("## Broken local links")
        md.append("")
        for item in broken_links:
            md.append(f"- `{item['source']}` → `{item['raw']}`")
        md.append("")

    args.md_out.write_text("\n".join(md) + "\n", encoding="utf-8")
    print(json.dumps(inventory["summary"], ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
