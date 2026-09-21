#!/usr/bin/env python3
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CURRENT = ROOT / "REASONING_KERNEL.md"
FROZEN = ROOT / "reviews" / "drafts" / "COMPACT_REASONING_KERNEL_V1.md"
MARKER = "## 1. Role and boundary"


def body(path: Path) -> str:
    text = path.read_text(encoding="utf-8")
    idx = text.find(MARKER)
    if idx < 0:
        raise SystemExit(f"missing kernel body marker in {path}")
    return text[idx:].strip()


def main() -> int:
    if not CURRENT.is_file() or not FROZEN.is_file():
        raise SystemExit("reasoning kernel or frozen validation source missing")

    current = CURRENT.read_text(encoding="utf-8")
    if len(current) > 15000:
        raise SystemExit(f"current reasoning kernel too large: {len(current)} chars")

    if body(CURRENT) != body(FROZEN):
        raise SystemExit(
            "REASONING_KERNEL.md decision body drifted from the behaviorally validated v1 body; "
            "run a new paired evaluation before accepting semantic changes"
        )

    required = [
        "## 3. Core causal sequence",
        "## 4. Diagnostic algorithm",
        "## 12. Evidence and uncertainty",
        "## 13. Temporal and provenance discipline",
        "## 16. Final rule",
    ]
    missing = [marker for marker in required if marker not in current]
    if missing:
        raise SystemExit(f"missing required kernel sections: {missing}")

    print(f"REASONING KERNEL: PASS chars={len(current)} validated_body=v1")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
