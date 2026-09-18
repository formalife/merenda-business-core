# Semantic Retrieval Model v1

Data: 2026-09-18
Stato: DRAFT — ARCHITECTURE REVIEW

## Scopo

Separare chiaramente:

1. struttura fisica della KB;
2. unità semantiche decisionali;
3. retrieval runtime;
4. costo del contesto.

Il modello nasce dal risultato behavioral in cui `current_plus_map` ha aumentato precisione ma ridotto recall rispetto a `current`.

---

## 1. Canonical Document

I Markdown sotto `merenda/` restano la fonte canonica della doctrine.

Il file è un contenitore editoriale e di provenance, non necessariamente la migliore unità runtime.

---

## 2. Structural Unit — GENERATED

Una Structural Unit è derivata automaticamente da heading e gerarchia Markdown.

Campi minimi:

- `structural_id`
- `path`
- `anchor`
- `heading`
- `heading_path`
- `level`
- `parent_structural_id`
- `children_structural_ids`
- `line_start`
- `line_end_direct`
- `line_end_subtree`
- dimensione del contenuto diretto e del subtree

### Regola

La Structural Unit NON interpreta la dottrina e NON decide quando usarla.

Serve a:

- trovare sezioni;
- navigare parent/child;
- espandere progressivamente il contesto;
- misurare quanto contenuto viene recuperato;
- mantenere auditabilità verso il Markdown canonico.

---

## 3. Decision Semantic Unit — CURATED

Una Decision Semantic Unit rappresenta un principio, gate, eccezione o dipendenza causale capace di cambiare una decisione.

Esempi:

- `MARKET.USER_VS_PAYER`
- `MARKET.NATURAL_CUSTOMER_EXPIRY`
- `DEMAND.OWNED_BEFORE_NEW`
- `COPY.TRIGGER_PRIORITY`

Campi candidati:

- `semantic_id`
- `label`
- `status`
- `canonical_structural_id`
- eventuali `supporting_structural_ids`
- `kind`
- `canonical_for`
- `use_when`
- `not_sufficient_for`
- `upstream`
- `must_read_with`
- `evidence_required`
- `provenance`
- `supersession`

### Regola

La Decision Map deve contenere soltanto metadata che cambiano routing, sufficiency o provenance.

Non deve elencare manualmente ogni heading della KB.

---

## 4. Retrieval flow candidato

### Step 1 — Case representation

Estrarre soltanto dimensioni che possono cambiare routing:

- outcome economico;
- sintomo/livello apparente;
- attori rilevanti;
- stato della relazione;
- domanda/intento/consapevolezza;
- economics noti;
- vincoli;
- tattica proposta;
- fatti vs ipotesi.

### Step 2 — Candidate generation

Usare due fonti indipendenti:

1. Decision Map — precisione causale;
2. Structural Index — discovery strutturale/lessicale.

La Decision Map non è un filtro esclusivo.

### Step 3 — Causal expansion

Aggiungere `upstream` e `must_read_with` solo quando le condizioni lo richiedono.

### Step 4 — Smallest canonical retrieval

Recuperare la Structural Unit minima che contiene il principio canonico.

### Step 5 — Sufficiency check

Chiedere se il contesto attuale è sufficiente per:

- capire il principio senza ambiguità;
- applicarlo al caso;
- preservare caveat/provenance;
- evitare una conclusione downstream prematura.

### Step 6 — Progressive expansion

Se insufficiente:

1. direct unit;
2. local sibling/window;
3. parent subtree;
4. full node.

Il full node è fallback, non default.

### Step 7 — Decision

La decisione viene formulata dal contenuto canonico recuperato + evidenza corrente, non dai metadata della Map.

---

## 5. Recall safety net

Il behavioral test ha mostrato che una mappa più precisa può ridurre troppo lo spazio di ricerca.

Perciò:

- nessun candidato della Map può impedire discovery alternativa;
- se mancano required checks/evidence, il runtime deve poter ampliare la ricerca;
- un `not_sufficient_for` attivo forza retrieval aggiuntivo o richiesta di evidenza;
- failure di retrieval deve essere distinguibile da failure di synthesis.

---

## 6. Context economics

Il runtime deve contabilizzare separatamente:

### Bootstrap tax
Contesto di governo sempre caricato.

### Retrieval tax
Contenuto specialistico letto per localizzare/applicare la doctrine.

### Expansion tax
Contesto aggiuntivo caricato perché una unità minima non era sufficiente.

### Synthesis cost
Input/output del modello per produrre la decisione.

Metriche candidate:

- input tokens;
- cached input tokens;
- output tokens;
- doctrine chars/words recuperati;
- structural units recuperate;
- parent expansions;
- full-node fallbacks;
- tokens per required semantic unit;
- tokens per decisione corretta.

---

## 7. Eval implications

La metrica primaria futura non deve essere `required_nodes` ma `required_semantic_units`.

`required_nodes` resta come historical compatibility signal.

Nuovi segnali:

- semantic unit recall;
- semantic context precision;
- expansion accuracy;
- context cost;
- required/upstream check recall;
- doctrine fidelity;
- provenance accuracy.

---

## 8. Non-goals v1

Questa versione NON introduce:

- embeddings;
- vector DB;
- reranker;
- LLM-generated contextual summaries;
- GraphRAG;
- riscrittura dei Markdown canonici;
- split manuale massivo dei file;
- Router v2.

Questi elementi entrano solo dopo una failure misurata che non può essere risolta con il modello strutturale/causale leggero.
