# Manual Project Status

## Stato generale

**ACTIVE — FASE 6 / DRAFTING DEL MANUALE**

Le fasi di architettura, coverage, curriculum, gap closure e chapter specs sono concluse e auditate. Il progetto può ora produrre prosa reader-facing senza dipendere da conoscenza implicita o da decisioni editoriali lasciate in chat.

## Baseline e freshness

Baseline dottrinale iniziale del progetto manuale:

`93f8eae978fdffb55c5623ae06603e5895b71e11`

Data baseline iniziale: 2026-09-20.

Le Fasi 0–5 sono consolidate nel checkpoint Git validato immediatamente precedente al drafting della Parte I.

Prima di ogni blocco sostanziale di drafting va verificato il `main` live e vanno riletti i nodi canonici pertinenti.

## Decisioni correnti

### D-001 — Publishing layer separato
**CURRENT** — `manual/` organizza e riscrive; `merenda/` resta doctrine layer canonico.

### D-002 — Beginner-first
**CURRENT** — prerequisiti e termini precedono l'uso operativo.

### D-003 — Voce autoriale agnostica
**CURRENT** — il testo reader-facing non cita Frank Merenda, la KB, Layer 1 o provenance interna.

### D-004 — Provenance preservata nel backend
**CURRENT** — origine reale, fonti assimilate, caveat e temporal precedence restano tracciati editorialmente.

### D-005 — Rewrite, not collage
**CURRENT** — la prosa viene riscritta da zero.

### D-006 — Gate prima della scrittura massiva
**SATISFIED** — Fasi 1–5 hanno superato i rispettivi gate.

### D-007 — Crosswalk modulare
**CURRENT** — 60/60 file canonici coperti.

### D-008 — Ricerca di mercato come evidenza multi-fonte
**CURRENT / VALIDATED EDITORIALLY** — sintesi: `manual/syntheses/voice-of-customer.md`.

### D-009 — Front-end definito dalla barriera, non dal prezzo
**CURRENT** — prezzo basso è soltanto una possibile implementazione.

### D-010 — Economics in progressive disclosure
**CURRENT** — Cap. 2 literacy minima; Capp. 30–32 approfondimento.

### D-011 — Curriculum definitivo di lavoro
**CURRENT** — 8 parti, 39 capitoli, Cap. 39 come operating system diagnostico.

## Fasi completate

### Fase 0 — DONE
Control plane e baseline creati.

### Fase 1 — DONE
**60/60** file censiti; corpus interpretativo/provenance separato.

### Fase 2 — DONE / PASS
**60/60 file covered; 709 unità semantiche first-pass**; deduplication, primary-home, dependency, provenance e case inventory completati. Audit: `manual/PHASE2_AUDIT.md`.

### Fase 3 — DONE / PASS
`MANUAL_CURRICULUM.md`: **8 parti / 39 capitoli**; D-01…D-35 verificati; G-006 risolto. Audit: `manual/PHASE3_AUDIT.md`.

### Fase 4 — DONE / PASS
VoC synthesis, beginner glossary, case inventory + sei casi sintetici; G-001…G-008 tutti `RESOLVED EDITORIALLY`; nessun doctrinal escalation. Audit: `manual/PHASE4_AUDIT.md`.

### Fase 5 — DONE / PASS
Otto file di chapter specs; **39/39 capitoli con spec**; prerequisite, primary-home, first-use, metriche/evidenza, casi e backend sources verificati. Audit: `manual/PHASE5_AUDIT.md`.

## Fase attiva

### Fase 6 — Drafting

Obiettivo: produrre nuova prosa autoriale, coerente e studiabile, aderente alle specs e indipendente dalla struttura originale della KB.

## Ordine operativo corrente

1. Parte I — Capp. 1–4 — **NEXT**;
2. Parte II — Capp. 5–8;
3. Parte III — Capp. 9–13;
4. Parte IV — Capp. 14–19;
5. Parte V — Capp. 20–24;
6. Parte VI — Capp. 25–29;
7. Parte VII — Capp. 30–35;
8. Parte VIII — Capp. 36–39.

## Next Action

Creare `manual/draft/part-01-fondamenti.md` seguendo `manual/chapter-specs/part-01-fondamenti.md`.

Vincoli:

- Capp. 1–4 in prosa reader-facing;
- termini definiti al first use;
- economics al solo livello previsto dal Cap. 2;
- niente anticipazioni profonde di mercato/positioning/offerta;
- casi ed esempi come strumenti didattici, non benchmark;
- chiusura operativa coerente con la spec;
- nessuna esposizione del backend.

Dopo la Parte I: mini-audit locale prima della Parte II.

## Gap aperti

**Nessun gap P0/P1/P2 corrente.**

## Blocchi

Nessun blocco corrente.

## Handoff obbligatorio

1. `manual/ROADMAP.md`;
2. questo file;
3. `manual/MANUAL_CONTRACT.md`;
4. `manual/MANUAL_CURRICULUM.md`;
5. `manual/MANUAL_GAPS.md`;
6. `manual/BEGINNER_GLOSSARY.md`;
7. chapter spec della parte attiva;
8. nodi canonici live necessari;
9. `PROVENANCE_MAP.md` quando sensibile.

Aggiornare questo file dopo ogni blocco di drafting.