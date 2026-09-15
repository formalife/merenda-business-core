# PROJECT STATUS

## Stato generale

ACTIVE — fasi 1–6 complete; contenuti **1–300 processati semanticamente**. Checkpoint **300 — FASE 14 + FASE 15 eseguite da Claude Code** sul branch `checkpoint-300`. Corpus Merenda ancora non dichiarato completo.

## Fase corrente

Checkpoint 300 chiuso: FASE 14 (refactor KB) e FASE 15 (audit tassonomico + riclassificazione residui) eseguite. Nessuna duplicazione sostanziale trovata nel batch 276–300: i tre nuovi nodi e gli altri inserimenti reggono ai confini richiesti senza necessità di merge/split. Nessun file di `merenda/` modificato in questo checkpoint.

Weighted Novelty del batch 276–300 (invariata, per riferimento):

- peso 2: **4**
- peso 1: **9**
- peso 0: **12**
- totale pesato: **17/50 = 34%**
- contenuti realmente incrementali: **13/25 = 52%**

## Corpus

- Video individuati: **468**
- Contenuti processati semanticamente: **300**
- STUDIATO / integrati o deduplicati: **294**
- ESCLUSO dalla dottrina attiva: **6**
- Da processare: **168**
- Corpus completo: NO
- 301 — `asMedYJtd4I` resta **DA STUDIARE**
- Nessun contenuto 301+ processato semanticamente né acquisito in questo checkpoint

## Nuovi nodi canonici (batch 276–300, verificati in FASE 14)

1. `merenda/07_copy_comunicazione/copy-posizionamento-e-temperatura-traffico.md`
2. `merenda/08_brand/reputazione-e-crisis-management.md`
3. `merenda/09_business/retention-onboarding-e-customer-success.md`

Tutti confermati privi di duplicazione sostanziale con i nodi confinanti dopo lettura integrale.

## Novelty recente

- Batch 226–250: **16/25 = 64%**
- Batch 251–275: **11/25 = 44%**
- Batch ottimizzato 276–300: **13/25 = 52%**, Weighted Novelty **17/50 = 34%**

## Audit residui post-300 (FASE 15)

Nuovo artefatto: `reviews/RESIDUAL_REPRIORITIZATION_301-468.md` (non sovrascrive il documento storico 276–468).

- MUST STUDY residuo: **0/168** (i 15 MUST STUDY del checkpoint 275 erano tutti nel batch 276–300, ora chiuso).
- TARGETED: **59/168**.
- LOW / DEFER: **109/168**.
- 7 downgrade TARGETED → LOW/DEFER applicati (framework numerici/KPI, delega strategica, CRM/LTV isolato: temi oggi ampiamente coperti in `numeri-cassa-e-crescita.md`, `marketing-first.md`, `scalabilita-e-operativita.md`).

## Decisione strategica del checkpoint 300

**B — CONTINUARE MERENDA SOLO SU GAP MIRATI.**

Motivazione sintetica: Weighted Novelty 34% ricade nella fascia intermedia della regola adattiva ("20–40% → niente avanzamento sequenziale; acquisire solo gap specifici"); il livello MUST STUDY dei residui è esaurito; i 168 residui sono concentrati per l'82% in aree già dense (`06_vendita`, `09_business`, `10_casi_studio`). La KB non è dichiarata satura: non si raccomanda ancora l'apertura dello strato esterno/evidence. Dettaglio completo in `reviews/CHECKPOINT_300.md`.

Un eventuale prossimo batch tecnico dovrebbe limitarsi a 8–12 ID scelti tra i 59 TARGETED con dedup "Media" in `RESIDUAL_REPRIORITIZATION_301-468.md`, non a un batch generico da 25 in ordine di coda.

## Validazione

Baseline **842 warning** (836 `Ordine/stato incoerente`, 3 `File congelato modificato`, 3 `Contatore STATUS errato`) confermata identica prima e dopo il checkpoint 300 (diff riga per riga vuoto). `git diff --check` pulito. File frozen byte-identici a `816090ef7f7998edc5571f1529a8192b72c7190f`. 0 link/ancore rotti, 0 file orfani, 0 contaminazione Formalife in `merenda/`.

## Workflow attivo

- CODEX: acquisizione tecnica.
- CHATGPT: revisione semantica e fasi 8–13.
- CLAUDE CODE: FASE 14 ogni 25; FASE 14 + FASE 15 ogni 50.
- A/B/C = profondità di review.
- Information Priority = ordine adattivo di acquisizione.
- C = FAST REVIEW, mai SKIP.

## Checkpoint

- Ultimo refactor KB completato: **300 — FASE 14**
- Ultimo audit tassonomia completato: **300 — FASE 15**
- Soglia semantica raggiunta: **300**
- Prossimo checkpoint Claude: **325 — FASE 14**
- Prossimo audit tassonomia: **350 — FASE 14 + FASE 15**

## Agente richiesto

**CODEX**, soltanto previa conferma dell'utente sulla dimensione/selezione di un batch tecnico mirato (8–12 ID tra i TARGETED indicati in `reviews/RESIDUAL_REPRIORITIZATION_301-468.md`). In assenza di conferma, nessuna azione tecnica 301+ va avviata.

## Next Action

Attendere decisione dell'utente su un eventuale batch tecnico mirato (opzione B del checkpoint 300). Non avviare acquisizione 301+ senza conferma esplicita e senza una selezione precisa di ID.

**Non acquisire né processare semanticamente 301+ finché non arriva tale conferma.**
