# Manual Revalidation — integrazione sales doctrine — 2026-09-22

## Scopo

Verificare che la rifusione Sandler → Merenda non renda obsoleta l'architettura editoriale già approvata e che la nuova doctrine abbia case didattiche complete senza duplicare sistemi, capitoli o provenance reader-facing.

Questa review **non riscrive retroattivamente** `PHASE2_AUDIT.md`, `PHASE3_AUDIT.md` o `PHASE5_AUDIT.md`. Quei documenti restano audit corretti del baseline 2026-09-20. Questa revalidation copre soltanto il delta introdotto il 2026-09-22.

---

# Stato all'ingresso

Baseline manuale:

- 39 capitoli;
- 60 file doctrine/routing tracciati;
- 709 unità semantiche;
- Phase 5 audit: PASS sul baseline precedente.

Delta dottrinale:

- nuovo nodo `05_acquisizione/prospecting-e-outbound.md`;
- rifusione di `06_vendita` in 11 nodi canonici specialistici + README;
- 4 vecchi path `06_vendita` trasformati in routing aliases `SUPERSEDED`;
- arricchimento di `09_business/retention-onboarding-e-customer-success.md` con handoff, Customer Success e account growth;
- provenance Sandler conservata nel backend, senza dipendenza operativa dalla repo Sandler.

---

# 1. Coverage

## Crosswalk delta

Creati:

- `crosswalk/05_acquisizione_integration_2026-09-22.md` — ACQ-068…ACQ-076;
- `crosswalk/06_vendita_integration_2026-09-22.md` — SAL-072…SAL-110;
- `crosswalk/09_business_integration_2026-09-22.md` — BUS-108…BUS-113.

Master aggiornato:

- file doctrine/routing tracciati: **72**;
- unità semantiche: **763**;
- nodi canonici omessi: **0**;
- routing aliases esclusi con ragione: **4**.

**Verdict coverage: PASS.**

---

# 2. Architettura didattica

La nuova conoscenza non richiede nuovi capitoli.

Routing editoriale finale:

- **Cap. 16** — canali + prospecting/outbound;
- **Cap. 22** — handoff e prequalifica, con confine prequalifica ≠ qualification;
- **Cap. 23** — relazione/processo → problema/Pain → investimento/Budget → Decision → Fulfillment → decisione → Post-Sell;
- **Cap. 24** — follow-up state-based + sales performance + Behavior/Attitude/Technique + behavior plan + coaching/accountability;
- **Cap. 25** — handoff sales→delivery, onboarding, Customer Success e value review;
- **Cap. 26** — lifecycle, account growth e requalification delle nuove opportunity.

Il curriculum resta a **39 capitoli**.

**Verdict architecture: PASS.**

---

# 3. Primary-home e redundancy control

## Confini preservati

- Prospecting è Acquisition, non trattativa.
- Marketing/prequalifica prepara ma non certifica Pain/Budget/Decision.
- Qualification vive in Sales.
- Fulfillment/proposta viene dopo qualification sufficiente.
- Post-Sell immediato chiude/stabilizza la decisione.
- Customer Success continuativo vive nel lifecycle/Business.
- Expansion non è un ottavo step: quando nasce una nuova opportunity, rientra nella normale qualification.
- Behavior/Attitude/Technique è un diagnostico di performance, non un secondo sales process.

## Legacy

I quattro vecchi file di `06_vendita` non hanno più una casa editoriale autonoma perché non contengono più doctrine; restano compatibilità di routing temporanea.

**Verdict redundancy/primary-home: PASS.**

---

# 4. Provenance e reader-facing agnosticism

Backend:

- MERENDA PRIMARY resta distinto da ASSIMILATED e SYNTHESIS;
- framework e tattiche Sandler mantengono provenance reale nei nodi/crosswalk;
- elementi current/institutional/historical non vengono appiattiti.

Reader-facing:

- chapter specs non insegnano “Merenda vs Sandler”;
- la vendita viene presentata come un unico sistema causale;
- nomi proprietari non necessari sono sostituiti da definizioni funzionali;
- il glossario non importa voci come `UFC`, `Cookbook`, `Negative Reverse` o `Strip-Lining` solo perché esistono nel backend;
- termini necessari al principiante — prospecting, qualification, disqualification, problema qualificato, investimento, decision process, readiness, Behavior/Attitude/Technique, behavior plan, coaching, account growth — sono definiti al first use.

**Verdict provenance/reader-facing: PASS.**

---

# 5. Causal integrity

La sequenza didattica corrente è:

**mercato/cliente → positioning/offerta/proof → domanda/canale/prospecting → database/funnel/pre-education → handoff/prequalifica → qualification → Fulfillment/decisione → follow-up/performance → handoff post-sale → customer success/lifecycle/account growth → economics/capacity/scale.**

Prerequisiti chiave esplicitati:

- outbound non precede target/economics;
- proposal non precede Pain/Budget/Decision;
- follow-up non compensa automaticamente qualification debole;
- activity volume non compensa automaticamente skill/target/pipeline deboli;
- expansion non precede valore realizzato e nuovo bisogno reale.

**Verdict causal integrity: PASS.**

---

# 6. Beginner clarity

Il nuovo materiale introduce più profondità commerciale senza presupporre familiarità con Sandler.

Aggiunte al glossario:

- prospecting/outbound/new conversation;
- qualification/light qualification/disqualification;
- problema qualificato/Pain;
- investimento/Budget;
- decision process/stakeholder;
- readiness/Post-Sell;
- Behavior/Attitude/Technique;
- behavior plan/coaching/accountability;
- customer service/value review/account growth.

Guardrail espliciti impediscono di interpretare:

- Pain come teatralizzazione emotiva;
- Budget come prezzo di listino;
- Decision come “chi firma?”;
- readiness score come matematica del close;
- performance framework come diagnosi clinica;
- Customer Success come vendita automatica.

**Verdict beginner clarity: PASS.**

---

# 7. Gap review

## P0 — blocker

**0**

## P1 — materiale prima del drafting

**0**

## P2 — opzionale / copy-edit successivo

- decidere in drafting quanto mantenere la parola inglese `Pain` dopo la prima definizione;
- decidere se usare sempre `investimento` reader-facing e tenere `Budget` solo come sinonimo/gloss;
- decidere se i nomi delle tattiche conversazionali meritino box/reference o se bastino le funzioni.

Nessuno dei tre punti cambia architettura, causalità o coverage.

---

# Verdict finale

**PASS — MANUAL ARCHITECTURE REMAINS VALID AFTER SALES INTEGRATION.**

Condizioni soddisfatte:

- 763 unità tracciate;
- 39 capitoli preservati;
- nessun nodo canonico senza casa;
- nessun secondo sistema di vendita;
- provenance conservata nel backend;
- reader-facing source-agnostic;
- nessun gap P0/P1.

Il manuale può procedere al drafting/revisione dei capitoli interessati usando le chapter specs correnti, senza riaprire Phase 2–5 da zero.
