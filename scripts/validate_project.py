#!/usr/bin/env python3
"""Controlli offline finali: frozen, corpus video storico, nuove fonti Merenda, routing, lock, link e contatori."""
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
NEW_SOURCE_ROOT = ROOT / 'sources' / 'merenda-sources'
NEW_SOURCE_CATALOG = NEW_SOURCE_ROOT / 'catalog.json'

SOURCE_TYPES = {
    'video', 'audio', 'podcast', 'interview', 'article', 'blog',
    'newsletter', 'webpage', 'pdf', 'document', 'transcript',
    'webinar', 'course', 'post', 'other',
}
SOURCE_STATUSES = {'DA STUDIARE', 'STUDIATO', 'ESCLUSO'}


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


def validate_new_sources(errors):
    if not NEW_SOURCE_CATALOG.exists():
        errors.append('Catalogo nuove fonti mancante: sources/merenda-sources/catalog.json')
        return []

    try:
        rows = json.loads(NEW_SOURCE_CATALOG.read_text())
    except json.JSONDecodeError as exc:
        errors.append('Catalogo nuove fonti non valido: ' + str(exc))
        return []

    if not isinstance(rows, list):
        errors.append('Catalogo nuove fonti deve essere una lista JSON')
        return []

    ids = []
    required = {
        'id', 'type', 'title', 'author_or_speaker', 'source_ref',
        'published_date', 'acquired_date', 'origin', 'status',
        'normalized_path', 'review_path', 'category',
        'weighted_novelty', 'notes',
    }

    for row in rows:
        if not isinstance(row, dict):
            errors.append('Record nuova fonte non è un oggetto JSON')
            continue

        missing = sorted(required - set(row))
        ident = str(row.get('id', '<senza-id>'))
        if missing:
            errors.append(f'Campi mancanti nuova fonte {ident}: ' + ','.join(missing))
            continue

        ids.append(row['id'])

        if not re.fullmatch(r'FM-SRC-\d{4}', row['id']):
            errors.append('ID nuova fonte non valido: ' + row['id'])
        if row['type'] not in SOURCE_TYPES:
            errors.append('Tipo nuova fonte sconosciuto: ' + row['id'])
        if row['status'] not in SOURCE_STATUSES:
            errors.append('Stato nuova fonte sconosciuto: ' + row['id'])
        if not str(row['title']).strip():
            errors.append('Titolo nuova fonte mancante: ' + row['id'])
        if not str(row['author_or_speaker']).strip():
            errors.append('Attribuzione nuova fonte mancante: ' + row['id'])
        if not str(row['source_ref']).strip():
            errors.append('Riferimento nuova fonte mancante: ' + row['id'])
        if not str(row['acquired_date']).strip():
            errors.append('Data acquisizione nuova fonte mancante: ' + row['id'])
        if not str(row['origin']).strip():
            errors.append('Origine nuova fonte mancante: ' + row['id'])

        source_ref = row['source_ref']
        if isinstance(source_ref, str) and source_ref.startswith('sources/'):
            if not (ROOT / source_ref).exists():
                errors.append('File sorgente nuova fonte mancante: ' + row['id'])

        if row['status'] in {'STUDIATO', 'ESCLUSO'}:
            review_path = row['review_path']
            if not review_path or not (ROOT / review_path).exists():
                errors.append('Review nuova fonte mancante: ' + row['id'])

        if row['status'] == 'STUDIATO':
            normalized_path = row['normalized_path']
            if not normalized_path or not (ROOT / normalized_path).exists():
                errors.append('Contenuto normalizzato nuova fonte mancante: ' + row['id'])

            category = row['category']
            if not category or not (ROOT / 'merenda' / category / 'README.md').exists():
                errors.append('Categoria nuova fonte inesistente: ' + row['id'])

            if row['weighted_novelty'] not in [0, 1, 2]:
                errors.append('Weighted Novelty nuova fonte errata: ' + row['id'])

        if row['status'] == 'ESCLUSO' and (row['notes'] is None or not str(row['notes']).strip()):
            errors.append('Esclusione nuova fonte senza motivo: ' + row['id'])

    if len(ids) != len(set(ids)):
        errors.append('ID duplicati nel catalogo nuove fonti')

    return rows


def main():
    errors = []

    for name in FROZEN:
        original = subprocess.check_output(
            ['git', 'show', FROZEN_BASELINE_REF + ':' + name],
            cwd=ROOT,
        )
        if original != (ROOT / name).read_bytes():
            errors.append('File congelato modificato: ' + name)

    # Corpus video storico: invarianti legacy.
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
        errors.append('next-batch.txt non vuoto nonostante acquisizione video chiusa')

    queue_records = parsed.get('queue', {})
    if queue_records:
        for ident, item in queue_records.items():
            pos = item['position']
            if pos <= 313 and item['status'] not in ['STUDIATO', 'ESCLUSO']:
                errors.append(f'Posizione {pos} non chiusa: {ident}')
            if pos >= 314 and item['status'] != 'DA STUDIARE':
                errors.append(f'Residuo {pos} non è DA STUDIARE: {ident}')

    new_sources = validate_new_sources(errors)

    for folder in ['merenda', 'sources/transcripts', 'sources/merenda-sources']:
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

    new_done = sum(r.get('status') == 'STUDIATO' for r in new_sources if isinstance(r, dict))
    new_excluded = sum(r.get('status') == 'ESCLUSO' for r in new_sources if isinstance(r, dict))
    new_pending = sum(r.get('status') == 'DA STUDIARE' for r in new_sources if isinstance(r, dict))

    status_text = (ROOT / 'STATUS.md').read_text()

    counters = [
        ('Video individuati', len(rows)),
        ('Video completati', done),
        ('Video esclusi', excluded),
        ('Video rimanenti', remaining),
        ('Processati semanticamente', processed_count),
        ('Nuove fonti Merenda registrate', len(new_sources)),
        ('Nuove fonti Merenda studiate', new_done),
        ('Nuove fonti Merenda escluse', new_excluded),
        ('Nuove fonti Merenda da processare', new_pending),
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
    print('Acquisizione YouTube Merenda LOCKED; queue/index/catalog/review/frozen/link coerenti.')
    print(
        f'Nuove fonti Merenda: {len(new_sources)} registrate '
        f'({new_done} STUDIATO + {new_excluded} ESCLUSO, {new_pending} da processare).'
    )
    print('Il controllo strutturale non certifica il merito della revisione semantica.')


if __name__ == '__main__':
    main()
