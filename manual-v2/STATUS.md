# Manual V2 Status

## Overall state

**ACTIVE — PHASE 6 / ARCHITECTURE PASS, WRITING-QUALITY GATE OPEN**

V1 remains frozen as the doctrine-coverage baseline. The first Golden A/B production model failed the founder reading-experience gate. The second prototype has now passed the founder gate on **structure/architecture**, but not yet on **prose quality**.

The current book hierarchy, titles, theory-first chapter architecture, generic/A-B example policy, numerical worked examples and quantitative charts are approved as the reader-facing baseline.

The project is **not approved for production scaling yet**. Golden A/B require a dedicated prose-depth rewrite before Golden C or the remaining chapters can proceed.

See:

- `FOUNDER_REVIEW_GOLDEN_AB.md` — first founder FAIL;
- `FOUNDER_REVIEW_GOLDEN_AB_2.md` — structure PASS / writing-quality FAIL.

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

## Structure — APPROVED

The following are now approved as baseline:

1. general framing before detail;
2. theory before substantial examples;
3. explicit Part → Chapter → Section → Paragraph hierarchy;
4. short, general, topical chapter titles;
5. 8-Part / 34-Chapter current architecture;
6. no invented branded fictional companies by default;
7. generic examples / A-B labels / sourced real cases;
8. numerical worked examples where useful;
9. explanatory quantitative charts;
10. arrow/process diagrams may receive later graphic redesign.

## Writing quality — NOT YET APPROVED

Founder feedback on the second prototype:

- insufficient cohesion between paragraphs/sections;
- insufficient fluidity;
- language still too artificial/mechanical in places;
- tone too sterile;
- explanations sometimes too compressed;
- insufficient depth on important distinctions;
- insufficient incisiveness and authority;
- practical applications should be more integrated;
- the text must explain until the subject is genuinely understandable and usable.

---

# Current architecture / editorial decisions

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
- **V2-D030 CURRENT:** reader-facing architecture = **8 Parts / 34 Chapters**, with explicit macro-sections.
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
- **V2-D032 CURRENT:** current 8-Part / 34-Chapter architecture has passed the founder structure gate and is now the architectural baseline.
- **V2-D033 CURRENT:** Golden A/B require a dedicated prose-depth pass before production scaling.
- **V2-D034 CURRENT:** prose quality is judged on cohesion, fluidity, naturalness, explanatory depth, incisiveness and practical applicability.
- **V2-D035 CURRENT:** no fixed chapter-length target; depth ends when the concept is understandable and usable, not merely named.
- **V2-D036 CURRENT:** theory-first remains binding, but micro-examples and practical implications may be integrated in the prose; larger worked examples remain boxed/isolated.
- **V2-D037 CURRENT:** voice must be natural and authoritative, neither mechanical nor sterile.
- **V2-D038 CURRENT:** Golden C remains blocked until the prose-depth pass and a third founder-read of A/B.

---

# Current phase state

- Phase 0 — DONE / PASS — V1 freeze and postmortem
- Phase 1 — DONE / PASS — research base and book contract
- Phase 2 — DONE / FOUNDER PASS — current architecture 8 Parts / 34 Chapters
- Phase 3 — ACTIVE / REFINEMENT — natural authorial prose needs deeper revision
- Phase 4 — DONE / FOUNDER PASS — theory-first chapter grammar and hierarchy
- Phase 5 — DONE / FOUNDER PASS WITH VISUAL DESIGN DEBT — visual/example/formula systems
- **Phase 6 — ACTIVE — Golden A/B prose-depth rewrite before third founder gate**
- Phase 7 — NOT STARTED — editorial QA/lint
- Phase 8 — NOT STARTED — production waves
- Phase 9 — NOT STARTED — whole-book independent audits
- Phase 10 — NOT STARTED — beta reader validation
- Phase 11 — NOT STARTED — definitive production

---

# Current control artifacts

## Architecture

- `EDITORIAL_HIERARCHY_V2.md` — CURRENT / FOUNDER PASS
- `TOC_V2.md` — CURRENT 8-Part / 34-Chapter baseline
- `LEARNING_OUTCOME_MAP.md` — CURRENT; 18/18 book outcomes covered
- `POST_FOUNDER_REDESIGN_AUDIT.md` — second architecture audit
- `CHAPTER_ARCHITECTURE_AUDIT.md` — historical first-pass audit

## Style / learning design

- `AUTHORIAL_STYLE_BIBLE.md` — CURRENT but requires prose-depth refinement
- `CHAPTER_GRAMMAR_V2.md` — CURRENT / FOUNDER PASS
- `CASE_SYSTEM_V2.md` — CURRENT / FOUNDER PASS
- `PEDAGOGICAL_FEATURES.md` — supporting palette
- `AI_SMELL_CATALOG.md` — supporting diagnostic catalog
- `FOUNDER_REVIEW_GOLDEN_AB_2.md` — current founder feedback

## Quantitative / visual

- `FORMULA_CATALOG.md` — retained
- `VISUAL_SYSTEM.md` — retained; arrow/process graphic design not final

## Golden control

- `FOUNDER_REVIEW_GOLDEN_AB.md` — first founder FAIL
- `FOUNDER_REVIEW_GOLDEN_AB_2.md` — structure PASS / writing-quality FAIL
- `GOLDEN_CHAPTER_PLAN.md` — must be refined for prose-depth cycle

---

# Current Golden status

## Golden A — Capitolo 1: `Il sistema di marketing`

- architecture/hierarchy: PASS;
- general framing: PASS;
- example placement: PASS;
- writing quality: OPEN;
- needs deeper explanation, more continuity, more natural voice, stronger practical implications.

## Golden B — Capitolo 25: `Economia del cliente`

- architecture/hierarchy: PASS;
- numerical examples/formulas/charts: PASS directionally;
- generic A/B example policy: PASS;
- writing quality: OPEN;
- needs deeper explanatory prose, more connective tissue and stronger interpretation/application around formulas.

Historical first Golden B remains under `golden/chapter-23/` and must not be treated as current reader-facing material.

## Golden C — Capitolo 19: `Vendita consulenziale`

- current reader-facing drafting: **PAUSED**;
- resume only after third founder PASS on rewritten A/B.

---

# Current blocker

**Writing-quality approval of Golden A/B.**

Architecture is no longer the blocker.

No doctrine blocker.  
No semantic coverage blocker.  
No current example/quantitative-system blocker.

---

# Next action

1. perform a line-by-line prose diagnosis of Golden A/B;
2. build `PROSE_DEPTH_SYSTEM.md` with positive standards and anti-patterns;
3. revise `AUTHORIAL_STYLE_BIBLE.md` around natural, cohesive, deeper exposition;
4. run a prose-depth rewrite of Golden A/B without changing approved architecture;
5. integrate micro-examples, practical implications and deeper explanations where useful;
6. ensure added depth does not reintroduce AI-smell, list density or redundancy;
7. build a third A/B PDF;
8. founder-read;
9. only after founder PASS, resume Golden C.

## Blockers

Production scaling remains blocked by the writing-quality gate only.
