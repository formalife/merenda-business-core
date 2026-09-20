# KB-to-Manual Crosswalk — Master Index

## Purpose

Questo è il coverage master della Fase 2.

Il suo compito è garantire che la trasformazione della KB in manuale non perda conoscenza rilevante. Non definisce l'indice del libro: le sezioni canoniche sono state usate soltanto come unità controllabili di decomposizione.

**Stato: COMPLETE — PHASE 2 GATE PASSED.**

Audit: `manual/PHASE2_AUDIT.md`.

---

## Unità semantica

Ogni unità di conoscenza riceve un ID stabile nel file di sezione.

Tipi ammessi:

- `DEFINITION`
- `PRINCIPLE`
- `CAUSAL_RULE`
- `DECISION_RULE`
- `GATE`
- `PROCEDURE`
- `METRIC`
- `ERROR_PATTERN`
- `CAVEAT`
- `EXAMPLE`
- `CASE`
- `DEPENDENCY`
- `FEEDBACK_LOOP`

Ruoli editoriali first-pass:

- `PRIMARY`
- `SUPPORTING`
- `EXAMPLE/CASE`
- `REFERENCE`
- `OPEN`

Il first pass è deliberatamente granulare. Il numero di unità serve alla tracciabilità, non misura qualità né lunghezza futura del manuale.

---

# Coverage finale

| Blocco | File canonici | Stato | Crosswalk | Unità |
|---|---:|---|---|---:|
| root routing | 2 | COMPLETE | `manual/crosswalk/root-routing.md` | RTR-001…RTR-017 — 17 |
| `00_fondamenti` | 3 | COMPLETE | `manual/crosswalk/00_fondamenti.md` | FND-001…FND-060 — 60 |
| `01_mercato` | 5 | COMPLETE | `manual/crosswalk/01_mercato.md` | MRC-001…MRC-053 — 53 |
| `02_posizionamento` | 4 | COMPLETE | `manual/crosswalk/02_posizionamento.md` | POS-001…POS-057 — 57 |
| `03_offerta` | 4 | COMPLETE | `manual/crosswalk/03_offerta.md` | OFF-001…OFF-071 — 71 |
| `04_marketing` | 7 | COMPLETE | `manual/crosswalk/04_marketing.md` | MKT-001…MKT-068 — 68 |
| `05_acquisizione` | 6 | COMPLETE | `manual/crosswalk/05_acquisizione.md` | ACQ-001…ACQ-067 — 67 |
| `06_vendita` | 5 | COMPLETE | `manual/crosswalk/06_vendita.md` | SAL-001…SAL-071 — 71 |
| `07_copy_comunicazione` | 5 | COMPLETE | `manual/crosswalk/07_copy_comunicazione.md` | CPY-001…CPY-064 — 64 |
| `08_brand` | 6 | COMPLETE | `manual/crosswalk/08_brand.md` | BRD-001…BRD-058 — 58 |
| `09_business` | 10 | COMPLETE | `manual/crosswalk/09_business.md` | BUS-001…BUS-107 — 107 |
| `10_casi_studio` | 3 | COMPLETE | `manual/crosswalk/10_casi_studio.md` | CAS-001…CAS-016 — 16 |
| **Totale** | **60** | **60/60 COVERED** | — | **709** |

Nessun file canonico è escluso per omissione.

---

# Consolidamento cross-section completato

## Semantic deduplication e primary homes

Artefatto: `manual/PRIMARY_HOME_MAP.md`.

Funzione: assegnare una sola casa primaria editoriale ai concetti ricorrenti e trasformare le ripetizioni residue in applicazioni/cross-reference.

Decisioni principali:

- economics completi → Business, con literacy minima anticipata;
- VoC → sintesi editoriale trasversale;
- lifecycle → customer success/Business con state-machine mechanics da Acquisition;
- sales end-to-end → Vendita;
- positioning → Posizionamento;
- offer/pricing → Offerta;
- demand/awareness/channel → Marketing;
- funnel/database/pre-education → Acquisition;
- copy/argumentation → Copy;
- authority/proof/reputation/community → Brand con split pre-sale/post-experience;
- router per sintomo → toolkit diagnostico.

## Dependency pass

Artefatto: `manual/DEPENDENCY_MAP.md`.

35 blocchi D-01…D-35 definiscono hard prerequisites, soft prerequisites e feedback loop.

Finding centrale: il problema del corpus non è una carenza di conoscenza fondamentale, ma l'ordine in cui deve essere insegnata.

## Provenance/temporal pass

Artefatto: `manual/PROVENANCE_MAP.md`.

Preservati i punti in cui fonte assimilata, temporal precedence o sintesi possono cambiare il significato editoriale.

## Case inventory

Artefatto: `manual/CASE_INVENTORY.md`.

I casi reali disponibili sono sufficienti a sostenere molti principi ma non tutti i collegamenti end-to-end. Il gap residuo sarà chiuso con casi sintetici dichiaratamente didattici, senza inventare evidenza fattuale.

---

# Gap status dopo Phase 2

- `G-001` vendita end-to-end → **RESOLVED EDITORIALLY**;
- `G-002` case library → **OPEN — CLOSURE PLAN DEFINED**;
- `G-003` provenance map → **RESOLVED EDITORIALLY**;
- `G-004` brand synthesis → **RESOLVED EDITORIALLY**;
- `G-005` Voice of Customer → **IN SYNTHESIS**;
- `G-006` economics early curriculum → **CONFIRMED — PHASE 3**;
- `G-007` beginner glossary → **OPEN**;
- `G-008` customer lifecycle → **RESOLVED EDITORIALLY**.

Registro: `manual/MANUAL_GAPS.md`.

---

# Fase 2 gate

Gate richiesto:

> ogni unità dottrinale rilevante ha almeno una destinazione editoriale candidata e ogni nodo canonico è coperto, escluso motivatamente o aperto.

Esito: **PASS**.

Verifica completa: `manual/PHASE2_AUDIT.md`.

---

# Next

**Fase 3 — Curriculum e architettura didattica.**

Il curriculum deve usare come vincoli:

1. `manual/MANUAL_CONTRACT.md`;
2. questo coverage master;
3. `manual/PRIMARY_HOME_MAP.md`;
4. `manual/DEPENDENCY_MAP.md`;
5. `manual/CASE_INVENTORY.md`;
6. `manual/MANUAL_GAPS.md`.

La tassonomia della KB non è l'indice del manuale.