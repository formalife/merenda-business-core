# Golden B — Capitolo 25 Spec

## Titolo reader-facing

**Economia del cliente**

## Status

**READY FOR REWRITE — POST FOUNDER GATE**

The first Golden B draft passed internal audits but failed founder review on architecture, voice and example placement. Its quantitative content remains approved source material.

Primary doctrine already verified:

- `merenda/09_business/numeri-cassa-e-crescita.md`
- `merenda/09_business/retention-onboarding-e-customer-success.md`
- `merenda/03_offerta/front-end-e-back-end.md`

Current governing editorial artifacts:

- `EDITORIAL_HIERARCHY_V2.md`
- `CHAPTER_GRAMMAR_V2.md`
- `AUTHORIAL_STYLE_BIBLE.md`
- `CASE_SYSTEM_V2.md`
- `FORMULA_CATALOG.md`

---

# 1. Chapter job

Teach how to evaluate the economic value of acquired customers over time.

The chapter deepens the minimum economic vocabulary introduced in Chapter 2 and shows why averages can hide materially different customer economics.

The reader should understand the relationships among:

- unit economics;
- cohorts;
- lifetime value;
- payback;
- sustainable acquisition cost;
- marginal acquisition economics.

The chapter is quantitative, but the logic of the measures is primary and the numerical example is subordinate.

---

# 2. General framing requirement

The opening must explain before calculations:

- why revenue does not equal customer value;
- why CAC alone does not describe the economics of a customer;
- why time, retention and cost-to-serve matter;
- why grouping customers into cohorts can reveal differences hidden by averages;
- how the six sections of the chapter fit together.

Do not open with a named fictional software company or a cohort puzzle.

---

# 3. Mandatory sections

## 25.1 Unit economics

Explain:

- economic unit of analysis;
- revenue vs variable service/delivery cost;
- contribution margin;
- fully loaded CAC;
- why denominator/perimeter choices matter.

Worked example after theory:

A generic subscription business charges €480/month and has €120/month variable service cost per active account; CAC = €1,800.

## 25.2 Analisi per coorti

Explain:

- what a cohort is;
- why acquisition month/source/segment/onboarding can create different economics;
- why averages can hide differences;
- which dimensions justify cohort separation.

Worked example:

Two cohorts, A and B, each with 100 acquired accounts and €1,800 CAC, but different activation, onboarding burden and retention.

## 25.3 Lifetime value

Explain:

- revenue LTV vs contribution-based economic value;
- observed horizon vs modeled lifetime;
- service/retention costs;
- assumptions and uncertainty.

Use the A/B data to show what is observed and what would require forecasting.

## 25.4 Payback avanzato

Explain:

- recovery of acquisition cost over time;
- observed cumulative contribution;
- relationship with cash financing;
- why equal LTV can coexist with different financing burdens.

Chart:

cumulative contribution of Coorte A and B against the acquisition-cost line.

## 25.5 Costo massimo di acquisizione

Explain:

- allowable/sustainable CAC as a management decision rule;
- chosen horizon;
- contribution reserved for structure/profit;
- risk/cash buffer;
- no universal threshold.

Worked calculation after theory using Coorte A data.

## 25.6 Costo marginale e leve di crescita

Explain:

- historical average CAC vs marginal CAC;
- next block of acquisition spend;
- sensitivity analysis;
- how price, service cost, activation, retention and frequency can change the ceiling.

Close by connecting to Chapter 26 on cash and working capital.

---

# 4. Doctrine that must survive

1. CAC must use an economically useful attributable perimeter.
2. Revenue is not contribution.
3. Customer economics unfold over time.
4. Cohorts can overturn blended averages.
5. Observed evidence outranks optimistic lifetime assumptions.
6. Economic LTV should be contribution-based for decisions.
7. LTV:CAC is a summary, not a universal traffic light.
8. Sustainable CAC is a decision rule, not a natural constant.
9. Marginal CAC matters for scale.
10. Growth levers interact with service cost, cash and capacity.

---

# 5. Numerical example baseline

Use generic labels only.

## Common acquisition facts

- Coorte A: 100 acquired accounts
- Coorte B: 100 acquired accounts
- CAC per account: €1,800
- Total acquisition cost per cohort: €180,000
- Price: €480/month
- Normal variable service cost: €120/month
- Contribution of a normally active account: €360/month

## Activation/onboarding

Coorte A:

- 90 active/activated in month 1
- €9,000 extra onboarding burden

Coorte B:

- 65 active/activated in month 1
- €25,000 extra onboarding burden

## Month-12 observed outcomes from first prototype

Coorte A:

- active accounts month 12: 69
- cumulative contribution at month 12: €329,760
- payback: month 7

Coorte B:

- active accounts month 12: 29
- cumulative contribution at month 12: €169,760
- CAC not yet recovered at month 12

Months 13–14, if used, must be explicitly labeled illustrative/forecast extension rather than observed.

## Allowable-CAC example

Coorte A observed 12-month contribution per acquired account:

- €3,297.60

Illustrative management requirements:

- €700 contribution to structure/profit
- €400 risk/cash buffer

Sustainable CAC rule under those assumptions:

- €3,297.60 − €700 − €400 = €2,197.60 ≈ €2,200

## Marginal block example

- incremental acquisition/sales spend: €130,000
- expected incremental customers: 50
- marginal CAC: €2,600

## Sensitivity example

If next cohort requires €600 more service/onboarding per acquired account:

- 12-month contribution falls from €3,297.60 to €2,697.60
- same decision rule yields ≈ €1,597.60 sustainable CAC

These are teaching assumptions, not benchmarks.

---

# 6. Example rules

Do not use:

- `TurnoChiaro`;
- `Dispensa Nord`;
- any invented branded company.

Use:

- `un software in abbonamento`;
- `Coorte A / Coorte B`;
- a generic ecommerce repeat-purchase transfer example.

The theory must remain complete if every worked example is removed.

---

# 7. Visual requirements

Retain the strongest quantitative visual work from the first Golden B:

1. comparison of same CAC / different starting economics;
2. cumulative contribution/payback chart;
3. cohort table;
4. optional observed-vs-modeled marker.

Graphic labels must be generic.

Charts remain approved in principle; diagrams can be refined later.

---

# 8. Voice requirements

Run:

- `PLAIN-ITALIAN`;
- `REMOVE-STAGECRAFT`;
- `AUTHOR-DISAPPEAR`;
- `PARAGRAPH-CONTINUITY`;
- `RHETORIC-REPEAT`;
- `THEORY-FIRST`;
- `MANUAL-VOICE`.

Avoid:

- `il CAC non mente...` aphorisms;
- dramatic reveals;
- artificial questions before every formula;
- formula catalogue tone;
- named-case storytelling;
- universal ratio benchmarks.

---

# 9. Founder-read gate

Golden B succeeds only if founder review confirms:

- the chapter explains the economic framework before the worked dataset;
- the title is simple and general;
- sections are logically visible and navigable;
- prose is natural Italian;
- numerical examples remain strong and reproducible;
- charts clarify rather than perform;
- no fictional-brand dependency remains;
- the chapter feels like a quantitative chapter in a professional manual rather than a constructed business case.
