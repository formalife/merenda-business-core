# Manual V2 — Architecture Postmortem 1

Date: 2026-09-21  
Status: **COMPLETE — input to full-manual reevaluation**

## Why this postmortem exists

After Chapters 1–5 were written and read in sequence, the architecture could finally be judged as a book rather than as a table of topics.

The prior 8-Part / 34-Chapter design was strong enough to support production, but production exposed a distinction that the earlier architecture audit had not tested hard enough:

**a good thematic map is not automatically a good reading sequence.**

This postmortem identifies what the first production wave revealed and what was corrected before the definitive architecture audit.

---

# 1. What worked

## 1.1 The macro causal progression is sound

The overall movement remains strong:

**system/economics/method → market/customer → positioning/offer/price → trust/demand/acquisition → communication/sales → experience/relationship/reputation → economics/organization → development/direction.**

This is compatible with the current Layer 1 causal sequence while remaining readable as a textbook.

No evidence emerged that the book needs a new macro architecture or a different number of Parts.

## 1.2 The first three chapters form a strong foundation

Chapter 1 teaches what kind of system is being studied.

Chapter 2 gives the minimum economic vocabulary required to judge that system.

Chapter 3 teaches how to turn observed problems into hypotheses, tests and decisions.

The sequence is pedagogically stronger than beginning immediately with market or tactics because later chapters can assume a common causal/economic language.

## 1.3 Market before customer remains correct

Chapter 4 asks whether there is a commercially practicable field in which to compete.

Chapter 5 asks which customers inside that field are worth acquiring and serving.

This preserves the distinction between market viability and customer desirability.

## 1.4 Advanced economics remains correctly delayed

Chapter 2 introduces only minimum literacy.

Chapters 25–27 deepen customer economics, cash and capacity only after the reader understands the commercial lifecycle that creates those numbers.

Moving advanced economics earlier would increase technical density before the reader understands what is being measured.

## 1.5 Brand/reputation remains correctly downstream

Positioning is taught early as a reason to choose.

Brand and reputation are taught later as accumulated market memory produced by promises, experiences, proof, referral and public behavior.

This separation should be preserved.

---

# 2. What the previous architecture got wrong or left ambiguous

## 2.1 Chapter 3 and Chapter 34 sounded more redundant than they are

`Diagnosi e test` and `Diagnosi strategica` describe different levels of competence but appeared to duplicate each other in the TOC.

Correction:

- Chapter 3 → `Metodo decisionale`;
- Chapter 34 remains `Diagnosi strategica`.

The first now clearly owns the general evidence/test method; the last owns whole-system strategic integration.

## 2.2 The Part II sequence lacked an explicit epistemic bridge

The order `Mercato → Cliente → Ricerca → Decisione d'acquisto` is pedagogically defensible, but the previous wording allowed a dangerous reading: Chapters 4–5 might appear to authorize conclusions before the reader has learned how to produce evidence.

Correction:

- Chapters 4–5 are now explicitly framed as **evaluation lenses and hypotheses**;
- Chapter 6 teaches how to test them;
- Chapter 7 turns evidence into an anatomy of the buying decision.

This preserves conceptual orientation before methodology without legitimizing intuition as fact.

## 2.3 Market-level and customer-level spending were too similarly named

Old:

- 4.3 `Capacità e disponibilità di spesa`;
- 5.3 `Capacità di spesa e disponibilità a pagare`.

The distinction existed in prose but not in navigation.

Correction:

- 4.3 → `Sostenibilità economica della domanda`;
- 5.3 remains customer-level capacity/willingness.

## 2.4 Market competition and buyer alternatives were too similarly framed

Old:

- 4.5 `Alternative e dinamica del mercato`;
- 7.2 `Alternative e status quo`.

Correction:

- 4.5 → `Struttura competitiva e dinamica del mercato`;
- 7.2 remains the buyer's concrete alternatives/status quo.

## 2.5 Part IV taught orchestration before all access routes

Old order:

**demand → channels → funnel/database → partnership/distribution.**

This is thematically plausible but operationally backwards. Partnership/distribution is another way to gain access to demand; funnel/database is what happens after demand enters through one or more routes.

Correction:

**demand → channels → partnership/distribution → funnel/database → sales handoff.**

This produces a cleaner access → orchestration transition.

## 2.6 Several Part titles described contents less precisely than their causal job

Corrections:

- Part IV → `Fiducia, domanda e acquisizione`;
- Part VI → `Esperienza, relazione e reputazione`;
- Part VIII → `Sviluppo e direzione dell'impresa`.

The new names expose the actual learning movement rather than only listing selected topics.

## 2.7 Late-stage titles created a misleading literal chronology

`Avvio e prototipazione` at Chapter 31 could suggest that a book should be organized in the literal chronological order of a company's life.

That would be pedagogically wrong: the reader needs market, customer, economics, positioning, offer and acquisition knowledge before a useful prototype chapter can be understood.

Correction:

- Chapter 31 → `Prototipazione`;
- Chapter 32 → `Allocazione del capitale`.

They are now stage-neutral decision subjects inside a final development/direction block.

## 2.8 The architecture lacked explicit Part completion conditions

A reader could finish a Part and continue without knowing what should now be true.

Correction:

Every Part will end with a short unnumbered `Prima di proseguire` gate stating the outputs/decisions/evidence that should exist before the next Part.

This is not courseware and not a checklist quota. It is a causal transition device.

---

# 3. Root cause

The prior architecture optimization emphasized:

- semantic coverage;
- stable topical navigation;
- prerequisite order;
- reduction of V1 fragmentation.

Those goals were correct, but one additional criterion was underweighted:

**transition logic between adjacent chapters and Parts.**

A book can have the right topics, the right chapter sizes and the right overall direction while still creating small local reversals or ambiguous handoffs.

Production of Chapters 1–5 made those defects visible because the reader experience became concrete.

---

# 4. Corrective principle

The final architecture must satisfy five independent tests:

1. **Coverage** — every important concept has a home.
2. **Prerequisites** — no chapter requires important knowledge not yet taught.
3. **Causality** — upstream decisions generally precede downstream amplification.
4. **Navigation** — titles expose real conceptual boundaries.
5. **Transitions** — the output of one block is a plausible input to the next.

The previous architecture passed the first four substantially well. The current correction pass strengthens the fifth.

---

# 5. Decision after Postmortem 1

Do not change the 8-Part macro structure or 34-chapter scale merely for novelty.

Instead, subject the corrected candidate to a complete second-order audit of:

- every Part job;
- every adjacent chapter pair;
- every Part-to-Part transition;
- hidden prerequisites;
- repeated concepts with different jobs;
- topics that may be too early/late;
- whether literal business chronology is being confused with learning chronology.

Only after that reevaluation should the TOC be frozen.
