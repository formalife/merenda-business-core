# Script operativi

Eseguire dalla radice con Python 3. Dipendenze esterne: `yt-dlp` per YouTube, `ffmpeg` per keyframe locali. Nessuna dipendenza Python aggiuntiva per elaborazione e validazione offline.

- `python3 scripts/scan_channel.py`: scarica le schede pubbliche videos, shorts e streams del solo canale ufficiale. Interrompe in caso di errore, senza pubblicare un catalogo parziale. I dati grezzi sono in `work/channel-*.json`.
- `python3 scripts/scan_channel.py --from-cache`: rigenera catalogo Markdown e queue dai dati già scaricati. Preserva stati, note e ordine esistente; la classificazione è preliminare sul titolo. `sources/catalog.json` è il supporto operativo delle due viste Markdown: modificare lì stato/note, poi rigenerare. Non modifica `STATUS.md` automaticamente.
- `python3 scripts/ingest_video.py`: mostra il primo video non completato. `--acquire` acquisisce sottotitoli italiani e metadati, poi normalizza il testo. Non marca mai un video studiato e non esegue il merge al posto dell'agente.
- `python3 scripts/transcript.py VIDEO_ID`: converte un JSON3 italiano già acquisito in Markdown temporizzato. Rifiuta metadati di altri canali; normalizza gli spazi senza inventare punteggiatura o correzioni. Non sovrascrivere un transcript revisionato senza conservarne prima le modifiche.
- `python3 scripts/extract_keyframes.py video.mp4 --seconds 1165 3452 4540 4695 4865 --output work/keyframes`: estrae solo i frame selezionati da un video locale. Rifiuta sovrascritture. Analisi visuale da eseguire sui file prodotti.
- `python3 scripts/validate_project.py`: confronta i file congelati con `merenda-system-v1.0`, controlla catalogo, queue, routing, collegamenti, separazione della KB e contatori di stato. Non certifica la revisione semantica.

I metadati archiviati sono ridotti ai campi utili, senza URL multimediali firmati e temporanei. Un nuovo download può ricreare il JSON completo; mantenere nell'archivio durevole solo dati operativi necessari. La lista `sources/queue/next-batch.txt` registra il batch già acquisito, non è la queue canonica.

La chiusura delle fasi 7–13 richiede lettura integrale, correzioni ragionevoli, gestione delle incomprensioni, eventuali visuali, merge e aggiornamento dello stato. Il primo checkpoint Claude scatta a 25 video realmente completati.
