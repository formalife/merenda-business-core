#!/usr/bin/env python3
"""
Pubblica gli ASR grezzi già prodotti da Codex in work/tmp/local-asr senza
ritrascrivere l'audio e senza correzioni semantiche.
"""
import json
import re
import subprocess
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RAW_DIR = ROOT / "work" / "tmp" / "local-asr"
OUT_DIR = ROOT / "sources" / "transcripts"

VIDEOS = [
    "jcVKVKvy78k",
    "joY6sigynis",
    "ijVoIMF_gn8",
]

def hms(sec):
    sec = max(0, int(float(sec)))
    return f"{sec//3600:02d}:{(sec%3600)//60:02d}:{sec%60:02d}"

def flatten_candidates(data):
    if isinstance(data, list):
        return data, {}
    if not isinstance(data, dict):
        raise ValueError(f"Formato JSON non supportato: {type(data).__name__}")

    for key in ("segments", "chunks"):
        if isinstance(data.get(key), list):
            return data[key], data

    for key in ("result", "results", "transcription", "output"):
        obj = data.get(key)
        if isinstance(obj, dict):
            for sub in ("segments", "chunks"):
                if isinstance(obj.get(sub), list):
                    meta = dict(data)
                    meta.update({f"nested_{k}": v for k, v in obj.items() if k != sub})
                    return obj[sub], meta
        elif isinstance(obj, list):
            return obj, data

    raise ValueError("Nessun array segments/chunks riconosciuto")

def parse_segment(seg):
    if not isinstance(seg, dict):
        return None

    text = seg.get("text")
    if text is None:
        text = seg.get("sentence")
    if text is None and isinstance(seg.get("words"), list):
        text = " ".join(
            str(w.get("word") or w.get("text") or "").strip()
            for w in seg["words"]
            if isinstance(w, dict)
        )
    text = re.sub(r"\s+", " ", str(text or "")).strip()
    if not text:
        return None

    start = seg.get("start")
    end = seg.get("end")
    if start is None:
        start = seg.get("start_time")
    if end is None:
        end = seg.get("end_time")

    ts = seg.get("timestamp")
    if (start is None or end is None) and isinstance(ts, (list, tuple)) and len(ts) >= 2:
        start, end = ts[0], ts[1]

    if start is None:
        start = seg.get("offset")
    if end is None and start is not None and seg.get("duration") is not None:
        end = float(start) + float(seg["duration"])

    if start is None or end is None:
        raise ValueError(f"Segmento senza start/end: {seg!r}")

    return {
        "start": round(float(start), 3),
        "end": round(float(end), 3),
        "text": text,
    }

def detect_provenance(meta, vid):
    log = RAW_DIR / f"{vid}.asr.log"
    log_text = log.read_text(errors="replace") if log.exists() else ""

    engine = meta.get("engine") or meta.get("backend")
    model = meta.get("model") or meta.get("model_name") or meta.get("model_id")

    if not engine:
        lowered = log_text.lower()
        if "mlx" in lowered:
            engine = "mlx-whisper"
        elif "faster-whisper" in lowered or "faster_whisper" in lowered:
            engine = "faster-whisper"
        elif "whisper" in lowered:
            engine = "whisper"
        else:
            engine = "local-whisper-asr"

    if not model:
        patterns = [
            r"(?:model|modello)\s*[:=]\s*([^\s,;]+)",
            r"(mlx-community/whisper-[A-Za-z0-9._-]+)",
            r"(large-v3(?:-turbo)?|medium|small|base|tiny)",
        ]
        for pat in patterns:
            m = re.search(pat, log_text, re.I)
            if m:
                model = m.group(1)
                break
    if not model:
        model = "non determinato dal raw/log"

    lang = (
        meta.get("language")
        or meta.get("language_detected")
        or meta.get("detected_language")
        or "it"
    )
    prob = (
        meta.get("language_probability")
        or meta.get("language_prob")
        or meta.get("probability")
    )
    return engine, model, lang, prob

def main():
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    summary = []

    for vid in VIDEOS:
        raw_path = RAW_DIR / f"{vid}.raw.json"
        info_path = OUT_DIR / f"{vid}.info.json"
        if not raw_path.exists():
            raise SystemExit(f"Manca {raw_path.relative_to(ROOT)}")
        if not info_path.exists():
            raise SystemExit(f"Manca {info_path.relative_to(ROOT)}")

        raw = json.loads(raw_path.read_text())
        candidates, meta = flatten_candidates(raw)
        rows = []
        for seg in candidates:
            parsed = parse_segment(seg)
            if parsed:
                rows.append(parsed)

        if len(rows) < 20:
            raise SystemExit(f"{vid}: troppo pochi segmenti ({len(rows)})")

        rows.sort(key=lambda x: (x["start"], x["end"]))
        for prev, curr in zip(rows, rows[1:]):
            if curr["start"] < prev["start"]:
                raise SystemExit(f"{vid}: timestamp non monotoni")

        info = json.loads(info_path.read_text())
        duration = float(info.get("duration") or 0)
        last_end = rows[-1]["end"]
        coverage = last_end / duration if duration else None
        if duration and coverage < 0.85:
            raise SystemExit(f"{vid}: copertura insufficiente {coverage:.2%}")

        counts = Counter(r["text"].strip().lower() for r in rows)
        max_repeat_text, max_repeat_n = counts.most_common(1)[0]

        engine, model, detected_lang, lang_prob = detect_provenance(meta, vid)

        payload = {
            "video_id": vid,
            "source_url": info.get("webpage_url") or f"https://www.youtube.com/watch?v={vid}",
            "provenance": "local automatic fallback from Codex raw ASR",
            "raw_source": f"work/tmp/local-asr/{vid}.raw.json",
            "language_requested": "it",
            "language_detected": detected_lang,
            "language_probability": lang_prob,
            "engine": engine,
            "model": model,
            "duration_seconds_metadata": duration,
            "last_segment_end_seconds": last_end,
            "coverage_ratio": coverage,
            "segment_count": len(rows),
            "max_exact_text_repeat": {
                "count": max_repeat_n,
                "text": max_repeat_text,
            },
            "segments": rows,
        }
        asr_path = OUT_DIR / f"{vid}.asr.json"
        asr_path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n")

        lines = [
            f"# {info['title']}",
            "",
            f"Fonte: {payload['source_url']}",
            f"Data pubblicazione: {info.get('upload_date', 'non disponibile')}",
            "",
            "Trascrizione automatica locale di fallback ricavata dall'audio del video perché non erano disponibili sottotitoli italiani utilizzabili.",
            f"Provenienza tecnica: {engine} / {model}. Raw originale: work/tmp/local-asr/{vid}.raw.json.",
            "Nessuna correzione semantica applicata; revisione semantica e visuale ancora da eseguire.",
            "",
        ]
        for row in rows:
            lines.append(f"[{hms(row['start'])}] {row['text']}")
            lines.append("")
        md_path = OUT_DIR / f"{vid}.md"
        md_path.write_text("\n".join(lines).rstrip() + "\n")

        summary.append({
            "id": vid,
            "segments": len(rows),
            "duration": duration,
            "last_end": last_end,
            "coverage": coverage,
            "engine": engine,
            "model": model,
            "max_repeat": max_repeat_n,
        })

    print("=== VALIDAZIONE RAW -> OUTPUT ===")
    for x in summary:
        print(
            f"{x['id']}: segments={x['segments']} "
            f"last={x['last_end']:.2f}/{x['duration']:.0f}s "
            f"coverage={x['coverage']:.4%} "
            f"engine={x['engine']} model={x['model']} "
            f"max_exact_repeat={x['max_repeat']}"
        )

if __name__ == "__main__":
    main()
