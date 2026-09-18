# PROJECT STATUS

## Stato generale

**MERENDA BUSINESS CORE — LAYER 1 OPERATIONAL. ARCHITECTURE REVIEW ACTIVE; BEHAVIORAL BASELINE COMPLETE; SEMANTIC RETRIEVAL REVIEW STARTED.**

Il progetto è il **Layer 1** del sistema aziendale: doctrine layer, routing decisionale e motore di diagnosi.

La fase video generalista è chiusa per saturazione al contenuto 313. Il lock operativo resta attivo in `sources/queue/ACQUISITION_CLOSED.md`; i residui 314–468 non sono backlog automatico.

Il corpus source-agnostic corrente è processato fino a `FM-SRC-0166`: 166 fonti registrate, 166 studiate, 0 pending.

Checkpoint semantico:

`reviews/FINAL_SEMANTIC_AUDIT.md`

Priorità corrente: **Architecture Review di semantic retrieval, decision fidelity e context economics** prima di riprendere l'uso operativo intensivo del Layer 1 su Formalife.

Roadmap attiva:

`reviews/ARCHITECTURE_IMPLEMENTATION_ROADMAP_V2.md`

Roadmap storica iniziale:

`reviews/ARCHITECTURE_REVIEW_ROADMAP.md`

Branch:

`architecture-review-routing-v2`

Draft PR:

`#15 — Architecture Review: routing and retrieval fidelity baseline`

---

## Architecture Review — stato corrente

### Decisione metodologica

**Eval first, refactor second. Fidelity e context cost devono migliorare insieme.**

`merenda/DECISION_ROUTER.md` non è stato modificato.

### Baseline gold

La suite contiene **30 casi**:

- `evals/routing/cases.jsonl`
- `evals/routing/cases_phase2.jsonl`
- `evals/routing/cases_phase3.jsonl`

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

Diagnosi ancora valida:

> **la KB è strutturalmente ben collegata; il problema prioritario è la discoverability delle unità semantiche dentro nodi già raggiungibili e spesso molto grandi.**

### Doctrine / Retrieval Map v1

Schema draft:

`reviews/DOCTRINE_RETRIEVAL_MAP_SCHEMA_V1.md`

Shard sperimentali:

- `reviews/drafts/DOCTRINE_RETRIEVAL_MAP_V1_SEED.json`
- `reviews/drafts/DOCTRINE_RETRIEVAL_MAP_V1_PHASE3.json`
- `reviews/drafts/DOCTRINE_RETRIEVAL_MAP_V1_PHASE4.json`
- `reviews/drafts/DOCTRINE_RETRIEVAL_MAP_V1_PHASE5.json`

Staticamente la Map chiudeva i blind spot della suite corrente:

- Router corrente: **82,8% mean direct recall**;
- Router corrente: **19/30 casi con full direct recall**;
- Router + Map: **100% mean direct recall**;
- Router + Map: **30/30 casi con full direct recall**.

Questa evidenza NON si è trasferita al comportamento reale.

### Behavioral baseline — COMPLETE

Commit congelato:

`4506e67e812c4e3270c4446d58f6a3d8c3934e82`

Confronto deterministic sui 30 casi:

| Configurazione | Mean required-node recall | Mean relevant retrieval precision | Over-retrieved nodes |
|---|---:|---:|---:|
| `current` | 0.7472 | 0.7644 | 24 |
| `current_plus_map` | 0.6778 | 0.8000 | 14 |

RESULT:

- la Map v1 riduce rumore e over-retrieval;
- la Map v1 riduce anche il required-node recall;
- **la Map v1 non viene adottata nel control plane**;
- non si espande la Map per inseguire la stessa suite;
- non si costruisce ancora Router v2;
- semantic judgment e failure decomposition sui trace congelati restano il prossimo gate interpretativo.

### Nuovo modello architetturale in review

Documento:

`reviews/SEMANTIC_RETRIEVAL_MODEL_V1.md`

Distinzione:

1. **Canonical Document** — Markdown doctrine canonica;
2. **Structural Unit — GENERATED** — heading/path/parent-child/range/dimensione;
3. **Decision Semantic Unit — CURATED** — causalità, gate, evidence, provenance, supersession.

Principio runtime candidato:

**smallest canonical unit → sufficiency check → local/parent expansion → full node only as fallback.**

La Decision Map futura è un segnale di precisione, non un filtro esclusivo.

### Structural Index — STARTED

Builder:

`python3 scripts/build_structural_index.py --json-out <path> --md-out <path>`

Il builder genera deterministicamente dalla struttura Markdown:

- `structural_id`;
- heading/anchor/heading path;
- parent/children;
- line range diretto e subtree;
- dimensioni chars/words;
- metadata documentali.

Nessuna interpretazione dottrinale e nessuna modifica a `merenda/`.

La CI ora costruisce e pubblica anche l'artifact `structural-index`.

---

## Principali finding architetturali correnti

1. **Static addressability non predice behavioral retrieval.** Il 100% statico della Map non ha prodotto maggiore recall reale.
2. **La Map v1 sembra migliorare precisione a costo di recall.** Va capita la causa prima di modificarla.
3. **File-level routing è troppo grossolano come metrica primaria.** I gold futuri devono migrare verso semantic units stabili.
4. **Retrieval unit e synthesis unit devono essere separate.** Trovare piccolo, espandere solo quando serve.
5. **Structural discovery e decision routing sono due layer diversi.** Il primo deve essere generato; il secondo curato.
6. **Serve una recall safety net.** La Decision Map non deve poter chiudere prematuramente lo spazio di discovery.
7. **Il bootstrap tax va misurato separatamente.** Il runner corrente carica cinque documenti di control plane completi prima del retrieval specialistico.
8. **Context economics è una metrica primaria.** Più recall ottenuto caricando molta più doctrine non è automaticamente un miglioramento.
9. **Embeddings/reranking/GraphRAG restano escalation.** Nessuna adozione senza failure residua misurata.
10. **La governance storica contiene istruzioni incompatibili con lo stato corrente.** Il conflitto frozen/current resta un P0 separato prima della chiusura della review.

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

1. **P0 — Semantic judgment + failure decomposition della behavioral baseline**
2. **P0 — Semantic-unit gold + Structural Index validation**
3. **P0 — Context economics instrumentation**
4. **P1 — Hierarchical Retriever prototype A senza embeddings**
5. **P1 — Compact Reasoning Kernel experiment**
6. **P1 — Risoluzione governance historical/current**
7. **P2 — Eventuale escalation lexical/embeddings/reranking solo se richiesta dagli eval**
8. **P2 — Vendita end-to-end / casi / brand / VoC / Git hardening dopo chiusura Architecture Review**

---

## Next Action

Sequenza attiva:

1. mantenere congelati i trace behavioral prodotti sul commit `4506e67...`;
2. eseguire semantic judgment sui 60 trace e classificare le failure;
3. costruire/validare Structural Index;
4. definire gold `required_semantic_units` senza rimuovere ancora `required_nodes`;
5. aggiungere token/context instrumentation al prossimo harness;
6. costruire il primo Hierarchical Retriever solo dopo questi gate;
7. confrontare fidelity + context cost contro `current` e baseline Map v1.

Non riaprire automaticamente il corpus YouTube residuo.
