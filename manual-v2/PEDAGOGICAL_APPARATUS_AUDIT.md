# Pedagogical Apparatus Audit — Golden A/B

Date: 2026-09-21  
Status: **INTERNAL PASS — FOUNDER REVIEW PENDING**

## Scope

This audit tests the founder-requested improvement to the manual's pedagogical apparatus without reopening the approved architecture or changing the current Golden A/B canonical prose.

The objective is a **second reading speed**: continuous prose for first reading, selective callouts for later retrieval, error prevention and application to the reader's own business.

---

# 1. System redesign

`PEDAGOGICAL_FEATURES.md` was narrowed from a broad instructional toolkit to a restrained editorial apparatus.

Current primary labels:

1. `ESEMPIO SVOLTO / ESEMPIO NUMERICO`
2. `ERRORE FREQUENTE`
3. `IN PRATICA`
4. `VERIFICA NELLA TUA AZIENDA`
5. `APPROFONDIMENTO`

Supporting label:

- `STRUMENTO OPERATIVO`, only when an actual reusable artifact exists.

Removed from the default recurring palette:

- `PRINCIPIO`;
- generic `CASO`;
- `FERMATI E PREVEDI`;
- `SPIEGA PERCHÉ`;
- `DIAGNOSTICA`;
- `TRASFERISCI`;
- recurring `COSA CAMBIA SE...` labels.

Reason: their learning jobs remain valid, but the permanent visual labels would make the manual feel too much like courseware.

---

# 2. Golden A apparatus

File: `golden/chapter-01/APPARATUS.md`

Retained/planned:

- `ERRORE FREQUENTE — Premiare il KPI più visibile`;
- existing `ESEMPIO SVOLTO — Più vendite, meno contribuzione`;
- `ERRORE FREQUENTE — Scambiare il contenimento per la soluzione`;
- `VERIFICA NELLA TUA AZIENDA — Segui una decisione attraverso il sistema`.

Explicitly rejected after `FEATURE-DELETE`:

- proposed `IN PRATICA` after Section 1.1.

Reason for rejection: the current prose already performs that operating translation. A second callout would repeat it and weaken reading continuity.

No `APPROFONDIMENTO` is needed in Chapter 1.

### Self-check evidence output

The reader produces a one-page causal map for one current initiative, identifying:

- local result;
- downstream consequence;
- upstream prerequisite;
- economic metric;
- alternative explanation.

This is evidence-producing application, not generic reflection.

---

# 3. Golden B apparatus

File: `golden/chapter-25/APPARATUS.md`

Retained/planned:

- existing `ESEMPIO NUMERICO — Economia elementare di un account`;
- existing `ESEMPIO SVOLTO — Due coorti con lo stesso CAC`;
- `ERRORE FREQUENTE — Usare il futuro per giustificare il presente`;
- `APPROFONDIMENTO — Perché lo stesso LTV:CAC può descrivere aziende molto diverse`;
- existing `ESEMPIO NUMERICO — Costruire una soglia di acquisizione`;
- `VERIFICA NELLA TUA AZIENDA — Costruisci la scheda economica di una coorte reale`.

Explicitly rejected after `FEATURE-DELETE`:

- proposed `IN PRATICA` after the CAC discussion.

Reason for rejection: the current prose already provides the operational check on CAC perimeter. A separate callout would duplicate rather than teach.

### Self-check evidence output

The reader builds one real cohort economics sheet separating:

- fully loaded CAC;
- observed contribution;
- observed payback;
- observed vs modeled value;
- sustainable acquisition ceiling;
- marginal acquisition economics.

---

# 4. Visual prototype

Workflow:

`.github/workflows/golden-ab-pedagogy-preview.yml`

Builder:

`.github/scripts/build_golden_ab_pedagogy.py`

Final validated run:

- run id: `35579306028`;
- head commit: `97b8efd21006fae34b2d74e048095ca724d004e3`;
- conclusion: SUCCESS;
- artifact: `manual-v2-pedagogical-apparatus-preview`;
- artifact id: `10629890821`.

PDF:

- 29 A4 pages;
- WeasyPrint 70.0;
- no forms, JavaScript or encryption.

The prototype changes the publishing layer only. Canonical Golden A/B `DRAFT.md` files remain the prose source and were not rewritten to embed optional support elements.

---

# 5. Render-first QA

All 29 pages were rendered after the final preview correction.

Checks:

- no clipping observed;
- no overlapping text observed;
- no broken glyphs observed;
- existing quantitative figures remain readable;
- self-check callouts remain visually distinct from continuous prose;
- optional support does not dominate chapter openings;
- Chapter 25 still reads as a quantitative chapter rather than a financial workbook.

### Finding fixed during QA

In the first successful layout version, the Chapter 1 `ERRORE FREQUENTE — Premiare il KPI più visibile` visually merged with the following `ESEMPIO SVOLTO` because adjacent Markdown blockquotes were parsed as one element.

The publishing prototype was corrected by inserting an explicit semantic break. The final render shows two separate elements.

### Remaining design debt

On one Chapter 25 page, `ERRORE FREQUENTE` and `APPROFONDIMENTO` can both appear on the same page, separated by ordinary prose. This is readable and not a blocker, but the final book-design system should allow more spacing/pagination control so optional callouts do not create unnecessary visual density.

---

# 6. Learning-job audit

## Core prose dominance

PASS.

Removing optional support elements leaves the chapters conceptually complete.

## Error prevention

PASS.

The selected error boxes address expensive misconceptions rather than trivial reminders:

- local KPI substitution;
- containment mistaken for correction;
- forecast LTV mistaken for observed evidence.

## Application

PASS.

Both self-checks require the reader to produce business evidence/decision inputs.

## Retrieval value

PASS.

The selected features are useful when returning to the book later, not only during linear reading.

## Feature deletion discipline

PASS.

Two candidate `IN PRATICA` boxes were explicitly removed because current prose already did the job.

## Courseware risk

PASS WITH DESIGN CAUTION.

The feature taxonomy is restrained enough for a professional manual. Final typography should keep optional boxes visually quieter than chapter hierarchy, figures and worked examples.

---

# 7. Internal verdict

**PEDAGOGICAL APPARATUS: INTERNAL PASS.**

Recommended production baseline:

- prose remains primary;
- use callouts only when they solve a distinct learning/retrieval job;
- no feature quota;
- prefer one strong own-business verification activity over repeated mini-prompts;
- keep `APPROFONDIMENTO` uncommon;
- reject `IN PRATICA` when the prose already translates theory into action;
- quantitative examples/figures/formulas remain part of core explanation rather than optional decoration.

Founder review is still required before this apparatus is frozen for all 34 chapters.
