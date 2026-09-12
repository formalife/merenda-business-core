#!/usr/bin/env python3
"""Estrae solo i secondi indicati da un video locale ottenuto dalla fonte ufficiale."""
import argparse
import os
import re
import sys
from pathlib import Path
import subprocess


def main():
    p = argparse.ArgumentParser()
    p.add_argument('video', type=Path)
    p.add_argument('--youtube', action='store_true', help='video è un ID del catalogo ufficiale; scarica estratti di 2 secondi')
    p.add_argument('--seconds', type=float, nargs='+', required=True)
    p.add_argument('--output', type=Path, required=True)
    args = p.parse_args()
    if args.youtube:
        download(args, p)
        return
    if not args.video.is_file() or any(t < 0 for t in args.seconds):
        p.error('Servono un video locale esistente e timestamp non negativi')
    args.output.mkdir(parents=True, exist_ok=True)
    for t in args.seconds:
        dest = args.output/f'{args.video.stem}-{t:g}.png'
        subprocess.run(['ffmpeg', '-nostdin', '-n', '-loglevel', 'error', '-ss', str(t), '-i', str(args.video), '-frames:v', '1', str(dest)], check=True)
        print(dest)

def download(args, parser):
    import json
    root = Path(__file__).resolve().parents[1]
    ident = str(args.video)
    if not re.fullmatch(r'[A-Za-z0-9_-]{11}', ident) or ident not in {r['id'] for r in json.loads((root/'sources/catalog.json').read_text())}:
        parser.error('Serve un ID presente nel catalogo ufficiale')
    if any(t < 0 for t in args.seconds):
        parser.error('Timestamp negativi')
    env = dict(os.environ)
    runtime = root/'work/tmp/yt-dlp-runtime'
    command = ['yt-dlp']
    if runtime.exists():
        env['PYTHONPATH'] = str(runtime)
        command = [sys.executable, '-m', 'yt_dlp']
    template = str(root/'work/keyframes'/f'{ident}-%(section_start)s.%(ext)s')
    sections = [arg for t in args.seconds for arg in ['--download-sections', f'*{t}-{t+2}']]
    subprocess.run(command+['-f', 'bv[height<=1080]/b[height<=1080]', *sections, '-o', template, 'https://www.youtube.com/watch?v='+ident], check=True, env=env)
    args.output.mkdir(parents=True, exist_ok=True)
    for t in args.seconds:
        candidates = list((root/'work/keyframes').glob(f'{ident}-{t:g}.*'))
        candidates = [p for p in candidates if p.suffix in ['.mp4', '.webm', '.mkv']]
        if len(candidates) != 1:
            raise SystemExit(f'Estratto non trovato o ambiguo per {t}')
        dest = args.output/f'{ident}-{t:g}.png'
        subprocess.run(['ffmpeg', '-nostdin', '-n', '-loglevel', 'error', '-ss', '1', '-i', str(candidates[0]), '-frames:v', '1', str(dest)], check=True)
        print(dest)

if __name__ == '__main__':
    main()
