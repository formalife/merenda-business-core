# Prototype A2 — Answer-Only Judgment Summary

Date: 2026-09-20
Status: FROZEN BEFORE RETRIEVAL DEBUG
Tested commit: `22af25f435b1d40009915f2b6062cde82ce0d97c`
Cases: `R002`, `R008`, `R019`, `R020`, `R027`, `R030`

## Result

- required checks satisfied: **18/19 = 94.74%**
- full-pass cases: **5/6**
- partial-pass cases: **1/6** (`R027`)
- forbidden shortcuts: **0**
- provenance errors: **0**
- unsupported inferences: **0**
- premature tactics: **0**
- founder accommodation failures: **0**
- material decision inversions: **0**

## Case outcome

| Case | Judgment | Miss |
|---|---|---|
| R002 | PASS | none |
| R008 | PASS | none |
| R019 | PASS | none |
| R020 | PASS | none |
| R027 | PARTIAL_PASS | transactional partnership vs structural/complementary integration |
| R030 | PASS | none |

## Interpretation before retrieval debug

Prototype A2 does **not** show a general answer-quality regression. Its semantic answer fidelity on this smoke remains effectively identical to Prototype A1.

The runtime patch tested in A2 has therefore **not yet demonstrated a behavioral fix** for the known R027 gap: the answer still fails to distinguish a transactional partnership from a structural/complementary integration.

Do not infer the retrieval cause from this answer-only result. The A2 retrieval-debug bundle must be inspected only after this judgment is frozen.

## Smoke metrics reported by runner

- mean verified semantic recall: `0.9028`
- reported verified precision: `0.7431`
- full verified recall: `4/6`
- reported over-verified units: `10`
- mean total context chars: `112,671`
- routing metadata chars: `11,657`
- structural metadata chars: `3,022`
- specialist doctrine chars: `8,800`
- control-plane chars: `89,192`

These retrieval/context metrics are recorded here for chronology but were **not used to alter the answer-only judgments above**.
