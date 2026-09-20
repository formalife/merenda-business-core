# Manual Project Roadmap

## Objective

Trasformare l'intera conoscenza utile del doctrine layer in un manuale teorico-operativo coerente, progressivo e studiabile da un lettore che parte da zero nel marketing.

Il progetto ottimizza per:

- completezza semantica;
- ordine pedagogico;
- coerenza causale;
- applicabilità operativa;
- minima ridondanza;
- tracciabilità interna;
- indipendenza della prosa finale dalle fonti personali originarie.

## Non-obiettivi

Il progetto non deve:

- trasformare la tassonomia corrente della KB nell'indice del libro senza riesame;
- fare copy-paste o merge dei nodi;
- perdere provenance o prevalenza temporale;
- modificare la dottrina canonica per esigenze narrative;
- esporre il backend editoriale nel testo reader-facing;
- sacrificare prerequisiti per accorciare artificialmente il percorso.

---

# Fase 0 — Control plane e baseline

**Stato: DONE**

Output: `manual/README.md`, `manual/ROADMAP.md`, `manual/STATUS.md`, `manual/MANUAL_CONTRACT.md` e baseline iniziale.

Gate: il progetto può ripartire dal repository senza dipendere dalla chat.

---

# Fase 1 — Architecture Review e corpus inventory

**Stato: DONE**

Output: `manual/CORPUS_INVENTORY.md`, `manual/MANUAL_GAPS.md` iniziale.

Gate: **60/60 file** sotto `merenda/` censiti e classificati.

---

# Fase 2 — Semantic decomposition e KB-to-Manual Crosswalk

**Stato: DONE — PASS 2026-09-20**

Output principali: crosswalk modulari, `PRIMARY_HOME_MAP.md`, `DEPENDENCY_MAP.md`, `PROVENANCE_MAP.md`, `CASE_INVENTORY.md`, `PHASE2_AUDIT.md`.

Esito: **60/60 file covered; 709 unità semantiche first-pass; nessun doctrinal gap bloccante.**

---

# Fase 3 — Curriculum e architettura didattica

**Stato: DONE — PASS 2026-09-20**

Output: `MANUAL_CURRICULUM.md`, **8 parti / 39 capitoli**, prerequisite order, case placement, first-use terminology map, `PHASE3_AUDIT.md`.

Decisioni strutturali: economics minimi presto; VoC prima di positioning/copy; positioning prima di offer; brand distribuito causalmente; funnel come state machine; vendita dall'handoff; lifecycle unitario; scale subordinata a economics/cash/capacity/process/people; expansion riapre market/positioning.

---

# Fase 4 — Gap closure e sintesi mancanti

**Stato: DONE — PASS 2026-09-20**

Output: VoC synthesis, sei casi sintetici, beginner glossary, gap register aggiornato, `PHASE4_AUDIT.md`.

Esito: G-001…G-008 tutti `RESOLVED EDITORIALLY`; nessun gap P0/P1/P2 bloccante; nessuna modifica necessaria a `merenda/`.

---

# Fase 5 — Chapter specs

**Stato: DONE — PASS 2026-09-20**

Output: otto file in `manual/chapter-specs/` + `manual/PHASE5_AUDIT.md`.

Esito: **39/39 capitoli con spec**; prerequisiti, primary homes, first-use, metriche/evidenza, casi e backend sources verificati.

---

# Fase 6 — Drafting del manuale

**Stato: DONE — LOCAL PASS 2026-09-20**

## Scopo

Riscrivere il sistema in voce autoriale unitaria, agnostica e reader-facing, seguendo le chapter specs senza esporre il backend.

## Pattern preferito

1. problema/decisione reale;
2. modello mentale;
3. definizioni;
4. causalità;
5. diagnosi;
6. procedura;
7. errori/eccezioni;
8. metriche/evidenza;
9. esempio/caso;
10. sintesi applicativa.

## Output

`manual/draft/`, organizzato in otto file reader-facing per le otto parti.

## Esito

- **8/8 parti draftate**;
- **39/39 capitoli presenti**;
- mini-audit locale eseguito su ogni parte;
- nessun finding P0/P1 emerso nei gate locali;
- P2 lessicali/copy-edit rimandati alla Fase 7–8.

## Regole rispettate nel drafting

- riscrittura originale, non collage;
- niente riferimenti reader-facing a Frank, Merenda, KB o Layer 1;
- definizioni al first use dove previste, con verifica globale rimandata alla Fase 7;
- una primary home per la teoria completa;
- casi sintetici esplicitamente didattici;
- numeri/casi non trattati come benchmark universali;
- nodi canonici live verificati prima di ogni blocco sostanziale.

Gate: **SATISFIED localmente; soggetto ad audit globale Fase 7.**

---

# Fase 7 — Audit didattico, dottrinale e operativo

**Stato: IN PROGRESS**

Audit:

- coverage;
- doctrine fidelity e temporal precedence;
- beginner clarity;
- operational usability;
- redundancy e primary-home discipline;
- provenance/copyright;
- terminology/first-use;
- case/evidence discipline;
- assenza di backend nella prosa;
- cross-reference e coerenza globale.

Output: `manual/AUDIT.md`.

Gate: **nessun finding P0/P1 aperto.**

---

# Fase 8 — Finalizzazione e release

**Stato: NOT STARTED**

Attività: uniformare terminologia/voce, consolidare cross-reference, finalizzare glossario/indice analitico/esercizi/casi, rimuovere tracce backend, produrre master finale.

Output: `manual/final/`.

---

# Regola di avanzamento

Una fase passa a `DONE` soltanto quando il suo gate è soddisfatto.

La priorità resta:

**non perdere conoscenza → non perdere causalità → non perdere il lettore.**