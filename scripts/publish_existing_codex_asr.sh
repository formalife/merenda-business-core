#!/usr/bin/env bash
set -euo pipefail

ROOT="$(git rev-parse --show-toplevel)"
cd "$ROOT"

BRANCH="fallback-transcripts-143-149"
if [[ "$(git branch --show-current)" != "$BRANCH" ]]; then
  echo "ERROR: branch attuale $(git branch --show-current), atteso $BRANCH" >&2
  exit 1
fi

python3 scripts/publish_existing_codex_asr.py

FILES=(
  sources/transcripts/jcVKVKvy78k.md
  sources/transcripts/jcVKVKvy78k.asr.json
  sources/transcripts/joY6sigynis.md
  sources/transcripts/joY6sigynis.asr.json
  sources/transcripts/ijVoIMF_gn8.md
  sources/transcripts/ijVoIMF_gn8.asr.json
)

python3 - <<'PY'
import json
from pathlib import Path
for vid in ["jcVKVKvy78k","joY6sigynis","ijVoIMF_gn8"]:
    p=Path(f"sources/transcripts/{vid}.asr.json")
    d=json.loads(p.read_text())
    assert d["coverage_ratio"] >= .85
    assert len(d["segments"]) > 20
    assert all(d["segments"][i]["start"] <= d["segments"][i+1]["start"] for i in range(len(d["segments"])-1))
    print(vid, len(d["segments"]), f"{d['coverage_ratio']:.4%}", d["engine"], d["model"])
PY

git add "${FILES[@]}"
git diff --cached --check
git diff --cached --stat

if git diff --cached --quiet; then
  echo "ERROR: nessun output da committare" >&2
  exit 1
fi

git commit -m "Add recovered local ASR transcripts for 143, 148 and 149"
git push -u origin "$BRANCH"

echo
echo "=== RECUPERO ASR COMPLETATO ==="
git status --short
git log -5 --oneline
git rev-parse HEAD
