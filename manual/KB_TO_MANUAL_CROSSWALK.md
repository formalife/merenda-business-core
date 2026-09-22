# KB-to-Manual Crosswalk — Master Index

## Purpose

Questo è il coverage master del manuale.

Il suo compito è garantire che la trasformazione della KB in manuale non perda conoscenza rilevante. Non definisce l'indice del libro: le sezioni canoniche sono usate soltanto come unità controllabili di decomposizione.

**Stato: COMPLETE — BASELINE PHASE 2 PASS + INTEGRATION DELTA REVALIDATED 2026-09-22.**

Baseline audit: `manual/PHASE2_AUDIT.md`.

Delta successivi alla rifusione Sandler → Merenda:

- `manual/crosswalk/05_acquisizione_integration_2026-09-22.md`;
- `manual/crosswalk/06_vendita_integration_2026-09-22.md`;
- `manual/crosswalk/09_business_integration_2026-09-22.md`.

La baseline conserva gli ID esistenti; i delta aggiungono soltanto conoscenza nuova o precisazioni materialmente nuove. In questo modo non vengono rinumerate unità già usate da curriculum e chapter specs.

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
- `EXCLUDED WITH REASON`

Il first pass è deliberatamente granulare. Il numero di unità serve alla tracciabilità, non misura qualità né lunghezza futura del manuale.

---

# Coverage corrente

| Blocco | File doctrine/routing tracciati | Stato | Crosswalk | Unità |
|---|---:|---|---|---:|
| root routing | 2 | COMPLETE | `manual/crosswalk/root-routing.md` | RTR-001…RTR-017 — 17 |
| `00_fondamenti` | 3 | COMPLETE | `manual/crosswalk/00_fondamenti.md` | FND-001…FND-060 — 60 |
| `01_mercato` | 5 | COMPLETE | `manual/crosswalk/01_mercato.md` | MRC-001…MRC-053 — 53 |
| `02_posizionamento` | 4 | COMPLETE | `manual/crosswalk/02_posizionamento.md` | POS-001…POS-057 — 57 |
| `03_offerta` | 4 | COMPLETE | `manual/crosswalk/03_offerta.md` | OFF-001…OFF-071 — 71 |
| `04_marketing` | 7 | COMPLETE | `manual/crosswalk/04_marketing.md` | MKT-001…MKT-068 — 68 |
| `05_acquisizione` | 7 | COMPLETE | baseline + `05_acquisizione_integration_2026-09-22.md` | ACQ-001…ACQ-076 — 76 |
| `06_vendita` | 16 | COMPLETE | baseline + `06_vendita_integration_2026-09-22.md` | SAL-001…SAL-110 — 110 |
| `07_copy_comunicazione` | 5 | COMPLETE | `manual/crosswalk/07_copy_comunicazione.md` | CPY-001…CPY-064 — 64 |
| `08_brand` | 6 | COMPLETE | `manual/crosswalk/08_brand.md` | BRD-001…BRD-058 — 58 |
| `09_business` | 10 | COMPLETE | baseline + `09_business_integration_2026-09-22.md` | BUS-001…BUS-113 — 113 |
| `10_casi_studio` | 3 | COMPLETE | `manual/crosswalk/10_casi_studio.md` | CAS-001…CAS-016 — 16 |
| **Totale** | **72** | **CURRENT COVERAGE COMPLETE** | — | **763** |

### Nota su `06_vendita`

I 16 file tracciati comprendono:

- README/routing;
- 11 nodi canonici rifondati;
- 4 vecchi path mantenuti temporaneamente come **routing aliases `SUPERSEDED`**.

I quattro alias sono `EXCLUDED WITH REASON` dal coverage dottrinale perché non contengono più conoscenza autonoma. Restano soltanto per non rompere link storici durante la migrazione.

Nessun nodo canonico corrente è escluso per omissione.

---

# Consolidamento cross-section

## Semantic deduplication e primary homes

Artefatto baseline: `manual/PRIMARY_HOME_MAP.md`.

Funzione: assegnare una sola casa primaria editoriale ai concetti ricorrenti e trasformare le ripetizioni residue in applicazioni/cross-reference.

Decisioni correnti:

- economics completi → Business, con literacy minima anticipata;
- VoC → sintesi editoriale trasversale;
- lifecycle → Customer Success/Business con state-machine mechanics da Acquisition;
- sales end-to-end → Vendita;
- prospecting/outbound → Acquisition, prima dell'handoff alla vendita;
- positioning → Posizionamento;
- offer/pricing → Offerta;
- demand/awareness/channel → Marketing;
- funnel/database/pre-education → Acquisition;
- copy/argumentation → Copy;
- authority/proof/reputation/community → Brand con split pre-sale/post-experience;
- router per sintomo → toolkit diagnostico.

### Riconciliazione vendita dopo integrazione 2026-09-22

Il manuale non insegna “Merenda” e “Sandler” come due scuole concorrenti.

L'architettura didattica corrente è una sola:

**marketing prepara → sales verifica → relazione/processo → Pain → Budget/Investment → Decision → Fulfillment selettivo → decisione → Post-Sell immediato → customer success/lifecycle.**

Prospecting resta a monte in Acquisition. Customer Success continuativo resta a valle in Business. Una nuova opportunità di expansion rientra nel normale processo di qualification.

La provenance Sandler resta nel backend editoriale; il lettore riceve il sistema integrato.

## Dependency pass

Artefatto baseline: `manual/DEPENDENCY_MAP.md`.

35 blocchi D-01…D-35 definiscono hard prerequisites, soft prerequisites e feedback loop.

La rifusione 2026-09-22 **non richiede nuovi macro-prerequisiti né nuovi capitoli**. Precisa invece le dipendenze interne già previste:

- prequalifica ≠ qualification;
- Pain → Budget → Decision prima della proposta;
- Fulfillment dopo qualification;
- follow-up dipende dallo stato reale e può richiedere diagnosi a monte;
- performance sales richiede diagnosi Behavior/Attitude/Technique prima del training;
- expansion richiede valore realizzato + nuova evidenza e poi requalification.

Finding centrale invariato: il problema del corpus non è una carenza di conoscenza fondamentale, ma l'ordine in cui deve essere insegnata.

## Provenance/temporal pass

Artefatto baseline: `manual/PROVENANCE_MAP.md`.

Preservati i punti in cui fonte assimilata, temporal precedence o sintesi possono cambiare il significato editoriale.

Regola aggiuntiva dopo integrazione Sandler:

- termini o framework Sandler possono comparire nel backend per precisione;
- la prosa reader-facing resta unitaria e source-agnostic;
- elementi historical/institutional non vengono presentati come regole universali se il current corpus non li supporta.

## Case inventory

Artefatto: `manual/CASE_INVENTORY.md`.

I casi reali disponibili sono sufficienti a sostenere molti principi ma non tutti i collegamenti end-to-end. I casi sintetici dichiaratamente didattici restano utilizzabili senza trasformarli in evidenza fattuale.

---

# Gap status

La baseline Phase 2 registrava G-001…G-008. Le successive fasi editoriali li hanno chiusi o resi non bloccanti.

L'integrazione 2026-09-22 **non apre un nuovo doctrinal gap bloccante**.

Nuovi controlli editoriali obbligatori:

- Cap. 16 deve coprire il prospecting come sistema, non solo la scelta del canale;
- Cap. 22 deve distinguere prequalifica da qualification;
- Cap. 23 deve contenere relazione/processo + Pain/Budget/Decision + disqualification + Fulfillment/Post-Sell;
- Cap. 24 deve integrare follow-up state-based + B.A.T. + behavior plan + reinforcement/coaching/accountability;
- Capp. 25–26 devono coprire handoff strutturato, valore realizzato e account growth/requalification.

Registro storico: `manual/MANUAL_GAPS.md`.

---

# Coverage gate corrente

Gate:

> ogni unità dottrinale rilevante ha almeno una destinazione editoriale candidata e ogni nodo canonico è coperto, escluso motivatamente o aperto.

Esito dopo i delta 2026-09-22: **PASS — 763 unità coperte.**

La vecchia Phase 2 audit resta provenance storica del baseline; non viene riscritta retroattivamente come se conoscesse la rifusione successiva.

---

# Next

Allineare curriculum e chapter specs alle unità delta **senza cambiare l'architettura da 39 capitoli**, quindi eseguire una revalidation editoriale prima del drafting/proseguimento del manuale.

Vincoli:

1. `manual/MANUAL_CONTRACT.md`;
2. questo coverage master + delta;
3. `manual/PRIMARY_HOME_MAP.md`;
4. `manual/DEPENDENCY_MAP.md`;
5. `manual/CASE_INVENTORY.md`;
6. `manual/MANUAL_GAPS.md`.

La tassonomia della KB non è l'indice del manuale.