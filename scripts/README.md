# Script operativi

## Acquisizione YouTube storica: stato finale

L'acquisizione generalista del corpus YouTube è chiusa. sources/queue/ACQUISITION_CLOSED.md è il lock operativo: finché esiste, scripts/ingest_video.py termina senza selezionare né acquisire video. sources/queue/next-batch.txt deve restare vuoto.

Per riaprire i residui YouTube servono: decisione esplicita dell'utente, gap nominabile, aggiornamento di STATUS.md, rimozione deliberata del lock e definizione di un micro-batch mirato.

Il lock non riguarda nuove fonti Merenda source-agnostic registrate in sources/merenda-sources/.

## Nuove fonti Merenda

Non esiste volutamente un ingestor universale. Video, audio, articoli, PDF, newsletter, interviste e altri materiali richiedono acquisizioni tecniche differenti.

Per ogni nuova fonte:

- assegnare un ID FM-SRC-NNNN;
- registrarla in sources/merenda-sources/catalog.json;
- conservare l'originale o un riferimento stabile quando appropriato;
- creare un contenuto normalizzato analizzabile;
- creare la review dopo la revisione semantica;
- aggiornare STATUS.md;
- eseguire python3 scripts/validate_project.py.

La convenzione completa è descritta in sources/merenda-sources/README.md.

## Script legacy video

Eseguire dalla radice con Python 3. Dipendenze esterne: yt-dlp per YouTube, ffmpeg per keyframe locali.

- python3 scripts/scan_channel.py: scansione del solo canale ufficiale storico.
- python3 scripts/scan_channel.py --from-cache: rigenera le viste del corpus video storico.
- python3 scripts/ingest_video.py: bloccato dal lock finché la fase video resta chiusa.
- python3 scripts/transcript.py VIDEO_ID: converte JSON3 italiano già acquisito in Markdown temporizzato.
- python3 scripts/extract_keyframes.py video.mp4 --seconds ... --output ...: estrae frame selezionati.
- python3 scripts/validate_project.py: controlla frozen, corpus video storico, lock, routing, link, contatori e nuovo registry source-agnostic.

I metadati archiviati devono restare ridotti ai campi utili. Evitare URL multimediali firmati e temporanei quando non servono come evidenza durevole.

## Acquisizione video mirata eventualmente riaperta

Solo dopo autorizzazione esplicita e rimozione deliberata del lock, i vecchi comandi di acquisizione monitorata possono essere usati per un micro-batch specifico. Nessuna opzione di acquisizione marca automaticamente un video come STUDIATO.
