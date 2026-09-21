# Golden B — Visual Brief

## Chapter

V2 Chapter 23 — Unit economics, cohorts and growth levers

Working reader-facing title: **Quando un cliente merita altra crescita**

## Visual objective

The chapter must let a non-finance reader **see** why two cohorts with the same price and CAC can require different growth decisions.

The visuals should carry time, accumulation and comparison. Prose should carry judgment, assumptions and limits.

---

# Figure 23.1 — Same CAC, different economic starting point

## Teaching job

Show that the first invoice is not the same thing as economic value and that activation/onboarding burden changes the starting economics of a cohort.

## Preferred form

Two side-by-side contribution bridges for one acquired account/cohort.

Reader should see:

### Common commercial surface

- subscription price: €480/month;
- fully loaded CAC: €1,800/account.

### Cohort A

- normal recurring variable service cost: €120/month for an active account;
- normal active contribution: €360/month;
- 90/100 accounts activated Month 1;
- extra onboarding burden: €9,000 total.

### Cohort B

- same normal recurring price/contribution structure once healthy;
- 65/100 accounts activated Month 1;
- extra onboarding burden: €25,000 total.

The figure should make it clear that `same price + same CAC` does not imply `same contribution starting point`.

## Do not

- label B as permanently bad;
- imply onboarding cost is the only difference;
- display more arithmetic than the reader needs at this stage.

---

# Figure 23.2 — Payback appears only when contribution is accumulated over time

## Teaching job

Make the time dimension visible.

## Preferred form

Line chart with:

- x-axis = months since acquisition, 0–14;
- y-axis = cumulative observed/illustrative contribution for the entire 100-account cohort;
- horizontal reference line at **€180,000 cohort CAC**;
- Cohort A cumulative contribution curve;
- Cohort B cumulative contribution curve.

Mark:

- Cohort A crosses CAC in Month 7;
- Cohort B is still below CAC at Month 12;
- Months 13–14 for B must be visually marked as illustrative extension unless explicitly framed as subsequently observed in the synthetic timeline.

## Visual semantics

Use line style or shaded region — not color alone — to distinguish observed and illustrative/future data.

Potential treatment:

- solid line through Month 12;
- dashed B line for Months 13–14.

## Reader takeaway

> CAC tells us what we paid. Payback tells us how long the business has to finance that decision before contribution earns the money back.

---

# Table 23.1 — Two cohorts hidden inside one average CAC

## Teaching job

Make the two cohorts directly comparable after the reader has seen the curves.

Columns:

- metric;
- Cohort A;
- Cohort B.

Rows:

- acquired accounts;
- CAC/account;
- Month-1 activation;
- extra Month-1 onboarding cost;
- Month-12 active accounts;
- 12-month observed contribution;
- observed contribution per acquired account;
- CAC recovered by Month 12?;
- payback status.

Avoid excessive row count.

---

# Figure 23.3 — Observed evidence ends before modeled lifetime value

## Teaching job

Prevent the reader from turning a 12-month observation into a false lifetime fact.

## Preferred form

Horizontal time band or continuation of the cohort curve:

- Months 0–12 = **observed**;
- after Month 12 = **model/forecast**;
- label the assumptions needed beyond observation: retention, service cost, price, account behavior.

## Reader takeaway

> The farther the model extends beyond observed behavior, the more the number becomes an assumption about the future rather than a measurement of the past.

This visual may be merged with Figure 23.2 if doing so reduces split attention.

---

# Figure 23.4 — Average CAC is not marginal CAC

## Teaching job

Show that the economics of the next acquisition block can differ from historical averages.

## Preferred form

Compact comparison, not necessarily a chart:

- historical CAC: €1,800;
- illustrative management ceiling: ~€2,200;
- next block marginal CAC: €2,600.

Could be a horizontal threshold graphic with a clear caveat that the €2,200 ceiling is built from TurnoChiaro's chosen assumptions, not a universal benchmark.

---

# Formula presentation visual

Formulas should not be converted into decorative equation cards.

Use display emphasis only for relationships the reader must reuse:

- contribution;
- fully loaded CAC;
- observed payback condition;
- allowable CAC;
- marginal CAC.

LTV:CAC may remain inline/table if a large equation adds no learning value.

---

# Transfer visual — Dispensa Nord

No new chart is required unless the draft demonstrates a need.

A compact table can show:

- same first-order revenue/contribution/CAC;
- repeat group X: 42/100 repurchase within 90 days;
- repeat group Y: 16/100;
- inventory funded before sale.

The reader should do the conceptual transfer without being given a finished LTV chart.

---

# Visual QA

Run:

- `VISUAL-JOB`
- `PROSE-OR-VISUAL`
- `REDUNDANCY-CHECK`
- `SPLIT-ATTENTION`
- `DATA-CLAIM-CHECK`
- `ACCESSIBILITY-CHECK`
- `OBSERVED-VS-MODELED`

Golden B-specific checks:

1. Do the curves make payback understandable before the formal definition?
2. Can the chart be read in grayscale?
3. Is the €180k acquisition line clearly a cohort cost, not monthly revenue?
4. Are Months 13–14 visually distinguishable from observed Months 1–12?
5. Does any figure accidentally imply a magic CAC/LTV benchmark?
6. Are tables compact enough to read at normal print size?
7. Does every visual change or clarify a decision?

---

# Prototype requirement

Golden B must render at least:

- one quantitative line chart;
- one economic comparison table;
- one contribution/starting-economics visual or equivalent explanatory exhibit.

All numbers must trace back to `CASE_LOCK.md`.