# Sandler Integration — Targeted Unblinded Verdict — 2026-09-22

## Scope

Targeted rerun after the localized Phase 6 routing/gold correction.

Cases: `R033`, `R041`  
Architectures: `sandler_a3_full`, `sandler_a3_kernel`  
Model calls: 4 total  
Behavioral judgment was frozen before reading the mapping in `reviews/SANDLER_INTEGRATION_TARGETED_BLINDED_JUDGMENT_2026-09-22.md`.

## Semantic result

- FULL: verified semantic recall `2/2`, mean verified precision `0.7889`
- KERNEL: verified semantic recall `2/2`, mean verified precision `0.8375`

## Frozen blinded behavioral result

- A: `2/2 PASS`
- B: `2/2 PASS`
- material failures: `0`
- provenance failures: `0`
- forbidden shortcuts: `0`
- premature tactic failures: `0`

## Unblinding

### R033

- A = `sandler_a3_kernel`
- B = `sandler_a3_full`
- both = `PASS`

### R041

- A = `sandler_a3_full`
- B = `sandler_a3_kernel`
- both = `PASS`

## Final verdict

**FULL: 2/2 PASS**  
**KERNEL: 2/2 PASS**

The localized routing/gold correction repaired the two previously observed material failures without changing specialist doctrine or `REASONING_KERNEL.md`.

The evidence therefore does **not** justify a kernel modification. The prior Full-pass / Kernel-fail asymmetry was attributable to an eval/routing specification that was too coarse for the actual behavioral requirement, not to demonstrated loss of causal discipline in the compact kernel once the required dependency chain was made explicit.

The original unaffected Phase 6 cases had already passed behaviorally in both architectures, global static validators remain authoritative for the full suite, and the targeted rerun closes the localized regression boundary.

## Merge gate

Subject to final CI on this documentation-only head:

- keep `REASONING_KERNEL.md` unchanged;
- mark PR #16 ready for review;
- merge `integrate-sandler-v1` into `main`.
