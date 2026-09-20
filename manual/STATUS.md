# Manual Project Status

## Stato generale

**ACTIVE — FASE 6 / DRAFTING DEL MANUALE**

Le fasi 0–5 sono concluse, auditate e pronte per il checkpoint su `main`. Il progetto può ora produrre prosa reader-facing senza dipendere da conoscenza implicita o da decisioni editoriali lasciate in chat.

## Baseline e freshness

Baseline dottrinale iniziale del progetto manuale: `93f8eae978fdffb55c5623ae06603e5895b71e11` — 2026-09-20.

Prima di ogni blocco sostanziale di drafting va verificato il `main` live e vanno riletti i nodi canonici pertinenti.

## Decisioni correnti

- **D-001 CURRENT — Publishing layer separato:** `manual/` organizza e riscrive; `merenda/` resta doctrine layer canonico.
- **D-002 CURRENT — Beginner-first:** prerequisiti e termini precedono l'uso operativo.
- **D-003 CURRENT — Voce autoriale agnostica:** niente Frank Merenda, KB, Layer 1 o provenance interna nel reader-facing.
- **D-004 CURRENT — Provenance backend:** origine reale, fonti assimilate, caveat e temporal precedence restano tracciati.
- **D-005 CURRENT — Rewrite, not collage:** nuova prosa, non concatenazione di nodi.
- **D-006 SATISFIED — Gate prima della scrittura massiva:** Fasi 1–5 superate.
- **D-007 CURRENT — Crosswalk modulare:** 60/60 file canonici coperti.
- **D-008 CURRENT — VoC multi-fonte:** sintesi in `manual/syntheses/voice-of-customer.md`.
- **D-009 CURRENT — Front-end = riduzione della barriera:** low price è solo una possibile implementazione.
- **D-010 CURRENT — Economics progressive disclosure:** Cap. 2 literacy minima; Capp. 30–32 approfondimento.
- **D-011 CURRENT — Curriculum:** 8 parti / 39 capitoli; Cap. 39 ricompone il sistema diagnostico.

## Fasi completate

- **Fase 0 — DONE:** control plane e baseline.
- **Fase 1 — DONE:** 60/60 file censiti.
- **Fase 2 — DONE / PASS:** 60/60 file covered; 709 unità semantiche; dedup/primary-home/dependency/provenance/cases completati. Audit: `PHASE2_AUDIT.md`.
- **Fase 3 — DONE / PASS:** 8 parti / 39 capitoli; D-01…D-35 verificati; G-006 risolto. Audit: `PHASE3_AUDIT.md`.
- **Fase 4 — DONE / PASS:** VoC, glossary e synthetic cases; G-001…G-008 `RESOLVED EDITORIALLY`; nessun doctrinal escalation. Audit: `PHASE4_AUDIT.md`.
- **Fase 5 — DONE / PASS:** 39/39 chapter specs; prerequisite, primary-home, first-use, metriche, casi e backend verificati. Audit: `PHASE5_AUDIT.md`.

## Fase attiva — Fase 6 / Drafting

Ordine:

1. Parte I — Capp. 1–4 — **NEXT**;
2. Parte II — Capp. 5–8;
3. Parte III — Capp. 9–13;
4. Parte IV — Capp. 14–19;
5. Parte V — Capp. 20–24;
6. Parte VI — Capp. 25–29;
7. Parte VII — Capp. 30–35;
8. Parte VIII — Capp. 36–39.

## Next Action

Creare `manual/draft/part-01-fondamenti.md` seguendo `manual/chapter-specs/part-01-fondamenti.md`, quindi eseguire un mini-audit locale prima della Parte II.

Vincoli della Parte I:

- termini definiti al first use;
- economics solo al livello previsto dal Cap. 2;
- niente anticipazioni profonde di mercato/positioning/offerta;
- esempi come strumenti didattici, non benchmark;
- nessuna esposizione del backend.

## Gap aperti

**Nessun gap P0/P1/P2 corrente.**

## Blocchi

Nessun blocco corrente.

## Handoff obbligatorio

Leggere in ordine: `ROADMAP.md` → `STATUS.md` → `MANUAL_CONTRACT.md` → `MANUAL_CURRICULUM.md` → `MANUAL_GAPS.md` → `BEGINNER_GLOSSARY.md` → chapter spec attiva → nodi canonici live → `PROVENANCE_MAP.md` se sensibile.

Aggiornare questo file dopo ogni blocco di drafting.