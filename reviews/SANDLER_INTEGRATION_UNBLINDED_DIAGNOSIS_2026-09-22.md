# Sandler Integration — Unblinded Diagnosis — 2026-09-22

## Stato

**DIAGNOSTIC RESULT — EVAL CORRECTED, FULL RERUN REQUIRED**

Original tested head:

`21081371299f4bcbcc47227be7e9ded9c6373abd`

Corrected integration head after diagnostic fixes:

`c12b421e18ec32c386b3778141c8bda87d083a33`

## Frozen original result

The blinded judgment was frozen before unblinding.

Unblinding established:

- FULL = 11/11 behavioral PASS;
- KERNEL = 9/11 behavioral PASS;
- Kernel material failures: R033 and R041;
- provenance failures: 0.

## Trace diagnosis

### R033

FULL selected and verified:

- `SALES.PAIN_QUALIFICATION`;
- `SALES.DIAGNOSE_BEFORE_PRESCRIBE`;
- `SALES.FULFILLMENT_DECISION`.

FULL response preserved the causal transition:

Pain → investment/Budget → Decision process → selective demo.

KERNEL selected and verified only:

- `SALES.PAIN_QUALIFICATION`;
- `SALES.DIAGNOSE_BEFORE_PRESCRIBE`.

KERNEL then moved from qualified Pain directly to selective demo.

The prior semantic gold required only `SALES.PAIN_QUALIFICATION`, even though the behavioral requirement explicitly required the remaining qualification gates before demo.

Diagnosis:

**GOLD_TOO_COARSE + ROUTING DEPENDENCY TOO WEAK.**

### R041

Both variants retrieved the Customer Success / Account Growth area.

FULL made stakeholder, investment and re-entry into the normal commercial process explicit.

KERNEL verified realized value and a new need but moved from need qualification toward proposal without making Budget/investment and Decision process mandatory.

The Account Growth semantic entry already said that a new opportunity re-enters normal qualification, but the prior gold made Pain optional and omitted Budget/Decision from required units.

Diagnosis:

**GOLD_TOO_COARSE + ROUTING DEPENDENCY TOO WEAK.**

## Corrections applied

On the corrected head:

1. R033 semantic gold now requires:
   - Pain;
   - Budget;
   - Decision;
   - Fulfillment.
2. R041 semantic gold now requires:
   - Customer Success;
   - Account Growth;
   - Pain;
   - Budget;
   - Decision.
3. `SALES.PAIN_QUALIFICATION` now conditionally routes to Budget, Decision and Fulfillment when the seller is moving toward a concrete solution/demo/proposal.
4. `CUSTOMER.ACCOUNT_GROWTH_VALUE` now conditionally routes to Pain, Budget and Decision for a new expansion opportunity.

Details: `reviews/SANDLER_INTEGRATION_EVAL_CORRECTION_2026-09-22.md`.

## Kernel decision

`REASONING_KERNEL.md` remains unchanged.

Reason:

The agreed causal order is specialist doctrine → routing → eval → kernel only if still necessary. The first demonstrated defect is now corrected at routing/gold level. Editing the kernel before rerunning would confound variables.

If the corrected full A/B still produces repeatable material Kernel failures with required semantic units retrieved and verified, then a compact-kernel causal rule is justified.

## Validation of corrected head

On `c12b421e18ec32c386b3778141c8bda87d083a33`:

- repository invariants: PASS;
- routing eval suite: PASS;
- architecture holdout validator: PASS;
- retrieval map validator: PASS;
- semantic gold validator: PASS;
- static routing addressability: PASS;
- scripts compile: PASS;
- Sandler A/B dry-run: PASS;
- generated indexes: PASS;
- clean working tree check: PASS;
- Reasoning Kernel validator: PASS.

## Next gate

The original A/B run is diagnostic only after the eval correction.

Required now:

- regenerate all 22 A/B runs on `c12b421e18ec32c386b3778141c8bda87d083a33`;
- perform a new blinded behavioral judgment;
- unblind only after freezing all judgments;
- final merge requires FULL 11/11 and KERNEL 11/11, material failures 0, provenance failures 0.

**PR #16 remains DRAFT — DO NOT MERGE.**
