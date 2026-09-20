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

Output: otto file in `manual/draft/`, per un totale di **39/39 capitoli**.

Esito:

- riscrittura originale e reader-facing;
- mini-audit locale su ogni parte;
- nessun finding P0/P1 locale;
- draft completo pronto per audit trasversale.

---

# Fase 7 — Audit didattico, dottrinale e operativo

**Stato: DONE — PASS 2026-09-20**

Output: `manual/AUDIT.md`.

Esito:

- coverage: 39/39 PASS;
- doctrine fidelity/temporal precedence: PASS;
- causal/prerequisite order: PASS;
- beginner clarity: PASS con P2 editoriali;
- reader-facing agnosticism/provenance: PASS con P2 editoriali;
- operational usability: PASS;
- economic grounding: PASS;
- redundancy discipline: PASS;
- case/evidence discipline: PASS;
- global integration: PASS.

Finding finali:

- **P0: 0**;
- **P1: 0**;
- **P2: 11**.

Gate: **SATISFIED**.

---

# Fase 8 — Finalizzazione e release

**Stato: IN PROGRESS**

## Ordine operativo

1. chiudere gli 11 P2 di `AUDIT.md`;
2. uniformare terminologia e first-use;
3. uniformare nomenclatura degli strumenti;
4. rimuovere micro-tracce del backend e formulazioni troppo vicine a catchphrase;
5. uniformare cross-reference e ritmo della voce;
6. finalizzare glossario reader-facing;
7. costruire indice e, se utile, indice analitico;
8. assemblare `manual/final/`;
9. final QA: 39/39, niente backend, niente attribution, niente finding P0/P1/P2 aperti.

## Output

`manual/final/` + control-plane aggiornato.

## Gate

Master finale coerente, studiabile e pubblicabile dal punto di vista editoriale, con tutti i finding di `AUDIT.md` chiusi o esplicitamente rinviati con motivazione.

---

# Regola di avanzamento

Una fase passa a `DONE` soltanto quando il suo gate è soddisfatto.

La priorità resta:

**non perdere conoscenza → non perdere causalità → non perdere il lettore.**