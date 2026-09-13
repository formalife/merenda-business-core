# PROJECT STATUS

## Stato generale

ACTIVE — fasi 1–6 complete; primi 125 contenuti processati semanticamente; checkpoint 125 e FASE 14 completati; asset tecnici del batch 126–150 integrati su main.

## Fase corrente

**Elaborazione semantica del batch 126–150 — 0/25 completati.**

## Corpus

- Video individuati: 468
- Contenuti processati semanticamente: 125
- STUDIATO / integrati nella KB: 121
- ESCLUSO dalla dottrina attiva: 4
- Da processare: 343
- Corpus completo: NO
- Asset tecnici 101–125: ACQUISITI 25/25
- Elaborazione semantica 101–125: 25/25 completati
- Batch tecnico 126–150: 25/25 tentati
- Asset 126–150: 22 ACQUIRED, 3 NO_IT_TRANSCRIPT, 0 ERROR, 0 PENDING
- Elaborazione semantica 126–150: 0/25 completati

## Workflow attivo — v1.1

- CODEX / script locale: acquisizione tecnica a batch e sincronizzazione meccanica.
- CHATGPT: revisione semantica e fasi 8–13.
- CLAUDE CODE: fase 14 ogni 25; fase 14 + 15 ogni 50.

## Checkpoint

- Ultimo refactor KB completato: 125
- Ultimo audit tassonomia completato: 100
- Prossimo checkpoint: 150 (FASE 14 + FASE 15)
- Checkpoint Claude richiesto ora: NO

Documento precedente: `reviews/CHECKPOINT_125.md`.

## Acquisizione tecnica 126–150

Branch tecnico integrato su main: `acquisition-126-150`.

- base: `0ee98de07664c9cf2a74c9dc90facea795293de2`
- head tecnico: `751003eb318f2d15b4a64238cfe9d175de4580d9`
- 25/25 tentati
- 22 ACQUIRED
- 3 NO_IT_TRANSCRIPT
- 0 ERROR
- 0 PENDING
- nessun video marcato STUDIATO/ESCLUSO durante l'acquisizione
- KB, queue canonica, catalogo, VIDEO_INDEX, reviews, file congelati e script invariati nel branch tecnico

Contenuti senza transcript italiano:
- `jcVKVKvy78k` — posizione 143
- `joY6sigynis` — posizione 148
- `ijVoIMF_gn8` — posizione 149

Per questi tre sono disponibili i metadata, ma non un transcript utilizzabile. Non inventare contenuti: servirà fallback audio/trascrizione tecnica prima della loro elaborazione semantica.

## Agente richiesto

**CHATGPT**

## Next Action

Procedere semanticamente in ordine di queue con le fasi 8–13 a partire dal contenuto 126:

`dwfknCGx8UI` — *MARKETING | Diventare il punto di riferimento per il tuo Settore [Jay Abraham]* — `04_marketing`.

Per ogni contenuto:
1. revisione/correzione ragionevole del transcript;
2. segnalazione di sole incomprensioni sostanziali;
3. verifica dell'eventuale necessità di analisi visuale/keyframe;
4. estrazione delle conoscenze importanti;
5. routing minimo nella KB;
6. MERGE, NON APPEND;
7. aggiornamento di stato video, queue, catalogo/VIDEO_INDEX e STATUS secondo workflow.

Procedere in ordine fino al primo contenuto senza transcript utilizzabile. Al raggiungimento di `jcVKVKvy78k` (143), se il transcript resta assente, passare a CODEX per un fallback audio/trascrizione locale prima di proseguire.

Non saltare contenuti della queue per completare quelli successivi.

## Primo pendente

`dwfknCGx8UI` — *MARKETING | Diventare il punto di riferimento per il tuo Settore [Jay Abraham]* — `04_marketing` — posizione 126.

Asset tecnici disponibili in `sources/transcripts/`.

## Validazione e blocchi

Le anomalie note di `scripts/validate_project.py` restano quelle preesistenti già documentate: confronto file congelati vs tag v1.0 e disallineamenti d'ordine tra catalogo, VIDEO_INDEX e queue. Nessuna nuova anomalia tecnica è stata rilevata nell'integrazione del batch.

Blocco previsto alla posizione 143: transcript italiano assente per `jcVKVKvy78k`.
