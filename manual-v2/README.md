# Manual V2 — Editorial Reconstruction

## Purpose

`manual-v2/` is the controlled reconstruction of the current manual into a real professional textbook / field manual.

The existing `manual/` subtree is frozen as **V1 coverage baseline**. It remains useful for semantic coverage, curriculum history, doctrine fidelity checks and provenance. It is **not** the prose/layout base to be incrementally polished into V2.

The V2 transformation is:

**V1 coverage baseline + canonical doctrine + editorial research → book contract → benchmark → zero-based TOC → chapter grammar → visual/case/formula systems → golden chapters → production waves → independent audits → beta test → definitive release**.

## Core rule

Do not confuse:

- complete knowledge coverage;
- good explanatory writing;
- good instructional design;
- good book design.

V1 proved the first. V2 must prove all four.

## Frozen baseline

V1 release branch baseline at V2 start:

`1a57b6e680c4bd62763116488b3bf6a790b52271`

The existing V1 files under `manual/` must not be rewritten merely to make V2 look cleaner. V2 gets a separate control plane and later a separate manuscript tree.

## Mandatory startup for V2 work

Before substantial V2 work read:

1. `manual-v2/ROADMAP.md`
2. `manual-v2/STATUS.md`
3. `manual-v2/BOOK_CONTRACT_V2.md`
4. the current phase artifact(s)
5. only then the relevant V1/canonical sources.

## Non-negotiables

- No mass chapter rewrite before golden-chapter approval.
- No visual element without an instructional job.
- No list used merely because it is easier to generate than prose.
- No chapter approved only for doctrine correctness.
- No “AI smell” accepted as harmless style debt.
- No figure, formula, case, box or exercise added decoratively.
- No sunk-cost protection for the 8-part / 39-chapter V1 architecture.
- No change to canonical `merenda/` doctrine for narrative convenience.

## Reader-facing objective

The definitive book should feel written by an expert author teaching a serious reader, not like a structured answer engine or a knowledge base exported to PDF.

It should be readable linearly, usable diagnostically, visually explanatory and operationally applicable.