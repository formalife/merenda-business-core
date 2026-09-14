# PROJECT STATUS

## Stato generale

ACTIVE — fasi 1–6 complete; contenuti 1–200 processati semanticamente; checkpoint 200 (FASE 14 + FASE 15) completato da Claude Code. Corpus ancora incompleto.

## Fase corrente

**Checkpoint 200 — FASE 14 + FASE 15: completato.** FASE 14: rilettura globale di `merenda/` (42 file), nessuna modifica strutturale necessaria (nessuna duplicazione, nessun file orfano, nessun link rotto). FASE 15: audit tassonomia, le 11 categorie restano valide. Prodotta classificazione strategica A/B/C dei 268 contenuti residui (`reviews/RESIDUAL_CLASSIFICATION_201-468.md`). Report completo in `reviews/CHECKPOINT_200.md`.

## Corpus

- Video individuati: 468
- Contenuti processati semanticamente: 200
- STUDIATO / integrati o deduplicati: 194
- ESCLUSO dalla dottrina attiva: 6
- Da processare: 268
- Corpus completo: NO
- Batch tecnico 176–200: 25/25 utilizzabili
- Elaborazione semantica 176–200: 25/25
- Transcript mancanti nel batch: 0
- Fallback ASR nel batch: 0
- Errori finali tecnici: 0
- Blocchi semantici aperti: 0

## Rendimento marginale batch 176–200

- Video con conoscenza incrementale integrata: **8/25 (32%)**
- Video studiati ma deduplicati/non incrementali: **17/25 (68%)**
- Shorts 176–184: **0/9 incrementali**
- Video 185–200: **8/16 incrementali (50%)**

Il dato è un campione operativo, non una regola universale. Al checkpoint 200 va usato per valutare una priorità differenziata dei contenuti 201–468 senza saltare la revisione semantica di alcun video.

## Workflow attivo — v1.1

- CODEX / strumenti locali: acquisizione tecnica a batch e sincronizzazione meccanica.
- CHATGPT: revisione semantica e fasi 8–13.
- CLAUDE CODE: FASE 14 ogni 25; FASE 14 + 15 ogni 50.

## Checkpoint

- Ultimo refactor KB completato: **200**
- Ultimo audit tassonomia completato: **200**
- Refactor KB dovuto: **225 — FASE 14**
- Audit tassonomia dovuto: **250 — FASE 14 + FASE 15**
- Checkpoint Claude richiesto ora: **NO**
- Documento checkpoint corrente: `reviews/CHECKPOINT_200.md` (report definitivo)
- Classificazione strategica residui: `reviews/RESIDUAL_CLASSIFICATION_201-468.md`

## Agente richiesto

**CODEX**

## Next Action

Acquisizione tecnica del batch **201–225** (fase 7: transcript, eventuale fallback ASR, keyframe candidati dove segnalato). Nessuno dei 25 transcript di questa porzione della coda è presente in `sources/transcripts/`.

Primo contenuto non completato: **201 — `vD7zMl6YXzs`** — *Marketing Campaigns: Why Cost Per Lead Is Not Enough (And Where You Should Really Invest)*, categoria preliminare `05_acquisizione`.

Al termine dell'acquisizione, restituire il controllo a ChatGPT via `STATUS.md` secondo `system/HANDOFFS.md` (Codex → ChatGPT), indicando il numero di video acquisiti e il primo non ancora studiato.

Per la revisione semantica dei contenuti 201–225 (a cura di ChatGPT), consultare `reviews/RESIDUAL_CLASSIFICATION_201-468.md` per la profondità suggerita (classe A/B/C) di ciascun contenuto — resta comunque obbligatorio processare ogni video e assegnargli stato finale.

## Validazione e blocchi

- Checkpoint 200 (FASE 14 + FASE 15) completato da Claude Code su `main` allo SHA di partenza `a8480238816ec8766fa96ad10c868ac9a2fc026c`.
- FASE 14: nessuna modifica strutturale alla KB necessaria (decisione documentata in `reviews/CHECKPOINT_200.md`).
- FASE 15: nessuna modifica alla tassonomia a 11 categorie (decisione documentata in `reviews/CHECKPOINT_200.md`).
- Validator locale: **841 segnalazioni prima e dopo il checkpoint** (diff vuoto) — tutte storiche/baseline (836 disallineamenti noti di `QUEUE.md`, 3 warning su file frozen dovuti al confronto con il tag `v1.0` invece di `v1.1`, 2 warning di nomenclatura contatori in `STATUS.md`). Nessuna nuova anomalia introdotta. Dettaglio completo in `reviews/CHECKPOINT_200.md`.
- File frozen non modificati in questo checkpoint.
- Nessun contenuto 201+ studiato, acquisito o processato semanticamente in questo checkpoint.
- Asset tecnici 201–225: **assenti**, confermato per tutti i 25 id della porzione di coda corrispondente.
