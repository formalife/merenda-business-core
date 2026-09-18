# Blind Semantic Judgment — Behavioral Baseline

Date: 2026-09-18
Status: FROZEN BEFORE UNBLINDING
Source bundle SHA-256: `ee67e65c16a5d9164e184bbba9f60a69378c49de2ed6eca9984c6ad2dc325da7`
Judgment file: `reviews/behavioral/BLIND_SEMANTIC_JUDGMENT_2026-09-18.jsonl`

## Method

The reviewer saw only per-case blind labels `A` and `B`. The mapping to `current` / `current_plus_map` was not available during judgment.

Each response was evaluated against:

- `required_checks`;
- `forbidden_shortcuts`;
- provenance requirements;
- unsupported inference;
- premature tactic;
- founder accommodation failure;
- observed retrieval trace.

File-level node recall was not treated as semantic failure when the answer demonstrably satisfied the required concept/check through another canonical section or control-plane reasoning.

## Blind aggregate

Because A/B are randomized independently per case, these aggregate labels are NOT architecture-level results and must not be interpreted as such before unblinding.

### Blind A

- cases: 30
- required checks: 96
- checks satisfied: 93
- check recall: 96.875%
- material failures: 0
- forbidden shortcuts triggered: 0
- provenance errors: 0
- unsupported inference: 0
- premature tactic: 0
- founder accommodation failures: 0
- failure classification counts:
  - `GOLD_TOO_COARSE`: 15
  - `DISCOVERY_MISS`: 2
  - `CORRECT_RETRIEVAL_BAD_SYNTHESIS`: 1

### Blind B

- cases: 30
- required checks: 96
- checks satisfied: 95
- check recall: 98.958%
- material failures: 0
- forbidden shortcuts triggered: 0
- provenance errors: 0
- unsupported inference: 0
- premature tactic: 0
- founder accommodation failures: 0
- failure classification counts:
  - `GOLD_TOO_COARSE`: 17
  - `CORRECT_RETRIEVAL_BAD_SYNTHESIS`: 1

## Semantic misses observed

Only four required-check misses were judged across the 60 blind responses:

- `R019/A`: did not explicitly shift enough of the economic mix toward retention/cross-sell/conversion under acquisition constraints.
- `R027/A`: omitted the distinction between transactional partnership and structural combination.
- `R027/B`: same omission.
- `R030/A`: event audience selection was not explicitly grounded in customer economics/appropriateness.

None of these was judged a material decision inversion in the final answer.

## Main finding before unblinding

The deterministic file-level node recall materially overstates behavioral failure in this suite.

A large number of cases miss one or more file-level gold nodes while still satisfying all required semantic checks. This occurs because:

1. multiple canonical files overlap at the principle level;
2. a specific section can supply the necessary principle without the full set of gold files;
3. the control plane can sometimes carry the required invariant even when a specialist node is not opened;
4. at least one case (`R013`) includes control-plane files in `required_nodes` even though the behavioral runner intentionally excludes control-plane files from `retrieved_nodes` instrumentation.

This supports replacing file-level gold as the primary retrieval unit with stable semantic-unit IDs and section-level evidence.

## Gate

Do not interpret A/B as `current` or `current_plus_map` until the separate mapping file is supplied after this judgment is frozen.

After unblinding:

1. remap the 60 frozen judgments to the real architectures;
2. compute semantic metrics per architecture;
3. compare semantic quality against deterministic node recall, precision and over-retrieval;
4. classify which apparent node misses are real discovery failures versus file-level metric artifacts;
5. use those results to design semantic-unit gold and the first hierarchical retrieval experiment.
