# Acquisition Progress

- Branch: `acquisition-201-225`
- Base SHA: `6304bdc7d3ae4d3fb6d2a22e94f87082eb727bc3`
- Batch canonico: **201–225**, esattamente 25 ID nell’ordine richiesto.
- Tentati: **25/25**; acquisiti: **25/25 ACQUIRED**; transcript utilizzabili: **25/25**, con limite temporale documentato per il 218.
- NO_IT_TRANSCRIPT / transcript mancanti: **0**; fallback ASR: **0**; errori finali: **0**; pending: **0**.
- Tracce: **24 automatiche italiane originali + 1 manuale italiana** (217).
- Commit: **25 individuali + 1 globale finale di handoff**, tutti sul branch tecnico.
- Semantica invariata: **200 processati / 194 STUDIATO / 6 ESCLUSO / 268 DA STUDIARE**; batch semanticamente 0/25.

## Selezione e persistenza

Lo script `scripts/ingest_video.py` non legge `next-batch.txt`: seleziona dalla QUEUE i primi 25 ID con stato catalogo diverso da STUDIATO/ESCLUSO. Prima dell’avvio è stata verificata l’uguaglianza esatta fra tale selezione, le posizioni 201–225 e i 25 ID dell’handoff. La lista resta fissa in memoria e lo script non modifica gli stati: non può proseguire al 226. Nessuna modifica agli script.

`next-batch.txt` aggiornato nel commit finale perché `--commit-each` richiede working tree pulito all’avvio. Eseguito il comando previsto con `--acquire --count 25 --commit-each --push-each --continue-on-error`. Ogni ID ha ricevuto un commit/push individuale; normalizzazione finale, preferenza manuale, keyframe e handoff sono nel commit globale.

## Errori transitori risolti

Il primo tentativo di creazione branch è stato bloccato dai permessi del sandbox; una successiva chiamata di acquisizione è partita prima che il branch fosse creato e ha fallito sul primo ID per DNS e poi sul Git index lock. Nessun asset o commit è stato prodotto su main. Il solo report temporaneo è stato ripristinato identico alla base dopo la creazione autorizzata del branch, quindi il comando è ripartito con working tree pulito sul branch corretto. Il download del primo keyframe è stato a sua volta bloccato dalla rete sandbox e ripetuto con autorizzazione. Tutti questi blocchi sono risolti. Il passaggio effettivo dei 25 ID non registra ERROR o NO_IT_TRANSCRIPT. Gli avvisi yt-dlp sull’impersonation non hanno impedito i download.

## Verifica per contenuto

Copertura = intervallo fra primo evento testuale e fine ultimo evento, limitato alla durata metadata, diviso per tale durata; non misura l’assenza di pause interne né certifica accuratezza semantica. Timestamp e testo MD verificati segmento per segmento contro il JSON3 selezionato.

| Pos. | ID | Stato | Traccia | Segmenti MD | Durata metadata (s) | Intervallo JSON3 (s) | Copertura | Metadata / JSON3↔MD | Visuali |
|---:|---|---|---|---:|---:|---|---:|---|---|
| 201 | `vD7zMl6YXzs` | ACQUIRED | automatica it-orig | 368 | 789 | 0.000–789.330 | 100.00% | OK / OK | Nessun riferimento esplicito emerso dal controllo tecnico. |
| 202 | `QJUjdX0zglA` | ACQUIRED | automatica it-orig | 136 | 300 | 0.000–302.199 | 100.00% | OK / OK | Nessun riferimento esplicito emerso dal controllo tecnico. |
| 203 | `uayjrQ6GWQc` | ACQUIRED | automatica it-orig | 505 | 1226 | 0.299–1225.700 | 99.95% | OK / OK | Occorrenze controllate nel contesto: nessun rinvio concreto a informazioni mostrate da estrarre. |
| 204 | `nAqH9enAM1U` | ACQUIRED | automatica it-orig | 558 | 1444 | 0.120–1443.320 | 99.94% | OK / OK | Occorrenze controllate nel contesto: nessun rinvio concreto a informazioni mostrate da estrarre. |
| 205 | `R22IWnVNYus` | ACQUIRED | automatica it-orig | 660 | 1377 | 0.000–1377.080 | 100.00% | OK / OK | Occorrenze controllate nel contesto: nessun rinvio concreto a informazioni mostrate da estrarre. |
| 206 | `zfmFg5L7VDU` | ACQUIRED | automatica it-orig | 446 | 1004 | 0.000–1003.940 | 99.99% | OK / OK | Nessun riferimento esplicito emerso dal controllo tecnico. |
| 207 | `saBj3DmgsCg` | ACQUIRED | automatica it-orig | 936 | 2430 | 0.420–2429.780 | 99.97% | OK / OK | 07:58: riferimento «come vedete»; frame a circa 07:59 con relatore e schermo parziale, nessun diagramma leggibile. |
| 208 | `-lqseFTfCzk` | ACQUIRED | automatica it-orig | 564 | 1276 | 0.420–1276.160 | 99.97% | OK / OK | Nessun riferimento esplicito emerso dal controllo tecnico. |
| 209 | `C4IfIcOkwdE` | ACQUIRED | automatica it-orig | 546 | 1189 | 0.179–1188.799 | 99.97% | OK / OK | Nessun riferimento esplicito emerso dal controllo tecnico. |
| 210 | `aEv9F66CZqA` | ACQUIRED | automatica it-orig | 154 | 361 | 0.299–361.039 | 99.92% | OK / OK | Nessun riferimento esplicito emerso dal controllo tecnico. |
| 211 | `WtyLO1gMqVI` | ACQUIRED | automatica it-orig | 1437 | 3036 | 0.320–3036.799 | 99.99% | OK / OK | Nessun riferimento esplicito emerso dal controllo tecnico. |
| 212 | `TrY_mDjr7I4` | ACQUIRED | automatica it-orig | 3100 | 7212 | 0.000–7204.409 | 99.89% | OK / OK | 36:45 diagramma, 50:03 slide, 63:16 slide, 65:32 grafico: 4 frame. Lavagna distante a 36:46, slide visibile a 63:17; altri frame con relatore/schermo parziale. |
| 213 | `_CPcSMMzIY0` | ACQUIRED | automatica it-orig | 76 | 171 | 0.000–170.280 | 99.58% | OK / OK | Nessun riferimento esplicito emerso dal controllo tecnico. |
| 214 | `I-YCFdXNSO0` | ACQUIRED | automatica it-orig | 225 | 478 | 0.849–477.639 | 99.75% | OK / OK | Nessun riferimento esplicito emerso dal controllo tecnico. |
| 215 | `bLmGe86nDAA` | ACQUIRED | automatica it-orig | 209 | 470 | 2.330–469.690 | 99.44% | OK / OK | 02:59 pagina mostrata: 1 frame a circa 03:00, pagina visibile. |
| 216 | `of0ppir9sq4` | ACQUIRED | automatica it-orig | 99 | 235 | 0.110–235.330 | 99.95% | OK / OK | Nessun riferimento esplicito emerso dal controllo tecnico. |
| 217 | `bY6Lb0Dld88` | ACQUIRED | manuale it | 68 | 317 | 12.880–318.670 | 95.94% | OK / OK | Nessun riferimento esplicito emerso dal controllo tecnico. |
| 218 | `JQXoKKwneBQ` | ACQUIRED | automatica it-orig | 1962 | 4259 | 0.220–4384.610 | 99.99% | OK / OK | 32:46 dati e 48:07 grafico: 2 frame. Primo con slide Amazon, secondo con slide funnel appena avviata. Possibile disallineamento temporale: vedi limiti. |
| 219 | `ji8rHHO_KHY` | ACQUIRED | automatica it-orig | 2166 | 4484 | 12.840–4485.369 | 99.71% | OK / OK | 11:15 pagina, 21:22 livelli mostrati, 25:05 annuncio di dimostrazione: 3 frame. Pagina e diagramma visibili nei primi due; relatore nel terzo. |
| 220 | `HwlqYf73Ctk` | ACQUIRED | automatica it-orig | 2787 | 6443 | 0.000–6442.150 | 99.99% | OK / OK | 42:02 slide: 1 frame a circa 42:03, slide visibile. |
| 221 | `G0fxszrL9_M` | ACQUIRED | automatica it-orig | 371 | 822 | 0.060–821.959 | 99.99% | OK / OK | Nessun riferimento esplicito emerso dal controllo tecnico. |
| 222 | `0rM-F7msbkA` | ACQUIRED | automatica it-orig | 521 | 1231 | 0.000–1231.160 | 100.00% | OK / OK | Nessun riferimento esplicito emerso dal controllo tecnico. |
| 223 | `sUkGSSqTq3c` | ACQUIRED | automatica it-orig | 648 | 1574 | 0.120–1573.940 | 99.99% | OK / OK | Occorrenze controllate nel contesto: nessun rinvio concreto a informazioni mostrate da estrarre. |
| 224 | `pJZSih3Lguw` | ACQUIRED | automatica it-orig | 28 | 58 | 0.000–59.420 | 100.00% | OK / OK | Nessun riferimento esplicito emerso dal controllo tecnico. |
| 225 | `WCP26HC6wd0` | ACQUIRED | automatica it-orig | 50 | 118 | 0.040–115.336 | 97.71% | OK / OK | Nessun riferimento esplicito emerso dal controllo tecnico. |

## Provenienza, normalizzazione e limiti

- Tutti i 25 metadata verificati: ID, titolo non vuoto, URL esatto, data pubblicazione, durata e canale ufficiale `UCaAzr7bvYcZRfGR8EyBynOA`. Nessuna fonte esterna o copia. Le liste `subtitle_languages` e `automatic_caption_languages` conservano la provenienza disponibile.
- Preferita la traccia manuale `bY6Lb0Dld88.it.json3` (68 segmenti), rigenerando il Markdown con `scripts/transcript.py` e correggendo esclusivamente l’etichetta manuale. La traccia automatica non selezionata è recuperabile nel commit individuale. Il primo evento manuale è a 12,880 s; copertura intervallo 95,94%.
- Negli altri 24 casi `it` e `it-orig` erano JSON equivalenti: conservato solo `it-orig`, dopo confronto strutturale. Rimossi soltanto spazi finali di formattazione JSON3, verificando uguaglianza dei dati prima/dopo. Nessuna correzione arbitraria del testo.
- Tutti i JSON3 sono validi, non vuoti, con timestamp ordinati. Tutti i Markdown corrispondono esattamente al testo e ai timestamp normalizzati del JSON3 selezionato.
- **218 — JQXoKKwneBQ:** durata metadata 4.259 s, ultimo evento termina a 4.384,610 s (+125,610 s). Possibile traccia riferita a una versione con montaggio/durata diversa; causa non accertata. Non applicato alcun offset né taglio. Il testo è utilizzabile per la revisione, ma ChatGPT deve verificare la corrispondenza temporale prima di usare timestamp/visuali come evidenza precisa. La coincidenza JSON3↔MD non risolve questo limite della fonte.
- Piccoli sforamenti finali di altri JSON3 sono conservati senza ritocchi. Il 225 termina a 115,336 s su 118 s (copertura intervallo 97,71%).
- Il controllo lessicale selettivo ha incluso slide, grafici, tabelle, schermo, diagrammi, schemi, mostrare e rinvii «come vedete». Le occorrenze generiche non hanno motivato download. Nessuna interpretazione dottrinale.

## Keyframe candidati

12 PNG in sei cartelle `sources/transcripts/VIDEO_ID-frames/`, estratti dal solo video ufficiale con `scripts/extract_keyframes.py`. I nomi indicano l’inizio dell’estratto di due secondi; il frame è estratto a +1 secondo circa. Ispezione tecnica completata: file decodificabili, inquadrature descritte nella tabella; la decisione semantica resta a ChatGPT. Gli estratti video temporanei restano in `work/keyframes/` e non sono duplicati nell’archivio durevole.

## Validazione e invarianti

- Validator prima/dopo: **841 warning identici, zero nuove anomalie**. Il confronto integrale dell’output è identico.
- Precisazione rispetto al checkpoint: i 836 disallineamenti sono distribuiti tra VIDEO_INDEX (418) e QUEUE (418), non tutti QUEUE; restano 3 divergenze frozen storiche rispetto a v1.0 e 2 warning sulla nomenclatura STATUS. Non corretti.
- Frozen, `merenda/`, `sources/catalog.json`, `sources/VIDEO_INDEX.md`, `sources/queue/QUEUE.md` invariati rispetto alla base. Nessun `.review.md` creato, nessuno stato semantico modificato.
- Esatti 25 URL in next-batch, primo `vD7zMl6YXzs`, ultimo `WCP26HC6wd0`; il diff degli asset è limitato a questi ID. **Nessun 226+ acquisito**.
- `git diff --check` rispetto alla base superato.

## Handoff

Agente richiesto: **CHATGPT**. Prossima azione: revisione semantica 201–225, primo **201 — vD7zMl6YXzs**. Tenere presente il limite temporale del 218. Prossimo checkpoint Claude dopo il completamento semantico del 225: **FASE 14**. Nessun merge in main; nessun branch semantic-201-225 creato.
