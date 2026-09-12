#!/usr/bin/env python3
"""Controlli offline: congelamento, routing, corpus, queue e contatori."""
import json
from pathlib import Path
import re
import subprocess

ROOT = Path(__file__).resolve().parents[1]

def main():
    errors = []
    frozen = ['MASTER_PLAN.md', 'system/RULES.md', 'system/PHASES.md', 'system/HANDOFFS.md', 'system/FROZEN_FILES.md']
    for name in frozen:
        original = subprocess.check_output(['git', 'show', 'merenda-system-v1.0:'+name], cwd=ROOT)
        if original != (ROOT/name).read_bytes():
            errors.append('File congelato modificato: '+name)
    rows = json.loads((ROOT/'sources/catalog.json').read_text())
    ids = [r['id'] for r in rows]
    if len(ids) != len(set(ids)):
        errors.append('ID duplicati')
    scanned = set()
    for tab in ['videos', 'shorts', 'streams']:
        data = json.loads((ROOT/f'work/channel-{tab}.json').read_text())
        if data['channel_id'] != 'UCaAzr7bvYcZRfGR8EyBynOA':
            errors.append('Canale errato: '+tab)
        scanned.update(e['id'] for e in data['entries'])
    if not scanned.issubset(set(ids)):
        errors.append('Video scansionati mancanti dal catalogo')
    for name in ['sources/VIDEO_INDEX.md', 'sources/queue/QUEUE.md']:
        lines = [line for line in (ROOT/name).read_text().splitlines() if re.match(r'\| \d+ \|', line)]
        if len(lines) != len(rows):
            errors.append('Conteggio righe errato: '+name)
        for row, line in zip(rows, lines):
            if row['id'] not in line or '| '+row['status']+' |' not in line:
                errors.append('Ordine/stato incoerente: '+name+' '+row['id'])
    for row in rows:
        if row['status'] not in ['DA STUDIARE', 'DA RIVEDERE', 'STUDIATO', 'ESCLUSO']:
            errors.append('Stato sconosciuto: '+row['id'])
        if not (ROOT/'merenda'/row['category']/'README.md').exists():
            errors.append('Categoria inesistente: '+row['id'])
        if row['priority'] not in [1, 2, 3]:
            errors.append('Priorità errata: '+row['id'])
        if row['status'] == 'ESCLUSO' and not row.get('notes'):
            errors.append('Esclusione senza motivo: '+row['id'])
        if row['status'] == 'STUDIATO':
            for ext in ['md', 'review.md']:
                if not (ROOT/f'sources/transcripts/{row["id"]}.{ext}').exists():
                    errors.append('Documentazione mancante: '+row['id'])
    for folder in ['merenda', 'sources/transcripts']:
        for path in (ROOT/folder).rglob('*.md'):
            content = path.read_text()
            if folder == 'merenda' and re.search('formalife', content, re.I):
                errors.append('Contaminazione KB: '+str(path))
            for target in re.findall(r'\]\(([^)]+)\)', content):
                if '://' not in target and not target.startswith('#'):
                    if not (path.parent/target.split('#')[0]).exists():
                        errors.append('Link locale rotto: '+str(path)+' → '+target)
    done = sum(r['status'] == 'STUDIATO' for r in rows)
    remaining = sum(r['status'] not in ['STUDIATO', 'ESCLUSO'] for r in rows)
    status = (ROOT/'STATUS.md').read_text()
    for label, count in [('Video individuati', len(rows)), ('Video completati', done), ('Video rimanenti', remaining)]:
        if f'- {label}: {count}\n' not in status:
            errors.append('Contatore STATUS errato: '+label)
    if errors:
        raise SystemExit('\n'.join(errors))
    print(f'OK: {len(rows)} video, {done} completati, {remaining} pendenti; file congelati e link coerenti.')
    print('Il controllo strutturale non certifica lettura, qualità del merge o analisi visuale.')

if __name__ == '__main__':
    main()
