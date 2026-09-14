# PROJECT STATUS

## Stato generale

ACTIVE — fasi 1–6 complete; contenuti 1–200 processati semanticamente; checkpoint 200 (FASE 14 + FASE 15) completato. Corpus ancora incompleto.

## Fase corrente

FASE 7 — batch tecnico **201–225 completato**, 25/25 acquisiti e utilizzabili. Revisione semantica del batch non iniziata. Branch `acquisition-201-225`, base `6304bdc7d3ae4d3fb6d2a22e94f87082eb727bc3`.

## Corpus

- Video individuati: 468
- Contenuti processati semanticamente: 200
- STUDIATO / integrati o deduplicati: 194
- ESCLUSO dalla dottrina attiva: 6
- Da processare: 268
- Corpus completo: NO
- Batch tecnico 201–225: 25/25 utilizzabili
- Elaborazione semantica 201–225: 0/25
- Transcript mancanti nel batch: 0
- Fallback ASR nel batch: 0
- Errori finali tecnici: 0
- Pending tecnici: 0

## Workflow attivo — v1.1

- CODEX: acquisizione tecnica e supporto meccanico.
- CHATGPT: revisione semantica e fasi 8–13.
- CLAUDE CODE: FASE 14 ogni 25; FASE 14 + 15 ogni 50.
- Nessuna modifica al workflow frozen; classificazione A/B/C non applicata all’acquisizione.

## Checkpoint

- Ultimo refactor KB completato: **200**
- Ultimo audit tassonomia completato: **200**
- Refactor KB dovuto dopo completamento semantico: **225 — FASE 14**
- Audit tassonomia dovuto: **250 — FASE 14 + FASE 15**
- Checkpoint Claude richiesto ora: **NO**
- Report checkpoint corrente: `reviews/CHECKPOINT_200.md`

## Agente richiesto

**CHATGPT**

## Next Action

Revisione semantica dei contenuti **201–225** sugli asset acquisiti. Primo contenuto: **201 — `vD7zMl6YXzs`** — *Marketing Campaigns: Why Cost Per Lead Is Not Enough (And Where You Should Really Invest)*, categoria preliminare `05_acquisizione`.

Report tecnico completo: `sources/queue/acquisition-progress.md`. 24 tracce automatiche italiane originali, 1 manuale italiana, 12 keyframe candidati per sei video. Acquisizione persistita in 25 commit individuali più handoff globale. Nessun merge su main, nessun contenuto 226+ acquisito.

## Validazione e limiti

- Validator: **841 warning**, identici alla baseline; zero nuove anomalie. I 836 disallineamenti storici riguardano VIDEO_INDEX e QUEUE; gli altri sono 3 divergenze frozen rispetto a v1.0 e 2 warning di nomenclatura contatori STATUS.
- Frozen, KB, catalogo, VIDEO_INDEX e QUEUE invariati. Nessun `.review.md` creato. Semantica ancora 200.
- Metadata/canale e corrispondenza JSON3–Markdown verificati per tutti i 25; copertura intervallo almeno 95,94%.
- **218 — `JQXoKKwneBQ`:** transcript termina a 4.384,610 s, durata metadata 4.259 s. Testo disponibile e coerente col JSON3; possibile disallineamento con il montaggio corrente. ChatGPT deve verificare timestamp/visuali prima di usarli come evidenza precisa. Nessuna correzione temporale inventata.
- Blocchi iniziali del sandbox risolti con esecuzione autorizzata; nessun asset o commit prodotto su main. Dettaglio nel report tecnico.
- `git diff --check` superato.
