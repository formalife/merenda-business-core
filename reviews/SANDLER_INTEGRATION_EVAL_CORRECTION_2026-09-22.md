# Sandler Integration — Phase 6 Eval Correction — 2026-09-22

## Stato

**EVAL CORRECTION AFTER BLINDED JUDGMENT — FULL RERUN REQUIRED**

Tested head that produced the diagnostic evidence:

`21081371299f4bcbcc47227be7e9ded9c6373abd`

Blinded judgment was frozen before unblinding in:

- `reviews/SANDLER_INTEGRATION_BLINDED_JUDGMENT_2026-09-22.md`
- `reviews/SANDLER_INTEGRATION_BLINDED_JUDGMENT_2026-09-22.jsonl`

Unblinding showed:

- FULL = 11/11 behavioral PASS;
- KERNEL = 9/11 behavioral PASS;
- material failures: R033 Kernel, R041 Kernel;
- provenance failures: 0.

This correction does **not** reinterpret those frozen judgments. It fixes an eval/routing specification defect exposed by them.

---

## 1. R033 — gold too coarse

Prompt intent: the seller wants to move from a surface problem directly to a demo.

Frozen behavioral requirement already said:

- distinguish surface problem from qualified Pain;
- deepen specificity/impact/priority;
- only then move through the remaining qualification gates before presentation.

Previous semantic gold required only:

- `SALES.PAIN_QUALIFICATION`.

That allowed the Kernel run to achieve semantic recall 1.0 while never selecting or verifying the downstream rule that demo/Fulfillment requires Pain + Budget + Decision.

Trace evidence:

- FULL selected/verified `SALES.FULFILLMENT_DECISION` and answered: qualify investment and decision process before selective demo;
- KERNEL selected only `SALES.PAIN_QUALIFICATION` + `SALES.DIAGNOSE_BEFORE_PRESCRIBE` and answered: after concrete Pain, proceed to selective demo.

Classification:

**GOLD_TOO_COARSE + ROUTING DEPENDENCY TOO WEAK.**

Correction:

R033 semantic required units are now:

- `SALES.PAIN_QUALIFICATION`;
- `SALES.BUDGET_QUALIFICATION`;
- `SALES.DECISION_QUALIFICATION`;
- `SALES.FULFILLMENT_DECISION`.

`SALES.PAIN_QUALIFICATION` now has explicit conditional `must_read_with` links for Budget, Decision and Fulfillment when the conversation is advancing toward a concrete solution/demo/proposal.

---

## 2. R041 — qualification re-entry under-specified

Prompt intent: a happy customer should not automatically receive a standard upsell.

Frozen behavioral requirement already said:

- verify realized value;
- identify a real new need/use case;
- re-enter the new opportunity into the normal sales qualification process before expansion/proposal.

Previous semantic gold required only:

- `CUSTOMER.SUCCESS_BEFORE_RETENTION_TACTIC`;
- `CUSTOMER.ACCOUNT_GROWTH_VALUE`.

`SALES.PAIN_QUALIFICATION` was optional and Budget/Decision were absent from required semantic units.

The Account Growth semantic entry itself already said that it is not sufficient to replace qualification and that every new opportunity returns to the normal commercial process. However, this was not expressed strongly enough as a routing dependency.

Trace evidence:

- FULL answer explicitly checked stakeholder, willingness to invest and then routed the opportunity into the normal commercial process;
- KERNEL answer verified realized value and a new need, but moved from `qualificazione del bisogno successivo` to `proposta coerente` without making investment/resources and Decision process mandatory.

Classification:

**GOLD_TOO_COARSE + ROUTING DEPENDENCY TOO WEAK.**

Correction:

R041 semantic required units are now:

- `CUSTOMER.SUCCESS_BEFORE_RETENTION_TACTIC`;
- `CUSTOMER.ACCOUNT_GROWTH_VALUE`;
- `SALES.PAIN_QUALIFICATION`;
- `SALES.BUDGET_QUALIFICATION`;
- `SALES.DECISION_QUALIFICATION`.

`CUSTOMER.ACCOUNT_GROWTH_VALUE` now has conditional `must_read_with` links to Pain, Budget and Decision when a new opportunity is being considered.

---

## 3. Kernel decision

**No kernel change in this correction pass.**

Reason:

The agreed architecture order is:

**specialist doctrine → routing → eval → kernel only if still necessary.**

The doctrine was already correct. The first demonstrated defect was that routing/gold did not fully encode the behavioral prerequisites already present in doctrine.

The Kernel remains a candidate cause because its compact Sales section does not explicitly name the integrated Pain → Budget → Decision → Fulfillment gate sequence. However, changing it before testing the corrected semantic routing would confound two variables.

Therefore:

1. correct routing/gold first;
2. rerun the complete A/B suite on the new head;
3. judge blinded again;
4. modify `REASONING_KERNEL.md` only if FULL still passes while KERNEL still shows a repeatable material omission attributable to bootstrap compression.

---

## 4. Rerun requirement

Because semantic gold and routing metadata changed after trace inspection, the previous A/B run is diagnostic only and **cannot close the merge gate**.

Required next state:

- static validators PASS on the corrected head;
- dry-run A/B PASS;
- regenerate all 22 runs, not only R033/R041;
- freeze a new blinded judgment;
- unblind only after judgment;
- final requirement remains FULL 11/11 + KERNEL 11/11, material failures 0, provenance failures 0.

Until then:

**PR #16 remains DRAFT — DO NOT MERGE.**
