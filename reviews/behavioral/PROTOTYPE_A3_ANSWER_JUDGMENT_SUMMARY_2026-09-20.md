# Prototype A3 — Answer-only Judgment

Date: 2026-09-20
Status: FROZEN BEFORE RETRIEVAL DEBUG
Tested commit: `5e036f01a01eace4d3d764a43a059a96f2f00226`
Cases: `R002`, `R008`, `R019`, `R020`, `R027`, `R030`

## Result

| Metric | A3 answer-only |
|---|---:|
| required checks satisfied | 18/19 = 94.74% |
| full-pass cases | 5/6 |
| material decision inversions | 0 |
| forbidden shortcuts | 0 |
| provenance errors | 0 |
| unsupported inferences | 0 |
| premature tactics | 0 |
| founder-accommodation failures | 0 |

## Case judgments

- `R002` — PASS, 3/3.
- `R008` — PASS, 3/3.
- `R019` — PASS, 3/3.
- `R020` — PARTIAL PASS, 2/3. The answer separates generic satisfaction from specific proof and distinguishes authority/credibility/trust, but it does not explicitly preserve differentiation/positioning as a distinct job. Immediate decision remains conservative, so there is no material inversion.
- `R027` — PASS, 4/4. The previous transactional-vs-structural gap is closed; the answer now distinguishes a bounded transactional audience deal from a durable integration of complementary assets.
- `R030` — PASS, 3/3.

## Interpretation frozen before debug

A3 improves deterministic semantic retrieval versus A1/A2, and it closes the previously persistent R027 answer gap. However, aggregate answer-check fidelity does not improve because a different omission appears in R020.

This means the next diagnostic question is not whether A3 is globally better or worse from aggregate scores alone. Retrieval debug must determine whether R020 failed because `POSITIONING.OPERATIONAL_DIFFERENCE` was not selected/verified, or because it was retrieved but not applied. The same debug should verify whether A3's higher semantic recall came from disciplined focused retrieval rather than broader context spend.

Do not modify semantic gold or doctrine before this attribution step.
