# Hierarchical Retriever Prototype A — Retrieval Debug Decomposition

Date: 2026-09-20
Status: FROZEN DEBUG RESULT
Tested commit: `f26417c0a84f673cf97687a8dea3aa896f0584a7`
Answer-only judgment was frozen before this debug bundle was opened.

## Executive result

The smoke result does **not** support a broad retriever regression.

Two different effects were mixed in the aggregate metrics:

1. one real selection/synthesis miss (`R027`);
2. a measurement artifact that inflated verified over-retrieval and depressed precision.

The context-economics result remains valid: Prototype A materially reduced specialist doctrine and total reconstructed context.

## Measurement artifact — verified precision

The Prototype A runner marked a semantic unit as `verified` whenever its canonical path had been read in full.

Because the five control-plane documents are mandatory full reads for every case, the two zero-based semantic units whose canonical sources are in the control plane were passively marked `verified` in every smoke case even when they had **not** been selected by the retriever.

This created:

- `2 passive bootstrap units × 6 cases = 12` false over-verified units;
- reported over-verified units: `15`;
- actual focused over-verified routing choices: `3`.

The three real focused extras are:

- `R008`: `MARKET.APPROPRIATENESS`;
- `R027`: `MARKET.APPROPRIATENESS`;
- `R027`: `MARKET.VALIDITY_GATE`.

If precision is calculated over semantic units that were both **selected and canonically verified**, the six-case mean is approximately `0.8917`, not `0.4770`.

The raw verified set remains useful for recall/exposure diagnostics, but it must not be used directly as the precision denominator when mandatory bootstrap reads can verify unrelated units passively.

## Case decomposition

### R002 — NO_MATERIAL_FAILURE

Required semantic units were selected and canonically verified.

`MARKET.APPROPRIATENESS` was selected but not pursued to canonical verification. The answer correctly diagnosed traffic intent/awareness, operational differentiation, offer and CTA before UI micro-optimization.

Classification: `NO_MATERIAL_FAILURE`.

### R008 — SELECTION_OVERBREADTH, no answer failure

All required semantic units were selected and verified:

- `MARKET.NATURAL_CUSTOMER_EXPIRY`;
- `CUSTOMER.SUCCESS_BEFORE_RETENTION_TACTIC`;
- `CUSTOMER.SECOND_PURCHASE_BRIDGE`.

`MARKET.APPROPRIATENESS` was additionally selected and verified. This was not needed by the semantic gold or the frozen answer judgment and generated extra doctrine reads.

Classification: `SELECTION_OVERBREADTH` with `NO_MATERIAL_FAILURE`.

Do not optimize this yet at the expense of recall.

### R019 — NO_MATERIAL_FAILURE / minimal retrieval

Prototype A selected and verified only `ECONOMICS.ACQUISITION_CONSTRAINTS_RELATION_MIX`, opened exactly the canonical section, and produced a full answer pass.

Classification: `NO_MATERIAL_FAILURE`.

This is the strongest example in the smoke of the desired progressive-disclosure behavior.

### R020 — CANONICAL_RETRIEVAL_MISS, no answer failure

Required semantic gold:

- `PROOF.SPECIFIC_RESULT_EVIDENCE`;
- `AUTHORITY.CREDIBILITY_TRUST_DISTINCT`;
- `POSITIONING.OPERATIONAL_DIFFERENCE`.

Prototype A selected and verified the first two but not `POSITIONING.OPERATIONAL_DIFFERENCE`.

The frozen answer judgment nevertheless passed all required checks because the fixed control plane preserved positioning as a separate upstream gate and the answer explicitly did not collapse reviews into differentiation.

Classification: `CANONICAL_RETRIEVAL_MISS` + `NO_MATERIAL_FAILURE`.

This should **not** be repaired by forcing every concept already present in the control plane to trigger an additional specialist read. Keep semantic retrieval recall and answer/check fidelity as separate metrics.

### R027 — SELECTION_MISS → SYNTHESIS_MISS

Required semantic gold:

- `PARTNERSHIP.PARTNER_WIN`;
- `PARTNERSHIP.STRUCTURAL_VS_TRANSACTIONAL`;
- `PARTNERSHIP.REVENUE_SHARE_ECONOMICS`;
- `PARTNERSHIP.HOST_TRUST`.

Prototype A selected and verified:

- `PARTNERSHIP.PARTNER_WIN`;
- `PARTNERSHIP.REVENUE_SHARE_ECONOMICS`;
- `PARTNERSHIP.HOST_TRUST`;

but never selected `PARTNERSHIP.STRUCTURAL_VS_TRANSACTIONAL`.

The unit existed in the compact index, so this is not an addressability/discovery-store failure. It is a **candidate-selection failure**. The structural safety net was not invoked because the model considered the semantic candidates sufficient.

The frozen answer judgment missed exactly the corresponding required check: distinguishing a transactional partnership from a structural/complementary integration.

Classification: `SELECTION_MISS` → `SYNTHESIS_MISS`.

Corrective action: add a **general conditional semantic dependency** from revenue-share evaluation to partnership-type classification when the proposal is framed as audience access / revenue share and structural integration has not yet been established. This is a doctrine-supported relation, not an R027-specific keyword rule.

### R030 — NO_MATERIAL_FAILURE

Both required semantic units were selected and verified. The answer passed all checks and the retrieval remained section-level with no full-node fallback.

Classification: `NO_MATERIAL_FAILURE`.

## Architecture decision after debug

Do **not** broadly tighten Prototype A yet.

The evidence supports only two immediate changes:

1. fix semantic precision instrumentation so mandatory bootstrap exposure does not count as focused over-retrieval;
2. strengthen the conditional semantic graph around revenue-share partnerships so `PARTNERSHIP.STRUCTURAL_VS_TRANSACTIONAL` becomes a conditional companion when partnership type is unresolved.

Do not:

- remove the Structural Index safety net;
- reduce candidate count globally from a six-case smoke;
- change canonical doctrine;
- rewrite the Decision Router;
- add embeddings/reranking;
- run the full 30-case suite before a second smoke confirms the R027 fix without fidelity/cost regression.

## Next gate

Prototype A2 smoke on the same six cases, new isolated workdir, same model and full bootstrap.

Primary acceptance:

- answer required-check recall: no regression from `18/19` and ideally `19/19` by recovering R027;
- no material decision inversion;
- focused semantic precision approximately comparable to or above corrected Prototype A (~`0.89` directional smoke figure);
- total context remains materially below frozen baseline;
- no full-node fallback explosion.
