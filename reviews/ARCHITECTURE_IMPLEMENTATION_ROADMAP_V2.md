# Architecture Implementation Roadmap v2 — Semantic Retrieval + Context Economics

Data: 2026-09-18
Stato: ACTIVE
Branch: `architecture-review-routing-v2`
Baseline congelata: `4506e67e812c4e3270c4446d58f6a3d8c3934e82`

## Perché questa roadmap sostituisce operativamente la precedente

La prima Architecture Review ha prodotto una baseline statica promettente ma il test comportamentale ha falsificato l'ipotesi forte che `current_plus_map` fosse già una migliore architettura di retrieval.

Risultato behavioral deterministic sui 30 casi:

| Configurazione | Mean required-node recall | Mean relevant retrieval precision | Over-retrieved nodes |
|---|---:|---:|---:|
| `current` | 0.7472 | 0.7644 | 24 |
| `current_plus_map` | 0.6778 | 0.8000 | 14 |

Interpretazione provvisoria:

- la Retrieval Map v1 ha ridotto rumore e over-retrieval;
- contemporaneamente ha ridotto il recall dei nodi gold;
- quindi la Map v1 NON viene adottata nel control plane;
- non si espande la Map per inseguire la stessa suite;
- non si riscrive ancora il Decision Router;
- il file-level retrieval non viene più assunto come unità primaria dell'architettura futura.

Il semantic judgment sui trace congelati è ancora necessario prima di attribuire causalmente il calo di recall a routing, granularità o synthesis.

---

## Obiettivo v2

Costruire e validare un sistema che massimizzi contemporaneamente:

1. **semantic recall** — trova i principi realmente necessari;
2. **decision fidelity** — usa quei principi nell'ordine causale corretto;
3. **context precision** — evita dottrina irrilevante;
4. **context economics** — riduce input/context consumato per decisione corretta;
5. **provenance fidelity** — preserva MERENDA_PRIMARY / ASSIMILATED / SYNTHESIS;
6. **auditability** — ogni retrieval deve essere ricostruibile e verificabile.

La metrica implicita non è più solo `qualità` ma:

**decision fidelity / context cost**.

---

# Architettura candidata da testare — NON ancora adottata

```text
compact reasoning kernel
        ↓
case representation
        ↓
┌────────────────────────┐
│ curated decision map   │  causalità / upstream / evidence / provenance
└────────────────────────┘
        +
┌────────────────────────┐
│ generated structural   │  file / heading path / parent-child / discovery
│ index                  │
└────────────────────────┘
        ↓
candidate semantic units
        ↓
smallest canonical section/block
        ↓
sufficiency check
        ↓
conditional local/parent expansion
        ↓
full node only when necessary
        ↓
decision
```

Questa è una HYPOTHESIS architetturale, non una decisione finale.

---

# Principi estratti dalla comparative review esterna

## 1. Retrieval unit ≠ synthesis unit

Pattern osservato in LlamaIndex/SentenceWindow e sistemi gerarchici: trovare una unità piccola e usare un contesto più ampio solo dopo il match.

Traduzione candidata:

`semantic block → local section/window → parent section → full node`.

## 2. Parent-child hierarchy esplicita

Pattern LlamaIndex/Haystack: conservare relazioni padre/figlio e risalire solo quando il child non è sufficiente o più child dello stesso parent sono rilevanti.

## 3. Structure-aware chunking

Pattern Unstructured/LlamaIndex Markdown: rispettare heading e confini semantici prima di ricorrere a split per dimensione.

## 4. Retrieval e decision routing sono problemi diversi

La struttura fisica della KB può essere generata meccanicamente. Causalità, gate, evidence requirements e provenance devono restare curati.

## 5. Context budget è parte dell'architettura

Il costo del contesto deve essere misurato e sottoposto a gate, non trattato come conseguenza accidentale.

## 6. Embeddings / reranking / GraphRAG sono escalation, non default

Entrano solo se una failure misurata resta irrisolta con struttura Markdown + routing causale + retrieval gerarchico deterministico.

---

# Fase 0 — Congelare e capire la behavioral baseline

Stato: **IN CORSO**

## 0.1 Congelare risultato deterministic

Baseline commit: `4506e67e812c4e3270c4446d58f6a3d8c3934e82`.

Non rieseguire o reinterpretare i trace con architettura diversa.

## 0.2 Semantic judgment sui 60 trace congelati

Per ciascun caso/configurazione valutare:

- required/upstream check recall;
- forbidden shortcut;
- provenance error;
- unsupported inference;
- premature tactic;
- founder accommodation failure.

## 0.3 Failure decomposition

Ogni failure materialmente rilevante va classificata in una delle categorie:

- `ROUTING_MISS` — non ha cercato il concetto necessario;
- `DISCOVERY_MISS` — cercava l'area corretta ma non ha trovato la unità;
- `EXPANSION_MISS` — ha trovato una unità troppo stretta ma non ha ampliato il contesto;
- `OVER_RETRIEVAL_DILUTION` — contesto corretto ma troppo rumore;
- `CORRECT_RETRIEVAL_BAD_SYNTHESIS` — retrieval corretto, conclusione errata;
- `GOLD_TOO_COARSE` — required node non è la vera unità necessaria;
- `MAP_SUPPRESSION` — la Map ha ridotto lo spazio di ricerca e fatto perdere un concetto necessario;
- `BOOTSTRAP_DILUTION` — control plane precaricato ha aumentato rumore/costo senza beneficio osservabile;
- `PROVENANCE_FAILURE` — principio corretto ma attribuzione/stato errati.

### Gate Fase 0

Nessun nuovo retriever viene adottato prima di sapere quali failure dominano.

---

# Fase 1 — Semantic Unit Model

Stato: **STARTED**

Obiettivo: separare definitivamente tre livelli.

## 1.1 Canonical document

Il Markdown sotto `merenda/` resta doctrine canonica human-readable.

## 1.2 Structural unit — GENERATED

Unità derivata automaticamente dalla struttura Markdown:

- `structural_id` stabile rispetto a path + anchor;
- path;
- heading;
- heading path;
- level;
- parent structural unit;
- child structural units;
- ordine nel documento;
- range di linee per audit;
- dimensione del contenuto.

Non contiene interpretazione dottrinale.

## 1.3 Decision semantic unit — CURATED

ID concettuale stabile come:

- `MARKET.USER_VS_PAYER`
- `DEMAND.OWNED_BEFORE_NEW`
- `COPY.TRIGGER_PRIORITY`

Contiene soltanto metadata che cambiano il routing/decisione:

- canonical structural unit;
- `canonical_for`;
- `use_when`;
- `upstream`;
- `must_read_with`;
- `evidence_required`;
- `not_sufficient_for`;
- provenance;
- supersession.

La decision map NON deve diventare un catalogo manuale di tutti gli heading.

### Gate Fase 1

Lo Structural Index deve essere rigenerabile deterministicamente dalla KB e non duplicare doctrine.

---

# Fase 2 — Eval v2: semantic-unit gold

Stato: PLANNED

Il file-level gold resta per compatibilità storica, ma la metrica primaria diventa semantic-level.

Campi candidati per caso:

- `required_semantic_units`
- `optional_semantic_units`
- `required_checks`
- `forbidden_shortcuts`
- eventuali `required_expansions`

Metriche deterministiche:

- Semantic Unit Recall;
- Semantic Context Precision;
- Expansion Accuracy;
- Over-retrieved Semantic Units.

Metriche judgment:

- Upstream / Required Check Recall;
- Doctrine Fidelity;
- Provenance Accuracy;
- Unsupported Inference Rate;
- Premature Tactic Rate;
- Founder Accommodation Failure.

### Gate Fase 2

I gold semantic IDs devono essere revisionabili umanamente e indipendenti dal path fisico dei file.

---

# Fase 3 — Context Economics instrumentation

Stato: PLANNED

Misurare per ogni run:

- model input tokens;
- cached input tokens;
- output tokens;
- control-plane content letto;
- specialist content letto;
- numero di structural/semantic units recuperate;
- full-node fallbacks;
- token/costo per required semantic unit trovata;
- token/costo per decisione semanticamente corretta.

Separare sempre:

1. **bootstrap tax**;
2. **retrieval tax**;
3. **synthesis cost**.

### Gate Fase 3

Una configurazione non può essere considerata migliore solo perché aumenta recall se il costo contestuale cresce in modo sproporzionato.

---

# Fase 4 — Hierarchical Retriever prototype A

Stato: BLOCKED da Fasi 0–3

Prima implementazione volutamente senza embeddings.

Candidate selection:

1. decision map per causalità/trigger;
2. structural index per discovery/heading matching;
3. union dei candidati;
4. deduplica;
5. upstream expansion obbligatoria;
6. canonical section retrieval.

Progressive expansion:

1. semantic/structural unit minima;
2. local siblings/window se necessario;
3. parent section;
4. full node come fallback finale.

La Map è un segnale di precisione, non un filtro esclusivo.

### Gate Fase 4

Il prototipo deve battere `current` su semantic fidelity senza aumentare il costo medio totale. Se aumenta fidelity con più costo, serve una soglia esplicita di trade-off prima dell'adozione.

---

# Fase 5 — Compact Reasoning Kernel experiment

Stato: BLOCKED da Fase 4

Problema da testare: il bootstrap corrente obbliga a leggere più documenti di governo completi prima del retrieval specialistico.

Non modificare subito i documenti canonici.

Creare una configurazione sperimentale parallela:

- kernel compatto con invarianti decisionali non negoziabili;
- rimandi on-demand al control plane esteso;
- specialist retrieval identico alla configurazione di confronto.

A/B:

- `full_bootstrap + best_retriever`
- `compact_kernel + best_retriever`

Gate:

adottare il compact kernel solo se mantiene doctrine/behavior fidelity entro la soglia stabilita e riduce materialmente input/context cost.

---

# Fase 6 — Escalation only if failure remains

Ordine di escalation:

1. deterministic structural + causal retrieval;
2. lexical/BM25-style fallback;
3. embeddings;
4. reranking;
5. contextual embeddings / late chunking;
6. graph-based retrieval solo se query globali/relazionali lo giustificano.

Ogni livello deve guadagnarsi il diritto di esistere tramite eval.

---

# Fase 7 — Adoption / cleanup

Solo dopo A/B validi:

- scegliere il runtime vincente;
- promuovere solo metadata necessari fuori da `reviews/`;
- decidere il destino della Retrieval Map v1;
- aggiornare bootstrap/control plane;
- risolvere governance historical/current;
- aggiornare CI;
- aggiungere regression eval;
- documentare migration e rollback.

`merenda/` resta doctrine canonica e non viene riscritta per adattarsi al retriever.

---

# Decisioni correnti

## DECISION — Map v1 non adottata

La Retrieval Map v1 resta artefatto sperimentale della Architecture Review. Non entra nel control plane corrente sulla base del solo static coverage.

## DECISION — Nessun Router v2 adesso

Il behavioral result non giustifica ancora una riscrittura del Router. Prima serve failure decomposition semantic-level.

## DECISION — Structural Index generato, Decision Map curata

La futura architettura deve evitare di mantenere manualmente l'inventario delle section.

## DECISION — File non è l'unità primaria di retrieval

Il file resta unità editoriale/canonica. Runtime ed eval migrano progressivamente verso semantic/structural units.

## DECISION — Cost è metrica di primo livello

Token/context economics entra negli acceptance criteria dell'architettura.

---

# Cose da NON fare durante questa roadmap

- non aggiungere entry alla Map solo per recuperare i 30 gold correnti;
- non riscrivere il Router prima della failure decomposition;
- non spezzare manualmente tutti i Markdown in nuovi file;
- non installare LlamaIndex/Haystack/Ragas solo per replicare primitive semplici;
- non introdurre embeddings/vector DB prima di una failure che li richieda;
- non introdurre GraphRAG come default;
- non usare più context come proxy di maggiore fidelity;
- non modificare i file doctrine per facilitare artificialmente gli eval.

---

# Next Action

In parallelo, senza alterare i trace congelati:

1. eseguire semantic judgment + failure decomposition sulla baseline;
2. generare il primo Structural Index deterministico della KB;
3. definire lo schema semantic-unit/eval v2;
4. aggiungere context economics instrumentation al prossimo harness;
5. solo allora costruire Hierarchical Retriever prototype A.
