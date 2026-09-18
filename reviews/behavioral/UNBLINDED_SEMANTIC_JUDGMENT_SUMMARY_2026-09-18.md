# Unblinded Semantic Judgment — Behavioral Baseline

Date: 2026-09-18
Status: COMPLETE
Baseline commit tested: `4506e67e812c4e3270c4446d58f6a3d8c3934e82`
Blind judgment: `reviews/behavioral/BLIND_SEMANTIC_JUDGMENT_2026-09-18.jsonl`
Blind freeze summary: `reviews/behavioral/BLIND_SEMANTIC_JUDGMENT_SUMMARY_2026-09-18.md`
Unblind mapping: `reviews/behavioral/UNBLIND_MAPPING_2026-09-18.json`

## Integrity of the comparison

The A/B judgments were frozen before the mapping to `current` and `current_plus_map` was revealed. The unblinding therefore remaps already-frozen judgments; it does not re-grade the answers.

## Deterministic retrieval metrics

| Architecture | Required-node recall | Relevant retrieval precision | Over-retrieved nodes |
|---|---:|---:|---:|
| `current` | 0.7472 | 0.7644 | 24 |
| `current_plus_map` | 0.6778 | 0.8000 | 14 |

At file level, `current_plus_map` looks worse on recall but better on precision and over-retrieval.

## Semantic judgment metrics after unblinding

Each architecture had 96 required semantic checks across the 30 cases.

| Architecture | Checks satisfied | Required-check recall | Material decision inversions | Discovery misses | Retrieval-correct synthesis misses |
|---|---:|---:|---:|---:|---:|
| `current` | 93/96 | 96.875% | 0 | 2 | 1 |
| `current_plus_map` | 95/96 | 98.958% | 0 | 0 | 1 |

For both architectures:

- forbidden shortcuts triggered: 0;
- provenance errors: 0;
- unsupported inference failures: 0;
- premature tactic failures: 0;
- founder accommodation failures: 0.

## Semantic misses by architecture

### `current`

- `R019`: did not explicitly shift enough of the economic mix toward retention/cross-sell/conversion under acquisition constraints. Classified `DISCOVERY_MISS`.
- `R027`: omitted the distinction between transactional partnership and structural combination even though the partnership node was retrieved. Classified `CORRECT_RETRIEVAL_BAD_SYNTHESIS`.
- `R030`: did not explicitly ground event audience selection in customer economics/appropriateness. Classified `DISCOVERY_MISS`.

### `current_plus_map`

- `R027`: same omission on transactional partnership vs structural combination. Classified `CORRECT_RETRIEVAL_BAD_SYNTHESIS`.

No miss in either architecture was judged a material inversion of the final business decision.

## File-level gold is materially too coarse

`GOLD_TOO_COARSE` was assigned when one or more required file-level nodes were not retrieved but the required semantic checks were nevertheless satisfied.

After unblinding:

- `current`: 14/30 case-responses classified `GOLD_TOO_COARSE`;
- `current_plus_map`: 18/30 case-responses classified `GOLD_TOO_COARSE`.

This explains a substantial part of the apparent node-recall degradation of `current_plus_map`: the Map often retrieved less at file level while still preserving the required decision logic.

The strongest known instrumentation mismatch remains `R013`, where control-plane files appear in `required_nodes` even though the runner intentionally excludes mandatory control-plane reads from specialist `retrieved_nodes`.

## Interpretation

### RESULT 1 — The hypothesis “Map v1 worsens behavioral quality” is not supported

The deterministic node metric suggested a recall regression. The semantic judgment does not reproduce that regression.

On this suite, `current_plus_map`:

- satisfies 2 more required checks than `current`;
- eliminates the two discovery misses observed in `current`;
- reduces over-retrieval from 24 to 14 nodes;
- improves relevant retrieval precision from 0.7644 to 0.8000;
- has no additional material or epistemic failure.

This is directional evidence in favor of the Map as a routing/precision signal, not proof that Map v1 should be adopted unchanged.

### RESULT 2 — Required-node recall is not an adequate primary success metric

A file is an editorial container, not necessarily the semantic unit needed for a decision. File-level recall penalizes selective retrieval when:

- the needed principle lives in one section;
- another canonical section carries an equivalent invariant;
- the control plane already carries the required rule;
- multiple gold files overlap semantically.

The primary eval must therefore move to stable semantic-unit IDs plus section-level evidence.

### RESULT 3 — The residual failure types are now much narrower

The observed residual problems are not broad routing collapse:

- `current` has two real discovery misses;
- both architectures share one synthesis miss on the same case;
- there are no observed material decision inversions.

This changes the architecture priority from “repair recall broadly” to “improve semantic-unit discovery while reducing context cost, then separately harden synthesis checks.”

## Decision

### Map v1 remains experimental, but its role is upgraded

Do not adopt Map v1 directly into the current control plane yet.

However, do not treat it as a failed approach. The behavioral evidence supports retaining it as one input to the next retriever because it appears to improve precision and discovery without degrading semantic decision quality on this suite.

The next architecture should use the Map as a **precision / causal-routing signal**, not as an exclusive filter.

### Router v2 remains deferred

The evidence does not justify rewriting `DECISION_ROUTER.md` yet. The main measurable problem is now retrieval granularity/context economics, not demonstrated failure of the Router's decision doctrine.

## Next gate

Proceed with:

1. semantic-unit gold migration;
2. generated Structural Index validation;
3. context/token instrumentation;
4. Hierarchical Retriever prototype A using `Decision Map + Structural Index + recall safety net`;
5. A/B against the frozen `current` baseline using semantic fidelity + context cost.

Do not add Map entries merely to improve the existing 30-case file-level score.
