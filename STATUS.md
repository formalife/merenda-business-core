# PROJECT STATUS

## Stato generale

**MERENDA BUSINESS CORE — LAYER 1 OPERATIONAL. ARCHITECTURE REVIEW ACTIVE; RETRIEVAL PROTOTYPE STABILIZED ON DEVELOPMENT CASES; BLIND HOLDOUT + COMPACT-KERNEL GATE READY.**

Il progetto è il **Layer 1** del sistema aziendale: doctrine layer, routing decisionale e motore di diagnosi.

La doctrine sotto `merenda/` non è stata modificata dalla Architecture Review. `merenda/DECISION_ROUTER.md` resta canonico e invariato.

Branch attivo:

`architecture-review-routing-v2`

Draft PR:

`#15 — Architecture Review: routing and retrieval fidelity baseline`

---

## Decisione metodologica

**Eval first, refactor second. Fidelity e context cost devono migliorare insieme.**

Il file non è la unità primaria di retrieval. L'architettura candidata separa:

1. **Canonical Document** — doctrine Markdown;
2. **Structural Unit — GENERATED** — heading/path/parent-child/range;
3. **Decision Semantic Unit — CURATED** — gate, causalità, evidence, provenance e dipendenze.

Pattern candidato:

**compact semantic index → semantic entry selettive → sezione canonica minima → sufficiency check → structural search/parent-child safety net → full node fallback.**

---

## Behavioral baseline — COMPLETE

Commit congelato:

`4506e67e812c4e3270c4446d58f6a3d8c3934e82`

### File-level deterministic retrieval

| Configurazione | Mean required-node recall | Mean relevant retrieval precision | Over-retrieved nodes |
|---|---:|---:|---:|
| `current` | 0.7472 | 0.7644 | 24 |
| `current_plus_map` | 0.6778 | 0.8000 | 14 |

### Blind semantic judgment + unblinding

| Configurazione | Required-check recall | Discovery misses | Synthesis misses | Material inversions |
|---|---:|---:|---:|---:|
| `current` | 93/96 = 96.875% | 2 | 1 | 0 |
| `current_plus_map` | 95/96 = 98.958% | 0 | 1 | 0 |

Per entrambe: 0 forbidden shortcut, 0 provenance error, 0 unsupported inference, 0 premature tactic, 0 founder-accommodation failure.

Decisione:

- required-node recall non è una metrica primaria adeguata;
- Map v1 non è production control plane, ma resta un buon precision / causal-routing signal;
- Map non deve essere filtro esclusivo;
- Router v2 resta deferred.

---

## Context-read baseline — COMPLETE

| Metrica media per caso | `current` | `current_plus_map` |
|---|---:|---:|
| reconstructed chars | 130,511 | 137,128 |
| control-plane chars | 92,751 | 91,985 |
| routing-metadata chars | 0 | 17,337 |
| specialist-doctrine chars | 27,136 | 20,589 |
| other chars | 10,625 | 7,217 |

La Map riduce doctrine specialistica ma, nel formato v1, costa troppo come metadata.

Il bootstrap fisso domina il contesto con circa **89–92k chars/case**.

---

## Structural Index — IMPLEMENTED / HARDENED

`scripts/build_structural_index.py`

Stato corrente:

- 60 documenti;
- 912 structural sections;
- schema 1.1;
- heading H1-H6;
- fenced-code exclusion;
- stable path+anchor IDs con gestione duplicati;
- parent/child reciprocity e range validation.

Generated artifact, non doctrine.

---

## Semantic Gold v2 — COMPLETE ON DEVELOPMENT SUITE

`evals/routing/semantic_gold_v2.jsonl`

- 30/30 casi manualmente revisionati;
- 42 semantic unit nel registry runtime;
- required/optional semantic units separate;
- `eval_cases` escluso dal runtime;
- Map usata solo come migration hint, non come automatic gold generator.

La suite da 30 casi è ora principalmente una **regression suite**, non un vero holdout: ha informato gold e sviluppo di A1/A2/A3.

---

## Prototype A3 — DEVELOPMENT STABILIZED

A3 aggiunge disciplina di selezione e application audit senza modificare doctrine:

- massimo iniziale di 4 semantic candidate salvo espansione causale motivata;
- specifico prima del generico;
- `must_read_with` solo quando la condizione è vera;
- stop dopo copertura del primo collo di bottiglia e dipendenze materiali;
- application audit delle semantic unit effettivamente verificate.

### Smoke A3 — 6 casi

- semantic verified recall: 0.9444;
- focused precision: 0.8889;
- full-recall cases: 5/6;
- mean reconstructed context: 110,373 chars/case;
- specialist doctrine: 6,580 chars/case;
- routing metadata: 11,499 chars/case;
- control plane: 89,192 chars/case;
- answer-only judgment: 18/19 required checks, 0 material inversions.

### Focused repair gate A31 — R020 + R027

- retrieval recall: 1.0000;
- focused precision: 0.9000;
- answer-only: 7/7 required checks;
- 0 forbidden shortcuts;
- 0 provenance errors;
- 0 material inversions.

Decisione: **non fare ulteriore tuning sui casi di sviluppo prima di un holdout nuovo.**

---

## Architecture Holdout v1 — FROZEN / READY

Protocollo:

`reviews/ARCHITECTURE_HOLDOUT_V1_PROTOCOL.md`

Gold nascosto al modello:

`evals/routing/holdout_v1.jsonl`

Sei casi nuovi, 18 required checks, zero overlap con R001–R030. Coprono:

- crisis management + internal control;
- earned media/notiziability;
- internal controls;
- current front-end doctrine;
- customer-facing AI governance;
- resilience/single-point-of-failure.

Nessuna semantic unit nuova è stata aggiunta per il holdout. La structural search deve agire come recall safety net dove la mappa corrente non basta.

---

## Compact Reasoning Kernel v1 — FROZEN / EXPERIMENTAL

`reviews/drafts/COMPACT_REASONING_KERNEL_V1.md`

È una sintesi sperimentale del control plane, non doctrine canonica.

Dry-run CI senza Codex:

- full fixed control: **89,192 chars**;
- compact kernel: **11,324 chars**;
- kernel/full ratio: **0.127**;
- riduzione potenziale del bootstrap fisso: **~87.3%**.

Il kernel deve ancora dimostrare di preservare decision fidelity.

---

## Next gate — HIGHEST INFORMATION PER CODEX CREDIT

Non eseguire ora il full run da 30 casi.

Eseguire un paired blind A/B sui 6 holdout:

- `holdout_a3_full` — A3 + cinque file di control plane completi;
- `holdout_a3_kernel` — stesso A3 + Compact Reasoning Kernel v1.

Totale: **12 Codex calls**.

Harness:

`scripts/run_architecture_holdout_ab_host.py`

Regole:

1. full e kernel sullo stesso holdout congelato;
2. nessuna patch fra i due variant;
3. A/B randomizzato localmente per caso;
4. giudicare prima `holdout-blind-answer-bundle.jsonl`;
5. rivelare mapping solo dopo il judgment;
6. retrieval/debug solo dopo unblinding.

Se entrambi falliscono: priorità retrieval/generalization.

Se full passa e kernel fallisce: ridisegnare kernel offline prima di altre call.

Se entrambi passano e kernel riduce materialmente il contesto: congelare la coppia retriever/kernel e decidere se il full regression da 30 casi ha ancora sufficiente valore informativo.

---

## Decisioni correnti

1. **File ≠ unità primaria di retrieval.**
2. **Map v1 non entra nel current control plane**; resta experimental metadata.
3. **Map non è un filtro esclusivo.** Structural discovery resta recall safety net.
4. **Nessun Router v2 per ora.**
5. **Embeddings/reranking/GraphRAG restano escalation**, solo dopo failure misurate.
6. **Context economics è acceptance criterion di primo livello.**
7. **A3 è congelato sui casi di sviluppo fino al holdout.**
8. **Compact Kernel è experimental** e non sostituisce doctrine prima del blind A/B.
9. **Governance historical/current resta un gap P1** prima della chiusura finale della review.

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

Non riaprire automaticamente il corpus YouTube residuo.
