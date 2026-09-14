#!/usr/bin/env python3
"""Checkpoint 200 — classificazione strategica A/B/C dei contenuti residui (201-468).

Non modifica lo stato dei contenuti (restano DA STUDIARE). Produce solo un
artefatto di pianificazione in reviews/RESIDUAL_CLASSIFICATION_201-468.md,
usato dal checkpoint FASE 14+15 per proporre un workflow differenziato.

Criteri (vedi checkpoint per motivazione estesa):
- Formato (short/stream/video) e categoria come segnali di partenza, non regole assolute.
- Titoli con struttura numerata/framework ("N passi/steps/modi/leve/regole/segreti/
  checklist/formula/metodo/sistema") spingono verso A.
- Categorie 07_copy_comunicazione e 08_brand: blocco piccolo, alta densità attesa
  (indicazione esplicita di governance) -> default A per i video lunghi.
- Casi studio su grandi brand esterni notissimi (probabile illustrazione di dottrina
  già consolidata) -> default C. Casi su PMI/aziende specifiche italiane -> default B.
- Contenuti motivazionali/polemici/mindset generico o fiscali senza trasferibilità
  -> default C.
- Shorts -> default C (coerente con 0/9 incrementali osservato nel batch 176-184),
  MAI saltati: restano da studiare con revisione rapida.
"""
import json
import re
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

FRAMEWORK_RE = re.compile(
    r'\b\d+\s*(passi|steps|modi|modalit[aà]|fasi|leve|principi|regole|segreti|strategie|tecniche|domande|condizioni|chiavi|errori)\b',
    re.I,
)
CHECKLIST_RE = re.compile(r'checklist|formula|framework|metodo|sistema completo|guida completa|complete guide|key (concepts|strategies)', re.I)

VENDITA_HIGH = re.compile(
    r'preventiv|testimonial|follow-?up|script|autorit|post-?vendita|provvigion|remunerazion|'
    r'rete vendita|qualificaz|closing|chius|obiezion|decisor|venditor',
    re.I,
)
BUSINESS_HIGH = re.compile(
    r'\bcac\b|\bltv\b|lifetime value|cash ?flow|cassa|margin|organigramma|deleg|recruiting|'
    r'crm|stagionalit|\bexit\b|franchising|controllo di gestione|capacit[aà]|scalabilit|roi',
    re.I,
)
MOTIVATIONAL_LOW = re.compile(
    r'mentalit[aà] vincente|mindset|\bscam\b|truffa|\bguru\b|\bfisco\b|\btasse\b|dan kennedy svela|rich mentality',
    re.I,
)
BIG_EXTERNAL_BRAND = re.compile(
    r'ferragni|balocco|coca[ -]?cola|\btesla\b|sneakers|\bthé\b|briatore|sorbillo|mcdonald|\bapple\b|\bamazon\b|\bdyson\b|\bnutella\b|\bbarilla\b|\bperlana\b',
    re.I,
)

def classify(row):
    title = row['title']
    fmt = row['tabs'][0]
    cat = row['category']
    reasons = []

    if MOTIVATIONAL_LOW.search(title):
        reasons.append('contenuto motivazionale/mindset/polemico/fiscale generico')
        return 'C', reasons

    if cat in ('07_copy_comunicazione', '08_brand') and fmt != 'shorts':
        reasons.append(f'blocco {cat} piccolo e ad alta densità attesa (indicazione di governance)')
        return 'A', reasons

    if FRAMEWORK_RE.search(title) or CHECKLIST_RE.search(title):
        reasons.append('titolo con struttura numerata/framework/checklist: alta probabilità di procedura riutilizzabile')
        return 'A', reasons

    if cat == '06_vendita' and VENDITA_HIGH.search(title):
        reasons.append('area vendita segnalata come poco satura (preventivi/testimonial/follow-up/script/qualificazione/closing)')
        return 'A', reasons

    if cat == '09_business' and BUSINESS_HIGH.search(title):
        reasons.append('area business segnalata come poco satura (numeri/cassa/CAC/LTV/organigramma/delega/CRM/exit/franchising)')
        return 'A', reasons

    if cat == '10_casi_studio':
        if BIG_EXTERNAL_BRAND.search(title):
            reasons.append('caso su grande brand esterno notissimo: alta probabilità di illustrare dottrina già consolidata')
            return 'C', reasons
        reasons.append('caso applicativo su azienda specifica: probabile ma non certo consolidamento di dottrina esistente')
        return 'B', reasons

    if fmt == 'shorts':
        reasons.append('formato short: alta probabilità di derivare da un video già in coda/già studiato (0/9 incrementali nel campione 176-184)')
        return 'C', reasons

    if fmt == 'streams':
        reasons.append('live/stream generico: alta probabilità di Q&A o commento estemporaneo a bassa densità dottrinale nuova')
        return 'C', reasons

    reasons.append('video lungo in area operativa senza segnali forti né di alta né di bassa densità')
    return 'B', reasons


def main():
    rows = json.loads((ROOT / 'sources/catalog.json').read_text())
    residual = [r for r in rows if r['status'] == 'DA STUDIARE']
    residual_ids = {r['id'] for r in residual}
    by_id = {r['id']: r for r in residual}

    # segue l'ordine reale di lavorazione in sources/queue/QUEUE.md, non l'ordine del catalogo
    queue_text = (ROOT / 'sources/queue/QUEUE.md').read_text()
    queue_order = re.findall(r'\[([^\]]+)\]\(https://www\.youtube\.com/watch\?v=', queue_text)
    order = [vid for vid in queue_order if vid in residual_ids]
    missing = [vid for vid in residual_ids if vid not in order]
    if missing:
        order.extend(missing)  # fallback di sicurezza, non dovrebbe accadere

    classified = []
    for vid in order:
        row = by_id[vid]
        klass, reasons = classify(row)
        classified.append((row, klass, reasons))

    counts = Counter(k for _, k, _ in classified)
    cat_counts = Counter((r['category'], k) for r, k, _ in classified)

    lines = []
    lines.append('# Classificazione strategica A/B/C — contenuti residui 201–468')
    lines.append('')
    lines.append('Artefatto prodotto al checkpoint 200 (FASE 14 + FASE 15).')
    lines.append('')
    lines.append('**Non modifica lo stato di alcun contenuto.** Tutti i 268 contenuti restano `DA STUDIARE` e dovranno comunque ricevere transcript, revisione, categoria finale e stato (`STUDIATO` o `ESCLUSO` motivato) quando processati da ChatGPT/Codex nei batch successivi. La classificazione stabilisce solo la **profondità iniziale suggerita** della revisione semantica, secondo le regole descritte in `scripts/classify_residual.py` e nel checkpoint.')
    lines.append('')
    lines.append('## Riepilogo')
    lines.append('')
    lines.append(f'- Totale residuo: {len(classified)}')
    for k in ['A', 'B', 'C']:
        n = counts.get(k, 0)
        pct = round(100 * n / len(classified))
        lines.append(f'- {k}: {n} ({pct}%)')
    lines.append('')
    lines.append('## Per categoria')
    lines.append('')
    lines.append('| Categoria | A | B | C | Totale |')
    lines.append('|---|---:|---:|---:|---:|')
    cats = sorted({r['category'] for r, _, _ in classified})
    for cat in cats:
        a = cat_counts.get((cat, 'A'), 0)
        b = cat_counts.get((cat, 'B'), 0)
        c = cat_counts.get((cat, 'C'), 0)
        lines.append(f'| {cat} | {a} | {b} | {c} | {a+b+c} |')
    lines.append('')
    lines.append('## Lista completa')
    lines.append('')
    lines.append('| ID | Categoria | Formato | Classe | Titolo | Motivazione |')
    lines.append('|---|---|---|:---:|---|---|')
    for row, klass, reasons in classified:
        title = row['title'].replace('|', '\\|')
        lines.append(f"| {row['id']} | {row['category']} | {row['tabs'][0]} | {klass} | {title} | {'; '.join(reasons)} |")

    out = ROOT / 'reviews/RESIDUAL_CLASSIFICATION_201-468.md'
    out.write_text('\n'.join(lines) + '\n')
    print(f'Scritto {out} — A={counts.get("A",0)} B={counts.get("B",0)} C={counts.get("C",0)}')

if __name__ == '__main__':
    main()
