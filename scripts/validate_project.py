#!/usr/bin/env python3
"""Controlli offline finali: frozen, corpus, routing, queue/index, lock, link e contatori."""
import json
from pathlib import Path
import re
import subprocess

ROOT = Path(__file__).resolve().parents[1]

# Commit della chiusura semantica a 313. I file frozen non sono stati modificati
# dalla successiva hardening operativa e vengono confrontati contro questo stato.
FROZEN_BASELINE_REF = 'e505ba63cc5befd38db11a222c2eb2ffa10fabfa'
FROZEN = [
    'MASTER_PLAN.md',
    'system/RULES.md',
    'system/PHASES.md',
    'system/HANDOFFS.md',
    'system/FROZEN_FILES.md',
]
LOCK = ROOT / 'sources' / 'queue' / 'ACQUISITION_CLOSED.md'
NEXT_BATCH = ROOT / 'sources' / 'queue' / 'next-batch.txt'


def parse_table(path, kind):
    lines = [line for line in path.read_text().splitlines() if re.match(r'\| \d+ \|', line)]
    records = {}
    positions = []

    for line in lines:
        parts = [part.strip() for part in line.split('|')]
        pos = int(parts[1])
        positions.append(pos)

        if kind == 'queue':
            m = re.match(r'\[([A-Za-z0-9_-]{11})\]\(', parts[2])
            if not m:
                raise ValueError(f'Riga queue non parsabile: {line}')
            ident = m.group(1)
            category = parts[3]
            status = parts[4]
        else:
            ident = parts[2]
            category = parts[6]
            status = parts[8]

        if ident in records:
            raise ValueError(f'ID duplicato in {path}: {ident}')
        records[ident] = {
            'position': pos,
            'category': category,
            'status': status,
        }

    return lines, records, positions


def main():
    errors = []

    for name in FROZEN:
        original = subprocess.check_output(
            ['git', 'show', FROZEN_BASELINE_REF + ':' + name],
            cwd=ROOT,
        )
        if original != (ROOT / name).read_bytes():
            errors.append('File congelato modificato: ' + name)

    rows = json.loads((ROOT / 'sources/catalog.json').read_text())
    ids = [r['id'] for r in rows]
    by_id = {r['id']: r for r in rows}

    if len(ids) != len(set(ids)):
        errors.append('ID duplicati nel catalogo')

    scanned = set()
    for tab in ['videos', 'shorts', 'streams']:
        data = json.loads((ROOT / f'work/channel-{tab}.json').read_text())
        if data['channel_id'] != 'UCaAzr7bvYcZRfGR8EyBynOA':
            errors.append('Canale errato: ' + tab)
        scanned.update(e['id'] for e in data['entries'])
    if not scanned.issubset(set(ids)):
        errors.append('Video scansionati mancanti dal catalogo')

    tables = [
        ('sources/VIDEO_INDEX.md', 'index'),
        ('sources/queue/QUEUE.md', 'queue'),
    ]
    parsed = {}

    for name, kind in tables:
        try:
            lines, records, positions = parse_table(ROOT / name, kind)
        except ValueError as exc:
            errors.append(str(exc))
            continue

        parsed[kind] = records

        if len(lines) != len(rows):
            errors.append('Conteggio righe errato: ' + name)
        if len(records) != len(rows):
            errors.append('Conteggio ID errato: ' + name)
        if set(records) != set(ids):
            missing = sorted(set(ids) - set(records))
            extra = sorted(set(records) - set(ids))
            if missing:
                errors.append('ID mancanti in ' + name + ': ' + ','.join(missing))
            if extra:
                errors.append('ID extra in ' + name + ': ' + ','.join(extra))
        if sorted(positions) != list(range(1, len(rows) + 1)):
            errors.append('Posizioni non contigue/univoche: ' + name)

        for ident, item in records.items():
            row = by_id.get(ident)
            if not row:
                continue
            if item['status'] != row['status']:
                errors.append(
                    f'Stato incoerente: {name} {ident} '
                    f'({item["status"]} != {row["status"]})'
                )
            if item['category'] != row['category']:
                errors.append(
                    f'Categoria incoerente: {name} {ident} '
                    f'({item["category"]} != {row["category"]})'
                )

    for row in rows:
        if row['status'] not in ['DA STUDIARE', 'DA RIVEDERE', 'STUDIATO', 'ESCLUSO']:
            errors.append('Stato sconosciuto: ' + row['id'])
        if not (ROOT / 'merenda' / row['category'] / 'README.md').exists():
            errors.append('Categoria inesistente: ' + row['id'])
        if row['priority'] not in [1, 2, 3]:
            errors.append('Priorità errata: ' + row['id'])
        if row['status'] == 'ESCLUSO' and not row.get('notes'):
            errors.append('Esclusione senza motivo: ' + row['id'])
        if row['status'] == 'STUDIATO':
            if not (ROOT / f'sources/transcripts/{row["id"]}.md').exists():
                errors.append('Transcript mancante: ' + row['id'])

    processed = {r['id'] for r in rows if r['status'] in ['STUDIATO', 'ESCLUSO']}
    review_files = list((ROOT / 'sources/transcripts').glob('*.review.md'))
    review_ids = {p.name[:-len('.review.md')] for p in review_files}
    if review_ids != processed:
        for ident in sorted(processed - review_ids):
            errors.append('Review mancante: ' + ident)
        for ident in sorted(review_ids - processed):
            errors.append('Review extra senza stato processato: ' + ident)

    if not LOCK.exists():
        errors.append('Lock acquisizione mancante: sources/queue/ACQUISITION_CLOSED.md')
    if NEXT_BATCH.read_text().strip():
        errors.append('next-batch.txt non vuoto nonostante acquisizione chiusa')

    queue_records = parsed.get('queue', {})
    if queue_records:
        for ident, item in queue_records.items():
            pos = item['position']
            if pos <= 313 and item['status'] not in ['STUDIATO', 'ESCLUSO']:
                errors.append(f'Posizione {pos} non chiusa: {ident}')
            if pos >= 314 and item['status'] != 'DA STUDIARE':
                errors.append(f'Residuo {pos} non è DA STUDIARE: {ident}')

    for folder in ['merenda', 'sources/transcripts']:
        for path in (ROOT / folder).rglob('*.md'):
            content = path.read_text()
            if folder == 'merenda' and re.search('formalife', content, re.I):
                errors.append('Contaminazione KB: ' + str(path))
            for target in re.findall(r'\]\(([^)]+)\)', content):
                if '://' not in target and not target.startswith('#'):
                    local = target.split('#')[0]
                    if local and not (path.parent / local).exists():
                        errors.append('Link locale rotto: ' + str(path) + ' → ' + target)

    done = sum(r['status'] == 'STUDIATO' for r in rows)
    excluded = sum(r['status'] == 'ESCLUSO' for r in rows)
    remaining = sum(r['status'] not in ['STUDIATO', 'ESCLUSO'] for r in rows)
    processed_count = done + excluded
    status_text = (ROOT / 'STATUS.md').read_text()

    counters = [
        ('Video individuati', len(rows)),
        ('Video completati', done),
        ('Video esclusi', excluded),
        ('Video rimanenti', remaining),
        ('Processati semanticamente', processed_count),
    ]
    for label, count in counters:
        if f'- {label}: {count}\n' not in status_text:
            errors.append('Contatore STATUS errato: ' + label)

    if errors:
        raise SystemExit('\n'.join(errors))

    print(
        f'OK: {len(rows)} video; {processed_count} processati '
        f'({done} STUDIATO + {excluded} ESCLUSO), {remaining} residui intenzionali.'
    )
    print('Acquisizione Merenda LOCKED; queue/index/catalog/review/frozen/link coerenti.')
    print('Il controllo strutturale non certifica il merito della revisione semantica.')


if __name__ == '__main__':
    main()
