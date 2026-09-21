# Pedagogical Apparatus — Manual V2

Status: **CURRENT — founder-directed refinement after prose-depth pass**  
Date: 2026-09-21

## Purpose

This document defines the secondary teaching apparatus of Manual V2.

The architecture and prose remain primary. The manual must still read naturally if every optional callout is hidden.

The apparatus exists to create a useful **second reading speed**:

- the first reading follows the continuous explanation;
- later consultation lets the reader quickly recover an example, a common mistake, an operational implication or a self-check.

The apparatus must never turn the book into courseware, a slide deck or a sequence of colored boxes.

---

# 1. Governing rule

Every feature must answer one question:

> **What does this element teach or make retrievable better than the surrounding prose?**

If the answer is weak, keep the material in ordinary prose or remove it.

The desired page hierarchy is:

1. **core narrative** — theory, causality, explanation and judgment;
2. **figures / formulas / tables** — when another representation genuinely explains a relationship better;
3. **pedagogical apparatus** — selective support for application, error prevention and later retrieval.

The apparatus is third, not first.

---

# 2. The five primary feature types

Manual V2 uses five stable reader-facing labels.

## 2.1 ESEMPIO SVOLTO / ESEMPIO NUMERICO

### Job

Show the complete application of a concept after the theory is already understandable.

### Use when

The reader benefits from seeing:

- assumptions;
- data;
- calculation or reasoning;
- result;
- interpretation;
- limitation or sensitivity when material.

### Rule

The example demonstrates the model. It does not carry the burden of defining the model.

For short examples, ordinary prose is preferable to a box.

---

## 2.2 ERRORE FREQUENTE

### Job

Protect the reader from a plausible mistake that can materially damage a decision.

### Required structure

A useful error box normally explains:

1. what people commonly do or infer;
2. why it appears reasonable;
3. why it fails;
4. what to do instead.

### Use only when

The error is common, costly or conceptually revealing.

Do not use this label for trivial reminders.

---

## 2.3 IN PRATICA

### Job

Translate a completed conceptual explanation into a concrete operating consequence.

### Typical contents

- what the manager should inspect;
- what changes in a decision;
- what information to request from a team/vendor;
- what not to optimize in isolation;
- what a principle means in an ordinary business situation.

### Rule

`IN PRATICA` is not a summary box. It must change what the reader would actually do.

Use sparingly. Often the practical implication belongs naturally in the prose and needs no visual separation.

---

## 2.4 VERIFICA NELLA TUA AZIENDA

### Job

Turn the chapter from knowledge into inspection of the reader's real business.

### Preferred form

A compact diagnostic exercise, normally 3–6 prompts, such as:

- identify a number;
- find a missing denominator;
- compare two segments;
- trace one customer path;
- locate one assumption;
- identify one decision that would change if the answer were different.

### Rule

Questions must lead to evidence or a decision. Avoid generic reflection prompts such as `Come ti senti rispetto a...` or questions whose answer cannot change anything.

Usually one strong self-check near the end of a chapter is better than many small interruptions.

---

## 2.5 APPROFONDIMENTO

### Job

Preserve an important nuance, boundary condition or specialist distinction without slowing the beginner's main path.

### Use when

The material is useful but not necessary to follow the core argument.

Examples:

- edge case;
- specialist terminology;
- methodological qualification;
- important historical/contextual note;
- a second-order consequence relevant mainly to experienced readers.

### Rule

The main chapter must remain complete if the box is skipped.

`APPROFONDIMENTO` should be uncommon.

---

# 3. Supporting feature: STRUMENTO OPERATIVO

`STRUMENTO OPERATIVO` is retained, but it is not a normal prose callout.

Use it only when the book provides an actual reusable artifact:

- worksheet;
- audit sheet;
- decision memo;
- calculation template;
- process map;
- interview guide;
- checklist with genuine decision value.

A list of advice is not automatically a tool.

Tools should later be reusable in the final Toolkit/Workbook without rewriting them from scratch.

---

# 4. Features deliberately removed from the default palette

The following are no longer default recurring labels:

- `PRINCIPIO`;
- `CASO` as a generic box label;
- `FERMATI E PREVEDI`;
- `SPIEGA PERCHÉ`;
- `DIAGNOSTICA`;
- `TRASFERISCI`;
- `COSA CAMBIA SE...` as a recurring visual label.

Their instructional jobs are still valid, but the labels created too much visible teaching machinery.

Instead:

- a principle should usually be expressed naturally in the prose;
- substantial real cases will have their own editorial treatment;
- prediction, transfer and sensitivity questions can appear inside an exercise or worked example without becoming permanent box families.

---

# 5. Integration with the prose-depth system

The apparatus must never compensate for weak explanation.

Before adding a box, run this sequence:

1. Is the underlying concept fully explained in the narrative?
2. Does the reader understand why it matters?
3. Are mechanism and consequence clear?
4. Would the feature add application/retrieval value rather than missing theory?

If question 1–3 fail, rewrite the prose first.

This is especially important after the third Golden rewrite: the book's new quality comes from deeper continuous explanation. The apparatus must preserve that gain.

---

# 6. Placement rules

## Do not interrupt orientation

The first pages of a chapter should normally establish the subject before any optional callout.

A formula or essential figure may appear early if it is part of the explanation. A support box normally should not.

## Place the feature after comprehension

A worked example follows the theory it demonstrates.

An `ERRORE FREQUENTE` follows enough explanation for the reader to understand why the error is tempting.

An `IN PRATICA` follows a conclusion that has operational consequences.

A `VERIFICA NELLA TUA AZIENDA` normally appears after the relevant model is complete, often late in the chapter.

## Avoid callout collisions

Do not place two optional support boxes back-to-back.

Do not create pages where the reader spends more time entering/exiting callouts than following the main argument.

A figure/table/formula plus a support box can coexist only when both are necessary and the page remains readable.

---

# 7. Density rule

There is no quota, minimum or target count.

As a warning heuristic rather than a production target:

- a conceptual chapter may need only 1–3 support features;
- a quantitative chapter can contain more worked examples because calculation is intrinsic to the subject;
- some chapters may need no `APPROFONDIMENTO` or `ERRORE FREQUENTE` at all;
- `VERIFICA NELLA TUA AZIENDA` should usually be one coherent activity rather than several fragmented prompts.

If the page starts to resemble a training workbook, feature density is too high for the main manual.

---

# 8. Practicality inside ordinary prose

Not every practical passage deserves a box.

The preferred pattern remains to integrate many operational consequences into normal paragraphs:

> Se un'agenzia riporta soltanto costo per lead e numero di contatti, chiedere anche costo completo di acquisizione e qualità economica dei clienti non è un esercizio finanziario: serve a evitare di premiare un canale che trasferisce costi alla vendita o all'erogazione.

This is practical and concrete without visual interruption.

Reserve `IN PRATICA` for an implication that benefits from later retrieval.

---

# 9. Error boxes must expose the mechanism

Weak:

> **ERRORE FREQUENTE**  
> Guardare solo il fatturato.

Strong:

> **ERRORE FREQUENTE — Scambiare crescita del fatturato per miglioramento economico**  
> Il fatturato può crescere mentre contribuzione e cassa peggiorano se i nuovi clienti richiedono più sconti, assistenza, rilavorazioni o capitale. Il controllo corretto non è eliminare il fatturato dai KPI, ma seguirlo abbastanza a valle da capire che cosa rimane e con quale fabbisogno operativo.

The feature must teach the causal correction.

---

# 10. Self-checks must produce evidence

A `VERIFICA NELLA TUA AZIENDA` should leave the reader with something concrete.

Good output examples:

- a list of the three customer segments with highest/lowest contribution;
- a reconstructed CAC numerator;
- the first bottleneck after an acquisition increase;
- a comparison between one local KPI and the downstream business result;
- an explicit assumption that currently supports an LTV model;
- one metric missing from a dashboard.

Bad output:

- `Rifletti sul tuo marketing`;
- `Pensi di conoscere bene i clienti?`;
- `Quanto è importante per te il posizionamento?`

The manual should produce better observation, not introspection for its own sake.

---

# 11. Relationship with chapter endings

Not every chapter needs a formal end-of-chapter exercise section.

Preferred options:

- one `VERIFICA NELLA TUA AZIENDA`;
- a compact operational tool;
- a short set of transfer questions;
- ordinary synthesis prose if the chapter is already highly applied.

Part-level exercises can integrate multiple chapters later.

The main manual should not look like a school textbook with obligatory questions after every chapter.

---

# 12. Relationship with real cases

Real cases are not part of this support-box taxonomy.

When real cases are introduced in the next editorial phase, they may use a separate treatment (`CASO REALE`) because they serve an evidentiary and integrative role different from a micro-example.

Synthetic examples remain generic/A-B and should never be visually styled to imply that they are documented companies.

---

# 13. Relationship with figures and formulas

A chart, table, formula or diagram is not a pedagogical callout merely because it is visually distinct.

- chart = quantitative pattern;
- table = structured comparison;
- formula = numerical relationship;
- diagram = structural/causal relationship;
- apparatus = application, error prevention, deeper optional nuance or self-diagnosis.

Do not duplicate the same message in a figure and an `IN PRATICA` box unless each does a different job.

---

# 14. Guidance across the book

Support changes with reader competence.

## Early Parts

Prefer:

- clearer interpretation;
- more worked examples;
- simple `VERIFICA NELLA TUA AZIENDA` activities;
- explicit explanation of why an error fails.

## Middle Parts

Increase:

- comparison between alternatives;
- partial examples;
- transfer across contexts;
- decision tools.

## Late Parts

Prefer:

- integrated diagnostic tools;
- multi-variable applications;
- decision memos;
- fewer elementary reminders.

The visual style stays coherent even as the cognitive support fades.

---

# 15. Production checks

## `APPARATUS-JOB`

State in one sentence why the feature teaches better than ordinary prose.

## `APPARATUS-DELETE`

Remove the feature temporarily. If comprehension, application or retrieval does not materially worsen, leave it out.

## `SECOND-READING`

Would the feature help a reader returning months later to solve a problem?

## `NO-COURSEWARE`

Does the page still look and read like a professional manual rather than a workbook or e-learning module?

## `EVIDENCE-OUTPUT`

Does a self-check produce an observation, number, comparison or decision input?

## `PROSE-FIRST`

Is the concept complete without opening the optional feature?

---

# 16. Acceptance rule

The pedagogical apparatus passes when:

- the core prose remains dominant;
- feature labels are few and predictable;
- each feature has a distinct learning job;
- examples remain subordinate to theory;
- practical application appears both in prose and selectively in callouts;
- self-checks produce evidence rather than generic reflection;
- the reader can use the apparatus for later consultation;
- pages remain calm and book-like rather than visually fragmented.
