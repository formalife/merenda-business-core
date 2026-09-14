# PROJECT STATUS

## Stato generale

ACTIVE — fasi 1–6 complete; contenuti **1–275 processati semanticamente**. Checkpoint **275 raggiunto**; FASE 14 Claude Code ancora da eseguire. Corpus ancora incompleto.

## Fase corrente

Revisione semantica **251–275 completata da ChatGPT**: 25/25 review, 25/25 STUDIATO, nessun nuovo ESCLUSO.

Report pre-handoff: `reviews/CHECKPOINT_275.md`.

## Corpus

- Video individuati: **468**
- Contenuti processati semanticamente: **275**
- STUDIATO / integrati o deduplicati: **269**
- ESCLUSO dalla dottrina attiva: **6**
- Da processare: **193**
- Corpus completo: NO
- Batch tecnico 251–275: **25/25 transcript utilizzabili**
- Sottotitoli batch: **25 automatici italiani originali / 0 manuali**
- Review 251–275: **25/25**
- Nuovi ESCLUSO nel batch: **0**

## Novelty 251–275

- Incrementali: **11/25 = 44%**
- Deduplicati/confermativi: **14/25 = 56%**
- Nessun nuovo ESCLUSO

Nuovi nodi KB principali:

- `merenda/04_marketing/test-creativita-annunci.md`
- `merenda/06_vendita/rete-vendita-script-allenamento-e-controllo.md`
- `merenda/08_brand/pr-earned-media-e-notiziabilita.md`

Dettaglio completo in `reviews/CHECKPOINT_275.md`.

## Validazione

Validator reale post-semantica 251–275: **842 warning**, identici alla baseline checkpoint 250:

- 836 `Ordine/stato incoerente` storici;
- 3 `File congelato modificato` dovuti al mismatch storico del validator;
- 3 `Contatore STATUS errato` storici.

`git diff --check`: pulito. Nessuna nuova classe o incremento di warning.

Frozen effettivamente non modificati nel batch. Nessuna contaminazione Formalife nella KB. Nessun contenuto 276+ processato semanticamente.

## Workflow attivo — v1.1

- CODEX: acquisizione tecnica e supporto meccanico.
- CHATGPT: revisione semantica e fasi 8–13.
- CLAUDE CODE: FASE 14 ogni 25; FASE 14 + 15 ogni 50.
- Classificazione A/B/C: priorità/profondità, mai esenzione dalla revisione.
- C = FAST REVIEW, mai SKIP.
- Nessuna modifica ai file frozen.

## Checkpoint

- Ultimo refactor KB completato: **250 — FASE 14**
- Ultimo audit tassonomia completato: **250 — FASE 15**
- Refactor KB richiesto ora: **275 — FASE 14**
- Prossimo audit tassonomia: **300 — FASE 14 + FASE 15**
- Checkpoint Claude richiesto ora: **SÌ**
- Report corrente: `reviews/CHECKPOINT_275.md` (pre-handoff)

## Agente richiesto

**CLAUDE CODE**

## Next Action

Eseguire **CHECKPOINT 275 — FASE 14** sulla KB completa.

Focus richiesti: nuovo nodo rete vendita e confini con diagnosi/prequalifica; creative testing; PR/earned media; nuova segmentazione per consapevolezza e storia d'acquisto. Applicare MERGE, NOT APPEND, preservare la prevalenza temporale, non processare 276+, non modificare frozen.

Rieseguire validator prima/dopo contro baseline **842** e `git diff --check`.

Dopo la chiusura Claude, il prossimo contenuto da acquisire/processare sarà **276 — `Hs8y1wNyamo`**. Nessuna acquisizione 276+ prima della chiusura del checkpoint 275.
