#!/usr/bin/env python3
"""Converte JSON3 in testo temporizzato senza inventare correzioni semantiche."""
import argparse
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

def main():
    p = argparse.ArgumentParser()
    p.add_argument('video_id')
    args = p.parse_args()
    if not re.fullmatch(r'[A-Za-z0-9_-]{11}', args.video_id):
        p.error('ID YouTube non valido')
    folder = ROOT/'sources/transcripts'
    source = folder/f'{args.video_id}.it-orig.json3'
    if not source.exists():
        source = folder/f'{args.video_id}.it.json3'
    data = json.loads(source.read_text())
    info = json.loads((folder/f'{args.video_id}.info.json').read_text())
    if info.get('channel_id') != 'UCaAzr7bvYcZRfGR8EyBynOA':
        raise SystemExit('Canale non ammesso')
    lines = []
    for event in data['events']:
        words = ''.join(s.get('utf8', '') for s in event.get('segs', []))
        words = re.sub(r'\s+', ' ', words).strip()
        if not words:
            continue
        seconds = event.get('tStartMs', 0)//1000
        lines.append(f'[{seconds//3600:02}:{seconds//60%60:02}:{seconds%60:02}] {words}')
    header = f'# {info["title"]}\n\nFonte: https://www.youtube.com/watch?v={args.video_id}\nData pubblicazione: {info.get("upload_date", "non disponibile")}\n\nSottotitoli automatici italiani. Normalizzati spazi e segmentazione; revisione semantica e visuale ancora da eseguire. Il JSON3 originale conserva i timestamp precisi.\n\n'
    (folder/f'{args.video_id}.md').write_text(header+'\n\n'.join(lines)+'\n')
    print(f'{len(lines)} segmenti; durata {info.get("duration")} secondi')

if __name__ == '__main__':
    main()
