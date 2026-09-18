# PROJECT STATUS

## Stato generale

**MERENDA BUSINESS CORE — LAYER 1 OPERATIONAL. ARCHITECTURE REVIEW ACTIVE; STATIC ROUTING BASELINE COMPLETE.**

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

La suite contiene **30 casi**:

- `evals/routing/cases.jsonl`
- `evals/routing/cases_phase2.jsonl`
- `evals/routing/cases_phase3.jsonl`

Copertura intenzionale: domanda, mercato/cliente, user-vs-payer, customer expiry, search intent, sell-in/sell-through, partnership, high spender, trigger/priorità, creative testing, eventi, lead state, founder dependency, automazione/processo, pricing, analogico, provenance e zero-based reconstruction.

Validator:

`python3 scripts/validate_routing_evals.py`

### Architecture Inventory

Builder:

`python3 scripts/build_architecture_inventory.py --json-out <path> --md-out <path>`

Risultato meccanico:

- 60 Markdown sotto `merenda/`;
- 47 nodi canonici non-README, esclusi INDEX/Router;
- ~636 KB di doctrine layer;
- 0 link locali rotti;
- 0 nodi canonici senza incoming link;
- 0 nodi completamente privi di visibilità se si includono i README di sezione;
- 12 nodi canonici non nominati direttamente dal Decision Router;
- 6 nodi scoperti soltanto tramite README di sezione rispetto ai control layer principali;
- 605 heading candidati meccanici non esplicitamente visibili nel control plane: upper bound rumoroso, non 605 gap reali.

Review:

- `reviews/ARCHITECTURE_INVENTORY_INITIAL_FINDINGS.md`
- `reviews/ARCHITECTURE_INVENTORY_MECHANICAL_REVIEW.md`

Diagnosi:

> **la KB è strutturalmente ben collegata; il problema prioritario è la discoverability delle unità semantiche dentro nodi già raggiungibili e spesso molto grandi.**

### Doctrine / Retrieval Map v1

Schema draft:

`reviews/DOCTRINE_RETRIEVAL_MAP_SCHEMA_V1.md`

Shard sperimentali:

- `reviews/drafts/DOCTRINE_RETRIEVAL_MAP_V1_SEED.json`
- `reviews/drafts/DOCTRINE_RETRIEVAL_MAP_V1_PHASE3.json`
- `reviews/drafts/DOCTRINE_RETRIEVAL_MAP_V1_PHASE4.json`
- `reviews/drafts/DOCTRINE_RETRIEVAL_MAP_V1_PHASE5.json`

La mappa usa entry semantiche con:

- path + anchor canonico;
- `upstream`;
- `must_read_with` condizionale;
- `evidence_required`;
- `not_sufficient_for`;
- provenance a livello di entry;
- supersession;
- eval linkage.

Validator:

`python3 scripts/validate_retrieval_map.py`

Checkpoint CI Phase 5:

- repository invariants: PASS;
- routing eval suite: PASS — 30 casi;
- retrieval map: PASS — **30 entry**;
- eval linkage coverage: **30/30 = 100%**;
- Architecture Inventory: PASS.

### Static addressability baseline

Report:

`reviews/STATIC_ADDRESSABILITY_BASELINE.md`

Script:

`python3 scripts/score_static_routing_coverage.py`

Risultati:

- Router corrente: **82,8% mean direct recall**;
- Router corrente: **19/30 casi con full direct recall**;
- Router + Map: **100% mean direct recall**;
- Router + Map: **30/30 casi con full direct recall**.

Questa è **static addressability, non behavioral performance**.

Decisione a questo gate:

**fermare l'espansione della Map guidata dalla suite corrente.**

Nuove entry entrano solo per failure comportamentali, nuovi casi reali o nuovi gap high-leverage nominabili.

### Behavioral run protocol

Pronti:

- `evals/routing/RUN_PROTOCOL.md`
- `scripts/export_routing_eval_prompts.py`
- `scripts/score_routing_run.py`
- `reviews/CODEX_ROUTING_BASELINE_TASK.md`

Il modello sotto test deve vedere solo prompt sanitizzati, mai required nodes/checks/forbidden shortcuts.

Confronto da eseguire:

1. `current`
2. `current_plus_map`

Metriche:

- observed required-node recall;
- relevant retrieval precision;
- over-retrieval;
- required/upstream check recall;
- forbidden shortcut rate;
- provenance error;
- unsupported inference;
- premature tactic;
- founder accommodation failure.

---

## Principali finding architetturali correnti

1. **Non serve una nuova tassonomia completa.** La struttura è collegata e non mostra orphan nodes o link rotti.
2. **Il Router corrente svolge troppe funzioni.** È manuale, lungo e inevitabilmente incompleto rispetto ai nodi specialistici.
3. **File-level routing non basta.** Concetti decisivi vivono come sezioni di nodi più ampi.
4. **I nodi-hub sono grandi.** Caricarli sempre interamente aumenterebbe recall ma peggiorerebbe precisione e token efficiency.
5. **Serve retrieval causale, non solo similarity.** `upstream`, `must_read_with` ed evidence sufficiency sono parte della decisione.
6. **La provenance deve vivere a livello di entry.** Alcuni file contengono insieme materiale MERENDA_PRIMARY e ASSIMILATED.
7. **La governance storica contiene istruzioni incompatibili con lo stato corrente.** Il conflitto frozen/current va risolto esplicitamente prima di chiudere la review.
8. **Non assumere full-text search perfetta come rete di sicurezza.**
9. **La Map chiude staticamente i blind spot senza richiedere una riscrittura del Router.** Ora deve guadagnarsi il diritto di entrare nel control plane tramite behavioral eval.

---

## Contatori canonici — corpus YouTube storico

- Video individuati: 468
- Video completati: 307
- Video esclusi: 6
- Video rimanenti: 155
- Processati semanticamente: 313

## Contatori canonici — layer source-agnostic

- Nuove fonti Merenda registrate: 166
- Nuove fonti Merenda studiate: 166
- Nuove fonti Merenda escluse: 0
- Nuove fonti Merenda da processare: 0

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

1. **P0 — Behavioral routing/retrieval baseline**
2. **P0 — Risoluzione esplicita governance historical/current**
3. **P1 — Decisione su adozione Doctrine/Retrieval Map**
4. **P1 — Vendita end-to-end**
5. **P1 — Casi studio**
6. **P2 — Sintesi brand**
7. **P2 — Voice of Customer / ricerca mercato**
8. **P2 — Hardening Git**

---

## Next Action

**Eseguire la behavioral baseline isolata prima di progettare Router v2.**

Sequenza:

1. esportare prompt sanitizzati con `scripts/export_routing_eval_prompts.py`;
2. eseguire i 30 casi con architettura `current` in contesti indipendenti;
3. catturare trace reali dei file/anchor letti;
4. eseguire gli stessi casi con `current_plus_map`, sempre isolati;
5. usare `scripts/score_routing_run.py`;
6. fare judgment semantico sui failure più importanti;
7. decidere se la Map migliora il comportamento abbastanza da essere adottata;
8. solo se restano failure strutturali non risolte, progettare Router v2.

Non riaprire automaticamente il corpus YouTube residuo.
