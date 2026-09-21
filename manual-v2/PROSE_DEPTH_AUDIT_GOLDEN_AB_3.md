# Prose Depth Audit — Golden A + Golden B, terzo prototipo

Date: 2026-09-21

## Verdict

**INTERNAL PASS — READY FOR THIRD FOUNDER READ**

This audit evaluates the prose-depth rewrite triggered by `FOUNDER_REVIEW_GOLDEN_AB_2.md`.

It does not declare founder approval.

---

# Scope

Current reader-facing prototypes:

- `golden/chapter-01/DRAFT.md` — `Il sistema di marketing`
- `golden/chapter-25/DRAFT.md` — `Economia del cliente`

Control system:

- `PROSE_DEPTH_SYSTEM.md`
- current `AUTHORIAL_STYLE_BIBLE.md`
- current `CHAPTER_GRAMMAR_V2.md`

Architecture remains unchanged from the founder-approved baseline.

---

# Quantitative comparison with second prototype

Rendered combined A/B founder preview:

- second prototype: 19 A4 pages; approximately 6,094 extracted words including cover/Part intros;
- third prototype: 25 A4 pages; approximately 8,962 extracted words including cover/Part intros;
- change: +6 pages / approximately +47% extracted words.

The increase is not treated as a quality result by itself.

Editorial inspection attributes the added material primarily to:

- causal mechanism;
- managerial consequences;
- concept boundaries;
- micro-examples;
- practical decision translation;
- stronger transitions between adjacent concepts.

No length target was used.

---

# Golden A audit — `Il sistema di marketing`

## Cohesion

**PASS**

Key improvements:

- chapter framing now develops why marketing is usually introduced too late rather than merely stating that it happens;
- `marketing vs promotion` now leads naturally into the system view through the question of what promotion cannot repair;
- system dependencies lead into metric hierarchy rather than appearing as an isolated diagram;
- metric hierarchy leads into diagnosis because better measurement still does not establish causality;
- cause/amplifier/symptom leads into strategy/tools through the distinction between understanding and accelerating a process.

Sections read as one developing argument rather than independent modules.

## Depth

**PASS**

Added explanation covers:

- consequences of treating marketing as downstream communication;
- limitations of agency/tool responsibility when upstream business decisions are frozen;
- forward and backward feedback loops in the commercial system;
- silo/local-optimization failure;
- activity vs operational effectiveness vs economic/capacity outcomes;
- containment vs structural correction;
- local technical failure as a boundary condition to systemic diagnosis;
- execution delegation vs judgment delegation.

## Practicality

**PASS**

Practical implications now appear inside the theory through:

- professional-service customer-selection micro-example;
- differentiation/price-comparison example;
- one-step-downstream KPI rule;
- KPI + downstream consequence pairing;
- containment/root-correction distinction;
- CRM/automation/AI decision examples.

The worked numerical example remains subordinate to theory.

## Voice

**PASS FOR FOUNDER TEST**

The rewrite uses firmer judgments where doctrine is strong without returning to slogan-heavy or theatrical prose.

Representative direction:

- `non chiedere al marketing di correggere ciò che l'impresa non ha ancora deciso`;
- `il fatto che un numero sia visibile non gli assegna automaticamente la priorità`;
- `intervenire rapidamente nel punto sbagliato può soltanto rendere più efficiente l'errore`.

These lines are supported by developed reasoning rather than used as isolated punchlines.

---

# Golden B audit — `Economia del cliente`

## Cohesion

**PASS**

The chapter now follows one economic question through time:

`investment to acquire → contribution while serving → cohort differences → future value → time to recover → allowable acquisition cost → marginal scale economics`.

Each concept becomes necessary because the previous concept leaves a material question unanswered.

## Depth

**PASS**

Added explanation covers:

- why unit choice matters;
- variable/incremental cost perimeter vs arbitrary overhead allocation;
- fully loaded CAC and attribution logic;
- cheap-lead/expensive-customer mechanism;
- cohort composition effects and decision-driven segmentation;
- observed vs modeled lifetime value;
- maturity of evidence and forecasting risk;
- limits of LTV:CAC ratios;
- payback as financeability, not only profitability;
- allowable CAC as an explicit management rule rather than a discovered universal number;
- segment-specific acquisition ceilings;
- historical average CAC vs marginal CAC;
- scaling through conversion/contribution/retention/service economics rather than media spend alone.

## Practicality

**PASS**

The chapter now contains practical questions in the core prose, including:

- what is the correct economic unit?;
- what resources disappear if these customers are not acquired?;
- would a cohort difference change a management decision?;
- how much future value is observed vs modeled?;
- how much contribution must be preserved for structure/profit/risk?;
- does the next euro of acquisition still satisfy the economics?

Worked examples remain reproducible and charts remain integral to the explanation.

## Voice

**PASS FOR FOUNDER TEST**

The chapter is more decisive on important points while preserving uncertainty around forecasts and modeled value.

Examples:

- `Il lead più economico può quindi produrre il cliente più costoso.`
- `il futuro non è un dato: è un modello.`
- `economia positiva e crescita finanziabile non sono sinonimi.`
- `non dovrebbe comprare quella crescita alle condizioni attuali senza modificare qualcosa.`

---

# AI-smell / over-expansion check

## Systematic templating

No new visible fixed section template has been introduced.

The prose-depth functions are internal controls, not reader-facing repeated blocks.

## Lists

Lists remain concentrated in:

- worked examples;
- numerical inputs;
- limited reference contexts.

They are not the explanatory grammar.

## Meta prose

Meta narration is reduced relative to prior prototypes. Some navigation remains where it helps a beginner understand scope and chapter-to-chapter dependency.

## Repetition

No material concept appears to have been expanded only by restating the same claim. Added length generally introduces a mechanism, boundary, consequence or practical interpretation.

## Named fictional companies

None reintroduced.

---

# Visual / PDF QA

Third combined preview build:

- GitHub Actions run: `35574017725`;
- conclusion: SUCCESS;
- pages: 25;
- page size: A4;
- openable: yes;
- encrypted: no;
- scanned: no.

Full PDF rendered at 150 DPI: 25/25 pages rendered successfully.

Visual inspection covered:

- chapter opening pages;
- prose-dense conceptual pages;
- formula pages;
- worked-example pages;
- cohort figure;
- payback chart;
- acquisition-threshold example;
- closing pages.

Findings:

- no clipping observed;
- no overlaps observed;
- no broken glyphs observed;
- tables and formulas remain readable;
- additional prose increased page count without creating obvious visual overload;
- arrow/process diagrams remain provisional visual design, as previously agreed.

---

# Gate result

Internal writing-quality gate:

- architecture drift: 0;
- doctrine P0/P1 found: 0;
- major prose-depth findings from founder review addressed: YES;
- PDF blocker: 0;
- founder approval: PENDING.

**Result: READY FOR THIRD FOUNDER READ.**

Golden C and production scaling remain blocked until founder verdict.