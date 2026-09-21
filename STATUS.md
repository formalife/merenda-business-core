# PROJECT STATUS

## Stato generale

**MERENDA BUSINESS CORE — LAYER 1 OPERATIONAL. ARCHITECTURE REVIEW: RETRIEVAL + COMPACT CONTROL PLANE VALIDATED ON BLIND HOLDOUT; STABILIZATION / ADOPTION ACTIVE.**

Il progetto è il Layer 1: doctrine layer, routing decisionale e motore di diagnosi.

La doctrine sotto `merenda/` non è stata modificata dalla Architecture Review. `merenda/DECISION_ROUTER.md` resta canonico e invariato.

Branch attivo: `architecture-review-routing-v2`

Draft PR: `#15 — Architecture Review: routing and retrieval fidelity baseline`

---

## Decisione architetturale corrente

Per uso strategico/diagnostico il control plane candidato corrente è:

**`REASONING_KERNEL.md` → compact semantic index → semantic entry selettive → sezione canonica minima → sufficiency check → structural search / parent-child safety net → full-node fallback.**

Regole:

1. **File ≠ unità primaria di retrieval.**
2. `REASONING_KERNEL.md` sostituisce il preload dei cinque full control-plane documents nel bootstrap operativo candidato.
3. La doctrine specialistica canonica resta autoritativa e va recuperata per decisioni materiali.
4. I full control-plane documents restano governance/reference/fallback; non vengono eliminati.
5. La semantic Map/index non è filtro esclusivo.
6. Structural discovery resta recall safety net.
7. Nessun Router v2 per ora.
8. Embeddings/reranking/GraphRAG restano escalation solo dopo failure misurate.

Decision record:

`reviews/behavioral/HOLDOUT_V1_UNBLINDED_ARCHITECTURE_DECISION_2026-09-21.md`

---

## Behavioral baseline — COMPLETE

Commit congelato: `4506e67e812c4e3270c4446d58f6a3d8c3934e82`

| Configurazione | Required-check recall | Material inversions |
|---|---:|---:|
| `current` | 93/96 = 96.875% | 0 |
| `current_plus_map` | 95/96 = 98.958% | 0 |

Deterministic file-level retrieval storico:

| Configurazione | Mean required-node recall | Mean precision | Over-retrieved |
|---|---:|---:|---:|
| `current` | 0.7472 | 0.7644 | 24 |
| `current_plus_map` | 0.6778 | 0.8000 | 14 |

Decisione metodologica: required-node/file recall non è una metrica primaria adeguata; semantic decision fidelity prevale.

---

## Context baseline — COMPLETE

| Metrica media/caso | `current` | `current_plus_map` |
|---|---:|---:|
| reconstructed chars | 130,511 | 137,128 |
| control-plane chars | 92,751 | 91,985 |
| routing metadata | 0 | 17,337 |
| specialist doctrine | 27,136 | 20,589 |

Conclusione: il vecchio bootstrap era il costo dominante.

---

## Retrieval architecture — IMPLEMENTED / STABILIZED

### Structural Index

`scripts/build_structural_index.py`

- 60 documenti;
- 912 structural sections;
- schema 1.1;
- path/anchor IDs;
- parent/children;
- section/subtree ranges;
- fenced-code exclusion;
- invariant validation.

### Semantic Gold v2

`evals/routing/semantic_gold_v2.jsonl`

- 30/30 development cases manual reviewed;
- 42 semantic units nel registry;
- `eval_cases` escluso dal runtime.

I 30 casi sono ora **regression suite**, non holdout.

### Prototype A3

A3 applica:

- massimo iniziale di 4 semantic candidate salvo espansione causale motivata;
- specifico prima del generico;
- `must_read_with` solo quando applicabile;
- stop dopo primo collo di bottiglia + dipendenze materiali;
- application audit delle unità verificate.

Smoke development A3:

- semantic verified recall 0.9444;
- focused precision 0.8889;
- 18/19 answer checks;
- 0 material inversions;
- mean context 110,373 chars/case;
- specialist doctrine 6,580 chars/case.

Focused repair gate A31, R020+R027:

- retrieval recall 1.0000;
- focused precision 0.9000;
- 7/7 answer checks;
- 0 material inversions.

---

## Blind Architecture Holdout v1 — PASSED

Holdout: `evals/routing/holdout_v1.jsonl`

Protocol: `reviews/ARCHITECTURE_HOLDOUT_V1_PROTOCOL.md`

Six new cases, 18 required checks, zero case-ID overlap with R001–R030. No semantic unit was added for the holdout.

Blind judgment was frozen before mapping:

| Blind variant | Required checks | Full-pass cases | Material inversions | Forbidden shortcuts |
|---|---:|---:|---:|---:|
| A | **18/18** | **6/6** | 0 | 0 |
| B | **18/18** | **6/6** | 0 | 0 |

After unblinding:

- A3 + full bootstrap: **18/18**;
- A3 + Compact Reasoning Kernel: **18/18**;
- observed quality delta: **0**.

Per-case mapping was randomized; kernel was B in H001/H003/H004/H005/H006 and A in H002.

Reports:

- `reviews/behavioral/HOLDOUT_V1_BLIND_ANSWER_JUDGMENT_2026-09-21.md`
- `reviews/behavioral/HOLDOUT_V1_UNBLINDED_ARCHITECTURE_DECISION_2026-09-21.md`

---

## Compact Reasoning Kernel v1 — VALIDATED / PROMOTED

Operational artifact: `REASONING_KERNEL.md`

Historical experimental source: `reviews/drafts/COMPACT_REASONING_KERNEL_V1.md`

Zero-Codex fixed-control measurement:

- full five-file control plane: **89,192 chars**;
- kernel: **11,324 chars**;
- kernel/full ratio: **0.127**;
- fixed-bootstrap reduction: **~87.3%**.

Blind paired holdout observed total context:

- full architecture: **120,116 chars/case**;
- kernel architecture: **34,288 chars/case**;
- total-context delta: **−71.5%**.

This is reconstructed-character instrumentation, not billed-token telemetry.

Decision: **stop Codex-heavy micro-tuning.** The validated kernel becomes the current control-plane candidate on this branch.

Do not further compress it without a new paired evaluation and a material expected gain.

---

## Remaining architecture work — LOW CODEX COST

1. Update operational entrypoints to preload `REASONING_KERNEL.md` instead of the five full control-plane documents for strategic/diagnostic use.
2. Keep full control plane as fallback/audit material.
3. Resolve governance historical/current debt in frozen files only under explicit authorization.
4. After Layer 1 merge, update Layer 2 bootstrap/reference files so Formalife operational chats use the compact bootstrap by default.
5. Treat new real failure classes as future regression cases; do not rerun the full 30-case suite without a material architecture change.

No further Codex-heavy evaluation is currently justified.

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
- Architecture Review può modificare eval, validator, metadata e control-plane experiments senza promuovere automaticamente nuova doctrine.

Non riaprire automaticamente il corpus YouTube residuo.
