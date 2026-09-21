# Prototype A3 — Retrieval Debug

Date: 2026-09-20
Tested commit: `5e036f01a01eace4d3d764a43a059a96f2f00226`
Cases: R002, R008, R019, R020, R027, R030

## Frozen answer judgment

Answer-only judgment was frozen before opening retrieval debug.

- Required checks satisfied: 18/19 = 94.74%
- Full answer passes: 5/6
- Material decision inversions: 0
- Forbidden shortcuts: 0
- Provenance errors: 0
- Unsupported inference failures: 0
- Premature tactic failures: 0

The only answer miss was R020: the answer correctly separated generic five-star satisfaction from specific proof and separated proof from authority/trust, but it did not explicitly preserve positioning/differentiation as a separate upstream job before moving to acquisition.

## Deterministic retrieval result

Smoke summary:

- mean verified semantic recall: 0.9444
- mean focused verified semantic precision: 0.8889
- full verified recall cases: 5/6
- focused over-verified units: 3
- mean reconstructed context chars: 110,373
- routing metadata chars/case: 11,499
- structural metadata chars/case: 3,102
- specialist doctrine chars/case: 6,580
- fixed control-plane chars/case: 89,192

## Failure decomposition

### R020 — true selection miss -> answer miss

Selected semantic units:

- `AUTHORITY.CREDIBILITY_TRUST_DISTINCT`
- `PROOF.SPECIFIC_RESULT_EVIDENCE`

The runner did not select or canonically read `POSITIONING.OPERATIONAL_DIFFERENCE`.

This matches the frozen answer miss: the final answer distinguished proof from authority/trust but did not explicitly preserve differentiation/positioning as a separate upstream job.

Classification: **SELECTION_MISS -> ANSWER_MISS**.

This is the only required-semantic-unit miss in A3.

### R027 — previous failure resolved

A3 selected and canonically verified:

- `PARTNERSHIP.REVENUE_SHARE_ECONOMICS`
- `PARTNERSHIP.PARTNER_WIN`
- `PARTNERSHIP.HOST_TRUST`
- `PARTNERSHIP.STRUCTURAL_VS_TRANSACTIONAL`

The frozen answer applied the structural-vs-transactional distinction and host-trust economics correctly. The previous R027 synthesis gap is therefore resolved in A3.

### Other cases

R002, R008, R019 and R030 produced no material answer failure. Some non-required semantic candidates were selected, but the A3 selection discipline materially reduced the broad over-selection observed in A2.

## Interpretation

Prototype A3 materially improves focused routing quality relative to A1/A2 while preserving the context advantage over the original behavioral baselines. The remaining observed failure is narrow and causally localized: generic proof/authority routing can still omit positioning when the founder uses positive reviews as permission to skip directly to acquisition.

The correct intervention is not a broader prompt or more doctrine. It is a conditional runtime relation:

`PROOF.SPECIFIC_RESULT_EVIDENCE -> POSITIONING.OPERATIONAL_DIFFERENCE`

when testimonials/reviews are being used to conclude that upstream commercial prerequisites are solved and that the system can move directly to acquisition.

This relation is already supported by canonical Layer 1: proof/authority do not substitute for positioning/differentiation.

## Decision

- Keep A3 retrieval discipline.
- Do not modify canonical `merenda/` doctrine or `DECISION_ROUTER.md`.
- Add the narrow conditional runtime relation above.
- Retest R020 plus R027 as a regression guard before spending credits on the full 30-case run.
- Do not alter semantic gold to make the current output pass.
