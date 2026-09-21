# Founder Review — Golden A + Golden B

Date: 2026-09-21

## Verdict

**FOUNDER GATE: FAIL — redesign required before Golden C or production scaling.**

Golden A and Golden B remain useful content/visual prototypes, but they are **not approved as the reader-facing model for Manual V2**.

The failure is architectural/editorial, not doctrinal.

---

# Founder feedback — binding requirements

## F-01 — General framing must precede detail

Current prototypes enter the concrete problem too quickly.

Required direction:

**general framing of the subject → conceptual map → progressive explanation → details/subtopics → illustrative example/application.**

The reader should first understand:

- what subject the chapter covers;
- why it matters;
- where it sits in the larger system;
- which major ideas/components the chapter will develop;
- only then the detailed mechanisms.

A concrete case may still appear later, but it should not routinely carry the burden of introducing the theory.

---

## F-02 — Voice is still too artificial/mechanical

Current prose is materially better than V1 but still sounds engineered.

Observed problems include:

- excessive causal choreography;
- too many deliberately constructed contrasts;
- consultant-like phrasing;
- sentences that sound designed to be quotable;
- artificial transitions that announce the reasoning;
- visible pedagogical machinery instead of natural exposition.

Required direction:

A more natural Italian expository voice: fluent, adult, discursive and precise, closer to a strong human-authored professional manual than to a narrated framework.

---

## F-03 — Theory first; examples later and clearly subordinate

The recurring named fictional-company approach is rejected as the default teaching architecture.

Do not invent brand/company names merely to make an example feel realistic.

Preferred illustrative forms:

- “supponiamo che un’azienda…”;
- “consideriamo due aziende, A e B…”;
- generic industry descriptions;
- real documented cases when they add evidentiary value.

Examples should normally follow the conceptual explanation and appear as:

- short examples inside prose;
- worked numerical examples;
- boxes/case studies after the theory;
- end-of-section or end-of-chapter applications.

The theory/concept must remain intelligible without the fictional example.

---

## F-04 — The hierarchy Part → Chapter → Section → Paragraph must become explicit

The current architecture does not yet communicate a sufficiently clear logical hierarchy.

Required semantic roles:

- **Part** = major domain/stage of the business/marketing system;
- **Chapter** = one broad, teachable subject within that domain;
- **Section** = one major component/subproblem needed to understand the chapter subject;
- **Paragraph** = one coherent explanatory move inside the section.

The hierarchy must be visible in the TOC and in page structure.

No backend/primary-home logic may leak into reader-facing boundaries.

---

## F-05 — Chapter titles must be short, general and topical

Current argumentative titles are rejected as final manual titles.

A chapter title should name the subject clearly, not summarize the chapter thesis.

Preferred direction:

- `Il sistema di marketing`
- `Economia del cliente`
- `Ricerca di mercato`
- `Posizionamento`
- `Offerta`
- `Prezzo`
- `Vendita consulenziale`
- `Retention`
- `Cassa e capitale circolante`

Longer thesis-like formulations belong in subtitles, opening paragraphs or section headings, not in the chapter title itself.

---

## F-06 — Preserve what worked

Founder explicitly approves the direction of:

- numerical worked examples where the subject requires them;
- quantitative explanation;
- charts/graphs used to make economic relationships visible.

Arrow/process diagrams are useful in principle but need later graphic redesign.

Do not throw away Golden B's quantitative teaching work while redesigning the chapter architecture.

---

# Root-cause diagnosis

The Golden prototypes over-applied several V2 design choices:

1. `problem/case first` became the default opener instead of one optional instructional form;
2. the recurring-case system became too prominent and started competing with the theory;
3. `visible expert reasoning` was implemented with an over-engineered consultant voice;
4. flexible chapter grammar did not create a strong enough visible textbook hierarchy;
5. chapter titles were optimized as provocative argument statements rather than navigational labels.

In short:

**V2 improved local writing quality but still did not fully switch from “AI-designed learning experience” to “human-authored systematic manual”.**

---

# Decisions

- **V2-D023 CURRENT:** general conceptual framing precedes detailed explanation by default.
- **V2-D024 CURRENT:** theory is primary; examples are subordinate explanatory/application devices.
- **V2-D025 CURRENT:** invented named recurring companies are not the default. Prefer generic unnamed examples, A/B labels, or sourced real cases.
- **V2-D026 CURRENT:** reader-facing hierarchy must explicitly enforce Part → Chapter → Section → Paragraph roles.
- **V2-D027 CURRENT:** chapter titles must be short, clear, topical nouns/noun phrases; thesis belongs below title level.
- **V2-D028 CURRENT:** numerical worked examples and explanatory charts are retained as approved instructional devices.
- **V2-D029 CURRENT:** current Golden A/B internal passes do not satisfy the founder gate; they are prototypes to mine, not templates to scale.
- **V2-D019 SUPERSEDED:** recurring named fictional case continuity is no longer a mandatory production rule.

---

# Consequence for Phase 6

Do **not** draft Golden C reader-facing prose yet.

Before further golden production:

1. redesign the book hierarchy and TOC naming;
2. replace the current chapter grammar with a general-to-specific expository architecture;
3. revise the Style Bible toward natural Italian manual prose;
4. replace the recurring fictional-case default with an example hierarchy;
5. re-spec Golden A and B under the new rules;
6. rewrite/restructure A and B and run founder-read again;
7. only after that resume Golden C.

The remaining chapters remain blocked.
