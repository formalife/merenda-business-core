# PROJECT STATUS

## Stato generale

ACTIVE — fasi 1–6 complete; primi 125 contenuti processati semanticamente; checkpoint 125 e FASE 14 completati; asset tecnici del batch 126–150 integrati su main.

## Fase corrente

**Elaborazione semantica del batch 126–150 — 18/25 completati; prossimo contenuto canonico: 144 `Sjmvw03Oxqc`.**

## Corpus

- Video individuati: 468
- Contenuti processati semanticamente: 143
- STUDIATO / integrati nella KB: 137
- ESCLUSO dalla dottrina attiva: 6
- Da processare: 325
- Corpus completo: NO
- Asset tecnici 101–125: ACQUISITI 25/25
- Elaborazione semantica 101–125: 25/25 completati
- Batch tecnico 126–150: 25/25 tentati
- Asset 126–150 utilizzabili: 25/25 — 22 acquisiti da YouTube + 3 fallback ASR locali
- Elaborazione semantica 126–150: 18/25 completati

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

Fallback ASR locale completato e integrato su `main` per i tre contenuti privi di sottotitoli italiani:
- `jcVKVKvy78k` — posizione 143
- `joY6sigynis` — posizione 148
- `ijVoIMF_gn8` — posizione 149

I file `.md` e `.asr.json` sono disponibili per la revisione semantica. Il contenuto 143 è stato revisionato e marcato STUDIATO.

## Agente richiesto

**CHATGPT**

## Next Action

Proseguire con CHATGPT in ordine canonico dal contenuto 144:

- `Sjmvw03Oxqc` — *Spot Anni '80: Il MARKETING della nostra infanzia!*

Non saltare 144–147 anche se i fallback ASR di 148 e 149 sono già disponibili. Dopo il completamento semantico del 150, fermarsi e passare a CLAUDE CODE per **FASE 14 + FASE 15**. Non acquisire 151–175 prima della conclusione della FASE 15.

## Primo pendente

`Sjmvw03Oxqc` — *Spot Anni '80: Il MARKETING della nostra infanzia!* — posizione 144.

Transcript italiano disponibile; pronto per revisione semantica.

## Validazione e blocchi

Le anomalie note di `scripts/validate_project.py` restano quelle preesistenti già documentate: confronto file congelati vs tag v1.0 e disallineamenti d'ordine tra catalogo, VIDEO_INDEX e queue. Nessuna nuova anomalia tecnica è stata rilevata nell'integrazione del batch.

Il blocco alla posizione 143 è risolto tramite fallback ASR locale. Restano soltanto le anomalie preesistenti già documentate.
