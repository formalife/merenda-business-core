#!/usr/bin/env bash
set -euo pipefail

ROOT="$(git rev-parse --show-toplevel)"
cd "$ROOT"

EXPECTED_BRANCH="fallback-transcripts-143-149"
CURRENT_BRANCH="$(git branch --show-current)"
if [[ "$CURRENT_BRANCH" != "$EXPECTED_BRANCH" ]]; then
  echo "ERROR: esegui questo script sul branch $EXPECTED_BRANCH (attuale: $CURRENT_BRANCH)" >&2
  exit 1
fi

if [[ -n "$(git status --porcelain)" ]]; then
  echo "ERROR: working tree non pulito. Salva o committa le modifiche prima di procedere." >&2
  git status --short
  exit 1
fi

WORK="work/local-asr"
VENV="$WORK/.venv"
mkdir -p "$WORK"

python3 -m venv "$VENV"
source "$VENV/bin/activate"
python -m pip install --upgrade pip wheel

if [[ "$(uname -s)" == "Darwin" && "$(uname -m)" == "arm64" ]]; then
  echo "Apple Silicon rilevato: uso mlx-whisper large-v3-turbo."
  python -m pip install yt-dlp mlx-whisper
  python scripts/fallback_local_asr.py     --backend mlx     --model mlx-community/whisper-large-v3-turbo
else
  echo "Apple Silicon non rilevato: uso faster-whisper medium."
  python -m pip install yt-dlp faster-whisper
  python scripts/fallback_local_asr.py     --backend faster     --model medium
fi

python - <<'PY'
import json
from pathlib import Path

expected = {
    "jcVKVKvy78k": 2228,
    "joY6sigynis": 5287,
    "ijVoIMF_gn8": 5548,
}
for vid, duration in expected.items():
    jp = Path(f"sources/transcripts/{vid}.asr.json")
    mp = Path(f"sources/transcripts/{vid}.md")
    assert jp.exists() and jp.stat().st_size > 1000, vid
    assert mp.exists() and mp.stat().st_size > 1000, vid
    data = json.loads(jp.read_text())
    segs = data["segments"]
    assert len(segs) > 20, (vid, len(segs))
    starts = [x["start"] for x in segs]
    assert starts == sorted(starts), vid
    coverage = float(data["coverage_ratio"])
    assert coverage >= 0.85, (vid, coverage)
    print(f"{vid}: segments={len(segs)} last={data['last_segment_end_seconds']} coverage={coverage:.4%}")
PY

git add   sources/transcripts/jcVKVKvy78k.md   sources/transcripts/jcVKVKvy78k.asr.json   sources/transcripts/joY6sigynis.md   sources/transcripts/joY6sigynis.asr.json   sources/transcripts/ijVoIMF_gn8.md   sources/transcripts/ijVoIMF_gn8.asr.json

git diff --cached --check
git diff --cached --stat

git commit -m "Add local ASR transcripts for 143, 148 and 149"
git push -u origin "$EXPECTED_BRANCH"

echo
echo "=== FALLBACK ASR COMPLETATO ==="
git status --short
git log -5 --oneline
git rev-parse HEAD
