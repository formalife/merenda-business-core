# V2 Research Base — How the definitive manual should teach

Date: 2026-09-20

## Purpose

This document converts external research on textbook design, multimedia learning and novice instruction into editorial rules for Manual V2.

It does **not** determine doctrine. Canonical business doctrine remains in `merenda/`. It governs how that doctrine should be taught.

---

# 1. Textbooks are not ordinary books with headings

Textbook-authoring guides distinguish ordinary narrative content from explicit instructional structure. Common elements include chapter openers, learning objectives, case problems, pedagogical illustrations, worked examples, summaries, review questions, exercises, glossaries and cross-references.

Relevant sources:

- Oregon State University OER Faculty Guide — *Developing your textbook structure* and *Textbook elements*.
- UBC Open Text Publishing Guide — *Textbook Design Rules*.
- Queen's Open Textbook Authoring Guide — planning learning objectives and chapter structures.
- OpenStax — *Principles of Marketing* preface and reinforcement architecture.

### Implication for V2

A chapter must be designed as a **learning experience**, not as a container of concepts.

Openers, main explanation and closers must each have jobs.

Possible jobs include:

- orient;
- motivate;
- activate prior knowledge;
- explain;
- demonstrate;
- compare;
- practice;
- assess;
- transfer.

The exact components may vary by chapter, but instructional functions cannot be absent by default.

---

# 2. Learning objectives should drive content depth

Open-textbook authoring guides recommend planning chapters from desired learner outcomes rather than from topic inventory alone.

OpenStax explicitly maps chapter/section content to learning outcomes and reinforces concepts through knowledge checks, cases, summaries and applied exercises.

### Implication for V2

For every chapter define no more than a small set of meaningful outcomes in verbs such as:

- explain;
- diagnose;
- compare;
- calculate;
- design;
- evaluate;
- decide.

Avoid low-value outcomes like “know” or “understand” unless they are translated into observable ability.

Each chapter element should trace to an outcome.

---

# 3. Novices benefit from worked examples

Cognitive-load research on the worked-example effect shows that novice learners often learn more effectively and efficiently from step-by-step solved examples than from being asked to solve complex problems immediately.

Tamara van Gog, Fred Paas and John Sweller summarize a large body of research supporting worked examples for novices, while also noting that guidance should fade as expertise grows.

### Implication for V2

Important procedures and quantitative models should usually progress through:

1. fully worked example;
2. partially guided example;
3. independent application or case.

A worked example must expose intermediate decisions, not just show inputs and final answer.

For business problems, this means showing:

- facts available;
- assumptions;
- calculation or diagnostic path;
- competing interpretations;
- decision;
- what would change the decision.

---

# 4. Words + meaningful visuals can improve learning

The multimedia-learning literature reports that learners often perform better when appropriate words and relevant pictures are integrated than when words are used alone.

This is not an argument for decorative imagery. It is an argument for visual representation when the visual carries instructional structure.

### Implication for V2

Use visuals when they can represent:

- relationships;
- sequences;
- feedback loops;
- state transitions;
- comparison;
- magnitude;
- timing;
- constraints;
- causal paths.

Typical V2 visual forms:

- causal diagrams;
- process maps;
- decision trees;
- state machines;
- matrices;
- charts;
- timelines;
- annotated examples;
- formula diagrams;
- before/after system maps.

No image quota.

---

# 5. Coherence beats decoration

Richard Mayer and Logan Fiorella's multimedia-learning work emphasizes coherence: extraneous material can consume cognitive resources without helping the learner understand the essential structure.

### Implication for V2

Do not add:

- generic stock photography;
- decorative icons with no semantic value;
- irrelevant anecdotes;
- visual flourishes that compete with the concept;
- sidebars included only to create variety.

A simpler page with one meaningful diagram is better than a visually busy page with five decorations.

---

# 6. Signaling helps readers see structure

Multimedia-learning research on signaling/cueing supports highlighting organization and relevant elements to guide attention.

### Implication for V2

Use a controlled visual grammar:

- consistent figure titles;
- explicit labels;
- arrows that encode direction or causality;
- limited recurring box types;
- typography that distinguishes principle, example, formula and warning;
- highlighted variables in worked examples;
- clear figure references in prose.

Signaling should reveal structure, not create visual noise.

---

# 7. Text and graphics should be spatially integrated

The spatial-contiguity principle suggests that corresponding words and graphics are easier to learn from when they are near each other rather than separated.

### Implication for V2

A diagram should appear next to the paragraph that explains it.

Avoid layouts where:

- a graph is several pages away from its interpretation;
- a figure requires the reader to flip repeatedly;
- labels are moved into distant legends when direct annotation is possible;
- tables are detached from the decision they support.

---

# 8. Pre-training and segmentation help with complex systems

Multimedia-learning research on pre-training and segmentation suggests learners benefit when they know the main components before processing a complex interaction, and when complex material is divided into meaningful learner-paced segments.

### Implication for V2

Before a complex system such as:

- CAC/LTV/payback/cash interaction;
- customer-state routing;
- end-to-end sales process;
- expansion economics;

first introduce the minimum components and vocabulary, then show how they interact.

This justifies progressive disclosure, but the segments must later be recombined into a complete model.

---

# 9. Consistency reduces navigation cost

Textbook-design guides recommend consistent use of structural features so students learn how to use the book.

### Implication for V2

We need a controlled set of recurring devices, not a unique layout in every chapter.

Candidate taxonomy:

- **Principio** — durable rule or mental model;
- **Esempio svolto** — guided reasoning;
- **Errore frequente** — predictable misconception/failure;
- **Approfondimento** — useful depth that can be skipped on first pass;
- **Numeri** — equation/calculation/data interpretation;
- **Caso** — richer scenario;
- **Applicazione** — task for the reader.

These are candidates to prototype, not a mandatory quota.

---

# 10. Realistic scenarios improve conceptual accessibility

OpenStax's *Principles of Marketing* explicitly uses realistic company and organization scenarios, closing cases, data-oriented “Marketing Dashboard” boxes, knowledge checks and a running marketing-plan exercise to reinforce concepts.

### Implication for V2

Examples should not be random one-off names created to fill a paragraph.

V2 should combine:

1. micro-examples for immediate clarification;
2. worked examples for procedures/calculations;
3. recurring fictional cases for longitudinal integration;
4. selected documented real cases when they add evidence or strategic contrast;
5. capstone cases that require multi-chapter diagnosis.

---

# 11. The book must ask the learner to retrieve and apply

Textbook structures routinely include review questions, self-assessment, exercises and case problems because reading recognition is not the same as usable knowledge.

### Implication for V2

Chapter closers should include selective active work, for example:

- two or three retrieval questions;
- one diagnostic question;
- one transfer scenario;
- one calculation when relevant;
- one “what would change your decision?” question.

Do not turn every chapter into an exam. Use practice where it improves transfer.

---

# 12. Editorial implications for the current V1 failure

The external research aligns with the founder's critique and the quantitative postmortem.

V1 has:

- strong organization;
- strong signaling through headings;
- weak worked-example depth;
- almost no visual representation;
- limited active practice;
- excessive list-based compression;
- little distinction between exposition and instructional devices.

The V2 solution is not “add images”.

It is to redesign the **instructional unit**.

---

# 13. Research-backed design rules adopted provisionally

Until golden-chapter testing disproves them, V2 will follow these provisional rules:

1. Learning outcome before content inventory.
2. Narrative explanation before checklist compression.
3. Worked example before independent complex application for novice material.
4. Visualize relationships, not decoration.
5. Keep explanatory text close to the figure/table it interprets.
6. Use recurring pedagogical devices consistently.
7. Introduce components before complex interactions.
8. Recombine segments into complete causal models.
9. Use cases to support transfer, not merely variety.
10. Include retrieval/application opportunities at meaningful intervals.
11. Treat page design as part of instruction.
12. Validate the full system on golden chapters before mass production.

---

# Reference set

Primary working references for the editorial architecture:

- OpenStax, *Principles of Marketing — Preface*: https://openstax.org/books/principles-marketing/pages/preface
- Oregon State University, *Textbook elements*: https://open.oregonstate.education/osufacultyguide/chapter/textbook-elements/
- Oregon State University, *Developing your textbook structure*: https://open.oregonstate.education/osufacultyguide/chapter/textbook-structure/
- UBC Open Text Publishing Guide, *Textbook Design Rules*: https://pressbooks.bccampus.ca/openubcpub/chapter/textbook-design-rules-open-ubc/
- Queen's Open Textbook Authoring Guide, *Planning Your Open Textbook*: https://ecampusontario.pressbooks.pub/authoringguide/chapter/planning-your-open-textbook/
- Mayer & Fiorella, *The Cambridge Handbook of Multimedia Learning*, chapters on multimedia, coherence, signaling, contiguity, segmenting and pre-training: https://www.cambridge.org/core/books/cambridge-handbook-of-multimedia-learning/
- van Gog, Paas & Sweller, *Cognitive Load Theory: Advances in Research on Worked Examples...*: https://link.springer.com/article/10.1007/s10648-010-9145-4

Additional references may be added during the benchmark phase.