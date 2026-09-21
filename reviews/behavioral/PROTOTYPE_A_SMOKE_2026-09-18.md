# Hierarchical Retriever Prototype A — Smoke Result

Date: 2026-09-18
Status: FROZEN RESULT — answer judgment pending
Tested commit: `f26417c0a84f673cf97687a8dea3aa896f0584a7`
Cases: `R002`, `R008`, `R019`, `R020`, `R027`, `R030`

## Deterministic semantic retrieval result

| Metric | Prototype A smoke |
|---|---:|
| cases | 6 |
| mean verified semantic recall | 0.9028 |
| mean verified semantic precision | 0.4770 |
| full verified recall | 4/6 |
| over-verified semantic units | 15 |

Interpretation is intentionally deferred until semantic answer judgment is frozen. A semantic-unit miss does not automatically imply a decision-quality miss, as demonstrated by the earlier file-level baseline.

## Context economics

Mean reconstructed context per case:

| Category | Prototype A |
|---|---:|
| total chars | 107,747 |
| control plane | 89,192 |
| routing metadata | 10,414 |
| structural metadata | 2,761 |
| specialist doctrine | 5,380 |

Frozen 30-case baselines for comparison:

| Metric | `current` | `current_plus_map` | Prototype A smoke |
|---|---:|---:|---:|
| total chars/case | 130,511 | 137,128 | **107,747** |
| control-plane chars/case | 92,751 | 91,985 | **89,192** |
| routing-metadata chars/case | 0 | 17,337 | **10,414** |
| specialist-doctrine chars/case | 27,136 | 20,589 | **5,380** |

Directional deltas, noting the smoke has only six deliberately difficult cases:

- total context: **−17.4% vs `current`**; **−21.4% vs `current_plus_map`**;
- routing metadata: **−39.9% vs `current_plus_map`**;
- specialist doctrine: **−80.2% vs `current`**; **−73.9% vs `current_plus_map`**;
- non-bootstrap context in Prototype A is `18,555` chars/case, versus ~`37,760` in `current` and ~`45,143` in `current_plus_map`.

The control-plane tax remains ~89k chars/case and therefore still dominates total context. It remains intentionally unchanged in Prototype A so retrieval and bootstrap effects are not confounded.

## Current diagnosis

Prototype A has **passed the context-economics direction test** but has **not yet passed the retrieval-quality gate**.

The positive result is strong: addressable semantic metadata + section-level doctrine retrieval materially reduces specialist/context consumption.

The unresolved result is also clear: 0.477 semantic precision and 15 over-verified units indicate candidate selection is still too broad, while two cases are not at full verified semantic recall.

Do not tune the retriever from these aggregate scores alone.

## Next gate

Freeze an answer-only judgment bundle from the six existing traces before inspecting per-case retrieval misses/over-retrieval.

Sequence:

1. judge answer quality against required checks without per-case retrieval metadata;
2. freeze semantic answer judgments;
3. only then inspect per-case selected/verified units and context operations;
4. classify each issue as `DISCOVERY_MISS`, `SELECTION_OVERBREADTH`, `VERIFICATION_MISS`, `SYNTHESIS_MISS`, `GOLD_PROBLEM`, or `NO_MATERIAL_FAILURE`;
5. modify Prototype A only from that decomposition;
6. do not run all 30 cases until the smoke failure modes are understood.

No change to `merenda/` or `merenda/DECISION_ROUTER.md` is justified by this smoke result.
