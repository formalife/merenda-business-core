#!/usr/bin/env python3
"""Acquisisce asset tecnici dei video pendenti senza eseguire il merge semantico."""
import argparse
from datetime import datetime, timezone
import json
import os
from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
TRANSCRIPTS = ROOT / 'sources' / 'transcripts'
PROGRESS = ROOT / 'sources' / 'queue' / 'acquisition-progress.md'
ACQUISITION_LOCK = ROOT / 'sources' / 'queue' / 'ACQUISITION_CLOSED.md'
OFFICIAL_CHANNEL_ID = 'UCaAzr7bvYcZRfGR8EyBynOA'


def run(cmd, **kwargs):
    return subprocess.run(cmd, check=True, **kwargs)


def git_clean():
    out = subprocess.run(
        ['git', 'status', '--porcelain'],
        cwd=ROOT,
        text=True,
        capture_output=True,
        check=True,
    ).stdout.strip()
    return not out


def write_progress(batch, states):
    done = sum(1 for s in states.values() if s['status'] != 'PENDING')
    lines = [
        '# Acquisition Progress',
        '',
        f'Ultimo aggiornamento: {datetime.now(timezone.utc).isoformat()}',
        '',
        f'Batch: {len(batch)} video',
        f'Completati tecnicamente: {done}/{len(batch)}',
        '',
        '| # | Video ID | Titolo | Stato | Nota |',
        '|---:|---|---|---|---|',
    ]
    for idx, item in enumerate(batch, 1):
        state = states[item['id']]
        title = item.get('title', '').replace('|', '\\|')
        note = state.get('note', '').replace('|', '\\|')
        lines.append(f"| {idx} | {item['id']} | {title} | {state['status']} | {note} |")
    PROGRESS.write_text('\n'.join(lines) + '\n')


def commit_and_push(item, push):
    ident = item['id']
    paths = [p for p in TRANSCRIPTS.glob(f'{ident}.*') if p.is_file()]
    paths.append(PROGRESS)
    rels = [str(p.relative_to(ROOT)) for p in paths]
    run(['git', 'add', '--', *rels], cwd=ROOT)
    changed = subprocess.run(
        ['git', 'diff', '--cached', '--quiet'],
        cwd=ROOT,
    ).returncode != 0
    if changed:
        run(['git', 'commit', '-m', f'Acquire technical assets for {ident}'], cwd=ROOT)
        if push:
            branch = subprocess.run(
                ['git', 'branch', '--show-current'],
                cwd=ROOT,
                text=True,
                capture_output=True,
                check=True,
            ).stdout.strip()
            if not branch:
                raise RuntimeError('Impossibile determinare il branch Git corrente.')
            run(['git', 'push', '-u', 'origin', branch], cwd=ROOT)


def acquire_one(item, command, env):
    ident = item['id']
    if not (TRANSCRIPTS / f'{ident}.it-orig.json3').exists() and not (TRANSCRIPTS / f'{ident}.it.json3').exists():
        run(
            command + [
                '--skip-download',
                '--write-info-json',
                '--write-subs',
                '--write-auto-subs',
                '--sub-langs', 'it-orig,it',
                '--sub-format', 'json3',
                '--socket-timeout', '20',
                '--retries', '1',
                '-o', str(TRANSCRIPTS / '%(id)s.%(ext)s'),
                'https://www.youtube.com/watch?v=' + ident,
            ],
            env=env,
        )

    info = TRANSCRIPTS / f'{ident}.info.json'
    if info.exists():
        data = json.loads(info.read_text())
        if data.get('channel_id') != OFFICIAL_CHANNEL_ID:
            raise RuntimeError('Canale non ammesso: ' + ident)
        keys = [
            'id', 'title', 'channel', 'channel_id', 'channel_url', 'uploader_id',
            'webpage_url', 'upload_date', 'duration', 'description',
            'availability', 'live_status', 'language', 'chapters'
        ]
        slim = {k: data.get(k) for k in keys}
        slim['subtitle_languages'] = list(data['subtitles']) if 'subtitles' in data else data.get('subtitle_languages', [])
        slim['automatic_caption_languages'] = list(data['automatic_captions']) if 'automatic_captions' in data else data.get('automatic_caption_languages', [])
        info.write_text(json.dumps(slim, ensure_ascii=False, indent=2) + '\n')

    transcript = TRANSCRIPTS / f'{ident}.md'
    if not transcript.exists():
        if (TRANSCRIPTS / f'{ident}.it-orig.json3').exists() or (TRANSCRIPTS / f'{ident}.it.json3').exists():
            run([sys.executable, str(ROOT / 'scripts' / 'transcript.py'), '--', ident])
        else:
            return 'NO_IT_TRANSCRIPT', 'Sottotitoli italiani assenti: servirà fallback audio/trascrizione.'

    return 'ACQUIRED', 'Metadata + transcript Markdown disponibili.'


def main():
    p = argparse.ArgumentParser()
    p.add_argument('--count', type=int, default=1, help='Numero di video pendenti da acquisire (1-25)')
    p.add_argument('--acquire', action='store_true', help='Scarica metadati e sottotitoli italiani')
    p.add_argument('--commit-each', action='store_true', help='Commit Git dopo ogni singolo video')
    p.add_argument('--push-each', action='store_true', help='Push sul branch Git corrente dopo ogni singolo video; implica --commit-each')
    p.add_argument('--continue-on-error', action='store_true', help='Continua il batch se un video fallisce')
    args = p.parse_args()

    if ACQUISITION_LOCK.exists():
        raise SystemExit(
            'Acquisizione Merenda chiusa per saturazione. '
            'Vedi sources/queue/ACQUISITION_CLOSED.md e STATUS.md. '
            'Non rimuovere il lock senza una decisione esplicita sul gap da riaprire.'
        )

    if args.count < 1 or args.count > 25:
        p.error('--count deve essere tra 1 e 25')
    if args.push_each:
        args.commit_each = True

    rows = json.loads((ROOT / 'sources' / 'catalog.json').read_text())
    by_id = {r['id']: r for r in rows}

    # QUEUE.md è la fonte canonica dell'ordine di apprendimento.
    # catalog.json conserva metadata/status ma può mantenere un ordine storico.
    queue_text = (ROOT / 'sources' / 'queue' / 'QUEUE.md').read_text()
    queue_ids = []
    for line in queue_text.splitlines():
        if not line.startswith('|'):
            continue
        parts = [part.strip() for part in line.split('|')]
        if len(parts) < 3 or not parts[1].isdigit():
            continue

        video_cell = parts[2]
        if not video_cell.startswith('[') or '](' not in video_cell:
            continue

        ident = video_cell[1:video_cell.index('](')]
        if len(ident) == 11 and all(ch.isalnum() or ch in '_-' for ch in ident):
            queue_ids.append(ident)

    pending = []
    for ident in queue_ids:
        row = by_id.get(ident)
        if row and row.get('status') not in ['STUDIATO', 'ESCLUSO']:
            pending.append(row)
            if len(pending) >= args.count:
                break

    if not pending:
        print('Nessun video pendente nella queue canonica: verificare fase 16 con Claude.')
        return

    if not args.acquire:
        print(json.dumps(pending[0], ensure_ascii=False, indent=2))
        return

    if args.commit_each and not git_clean():
        raise SystemExit('Working tree non pulito. Esegui git status e salva/stasha le modifiche prima di usare --commit-each.')

    runtime = ROOT / 'work' / 'tmp' / 'yt-dlp-runtime'
    env = dict(os.environ)
    command = ['yt-dlp']
    if runtime.exists():
        env['PYTHONPATH'] = str(runtime)
        command = [sys.executable, '-m', 'yt_dlp']

    states = {r['id']: {'status': 'PENDING', 'note': ''} for r in pending}
    write_progress(pending, states)

    for idx, item in enumerate(pending, 1):
        ident = item['id']
        title = item.get('title', '')
        print(f'\n===== [{idx}/{len(pending)}] {ident} — {title} =====', flush=True)
        try:
            status, note = acquire_one(item, command, env)
            states[ident] = {'status': status, 'note': note}
            print(f'[{idx}/{len(pending)}] {status}: {note}', flush=True)
        except Exception as exc:
            states[ident] = {'status': 'ERROR', 'note': str(exc)}
            print(f'[{idx}/{len(pending)}] ERROR: {exc}', file=sys.stderr, flush=True)

        write_progress(pending, states)

        if args.commit_each:
            commit_and_push(item, args.push_each)

        if states[ident]['status'] == 'ERROR' and not args.continue_on_error:
            raise SystemExit(f'Batch interrotto su {ident}. I progressi precedenti restano salvati.')

    print(f'\nAcquisizione conclusa: {len(pending)} video processati tecnicamente.', flush=True)
    print(f'Monitor: {PROGRESS.relative_to(ROOT)}', flush=True)
    print('Nessun video è stato marcato STUDIATO: revisione semantica e merge restano separati.', flush=True)


if __name__ == '__main__':
    main()
