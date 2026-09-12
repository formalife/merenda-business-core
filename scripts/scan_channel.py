#!/usr/bin/env python3
"""Censisce le tre schede pubbliche; genera catalogo e queue senza perdere stati."""
import argparse
import datetime as dt
import json
from pathlib import Path
import subprocess

ROOT = Path(__file__).resolve().parents[1]
CHANNEL = 'https://www.youtube.com/@FrankMerendaTV'
CHANNEL_ID = 'UCaAzr7bvYcZRfGR8EyBynOA'
SECTIONS = ['00_fondamenti', '01_mercato', '02_posizionamento', '03_offerta', '04_marketing', '05_acquisizione', '06_vendita', '07_copy_comunicazione', '08_brand', '09_business', '10_casi_studio']
RULES = [(10, ['vlog', 'case history', 'caso studio', 'gelateria', 'cammi gomme', 'europa 92', 'le iene', 'posta power']), (5, ['landing page', 'front-end', 'front end', 'traffic', 'google ads', 'campagne online', 'referral', 'trovare i clienti', 'get clients']), (6, ['preventivo', 'non convertiti']), (9, ['tasse', 'fisco', 'investimento', 'entrepreneur', 'company', 'e-commerce', 'guadagnare']), (7, ['copy', 'comunicaz']), (2, ['position', 'posizion', 'differenz', 'focus']), (3, ['offert', 'offer', 'prezz', 'pric']), (5, ['funnel', 'lead', 'acquisi', 'advertis', 'pubblicit']), (6, ['vendit', 'sales', 'sell', 'vendere', 'negozi']), (1, ['mercato', 'market research', 'nicchia', 'target']), (8, ['brand']), (10, ['vlog', 'case history', 'caso studio']), (9, ['business', 'imprend', 'azienda', 'aziende', 'deleg', 'employee']), (4, ['marketing'])]
FIRST = 'iR0e4AgmAGE'

def classify(title):
    t = title.lower()
    if any(x in t for x in ['principi inviolabili', 'fondamenti', 'fundamentals']):
        return SECTIONS[0]
    return next((SECTIONS[n] for n, words in RULES if any(w in t for w in words)), SECTIONS[4])

def cell(value):
    return str(value).replace('|', '&#124;').replace('\n', ' ')

def render(rows):
    intro = '# VIDEO INDEX\n\nCatalogo del canale ufficiale `@FrankMerendaTV`. Dati dalla scansione delle schede videos, shorts e streams.\n\nClassificazione preliminare euristica sul titolo, da confermare con il transcript. Priorità 1 = fondamenti, 2 = percorso tematico, 3 = Shorts. Date non disponibili nella scansione piatta: da acquisire prima di valutare contraddizioni; nessuna cronologia dedotta dalla queue.\n\nStati: `DA STUDIARE`, `STUDIATO`, `DA RIVEDERE`, `ESCLUSO` (con motivo).\n\n| Ordine | Video ID | Data | Titolo | Durata (s) | Categoria preliminare | Priorità | Stato | Note |\n|---:|---|---|---|---:|---|---:|---|---|\n'
    queue = '# LEARNING QUEUE\n\nPrendere il primo video non completato. Fermarsi ogni 25 completati per checkpoint Claude (anche audit ogni 50).\n\nOrdine: corso sui sette principi, fondamenti, poi mercato → posizionamento → offerta → marketing → acquisizione → vendita → comunicazione → brand → business → casi studio; Shorts in coda. Entro categoria si mantiene l’ordine restituito dalla scheda. Il titolo non costituisce conoscenza acquisita.\n\n| Ordine | Video | Categoria preliminare | Stato |\n|---:|---|---|---|\n'
    for n, r in enumerate(rows, 1):
        url = 'https://www.youtube.com/watch?v=' + r['id']
        intro += '| ' + ' | '.join(map(cell, [n, r['id'], r.get('upload_date') or 'da acquisire', f'[{r["title"]}]({url})', r.get('duration') or 'n.d.', r['category'], r['priority'], r['status'], ', '.join(r['tabs']) + ('; '+r['notes'] if r.get('notes') else '')])) + ' |\n'
        queue += f'| {n} | [{r["id"]}]({url}) — {cell(r["title"])} | {r["category"]} | {r["status"]} |\n'
    (ROOT/'sources/VIDEO_INDEX.md').write_text(intro)
    (ROOT/'sources/queue/QUEUE.md').write_text(queue)

def main():
    p = argparse.ArgumentParser()
    p.add_argument('--from-cache', action='store_true', help='Usa le tre scansioni in work/ senza rete')
    args = p.parse_args()
    db = ROOT/'sources/catalog.json'
    old = json.loads(db.read_text()) if db.exists() else []
    rows = {r['id']: r for r in old}
    counts = {}
    for tab in ['videos', 'shorts', 'streams']:
        path = ROOT/f'work/channel-{tab}.json'
        if not args.from_cache:
            result = subprocess.run(['yt-dlp', '--flat-playlist', '--dump-single-json', '--skip-download', '--socket-timeout', '20', '--retries', '1', CHANNEL+'/'+tab], capture_output=True, text=True)
            if result.returncode:
                raise SystemExit(result.stderr)
            json.loads(result.stdout)
            path.write_text(result.stdout)
        data = json.loads(path.read_text())
        if data.get('channel_id') != CHANNEL_ID:
            raise SystemExit(f'Canale inatteso: {path}')
        counts[tab] = len(data['entries'])
        for entry in data['entries']:
            ident = entry['id']
            if ident not in rows:
                cat = classify(entry['title'])
                rows[ident] = dict(id=ident, title=entry['title'], duration=entry.get('duration'), upload_date=entry.get('upload_date'), category=cat, priority=3 if tab == 'shorts' else (1 if cat == SECTIONS[0] else 2), status='DA STUDIARE', tabs=[], notes='')
            if tab not in rows[ident]['tabs']:
                rows[ident]['tabs'].append(tab)
    # Non riordinare una queue già avviata.
    ordered = list(rows.values())
    if not old:
        ordered.sort(key=lambda r: (r['id'] != FIRST, r['priority'], SECTIONS.index(r['category'])))
    db.write_text(json.dumps(ordered, ensure_ascii=False, indent=2)+'\n')
    render(ordered)
    report = dict(scanned_at=dt.datetime.now(dt.timezone.utc).isoformat(), channel_id=CHANNEL_ID, channel_url=CHANNEL, tab_counts=counts, unique_videos=len(rows), limits=['Solo video pubblicamente elencati nelle tre schede; privati, eliminati e non in elenco non censibili.', 'Date esatte non restituite dalla scansione piatta; acquisizione per video prima del merge.', 'Titoli restituiti da YouTube talvolta localizzati in inglese.'])
    (ROOT/'sources/scan-report.json').write_text(json.dumps(report, ensure_ascii=False, indent=2)+'\n')
    print(json.dumps(report, ensure_ascii=False))

if __name__ == '__main__':
    main()
