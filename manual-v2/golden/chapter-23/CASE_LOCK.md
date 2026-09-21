# Golden B — Case Lock: TurnoChiaro Cohort Economics

## Status

**LOCKED FOR CHAPTER 23 PROTOTYPE — synthetic teaching data**

This is a fictional recurring case. All numbers are synthetic and exist to teach unit economics, cohort payback, observed vs modeled value and growth decisions. They are not SaaS benchmarks.

Do not change the reader-facing numbers inside Golden B without updating this file and the audit trail.

---

# Business context

`TurnoChiaro` sells subscription software for shift scheduling and workforce coordination to multi-location service businesses.

Base commercial model used in earlier V2 planning:

- monthly subscription revenue per paying account: **€480**;
- recurring variable service/support cost for a normally functioning account: **€120/month**;
- recurring contribution from a normally functioning active account: **€360/month**;
- fully loaded acquisition cost in the two cohorts examined here: **€1,800 per newly acquired paying account**.

The company has been reporting blended CAC around €1,800 and initially considers acquisition efficient.

The problem: account types differ materially in implementation effort, activation and retention.

---

# Why two cohorts exist

The sales team historically treated two account types as economically equivalent because:

- both buy the same €480/month plan;
- both show approximately €1,800 fully loaded CAC;
- both are counted as new paying customers when contracts start.

They are not operationally equivalent.

## Cohort A — Standard-fit accounts

Typical profile:

- 2–5 locations;
- relatively standard scheduling rules;
- one operational owner responsible for implementation;
- data import usually clean;
- self-service setup plus limited assisted onboarding is usually sufficient.

## Cohort B — Complex implementation accounts

Typical profile:

- more locations and exceptions;
- fragmented responsibility;
- older data/processes that require cleanup;
- multiple stakeholders before the workflow becomes stable;
- materially more assisted onboarding/support.

The chapter must not frame Cohort B as a universally bad segment. It is bad **under the current price/process/economics**. Later redesign could change the conclusion.

---

# Acquisition baseline

Each cohort begins with **100 newly acquired paying accounts**.

For both Cohort A and Cohort B:

- fully loaded acquisition + sales cost: **€180,000 total**;
- new paying accounts: **100**;
- fully loaded CAC: **€1,800/account**.

At this point a blended CAC dashboard makes the cohorts look identical.

---

# Activation and onboarding difference

## Cohort A

- accounts reaching first usable scheduling workflow during Month 1: **90**;
- extra variable onboarding/support cost in Month 1 beyond normal recurring service: **€9,000 total**.

## Cohort B

- accounts reaching first usable scheduling workflow during Month 1: **65**;
- extra variable onboarding/support cost in Month 1 beyond normal recurring service: **€25,000 total**.

Interpretation:

- the commercial event `customer acquired` happened for 100 accounts in both cohorts;
- economic value creation does not begin equally for all of them;
- unactivated or badly activated accounts can still create support cost and early churn.

---

# Observed active-account series

For the prototype, `active account` means an acquired account that has completed setup sufficiently to receive ongoing value and remains a paying, serviced account during the period.

## Cohort A — observed active accounts

| Month | Active accounts |
|---:|---:|
| 1 | 90 |
| 2 | 88 |
| 3 | 85 |
| 4 | 83 |
| 5 | 81 |
| 6 | 79 |
| 7 | 77 |
| 8 | 75 |
| 9 | 73 |
| 10 | 71 |
| 11 | 70 |
| 12 | 69 |

Monthly recurring contribution before the extra Month-1 onboarding cost:

`active accounts × €360`.

Month 1 cohort contribution after extra onboarding:

`90 × €360 - €9,000 = €23,400`.

Observed 12-month cumulative contribution before acquisition cost:

**€329,760**.

Observed contribution per acquired account over 12 months:

**€3,297.60**.

Observed cohort CAC:

**€180,000**.

Observed CAC payback:

cumulative cohort contribution first exceeds €180,000 in **Month 7**.

Observed 12-month contribution after CAC:

**€149,760 total**, or **€1,497.60 per acquired account** before fixed structure/tax/capital charges.

---

## Cohort B — observed active accounts

| Month | Active accounts |
|---:|---:|
| 1 | 65 |
| 2 | 62 |
| 3 | 57 |
| 4 | 53 |
| 5 | 49 |
| 6 | 45 |
| 7 | 42 |
| 8 | 39 |
| 9 | 36 |
| 10 | 33 |
| 11 | 31 |
| 12 | 29 |

Month 1 cohort contribution after extra onboarding:

`65 × €360 - €25,000 = -€1,600`.

Observed 12-month cumulative contribution before acquisition cost:

**€169,760**.

Observed contribution per acquired account over 12 months:

**€1,697.60**.

Observed cohort CAC:

**€180,000**.

Observed status at Month 12:

**CAC has not yet been recovered.**

If the following illustrative active-account counts occur:

- Month 13: 27 active accounts → €9,720 contribution;
- Month 14: 25 active accounts → €9,000 contribution;

then cumulative contribution would first exceed the original €180,000 CAC in **Month 14**.

Months 13–14 are an extension used to demonstrate observed payback if the specified counts are later observed; they must not be silently treated as a forecast when discussing Month-12 evidence.

---

# Core comparison

| Metric | Cohort A | Cohort B |
|---|---:|---:|
| Newly acquired paying accounts | 100 | 100 |
| Fully loaded CAC/account | €1,800 | €1,800 |
| Month-1 activated accounts | 90 | 65 |
| Extra Month-1 onboarding cost | €9,000 | €25,000 |
| Month-12 active accounts | 69 | 29 |
| 12-month observed contribution | €329,760 | €169,760 |
| 12-month observed contribution/acquired account | €3,297.60 | €1,697.60 |
| CAC recovered by Month 12? | Yes | No |
| Observed/illustrative payback | Month 7 | Month 14 if M13–M14 counts occur |

Teaching point:

**same subscription price + same headline CAC ≠ same customer economics.**

Activation, service burden and retention change the contribution curve and the capital required to grow.

---

# Observed vs modeled boundary

The chapter must explicitly distinguish:

## Observed through Month 12

- acquired accounts;
- CAC;
- activation;
- extra onboarding cost;
- active-account counts;
- contribution generated through Month 12.

## Estimate/model beyond Month 12

Any future LTV or future retention beyond observed data is an estimate unless the chapter labels later months as subsequently observed in the synthetic timeline.

The chapter may calculate a **12-month observed contribution value** without calling it full lifetime value.

A modeled LTV may be introduced only after the reader sees why extending the horizon requires assumptions.

---

# LTV:CAC teaching use

At Month 12:

- Cohort A observed contribution/CAC ratio: `€329,760 / €180,000 ≈ 1.83`;
- Cohort B observed contribution/CAC ratio: `€169,760 / €180,000 ≈ 0.94`.

These ratios are descriptive of the chosen 12-month observation window.

They must **not** be presented as universal good/bad benchmarks.

A later forecast could increase either ratio, but it also increases assumption risk.

---

# Acquisition ceiling / allowable CAC scenario

To teach that allowable CAC is a management rule rather than a universal formula, use Cohort A's **observed 12-month contribution per acquired account = €3,297.60**.

Suppose management wants, over the chosen 12-month horizon:

- at least **€700/account** of contribution available for fixed structure/profit;
- a **€400/account** risk/cash buffer because future cohorts may perform worse and acquisition is paid before contribution is recovered.

Then one chosen decision rule is:

`allowable CAC = €3,297.60 - €700 - €400 = €2,197.60`.

Round operational ceiling for the example: **about €2,200**.

This is not a doctrine benchmark. It is a company-specific threshold built from:

- chosen observation horizon;
- observed contribution;
- required structure/profit contribution;
- risk/cash buffer.

---

# Marginal CAC scale scenario

TurnoChiaro considers buying the next block of acquisition.

Historical/blended CAC for Cohort A-like accounts: **€1,800**.

Proposed incremental campaign:

- additional acquisition + sales spend: **€130,000**;
- expected incremental customers under the media plan: **50**.

Marginal CAC if the plan performs exactly as forecast:

`€130,000 / 50 = €2,600`.

This exceeds the illustrative management ceiling of about €2,200.

Teaching point:

Historical average CAC does not answer whether the **next** euro of acquisition is attractive.

Possible decisions are not limited to `scale` or `stop`:

- improve conversion or sales efficiency;
- improve activation/retention and thereby observed contribution;
- change target/segment mix;
- redesign onboarding for Cohort B-like accounts;
- raise price if value/market conditions support it;
- reduce expected volume;
- reject the incremental acquisition block.

The chapter should not prescribe one without further evidence.

---

# Sensitivity scenario

Use Cohort A to show how one assumption can change the decision.

Base observed 12-month contribution/acquired account:

**€3,297.60**.

Sensitivity question:

What if the next cohort has the same CAC and price but extra onboarding cost rises by **€600/account** because more customers need human implementation?

All else equal, 12-month contribution per acquired account would fall by €600 to approximately:

**€2,697.60**.

Using the same €700 structure/profit requirement and €400 risk/cash buffer:

new illustrative allowable CAC becomes:

`€2,697.60 - €700 - €400 = €1,597.60`.

The old €1,800 CAC would now exceed the chosen ceiling.

Teaching point:

The relevant question is not whether one metric moved, but **which assumption crosses the decision threshold**.

---

# Transfer case — Dispensa Nord

Golden B should end with a compact transfer case, not a worked full solution.

Locked inputs:

- average first online order revenue: **€68**;
- variable product/packing/fulfillment/payment cost: **€36**;
- first-order contribution before acquisition: **€32**;
- blended new-customer CAC: **€24**;
- first-order contribution after CAC: **€8/customer**;
- repeat purchase is irregular, not subscription-based;
- inventory must often be purchased before the final sale occurs.

Two observed 90-day customer groups:

### Group X

- 100 acquired customers;
- 42 make at least one repeat purchase within 90 days.

### Group Y

- 100 acquired customers;
- 16 make at least one repeat purchase within 90 days.

Do **not** give a full lifetime-value forecast.

Reader task:

- explain why equal first-order economics do not make X and Y equivalent;
- identify what repeat-purchase contribution data are needed;
- explain why inventory/cash timing creates an additional question even if contribution is positive;
- state why subscription churn formulas should not be copied mechanically into this category.

---

# What the case must teach

Golden B must make the reader able to say, in ordinary language:

1. CAC is not cost per lead and must include the real acquisition/sales burden;
2. contribution, not revenue, funds CAC recovery and structure;
3. payback adds time to customer economics;
4. averages can hide materially different cohorts;
5. observed cohort data deserve priority over optimistic lifetime assumptions;
6. LTV is a contribution estimate unless fully observed;
7. LTV:CAC is descriptive, not a universal law;
8. allowable CAC is a chosen threshold derived from economics, risk and objectives;
9. marginal CAC answers a different question from historical average CAC;
10. growth deserves more spending only when the incremental economics, cash and capacity still hold.

---

# Continuity note

These values should become the working `TurnoChiaro` cohort dataset for later V2 use unless a later chapter documents an explicit business event that changes them.

Future process/onboarding chapters may use the Cohort B evidence to justify redesign, but must not retroactively improve these historical cohort results.