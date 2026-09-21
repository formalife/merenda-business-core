# Prototype A — Answer-Only Semantic Judgment

Date: 2026-09-20
Status: FROZEN BEFORE RETRIEVAL DEBUG
Tested smoke commit: `f26417c0a84f673cf97687a8dea3aa896f0584a7`
Cases: R002, R008, R019, R020, R027, R030

## Method

Judgment was performed from the answer-only bundle. Per-case selected/verified semantic IDs, retrieval misses, over-retrieval and context operations were intentionally not inspected before freezing these judgments.

Primary comparison is against the original case `required_checks`, `forbidden_shortcuts`, expected behavior and provenance requirements.

## Result

- cases PASS: **5/6**
- cases PARTIAL_PASS: **1/6**
- required checks satisfied: **18/19 = 94.74%**
- required checks missed: **1/19**
- material decision inversions: **0**
- forbidden shortcuts triggered: **0**
- provenance errors: **0**
- unsupported inferences: **0**
- premature tactics: **0**
- founder-accommodation failures: **0**

## Single answer-level miss

### R027 — partnership

Satisfied:

- partner economic/reputational win;
- revenue-share cost/risk/economics allocation;
- host trust/reputation protection.

Missed:

- explicit distinction between **transactional partnership** and **structural/complementary integration**.

The immediate decision is still correct: do not approve/scale from audience size alone; test with measurable economics and clear responsibilities. Therefore this is a synthesis completeness miss, not a material decision inversion.

This repeats the R027 synthesis gap already observed in the earlier baseline.

## R020 note

R020 may still have a retrieval-level miss, but the answer itself is acceptable against the required checks: it separates generic five-star satisfaction from specific proof, distinguishes authority/credibility/trust, and keeps positioning as a separate upstream gate. The distinction from differentiation is less explicit than ideal, but no required check is judged failed at answer level.

## Interpretation before debug

Prototype A does **not** show a broad answer-quality regression on this smoke set.

Combined with the frozen deterministic result:

- answer required-check recall: **94.74%**;
- deterministic verified semantic recall: **90.28%**;
- context total: **107,747 chars/case**;
- specialist doctrine: **5,380 chars/case**.

This creates two hypotheses to test only after opening retrieval debug:

1. at least one deterministic semantic miss did not materially damage the answer (likely `NO_MATERIAL_FAILURE` / gold or equivalent-coverage issue);
2. R027 remains a genuine synthesis or retrieval-to-synthesis failure that must be localized before tuning.

Do not modify Prototype A before retrieval-debug decomposition.
