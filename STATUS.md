# PROJECT STATUS

## Stato generale

ACTIVE — fasi 1–6 complete; ingestion loop in corso.

## Fase corrente

FASE 7 — prossimo video `27Bt3nswSyg`.

Completati i primi sette video della queue. Transcript letti, revisioni individuali e merge in nove documenti KB collegati. Analisi visuale selettiva effettuata dove utile; file congelati invariati.

## Corpus

- Video individuati: 468
- Video completati: 7
- Video rimanenti: 461
- Corpus completo: NO

296 video, 109 Shorts, 63 dirette; nessun duplicato tra le tre schede. Scansione del 2026-09-12. Video privati, eliminati e non in elenco non censibili dalle schede pubbliche.

Acquisiti metadati per 25 video e sottotitoli disponibili in anticipo: `sources/transcripts/ACQUISITION.md`. I primi sette transcript della queue sono stati letti. Le acquisizioni anticipate non contano come completamenti e non cambiano l'ordine canonico della queue.

## Checkpoint

- Ultimo refactor KB: nessuno
- Prossimo refactor KB: 25 video completati
- Ultimo audit tassonomia: nessuno
- Prossimo audit tassonomia: 50 video completati
- Checkpoint Claude richiesto: NO

## Agente richiesto

CODEX

## Next Action

Acquisire e processare `27Bt3nswSyg`, primo pendente in `sources/queue/QUEUE.md`, poi continuare le fasi 7–13 fino a 25 completati. Allora checkpoint Claude fase 14. Avvio: `python3 scripts/ingest_video.py --acquire`.

Aggiornare stati in `sources/catalog.json`, rigenerare viste con `python3 scripts/scan_channel.py --from-cache`, aggiornare STATUS ed eseguire `python3 scripts/validate_project.py`.

## Blocchi / intervento umano

Nessun blocco tecnico: HTTP 403 del vecchio downloader risolto usando yt-dlp 2026.08.19 in `work/tmp/yt-dlp-runtime`; lo script di acquisizione lo seleziona automaticamente quando presente.

DA VERIFICARE MANUALMENTE, locale e non bloccante: attribuzioni cronologiche della seconda mappa Disney a 77:35–81:22 nel primo corso. La registrazione precede la pubblicazione del 2022; data esatta dell'evento non verificata. Dettagli in `sources/transcripts/iR0e4AgmAGE.review.md`. Altri dubbi locali documentati nelle revisioni: nome del sistema di soddisfazione in `GesepBOY5E8`, voce contabile dei 40.000 € in `hYqP4mBG22o`, organico dello studio in `m-xKoXkdRak`. Non consolidati fatti incerti.

## Verifica operativa

Script di scansione, acquisizione, conversione, keyframe e validazione implementati. Validazione offline superata su 468 video; confronta file congelati con `merenda-system-v1.0`, routing, catalogo, queue e contatori. Nessuna modifica all'architettura di governo.
