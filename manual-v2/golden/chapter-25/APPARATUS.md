# Golden B — Pedagogical Apparatus

Chapter: `Capitolo 25 — Economia del cliente`  
Status: **CURRENT PROTOTYPE — to be integrated in publishing/layout layer after founder approval**

## Objective

Make a quantitative chapter easier to reuse without turning it into a formula handbook.

The existing prose, formulas, figures and worked calculations remain primary. The apparatus should help the reader avoid measurement errors and apply the model to real customer economics.

---

# Rejected feature — IN PRATICA after CAC discussion

The first apparatus draft proposed an `IN PRATICA` box after the explanation of fully loaded CAC.

**FEATURE-DELETE RESULT: REMOVE.**

Reason: the current prose already gives a strong practical check — asking which resources would really disappear if those customers were not acquired. Repeating the same job in a callout would fragment a section that already works.

This rejection is retained as evidence that the apparatus is not quota-driven.

---

# Existing feature B1 — ESEMPIO NUMERICO

Existing chapter feature:

`ESEMPIO NUMERICO — Economia elementare di un account`

## Decision

KEEP.

It demonstrates contribution and CAC after the concepts have been explained.

---

# Existing feature B2 — ESEMPIO SVOLTO

Existing chapter feature:

`ESEMPIO SVOLTO — Due coorti con lo stesso CAC`

## Decision

KEEP with Figures 25.1 and 25.2.

## Publishing note

The example, figures and table are one instructional sequence. Avoid styling them as three unrelated callouts.

---

# Feature B3 — ERRORE FREQUENTE

## Placement

Section `25.3 Lifetime value`, after the distinction between observed value and modeled future value and before using LTV:CAC as a summary ratio.

## Reader-facing copy

> **ERRORE FREQUENTE — Usare il futuro per giustificare il presente**
>
> Il lifetime value può diventare molto convincente proprio quando è meno affidabile. Se il valore futuro dipende da retention, rinnovi, upsell o frequenze che non sono ancora state osservate, aumentare quelle ipotesi fa salire facilmente il CAC che l'impresa sembra potersi permettere. La disciplina corretta è separare sempre ciò che una coorte ha già prodotto da ciò che il modello prevede che produrrà. Le previsioni servono a decidere; non devono essere presentate come prova già acquisita.

## Learning job

Prevent forecast-as-evidence errors that can authorize economically dangerous acquisition spend.

---

# Feature B4 — APPROFONDIMENTO

## Placement

Section `25.3 Lifetime value`, after the paragraph on LTV:CAC not having a universal threshold.

## Reader-facing copy

> **APPROFONDIMENTO — Perché lo stesso LTV:CAC può descrivere aziende molto diverse**
>
> Un rapporto LTV:CAC identico non implica lo stesso rischio finanziario. Un'impresa che recupera il CAC in tre mesi può reinvestire lo stesso capitale più volte nell'anno; un'altra che lo recupera in diciotto mesi deve finanziare molto più a lungo la crescita. Inoltre, la qualità del rapporto cambia con la stabilità dei dati: un LTV quasi interamente osservato è diverso da un LTV costruito su diversi anni di previsioni. Per questo il rapporto va letto insieme a payback, cassa e incertezza, non come una soglia automatica di salute.

## Learning job

Add a second-order financial interpretation useful to advanced readers without interrupting the beginner's main path.

## Why this earns an `APPROFONDIMENTO`

The core chapter already explains the ratio sufficiently for first understanding; this box is additional nuance rather than missing theory.

---

# Existing feature B5 — ESEMPIO NUMERICO

Existing chapter feature:

`ESEMPIO NUMERICO — Costruire una soglia di acquisizione`

## Decision

KEEP.

The worked threshold is a decision-rule example, not a benchmark.

---

# Feature B6 — VERIFICA NELLA TUA AZIENDA

## Placement

Near the end of Section `25.6 Costo marginale e leve di crescita`, before the final bridge to the cash chapter.

## Reader-facing copy

> **VERIFICA NELLA TUA AZIENDA — Costruisci la scheda economica di una coorte reale**
>
> Scegli un gruppo di clienti abbastanza omogeneo: per esempio quelli acquisiti nello stesso mese, dallo stesso canale o con la stessa offerta. Usa dati reali per ricostruire:
>
> 1. **CAC completo della coorte.** Quali costi hai incluso nel numeratore e quanti nuovi clienti stai usando come denominatore?
> 2. **Contribuzione osservata.** Quanto è rimasto dopo i costi variabili attribuibili nei primi 3, 6 o 12 mesi disponibili?
> 3. **Payback osservato.** In quale periodo la contribuzione cumulata ha recuperato il CAC, se lo ha già fatto?
> 4. **Parte modellata.** Quale quota del valore futuro deriva da dati osservati e quale da ipotesi su retention, frequenza, prezzo o upsell?
> 5. **Costo massimo sostenibile.** Quanto deve rimanere per struttura/profitto e quale margine di sicurezza richiedono cassa e rischio?
> 6. **Economia marginale.** Il prossimo incremento di acquisizione dovrebbe produrre clienti allo stesso costo storico oppure a un costo diverso?
>
> Se non riesci a compilare uno dei punti, non riempire il vuoto con una stima silenziosa. Segnalo come dato mancante o ipotesi: è precisamente l'informazione che il prossimo ciclo di misurazione deve produrre.

## Learning job

Convert formulas into one coherent customer-economics diagnostic on real data.

## Evidence output

One cohort economics sheet with observed vs modeled values explicitly separated.

---

# Feature-density audit

Support apparatus in Chapter 25:

- 1 new `ERRORE FREQUENTE`;
- 1 `APPROFONDIMENTO`;
- 1 `VERIFICA NELLA TUA AZIENDA`;
- 3 existing worked/numerical example sequences;
- 2 quantitative figures + comparison table + displayed formulas.

No additional `IN PRATICA` box is needed because the prose already contains the operating implication.

This is already a high-density chapter because the subject is quantitative.

## Layout rule

Do not style every formula as a separate box. Formulas belong to the narrative. The optional callouts above should be visually quieter than worked examples and charts.

## Gate

**APPARATUS DENSITY: PASS WITH LAYOUT CAUTION.**

The publishing prototype must verify that the chapter still feels like continuous explanatory prose rather than a financial workbook.
