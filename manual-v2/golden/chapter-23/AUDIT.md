# Golden B Audit — Chapter 23

Date: 2026-09-21

## Verdict

**INTERNAL PASS — founder-read still pending.**

Golden B has passed the internal doctrine, quantitative, instructional, editorial and visual gates required before founder review.

The chapter does not authorize production scaling. Phase 6 still requires Golden C and explicit founder approval of the three-prototype reading experience.

---

# Prototype inspected

Reader-facing chapter:

- `DRAFT.md`
- working title: **Quando un cliente merita altra crescita**

Supporting artifacts:

- `SPEC.md`
- `CASE_LOCK.md`
- `VISUAL_BRIEF.md`
- `figures/figure-23-1-same-cac-different-start.svg`
- `figures/figure-23-2-cohort-payback.svg`

Latest layout prototype:

- 13 A4 pages;
- approximately 4,020 words by workflow `wc`;
- rendered and inspected page-by-page;
- second render performed after fixing an actual Figure 23.1 text-overflow defect;
- no remaining clipping/overlap observed in the revised prototype.

The provisional 5,000–8,000 word band in the spec remains a diagnostic range rather than a quota. The figures and worked calculations carry genuine explanatory load, so the chapter should not be padded merely to meet the initial range.

---

# 1. Doctrine audit

## Fully loaded CAC

**PASS.**

The chapter explicitly distinguishes cost per click/lead/opportunity from customer acquisition cost and includes sales/commercial resources inside the chosen CAC scope.

It also makes the denominator explicit.

## Revenue vs contribution

**PASS.**

The chapter moves from €480 revenue to €360 recurring contribution only after subtracting attributable recurring service cost.

It never uses revenue LTV as economic customer value.

## Payback and time

**PASS.**

CAC recovery is taught as cumulative contribution crossing acquisition cost.

The chapter explains that equal eventual value can still imply different financing needs when payback differs.

## Cohort granularity

**PASS.**

The same €1,800 CAC is deliberately shown to hide materially different activation, onboarding burden, retention and contribution curves.

The conclusion is not that Cohort B is intrinsically bad. It is weaker under the current price/process/economics and could be redesigned.

## Observed vs modeled value

**PASS.**

Months 1–12 are treated as observed case evidence. Months 13–14 for Cohort B are explicitly hypothetical/illustrative and visually dashed.

Future lifetime value is identified as a model/estimate unless fully observed.

## LTV:CAC

**PASS.**

The chapter refuses universal magic thresholds.

The 1.83 and 0.94 ratios are explicitly described as summaries of the chosen 12-month observation window, not as universal good/bad scores.

## Allowable CAC

**PASS.**

The ≈€2,200 acquisition ceiling is labeled as a management decision rule based on:

- observed 12-month contribution;
- required contribution to structure/profit;
- explicit risk/cash buffer.

It is not taught as doctrine or benchmark.

## Marginal CAC

**PASS.**

Historical CAC and the economics of the next spend block are separated.

The €2,600 marginal CAC is conditional on the forecast of 50 incremental customers from €130k incremental spend.

### Doctrine finding

- P0: 0
- P1: 0
- P2: 0 blocking

---

# 2. Quantitative audit

## TurnoChiaro Cohort A

Inputs:

- 100 acquired accounts;
- cohort CAC €180,000;
- normal active contribution €360/month;
- extra Month-1 onboarding €9,000;
- active-account series matches `CASE_LOCK.md`.

Verified outputs:

- Month 1 contribution = €23,400;
- 12-month cumulative observed contribution = €329,760;
- observed contribution/acquired account = €3,297.60;
- CAC recovery first occurs in Month 7;
- contribution after CAC at Month 12 = €149,760 total before fixed structure/tax/capital charges.

**PASS.**

## TurnoChiaro Cohort B

Inputs:

- 100 acquired accounts;
- cohort CAC €180,000;
- extra Month-1 onboarding €25,000;
- active-account series matches `CASE_LOCK.md`.

Verified outputs:

- Month 1 contribution = −€1,600;
- 12-month cumulative observed contribution = €169,760;
- CAC not recovered by Month 12;
- illustrative Month 13/14 extension reaches €188,480 and crosses CAC in Month 14 if those counts occur.

**PASS.**

## Decision-rule arithmetic

Base illustrative allowable CAC:

`€3,297.60 - €700 - €400 = €2,197.60`

Rounded operationally to about €2,200.

Sensitivity with +€600/account onboarding burden:

`€2,697.60 - €700 - €400 = €1,597.60`

Marginal acquisition block:

`€130,000 / 50 = €2,600`.

**PASS.**

No synthetic number is represented as an external benchmark.

---

# 3. Instructional audit

## Problem before formula

**PASS.**

The chapter opens with two cohorts that appear identical on price/CAC and reveals the economic divergence before teaching the relevant formulas.

Definitions are earned by a live decision problem.

## Formula progression

**PASS.**

The sequence is:

- revenue leaves contribution;
- acquisition cost requires recovery;
- cumulative contribution creates payback;
- cohort comparison creates the need for segmentation;
- unobserved future creates the need for LTV/model caveat;
- growth decision creates allowable CAC;
- incremental spend creates marginal CAC;
- uncertainty creates sensitivity analysis.

The formulas do not arrive as a glossary cascade.

## Beginner reproducibility

**PASS.**

The calculations use visible inputs and simple arithmetic. A non-finance reader can reconstruct the core results without an external spreadsheet.

## Decision interpretation

**PASS.**

Each calculation changes or narrows a decision. The chapter does not stop at obtaining a numerical result.

## Sensitivity

**PASS.**

The +€600/account onboarding scenario demonstrates the correct job of sensitivity analysis: identify which plausible variable can flip the acquisition decision.

## Transfer

**PASS.**

Dispensa Nord forces the same reasoning into irregular repeat purchase and inventory. The chapter explicitly blocks mechanical transfer of subscription churn formulas.

## Bridge to cash chapter

**PASS.**

The closing unresolved problem is timing of cash outflow/inflow, not a generic editorial transition.

### Instructional finding

- P0: 0
- P1: 0
- P2: 0 blocking

---

# 4. Editorial / AI-smell audit

## Spreadsheet-manual risk

**PASS.**

The chapter remains a narrative about a management decision. Formulas and tables support the argument rather than becoming its skeleton.

## List density

**PASS.**

Lists are rare and used for actual assumption sets/decision alternatives. Exposition remains paragraph-driven.

## Formula-box density

**PASS with production note.**

Several displayed equations appear around the allowable/marginal CAC section. In the rendered prototype this remains readable and does not become a formula catalogue.

Production-stage design should preserve hierarchy so equation treatment does not visually compete with principle/error boxes.

## Repetitive rhetorical templates

**NOT OBSERVED at blocking level.**

No systematic `definition → bullets → rule` loop or serial `not X but Y` structure returns.

## Authorial judgment

**PASS.**

The prose repeatedly distinguishes what a number can establish from what remains unknown or managerial.

### Editorial finding

- P0: 0
- P1: 0
- P2: final design harmonization only

---

# 5. Visual audit

## Figure 23.1

Initial render finding:

**P1 visual defect found and fixed.**

The bottom takeaway line overflowed the SVG frame in the first PDF prototype.

Correction:

- takeaway box enlarged;
- sentence split across two centered lines;
- revised PDF re-rendered and visually re-inspected.

Current status: **PASS.**

Learning job is clear: same surface price/CAC, different activation/onboarding economics in Month 1.

## Figure 23.2

**PASS.**

The payback curve makes time visible before formal definition.

- axes have units;
- €180k cohort CAC line is explicit;
- Cohort A recovery is visible at Month 7;
- Cohort B is below CAC at Month 12;
- Month 13–14 extension is dashed and labeled illustrative;
- meaning does not depend solely on color.

## Cohort comparison table

**PASS.**

It compresses evidence already explained instead of introducing unexplained numbers.

## Overall 13-page layout

**PASS.**

The pages alternate sustained prose, equations, one comparison table and two quantitative visuals without collapsing into a slide deck or finance handout.

### Visual finding

- P0: 0
- P1: 0 open
- P2: final typography/production styling only

---

# 6. Depth decision

The prototype is about **4,020 words**, below the provisional 5,000–8,000 range.

Decision:

**DO NOT PAD.**

The chapter already includes:

- opening management tension;
- contribution explanation;
- fully loaded CAC scope;
- activation/service burden;
- cumulative cohort/payback;
- cohort segmentation;
- observed vs modeled lifetime value;
- LTV:CAC caveat;
- allowable CAC worked example;
- marginal CAC;
- sensitivity;
- cross-model transfer case;
- bridge to cash timing.

If founder review finds a missing reasoning step, add that step. Do not add generic prose to hit a word target.

---

# 7. System lessons from Golden B

Golden B validates several V2 systems:

1. formulas can be introduced after their decision problem rather than as a reference list;
2. a recurring synthetic case can support coherent multi-period arithmetic;
3. visual distinction between observed and modeled data materially improves honesty;
4. sensitivity analysis is most teachable when tied to a decision threshold;
5. average-vs-marginal economics deserves explicit treatment before scale;
6. quantitative chapters can be shorter in prose when charts/tables genuinely carry explanation;
7. actual PDF rendering is mandatory: it caught a figure overflow that text review did not.

No Layer 1 doctrine change is required.

No architecture change is required by Golden B.

---

# 8. Founder-read gate

**PENDING.**

Primary founder question:

> Could a non-finance entrepreneur reproduce the calculations and explain what decision changes because of them without feeling that the chapter became a spreadsheet tutorial?

---

# Internal decision

**GOLDEN B = INTERNAL PASS / FOUNDER REVIEW PENDING.**

Proceed to Golden C prototyping.

The remaining 28 chapters remain blocked until Golden C passes internally and the founder explicitly approves the golden-prototype reading experience.