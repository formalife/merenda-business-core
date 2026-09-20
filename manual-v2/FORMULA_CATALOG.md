# Formula Catalog — Manual V2

## Purpose

This catalog governs how V2 teaches business quantities.

The manual must not present formulas as decorative sophistication or universal truth.

Every quantitative relationship must be classified as one of:

- **IDENTITY** — follows from definitions/accounting structure;
- **OPERATIONAL METRIC** — useful measurement whose denominator/scope must be defined;
- **ESTIMATE/MODEL** — depends on assumptions about future behavior or attribution;
- **DECISION RULE** — management threshold chosen from economics, risk and objectives.

The teaching sequence remains:

**business question → quantities → formula/model → worked example → interpretation → sensitivity → misuse/limit.**

---

# 1. Variable conventions

Use consistent notation only where it improves clarity.

Reader-facing prose should normally show the plain-language variable name first.

Suggested symbols for displayed formulas:

- `R` = revenue / ricavi;
- `VC` = variable costs / costi variabili;
- `CM` = contribution margin / margine di contribuzione;
- `FC` = fixed costs / costi fissi;
- `CAC` = customer acquisition cost;
- `LTV_CM` = lifetime contribution margin, not lifetime revenue;
- `AOV` = average order value;
- `f` = purchase frequency over a defined period;
- `r` = retention probability/rate where model structure justifies it;
- `C` = practical capacity;
- `U` = capacity used;
- `DSO`, `DIO`, `DPO` = cash-conversion components where relevant.

Avoid symbolic notation when plain arithmetic is easier for the intended reader.

---

# 2. Core economic identities and metrics

## F-01 — Revenue

**Class:** IDENTITY

`Revenue = price × quantity sold`

For a multi-transaction customer view, a useful decomposition can be:

`Revenue over period = customers × average transaction value × average purchase frequency`

### Teaching job

Show that revenue can rise through different mechanisms with different economics.

### Misuse

Treating revenue as contribution/profit/cash.

---

## F-02 — Contribution margin per transaction/customer

**Class:** IDENTITY / management accounting simplification

`CM = net revenue - variable costs attributable to serving the transaction/customer`

### Teaching job

Separate money collected from economic value available to recover acquisition and fixed structure.

### Misuse

Calling CM "profit" before fixed/period costs and other commitments.

---

## F-03 — Contribution margin percentage

**Class:** OPERATIONAL METRIC

`CM% = CM / net revenue`

### Teaching job

Compare economic structure across offers, products or segments.

### Misuse

Comparing percentages without absolute contribution or capacity requirements.

---

## F-04 — Conversion rate

**Class:** OPERATIONAL METRIC

`Conversion rate = successful transitions / eligible starting opportunities`

### Critical rule

Define the denominator.

Examples:

- visitor → lead;
- lead → qualified opportunity;
- qualified opportunity → customer;
- proposal → customer.

### Misuse

Comparing conversion rates built from different denominators or different lead quality.

---

## F-05 — Fully loaded CAC

**Class:** OPERATIONAL METRIC with attribution choices

`CAC = attributable acquisition + sales costs / new customers acquired`

Potential numerator components:

- media;
- creative/production;
- agency/team labor;
- sales labor/commissions;
- tools directly attributable;
- events/materials;
- follow-up costs.

### Teaching job

Show why cost per lead or ad spend alone is not customer acquisition cost.

### Misuse

Leaving expensive human selling outside the numerator while comparing channels with different sales burden.

---

## F-06 — Cost-to-serve

**Class:** OPERATIONAL METRIC

`Cost-to-serve = attributable post-sale delivery/support cost for a customer/cohort over a defined period`

### Teaching job

Expose hidden customer-quality differences.

### Misuse

Assuming customers with equal revenue are equally valuable.

---

## F-07 — First-transaction CAC recovery gap

**Class:** DERIVED METRIC

`CAC recovery gap = CAC - first-transaction contribution margin`

If result <= 0, the first transaction has recovered CAC at contribution level.

### Teaching job

Make front-end/backend economics visible.

### Misuse

Treating a positive gap as automatically bad when later contribution is credible and cash/risk are manageable.

---

# 3. Payback and lifetime economics

## F-08 — Simple payback period

**Class:** OPERATIONAL MODEL

For approximately regular contribution:

`Payback periods = CAC / contribution margin per period attributable to the customer`

### Teaching job

Show the time dimension of acquisition economics.

### Misuse

Using the simple formula when contribution is irregular, delayed or heavily front-loaded without acknowledging timing.

For irregular flows use cumulative cohort contribution over time instead.

---

## F-09 — Observed cohort payback

**Class:** OPERATIONAL METRIC

Find the first period where:

`cumulative observed contribution >= CAC`

### Teaching job

Prefer actual cohort behavior when available.

### Misuse

Replacing observed data with an optimistic average customer model.

---

## F-10 — Lifetime contribution value

**Class:** ESTIMATE/MODEL unless fully observed

General form:

`LTV_CM = expected total contribution margin over the relationship - incremental retention/service costs not already included`

For a fully observed closed cohort, use observed cumulative contribution.

### Teaching job

Keep LTV tied to margin rather than top-line revenue.

### Misuse

- lifetime revenue labeled as LTV economic value;
- infinite/overlong horizon;
- future retention assumed without evidence;
- ignoring cost-to-serve;
- using LTV to excuse unacceptable cash timing.

---

## F-11 — LTV:CAC ratio

**Class:** DIAGNOSTIC RATIO, not universal decision law

`LTV_CM / CAC`

### Teaching job

Provide a compact relationship between expected contribution and acquisition cost.

### Critical caveat

The same ratio can hide radically different payback timing, uncertainty and capital needs.

### Rule

Never teach a universal "good" ratio as doctrine.

---

# 4. Pricing and offer economics

## F-12 — Scenario contribution

**Class:** IDENTITY within assumptions

`Expected contribution per opportunity = conversion rate × contribution margin per customer`

For channel/offer comparison, extend when necessary to include acquisition/sales cost.

### Teaching job

Show why lower conversion can still produce superior economics at a higher price.

### Misuse

Optimizing conversion rate without contribution or customer quality.

---

## F-13 — Expected contribution after acquisition cost

**Class:** MODEL

`Expected net contribution per acquired customer over chosen horizon = expected contribution over horizon - CAC`

### Teaching job

Compare pricing/offers on an economically common basis.

### Misuse

Hiding uncertainty in the horizon or future purchases.

---

## F-14 — Allowable CAC / acquisition ceiling

**Class:** DECISION RULE

One general form:

`Allowable CAC = expected contribution over chosen horizon - required contribution to structure/profit - risk/cash buffer`

### Teaching job

Turn customer economics into a bidding/acquisition constraint.

### Critical caveat

There is no universal allowable-CAC formula independent of business objectives, capital, risk and time horizon.

---

## F-15 — Marginal CAC

**Class:** OPERATIONAL METRIC

`Marginal CAC = incremental acquisition spend / incremental customers produced by that spend`

### Teaching job

Show why average historical CAC can hide deteriorating scale economics.

### Misuse

Using average CAC to justify the next block of spend.

---

# 5. Break-even and operating structure

## F-16 — Simple break-even quantity

**Class:** IDENTITY under single-product/simple-mix assumptions

`Break-even units = fixed costs / contribution margin per unit`

### Teaching job

Connect price/cost structure to required volume.

### Misuse

Applying a single contribution value to a changing multi-product/customer mix.

---

## F-17 — Break-even customers over period

**Class:** MODEL / IDENTITY depending on assumptions

`Break-even customers = period fixed costs / average contribution per customer over the same period`

### Critical rule

Ensure time periods and contribution definitions match.

---

## F-18 — Marketing return on contribution basis

**Class:** MODEL / attribution-sensitive

`Marketing return = (incremental contribution attributable to marketing - marketing cost) / marketing cost`

### Teaching job

Move ROI discussion closer to contribution rather than revenue.

### Misuse

Claiming incremental attribution without a defensible comparison/baseline.

---

# 6. Retention and recurring economics

## F-19 — Period retention rate

**Class:** OPERATIONAL METRIC

For subscription-like relationships:

`Retention rate = customers retained at period end / customers eligible to remain from period start`

Define additions/reactivations separately.

### Misuse

Using subscription retention logic for categories with naturally irregular purchase cycles.

---

## F-20 — Churn rate

**Class:** OPERATIONAL METRIC

Simple customer churn:

`Churn rate = customers lost during period / customers at risk of loss at period start`

### Critical caveat

Definitions vary. Revenue churn and customer churn are different metrics.

### Teaching job

Teach denominator discipline, not a single universal churn formula.

---

## F-21 — Repeat-purchase rate

**Class:** OPERATIONAL METRIC

One possible cohort form:

`Repeat purchase rate = customers making another purchase within defined window / customers eligible to repurchase`

### Teaching job

Handle non-subscription relationships more honestly than forcing churn terminology.

---

# 7. Cash and working capital

## F-22 — Net cash burn

**Class:** OPERATIONAL METRIC

When outflows exceed inflows:

`Net burn per period = cash outflows - cash inflows`

### Misuse

Confusing accounting loss with cash burn.

---

## F-23 — Simple runway

**Class:** ESTIMATE/MODEL

`Runway periods = available cash / expected net burn per period`

### Critical caveat

Assumes burn remains approximately stable; growth, seasonality and one-off payments can invalidate the estimate.

---

## F-24 — Cash Conversion Cycle

**Class:** OPERATIONAL METRIC for inventory/receivables/payables businesses

`CCC = DIO + DSO - DPO`

Where:

- DIO = days inventory outstanding;
- DSO = days sales outstanding;
- DPO = days payables outstanding.

### Teaching job

Show how growth can consume cash before profit is realized.

### Misuse

Applying the metric mechanically to business models where inventory/receivables structure is not relevant.

---

# 8. Capacity economics

## F-25 — Practical capacity utilization

**Class:** OPERATIONAL METRIC

`Utilization = capacity actually used / practical available capacity`

### Critical rule

Use practical capacity, not theoretical maximum, when maintenance, setup, variability and normal downtime matter.

### Misuse

Treating 100% utilization as inherently optimal in a variable service system.

---

## F-26 — Throughput rate

**Class:** OPERATIONAL METRIC

`Throughput = completed units/jobs/customers / time period`

### Teaching job

Separate work started from work completed.

### Misuse

Increasing throughput locally while creating downstream queue/rework.

---

## F-27 — Contribution per constrained unit

**Class:** DECISION METRIC

`Contribution per constrained unit = contribution margin / units of scarce capacity consumed`

Possible constrained unit:

- technician hour;
- machine hour;
- consultation slot;
- warehouse position;
- delivery route capacity.

### Teaching job

Compare customers/products when capacity is the bottleneck.

### Misuse

Using this metric when the named capacity is not actually constraining the system.

---

## F-28 — Opportunity cost of scarce capacity

**Class:** DECISION MODEL

`Opportunity cost ≈ contribution of the best feasible alternative displaced by the current use of scarce capacity`

### Teaching job

Explain why a positive-margin job can still be economically weak during a bottleneck.

### Caveat

This is a management estimate, not a directly observed accounting cost.

---

# 9. Growth decomposition

## F-29 — Customer-value-frequency decomposition

**Class:** MODEL / explanatory identity at defined period

`Revenue ≈ number of customers × average transaction value × average purchase frequency`

### Teaching job

Locate growth levers.

### Misuse

Treating the three levers as independent when changes in price, frequency or customer mix affect conversion, service cost or retention.

---

## F-30 — Cohort contribution curve

**Class:** OBSERVED/MODELED SERIES

For each cohort and time period, track cumulative contribution net of acquisition cost.

### Teaching job

Integrate CAC, retention, repeat purchase, cost-to-serve and payback in one view.

### Rule

Observed and forecast portions must be visually distinguished.

---

# 10. Canonical teaching datasets — provisional

These are synthetic and illustrative. They exist to create continuity across worked examples. They may be revised during golden-chapter production if doctrine/learning needs require it.

## Dataset A — LineaCasa

Working values for capacity/sales examples:

- average contract revenue: €18,000;
- direct variable delivery cost: €11,000;
- contribution before acquisition/structure: €7,000;
- fully loaded CAC for qualified won project: €2,100;
- average site-supervisor requirement: 32 hours/project;
- practical supervisor capacity: 160 hours/month;
- deposit: 30% at contract signing;
- balance timing staged through project.

Teaching uses:

- customer quality;
- quote/sales economics;
- contribution per constrained supervisor hour;
- cash timing;
- expansion capacity.

## Dataset B — Officina Dati

Working values:

- project price: €6,000;
- delivery labor/variable cost: €2,400;
- first-project contribution: €3,600;
- fully loaded CAC: €1,800;
- optional recurring monitoring price: €900/month;
- recurring variable service cost: €300/month;
- recurring contribution: €600/month;
- not every project customer converts to recurring service.

Teaching uses:

- project vs recurring model;
- CAC recovery;
- payback;
- offer architecture;
- automation investment.

## Dataset C — Dispensa Nord

Working values:

- average online order: €68;
- product/pack/fulfillment/payment variable cost: €36;
- contribution/order before CAC: €32;
- blended new-customer CAC: €24;
- repeat interval varies strongly by cohort;
- wholesale orders have different margins/payment timing;
- inventory must be funded before some sales occur.

Teaching uses:

- pricing/promotion;
- repeat-purchase economics;
- CAC/payback;
- inventory/working capital;
- channel mix.

## Dataset D — TurnoChiaro

Working values:

- monthly subscription revenue/account: €480;
- recurring variable service/support cost: €120;
- monthly contribution/account: €360;
- fully loaded CAC: €1,800;
- simple steady-state payback at full contribution: 5 months;
- activation and retention differ by account type;
- high-implementation accounts consume more onboarding/support capacity.

Teaching uses:

- activation/retention;
- cohort payback;
- cost-to-serve;
- self-service vs assisted onboarding;
- scale decision.

---

# 11. Sensitivity teaching

For major quantitative chapters, do not stop at the base calculation.

Change one material assumption at a time.

Examples:

- conversion drops when price rises;
- repeat rate is lower than forecast;
- CAC rises at higher spend;
- onboarding cost doubles for a segment;
- payment terms move from advance to 60 days;
- capacity utilization crosses a queue threshold.

Then ask:

> Which variable changes the decision, not merely the result?

This teaches threshold thinking rather than spreadsheet worship.

---

# 12. Numerical provenance and labeling

Every numerical example must be labeled in backend and, when needed, reader-facing as one of:

- observed real data;
- documented external data;
- synthetic teaching data;
- forecast/assumption;
- illustrative simplification.

Do not allow synthetic numbers to migrate into prose as empirical benchmarks.

---

# 13. Common quantitative AI-smells to avoid

## Round-number theater

Using clean numbers only because they make arithmetic easy, then drawing strong conclusions.

## Formula without decision

Showing an equation without explaining what decision it changes.

## Ratio worship

Presenting an industry ratio as universally good/bad without context.

## False precision

Showing decimals or detailed forecasts beyond the evidence quality.

## Denominator drift

Comparing metrics whose populations or time windows differ.

## Future-value optimism

Using estimated LTV to justify current CAC/cash risk without evidence.

## Average masking

Using average CAC/margin/retention when cohorts/segments behave differently.

---

# 14. Pseudocommands

## `FORMULA-JOB`

What business decision becomes better because this formula exists?

## `DENOMINATOR-CHECK`

Are numerator, denominator, population and period defined?

## `OBSERVED-VS-MODELED`

Which values are facts and which are assumptions?

## `SENSITIVITY-CHECK`

Which assumption could flip the decision?

## `CASH-TIMING`

Does the formula hide when money actually moves?

## `AVERAGE-MASKING`

Should this be segmented/cohorted?

## `CAPACITY-CHECK`

Does economic value consume scarce operating capacity differently across options?

## `INTERPRETATION-CHECK`

Can the reader explain the result in business language without repeating the formula?

---

# 15. Golden-chapter quantitative test

The quantitative golden chapter must demonstrate at least:

- one metric derived from a real decision problem;
- one complete worked calculation;
- one visual representation of the same economics;
- one sensitivity change that materially affects interpretation;
- one misuse/counterexample;
- one transfer exercise using a different recurring case.

---

# 16. Acceptance rule

The formula system succeeds when a beginner can reproduce the arithmetic, explain what the result means, state the main assumption/limit and use the metric to make a better decision.

If the reader can calculate but not decide, the teaching has failed.