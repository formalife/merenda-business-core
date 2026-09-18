# PROJECT STATUS

## Stato generale

**MERENDA BUSINESS CORE — LAYER 1 OPERATIONAL. ARCHITECTURE REVIEW ACTIVE; BEHAVIORAL + SEMANTIC + CONTEXT BASELINES COMPLETE.**

Il progetto è il **Layer 1** del sistema aziendale: doctrine layer, routing decisionale e motore di diagnosi.

La fase video generalista è chiusa per saturazione al contenuto 313. Il lock operativo resta attivo in `sources/queue/ACQUISITION_CLOSED.md`; i residui 314–468 non sono backlog automatico.

Il corpus source-agnostic corrente è processato fino a `FM-SRC-0166`: 166 fonti registrate, 166 studiate, 0 pending.

Checkpoint semantico:

`reviews/FINAL_SEMANTIC_AUDIT.md`

Priorità corrente: **semantic-unit gold v2 → addressable hierarchical retrieval → fidelity/context-cost A/B**, prima dell'uso operativo intensivo del Layer 1 su Formalife.

Roadmap attiva:

- `reviews/ARCHITECTURE_IMPLEMENTATION_ROADMAP_V2.md`
- `reviews/ARCHITECTURE_IMPLEMENTATION_ROADMAP_V2_UNBLINDED_ADDENDUM.md`

Branch:

`architecture-review-routing-v2`

Draft PR:

`#15 — Architecture Review: routing and retrieval fidelity baseline`

---

## Decisione metodologica

**Eval first, refactor second. Fidelity e context cost devono migliorare insieme.**

`merenda/DECISION_ROUTER.md` non è stato modificato. La doctrine sotto `merenda/` resta canonica e invariata dalla review.

---

## Behavioral baseline — COMPLETE

Commit congelato:

`4506e67e812c4e3270c4446d58f6a3d8c3934e82`

### Deterministic file-level retrieval

| Configurazione | Mean required-node recall | Mean relevant retrieval precision | Over-retrieved nodes |
|---|---:|---:|---:|
| `current` | 0.7472 | 0.7644 | 24 |
| `current_plus_map` | 0.6778 | 0.8000 | 14 |

Il file-level recall faceva apparire la Map peggiore.

### Blind semantic judgment + unblinding — COMPLETE

Report:

- `reviews/behavioral/BLIND_SEMANTIC_JUDGMENT_2026-09-18.jsonl`
- `reviews/behavioral/BLIND_SEMANTIC_JUDGMENT_SUMMARY_2026-09-18.md`
- `reviews/behavioral/UNBLIND_MAPPING_2026-09-18.json`
- `reviews/behavioral/UNBLINDED_SEMANTIC_JUDGMENT_SUMMARY_2026-09-18.md`

| Configurazione | Required-check recall | Discovery misses | Synthesis misses | Material inversions |
|---|---:|---:|---:|---:|
| `current` | 93/96 = 96.875% | 2 | 1 | 0 |
| `current_plus_map` | 95/96 = 98.958% | 0 | 1 | 0 |

Per entrambe: 0 forbidden shortcut, 0 provenance error, 0 unsupported inference, 0 premature tactic, 0 founder-accommodation failure.

`GOLD_TOO_COARSE`:

- `current`: 14/30 case-response;
- `current_plus_map`: 18/30.

RESULT:

- required-node recall non è una metrica primaria adeguata;
- il file è un contenitore editoriale, non necessariamente la unità semantica richiesta;
- l'ipotesi **“Map v1 peggiora il comportamento” è falsificata su questa suite**;
- Map v1 resta sperimentale ma ha guadagnato il ruolo di **precision / causal-routing signal**;
- non deve essere un filtro esclusivo;
- Router v2 resta deferred.

---

## Context-read baseline — COMPLETE

Report:

`reviews/behavioral/CONTEXT_READ_BASELINE_2026-09-18.md`

Misura: ricostruzione deterministica del testo restituito dai comandi `EVAL_READER` completati nei workspace congelati. Non equivale ai token API billed.

| Metrica media per caso | `current` | `current_plus_map` | Delta plus-map |
|---|---:|---:|---:|
| read operations | 15.20 | 15.67 | +0.47 |
| reconstructed chars | 130,511 | 137,128 | +5.1% |
| reconstructed words | 17,766 | 17,222 | −3.1% |
| control-plane chars | 92,751 | 91,985 | −0.8% |
| routing-metadata chars | 0 | 17,337 | +17,337 |
| specialist-doctrine chars | 27,136 | 20,589 | **−24.1%** |
| other chars | 10,625 | 7,217 | **−32.1%** |

RESULT:

- la Map riduce materialmente doctrine specialistica e letture accessorie;
- il formato/runtime attuale della Map costa troppo: i 17,337 chars/case di routing metadata più che compensano il risparmio, portando il totale a +5.1% chars;
- Prototype A deve rendere la Map **addressable**, non precaricarla;
- il bootstrap domina il contesto con ~92k chars/case e verrà testato separatamente solo dopo stabilizzazione del retriever.

---

## Semantic retrieval model — ACTIVE

Documento:

`reviews/SEMANTIC_RETRIEVAL_MODEL_V1.md`

Tre livelli distinti:

1. **Canonical Document** — Markdown doctrine canonica;
2. **Structural Unit — GENERATED** — heading/path/parent-child/range/dimensione;
3. **Decision Semantic Unit — CURATED** — causalità, gate, evidence, provenance, supersession.

Pattern candidato:

**compact semantic index → candidate semantic IDs → selected routing entries → smallest canonical section → sufficiency check → local/parent expansion → full node fallback.**

La Decision Map è un segnale di precisione; Structural Index/discovery è la recall safety net.

---

## Structural Index — IMPLEMENTED / HARDENED

Builder:

`python3 scripts/build_structural_index.py --json-out <path> --md-out <path>`

Genera deterministicamente:

- `structural_id`;
- heading/anchor/heading path;
- parent/children;
- line range diretto e subtree;
- chars/words;
- metadata documentali.

Ignora heading dentro fenced code block e valida invarianti parent/child/range/ID.

Nessuna interpretazione dottrinale e nessuna modifica a `merenda/`.

---

## Semantic Gold v2 — STARTED

Schema:

`evals/routing/SEMANTIC_GOLD_V2.md`

Migration builder:

`scripts/build_semantic_gold_draft.py`

Regola:

- Map `eval_cases` produce solo **candidate hints**;
- `required_semantic_units` deve essere revisionato manualmente contro required checks + canonical doctrine;
- `required_nodes` resta compatibilità/debug, non target primario;
- serve holdout blind prima dell'adozione finale.

---

## Context instrumentation — IMPLEMENTED

Scorer:

`scripts/score_context_reads.py`

Lo scorer usa i workspace congelati della baseline, non la repo corrente, e conta solo command execution completati con successo.

Nel prossimo harness vanno aggiunti anche input/cached/output token model-reported quando disponibili.

---

## Decisioni correnti

1. **File ≠ unità primaria di retrieval.**
2. **Map v1 non entra nel current control plane**, ma resta experimental routing metadata.
3. **Prototype A non deve preloadare la Map.** Deve recuperare solo entry selezionate.
4. **Structural Index generato + Decision Semantic Units curate** restano layer separati.
5. **Nessun Router v2 per ora.**
6. **Context economics è acceptance criterion di primo livello.**
7. **Full bootstrap resta fisso durante Prototype A** per non confondere effetti retrieval/bootstrap.
8. **Embeddings/reranking/GraphRAG restano escalation**, non default.
9. **La governance historical/current resta P0 separato** prima della chiusura finale della review.

---

## Acceptance direction — Prototype A

Con full bootstrap tenuto costante:

- semantic required-check recall ≥ `95/96` sulla suite corrente;
- 0 material/epistemic regression;
- retrieval precision almeno comparabile a `current_plus_map`;
- specialist doctrine ≤ baseline `current_plus_map` dove possibile;
- routing metadata **materialmente sotto 17,337 chars/case**;
- total non-bootstrap reconstructed context ≤ `current`, salvo miglioramento materiale di fidelity;
- nessuna dipendenza esclusiva dalla copertura manuale della Map.

Questi target sono criteri sperimentali, non doctrine contract permanente.

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

- `merenda/` resta doctrine layer canonico;
- Formalife non entra automaticamente nella dottrina;
- una fonte assimilata non viene attribuita a Frank;
- `MERGE, NOT APPEND` resta la regola di consolidamento;
- il lock YouTube resta attivo;
- i file frozen restano invariati salvo autorizzazione esplicita;
- risultati Formalife non diventano automaticamente principi generali;
- Architecture Review può modificare eval, validator, draft metadata e control-plane experiments senza promuovere automaticamente nuova doctrine.

---

## Gap ordinati rispetto alla Architecture Review

1. **P0 — Manual semantic-unit gold v2 review**
2. **P0 — Hierarchical Retriever Prototype A, Map addressable**
3. **P0 — Behavioral A/B: semantic fidelity + context economics**
4. **P1 — Compact Reasoning Kernel experiment sul bootstrap tax**
5. **P1 — Risoluzione governance historical/current**
6. **P2 — Eventuale lexical/BM25 → embeddings → reranking escalation solo su failure misurate**
7. **P2 — Vendita end-to-end / casi / brand / VoC / Git hardening dopo chiusura Architecture Review**

---

## Next Action

Sequenza attiva:

1. revisionare i 30 semantic gold contro required checks e doctrine canonica;
2. costruire un compact semantic index addressable;
3. implementare Hierarchical Retriever Prototype A senza embeddings;
4. instrumentare per entry/section/parent/full-node reads;
5. A/B contro baseline congelate con full bootstrap invariato;
6. solo dopo testare Compact Reasoning Kernel per ridurre ~92k chars/case di bootstrap.

Non riaprire automaticamente il corpus YouTube residuo.
