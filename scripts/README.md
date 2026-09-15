# Script operativi

## Acquisizione Merenda: stato finale

L'acquisizione generalista è chiusa. `sources/queue/ACQUISITION_CLOSED.md` è il lock operativo: finché esiste, `scripts/ingest_video.py` termina senza selezionare né acquisire video. `sources/queue/next-batch.txt` deve restare vuoto.

Per riaprire l'acquisizione servono: decisione esplicita dell'utente, gap nominabile, aggiornamento di `STATUS.md`, rimozione deliberata del lock e definizione di un batch mirato.

Eseguire dalla radice con Python 3. Dipendenze esterne: `yt-dlp` per YouTube, `ffmpeg` per keyframe locali. Nessuna dipendenza Python aggiuntiva per elaborazione e validazione offline.

- `python3 scripts/scan_channel.py`: scarica le schede pubbliche videos, shorts e streams del solo canale ufficiale. Interrompe in caso di errore, senza pubblicare un catalogo parziale. I dati grezzi sono in `work/channel-*.json`.
- `python3 scripts/scan_channel.py --from-cache`: rigenera catalogo Markdown e queue dai dati già scaricati. Preserva stati, note e ordine esistente; la classificazione è preliminare sul titolo. `sources/catalog.json` è il supporto operativo delle due viste Markdown: modificare lì stato/note, poi rigenerare. Non modifica `STATUS.md` automaticamente.
- `python3 scripts/ingest_video.py`: mostra il primo video non completato. `--acquire` acquisisce sottotitoli italiani e metadati, poi normalizza il testo. Non marca mai un video studiato e non esegue il merge al posto dell'agente.
- `python3 scripts/transcript.py VIDEO_ID`: converte un JSON3 italiano già acquisito in Markdown temporizzato. Rifiuta metadati di altri canali; normalizza gli spazi senza inventare punteggiatura o correzioni. Non sovrascrivere un transcript revisionato senza conservarne prima le modifiche.
- `python3 scripts/extract_keyframes.py video.mp4 --seconds 1165 3452 4540 4695 4865 --output work/keyframes`: estrae solo i frame selezionati da un video locale. Rifiuta sovrascritture. Analisi visuale da eseguire sui file prodotti.
- `python3 scripts/validate_project.py`: confronta i file congelati con `merenda-system-v1.0`, controlla catalogo, queue, routing, collegamenti, separazione della KB e contatori di stato. Non certifica la revisione semantica.

I metadati archiviati sono ridotti ai campi utili, senza URL multimediali firmati e temporanei. Un nuovo download può ricreare il JSON completo; mantenere nell'archivio durevole solo dati operativi necessari. La lista `sources/queue/next-batch.txt` è vuota quando l'acquisizione è chiusa; durante una riapertura mirata può registrare il batch autorizzato, ma non è mai la queue canonica.

La chiusura delle fasi 7–13 richiede lettura integrale, correzioni ragionevoli, gestione delle incomprensioni, eventuali visuali, merge e aggiornamento dello stato. Il primo checkpoint Claude scatta a 25 video realmente completati.


## Acquisizione monitorata e persistente

Per acquisire un batch mostrando avanzamento video per video e salvando ogni risultato su GitHub:

```bash
python3 scripts/ingest_video.py --acquire --count 25 --commit-each --push-each
```

Durante l'esecuzione il terminale mostra:

```text
[1/25] VIDEO_ID — Titolo
[1/25] ACQUIRED: Metadata + transcript Markdown disponibili.
...
```

Lo stato live viene scritto in `sources/queue/acquisition-progress.md` con valori:

- `PENDING`
- `ACQUIRED`
- `NO_IT_TRANSCRIPT`
- `ERROR`

Con `--commit-each --push-each`, dopo ogni video vengono eseguiti commit e push separati. Se il processo si interrompe, tutto ciò che è già stato acquisito rimane salvato su GitHub.

Per continuare anche quando un singolo video fallisce:

```bash
python3 scripts/ingest_video.py --acquire --count 25 --commit-each --push-each --continue-on-error
```

Nessuna di queste opzioni marca un video come `STUDIATO`: il completamento semantico resta responsabilità della fase 8–13.
