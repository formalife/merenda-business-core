#!/usr/bin/env python3
import argparse
import json
import subprocess
import sys
from pathlib import Path

IDS = [
    "jcVKVKvy78k",
    "joY6sigynis",
    "ijVoIMF_gn8",
]

def run(*args):
    print("+", " ".join(map(str,args)), flush=True)
    subprocess.run(list(map(str,args)), check=True)

def hms(sec):
    sec=max(0,int(sec))
    return f"{sec//3600:02d}:{(sec%3600)//60:02d}:{sec%60:02d}"

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--model", default="medium")
    ap.add_argument("--workdir", default="work/local-asr")
    ap.add_argument("--ids", nargs="*", default=IDS)
    args=ap.parse_args()

    try:
        from faster_whisper import WhisperModel
    except Exception:
        raise SystemExit("Missing faster-whisper. Install with: python3 -m pip install faster-whisper yt-dlp")

    work=Path(args.workdir)
    work.mkdir(parents=True, exist_ok=True)
    model=WhisperModel(args.model, device="cpu", compute_type="int8")

    for vid in args.ids:
        info_path=Path(f"sources/transcripts/{vid}.info.json")
        if not info_path.exists():
            raise SystemExit(f"Missing metadata: {info_path}")
        info=json.loads(info_path.read_text())
        audio=work/f"{vid}.m4a"

        if not audio.exists():
            run(sys.executable,"-m","yt_dlp","--no-playlist","-f","bestaudio[ext=m4a]/bestaudio","-o",str(work/"%(id)s.%(ext)s"),info["webpage_url"])
            candidates=list(work.glob(f"{vid}.*"))
            candidates=[p for p in candidates if p.suffix not in {".json",".md"}]
            if not candidates:
                raise SystemExit(f"Audio download missing for {vid}")
            src=candidates[0]
            if src != audio:
                run("ffmpeg","-y","-i",src,"-vn","-acodec","aac",audio)

        print(f"Transcribing {vid} with {args.model}", flush=True)
        segs,detected=model.transcribe(str(audio), language="it", beam_size=5, vad_filter=True, condition_on_previous_text=True)
        rows=[]
        for s in segs:
            t=(s.text or "").strip()
            if t:
                rows.append({"start":round(float(s.start),3),"end":round(float(s.end),3),"text":t})
        if not rows:
            raise SystemExit(f"No ASR segments for {vid}")

        duration=float(info.get("duration") or 0)
        last=rows[-1]["end"]
        coverage=last/duration if duration else None
        if duration and coverage < .85:
            raise SystemExit(f"Coverage too low for {vid}: {coverage:.3f}")

        payload={
            "video_id":vid,
            "source_url":info.get("webpage_url"),
            "language_requested":"it",
            "language_detected":getattr(detected,"language",None),
            "language_probability":getattr(detected,"language_probability",None),
            "engine":"faster-whisper",
            "model":args.model,
            "device":"cpu",
            "compute_type":"int8",
            "beam_size":5,
            "vad_filter":True,
            "duration_seconds_metadata":duration,
            "last_segment_end_seconds":last,
            "coverage_ratio":coverage,
            "segments":rows,
        }
        Path(f"sources/transcripts/{vid}.asr.json").write_text(json.dumps(payload,ensure_ascii=False,indent=2)+"\n")
        lines=[
            f"# {info['title']}","",
            f"Fonte: {info.get('webpage_url','')}",
            f"Data pubblicazione: {info.get('upload_date','')}","",
            "Trascrizione locale automatica da audio usata come fallback perché il video non dispone di sottotitoli italiani utilizzabili.",
            f"Motore/modello: faster-whisper / {args.model} (CPU int8, lingua=it, beam_size=5, VAD attivo).",
            "Revisione semantica ancora da eseguire.",""
        ]
        for row in rows:
            lines += [f"[{hms(row['start'])}] {row['text']}",""]
        Path(f"sources/transcripts/{vid}.md").write_text("\n".join(lines).rstrip()+"\n")
        print(json.dumps({"id":vid,"segments":len(rows),"last":last,"coverage":coverage,"lang":getattr(detected,"language",None),"prob":getattr(detected,"language_probability",None)},ensure_ascii=False), flush=True)

if __name__=="__main__":
    main()
