# Manual Project Status

## Stato generale

**ACTIVE — FASE 7 / AUDIT GLOBALE DEL MANUALE**

Le Fasi 0–6 sono concluse. Il draft reader-facing completo è presente sul branch `manual-drafting-2026-09-20`: **8 parti / 39 capitoli**.

## Baseline e freshness

Baseline dottrinale iniziale: `93f8eae978fdffb55c5623ae06603e5895b71e11` — 2026-09-20.

Per audit e correzioni rileggere sempre la versione corrente del branch e i nodi canonici live quando emerge un dubbio dottrinale.

## Decisioni correnti

- **D-001 CURRENT:** `manual/` è publishing layer; `merenda/` resta canonico.
- **D-002 CURRENT:** beginner-first.
- **D-003 CURRENT:** voce reader-facing agnostica, senza Frank/Merenda/KB/Layer 1.
- **D-004 CURRENT:** provenance e temporal precedence preservate nel backend.
- **D-005 CURRENT:** rewrite, not collage.
- **D-006 SATISFIED:** drafting massivo completato dopo PASS delle Fasi 1–5.
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
- **Fase 6 — DONE / LOCAL PASS:** 39/39 capitoli draftati; tutte le otto parti hanno superato mini-audit locale senza finding P0/P1.

## Draft completo

1. Parte I — Capp. 1–4 — `manual/draft/part-01-fondamenti.md` — READY
2. Parte II — Capp. 5–8 — `manual/draft/part-02-mercato.md` — READY
3. Parte III — Capp. 9–13 — `manual/draft/part-03-posizionamento-offerta.md` — READY
4. Parte IV — Capp. 14–19 — `manual/draft/part-04-domanda-acquisizione.md` — READY
5. Parte V — Capp. 20–24 — `manual/draft/part-05-copy-vendita.md` — READY
6. Parte VI — Capp. 25–29 — `manual/draft/part-06-lifecycle-brand.md` — READY
7. Parte VII — Capp. 30–35 — `manual/draft/part-07-economics-organizzazione.md` — READY
8. Parte VIII — Capp. 36–39 — `manual/draft/part-08-crescita-capstone.md` — READY

### Gate locali Part VII

PASS: LTV letto come margine/probabilità e non ricavo; payback separato dal cash-conversion timing; capacity su vincoli/picchi/costo opportunità; process-first before software; hiring after bottleneck/economics; delegation/transferability su KPI, decision rights e asset control.

### Gate locali Part VIII

PASS: prototipo economico prima della struttura; prevendita/manual delivery trasparenti; reinvestimento distinto dalla spesa; capitale esterno trattato insieme a governance/control; espansione subordinata alla prova del core; nuova geografia/categoria riapre market/positioning; Cap. 39 funziona come router diagnostico e include gli otto symptom routers previsti.

## Fase attiva — Fase 7 / Audit globale

Audit richiesto su:

- coverage 39/39 e rispetto delle chapter specs;
- doctrine fidelity e temporal precedence;
- beginner clarity e first-use definitions;
- causalità e prerequisite order;
- operational usability;
- ridondanza e primary-home discipline;
- casi, numeri, prove e caveat;
- provenance/copyright e assenza di backend reader-facing;
- terminologia, voce e inglesismi;
- cross-reference fra capitoli/parti.

Output previsto dal roadmap: `manual/AUDIT.md`.

Gate: **nessun finding P0/P1 aperto**.

## Finding già noti da verificare globalmente

- **P2:** uniformare/italianizzare gli inglesismi non necessari (`advocacy`, nomi di alcuni canvas, economics/operations terminology dove esiste un equivalente chiaro).
- **P2:** piccoli refusi e uniformità lessicale nelle Parti II, V, VI e VII.
- **P2 candidate:** verificare nel Cap. 30 che la regola “una spesa è investimento solo se esiste ritorno causale plausibile” sia abbastanza esplicita come primary teaching point, non solo distribuita nei capitoli successivi.

## Next Action

Eseguire Fase 7 sul manoscritto completo e scrivere `manual/AUDIT.md`; correggere eventuali P0/P1 sul draft prima di dichiarare PASS.

## Blocchi

Nessun blocco corrente.

## Handoff obbligatorio

`ROADMAP.md` → `STATUS.md` → `MANUAL_CONTRACT.md` → `MANUAL_CURRICULUM.md` → `MANUAL_GAPS.md` → `BEGINNER_GLOSSARY.md` → chapter specs → draft corrente → nodi canonici live/provenance quando necessario.
