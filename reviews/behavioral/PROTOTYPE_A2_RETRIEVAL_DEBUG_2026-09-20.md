# Prototype A2 — Retrieval Debug

Date: 2026-09-20
Status: FROZEN DEBUG RESULT
Tested commit: `22af25f435b1d40009915f2b6062cde82ce0d97c`
Cases: R002, R008, R019, R020, R027, R030

## Answer judgment already frozen

Before this retrieval debug was inspected, the answer-only judgment was frozen:

- required checks satisfied: 18/19 = 94.74%;
- full-pass cases: 5/6;
- material decision inversions: 0;
- only answer miss: R027 does not distinguish transactional partnership from structural/complementary integration.

This report therefore attributes causes without changing the answer judgment.

## Aggregate A2 result

- verified semantic recall: 0.9028;
- focused verified semantic precision: 0.7431;
- full-recall cases: 4/6;
- focused over-verified units: 10;
- mean reconstructed context: 112,671 chars/case;
- routing metadata: 11,657 chars/case;
- structural metadata: 3,022 chars/case;
- specialist doctrine: 8,800 chars/case;
- control plane: 89,192 chars/case.

Compared with A1, A2 uses more context without improving aggregate semantic recall or answer-check recall.

## Per-case decomposition

### R002 — PASS WITH ONE GENERIC EXTRA

Selected: source/intent match, offer/CTA, positioning difference, plus MARKET.APPROPRIATENESS.

The answer is correct. MARKET.APPROPRIATENESS is extra for this case. No material failure.

Classification: `SELECTION_OVERBREADTH`, non-material.

### R008 — PASS

A2 improves over A1 by selecting only the three required semantic units and reducing section reads/context.

Classification: `NO_MATERIAL_FAILURE`.

### R019 — MAJOR SELECTION VARIANCE / OVERBREADTH

A1 selected only `ECONOMICS.ACQUISITION_CONSTRAINTS_RELATION_MIX` and solved the case.

A2 selected six units: the required economic-mix unit plus active-vs-latent demand, analog conditionality, owned demand, identifiability and appropriateness. This increased case context by ~28k chars with no answer-quality gain.

Classification: `SELECTION_OVERBREADTH` driven by agentic selection variance.

### R020 — RETRIEVAL MISS WITHOUT ANSWER FAILURE

Selected/verified proof specificity and authority/credibility/trust, but not `POSITIONING.OPERATIONAL_DIFFERENCE`.

The answer nevertheless keeps positioning as a distinct upstream gate and passes all required checks.

Classification: `DISCOVERY_OR_SELECTION_MISS` + `NO_MATERIAL_FAILURE`.

### R027 — SELECTION FIXED, SYNTHESIS STILL FAILS

A2 successfully selects and canonically verifies `PARTNERSHIP.STRUCTURAL_VS_TRANSACTIONAL`, fixing the A1 selection miss.

However the final answer still omits the transactional-vs-structural distinction. Therefore the remaining failure is not retrieval of that unit: it is synthesis/application.

A2 also fails to select `PARTNERSHIP.HOST_TRUST`, although the final answer still protects borrowed trust/reputation. The canonical doctrine confirms that partner win, partnership type and host-trust protection are distinct semantic jobs, so the gold is not collapsed merely to improve the score.

A2 further over-selects generic market/economics/offer/positioning units, taking the case from 5 semantic-entry reads in A1 to 8 in A2.

Classification:
- `SYNTHESIS_MISS` on STRUCTURAL_VS_TRANSACTIONAL;
- `SELECTION_MISS` on HOST_TRUST, behaviorally non-material in this trace;
- `SELECTION_OVERBREADTH` on generic units.

### R030 — PASS

Exact required semantic units selected. No material failure.

Classification: `NO_MATERIAL_FAILURE`.

## Causal finding

The remaining bottleneck is not structural-index coverage and not lack of semantic units.

It is now the combination of:

1. **agentic candidate-selection variance** — the same architecture can choose 1 unit in one run and 6 in another for an equivalent case;
2. **generic-unit drift** — broad market/positioning/economics units can crowd out more specific case-matched units and raise context cost;
3. **application/synthesis loss** — a unit can be selected and canonically verified but still fail to appear in the final diagnosis.

Therefore adding more semantic units or more doctrine would be the wrong response.

## Decision for A3

Prototype A3 will change runtime discipline, not doctrine:

- begin with at most four primary semantic candidates;
- prefer the most case-specific semantic units over generic upstream/gate units;
- exceed the initial candidate budget only for a justified upstream, conditional `must_read_with`, or structural blind-spot expansion;
- when a conditional `must_read_with` condition is visibly true, fetch and verify it;
- before final answer, perform an application audit: every selected + canonically verified gate/distinction that materially applies must be represented in the diagnosis, while non-material retrieved units must not be forced into the answer;
- extend the revenue-share runtime dependency to include host-trust protection when borrowed audience/trust is involved.

No change to canonical doctrine or `merenda/DECISION_ROUTER.md` is justified.
