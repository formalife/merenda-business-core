#!/usr/bin/env python3
import argparse
import json
import platform
import subprocess
import sys
from pathlib import Path

IDS = [
    "jcVKVKvy78k",
    "joY6sigynis",
    "ijVoIMF_gn8",
]

def run(*args):
    print("+", " ".join(map(str, args)), flush=True)
    subprocess.run(list(map(str, args)), check=True)

def hms(sec):
    sec = max(0, int(sec))
    return f"{sec//3600:02d}:{(sec%3600)//60:02d}:{sec%60:02d}"

def choose_backend(requested):
    if requested != "auto":
        return requested
    if platform.system() == "Darwin" and platform.machine() == "arm64":
        return "mlx"
    return "faster"

def find_audio(work, vid):
    candidates = [
        p for p in work.glob(f"{vid}.*")
        if p.suffix not in {".json", ".md", ".part"}
        and not p.name.endswith(".asr.json")
    ]
    return sorted(candidates)[0] if candidates else None

def transcribe_mlx(audio, model_name):
    try:
        import mlx_whisper
    except Exception as exc:
        raise SystemExit(
            "Backend MLX non disponibile. Installa con: python3 -m pip install mlx-whisper yt-dlp"
        ) from exc
    result = mlx_whisper.transcribe(
        str(audio),
        path_or_hf_repo=model_name,
        language="it",
        word_timestamps=False,
    )
    rows = []
    for seg in result.get("segments", []):
        text = (seg.get("text") or "").strip()
        if text:
            rows.append({
                "start": round(float(seg["start"]), 3),
                "end": round(float(seg["end"]), 3),
                "text": text,
            })
    return rows, {
        "engine": "mlx-whisper",
        "model": model_name,
        "device": "Apple Silicon / MLX",
        "compute_type": "MLX model native",
        "beam_size": None,
        "vad_filter": None,
        "language_detected": result.get("language"),
        "language_probability": None,
    }

def transcribe_faster(audio, model_name):
    try:
        from faster_whisper import WhisperModel
    except Exception as exc:
        raise SystemExit(
            "Backend faster-whisper non disponibile. Installa con: python3 -m pip install faster-whisper yt-dlp"
        ) from exc
    model = WhisperModel(model_name, device="cpu", compute_type="int8")
    segments, detected = model.transcribe(
        str(audio),
        language="it",
        beam_size=5,
        vad_filter=True,
        condition_on_previous_text=True,
    )
    rows = []
    for seg in segments:
        text = (seg.text or "").strip()
        if text:
            rows.append({
                "start": round(float(seg.start), 3),
                "end": round(float(seg.end), 3),
                "text": text,
            })
    return rows, {
        "engine": "faster-whisper",
        "model": model_name,
        "device": "cpu",
        "compute_type": "int8",
        "beam_size": 5,
        "vad_filter": True,
        "language_detected": getattr(detected, "language", None),
        "language_probability": getattr(detected, "language_probability", None),
    }

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--backend", choices=["auto", "mlx", "faster"], default="auto")
    ap.add_argument("--model", default=None)
    ap.add_argument("--workdir", default="work/local-asr")
    ap.add_argument("--ids", nargs="*", default=IDS)
    args = ap.parse_args()

    backend = choose_backend(args.backend)
    if args.model:
        model_name = args.model
    elif backend == "mlx":
        model_name = "mlx-community/whisper-large-v3-turbo"
    else:
        model_name = "medium"

    work = Path(args.workdir)
    work.mkdir(parents=True, exist_ok=True)

    print(f"Backend: {backend}", flush=True)
    print(f"Model: {model_name}", flush=True)

    for vid in args.ids:
        info_path = Path(f"sources/transcripts/{vid}.info.json")
        if not info_path.exists():
            raise SystemExit(f"Missing metadata: {info_path}")
        info = json.loads(info_path.read_text())

        audio = find_audio(work, vid)
        if audio is None:
            run(
                sys.executable, "-m", "yt_dlp",
                "--no-playlist",
                "-f", "bestaudio",
                "-o", str(work / "%(id)s.%(ext)s"),
                info["webpage_url"],
            )
            audio = find_audio(work, vid)
        if audio is None:
            raise SystemExit(f"Audio download missing for {vid}")

        print(f"Transcribing {vid} from {audio.name}", flush=True)
        if backend == "mlx":
            rows, provenance = transcribe_mlx(audio, model_name)
        else:
            rows, provenance = transcribe_faster(audio, model_name)

        if not rows:
            raise SystemExit(f"No ASR segments for {vid}")

        duration = float(info.get("duration") or 0)
        last = rows[-1]["end"]
        coverage = last / duration if duration else None
        if duration and coverage < 0.85:
            raise SystemExit(f"Coverage too low for {vid}: {coverage:.3f}")

        payload = {
            "video_id": vid,
            "source_url": info.get("webpage_url"),
            "language_requested": "it",
            **provenance,
            "duration_seconds_metadata": duration,
            "last_segment_end_seconds": last,
            "coverage_ratio": coverage,
            "segments": rows,
        }
        Path(f"sources/transcripts/{vid}.asr.json").write_text(
            json.dumps(payload, ensure_ascii=False, indent=2) + "\n"
        )

        details = f"{provenance['engine']} / {provenance['model']}"
        lines = [
            f"# {info['title']}",
            "",
            f"Fonte: {info.get('webpage_url','')}",
            f"Data pubblicazione: {info.get('upload_date','')}",
            "",
            "Trascrizione locale automatica da audio usata come fallback perché il video non dispone di sottotitoli italiani utilizzabili.",
            f"Motore/modello: {details}; lingua richiesta=it.",
            "Revisione semantica ancora da eseguire.",
            "",
        ]
        for row in rows:
            lines += [f"[{hms(row['start'])}] {row['text']}", ""]
        Path(f"sources/transcripts/{vid}.md").write_text(
            "\n".join(lines).rstrip() + "\n"
        )

        print(json.dumps({
            "id": vid,
            "segments": len(rows),
            "last": last,
            "duration": duration,
            "coverage": coverage,
            "engine": provenance["engine"],
            "model": provenance["model"],
            "language_detected": provenance["language_detected"],
        }, ensure_ascii=False), flush=True)

if __name__ == "__main__":
    main()
