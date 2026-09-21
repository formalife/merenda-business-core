# Editorial Hierarchy — Manual V2

Status: **CURRENT — post founder-review redesign**  
Date: 2026-09-21

## Purpose

This document defines the reader-facing architecture of Manual V2 after the founder rejection of the first Golden A/B production model.

The manual must read as a systematic professional manual, not as a sequence of designed learning experiences or isolated knowledge modules.

The governing hierarchy is:

**Part → Chapter → Section → Paragraph**

Each level has one semantic job. Reader-facing structure must never be derived from backend primary-home logic, source folders, or the need to give every semantic unit a separate visible heading.

---

# 1. Part

A **Part** is a major domain or stage of the commercial/business system.

A Part answers a broad question such as:

- what is the system and how should it be read?;
- which market and customer should be served?;
- why should the customer choose and buy?;
- how is demand created and captured?;
- how are persuasion and selling managed?;
- what happens after the first sale?;
- do economics and organization withstand growth?;
- how should the business be built, reinvested in and expanded?

A Part should contain several chapters that belong together conceptually.

A Part title should be short, stable and suitable for a table of contents.

Good:

- `Mercato e cliente`
- `Domanda e acquisizione`
- `Economia e organizzazione`

Weak:

- `Come scegliere il mercato giusto prima di sprecare soldi in acquisizione`

The thesis belongs in the Part introduction, not in the title.

---

# 2. Chapter

A **Chapter** is one broad teachable subject inside a Part.

The title names the subject.

Preferred title forms:

- noun;
- short noun phrase;
- established technical term when useful.

Examples:

- `Posizionamento`
- `Offerta`
- `Prezzo`
- `Ricerca di mercato`
- `Vendita consulenziale`
- `Cassa e capitale circolante`

Avoid titles that are:

- questions;
- conclusions;
- slogans;
- provocative claims;
- summaries of the chapter's thesis.

A chapter may use a subtitle in production if it materially helps orientation, but the table-of-contents title remains topical.

Each chapter should answer four reader-orientation questions near the beginning, usually in prose rather than a checklist:

1. What subject are we studying?
2. Why does it matter to the business?
3. Where does it sit in the larger system?
4. What are the main components we need to understand?

Only after this general frame should the chapter descend into specific mechanisms, formulas, procedures or examples.

---

# 3. Section

A **Section** is one major component, distinction or subproblem required to understand the chapter subject.

A section should be large enough to develop a coherent explanation across several paragraphs.

Good section jobs:

- distinguish marketing from promotion;
- explain contribution margin;
- explain how awareness changes the communication task;
- explain the relationship between diagnosis and prescription;
- explain how working capital creates a financing gap.

A section title should orient, not perform copywriting.

Prefer:

- `Marketing e promozione`
- `Margine di contribuzione`
- `Stati della domanda`
- `Diagnosi e prescrizione`
- `Il ciclo di conversione della cassa`

Avoid over-clever titles whose meaning is not obvious from the TOC.

A chapter should usually have a limited number of substantial sections. There is no hard quota, but repeated one-page sections are a warning that the architecture may be too fragmented.

---

# 4. Paragraph

A **Paragraph** is one coherent explanatory move inside a section.

It can:

- state and develop a concept;
- explain a causal relationship;
- distinguish two ideas;
- interpret a formula;
- qualify a rule;
- connect theory to a practical consequence;
- introduce or interpret an example.

The paragraph is the primary unit of prose.

Default expectation:

- multi-sentence development;
- natural sentence-length variation;
- one intellectual move per paragraph;
- transitions carried by reasoning, not by constant headings.

One-sentence paragraphs are permitted for real emphasis, but should be exceptional.

---

# 5. Default chapter movement

The new default is **general to specific**.

## 5.1 General framing

Open by defining the field of the chapter in ordinary language.

Establish:

- scope;
- business relevance;
- relationship to previous and later chapters;
- main conceptual map.

This is not a summary of everything that follows. It is the reader's orientation layer.

## 5.2 Theory and conceptual structure

Explain the core model before relying on examples.

Definitions should be introduced as part of the exposition, not as a glossary dump.

## 5.3 Components and mechanisms

Move section by section through the main parts of the subject.

The ordering should answer:

**what must the reader understand first so that the next distinction makes sense?**

## 5.4 Examples and worked applications

Use examples after the relevant theory is intelligible.

Examples may include:

- generic company scenario;
- Company A / Company B comparison;
- numerical worked example;
- real sourced case;
- operational artifact.

The example demonstrates the theory. It does not carry the burden of defining it.

## 5.5 Synthesis and application

Close by reconnecting the components and showing what decision competence the reader now has.

A checklist, tool or exercise may follow when useful.

---

# 6. Exceptions to the default

A chapter may open with a short example, fact, contradiction or question when it genuinely improves orientation.

However:

- the example must be short;
- it must not delay the general framing;
- it must not become a recurring fictional narrative the reader has to remember;
- the theory must remain understandable if the example is removed.

The exception must be earned by the topic, not used as a house style.

---

# 7. Navigation rules

The table of contents should be useful as a conceptual map even before reading the book.

Therefore:

- Part titles identify domains;
- Chapter titles identify subjects;
- Section titles identify major components;
- paragraph-level claims do not appear in the TOC;
- examples and boxes normally do not define structural boundaries unless they are substantial case-study sections.

A reader looking for `Prezzo`, `Retention` or `Capacità` should find those concepts directly from the TOC.

---

# 8. Relationship to backend knowledge architecture

Backend artifacts remain useful for:

- semantic coverage;
- primary-home assignment;
- provenance;
- dependency checking;
- doctrine audit.

They do **not** determine the visible hierarchy of the manual.

The mapping is many-to-one:

multiple backend semantic units may be synthesized into one paragraph or section.

A visible section exists because the reader needs it, not because a source file exists.

---

# 9. Naming rules

## Part title

2–5 words preferred.

## Chapter title

Usually 1–4 words; longer only when technical precision requires it.

## Section title

Clear descriptive phrase; normally shorter than a sentence.

## Subtitle

Optional. Can carry thesis, question or practical angle when useful, but should not replace a clear chapter title.

---

# 10. Architecture quality checks

## `PART-JOB`

Can the Part's domain be explained in one sentence without listing its chapters?

## `CHAPTER-SUBJECT`

Does the chapter title name a subject rather than make an argument?

## `SECTION-NECESSITY`

Is every section required to understand the chapter, or is it merely a leftover semantic unit?

## `GENERAL-FIRST`

Could a smart beginner explain the chapter's scope and conceptual map before encountering its first detailed case?

## `TOC-AS-MAP`

Can the TOC alone show the logical progression of the manual?

## `REMOVE-BACKEND`

Would the visible hierarchy still make sense to a reader who knows nothing about the repository or source taxonomy?

---

# 11. Acceptance rule

The hierarchy passes when:

1. every Part has one clear domain;
2. every Chapter names one broad subject;
3. every Section represents a necessary component of that subject;
4. paragraphs carry most of the explanation;
5. examples are subordinate to theory;
6. the TOC is usable as a map of the discipline;
7. no chapter title reads like an article headline or a generated thesis statement.
