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

Output:

- `manual/README.md`;
- `manual/ROADMAP.md`;
- `manual/STATUS.md`;
- `manual/MANUAL_CONTRACT.md`;
- baseline iniziale del doctrine layer.

Gate: il progetto può ripartire dal repository senza dipendere dalla chat.

---

# Fase 1 — Architecture Review e corpus inventory

**Stato: DONE**

Output:

- `manual/CORPUS_INVENTORY.md`;
- `manual/MANUAL_GAPS.md` iniziale.

Gate soddisfatto: **60/60 file** sotto `merenda/` censiti e classificati; corpus interpretativo/provenance separato.

---

# Fase 2 — Semantic decomposition e KB-to-Manual Crosswalk

**Stato: DONE — PASS 2026-09-20**

Output principali:

- `manual/KB_TO_MANUAL_CROSSWALK.md`;
- `manual/crosswalk/root-routing.md`;
- `manual/crosswalk/00_fondamenti.md` … `10_casi_studio.md`;
- `manual/PRIMARY_HOME_MAP.md`;
- `manual/DEPENDENCY_MAP.md`;
- `manual/PROVENANCE_MAP.md`;
- `manual/CASE_INVENTORY.md`;
- `manual/PHASE2_AUDIT.md`.

Esito:

- **60/60 file covered**;
- **709 unità semantiche first-pass**;
- primary-home, dependency, provenance/temporal e case inventory pass completati;
- nessun doctrinal gap bloccante.

---

# Fase 3 — Curriculum e architettura didattica

**Stato: DONE — PASS 2026-09-20**

Output:

- `manual/MANUAL_CURRICULUM.md`;
- **8 parti / 39 capitoli**;
- prerequisite order;
- case placement;
- first-use terminology map;
- `manual/PHASE3_AUDIT.md`.

Decisioni strutturali principali:

1. economics minimi al Cap. 2, economics avanzati ai Capp. 30–32;
2. VoC prima di positioning e copy;
3. positioning prima di offer/amplification;
4. brand distribuito causalmente: proof prima della vendita, reputation/community dopo esperienza;
5. funnel insegnato come state machine;
6. vendita parte dall'handoff;
7. lifecycle trattato come sistema unico;
8. scale = economics + cash + capacity + process + people + governance;
9. expansion riapre market e positioning;
10. Cap. 39 ricompone il sistema come operating system diagnostico.

Gate: curriculum beginner-first completo, D-01…D-35 verificati, G-006 risolto.

---

# Fase 4 — Gap closure e sintesi mancanti

**Stato: DONE — PASS 2026-09-20**

Output:

- `manual/syntheses/voice-of-customer.md`;
- `manual/syntheses/synthetic-cases.md`;
- `manual/BEGINNER_GLOSSARY.md`;
- `manual/MANUAL_GAPS.md` aggiornato;
- `manual/PHASE4_AUDIT.md`.

Esito:

- G-001…G-008 tutti `RESOLVED EDITORIALLY`;
- nessun gap P0/P1/P2 bloccante;
- nessuna modifica necessaria a `merenda/`.

---

# Fase 5 — Chapter specs

**Stato: DONE — PASS 2026-09-20**

Output:

- `manual/chapter-specs/README.md`;
- `manual/chapter-specs/part-01-fondamenti.md`;
- `manual/chapter-specs/part-02-mercato.md`;
- `manual/chapter-specs/part-03-posizionamento-offerta.md`;
- `manual/chapter-specs/part-04-domanda-acquisizione.md`;
- `manual/chapter-specs/part-05-copy-vendita.md`;
- `manual/chapter-specs/part-06-lifecycle-brand.md`;
- `manual/chapter-specs/part-07-economics-organizzazione.md`;
- `manual/chapter-specs/part-08-crescita-capstone.md`;
- `manual/PHASE5_AUDIT.md`.

Esito:

- **39/39 capitoli con spec**;
- prerequisiti, primary homes e first-use rispettati;
- decision framework, metriche/evidenza, errori, casi e backend sources definiti;
- nessun cluster primario senza casa;
- nessun gap bloccante.

---

# Fase 6 — Drafting del manuale

**Stato: IN PROGRESS**

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

`manual/draft/`, organizzato per le otto parti del curriculum.

## Regole

- riscrittura originale, non collage;
- niente riferimenti reader-facing a Frank, Merenda, KB o Layer 1;
- definire i termini al first use;
- una primary home per la teoria completa;
- usare casi reali con caveat e casi sintetici come esplicitamente didattici;
- non trasformare numeri/casi in benchmark universali;
- verificare il doctrine backend prima di ogni blocco sostanziale.

## Gate

Tutti i 39 capitoli esistono in draft e rispettano spec, curriculum, coverage e voce editoriale.

## Ordine di drafting

1. Parte I — Capp. 1–4;
2. Parte II — Capp. 5–8;
3. Parte III — Capp. 9–13;
4. Parte IV — Capp. 14–19;
5. Parte V — Capp. 20–24;
6. Parte VI — Capp. 25–29;
7. Parte VII — Capp. 30–35;
8. Parte VIII — Capp. 36–39.

---

# Fase 7 — Audit didattico, dottrinale e operativo

**Stato: NOT STARTED**

Audit obbligatori:

- coverage;
- doctrine fidelity;
- beginner clarity;
- operational usability;
- redundancy;
- provenance/copyright;
- terminology/first-use;
- case/evidence discipline.

Output: `manual/AUDIT.md`.

Gate: nessun finding P0/P1 aperto.

---

# Fase 8 — Finalizzazione e release

**Stato: NOT STARTED**

Attività:

- uniformare terminologia e voce;
- consolidare cross-reference;
- finalizzare glossario e indice analitico;
- finalizzare esercizi/checklist;
- finalizzare casi end-to-end;
- rimuovere tracce del backend;
- produrre master finale.

Output: `manual/final/`.

---

# Regola di avanzamento

Una fase passa a `DONE` soltanto quando il suo gate è soddisfatto.

La priorità resta:

**non perdere conoscenza → non perdere causalità → non perdere il lettore.**