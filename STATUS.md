# PROJECT STATUS

## Stato generale

ACTIVE — fasi 1–6 complete; contenuti 1–175 processati semanticamente; refactor KB checkpoint 175 (FASE 14) completato; corpus ancora incompleto.

## Fase corrente

**Checkpoint 175 completato.** FASE 14 eseguita (rilettura globale della KB, verifica integrazioni batch 151–175, validazione tecnica). FASE 15 non dovuta ed esplicitamente non eseguita. È dovuta ora l'acquisizione tecnica del batch 176–200.

## Corpus

- Video individuati: 468
- Contenuti processati semanticamente: 175
- STUDIATO / integrati nella KB: 169
- ESCLUSO dalla dottrina attiva: 6
- Da processare: 293
- Corpus completo: NO
- Batch tecnico 151–175: 25/25 utilizzabili
- Elaborazione semantica 151–175: 25/25 completata
- Fallback ASR nel batch 151–175: 0
- Blocchi semantici aperti nel batch: 0

## Workflow attivo — v1.1

- CODEX / strumenti locali: acquisizione tecnica a batch e sincronizzazione meccanica.
- CHATGPT: revisione semantica e fasi 8–13.
- CLAUDE CODE: FASE 14 ogni 25; FASE 14 + 15 ogni 50.

## Checkpoint

- Ultimo refactor KB completato: **175**
- Prossimo refactor KB dovuto: **200**
- Ultimo audit tassonomia completato: 150
- Prossimo audit tassonomia: **200**
- Checkpoint Claude richiesto ora: **NO**
- Documento checkpoint corrente: `reviews/CHECKPOINT_175.md`
- Checkpoint precedente: `reviews/CHECKPOINT_150.md`

## FASE 14 — esito checkpoint 175

- Rilettura integrale di `merenda/`: 39 file (INDEX + 11 README + 27 documenti).
- Le sette integrazioni del batch 151–175 verificate singolarmente: tutte correttamente fuse, nessuna duplicazione.
- Nessun problema strutturale trovato: 0 link rotti, 0 anchor non risolti, 0 file orfani, nessuna contraddizione attiva, Formalife assente.
- Nessun merge/split/ristrutturazione necessario: la KB era già in buono stato dopo il merge semantico del batch.
- Validator tecnico: 841 segnalazioni, invariato rispetto alla baseline nota (836 ordine/stato queue, 3 frozen file storici, 2 contatori STATUS non riconosciuti). Nessuna nuova anomalia.
- Dettagli completi: `reviews/CHECKPOINT_175.md`.

## Agente richiesto

**CODEX**

## Next Action

Acquisizione tecnica del batch **176–200** (metadata, transcript, versione Markdown normalizzata, keyframe candidati quando utili). Nessun asset tecnico per 176–200 risulta già presente in `sources/transcripts/`.

Il primo contenuto pendente della coda è `176 — aQ5V7845jX4` (categoria preliminare `10_casi_studio`, da confermare in fase di ingestione).

Dopo l'acquisizione, restituire il controllo a **CHATGPT** per l'elaborazione semantica (fasi 8–13) del batch 176–200.

## Validazione e blocchi

- Nessun blocco semantico residuo dal batch 151–175.
- Nessun fallback ASR richiesto nel batch.
- Nessun contenuto 176+ acquisito.
- Baseline validator tecnica confermata invariata al checkpoint 175: 841 segnalazioni (836 disallineamenti d'ordine/stato in `sources/queue/QUEUE.md`, 3 divergenze storiche dei frozen file rispetto al tag v1.0, 2 etichette STATUS non riconosciute dal validator).
- Nessuna modifica ai file congelati in questo checkpoint.
