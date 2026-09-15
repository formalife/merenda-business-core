# PROJECT STATUS

## Stato generale

ACTIVE — fasi 1–6 complete; contenuti **1–275 processati semanticamente**. Checkpoint **275 chiuso**: FASE 14 Claude Code eseguita. La coda residua **276–468 è stata riprogettata per information gain**; nessun contenuto 276+ è stato ancora acquisito o processato semanticamente. Corpus ancora incompleto.

## Fase corrente

Revisione semantica **251–275 completata da ChatGPT**: 25/25 review, 25/25 STUDIATO, nessun nuovo ESCLUSO. FASE 14 Claude Code eseguita e checkpoint 275 definitivamente chiuso.

Dopo il checkpoint è stata eseguita una riprioritizzazione strategica dei **193 residui**, separando la vecchia classe A/B/C (profondità di review) dalla nuova **Information Priority** (ordine di acquisizione): **15 MUST STUDY / 76 TARGETED / 102 LOW-DEFER**.

Report: `reviews/RESIDUAL_REPRIORITIZATION_276-468.md`.

## Corpus

- Video individuati: **468**
- Contenuti processati semanticamente: **275**
- STUDIATO / integrati o deduplicati: **269**
- ESCLUSO dalla dottrina attiva: **6**
- Da processare: **193**
- Corpus completo: NO
- Nessun contenuto del nuovo batch 276–300 ancora acquisito
- Nessuna variazione dei contatori semantici dovuta alla riprioritizzazione

## Novelty recente

- Batch 226–250: **16/25 incrementali = 64%**
- Batch 251–275: **11/25 incrementali = 44%**
- Il calo del valore marginale ha motivato il passaggio da coda sequenziale a coda adattiva basata su information gain.

## Priorità informativa residua

- MUST STUDY: **15**
- TARGETED: **76**
- LOW / DEFER: **102**
- Totale residuo: **193**

Il nuovo batch 276–300 contiene tutti i 15 MUST STUDY più 10 TARGETED scelti per coprire gap e diversificare l'informazione: **5 copy, 5 brand, 5 vendita, 10 business**.

La vecchia classificazione `reviews/RESIDUAL_CLASSIFICATION_201-468.md` resta storica. La nuova fonte operativa è `reviews/RESIDUAL_REPRIORITIZATION_276-468.md`.

## Validazione

Baseline strutturale precedente al riordino: **842 warning storici**:

- 836 `Ordine/stato incoerente`;
- 3 `File congelato modificato` dovuti al mismatch storico del validator;
- 3 `Contatore STATUS errato` storici.

Il riordino modifica intenzionalmente soltanto l'ordine dei residui in `QUEUE.md`; 1–275, stati semantici, KB, frozen, catalogo e VIDEO_INDEX restano invariati. Poiché le posizioni residue erano già comprese nel mismatch storico catalogo/queue, il riordino non deve essere “corretto” riallineando fuori scope il catalogo.

## Workflow attivo — v1.1

- CODEX: acquisizione tecnica e supporto meccanico.
- CHATGPT: revisione semantica e fasi 8–13.
- CLAUDE CODE: FASE 14 ogni 25; FASE 14 + 15 ogni 50.
- Classificazione A/B/C: priorità/profondità di revisione, mai esenzione.
- Information Priority: ordine adattivo di acquisizione basato sul valore marginale atteso.
- C = FAST REVIEW, mai SKIP.
- Nessuna modifica ai file frozen.

## Checkpoint

- Ultimo refactor KB completato: **275 — FASE 14**
- Ultimo audit tassonomia completato: **250 — FASE 15**
- Prossimo checkpoint Claude: **300 — FASE 14 + FASE 15**
- Checkpoint Claude richiesto ora: **NO**

## Agente richiesto

**CODEX**

## Next Action

Acquisizione tecnica del **nuovo batch ottimizzato 276–300**, a partire da:

**276 — `KipX0tAAWr4` — "Why COPYWRITING starts with your positioning [Full Course]"**

Il batch termina con:

**300 — `Fo8PB_7fE60` — "HOW TO DO BUSINESS | The organizational chart of a modern company"**

Dopo l'acquisizione tecnica, restituire il controllo a ChatGPT per la revisione semantica 276–300 (fasi 8–13) e misurare anche la **Weighted Novelty**. Solo dopo il checkpoint 300 si deciderà se continuare con altri TARGETED, passare a gap specifici o considerare sufficientemente satura la KB Merenda.
