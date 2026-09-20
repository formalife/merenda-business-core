# Manual Project Status

## Stato generale

**ACTIVE — FASE 6 / DRAFTING DEL MANUALE**

Le Fasi 0–5 sono concluse e auditate. Il drafting reader-facing è in corso sul branch `manual-drafting-2026-09-20`.

## Baseline e freshness

Baseline dottrinale iniziale: `93f8eae978fdffb55c5623ae06603e5895b71e11` — 2026-09-20.

Prima di ogni blocco sostanziale di drafting verificare `main` live e rileggere i nodi canonici pertinenti.

## Decisioni correnti

- **D-001 CURRENT:** `manual/` è publishing layer; `merenda/` resta canonico.
- **D-002 CURRENT:** beginner-first.
- **D-003 CURRENT:** voce reader-facing agnostica, senza Frank/Merenda/KB/Layer 1.
- **D-004 CURRENT:** provenance e temporal precedence preservate nel backend.
- **D-005 CURRENT:** rewrite, not collage.
- **D-006 SATISFIED:** drafting massivo autorizzato dopo PASS delle Fasi 1–5.
- **D-007 CURRENT:** 60/60 file canonici coperti.
- **D-008 CURRENT:** VoC multi-fonte consolidata in `syntheses/voice-of-customer.md`.
- **D-009 CURRENT:** front-end = riduzione della barriera, non sinonimo di low price.
- **D-010 CURRENT:** economics in progressive disclosure: Cap. 2 base, Capp. 30–32 avanzati.
- **D-011 CURRENT:** 8 parti / 39 capitoli; Cap. 39 = operating system diagnostico.

## Fasi completate

- **Fase 0 — DONE:** control plane e baseline.
- **Fase 1 — DONE:** 60/60 file censiti.
- **Fase 2 — DONE / PASS:** 60/60 covered; 709 unità semantiche; primary-home/dependency/provenance/cases completati.
- **Fase 3 — DONE / PASS:** curriculum 8 parti / 39 capitoli; D-01…D-35 verificati.
- **Fase 4 — DONE / PASS:** VoC, glossary, synthetic cases; G-001…G-008 risolti editorialmente.
- **Fase 5 — DONE / PASS:** 39/39 chapter specs.

## Fase attiva — Fase 6 / Drafting

### Parte I — Capp. 1–4
**READY / MINI-AUDIT PASS** — `manual/draft/part-01-fondamenti.md`

### Parte II — Capp. 5–8
**READY / MINI-AUDIT PASS CON P2 LESSICALI NON BLOCCANTI** — `manual/draft/part-02-mercato.md`

### Parte III — Capp. 9–13
**READY / MINI-AUDIT PASS** — `manual/draft/part-03-posizionamento-offerta.md`

### Parte IV — Capp. 14–19
**READY / MINI-AUDIT PASS** — `manual/draft/part-04-domanda-acquisizione.md`

### Parte V — Capp. 20–24
**READY / MINI-AUDIT PASS CON P2 LESSICALI NON BLOCCANTI** — `manual/draft/part-05-copy-vendita.md`

### Parte VI — Capp. 25–29
**READY / MINI-AUDIT PASS CON P2 LESSICALI NON BLOCCANTI** — `manual/draft/part-06-lifecycle-brand.md`

Copre:

- onboarding come transizione al first value, non semplice welcome;
- customer success, customer effort, segnali di uso/frizione e feedback loop verso processo/prodotto;
- durata/frequenza naturale prima di retention, churn e riattivazione;
- distinzione fra retention preventiva, riattivazione, riconquista e uscita naturale;
- seconda vendita e next-best-offer come ipotesi fondate sul bisogno reale;
- referral, testimonianze e review dopo risultato verificato e con rischio reputazionale del promotore esplicito;
- reputazione e crisi su stakeholder, pre-mortem, verifica, rimedio e correzione sistemica;
- brand come accumulo di significato distinto, prova, esperienza, reputazione e ripetizione nel tempo;
- audience/fanbase separate dalla customer base economica.

Mini-audit:

- coverage Capp. 25–29: PASS;
- onboarding → first value: PASS;
- ticket/support → root-cause feedback: PASS;
- retention ≠ keep forever: PASS;
- natural exit ≠ pathological churn: PASS;
- reactivation/win-back separated: PASS;
- referral/proof after verified value: PASS;
- reputation recovery requires operational remedy: PASS;
- brand ≠ logo/notoriety/community-first: PASS;
- reader-facing agnosticism: PASS;
- nessun P0/P1.

## Ordine rimanente

1. Parte VII — Capp. 30–35 — **NEXT**;
2. Parte VIII — Capp. 36–39.

## Next Action

Draftare `manual/draft/part-07-economics-scala.md` da `chapter-specs/part-07-economics-scala.md` dopo freshness read dei nodi live su unit economics, cassa/capacità, controlli interni, processi/delega, persone e trasferibilità.

Vincoli principali:

- economics avanzati senza perdere il beginner-first;
- LTV non usato come scusa per ignorare payback/cassa;
- crescita subordinata a capacità e capitale;
- processi costruiti sui workflow reali, non SOP decorative;
- delega con decision rights e accountability;
- persone/ruoli specializzati solo quando il collo di bottiglia e l'economia lo giustificano;
- scalabilità e transferability separate dalla sola crescita di fatturato.

## Gap aperti

**Nessun gap P0/P1.**

P2 editoriali correnti: uniformare nel copy-edit globale alcuni inglesismi reader-facing non indispensabili nelle Parti I–VI, definire/italianizzare dove utile termini come `advocacy`, nomi dei canvas e correggere piccoli refusi locali.

## Blocchi

Nessun blocco corrente.

## Handoff obbligatorio

`ROADMAP.md` → `STATUS.md` → `MANUAL_CONTRACT.md` → `MANUAL_CURRICULUM.md` → `MANUAL_GAPS.md` → `BEGINNER_GLOSSARY.md` → chapter spec attiva → nodi canonici live → `PROVENANCE_MAP.md` se sensibile.

Aggiornare questo file dopo ogni blocco di drafting.