# Prototype A31 — Focused answer judgment

Date: 2026-09-20
Tested commit: `feea964d1e807d289cda3fa8d3e785bcc1422a41`
Cases: `R020`, `R027`

## Frozen answer-only result

The answer judgment was frozen before inspecting any A31 retrieval-debug bundle.

- Required checks satisfied: **7/7 = 100%**
- Full-pass cases: **2/2**
- Forbidden shortcuts: **0**
- Provenance errors: **0**
- Unsupported inference: **0**
- Premature tactics: **0**
- Founder-accommodation failures: **0**
- Material decision inversions: **0**

### R020

PASS, 3/3 required checks.

The response now keeps four jobs separate: generic satisfaction, specific evidence, authority/credibility/trust, and operational differentiation. It does not use reviews as a substitute for positioning and links proof to concrete claims, risks and objections.

### R027

PASS, 4/4 required checks.

The response preserves partner win, transactional-vs-structural classification, revenue-share economics/risk/control, and host-trust protection.

## Retrieval score reported by the frozen run

- semantic verified recall: **1.0000**
- focused verified precision: **0.9000**
- full-recall cases: **2/2**
- focused over-verified: **1**
- mean reconstructed context: **113,488 chars/case**
- routing metadata: **12,050 chars/case**
- structural metadata: **1,984 chars/case**
- specialist doctrine: **10,262 chars/case**
- control plane: **89,192 chars/case**

## Decision

The known R020/R027 regression pair is closed. Do not tune further on these cases before a broader run.

Next gate: run Prototype A3 across all 30 existing cases, freeze traces, judge answers separately from retrieval diagnostics, then compare behavioral fidelity and context economics against `current` and `current_plus_map`.

This focused retest is evidence that the known defects were repaired, not evidence of generalization. Final architecture adoption still requires broader evaluation and a blind holdout.
