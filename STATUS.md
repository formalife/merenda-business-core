# PROJECT STATUS

## Stato generale

ACTIVE — fasi 1–6 complete; primi 125 contenuti processati semanticamente; checkpoint 125 e FASE 14 completati; asset tecnici del batch 126–150 integrati su main.

## Fase corrente

**Elaborazione semantica del batch 126–150 — 17/25 completati; BLOCCATA al contenuto 143 per transcript assente.**

## Corpus

- Video individuati: 468
- Contenuti processati semanticamente: 142
- STUDIATO / integrati nella KB: 136
- ESCLUSO dalla dottrina attiva: 6
- Da processare: 326
- Corpus completo: NO
- Asset tecnici 101–125: ACQUISITI 25/25
- Elaborazione semantica 101–125: 25/25 completati
- Batch tecnico 126–150: 25/25 tentati
- Asset 126–150: 22 ACQUIRED, 3 NO_IT_TRANSCRIPT, 0 ERROR, 0 PENDING
- Elaborazione semantica 126–150: 17/25 completati

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

**CODEX**

## Next Action

Il prossimo contenuto canonico è `jcVKVKvy78k` (posizione 143), ma non dispone di transcript italiano utilizzabile.

Passare a CODEX per un fallback tecnico locale di trascrizione audio. Per evitare ulteriori interruzioni nello stesso batch, il fallback può essere preparato nello stesso intervento anche per gli altri due contenuti già noti senza transcript:

- `jcVKVKvy78k` — posizione 143
- `joY6sigynis` — posizione 148
- `ijVoIMF_gn8` — posizione 149

L'acquisizione/trascrizione tecnica di 148 e 149 in anticipo non modifica l'ordine semantico: ChatGPT dovrà comunque riprendere dal 143 e procedere in ordine.

Non marcare questi video STUDIATO o ESCLUSO durante il fallback tecnico. Non modificare KB, queue canonica, categorie o review semantiche.

## Primo pendente

`jcVKVKvy78k` — *Le Tattiche Segrete dei Samurai Italiani applicate al Marketing* — `04_marketing` — posizione 143.

Metadata disponibili; transcript italiano assente.

## Validazione e blocchi

Le anomalie note di `scripts/validate_project.py` restano quelle preesistenti già documentate: confronto file congelati vs tag v1.0 e disallineamenti d'ordine tra catalogo, VIDEO_INDEX e queue. Nessuna nuova anomalia tecnica è stata rilevata nell'integrazione del batch.

Blocco previsto alla posizione 143: transcript italiano assente per `jcVKVKvy78k`.
