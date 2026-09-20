# AI Smell Catalog — Manual V2

## Purpose

This document identifies recurring rhetorical and structural patterns in Manual V1 that make the text feel machine-generated, reference-like or mechanically assembled even when the underlying doctrine is correct.

It is not a detector and does not claim that any single feature proves AI authorship.

The purpose is editorial:

**identify repeated patterns that reduce authorial credibility, narrative continuity and learning quality, then prevent them from becoming the default grammar of V2.**

V1 remains frozen. These findings govern V2 only.

---

# Evidence base

Source inspected:

- V1 final PDF — 313 pages;
- V1 final chapter structure — 39 chapters;
- extracted text used for quantitative checks;
- representative visual inspection of beginning, middle and late pages;
- direct comparison against the V1 curriculum and chapter architecture.

Key signals already established in the V2 postmortem:

- approximately 46,948 extracted words;
- 39.1% of non-empty lines are list items;
- median paragraph length approximately 9 words in source-oriented analysis;
- approximately 66.7% of paragraphs are <=12 words;
- zero embedded explanatory images in the final PDF.

Additional direct checks on the extracted V1 PDF text:

- 590 separate bullet-list runs;
- median bullet run = 5 items;
- 336 bullet runs contain at least 5 items;
- 198 sentences begin with `Non...`;
- median length of those `Non...` sentences = 6 words;
- recurrent sentence openings include `La domanda è`, `La regola è`, `Il principio è`, `Questo non significa`, `La sequenza è` and structurally similar variants;
- the shortest chapter is materially under 1,000 words, while a few chapters are several times longer, showing that V1 chapter boundaries were not consistently learning-sized units.

These numbers are diagnostic signals, not future quotas.

---

# Research note

Recent NLP research is relevant to the editorial diagnosis, but must not be overinterpreted.

Two findings are particularly useful:

1. model-generated prose tends to show more repeated syntactic templates than human-reference prose;
2. human-written discourse tends to exhibit greater structural variability across contexts and genres.

This supports an editorial focus on structural/rhetorical diversity rather than merely replacing a few stereotyped words.

Backend references:

- Shaib, Elazar, Li & Wallace, **Detection and Measurement of Syntactic Templates in Generated Text**, EMNLP 2024.
- Kim et al., **Threads of Subtlety: Detecting Machine-Generated Texts Through Discourse Motifs**, ACL 2024.
- Terčon & Dobrovoljc, **Linguistic Characteristics of AI-Generated Text: A Survey**, 2025 preprint.

The rule remains: we do not write to fool AI detectors. We write to produce a better book.

---

# Smell taxonomy

## AS-01 — Bullet-as-prose

### Symptom

An explanation that should unfold causally is converted into a vertical inventory.

Typical V1 pattern:

- statement;
- list of 5–8 items;
- short conclusion;
- another list.

### Why it fails

Lists compress information efficiently but suppress relations between ideas. The reader sees components without being shown why one leads to another, when the relation matters, or which item deserves more weight.

At V1 density, the bullet becomes the default sentence architecture.

### V2 rule

Use a list only when the reader benefits from seeing items as a set:

- checklist;
- mutually comparable alternatives;
- procedural steps;
- compact reference material;
- variables in a model.

If the value lies in causality, contrast, judgment or interpretation, write prose first.

---

## AS-02 — Telegraphic paragraph rhythm

### Symptom

Many paragraphs contain one very short sentence, often immediately followed by another one-sentence paragraph.

Example shape:

> X is not Y.
>
> It is Z.
>
> This matters.
>
> Therefore...

### Why it fails

Occasional short paragraphs create emphasis. Repeated continuously, they create the rhythm of chat output, keynote slides or social copy rather than sustained explanatory prose.

They also make every statement look equally important.

### V2 rule

Default paragraphs should develop one thought through several connected sentences. A one-sentence paragraph must earn its isolation through genuine rhetorical or conceptual weight.

---

## AS-03 — Mechanical negation contrast

### Symptom

Frequent use of structures such as:

- `X non è Y. È Z.`
- `Non significa... Significa...`
- `Il punto non è... Il punto è...`
- repeated sentences beginning with `Non...`.

### Evidence

The extracted V1 text contains 198 sentences beginning with `Non...`, with a median length of 6 words.

### Why it fails

Contrast is useful for correcting misconceptions. When it becomes the main explanatory device, the prose sounds adversarial, formulaic and over-signposted. It defines concepts by perpetual correction rather than by building them positively.

### V2 rule

Use explicit `not X but Y` contrast when a real misconception must be removed. Otherwise explain the positive model directly and integrate qualifications naturally in the paragraph.

---

## AS-04 — Metadiscursive template repetition

### Symptom

Repeated scaffolds such as:

- `La domanda è...`
- `La regola è...`
- `Il principio è...`
- `La sequenza è...`
- `La logica è...`
- `Questo non significa...`.

### Why it fails

The phrases are not inherently wrong. Their recurrence exposes the generating template. The reader starts predicting the syntax instead of following the argument.

### V2 rule

Do not ban these constructions. Break their monopoly. Let the argument itself signal importance through context, causality, examples and paragraph architecture.

---

## AS-05 — Heading inflation

### Symptom

A heading appears for nearly every conceptual turn, sometimes after only a few paragraphs.

### Why it fails

Headings become substitutes for transitions. The page reads like a hierarchical knowledge base or documentation site rather than a chapter with an argument.

Too many headings also weaken hierarchy: when everything has a label, nothing feels structurally important.

### V2 rule

A heading marks a meaningful phase of the chapter argument, not every note-sized concept. Minor distinctions can live inside prose, figures, examples or sidebars.

---

## AS-06 — List–summary–list choreography

### Symptom

Repeated local structure:

1. definition;
2. list;
3. short interpretive line;
4. another list;
5. a punchline.

### Why it fails

Even when every local section is clear, dozens of identical micro-structures create global monotony.

### V2 rule

Vary explanatory mode according to the learning job: scene, worked example, causal explanation, comparison, diagram, derivation, counterexample, narrative case, procedure, reflection.

---

## AS-07 — Synthetic punchline

### Symptom

A short, bold or isolated sentence is used to manufacture importance after nearly every section.

Typical shape:

> More volume does not necessarily mean a better business.

### Why it fails

A punchline works when it crystallizes a developed argument. Repeated constantly, it becomes a verbal tic and creates the feeling of generated business-content prose.

### V2 rule

Reserve aphoristic compression for principles worth remembering after the explanation, not as a mandatory ending device.

---

## AS-08 — Generic hypothetical business

### Symptom

`Immagina una piccola impresa...`, `Supponiamo che...`, followed by clean round numbers or a generic service business with no operational texture.

### Why it fails

The example demonstrates the sentence but not the world. It rarely contains competing objectives, imperfect data, timing, incentives or constraints — the things that make actual business reasoning difficult.

### V2 rule

Examples need context proportional to their teaching role. Micro-examples may stay simple; worked examples and cases must include enough reality to force a decision.

---

## AS-09 — Definition cascade

### Symptom

Several terms are defined one after another before the reader has a reason to care about them.

### Why it fails

The manual becomes vocabulary acquisition rather than problem solving. Definitions are remembered poorly when they are detached from a live question.

### V2 rule

Introduce terminology at the point where a problem requires it. Prefer: situation → need for distinction → term → example → application.

---

## AS-10 — Authorless certainty

### Symptom

The text states many correct propositions but rarely exposes the reasoning process that made the author prefer one interpretation over another.

### Why it fails

The reader receives conclusions without experiencing an expert mind at work. This contributes to the feeling that the prose is a compiled knowledge layer.

### V2 rule

The V2 voice must show judgment:

- what evidence matters and what does not;
- why two superficially similar cases differ;
- where the model breaks;
- what the author would inspect next;
- what would change the conclusion.

Authorial presence is reasoning presence, not autobiography.

---

## AS-11 — Excessive symmetry

### Symptom

Concepts repeatedly appear in balanced pairs, triplets and neat taxonomies even when reality is messier.

### Why it fails

Symmetry is memorable, but too much symmetry creates an impression of synthetic completeness. It can also hide asymmetric importance between variables.

### V2 rule

Use taxonomy only when it clarifies a real structure. Allow uneven explanations when the subject is uneven.

---

## AS-12 — Caveat chain

### Symptom

A principle is followed by multiple micro-paragraphs clarifying what it does not mean.

### Why it fails

This creates defensive prose. The reader receives the rule, then watches it immediately dissolve into qualifications.

### V2 rule

Separate three cases:

- core rule;
- material boundary condition;
- rare exception.

Integrate normal nuance into the explanation; place edge cases in a dedicated paragraph or box only when they matter to application.

---

## AS-13 — Premature abstraction

### Symptom

The text names a model before the reader has seen a concrete situation that makes the model useful.

### Why it fails

The reader must carry abstract variables in working memory without a schema.

### V2 rule

For novice-facing sections, prefer concrete → model → second example → abstraction, especially for difficult causal/economic concepts.

---

## AS-14 — Repeated chapter closure

### Symptom

Chapters tend to end with a principle, checklist, short concluding line or transition in similar rhythm.

### Why it fails

The book begins to feel assembled from the same chapter-generation prompt.

### V2 rule

Closers should match the chapter job. Possible endings include:

- unresolved decision leading into the next chapter;
- transfer exercise;
- synthesis diagram;
- worked result;
- short principle;
- case consequence;
- diagnostic checkpoint.

Do not force all of them into every chapter.

---

## AS-15 — False conversationality

### Symptom

Frequent direct questions create the appearance of conversation without genuine dialogue or narrative development.

### Why it fails

The reader is constantly asked questions whose answers the text immediately supplies. The device loses force and resembles assistant-style prompting.

### V2 rule

Use direct questions when they genuinely focus inquiry, create tension or function as a diagnostic tool. Otherwise state the issue in normal prose.

---

## AS-16 — Markdown as invisible composition model

### Symptom

Even after professional PDF rendering, the underlying text still behaves like Markdown documentation:

- heading;
- short paragraph;
- list;
- bold principle;
- heading;
- list.

### Why it fails

Typography cannot transform documentation architecture into book architecture.

### V2 rule

Compose chapters as chapters first. Markdown may remain the storage format, but it must not dictate the rhetorical form.

---

# Red-team tests for V2 prose

Use these pseudocommands during drafting and editing.

## `AI-SMELL`

Ask:

- could the next paragraph have been generated by the same rhetorical template as the previous three?;
- are sentence openings or contrasts repeating?;
- is a bullet list doing work prose should do?;
- is a short sentence isolated only to sound emphatic?;
- are headings replacing transitions?

## `HUMAN-RHYTHM`

Read the passage aloud and inspect:

- sentence-length variation;
- paragraph-length variation;
- transition quality;
- whether emphasis feels earned;
- whether the argument breathes naturally.

## `AUTHOR-MIND`

Ask whether the passage reveals:

- what the author notices;
- what the author discounts;
- why the author chooses one interpretation;
- what evidence would change the conclusion.

If it only delivers propositions, authorial presence is too weak.

## `LIST-CHALLENGE`

For every list longer than three items:

> Would the reader learn more if this were explained as a causal paragraph, comparison, table, figure or worked example?

Keep the list only if the answer is no.

## `TEMPLATE-DIVERSITY`

Compare adjacent sections. If they share the same opening, explanatory sequence and closing pattern, deliberately change the rhetorical mode unless the repetition itself has pedagogical value.

---

# Non-goals

The V2 process must not overcorrect by:

- banning all lists;
- banning all short sentences;
- banning rhetorical questions;
- adding decorative narrative everywhere;
- making every paragraph long;
- replacing clarity with literary flourish;
- deliberately inserting errors or eccentricities to appear human;
- writing to defeat AI-detection software.

The goal is not randomness.

The goal is **controlled rhetorical variety in service of understanding**.

---

# Phase implication

The central editorial diagnosis is:

**V1 often explains correct concepts through a small set of repeated presentation templates. V2 must preserve conceptual discipline while greatly increasing rhetorical, narrative and pedagogical range.**

This catalog is a warning system. The positive writing model lives in `AUTHORIAL_STYLE_BIBLE.md`.