# PROJECT STATUS

## Stato generale

**MERENDA BUSINESS CORE — LAYER 1 OPERATIONAL. ARCHITECTURE REVIEW ACTIVE; CURRENT KNOWN CORPUS EXHAUSTED.**

Il progetto è il **Layer 1** del sistema aziendale: doctrine layer, routing decisionale e motore di diagnosi.

La fase video generalista è chiusa per saturazione al contenuto 313. Il lock operativo resta attivo in `sources/queue/ACQUISITION_CLOSED.md`; i residui 314–468 non sono backlog automatico.

Il corpus source-agnostic corrente è processato fino a `FM-SRC-0166`: 166 fonti registrate, 166 studiate, 0 pending.

Checkpoint semantico:

`reviews/FINAL_SEMANTIC_AUDIT.md`

Priorità corrente: **Architecture Review di routing, retrieval e fidelity** prima di riprendere l'uso operativo intensivo del Layer 1 su Formalife.

Roadmap:

`reviews/ARCHITECTURE_REVIEW_ROADMAP.md`

Branch:

`architecture-review-routing-v2`

Draft PR:

`#15 — Architecture Review: routing and retrieval fidelity baseline`

---

## Architecture Review — stato corrente

### Decisione metodologica

**Eval first, refactor second.**

`merenda/DECISION_ROUTER.md` non è ancora stato modificato.

### Baseline gold

La suite contiene **30 casi** distribuiti in:

- `evals/routing/cases.jsonl`
- `evals/routing/cases_phase2.jsonl`
- `evals/routing/cases_phase3.jsonl`

Copre fra gli altri:

- domanda posseduta vs nuova acquisizione;
- user vs payer;
- clienti a scadenza;
- search volume vs intent;
- sell-in/sell-through;
- partnership;
- high spender: capacità vs propensione;
- trigger/priorità prima del copy;
- creative testing da winner;
- eventi proprietari;
- lead source vs stato;
- founder dependency;
- automazione/processo;
- temporal caveat su analogico e premium pricing;
- provenance assimilata.

Validator:

`python3 scripts/validate_routing_evals.py`

### Architecture Inventory

Builder:

`python3 scripts/build_architecture_inventory.py --json-out <path> --md-out <path>`

Risultato meccanico corrente:

- 60 Markdown sotto `merenda/`;
- 47 nodi canonici non-README, esclusi INDEX/Router;
- ~636 KB di doctrine layer;
- 0 link locali rotti;
- 0 nodi canonici senza incoming link;
- 0 nodi completamente privi di visibilità se si includono i README di sezione;
- 12 nodi canonici non nominati direttamente dal Decision Router;
- 6 nodi scoperti soltanto tramite README di sezione rispetto ai control layer principali;
- 605 heading candidati meccanici come non esplicitamente visibili nel control plane: upper bound rumoroso, non 605 gap reali.

Review:

- `reviews/ARCHITECTURE_INVENTORY_INITIAL_FINDINGS.md`
- `reviews/ARCHITECTURE_INVENTORY_MECHANICAL_REVIEW.md`

Diagnosi confermata:

> **la KB è strutturalmente ben collegata; il problema prioritario è la discoverability delle unità semantiche dentro nodi già raggiungibili e spesso molto grandi.**

### Doctrine / Retrieval Map v1

Schema draft:

`reviews/DOCTRINE_RETRIEVAL_MAP_SCHEMA_V1.md`

Shard sperimentali:

- `reviews/drafts/DOCTRINE_RETRIEVAL_MAP_V1_SEED.json`
- `reviews/drafts/DOCTRINE_RETRIEVAL_MAP_V1_PHASE3.json`
- `reviews/drafts/DOCTRINE_RETRIEVAL_MAP_V1_PHASE4.json`

La mappa usa entry semantiche con:

- path + anchor canonico;
- `upstream`;
- `must_read_with` condizionale;
- `evidence_required`;
- `not_sufficient_for`;
- provenance a livello di entry;
- supersession;
- collegamento agli eval.

Questo permette di rappresentare correttamente file con provenance mista e concetti nascosti nel nome del nodo.

Validator:

`python3 scripts/validate_retrieval_map.py`

Ultimo checkpoint CI completo prima dello shard Phase 4:

- repository invariants: PASS;
- routing eval suite: PASS — 30 casi;
- retrieval map: PASS — 23 entry;
- eval coverage della map: 26/30 = 86,7%;
- Architecture Inventory: PASS.

I quattro gap di coverage R007/R014/R015/R021 sono stati successivamente trasformati in entry semantiche Phase 4; la relativa CI deve confermare il nuovo stato.

### Run protocol e scoring

Creati:

- `evals/routing/RUN_PROTOCOL.md`
- `scripts/score_routing_run.py`

Il protocollo separa:

1. gold case;
2. agent trace effettivo;
3. judgment.

Metriche deterministiche supportate:

- required-node recall;
- relevant retrieval precision;
- over-retrieval.

Metriche judgment-ready:

- required/upstream check recall;
- forbidden shortcut rate;
- provenance error;
- unsupported inference;
- premature tactic;
- founder accommodation failure.

Questo rende possibile il prossimo confronto reale:

**`current` vs `current_plus_map`.**

---

## Principali finding architetturali correnti

1. **Non serve una nuova tassonomia completa.** La struttura è collegata e non mostra orphan nodes o link rotti.
2. **Il Router corrente svolge troppe funzioni.** È manuale, lungo e inevitabilmente incompleto rispetto ai nodi specialistici.
3. **File-level routing non basta.** Concetti decisivi come user-vs-payer, customer expiry, search intent, sell-in/sell-through e whale curve vivono come sezioni di nodi più ampi.
4. **I nodi-hub sono grandi.** Caricarli sempre interamente aumenterebbe recall ma peggiorerebbe precisione e token efficiency.
5. **Serve retrieval causale, non solo similarity.** Le relazioni `upstream`, `must_read_with` ed evidence sufficiency sono parte della decisione.
6. **La provenance deve vivere a livello di entry.** Alcuni file contengono insieme materiale MERENDA_PRIMARY e ASSIMILATED.
7. **La governance storica contiene istruzioni incompatibili con lo stato corrente.** Il conflitto frozen/current va risolto esplicitamente prima di chiudere la review.
8. **Non assumere full-text search perfetta come rete di sicurezza.** Il control plane deve funzionare anche quando il search connector non recupera termini presenti nella KB.

---

## Contatori canonici — corpus YouTube storico

- Video individuati: 468
- Video completati: 307
- Video esclusi: 6
- Video rimanenti: 155
- Processati semanticamente: 313

## Contatori canonici — layer source-agnostic

- Fonti registrate: 166
- STUDIATO: 166
- ESCLUSO: 0
- pending: 0

Categorie operative rilevanti:

- `MERENDA_PRIMARY`
- `ASSIMILATED_AS_MERENDA_BY_USER`
- `DEFERRED_EXTERNAL_GENERAL_UPDATE`

La provenance reale non viene mai falsificata.

---

## Invarianti Layer 1

- `merenda/` resta il doctrine layer canonico;
- Formalife non entra automaticamente nella dottrina;
- una fonte assimilata non viene attribuita a Frank;
- `MERGE, NOT APPEND` resta la regola di consolidamento;
- il lock YouTube resta attivo;
- i file frozen restano invariati salvo autorizzazione esplicita;
- risultati Formalife non diventano automaticamente principi generali;
- la Architecture Review può modificare control plane, eval, validator e draft metadata senza promuovere automaticamente nuova dottrina.

---

## Gap ordinati rispetto alla Architecture Review

1. **P0 — Routing/retrieval fidelity + baseline comportamentale**
2. **P0 — Risoluzione esplicita governance historical/current**
3. **P1 — Doctrine/Retrieval Map**
4. **P1 — Vendita end-to-end**
5. **P1 — Casi studio**
6. **P2 — Sintesi brand**
7. **P2 — Voice of Customer / ricerca mercato**
8. **P2 — Hardening Git**

---

## Next Action

**Eseguire la baseline comportamentale prima di progettare Router v2.**

Sequenza:

1. confermare CI su Phase 4 e coverage corrente della Retrieval Map;
2. eseguire i 30 casi in contesto isolato con architettura `current`;
3. catturare trace reali dei nodi letti;
4. eseguire gli stessi casi con `current_plus_map` senza esporre il gold al modello;
5. usare `scripts/score_routing_run.py` per il confronto;
6. fare judgment semantico sui failure più importanti;
7. decidere sulla base dei dati se basta `current + map` o se serve davvero Router v2;
8. solo dopo modificare il Router.

Non riaprire automaticamente il corpus YouTube residuo.
