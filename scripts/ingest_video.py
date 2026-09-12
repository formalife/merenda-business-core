#!/usr/bin/env python3
"""Avvia acquisizione del primo video pendente. Il merge richiede lettura umana/agente."""
import argparse
import json
import os
from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]

def main():
    p = argparse.ArgumentParser()
    p.add_argument('--count', type=int, default=1, help='Prefetch dei primi N pendenti; non completa video')
    p.add_argument('--acquire', action='store_true', help='Scarica metadati e sottotitoli italiani')
    args = p.parse_args()
    rows = json.loads((ROOT/'sources/catalog.json').read_text())
    row = next((r for r in rows if r['status'] not in ['STUDIATO', 'ESCLUSO']), None)
    if not row:
        print('Nessun video pendente: verificare fase 16 con Claude.')
        return
    print(json.dumps(row, ensure_ascii=False, indent=2), flush=True)
    if not args.acquire:
        return
    if args.count < 1 or args.count > 25:
        p.error('--count deve essere tra 1 e 25')
    runtime = ROOT/'work/tmp/yt-dlp-runtime'
    env = dict(os.environ)
    command = ['yt-dlp']
    if runtime.exists():
        env['PYTHONPATH'] = str(runtime)
        command = [sys.executable, '-m', 'yt_dlp']
    pending = [r for r in rows if r['status'] not in ['STUDIATO', 'ESCLUSO']][:args.count]
    for item in pending:
        ident = item['id']
        folder = ROOT/'sources/transcripts'
        if not (folder/f'{ident}.it-orig.json3').exists() and not (folder/f'{ident}.it.json3').exists():
            subprocess.run(command+['--skip-download', '--write-info-json', '--write-subs', '--write-auto-subs', '--sub-langs', 'it-orig,it', '--sub-format', 'json3', '--socket-timeout', '20', '--retries', '1', '-o', str(folder/'%(id)s.%(ext)s'), 'https://www.youtube.com/watch?v='+ident], check=True, env=env)
        info = folder/f'{ident}.info.json'
        if info.exists():
            data = json.loads(info.read_text())
            if data.get('channel_id') != 'UCaAzr7bvYcZRfGR8EyBynOA':
                raise SystemExit('Canale non ammesso: '+ident)
            keys = ['id', 'title', 'channel', 'channel_id', 'channel_url', 'uploader_id', 'webpage_url', 'upload_date', 'duration', 'description', 'availability', 'live_status', 'language', 'chapters']
            slim = {k: data.get(k) for k in keys}
            slim['subtitle_languages'] = list(data['subtitles']) if 'subtitles' in data else data.get('subtitle_languages', [])
            slim['automatic_caption_languages'] = list(data['automatic_captions']) if 'automatic_captions' in data else data.get('automatic_caption_languages', [])
            info.write_text(json.dumps(slim, ensure_ascii=False, indent=2)+'\n')
        if not (folder/f'{ident}.md').exists():
            if (folder/f'{ident}.it-orig.json3').exists() or (folder/f'{ident}.it.json3').exists():
                subprocess.run([sys.executable, str(ROOT/'scripts/transcript.py'), ident], check=True)
            else:
                print('Transcript italiano assente: serve audio/trascrizione per '+ident, flush=True)
    print('Acquisizione conclusa. Non cambia stato: eseguire revisione, visuale, merge e fase 13.')

if __name__ == '__main__':
    main()
