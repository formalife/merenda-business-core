# Golden B — Chapter 23 Spec

## Working title

**Quando un cliente merita altra crescita**

Backend chapter identity: V2 Chapter 23 — Unit economics, cohorts and growth levers.

Reader-facing title may change after drafting.

## Status

**READY FOR DRAFTING — INPUTS LOCKED**

Doctrine freshness checked against current `main` on 2026-09-21.

Primary live doctrine reread:

- `merenda/09_business/numeri-cassa-e-crescita.md`
- `merenda/09_business/retention-onboarding-e-customer-success.md`
- `merenda/03_offerta/front-end-e-back-end.md`
- relevant foundations/system doctrine already audited in earlier phases.

V2 systems:

- `FORMULA_CATALOG.md`
- `CASE_SYSTEM_V2.md`
- `VISUAL_SYSTEM.md`
- `AUTHORIAL_STYLE_BIBLE.md`
- `CHAPTER_GRAMMAR_V2.md`

Case lock:

- `CASE_LOCK.md`

---

# 1. Learning problem

A manager often sees one acquisition number — CAC — and one value number — revenue or a forecast LTV — then decides whether to scale.

That is insufficient.

Two cohorts with the same price and the same CAC can create radically different economics because:

- activation differs;
- service burden differs;
- retention/repeat behavior differs;
- contribution arrives at different speeds;
- acquisition cost is paid before its recovery;
- marginal acquisition economics can deteriorate as spend increases.

The reader needs to learn to reconstruct the **economic path of an acquired customer over time**, not memorize ratio benchmarks.

---

# 2. Central question

**Does the next customer create enough contribution, fast enough and with enough certainty, to deserve more acquisition?**

---

# 3. Target competence

After the chapter, the reader should be able to:

- distinguish revenue, variable cost and contribution;
- calculate a fully loaded CAC with a declared denominator;
- explain why cost per lead and CAC answer different questions;
- build/read an observed cohort contribution series;
- identify observed payback from cumulative contribution;
- distinguish observed contribution from modeled lifetime value;
- explain why equal CAC can hide unequal customers;
- use LTV:CAC only as a diagnostic summary, not a universal threshold;
- derive a company-specific allowable-CAC rule from an explicit horizon, required contribution and risk/cash buffer;
- distinguish historical average CAC from marginal CAC;
- identify which assumption would flip a scale/no-scale decision;
- transfer the same reasoning from subscription software to irregular repeat-purchase retail/e-commerce.

The chapter does **not** need to teach full cash-conversion-cycle mechanics; Chapter 24 owns that depth.

---

# 4. Doctrine that must survive the rewrite

## D1 — CAC is fully loaded

The economically useful acquisition cost includes the resources required to convert a person/account into a customer, not only media spend or cost per click/lead.

Scope must be declared.

## D2 — Revenue is not contribution

Money billed/collected is not the amount available to recover acquisition and support structure.

Variable delivery/service costs matter.

## D3 — CAC recovery has a time dimension

A customer that eventually generates value may still require substantial financing if contribution arrives slowly.

Payback must therefore be taught together with CAC/LTV.

## D4 — Cohorts can overturn averages

Source, segment, seller, activation and service burden can create materially different customer economics hidden inside one average.

## D5 — Observed evidence outranks optimistic lifetime assumptions

When cohort data exist, use them.

Future lifetime contribution remains a model/estimate until observed.

## D6 — LTV should be contribution-based for economic decisions

Do not label lifetime revenue as economic LTV.

Cost-to-serve and incremental retention/service costs cannot disappear from the model.

## D7 — LTV:CAC has no universal magic threshold

Ratio can summarize a relationship but can hide payback, uncertainty and capital needs.

No `3:1` or other universal benchmark is to be taught as doctrine.

## D8 — Allowable CAC is a decision rule

The ceiling depends on chosen horizon, expected/observed contribution, required return to structure/profit, cash availability, risk and objectives.

## D9 — Marginal CAC matters for scale

Historical average CAC does not answer whether the next block of spend works.

## D10 — Growth levers interact

Price, conversion, frequency, retention and acquisition volume are not independent. A change to one can affect contribution, service cost, demand quality, cash or capacity.

---

# 5. Narrative architecture

This is the intended argument, not a visible template.

## Movement 1 — Let the average CAC create the wrong confidence

Open with TurnoChiaro management reviewing two customer cohorts.

Both cohorts:

- 100 new paying accounts;
- €1,800 CAC;
- same €480/month price.

Management initially treats them as economically equivalent.

Ask the reader to hold that conclusion.

## Movement 2 — What does one euro of revenue leave behind?

Before cohort complexity, build the simplest economic bridge:

`€480 revenue - €120 normal variable service cost = €360 contribution/month for a normally active account`.

Explain what contribution is and is not.

Do not begin with a formula catalogue.

Introduce fully loaded CAC only after explaining why the first €480 invoice does not recover €1,800 acquisition cost.

## Movement 3 — Reveal activation/service burden

Show that Cohort A activates 90 accounts with €9k extra onboarding cost; Cohort B activates 65 with €25k.

This should create the first reinterpretation:

same sale ≠ same economic starting point.

Use a compact contribution bridge/waterfall.

## Movement 4 — Time turns economics into a financing problem

Introduce cumulative contribution by month.

Plot both cohort curves against the €180k CAC line.

Let the reader see Cohort A cross in Month 7 while B remains unrecovered through Month 12.

Then name **payback**.

Definition arrives after the visual problem.

## Movement 5 — Cohorts before averages

Show the Month-12 comparison table and explain why a blended average can hide two different businesses.

Explicitly separate:

- observed 12-month contribution;
- observed payback;
- future modeled lifetime value.

## Movement 6 — LTV without fortune telling

Explain lifetime contribution value as a model when future months are not yet observed.

Use the TurnoChiaro data to show what is known and what would require assumptions.

Introduce LTV:CAC only as a compact diagnostic and immediately show why equal ratios could still hide different payback/cash profiles.

## Movement 7 — The acquisition ceiling is chosen, not discovered

Use Cohort A observed 12-month contribution (€3,297.60/account) and management requirements:

- €700 to structure/profit;
- €400 risk/cash buffer.

Derive an illustrative allowable CAC ≈ €2,200.

Make explicit that this is a management decision rule under stated assumptions.

## Movement 8 — Average CAC vs marginal CAC

TurnoChiaro is offered the next acquisition block:

- €130k incremental spend;
- 50 expected incremental customers;
- marginal CAC = €2,600.

Historical CAC €1,800 is irrelevant to this block.

Discuss possible responses without forcing a binary answer.

## Movement 9 — Sensitivity: which assumption flips the decision?

Increase extra onboarding burden by €600/account.

Show the allowable ceiling fall from ≈€2,200 to ≈€1,600.

The old €1,800 CAC crosses the threshold.

Teaching point:

Sensitivity is not changing numbers for sport; it is finding which uncertainty changes the decision.

## Movement 10 — Transfer to Dispensa Nord

Move to irregular repeat purchase.

First-order economics are equal; repeat rates differ; inventory must be financed.

Do not solve completely.

Ask the reader to identify:

- contribution data needed for repeats;
- observation window;
- why churn formulas do not transfer mechanically;
- why cash can still constrain growth.

## Movement 11 — Close on the scale question

Return to the central question:

not `is CAC low?`, but `does the next customer create enough contribution, fast enough and with enough certainty to justify the next acquisition euro?`

Bridge to Chapter 24: even economically positive customers can create a cash problem when timing is adverse.

---

# 6. Formula sequence

Formulas should appear only when their question is alive in the prose.

## Formula A — contribution

`Contribution = revenue - variable costs attributable to serving the customer`

Classification: identity/management simplification.

## Formula B — fully loaded CAC

`CAC = attributable acquisition + sales costs / new customers acquired`

Classification: operational metric with attribution choices.

## Formula C — observed payback

Find first period where:

`cumulative observed contribution >= cohort CAC`.

Classification: operational metric.

## Formula D — lifetime contribution value

General form:

`expected total contribution over relationship - incremental retention/service costs not already included`.

Classification: estimate/model until fully observed.

## Formula E — LTV:CAC

`contribution-based lifetime/selected-horizon value / CAC`.

Classification: diagnostic ratio, no universal benchmark.

## Formula F — allowable CAC

`contribution over chosen horizon - required contribution to structure/profit - risk/cash buffer`.

Classification: decision rule.

## Formula G — marginal CAC

`incremental acquisition spend / incremental customers caused by that spend`.

Classification: operational metric/model depending forecast status.

---

# 7. Pedagogical features

Required:

- opener decision scene;
- one contribution bridge/waterfall;
- cohort comparison table;
- cumulative contribution/payback chart;
- one observed-vs-modeled visual marker;
- one `ESEMPIO SVOLTO` or integrated worked calculation for allowable CAC;
- one `COSA CAMBIA SE...` sensitivity prompt;
- one `TRASFERISCI` case using Dispensa Nord.

Optional if narrative needs it:

- `ERRORE FREQUENTE` box for LTV revenue / magic ratio benchmark;
- compact formula reference at chapter end.

Do not create a formula box for every formula.

---

# 8. Visual plan

Detailed in `VISUAL_BRIEF.md`.

Minimum prototype visuals:

1. **Figure 23.1 — Same CAC, different economic starting point**
   - contribution/onboarding bridge for A vs B.
2. **Figure 23.2 — Payback is visible when contribution is accumulated over time**
   - cumulative contribution curves with CAC recovery line.
3. **Table 23.1 — Two cohorts hidden inside one average CAC**
   - compact observed comparison.
4. **Figure/Table 23.3 — Observed vs modeled horizon**
   - visual boundary between known data and forecast assumptions, if needed.

The prototype must include at least one real quantitative chart rather than only tables.

---

# 9. AI-smell stress points

Run:

- `AI-SMELL`
- `AUTHOR-MIND`
- `HUMAN-RHYTHM`
- `LIST-CHALLENGE`
- `FORMULA-JOB`
- `DENOMINATOR-CHECK`
- `OBSERVED-VS-MODELED`
- `SENSITIVITY-CHECK`
- `CASE-CONTINUITY`

Specific warnings:

- do not write `CAC is... LTV is... payback is...` as a definition cascade;
- do not present eight formulas in sequence;
- do not use synthetic numbers as benchmarks;
- do not imply Cohort B is intrinsically a bad market forever;
- do not treat a forecast as observed evidence;
- do not teach a universal LTV:CAC threshold;
- do not let arithmetic crowd out decision interpretation;
- do not end every section with a boxed rule.

---

# 10. Depth target

Golden B should be long enough for a beginner to reproduce the calculations and understand the decisions.

Provisional range:

**5,000–8,000 words before final copyedit**, with substantial visual/table content.

Not a quota.

If the chapter needs fewer words because charts carry genuine explanatory load, do not pad it.

---

# 11. Audit plan

## Doctrine

- fully loaded CAC;
- contribution-based value;
- payback/cash time dimension;
- cohort/source granularity;
- no magic ratios;
- no optimistic LTV replacing observed evidence;
- marginal economics before scale.

## Instructional

- non-finance beginner can reproduce each required calculation;
- reader can explain why A and B differ despite same CAC;
- reader can separate observed vs modeled value;
- reader can use sensitivity to identify a decision threshold;
- transfer to irregular repeat-purchase context works.

## Editorial

- numbers appear inside an argument;
- formulas do not become the chapter's narrative skeleton;
- authorial judgment is visible;
- no spreadsheet-manual tone.

## Visual

- curve axes/units clear;
- CAC recovery line interpretable;
- observed/forecast distinction visible;
- no chart is ornamental;
- tables remain readable in grayscale/print.

## Founder-read

Can a non-finance entrepreneur follow the chapter, repeat the calculation and explain what decision changes because of it?