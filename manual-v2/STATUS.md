# Manual V2 Status

## Overall state

**ACTIVE — GOLDEN PRODUCTION DESIGN TEST / FOUNDER REVIEW PENDING**

The current Manual V2 architecture has founder PASS. Golden A/B have completed the prose-depth rewrite and received a materially positive founder response (`molto più soddisfatto`), but the prose model has not yet been explicitly frozen as the final production standard.

Before scaling the manuscript, the founder approved proceeding with a **Golden Production Test** for the publishing/design system.

Current publishing direction:

**GitHub canonical manuscript → controlled LaTeX publishing layer → Prism/LaTeX → PDF/print.**

Prism is a publishing environment, not the source of truth.

Full production remains blocked until the current content/prose model and the candidate design system have both passed founder review.

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

Founder response to the third prototype: **strong positive improvement, not yet recorded as an explicit final prose freeze.**

---

# Publishing / design control

Current candidate sources:

- `EDITORIAL_DESIGN_BIBLE.md` — CANDIDATE / founder review pending;
- `PRISM_PUBLISHING_WORKFLOW.md` — CANDIDATE workflow;
- Golden Production Test — LaTeX/Prism-importable prototype built and visually verified.

Candidate design:

- 170 × 240 mm book format;
- two-sided / print-oriented;
- recto Part/Chapter starts;
- serif long-form body + sans-serif navigation;
- restrained one-accent palette;
- explicit Part / Chapter / Section hierarchy;
- reusable `IN PRATICA`, `ESEMPIO SVOLTO`, formula and key-emphasis components;
- chapter-local figure numbering;
- professional book tables;
- TikZ system diagrams;
- PGFPlots quantitative charts;
- restrained running heads and folios.

The prototype has been compiled and fully rendered after correcting:

- LaTeX `0.x` section numbering;
- chapter-local figure numbering;
- formula overflow;
- horizontal-rule overflow;
- scientific notation on the economic chart.

No remaining clipping/overlap/broken-glyph blocker was observed in the final render.

---

# Current decisions

- **V2-D001 CURRENT:** V1 remains frozen as coverage baseline.
- **V2-D005 CURRENT:** full production cannot start before Golden prototypes pass founder review.
- **V2-D030 CURRENT:** reader-facing architecture = 8 Parts / 34 Chapters.
- **V2-D032 CURRENT:** architecture has founder PASS.
- **V2-D034 CURRENT:** prose quality is judged on cohesion, fluidity, naturalness, explanatory depth, incisiveness and practical applicability.
- **V2-D035 CURRENT:** no fixed length target; explanation ends when the concept is understandable and usable.
- **V2-D036 CURRENT:** theory-first remains binding; micro-examples/practical consequences may be integrated in prose.
- **V2-D037 CURRENT:** voice must be natural and authoritative, neither mechanical nor sterile.
- **V2-D039 CURRENT:** prose-depth control is governed by `PROSE_DEPTH_SYSTEM.md`; added words must contribute mechanism, distinction, consequence, boundary, example or decision translation.
- **V2-D040 CURRENT:** run a Golden Production Test before full publishing/production scaling.
- **V2-D041 CURRENT:** GitHub remains canonical; Prism/LaTeX is the publishing/design layer and must not become a divergent manuscript source.
- **V2-D042 CANDIDATE:** 170 × 240 mm two-sided book format and current typography/component system are under founder review, not yet frozen.

---

# Phase state

- Phase 0 — DONE / PASS — V1 freeze and postmortem
- Phase 1 — DONE / PASS — research base and book contract
- Phase 2 — DONE / FOUNDER PASS — 8 Parts / 34 Chapters
- Phase 3 — INTERNAL PASS / FOUNDER POSITIVE — prose-depth model awaiting explicit freeze
- Phase 4 — DONE / FOUNDER PASS — theory-first chapter grammar
- Phase 5 — DONE / FOUNDER PASS WITH DESIGN DEBT — content visual/formula systems
- **Phase 6 — ACTIVE — Golden production design test / founder review**
- Phase 7 — NOT STARTED — editorial QA/lint
- Phase 8 — NOT STARTED — production waves
- Phase 9 — NOT STARTED — independent whole-book audits
- Phase 10 — NOT STARTED — beta reader validation
- Phase 11 — NOT STARTED — definitive production

---

# Golden content status

## Golden A — Capitolo 1: `Il sistema di marketing`

- architecture/hierarchy: PASS;
- prose-depth internal audit: PASS;
- third founder response: strongly positive;
- used in current Golden Production Test.

## Golden B — Capitolo 25: `Economia del cliente`

- architecture/hierarchy: PASS;
- quantitative/formula/chart direction: PASS;
- prose-depth internal audit: PASS;
- third founder response: strongly positive;
- used in current Golden Production Test.

## Golden C — Capitolo 19: `Vendita consulenziale`

**PAUSED.**

Do not resume reader-facing drafting until the current content/design gate is resolved.

---

# Current blocker

**Founder review of the Golden Production Test and explicit freeze of the production model.**

No architecture blocker.  
No doctrine blocker identified.  
No semantic coverage blocker identified.  
No current technical PDF blocker identified.

---

# Next action

1. founder reviews the Golden Production Test PDF;
2. founder judges page format, typography, hierarchy, boxes, tables, charts and overall book feel;
3. classify feedback as typography / spacing / color / components / figures / print behavior;
4. if design PASS, freeze `EDITORIAL_DESIGN_BIBLE.md` and promote the LaTeX template to production infrastructure;
5. explicitly freeze or revise the current prose model at the same gate;
6. resume Golden C under the approved content + design system;
7. only after Golden C passes, begin Phase 7 editorial QA and production waves.
