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
- riempire il testo reader-facing di riferimenti interni;
- sacrificare prerequisiti per accorciare artificialmente il percorso.

---

# Fase 0 — Control plane e baseline

**Stato: DONE**

Output:

- `manual/README.md`
- `manual/ROADMAP.md`
- `manual/STATUS.md`
- `manual/MANUAL_CONTRACT.md`
- baseline iniziale del doctrine layer

Gate: il progetto può ripartire dal repository senza dipendere dalla chat.

---

# Fase 1 — Architecture Review e corpus inventory

**Stato: DONE**

Output:

- `manual/CORPUS_INVENTORY.md`
- `manual/MANUAL_GAPS.md`

Gate soddisfatto: **60/60 file** sotto `merenda/` censiti e classificati; corpus interpretativo/provenance separato.

---

# Fase 2 — Semantic decomposition e KB-to-Manual Crosswalk

**Stato: DONE — PASS 2026-09-20**

## Scopo

Trasformare i documenti della KB in unità di conoscenza indipendenti dalla loro collocazione originale e consolidare duplicazioni, dipendenze, provenance e casi.

## Output completati

- `manual/KB_TO_MANUAL_CROSSWALK.md`;
- `manual/crosswalk/root-routing.md`;
- `manual/crosswalk/00_fondamenti.md` … `10_casi_studio.md`;
- `manual/PRIMARY_HOME_MAP.md`;
- `manual/DEPENDENCY_MAP.md`;
- `manual/PROVENANCE_MAP.md`;
- `manual/CASE_INVENTORY.md`;
- `manual/PHASE2_AUDIT.md`;
- `manual/MANUAL_GAPS.md` aggiornato.

## Esito

- **60/60 file covered**;
- **709 unità semantiche first-pass**;
- primary-home pass completato;
- dependency pass completato;
- provenance/temporal pass completato;
- case inventory completato;
- nessun doctrinal gap che impedisca il curriculum.

Gate: **PASS**. Vedi `manual/PHASE2_AUDIT.md`.

---

# Fase 3 — Curriculum e architettura didattica

**Stato: IN PROGRESS**

## Scopo

Definire l'ordine in cui una persona inesperta deve apprendere il sistema.

## Principio

L'indice finale nasce dalle **dipendenze cognitive e causali**, non dalle cartelle correnti della KB.

## Vincoli già emersi dalla Fase 2

1. economic literacy minima deve arrivare all'inizio;
2. Voice of Customer precede positioning e copy;
3. positioning precede offer e amplification;
4. offer precede acquisition;
5. authority/proof deve essere disponibile prima delle decisioni costose;
6. awareness/intent precedono channel e directness;
7. database/stati precedono funnel adattivo e lifecycle;
8. copy operativo viene dopo strategia, proof e awareness;
9. vendita parte dall'handoff;
10. delivery precede retention/referral/reputation;
11. advanced economics + cash + capacity precedono scale;
12. process/governance precedono automation e organizational scale;
13. expansion riapre market e positioning.

## Attività

1. definire learning outcomes finali;
2. trasformare `DEPENDENCY_MAP.md` in parti/moduli/capitoli;
3. verificare i prerequisiti capitolo per capitolo;
4. assegnare una primary home alle unità tramite `PRIMARY_HOME_MAP.md`;
5. distribuire casi/esercizi tramite `CASE_INVENTORY.md`;
6. definire first-use dei termini beginner-critical;
7. verificare coverage dell'intero corpus;
8. produrre l'indice ragionato v1.

## Output

- `manual/MANUAL_CURRICULUM.md`;
- indice ragionato v1;
- prerequisite references;
- case placement;
- first-use terminology map;
- coverage check contro il crosswalk.

## Gate di completamento

Il curriculum:

- copre l'intero corpus rilevante;
- non usa concetti operativamente prima di averli introdotti;
- può essere percorso da zero fino alla diagnosi e progettazione end-to-end di un business;
- assegna una casa a tutti i cluster primari;
- risolve G-006;
- rende espliciti i gap da chiudere in Fase 4.

---

# Fase 4 — Gap closure e sintesi mancanti

**Stato: NOT STARTED**

## Scopo

Chiudere i residui che impediscono al manuale di essere autosufficiente.

## Gap attesi dopo Phase 2

- G-002 — case library: closure plan con casi sintetici;
- G-005 — Voice of Customer / market research: sintesi editoriale unica;
- G-007 — glossary/linguaggio beginner-first.

G-001, G-003, G-004 e G-008 sono già `RESOLVED EDITORIALLY`. G-006 deve essere risolto dal curriculum.

## Output

- sintesi editoriali necessarie;
- `manual/MANUAL_GAPS.md` aggiornato;
- eventuale doctrine review separata solo se una sintesi non è sostenibile col corpus corrente.

## Gate

Nessun capitolo fondamentale dipende da conoscenza implicita che un principiante non potrebbe ricostruire autonomamente.

---

# Fase 5 — Chapter specs

**Stato: NOT STARTED**

Ogni chapter spec deve contenere:

- domanda;
- learning outcome;
- prerequisiti;
- concetti obbligatori;
- causalità centrale;
- errori;
- procedura/decision framework;
- metriche;
- esempi/casi;
- cross-reference;
- fonti backend;
- criteri di completezza.

Output: `manual/chapter-specs/`.

Gate: ogni capitolo del curriculum possiede una spec e nessuna unità critica resta senza casa.

---

# Fase 6 — Drafting del manuale

**Stato: NOT STARTED**

Pattern preferito:

1. problema/decisione reale;
2. modello mentale;
3. definizioni;
4. causalità;
5. diagnosi;
6. procedura;
7. errori/eccezioni;
8. metriche;
9. esempio/caso;
10. sintesi applicativa.

Output: `manual/draft/`.

---

# Fase 7 — Audit didattico, dottrinale e operativo

**Stato: NOT STARTED**

Audit:

- coverage;
- doctrine fidelity;
- beginner clarity;
- operational usability;
- redundancy;
- provenance/copyright.

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