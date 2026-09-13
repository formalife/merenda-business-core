# PROJECT STATUS

## Stato generale

ACTIVE — fasi 1–6 complete; primi 100 contenuti processati semanticamente; checkpoint 100 (fase 14 + fase 15) completato.

## Fase corrente

**Post-checkpoint 100 — in attesa di acquisizione tecnica del batch 101–125.**

## Corpus

- Video individuati: 468
- Contenuti processati: 100
- STUDIATO / integrati nella KB: 96
- ESCLUSO dalla dottrina attiva: 4
- Da processare: 368
- Corpus completo: NO

## Workflow attivo — v1.1

- CODEX / script locale: acquisizione tecnica a batch.
- CHATGPT: revisione semantica e fasi 8–13.
- CLAUDE CODE: fase 14 ogni 25; fase 14 + 15 ogni 50.

## Checkpoint

- Ultimo refactor KB completato: 100
- Ultimo audit tassonomia completato: 100
- Prossimo checkpoint: 125 (fase 14)
- Checkpoint Claude richiesto ora: NO

Esito dettagliato: `reviews/CHECKPOINT_100.md`.

## Esito sintetico checkpoint 100

- FASE 14: KB già ben architettata; aggiunti solo 3 collegamenti incrociati mancanti in `01_mercato`/`05_acquisizione`. Nessun file creato/eliminato/fuso/rinominato.
- FASE 15: tassonomia a 11 categorie confermata adeguata. 11 contenuti 101+ riclassificati da titolo (caso aziendale nominato) verso `10_casi_studio` e riordinati in coda a quella sezione. Corretto un disallineamento pregresso tra `sources/catalog.json` e `sources/queue/QUEUE.md` su 36 contenuti 101+ (categoria non sincronizzata dal checkpoint 50). Nessun contenuto 101+ visionato o marcato STUDIATO; nessuna modifica ai primi 100.

## Agente richiesto

**CODEX**

## Next Action

Acquisire a batch gli asset tecnici (metadata, transcript, markdown normalizzato, keyframe candidati quando utili) per i video 101–125 della queue post-audit, tutti in `04_marketing`:

`zZFg2oM208w`, `kmtvBlfL25I`, `MuHs2UrVGEg`, `J7WZ-gzN3zg`, `68H6aOPXITg`, `FIOKn72b_Bk`, `4beA9XR2tHE`, `Qlk15QgvaK4`, `3oDGQ4SImC8`, `tcOwLBoPC-8`, `2R2u-O-uoYg`, `k8d8CYjp3u8`, `qQ8htL2fA9o`, `5q1QvjuXX_w`, `AsD7LxX-n2I`, `lQd9lhLJMXk`, `Aq0dxMu8AqU`, `txFb7PkaVAw`, `dYc5k5tRZx0`, `gy-80USEC8g`, `-GsWbIj44dQ`, `8bQmDJJTEqs`, `nJuSh2u1dOE`, `_zqwnqzzv-4`, `0qipJSkZxmg`.

Al termine del batch, impostare `Agente richiesto: CHATGPT` per l'elaborazione semantica (fasi 8–13), partendo da `zZFg2oM208w`.

## Primo pendente

`zZFg2oM208w` — *Come Fare Marketing: 3 Passi Chiave Per Trovare Clienti Top* — `04_marketing`.

Asset tecnici 101–125: verificati assenti in `sources/transcripts/`. Non acquisiti durante il checkpoint 100.

## Blocchi

Nessun blocco semantico aperto sui primi 100 contenuti.
