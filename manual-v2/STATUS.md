# Manual V2 Status

## Overall state

**ACTIVE — PHASE 6 / THIRD FOUNDER PROTOTYPE READY**

The current Manual V2 architecture has passed founder review. The remaining production gate is reader-facing prose quality.

Golden A and Golden B have now completed the requested prose-depth rewrite and internal audit. A third combined founder PDF has been built and visually verified.

**Production scaling remains blocked until founder approval of this third prototype.**

---

# Approved architecture baseline

Founder-approved and no longer under routine redesign:

- 8 Parts / 34 Chapters;
- explicit Part → Chapter → Section → Paragraph hierarchy;
- short topical chapter titles;
- general framing before detailed treatment;
- theory before substantial examples;
- generic unnamed / A-B examples by default;
- sourced real cases when they add evidence;
- worked numerical examples where useful;
- explanatory quantitative charts;
- no fixed chapter-length target.

Current architecture source:

- `EDITORIAL_HIERARCHY_V2.md`
- `TOC_V2.md`
- `LEARNING_OUTCOME_MAP.md`

---

# Writing-quality control

Founder feedback on the second prototype is canonical in:

- `FOUNDER_REVIEW_GOLDEN_AB_2.md`

Current prose-depth system:

- `PROSE_DEPTH_SYSTEM.md`
- `PROSE_AUDIT_GOLDEN_AB_2.md`
- `PROSE_DEPTH_AUDIT_GOLDEN_AB_3.md`

Binding writing requirements:

- natural Italian professional prose;
- high paragraph/section cohesion;
- sufficient explanatory depth for real understanding;
- mechanism and consequences, not only correct statements;
- firm authorial judgment when doctrine is clear;
- explicit uncertainty when evidence is not clear;
- practical implications integrated inside theory;
- micro-examples without returning to case-first structure;
- large boxes reserved for substantial worked examples/cases;
- no padding and no fixed word quota;
- no systematic AI-like rhetorical cadence.

---

# Current decisions

- **V2-D001 CURRENT:** V1 remains frozen as coverage baseline.
- **V2-D005 CURRENT:** full production cannot start before Golden prototypes pass founder review.
- **V2-D030 CURRENT:** reader-facing architecture = 8 Parts / 34 Chapters.
- **V2-D032 CURRENT:** architecture has founder PASS.
- **V2-D033 CURRENT:** Golden A/B required a dedicated prose-depth pass before production scaling.
- **V2-D034 CURRENT:** prose quality is judged on cohesion, fluidity, naturalness, explanatory depth, incisiveness and practical applicability.
- **V2-D035 CURRENT:** no fixed length target; explanation ends when the concept is understandable and usable.
- **V2-D036 CURRENT:** theory-first remains binding; micro-examples/practical consequences may be integrated in prose.
- **V2-D037 CURRENT:** voice must be natural and authoritative, neither mechanical nor sterile.
- **V2-D038 CURRENT:** Golden C remains blocked until founder verdict on the third A/B prototype.
- **V2-D039 CURRENT:** prose-depth control is governed by `PROSE_DEPTH_SYSTEM.md`; added words must contribute mechanism, distinction, consequence, boundary, example or decision translation.

---

# Phase state

- Phase 0 — DONE / PASS — V1 freeze and postmortem
- Phase 1 — DONE / PASS — research base and book contract
- Phase 2 — DONE / FOUNDER PASS — 8 Parts / 34 Chapters
- Phase 3 — ACTIVE / THIRD FOUNDER GATE — authorial prose refinement
- Phase 4 — DONE / FOUNDER PASS — theory-first chapter grammar
- Phase 5 — DONE / FOUNDER PASS WITH VISUAL DESIGN DEBT — visual/example/formula systems
- **Phase 6 — ACTIVE — third Golden A/B founder read**
- Phase 7 — NOT STARTED — editorial QA/lint
- Phase 8 — NOT STARTED — production waves
- Phase 9 — NOT STARTED — independent whole-book audits
- Phase 10 — NOT STARTED — beta reader validation
- Phase 11 — NOT STARTED — definitive production

---

# Golden A — Capitolo 1: `Il sistema di marketing`

Current:

- `golden/chapter-01/DRAFT.md`

Third-pass changes:

- deeper explanation of marketing vs promotion;
- clearer managerial consequences of treating marketing as downstream communication;
- stronger explanation of forward and backward feedback loops;
- activity / operating-effectiveness / economic-outcome metric hierarchy;
- containment vs root correction;
- local technical failure as a boundary to systemic diagnosis;
- delegation of execution vs delegation of judgment;
- practical implications distributed through the theory.

Internal prose-depth audit: **PASS FOR FOUNDER TEST**.

---

# Golden B — Capitolo 25: `Economia del cliente`

Current:

- `golden/chapter-25/DRAFT.md`
- `golden/chapter-25/figures/figure-25-1-same-cac-different-start.svg`
- `golden/chapter-25/figures/figure-25-2-cohort-payback.svg`

Third-pass changes:

- deeper unit-choice and contribution explanation;
- stronger fully loaded CAC attribution logic;
- cohort composition/mix effects;
- observed vs modeled LTV with forecasting risk;
- payback as financeability and capital recycling;
- allowable CAC as management decision rule;
- segment-specific acquisition ceilings;
- average vs marginal CAC;
- growth levers beyond media spend;
- practical questions integrated throughout.

Internal prose-depth audit: **PASS FOR FOUNDER TEST**.

---

# Third founder PDF / QA

GitHub Actions run:

- `35574017725` — SUCCESS

Combined prototype:

- 25 A4 pages;
- approximately 8,962 extracted words including cover and Part introductions;
- prior second prototype: 19 pages / approximately 6,094 extracted words;
- full 25-page render completed successfully;
- no clipping, overlaps or broken glyphs observed;
- tables, formula boxes and quantitative charts remain readable;
- arrow/process diagrams remain provisional visual design by prior founder decision.

The increase in length is not a target. Internal audit attributes it to added explanatory mechanism, consequences, boundaries and practical application.

---

# Golden C — Capitolo 19: `Vendita consulenziale`

**PAUSED.**

Do not resume reader-facing drafting until the third A/B founder verdict.

---

# Current blocker

**Founder approval of prose quality in the third A/B prototype.**

No architecture blocker.  
No doctrine blocker identified.  
No semantic coverage blocker identified.  
No PDF/layout blocker identified.

---

# Next action

1. founder reads the third A/B prototype;
2. classify remaining feedback as prose / depth / naturalness / practical utility / visual;
3. if founder PASS, freeze the production prose model;
4. rewrite Golden C under the approved model;
5. founder-review Golden C;
6. only after all Golden gates pass, start Phase 7 editorial QA and production waves.