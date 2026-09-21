# Manual V2 Status

## Overall state

**ACTIVE — PHASE 6 / GOLDEN CHAPTER REDESIGN AFTER FOUNDER GATE FAIL**

V1 is frozen as coverage baseline. V2 has completed postmortem, research/book contract, zero-based architecture, authorial style system, chapter-learning grammar, and visual/case/quantitative systems. Golden A and B passed internal doctrine/instructional/visual checks but **failed the founder reading-experience gate** and must not be scaled as the production template.

See: `FOUNDER_REVIEW_GOLDEN_AB.md`.

## V1 baseline

- release baseline: `1a57b6e680c4bd62763116488b3bf6a790b52271`;
- V1 classification: **CONTENT BASELINE / DOCTRINE-COVERAGE PASS / EDITORIAL PROTOTYPE FAIL**;
- PDF: 313 pages;
- approximately 46,948 extracted words;
- 39.1% list-line share;
- median paragraph length 9 words;
- 66.7% of paragraphs <=12 words;
- embedded images: 0.

Additional style evidence recorded in Phase 3:

- 590 bullet-list runs;
- median bullet run = 5 items;
- 336 runs contain >=5 items;
- 198 extracted sentences begin with `Non...`;
- recurrent syntactic/metadiscursive templates identified and cataloged.

These metrics are diagnostic signals, not blind V2 targets.

## Current decisions

- **V2-D001 CURRENT:** V1 is frozen; V2 is separate under `manual-v2/`.
- **V2-D002 SUPERSEDED:** V1 8 parts / 39 chapters is coverage architecture, not binding TOC.
- **V2-D003 CURRENT:** target form = professional textbook / business book / field manual hybrid.
- **V2-D004 CURRENT:** target reader = intelligent operator without systematic marketing education.
- **V2-D005 CURRENT:** full production cannot start before golden prototypes pass the founder gate.
- **V2-D006 CURRENT:** examples, figures, formulas, cases and exercises are instructional components, not cosmetic enrichment.
- **V2-D007 CURRENT:** no figure/image quota; coherence beats decoration.
- **V2-D008 CURRENT:** quantitative topics require reproducible worked calculations and decision interpretation.
- **V2-D009 CURRENT:** doctrine, instructional, editorial and visual audits remain separate gates.
- **V2-D010 CURRENT:** lists are reference/compression devices, not default explanatory prose.
- **V2-D011 CURRENT BUT UNDER REVIEW:** provisional V2 architecture = 8 parts / 31 chapters; founder feedback requires a new hierarchy/title pass before further drafting.
- **V2-D012 CURRENT:** chapter boundaries are learning-problem boundaries, not primary-home/backend boundaries.
- **V2-D013 CURRENT BUT TO BE REFINED:** target authorial voice = experienced operator-teacher with visible judgment; current implementation still reads too engineered.
- **V2-D014 CURRENT:** authorial presence comes from reasoning/judgment, not autobiography or stylistic cosplay.
- **V2-D015 SUPERSEDED IN CURRENT FORM:** flexible orient/model/demonstrate/apply/integrate grammar over-weighted problem/case-first openings; new default must be general-to-specific exposition.
- **V2-D016 CURRENT:** novice guidance should fade from worked examples toward independent transfer as competence grows.
- **V2-D017 CURRENT:** pedagogical features must state a learning job; no decorative box/figure quota.
- **V2-D018 CURRENT:** visuals use the simplest representation that exposes the relationship; text and visual divide explanatory work.
- **V2-D019 SUPERSEDED:** recurring named fictional case continuity is no longer a mandatory production rule.
- **V2-D020 CURRENT:** quantitative content distinguishes identities, operational metrics, estimates/models and decision rules.
- **V2-D021 CURRENT:** real cases must separate fact, company claim, third-party analysis, synthesis and unknowns.
- **V2-D022 CURRENT:** Golden A, B and C remain stress-test topics, but Golden C prose is paused until the redesign is applied to A/B.
- **V2-D023 CURRENT:** general conceptual framing precedes detailed explanation by default.
- **V2-D024 CURRENT:** theory is primary; examples are subordinate explanatory/application devices.
- **V2-D025 CURRENT:** invented named companies are not the default; prefer generic unnamed examples, A/B labels or sourced real cases.
- **V2-D026 CURRENT:** reader-facing hierarchy must explicitly enforce Part → Chapter → Section → Paragraph roles.
- **V2-D027 CURRENT:** chapter titles must be short, clear and topical; thesis-like wording belongs below title level.
- **V2-D028 CURRENT:** numerical worked examples and explanatory charts are retained as approved instructional devices.
- **V2-D029 CURRENT:** Golden A/B internal passes do not satisfy the founder gate; they are prototypes to mine, not templates to scale.

## Phases

- Phase 0 — DONE / PASS — postmortem and V1 freeze
- Phase 1 — DONE / PASS — research base, book contract, preliminary benchmark
- Phase 2 — DONE / PASS AS FIRST ARCHITECTURE — zero-based architecture; now subject to founder-driven hierarchy/title revision
- Phase 3 — DONE / PASS AS FIRST STYLE SYSTEM — now subject to natural-language revision
- Phase 4 — DONE / PASS AS FIRST CHAPTER GRAMMAR — current default opener architecture superseded
- Phase 5 — DONE / PASS — visual/formula systems retained; recurring named-case default superseded
- **Phase 6 — ACTIVE / REDESIGN — Golden A/B founder gate failed**
- Phase 7 — NOT STARTED — editorial QA/lint
- Phase 8 — NOT STARTED — production waves
- Phase 9 — NOT STARTED — independent audits
- Phase 10 — NOT STARTED — beta readers
- Phase 11 — NOT STARTED — definitive production

## Golden prototype status

### Golden A — Chapter 1

- internal doctrine/instructional/visual audit: PASS;
- founder gate: **FAIL**;
- preserve useful content/figures, but restructure theory-first and retitle.

### Golden B — Chapter 23

- internal doctrine/instructional/visual audit: PASS after figure overflow correction;
- founder gate: **FAIL** on architecture/voice/example placement;
- preserve numerical examples, formulas and charts; restructure theory-first and remove named-company dependency.

### Golden C — Chapter 18

- case/spec/visual inputs prepared;
- reader-facing prose: **PAUSED**;
- do not draft until redesigned A/B pass founder-read.

## Current blocker

**The production model is not yet approved.**

The problem is not missing doctrine. It is the reader-facing architecture:

- insufficient general framing at chapter start;
- voice still too artificial/mechanical;
- examples too dominant and too early;
- invented named companies feel artificial;
- Part → Chapter → Section → Paragraph hierarchy insufficiently explicit;
- chapter titles too long/argumentative.

## Next action

Run a founder-driven architecture correction before any new reader-facing chapter:

1. redesign Part → Chapter → Section → Paragraph hierarchy;
2. retitle the entire provisional TOC using short topical chapter names;
3. rewrite `CHAPTER_GRAMMAR_V2.md` around **general framing → theory/model → components/details → examples/applications → synthesis**;
4. revise `AUTHORIAL_STYLE_BIBLE.md` toward more natural Italian expository prose;
5. supersede the named recurring-fictional-company default in `CASE_SYSTEM_V2.md`;
6. respec and rewrite Golden A and B under the new rules;
7. founder-read A/B again;
8. only after PASS, resume Golden C.

## Blockers

Founder gate on the production model is open.
