#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import re
from collections import defaultdict
from pathlib import Path
from statistics import mean

CONTROL = {
    "LAYER1_CONTRACT.md",
    "FORMALIFE_REBUILD_PROTOCOL.md",
    "MERENDA_MODE.md",
    "merenda/DECISION_ROUTER.md",
    "merenda/00_fondamenti/sistema-operativo-merenda.md",
}
READ_RE = re.compile(
    r"EVAL_READER\.py\s+(?P<op>headings|read|section)\s+"
    r"(?P<path>[^\s\"']+|\"[^\"]+\"|'[^']+')"
    r"(?:\s+(?P<anchor>[^\s\"']+|\"[^\"]+\"|'[^']+'))?"
)
HEADING_RE = re.compile(r"^(#{1,6})\s+(.+?)\s*$")
WORKSPACE_BY_ARCH = {
    "current": "workspace-current",
    "current_plus_map": "workspace-current-plus-map",
}


def unq(s: str | None) -> str | None:
    if s and len(s) >= 2 and s[0] == s[-1] and s[0] in "'\"":
        return s[1:-1]
    return s


def slug(s: str) -> str:
    s = s.strip().lower()
    s = re.sub(r"[^\w\s\-]", "", s, flags=re.UNICODE)
    s = re.sub(r"\s+", "-", s)
    return re.sub(r"-+", "-", s).strip("-")


def safe(root: Path, rel: str) -> Path:
    p = (root / rel).resolve()
    if p != root and root not in p.parents:
        raise ValueError(f"path escapes workspace: {rel}")
    if not p.is_file():
        raise FileNotFoundError(rel)
    return p


def headings_output(text: str) -> str:
    out = []
    code_block = False
    for line in text.splitlines():
        if line.lstrip().startswith("```"):
            code_block = not code_block
            continue
        if code_block:
            continue
        m = HEADING_RE.match(line)
        if m:
            out.append(f"{len(m.group(1))}\t{slug(m.group(2))}\t{m.group(2)}")
    return "\n".join(out) + ("\n" if out else "")


def section_output(text: str, anchor: str) -> str:
    lines = text.splitlines()
    code_block = False
    start = None
    level = None
    for i, line in enumerate(lines):
        if line.lstrip().startswith("```"):
            code_block = not code_block
            continue
        if code_block:
            continue
        m = HEADING_RE.match(line)
        if m and slug(m.group(2)) == anchor:
            start = i
            level = len(m.group(1))
            break
    if start is None or level is None:
        raise ValueError(f"anchor not found: {anchor}")
    end = len(lines)
    code_block = False
    for i in range(start + 1, len(lines)):
        line = lines[i]
        if line.lstrip().startswith("```"):
            code_block = not code_block
            continue
        if code_block:
            continue
        m = HEADING_RE.match(line)
        if m and len(m.group(1)) <= level:
            end = i
            break
    return "\n".join(lines[start:end]) + ("\n" if start < end else "")


def classify(path: str) -> str:
    if path in CONTROL:
        return "control_plane"
    if path.startswith("reviews/drafts/DOCTRINE_RETRIEVAL_MAP_"):
        return "routing_metadata"
    if path.startswith("merenda/"):
        return "specialist_doctrine"
    return "other"


def successful_commands(events: list[dict]) -> list[str]:
    """Return unique completed command executions that did not fail.

    The baseline event stream can contain both item.started and item.completed
    records. Counting started commands can accidentally treat a failed file read
    as consumed context, so context accounting uses completed successful reads
    only.
    """
    out = []
    for event in events:
        if event.get("type") != "item.completed":
            continue
        item = event.get("item")
        if not isinstance(item, dict) or item.get("type") != "command_execution":
            continue
        command = item.get("command")
        if not isinstance(command, str):
            continue
        exit_code = item.get("exit_code")
        status = item.get("status")
        if isinstance(exit_code, int) and exit_code != 0:
            continue
        if isinstance(status, str) and status.lower() in {"failed", "error", "cancelled"}:
            continue
        if command not in out:
            out.append(command)
    return out


def operation_payload(workspace: Path, op: str, path: str, anchor: str | None) -> str:
    text = safe(workspace, path).read_text(encoding="utf-8")
    if op == "read":
        return text
    if op == "headings":
        return headings_output(text)
    if op == "section":
        if not anchor:
            raise ValueError(f"section without anchor: {path}")
        return section_output(text, anchor)
    raise ValueError(op)


def load_events(path: Path) -> list[dict]:
    rows = []
    for raw in path.read_text(encoding="utf-8").splitlines():
        if raw.strip():
            rows.append(json.loads(raw))
    return rows


def workspace_for(base: Path, arch: str) -> Path:
    name = WORKSPACE_BY_ARCH.get(arch)
    if not name:
        raise SystemExit(f"unknown architecture directory: {arch}")
    root = (base / name).resolve()
    if not root.is_dir():
        raise SystemExit(
            f"missing frozen workspace for {arch}: {root}. "
            "Do not reconstruct context cost from the current repository; "
            "the exact baseline workspace is required."
        )
    return root


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--baseline-dir", type=Path, default=Path("/tmp/formalife-routing-baseline"))
    ap.add_argument("--json-out", type=Path, default=Path("/tmp/formalife-context-read-summary.json"))
    args = ap.parse_args()

    base = args.baseline_dir.resolve()
    events_root = base / "events"
    if not events_root.is_dir():
        raise SystemExit(f"missing baseline events directory: {events_root}")

    rows = []
    skipped_failed_reads = 0

    for arch_dir in sorted(events_root.iterdir()):
        if not arch_dir.is_dir():
            continue
        arch = arch_dir.name
        workspace = workspace_for(base, arch)
        for event_path in sorted(arch_dir.glob("R*.jsonl")):
            cid = event_path.stem
            events = load_events(event_path)
            ops = []
            category_chars: dict[str, int] = defaultdict(int)
            category_words: dict[str, int] = defaultdict(int)
            seen_targets = set()
            unique_chars = 0
            unique_words = 0

            all_read_commands = []
            for event in events:
                item = event.get("item")
                if (
                    event.get("type") in ("item.started", "item.completed")
                    and isinstance(item, dict)
                    and item.get("type") == "command_execution"
                    and isinstance(item.get("command"), str)
                    and "EVAL_READER.py" in item["command"]
                ):
                    all_read_commands.append(item["command"])
            successful = successful_commands(events)
            skipped_failed_reads += len(set(all_read_commands) - set(successful))

            for command in successful:
                m = READ_RE.search(command)
                if not m:
                    continue
                op = m.group("op")
                path = unq(m.group("path"))
                anchor = unq(m.group("anchor"))
                if path is None:
                    continue
                try:
                    payload = operation_payload(workspace, op, path, anchor)
                except (FileNotFoundError, ValueError) as exc:
                    raise SystemExit(
                        f"{arch}/{cid}: successful baseline command cannot be reconstructed "
                        f"from frozen workspace: {op} {path} {anchor or ''}: {exc}"
                    )
                chars = len(payload)
                words = len(payload.split())
                category = classify(path)
                category_chars[category] += chars
                category_words[category] += words
                target = (op, path, anchor)
                if target not in seen_targets:
                    seen_targets.add(target)
                    unique_chars += chars
                    unique_words += words
                ops.append(
                    {
                        "op": op,
                        "path": path,
                        "anchor": anchor,
                        "category": category,
                        "chars": chars,
                        "words": words,
                    }
                )

            rows.append(
                {
                    "case_id": cid,
                    "architecture": arch,
                    "read_operations": len(ops),
                    "operation_chars": sum(x["chars"] for x in ops),
                    "operation_words": sum(x["words"] for x in ops),
                    "unique_target_chars": unique_chars,
                    "unique_target_words": unique_words,
                    "category_chars": dict(category_chars),
                    "category_words": dict(category_words),
                    "operations": ops,
                }
            )

    by_arch: dict[str, list[dict]] = defaultdict(list)
    for row in rows:
        by_arch[row["architecture"]].append(row)

    summary = {}
    for arch, arch_rows in sorted(by_arch.items()):
        summary[arch] = {
            "cases": len(arch_rows),
            "mean_read_operations": mean(r["read_operations"] for r in arch_rows),
            "mean_operation_chars": mean(r["operation_chars"] for r in arch_rows),
            "mean_operation_words": mean(r["operation_words"] for r in arch_rows),
            "mean_unique_target_chars": mean(r["unique_target_chars"] for r in arch_rows),
            "mean_unique_target_words": mean(r["unique_target_words"] for r in arch_rows),
            "total_category_chars": {
                category: sum(r["category_chars"].get(category, 0) for r in arch_rows)
                for category in ("control_plane", "routing_metadata", "specialist_doctrine", "other")
            },
        }

    output = {
        "measurement": (
            "deterministically reconstructed successful EVAL_READER outputs from the exact frozen "
            "baseline workspaces; repository list output and model/system tokens excluded"
        ),
        "skipped_failed_or_incomplete_command_variants": skipped_failed_reads,
        "summary": summary,
        "cases": rows,
    }
    args.json_out.parent.mkdir(parents=True, exist_ok=True)
    args.json_out.write_text(json.dumps(output, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(summary, ensure_ascii=False, indent=2))
    print(f"Skipped failed/incomplete command variants: {skipped_failed_reads}")
    print(f"CONTEXT READ SCORE: PASS out={args.json_out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
