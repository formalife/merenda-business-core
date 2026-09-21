# Editorial Design Bible — Manual V2

Status: **CANDIDATE — GOLDEN PRODUCTION TEST / FOUNDER REVIEW PENDING**  
Date: 2026-09-21

## Purpose

Define the visual and publishing grammar of Manual V2 before full production.

This file does not change the approved content architecture or prose model. It governs how approved content is turned into a professional book.

The design must support reading and consultation. It must not compete with the text.

---

# 1. Design direction

Target character:

**professional manual / premium business textbook / reference book**

The book should feel:

- authoritative;
- calm;
- contemporary;
- highly readable;
- structured without looking like a slide deck;
- visually rich only where the visual carries explanatory work;
- suitable for both PDF and print.

Avoid:

- corporate-report aesthetics;
- excessive color;
- decorative infographics;
- over-designed callouts;
- dashboard-like pages;
- presentation-slide density;
- visual novelty for its own sake.

---

# 2. Page format

Golden candidate:

**170 × 240 mm, two-sided, open-right chapters.**

Reason:

- more book-like than A4;
- enough width for formulas, compact tables and diagrams;
- manageable for a long professional manual;
- suitable for print and comfortable tablet/PDF reading.

A4 is no longer the preferred final-book format unless future production evidence requires it.

---

# 3. Typography

Golden prototype:

- body: Libertinus Serif;
- headings/navigation: Source Sans Pro;
- serif/sans contrast used to separate reading from navigation;
- no decorative display font.

Principles:

- body typography must disappear during long reading;
- headings should be clear, short and navigational;
- formulas and numbers must remain readable at print size;
- line length should remain appropriate for sustained reading;
- hyphenation and microtypography are preferred over forced line breaks.

Exact fonts may change after founder/design review, but the serif-body / sans-navigation model is the current candidate.

---

# 4. Hierarchy on page

Reader-facing hierarchy remains:

**Part → Chapter → Section → Paragraph.**

## Part opener

One dedicated page.

Contains:

- `PARTE N` overline;
- short general title;
- concise orientation text;
- compact list of chapters in the Part.

The page should create a clear change of scale without becoming decorative.

## Chapter opener

Starts on a right-hand page in print-oriented output.

Contains:

- chapter number;
- short topical title;
- one-line deck explaining scope;
- generous space before the opening exposition.

## Sections

Numbered as `chapter.section`.

Section title must remain topical and useful in navigation.

No rhetorical/article-style section headings by default.

---

# 5. Page rhythm

Default body pages should be prose-led.

Desired rhythm:

- long readable paragraphs;
- occasional section headings;
- figures/tables/formulas only when they carry information;
- callouts used as pauses, not as the main grammar of the page.

A reader should be able to see at a glance whether a page is primarily:

- explanation;
- worked example;
- quantitative analysis;
- visual model;
- practical application.

But the book should still feel like one continuous object.

---

# 6. Color

Golden candidate uses one restrained primary accent plus neutral tones.

Current prototype:

- ink: near-black;
- navigation/accent: muted petrol blue;
- secondary example accent: muted warm brown;
- backgrounds: very light neutral/warm gray.

Rules:

- body text remains near-black;
- color does not encode information that disappears in grayscale;
- figures must remain understandable in print;
- no rainbow palette;
- no chapter-specific color system unless later evidence justifies it.

Palette is swappable after founder review without changing component architecture.

---

# 7. Editorial components

## `IN PRATICA`

Function: translate a concept into an immediate managerial action/question.

Visual treatment:

- very light accent background;
- small sans label;
- same prose voice as main text.

Not required in every section.

## `ESEMPIO SVOLTO`

Function: substantial generic/numerical worked example after the theory.

Visual treatment:

- neutral background;
- thin border / restrained warm accent;
- may contain tables/calculations;
- should remain readable as a self-contained unit.

## Principle/key emphasis

Use rarely.

Treatment:

- no poster-style slogans;
- thin horizontal accent rules or understated boxed treatment;
- content must compress something already explained.

## Formula

Treatment:

- centered formula in a restrained framed block;
- plain-language label above;
- interpretation in normal prose immediately before/after;
- formulas may wrap over multiple lines rather than overflow the measure.

---

# 8. Tables

Use professional book tables:

- no dense spreadsheet grid;
- minimal horizontal rules;
- numeric alignment;
- strong but understated header;
- readable without color;
- limited number of columns where possible.

A table should compare values, not replace explanation.

---

# 9. Figures and diagrams

Figures are numbered by chapter (`Figura 25.1`, etc.).

Caption style:

- sans-serif;
- figure number emphasized;
- explanatory caption, not a generic label.

Visual families to standardize later:

1. causal/system map;
2. process/state map;
3. matrix/comparison;
4. economic line/bar chart;
5. timeline;
6. decision tree;
7. before/after bridge;
8. quantitative table/figure hybrid.

Arrow diagrams from earlier Golden prototypes are historical/temporary. The production system should favor cleaner, simpler relationships and less connector clutter.

---

# 10. Quantitative charts

Charts must be generated from reproducible data where practical.

Rules:

- axes and units explicit;
- no unnecessary scientific notation;
- observed vs modeled periods distinguishable;
- captions explain the decision-relevant pattern;
- restrained palette;
- no chartjunk;
- grayscale legibility remains a requirement.

Current Golden chart style (PGFPlots/LaTeX) is an acceptable baseline, subject to founder review.

---

# 11. Running navigation

Candidate print system:

- even page: Part name + page number;
- odd page: current Section/Chapter context + page number;
- thin neutral divider;
- no heavy header/footer furniture.

Page numbers should support navigation without drawing attention during reading.

---

# 12. Print behavior

Candidate production rules:

- Parts and Chapters may open on recto/right pages;
- intentional blank versos are acceptable in print-oriented output;
- PDF/tablet edition may later use a reduced-blank-page variant if useful;
- widow/orphan control required;
- no clipped boxes, formulas, figures or tables;
- every release requires full PDF render QA.

---

# 13. Source and publishing architecture

GitHub remains the canonical content/version source.

Publishing flow:

**GitHub content → controlled LaTeX publishing source → Prism/LaTeX editing and compilation → PDF/print output**

Prism is not the source of truth.

Content edits discovered during layout must be reconciled back into GitHub.

The publishing layer may contain:

- LaTeX template/style;
- figure build code;
- layout-specific transformations;
- indexes/glossary/bibliography configuration;
- print/PDF variants.

It must not silently fork the canonical manuscript.

---

# 14. Golden Production Test

Current prototype includes:

- cover;
- Part I opener;
- Chapter 1 opener;
- prose-led pages;
- `IN PRATICA`;
- `ESEMPIO SVOLTO`;
- system diagram;
- cause/amplifier/symptom diagram;
- Part VII opener;
- Chapter 25 opener;
- formulas;
- quantitative table;
- cohort/payback graph;
- chapter closing treatment;
- running heads/page numbering.

Format: 170 × 240 mm, two-sided.

Founder review is required before this becomes the production standard.

---

# 15. Acceptance gate

The design system passes when the founder judges that:

- it looks like a professionally published manual rather than an exported document;
- typography supports long reading;
- hierarchy is immediately legible;
- boxes/figures are useful rather than decorative;
- quantitative material feels native to the book;
- pages have enough variation without losing visual unity;
- the design does not make the manual feel academic, sterile or corporate;
- the system is strong enough to scale to the full manuscript without redesigning every chapter.

Until founder PASS: **CANDIDATE ONLY — DO NOT SCALE FULL PUBLISHING.**
