# Manual V2 Status

## Overall state

**ACTIVE — PEDAGOGICAL APPARATUS PROTOTYPE / FOUNDER REVIEW PENDING**

The Manual V2 architecture has founder PASS. Golden A/B have completed the prose-depth rewrite and received a materially positive founder response (`molto più soddisfatto`). The founder then explicitly chose to proceed with the second proposed improvement: **the pedagogical apparatus**.

The current task is therefore not a new architecture or prose redesign. It is the design of a restrained second reading speed around the approved chapter model.

Full production remains blocked until the current Golden content/prose model and the selective pedagogical apparatus have passed founder review.

Prism/LaTeX and the broader book-design system remain a later publishing task; they are not the current gate.

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
- no padding and no fixed word quota;
- no systematic AI-like rhetorical cadence.

Founder response to the third prototype: **strong positive improvement, not yet recorded as an explicit final prose freeze.**

---

# Pedagogical apparatus control

Current source:

- `PEDAGOGICAL_FEATURES.md` — CURRENT refined apparatus;
- `PEDAGOGICAL_APPARATUS_AUDIT.md` — INTERNAL PASS / founder review pending;
- `golden/chapter-01/APPARATUS.md`;
- `golden/chapter-25/APPARATUS.md`.

## Current primary feature palette

1. `ESEMPIO SVOLTO / ESEMPIO NUMERICO`
2. `ERRORE FREQUENTE`
3. `IN PRATICA`
4. `VERIFICA NELLA TUA AZIENDA`
5. `APPROFONDIMENTO`

Supporting only when an actual reusable artifact exists:

- `STRUMENTO OPERATIVO`.

Removed from the default recurring palette because they create too much visible teaching machinery:

- `PRINCIPIO`;
- generic `CASO`;
- `FERMATI E PREVEDI`;
- `SPIEGA PERCHÉ`;
- `DIAGNOSTICA`;
- `TRASFERISCI`;
- recurring `COSA CAMBIA SE...` labels.

## Binding apparatus rules

- prose remains conceptually complete without optional callouts;
- no feature quota;
- a callout must solve a learning/retrieval job better than prose;
- practical consequences should remain in ordinary prose when visual separation adds nothing;
- `ERRORE FREQUENTE` is reserved for plausible, materially costly mistakes;
- `VERIFICA NELLA TUA AZIENDA` must produce evidence, a number, a comparison or a decision input;
- `APPROFONDIMENTO` is optional nuance and should remain uncommon;
- formulas, charts, tables and core worked examples are part of explanation, not decorative apparatus;
- final pages must remain calm and book-like rather than resembling courseware.

### Feature-delete evidence

Two proposed `IN PRATICA` callouts were deliberately removed during the Golden test:

- Chapter 1 after `Marketing e promozione`;
- Chapter 25 after the CAC-perimeter discussion.

Reason: the current prose already did the practical translation. Keeping the callouts would have added repetition and visual fragmentation.

---

# Pedagogical apparatus Golden test

Workflow:

- `.github/workflows/golden-ab-pedagogy-preview.yml`

Builder:

- `.github/scripts/build_golden_ab_pedagogy.py`

Final validated run:

- run `35579306028` — SUCCESS;
- head commit `97b8efd21006fae34b2d74e048095ca724d004e3`;
- artifact `manual-v2-pedagogical-apparatus-preview`;
- artifact id `10629890821`.

Preview:

- 29 A4 pages;
- current Golden A/B prose unchanged as canonical source;
- optional apparatus injected only in the publishing prototype.

Render-first QA:

- all 29 pages rendered;
- no clipping observed;
- no text overlap observed;
- no broken glyphs observed;
- Chapter 1 callout collision found in first preview and corrected;
- final render keeps `ERRORE FREQUENTE` and following `ESEMPIO SVOLTO` semantically and visually separate;
- self-checks remain readable;
- Chapter 25 remains a continuous quantitative chapter rather than a workbook.

Minor design debt:

- final publishing design should allow more pagination/spacing control when `ERRORE FREQUENTE` and `APPROFONDIMENTO` happen to fall on the same page.

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
- **V2-D043 CURRENT:** pedagogical apparatus is subordinate to core prose and exists to support application, error prevention and later retrieval.
- **V2-D044 CURRENT:** no apparatus quota; redundant callouts must be removed even if they belong to the approved taxonomy.
- **V2-D045 CURRENT:** current primary apparatus labels are `ESEMPIO SVOLTO/NUMERICO`, `ERRORE FREQUENTE`, `IN PRATICA`, `VERIFICA NELLA TUA AZIENDA`, `APPROFONDIMENTO`; `STRUMENTO OPERATIVO` is reserved for genuine artifacts.
- **V2-D046 CURRENT:** self-checks must produce evidence/decision inputs rather than generic reflection.
- **V2-D047 CURRENT:** the Golden A/B pedagogical apparatus has internal PASS and awaits founder review before being frozen for all chapters.

---

# Phase state

- Phase 0 — DONE / PASS — V1 freeze and postmortem
- Phase 1 — DONE / PASS — research base and book contract
- Phase 2 — DONE / FOUNDER PASS — 8 Parts / 34 Chapters
- Phase 3 — INTERNAL PASS / FOUNDER POSITIVE — prose-depth model awaiting explicit freeze
- Phase 4 — DONE / FOUNDER PASS — theory-first chapter grammar
- **Phase 5 — ACTIVE REFINEMENT — selective pedagogical apparatus internal PASS / founder review pending**
- Phase 6 — Golden C PAUSED until current content/apparatus gate is resolved
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
- apparatus prototype: INTERNAL PASS;
- planned support: 2 `ERRORE FREQUENTE`, existing worked example, 1 own-business verification;
- no deep-dive box required.

## Golden B — Capitolo 25: `Economia del cliente`

- architecture/hierarchy: PASS;
- quantitative/formula/chart direction: PASS;
- prose-depth internal audit: PASS;
- third founder response: strongly positive;
- apparatus prototype: INTERNAL PASS WITH LAYOUT CAUTION;
- planned support: existing numerical/worked examples, 1 `ERRORE FREQUENTE`, 1 `APPROFONDIMENTO`, 1 own-business verification.

## Golden C — Capitolo 19: `Vendita consulenziale`

**PAUSED.**

Do not resume reader-facing drafting until the current Golden content/apparatus gate is resolved.

---

# Current blocker

**Founder review of the selective pedagogical apparatus and explicit freeze/revision of the current Golden production model.**

No architecture blocker.  
No doctrine blocker identified.  
No semantic coverage blocker identified.  
No current technical PDF blocker identified.

---

# Next action

1. founder reviews the pedagogical apparatus preview PDF;
2. judge whether support elements improve retrieval/application without interrupting reading;
3. if PASS, freeze the apparatus taxonomy and placement rules;
4. explicitly freeze or revise the current prose model at the same gate;
5. then either proceed to the next requested improvement (real documented cases / visual system / publishing design) or resume Golden C, according to founder direction.
