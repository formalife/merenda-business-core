# PROJECT STATUS

## Stato generale

ACTIVE — fasi 1–6 complete; primi 100 contenuti processati semanticamente; checkpoint 100 (fase 14 + fase 15) completato; asset tecnici 101–125 acquisiti e integrati su main.

## Fase corrente

**Elaborazione semantica del batch 101–125 — 18/25 completati; continuare dal contenuto 119.**

## Corpus

- Video individuati: 468
- Contenuti processati semanticamente: 118
- STUDIATO / integrati nella KB: 114
- ESCLUSO dalla dottrina attiva: 4
- Da processare: 350
- Corpus completo: NO
- Asset tecnici 101–125: ACQUISITI 25/25
- Elaborazione semantica 101–125: 18/25 completati

## Workflow attivo — v1.1

- CODEX / script locale: acquisizione tecnica a batch.
- CHATGPT: revisione semantica e fasi 8–13.
- CLAUDE CODE: fase 14 ogni 25; fase 14 + 15 ogni 50.

## Checkpoint

- Ultimo refactor KB completato: 100
- Ultimo audit tassonomia completato: 100
- Prossimo checkpoint: 125 (fase 14)
- Checkpoint Claude richiesto ora: NO

Esito dettagliato checkpoint precedente: `reviews/CHECKPOINT_100.md`.

## Acquisizione tecnica 101–125

Branch tecnico completato: `acquisition-101-125`.

- base: `181ae92b097d56cc3681e13eb9f38ab27e9d51da`
- head tecnico: `7989d84ff84bd6da9774c379fc60341800c7937e`
- 25/25 video ACQUIRED
- 0 NO_IT_TRANSCRIPT
- 0 ERROR
- 0 PENDING
- asset creati: metadata JSON, sottotitoli JSON3 `it-orig` + `it`, Markdown normalizzati e temporizzati
- nessun keyframe necessario in acquisizione
- nessun video marcato STUDIATO durante l'acquisizione
- KB, queue canonica, catalogo, VIDEO_INDEX, review e file congelati invariati nel branch tecnico

Gli asset tecnici sono stati integrati su `main` preservando i 25 commit di acquisizione.

## Agente richiesto

**CHATGPT**

## Next Action

Continuare semanticamente, in ordine di queue, dai contenuti 119–125 eseguendo per ciascuno le fasi 8–13:

1. revisione/correzione ragionevole del transcript;
2. segnalazione di sole incomprensioni sostanziali;
3. verifica dell'eventuale necessità di analisi visuale/keyframe;
4. estrazione delle conoscenze importanti;
5. routing minimo nella KB;
6. MERGE, NON APPEND nella KB;
7. aggiornamento di stato video, queue, catalogo/VIDEO_INDEX se previsto dal workflow e `STATUS.md`;
8. passaggio al successivo finché scatta il checkpoint 125.

Batch canonico:

`zZFg2oM208w`, `kmtvBlfL25I`, `MuHs2UrVGEg`, `J7WZ-gzN3zg`, `68H6aOPXITg`, `FIOKn72b_Bk`, `4beA9XR2tHE`, `Qlk15QgvaK4`, `3oDGQ4SImC8`, `tcOwLBoPC-8`, `2R2u-O-uoYg`, `k8d8CYjp3u8`, `qQ8htL2fA9o`, `5q1QvjuXX_w`, `AsD7LxX-n2I`, `lQd9lhLJMXk`, `Aq0dxMu8AqU`, `txFb7PkaVAw`, `dYc5k5tRZx0`, `gy-80USEC8g`, `-GsWbIj44dQ`, `8bQmDJJTEqs`, `nJuSh2u1dOE`, `_zqwnqzzv-4`, `0qipJSkZxmg`.

Al completamento semantico del 125° contenuto:

- aggiornare i contatori;
- creare/aggiornare il checkpoint 125 secondo il sistema;
- impostare `Agente richiesto: CLAUDE CODE`;
- richiedere **solo FASE 14** (checkpoint 125).

## Primo pendente

`dYc5k5tRZx0` — *Marketing a Risposta diretta | Come fare PROMO efficaci [Parte 2]* — `04_marketing`.

Asset tecnici disponibili in `sources/transcripts/`.

## Blocchi

Nessun blocco aperto.
