# Architecture Implementation Roadmap v2 — Unblinded Addendum

Date: 2026-09-18
Status: ACTIVE ADDENDUM
Applies to: `reviews/ARCHITECTURE_IMPLEMENTATION_ROADMAP_V2.md`

## Why this addendum exists

The roadmap was written after deterministic retrieval scoring but before semantic unblinding. The frozen semantic judgment now changes the interpretation of the behavioral baseline.

Canonical result report:

`reviews/behavioral/UNBLINDED_SEMANTIC_JUDGMENT_SUMMARY_2026-09-18.md`

## Phase 0 — CLOSED

Behavioral semantic decomposition is complete.

Unblinded results:

| Architecture | Required-check recall | Discovery misses | Synthesis misses | Material inversions |
|---|---:|---:|---:|---:|
| `current` | 93/96 = 96.875% | 2 | 1 | 0 |
| `current_plus_map` | 95/96 = 98.958% | 0 | 1 | 0 |

Deterministic retrieval remained:

| Architecture | Node recall | Precision | Over-retrieved |
|---|---:|---:|---:|
| `current` | 0.7472 | 0.7644 | 24 |
| `current_plus_map` | 0.6778 | 0.8000 | 14 |

## Revised interpretation

The apparent node-recall regression of `current_plus_map` does not correspond to a semantic decision-quality regression in this suite.

Instead:

- file-level gold is materially too coarse;
- selective retrieval is often penalized even when the necessary principle is applied correctly;
- `current_plus_map` shows directional evidence of better discovery/precision with less over-retrieval;
- the Map should not be adopted unchanged, but it should remain a routing/precision signal in the next prototype;
- no evidence currently justifies Router v2.

`GOLD_TOO_COARSE` occurred in 14/30 `current` responses and 18/30 `current_plus_map` responses.

## Revised decisions

### DECISION — Map v1 is retained as experimental routing metadata

Supersedes the interpretation that Map v1 was a behavioral failure.

Map v1 is still **not adopted into the production/current control plane**, but the next retriever will use its causal metadata as one candidate-selection signal.

It must not be an exclusive filter; structural discovery provides the recall safety net.

### DECISION — Semantic units become the primary eval retrieval target

`required_nodes` remains only for historical comparison and debugging.

New evaluation work targets stable semantic IDs and canonical section evidence.

### DECISION — Phase order

Active order is now:

1. Phase 1: validate generated Structural Index;
2. Phase 2: build semantic-unit gold v2;
3. Phase 3: add context-economics instrumentation;
4. Phase 4: build Hierarchical Retriever prototype A;
5. Phase 5: test Compact Reasoning Kernel only after the retriever is stable.

## Acceptance direction for Prototype A

Prototype A must be compared against the frozen `current` baseline and should target:

- semantic required-check recall at least as high as the strongest observed baseline;
- no increase in material/epistemic failures;
- retrieval precision at least comparable to `current_plus_map`;
- lower or equal doctrine context consumption than the current full-file approach;
- no exclusive dependence on manually curated Map coverage.

No threshold is promoted to a permanent architecture contract until context-cost instrumentation exists.
