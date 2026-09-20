# Manual Project Status

## Stato generale

**ACTIVE — FASE 6 / DRAFTING DEL MANUALE**

Le Fasi 0–5 sono concluse e auditate. Il drafting reader-facing è in corso sul branch `manual-drafting-2026-09-20`.

## Baseline e freshness

Baseline dottrinale iniziale: `93f8eae978fdffb55c5623ae06603e5895b71e11` — 2026-09-20.

Prima di ogni blocco sostanziale di drafting verificare `main` live e rileggere i nodi canonici pertinenti.

## Decisioni correnti

- **D-001 CURRENT:** `manual/` è publishing layer; `merenda/` resta canonico.
- **D-002 CURRENT:** beginner-first.
- **D-003 CURRENT:** voce reader-facing agnostica, senza Frank/Merenda/KB/Layer 1.
- **D-004 CURRENT:** provenance e temporal precedence preservate nel backend.
- **D-005 CURRENT:** rewrite, not collage.
- **D-006 SATISFIED:** drafting massivo autorizzato dopo PASS delle Fasi 1–5.
- **D-007 CURRENT:** 60/60 file canonici coperti.
- **D-008 CURRENT:** VoC multi-fonte consolidata in `syntheses/voice-of-customer.md`.
- **D-009 CURRENT:** front-end = riduzione della barriera, non sinonimo di low price.
- **D-010 CURRENT:** economics in progressive disclosure: Cap. 2 base, Capp. 30–32 avanzati.
- **D-011 CURRENT:** 8 parti / 39 capitoli; Cap. 39 = operating system diagnostico.

## Fasi completate

- **Fase 0 — DONE:** control plane e baseline.
- **Fase 1 — DONE:** 60/60 file censiti.
- **Fase 2 — DONE / PASS:** 60/60 covered; 709 unità semantiche; primary-home/dependency/provenance/cases completati.
- **Fase 3 — DONE / PASS:** curriculum 8 parti / 39 capitoli; D-01…D-35 verificati.
- **Fase 4 — DONE / PASS:** VoC, glossary, synthetic cases; G-001…G-008 risolti editorialmente.
- **Fase 5 — DONE / PASS:** 39/39 chapter specs.

## Fase attiva — Fase 6 / Drafting

### Parte I — Capp. 1–4

**Stato: READY / MINI-AUDIT PASS**

Output: `manual/draft/part-01-fondamenti.md`.

Copre:

- marketing come sistema di valore;
- economic literacy minima;
- diagnosi causa/sintomo/bottleneck;
- metodo di test e gate di scala.

Il pass beginner-first ha rimosso anticipazioni di gergo non necessario.

### Parte II — Capp. 5–8

**Stato: READY / MINI-AUDIT PASS CON P2 LESSICALI NON BLOCCANTI**

Output: `manual/draft/part-02-mercato.md`.

Copre:

- market gate: domanda, raggiungibilità, capacità di acquisto, direzione e bacino;
- cliente desiderabile: appropriatezza, economics, RFM, cost-to-serve e criteri di rifiuto;
- Voice of Customer decision-first, complaint mining, interviste event-based, triangolazione e Market Evidence Map;
- problema/desiderio, alternative, status quo, trigger, ruoli decisionali e durata naturale della relazione.

Mini-audit:

- coverage: PASS;
- doctrine fidelity: PASS;
- causal clarity: PASS;
- operational usability: PASS;
- economic grounding: PASS;
- reader-facing agnosticism: PASS;
- beginner clarity: PASS con piccoli inglesismi/etichette da uniformare nel copy-edit globale; nessun P0/P1.

## Ordine rimanente

1. Parte III — Capp. 9–13 — **NEXT**;
2. Parte IV — Capp. 14–19;
3. Parte V — Capp. 20–24;
4. Parte VI — Capp. 25–29;
5. Parte VII — Capp. 30–35;
6. Parte VIII — Capp. 36–39.

## Next Action

Draftare `manual/draft/part-03-posizionamento-offerta.md` da `chapter-specs/part-03-posizionamento-offerta.md` dopo freshness read dei nodi live di positioning e offer.

Vincoli principali:

- differenza reale prima del claim;
- focus/categoria prima delle estensioni;
- offerta distinta dal prodotto;
- front-end definito dalla barriera, non dal prezzo;
- pricing trattato come sistema conversione × margine × target × capacity, non come ideologia premium;
- nessuna anticipazione profonda di authority/acquisition/copy.

## Gap aperti

**Nessun gap P0/P1.**

P2 editoriali correnti: uniformare nel copy-edit globale alcuni inglesismi reader-facing non indispensabili nelle Parti I–II.

## Blocchi

Nessun blocco corrente.

## Handoff obbligatorio

`ROADMAP.md` → `STATUS.md` → `MANUAL_CONTRACT.md` → `MANUAL_CURRICULUM.md` → `MANUAL_GAPS.md` → `BEGINNER_GLOSSARY.md` → chapter spec attiva → nodi canonici live → `PROVENANCE_MAP.md` se sensibile.

Aggiornare questo file dopo ogni blocco di drafting.