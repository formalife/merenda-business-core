# Manual V2 Status

## Overall state

**ACTIVE — PHASE 6 / SECOND FOUNDER PROTOTYPE READY**

V1 remains frozen as the doctrine-coverage baseline. The first Golden A/B production model failed the founder reading-experience gate. The architecture, chapter grammar, authorial voice and example system have now been redesigned and applied to a second A/B prototype.

The project is **not approved for production scaling yet**. Founder review of the second prototype is the current gate.

---

# V1 baseline

- release baseline: `1a57b6e680c4bd62763116488b3bf6a790b52271`;
- classification: **CONTENT BASELINE / DOCTRINE-COVERAGE PASS / EDITORIAL PROTOTYPE FAIL**;
- PDF: 313 pages;
- approximately 46,948 extracted words;
- 39.1% list-line share;
- median paragraph length: 9 words;
- 66.7% of paragraphs <=12 words;
- embedded images: 0.

These metrics remain diagnostic evidence, not V2 optimization targets.

---

# Binding founder feedback

Recorded in `FOUNDER_REVIEW_GOLDEN_AB.md`.

Current requirements:

1. general framing before detail;
2. more natural and less engineered Italian prose;
3. theory before substantial examples;
4. no invented branded fictional companies by default;
5. explicit Part → Chapter → Section → Paragraph hierarchy;
6. short, general, topical chapter titles;
7. preserve strong numerical worked examples and useful charts;
8. arrow/process diagrams can receive later graphic redesign.

---

# Current architecture decisions

- **V2-D001 CURRENT:** V1 is frozen; V2 is separate under `manual-v2/`.
- **V2-D003 CURRENT:** target form = professional textbook / business book / field manual hybrid.
- **V2-D004 CURRENT:** target reader = intelligent operator without systematic marketing education.
- **V2-D005 CURRENT:** full production cannot start before Golden prototypes pass founder review.
- **V2-D006 CURRENT:** examples, formulas, visuals and exercises are instructional devices, not cosmetic enrichment.
- **V2-D007 CURRENT:** no visual quota; coherence beats decoration.
- **V2-D008 CURRENT:** quantitative subjects require reproducible worked calculations and interpretation.
- **V2-D009 CURRENT:** doctrine, instructional, editorial and visual audits remain separate gates.
- **V2-D010 CURRENT:** lists are reference/compression devices, not default explanatory prose.
- **V2-D011 SUPERSEDED:** first V2 8-Part / 31-Chapter architecture is historical prototype architecture.
- **V2-D030 CURRENT:** current reader-facing candidate = **8 Parts / 34 Chapters**, with explicit macro-sections.
- **V2-D012 CURRENT:** reader-facing boundaries follow subject hierarchy, not backend primary-home logic.
- **V2-D013 REFINED:** target voice = competent human author explaining the subject clearly, naturally and systematically.
- **V2-D015 SUPERSEDED:** case/problem-first chapter grammar is no longer the default.
- **V2-D031 CURRENT:** default chapter movement = general framing → conceptual structure → progressive detail → examples/applications → synthesis.
- **V2-D016 CURRENT:** guidance can fade as reader competence grows.
- **V2-D017 CURRENT:** pedagogical features require a learning job; no decorative quotas.
- **V2-D018 CURRENT:** visuals use the simplest form that exposes the relevant relationship.
- **V2-D019 SUPERSEDED:** recurring named fictional-company continuity is not a production rule.
- **V2-D020 CURRENT:** quantitative content distinguishes identities, metrics, estimates/models and decision rules.
- **V2-D021 CURRENT:** real cases require evidence/provenance control.
- **V2-D023 CURRENT:** general framing precedes detailed explanation by default.
- **V2-D024 CURRENT:** theory is primary; examples are subordinate.
- **V2-D025 CURRENT:** prefer generic unnamed examples, A/B labels or sourced real cases.
- **V2-D026 CURRENT:** hierarchy roles are explicit: Part = domain; Chapter = subject; Section = major component; Paragraph = explanatory move.
- **V2-D027 CURRENT:** chapter titles are short, clear and topical.
- **V2-D028 CURRENT:** numerical worked examples and explanatory charts remain approved.
- **V2-D029 CURRENT:** first Golden A/B internal passes remain historical prototypes and do not satisfy founder gate.

---

# Current phase state

- Phase 0 — DONE / PASS — V1 freeze and postmortem
- Phase 1 — DONE / PASS — research base and book contract
- Phase 2 — DONE / REVISED — current architecture 8 Parts / 34 Chapters
- Phase 3 — DONE / REVISED — natural authorial style system
- Phase 4 — DONE / REVISED — theory-first chapter grammar
- Phase 5 — DONE / REVISED — visual/example/formula systems
- **Phase 6 — ACTIVE — second Golden A/B founder gate**
- Phase 7 — NOT STARTED — editorial QA/lint
- Phase 8 — NOT STARTED — production waves
- Phase 9 — NOT STARTED — whole-book independent audits
- Phase 10 — NOT STARTED — beta reader validation
- Phase 11 — NOT STARTED — definitive production

---

# Current control artifacts

## Architecture

- `EDITORIAL_HIERARCHY_V2.md` — CURRENT
- `TOC_V2.md` — CURRENT 8-Part / 34-Chapter candidate
- `LEARNING_OUTCOME_MAP.md` — CURRENT remap; 18/18 book outcomes covered
- `POST_FOUNDER_REDESIGN_AUDIT.md` — CURRENT redesign audit
- `CHAPTER_ARCHITECTURE_AUDIT.md` — historical first-pass audit

## Style / learning design

- `AUTHORIAL_STYLE_BIBLE.md` — CURRENT founder-revised voice
- `CHAPTER_GRAMMAR_V2.md` — CURRENT theory-first grammar
- `CASE_SYSTEM_V2.md` — CURRENT generic/A-B/real-case example system
- `PEDAGOGICAL_FEATURES.md` — supporting palette
- `AI_SMELL_CATALOG.md` — supporting diagnostic catalog

## Quantitative / visual

- `FORMULA_CATALOG.md`
- `VISUAL_SYSTEM.md`

## Golden control

- `FOUNDER_REVIEW_GOLDEN_AB.md` — first founder FAIL
- `GOLDEN_CHAPTER_PLAN.md` — reset/current plan

---

# Second Golden prototype status

## Golden A — Capitolo 1: `Il sistema di marketing`

Current path:

- `golden/chapter-01/SPEC.md`
- `golden/chapter-01/DRAFT.md`

State:

- rewritten from zero under theory-first architecture;
- general framing before section 1.1;
- five explicit sections;
- no named fictional-company dependency;
- numerical service-business example moved after the theory;
- conceptual system and cause/amplifier/symptom visuals retained provisionally;
- Part I introduction added in `golden/part-01-intro.md`.

## Golden B — Capitolo 25: `Economia del cliente`

Current path:

- `golden/chapter-25/SPEC.md`
- `golden/chapter-25/DRAFT.md`
- `golden/chapter-25/figures/figure-25-1-same-cac-different-start.svg`
- `golden/chapter-25/figures/figure-25-2-cohort-payback.svg`

State:

- rewritten from zero under theory-first architecture;
- general chapter map before calculations;
- six explicit sections;
- no `TurnoChiaro` / `Dispensa Nord` dependency;
- generic `Coorte A / Coorte B` used only as worked numerical example;
- CAC, contribution, cohorts, LTV, payback, sustainable CAC, marginal CAC and sensitivity preserved;
- Part VII introduction added in `golden/part-07-intro.md`.

Historical first Golden B remains under `golden/chapter-23/` and must not be treated as current reader-facing material.

## Golden C — Capitolo 19: `Vendita consulenziale`

- existing old prep material is historical/reference material;
- current reader-facing drafting remains **PAUSED**;
- do not resume until revised A/B pass founder review.

---

# Second founder PDF

Workflow:

- `.github/workflows/golden-ab-redesign-preview.yml`
- run `35571525446` — SUCCESS

Artifact:

- `manual-v2-redesigned-golden-ab-preview`
- 19 pages, A4

Composition:

1. cover;
2. Parte I introduction;
3. revised Chapter 1;
4. Parte VII introduction;
5. revised Chapter 25.

Visual QA completed on the rendered pages:

- hierarchy pages render correctly;
- chapter openings show general framing before detail;
- figures fit without clipping;
- Figure 25.1 uses generic cohorts and no fictional brand;
- Figure 25.2 clearly distinguishes observed period from illustrative projection;
- tables/formula boxes are readable;
- no material layout blocker found.

Arrow/process diagrams remain intentionally non-final graphic design.

---

# Current blocker

**Founder approval of the redesigned reading experience.**

Internal redesign audit result:

`POST_FOUNDER_REDESIGN_AUDIT.md` → **INTERNAL PASS FOR SECOND FOUNDER PROTOTYPE**.

This is not equivalent to founder approval.

---

# Next action

1. founder reads the second A/B PDF;
2. classify feedback as architecture / voice / hierarchy / examples / quantitative / visual;
3. if A/B founder PASS, freeze the production model;
4. rewrite Golden C as Chapter 19 under the approved model;
5. founder-review Golden C;
6. only after all Golden gates pass, start Phase 7 and production planning.

## Blockers

No doctrine blocker.  
No known semantic coverage blocker.  
Production model remains blocked only by founder reading-experience gate.
