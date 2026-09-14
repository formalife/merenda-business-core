# Acquisition Progress

- Branch: `acquisition-226-250`
- Base SHA: `da0a20c00882f287674635109e625fef47f23408`
- Batch canonico: **226–250**, esattamente 25 ID in ordine.
- Tentati/completati tecnicamente: **25/25 ACQUIRED**; transcript utilizzabili: **25/25** (verifica tecnica, revisione semantica non eseguita).
- Tracce manuali: **0**; automatiche italiane originali: **25**; fallback ASR: **0**.
- NO_IT_TRANSCRIPT: **0**; errori finali: **0**; pending: **0**.
- Persistenza: **25 commit individuali + 1 commit globale finale di handoff** sul solo branch tecnico.
- Semantica invariata: **225 processati / 219 STUDIATO / 6 ESCLUSO / 243 DA STUDIARE**; batch semanticamente 0/25.

## Selezione, stato iniziale e persistenza

Fetch e aggiornamento ff-only di main: HEAD locale e origin/main uguali alla base attesa, working tree pulito. Branch tecnico creato dalla base e pubblicato prima dell’acquisizione. Nessun merge su main e nessun branch semantic-226-250 creato.

Differenza verificata rispetto all’handoff iniziale: i metadata e JSON3 it-orig dei video **232 e 233 erano già tracciati nella base** (commit originario `2224db9`, prima dei successivi riordini della queue); mancava il Markdown. Riutilizzati e verificati, con normalizzazione Markdown nei rispettivi commit individuali. Quindi 23 nuovi download metadata/sottotitoli e 2 completamenti da asset ufficiali preesistenti; tutti e 25 hanno ricevuto il proprio commit/push. L’asserzione preliminare di assenza totale degli asset ha rilevato questa differenza prima di qualsiasi acquisizione; nessuna modifica agli stati.

Riprodotta la selezione di `scripts/ingest_video.py`: primi 25 ID della QUEUE con stato catalogo diverso da STUDIATO/ESCLUSO, identici alle posizioni 226–250 e alla lista vincolante. La lista è fissa in memoria. `next-batch.txt` preparato e verificato prima dell’avvio in work/tmp, applicato nel commit finale per rispettare il working tree pulito richiesto da --commit-each. Contiene esattamente 25 URL, primo m53_BsS_x8U, ultimo uOu65O88jrU. Nessun 251+ selezionato.

Comando eseguito: `python3 scripts/ingest_video.py --acquire --count 25 --commit-each --push-each --continue-on-error`. Nessun ERROR/NO_IT_TRANSCRIPT nel log, nessun retry di acquisizione necessario. Avvisi yt-dlp sull’impersonation non bloccanti. Keyframe scaricati senza errori finali. Nessuna modifica agli script o al classificatore.

## Verifica per contenuto

Copertura = (min(fine ultimo evento testuale, durata metadata) − inizio primo evento testuale) / durata metadata. Non misura le pause interne o l’accuratezza semantica. JSON3 valido/non vuoto; timestamp ordinati verificati in millisecondi; ogni segmento e timestamp Markdown confrontato con la normalizzazione del JSON3 selezionato.

| Pos. | ID | Stato / traccia | Data pubblicazione | Segmenti | Durata (s) | Intervallo JSON3 (s) | Copertura | Metadata / JSON3↔MD | Visuali |
|---:|---|---|---|---:|---:|---|---:|---|---|
| 226 | `m53_BsS_x8U` | ACQUIRED / auto it-orig | 20230124 | 24 | 47 | 1.820–48.440 | 96.13% | OK / OK | Nessun riferimento visuale esplicito emerso dal controllo tecnico. |
| 227 | `n_5xPjN-NZY` | ACQUIRED / auto it-orig | 20260425 | 49 | 114 | 0.560–109.441 | 95.51% | OK / OK | Nessun riferimento visuale esplicito emerso dal controllo tecnico. |
| 228 | `W90bBHzfPMI` | ACQUIRED / auto it-orig | 20260217 | 41 | 96 | 0.199–89.280 | 92.79% | OK / OK | Nessun riferimento visuale esplicito emerso dal controllo tecnico. |
| 229 | `7zRyOC3Z0lM` | ACQUIRED / auto it-orig | 20251216 | 57 | 119 | 0.040–121.360 | 99.97% | OK / OK | Nessun riferimento visuale esplicito emerso dal controllo tecnico. |
| 230 | `Qg8Z2Oh5z3s` | ACQUIRED / auto it-orig | 20251030 | 34 | 72 | 0.080–73.720 | 99.89% | OK / OK | Nessun riferimento visuale esplicito emerso dal controllo tecnico. |
| 231 | `xBM5PST7ZKs` | ACQUIRED / auto it-orig | 20230831 | 21 | 46 | 0.780–47.090 | 98.30% | OK / OK | Nessun riferimento visuale esplicito emerso dal controllo tecnico. |
| 232 | `MwNCMJE8sRk` | ACQUIRED / auto it-orig | 20241101 | 488 | 1090 | 0.240–1090.640 | 99.98% | OK / OK | Occorrenze generiche verificate nel contesto: nessun rinvio concreto da estrarre. |
| 233 | `g-VOlvqnL_8` | ACQUIRED / auto it-orig | 20240920 | 355 | 767 | 0.000–767.830 | 100.00% | OK / OK | Nessun riferimento visuale esplicito emerso dal controllo tecnico. |
| 234 | `ggJnCJCXIO4` | ACQUIRED / auto it-orig | 20250702 | 1929 | 3946 | 0.040–3946.209 | 100.00% | OK / OK | Nessun riferimento visuale esplicito emerso dal controllo tecnico. |
| 235 | `KZ78VhszH_o` | ACQUIRED / auto it-orig | 20250521 | 1642 | 3329 | 0.080–3329.550 | 100.00% | OK / OK | Rinvii 43:47, 48:01, 53:16: estratti selettivi; schema a blocchi a 48:06; vedere elenco frame. |
| 236 | `3ZNE75sPen8` | ACQUIRED / auto it-orig | 20250430 | 2063 | 4432 | 0.040–4432.089 | 100.00% | OK / OK | Rinvii 13:04, 48:58, 67:23: pagine/annunci visibili nei 3 frame. |
| 237 | `lwuJ6MYETUw` | ACQUIRED / auto it-orig | 20250416 | 1745 | 3844 | 0.040–3844.869 | 100.00% | OK / OK | Occorrenze generiche verificate nel contesto: nessun rinvio concreto da estrarre. |
| 238 | `T5ccJyQqX9c` | ACQUIRED / auto it-orig | 20250411 | 1443 | 3397 | 0.120–3397.309 | 100.00% | OK / OK | Occorrenze generiche verificate nel contesto: nessun rinvio concreto da estrarre. |
| 239 | `t-rvhD0P5Iw` | ACQUIRED / auto it-orig | 20250318 | 1352 | 2988 | 0.080–2988.050 | 100.00% | OK / OK | Occorrenze generiche verificate nel contesto: nessun rinvio concreto da estrarre. |
| 240 | `dYMeQuuT8QY` | ACQUIRED / auto it-orig | 20250304 | 1045 | 2328 | 0.160–2328.829 | 99.99% | OK / OK | Occorrenze generiche verificate nel contesto: nessun rinvio concreto da estrarre. |
| 241 | `8XduYN366z0` | ACQUIRED / auto it-orig | 20250227 | 1150 | 2643 | 0.040–2643.969 | 100.00% | OK / OK | 02:23 e 03:09: stesso grafico; 1 frame a circa 02:24. |
| 242 | `rcVXvepx-l8` | ACQUIRED / auto it-orig | 20250225 | 358 | 885 | 0.120–885.090 | 99.99% | OK / OK | Occorrenze generiche verificate nel contesto: nessun rinvio concreto da estrarre. |
| 243 | `gcQKKrbZW28` | ACQUIRED / auto it-orig | 20250213 | 1153 | 2404 | 0.160–2404.929 | 99.99% | OK / OK | Occorrenze generiche verificate nel contesto: nessun rinvio concreto da estrarre. |
| 244 | `sa45UbN4sMI` | ACQUIRED / auto it-orig | 20250211 | 723 | 1474 | 0.199–1474.029 | 99.99% | OK / OK | Occorrenze generiche verificate nel contesto: nessun rinvio concreto da estrarre. |
| 245 | `Zzh6PXGTmD0` | ACQUIRED / auto it-orig | 20250117 | 531 | 1227 | 0.040–1227.289 | 100.00% | OK / OK | Occorrenze generiche verificate nel contesto: nessun rinvio concreto da estrarre. |
| 246 | `bWNr-tHknvw` | ACQUIRED / auto it-orig | 20250115 | 546 | 1148 | 0.000–1148.329 | 100.00% | OK / OK | Occorrenze generiche verificate nel contesto: nessun rinvio concreto da estrarre. |
| 247 | `V8CVwcH5rwA` | ACQUIRED / auto it-orig | 20250107 | 631 | 1362 | 0.040–1362.609 | 100.00% | OK / OK | 20:29: riferimento al volume tenuto in mano; copertina visibile, pagine interne non leggibili. |
| 248 | `r649dAXopLM` | ACQUIRED / auto it-orig | 20241218 | 370 | 903 | 0.120–902.040 | 99.88% | OK / OK | Occorrenze generiche verificate nel contesto: nessun rinvio concreto da estrarre. |
| 249 | `Q3SCQG-aZSM` | ACQUIRED / auto it-orig | 20241016 | 429 | 962 | 0.160–961.959 | 99.98% | OK / OK | Occorrenze generiche verificate nel contesto: nessun rinvio concreto da estrarre. |
| 250 | `uOu65O88jrU` | ACQUIRED / auto it-orig | 20240909 | 187 | 394 | 0.080–395.090 | 99.98% | OK / OK | Occorrenze generiche verificate nel contesto: nessun rinvio concreto da estrarre. |

## Provenienza e titoli

Tutti i metadata verificati: ID, URL watch esatto, titolo non vuoto, nome canale, uploader @FrankMerendaTV, channel URL e channel ID `UCaAzr7bvYcZRfGR8EyBynOA`, data pubblicazione e durata. Le liste subtitle_languages (nessuna traccia manuale disponibile) e automatic_caption_languages conservano la provenienza. Tutti i JSON3 selezionati sono `it-orig`. Le 23 coppie appena scaricate it/it-orig erano strutturalmente identiche: conservato solo it-orig; it resta recuperabile dai commit individuali. Per 232/233 era già conservato solo it-orig. Rimossi esclusivamente spazi finali JSON3, verificando uguaglianza dei dati; nessuna correzione testuale, offset o taglio.

I titoli attuali possono essere la versione italiana di quelli inglesi del catalogo/handoff; verificati sullo stesso ID del canale ufficiale e conservati senza riscrittura. Elenco effettivo:

| Pos. | ID | Titolo metadata | Confronto catalogo |
|---:|---|---|---|
| 226 | `m53_BsS_x8U` | Video animati per Landing page - Strategia di marketing corretta? #shorts | Identico |
| 227 | `n_5xPjN-NZY` | Il 50% dei Clienti Va dal Leader. E Tu Cosa Stai Facendo? | Versione italiana ricevuta da YouTube |
| 228 | `W90bBHzfPMI` | ❌ Smetti di Buttare Soldi in Pubblicità: ✅ Lavora sui Clienti che Hai Già! | Versione italiana ricevuta da YouTube |
| 229 | `7zRyOC3Z0lM` | Basta Perdere SOLDI Con Front-End E Funnel Marketing: Perché il Tuo "Cliente" NON È un Cliente | Versione italiana ricevuta da YouTube |
| 230 | `Qg8Z2Oh5z3s` | FUNNEL di VENDITA: Il Marketing che ELIMINA la Carne da Cannone dei Venditori | Versione italiana ricevuta da YouTube |
| 231 | `xBM5PST7ZKs` | Il concetto di Lead Generation, esca e Funnel spiegato semplice #shorts | Identico |
| 232 | `MwNCMJE8sRk` | 7 Tecniche Invincibili Per Riportare Soldi In Cassa Dai Clienti Non Convertiti | Identico |
| 233 | `g-VOlvqnL_8` | Come Trasformare Il Preventivo In Un’arma Letale Per Chiudere Contratti | Identico |
| 234 | `ggJnCJCXIO4` | Strategia Marketing Per PMI: 8 Passi Per Vendere di Più [Senza Sprecare Budget] | Identico |
| 235 | `KZ78VhszH_o` | Come VENDERE Di Più e Generare PROFITTI Straordinari Per La Tua Azienda | Versione italiana ricevuta da YouTube |
| 236 | `3ZNE75sPen8` | Come Aumentare Le Conversioni: La Checklist Segreta Che Fa Impazzire I Venditori | Identico |
| 237 | `lwuJ6MYETUw` | Testimonianze Che Vendono: Come Renderle Perfette in 7 Step | Versione italiana ricevuta da YouTube |
| 238 | `T5ccJyQqX9c` | Come Vendere di Più: Le 4 Fasi Cruciali del Follow Up di Marketing | Versione italiana ricevuta da YouTube |
| 239 | `t-rvhD0P5Iw` | 🔥 Come Far Esplodere Le Vendite Senza Acquisire Nuovi Clienti | Versione italiana ricevuta da YouTube |
| 240 | `dYMeQuuT8QY` | Come Vendere Di Più Trasformando Il Tuo Marketing In Un Magnete | Versione italiana ricevuta da YouTube |
| 241 | `8XduYN366z0` | Come Creare Clienti A Vita: 7 Azioni Top Per Aumentare Le Vendite [Masterclass] | Versione italiana ricevuta da YouTube |
| 242 | `rcVXvepx-l8` | Le 6 Personalità Di Acquisto Che Ti Faranno Vendere Di Più [Senza Inseguire I Ricchi!] | Identico |
| 243 | `gcQKKrbZW28` | Eventi Dal Vivo: Come Generare Vendite Straordinarie Senza Sprecare Budget | Versione italiana ricevuta da YouTube |
| 244 | `sa45UbN4sMI` | 🔴 Come Vendere Di Più: L’unico Metodo Testato Per Eliminare La Resistenza All’Acquisto | Versione italiana ricevuta da YouTube |
| 245 | `Zzh6PXGTmD0` | Come Vendere di Più (E Battere I Colossi): La Fiducia Che Genera Profitto Immediato | Identico |
| 246 | `bWNr-tHknvw` | La Formula Di Frank Merenda Per Vendere Qualsiasi Prodotto | Versione italiana ricevuta da YouTube |
| 247 | `V8CVwcH5rwA` | 🔴 TECNICHE DI VENDITA: Prepara La Tua Rete Vendita Per Sconfiggere I Brand Famosi | Identico |
| 248 | `r649dAXopLM` | Testimonianze Che Fanno Esplodere Le Vendite: La Guida Inedita di Frank Merenda | Versione italiana ricevuta da YouTube |
| 249 | `Q3SCQG-aZSM` | #4 TECNICHE DI VENDITA Micidiali Per Vendere Agli "Indecisi" | Identico |
| 250 | `uOu65O88jrU` | L’errore Che Ti Impedisce Di VENDERE 10 VOLTE Di Più (E Spendere 10 Volte Meno) | Versione italiana ricevuta da YouTube |

## Limiti temporali

- **227 n_5xPjN-NZY:** intervallo 0,560–109,441 s su 114 s; copertura 95,51%; ultimi 4,559 s fuori dall’intervallo della traccia. Ultimo evento testuale: indicazione [musica].
- **228 W90bBHzfPMI:** intervallo 0,199–89,280 s su 96 s; copertura 92,79%; ultimi 6,720 s fuori dall’intervallo della traccia. Il testo finale disponibile termina con «noi. Sì.». Non è stata verificata via ascolto l’eventuale presenza di parlato ulteriore nella coda: limite della copertura della fonte, non perdita JSON3→MD.
- Gli sforamenti finali positivi sono fra 0,029 e 2,360 s (massimo: 229). Nessuna anomalia ampia comparabile ai +125,610 s del 218. Conservati i tempi originali; nessun riallineamento intuitivo. Tutti i valori esatti sono in tabella.
- L’utilizzabilità è tecnica: testo disponibile e corrispondenza integra, senza certificazione semantica o verifica audio integrale. Il controllo selettivo ha incluso slide, grafici, tabelle, diagrammi, lavagna, schermo, pagina, formule, numeri associati a rinvii visuali e locuzioni come «qui vedi»/«ti faccio vedere». Le menzioni generiche non hanno motivato download.

## Keyframe candidati

9 PNG in 4 cartelle `sources/transcripts/VIDEO_ID-frames/`, estratti con `scripts/extract_keyframes.py --youtube`. I nomi indicano l’inizio dell’estratto di 2 secondi; il frame è a circa +1 secondo. Tutti decodificati e ispezionati tecnicamente. Solo immagini contenute nei video ufficiali: nessun sito o fonte esterna consultato, neppure quando compare nelle slide. Gli estratti temporanei restano in work/keyframes, senza duplicazioni durevoli.

| Video | File / secondo iniziale | Contenuto tecnico |
|---|---|---|
| 235 KZ78VhszH_o | KZ78VhszH_o-2657.png | Relatore alla scrivania, nessuna slide nel frame. |
| 235 KZ78VhszH_o | KZ78VhszH_o-2885.png | Slide sovrapposta con blocchi colorati, frecce e canali/siti/team; testo leggibile. |
| 235 KZ78VhszH_o | KZ78VhszH_o-3198.png | Relatore, nessuna slide nel frame; effettuato un ulteriore campione selettivo a 3208. |
| 235 KZ78VhszH_o | KZ78VhszH_o-3208.png | Slide blu con due diagrammi affiancati, titoli «N.2 Campagne Quiz» e «N.2 Campagne Corsi Gratuiti»; dettagli minuti, animazione non necessariamente completa. |
| 236 3ZNE75sPen8 | 3ZNE75sPen8-784.png | Slide con pagine De Beers e Backlinko, form e pulsanti visibili. |
| 236 3ZNE75sPen8 | 3ZNE75sPen8-2938.png | Relatore e riquadro con due annunci, prodotti e importi visibili. |
| 236 3ZNE75sPen8 | 3ZNE75sPen8-4043.png | Pagina VoiceNation con headline, CTA, telefono e badge visibili. |
| 241 8XduYN366z0 | 8XduYN366z0-143.png | Slide «1000 Veri Fan», grafico con assi e curva, testo leggibile. |
| 247 V8CVwcH5rwA | V8CVwcH5rwA-1229.png | Relatore con volume, copertina e URL sovrapposto visibili; pagine interne non leggibili. |

## Validazione e invarianti

- Validator pre/post: **841 warning storici, output integrale identico, zero nuove anomalie**; exit code 1 storico. Output completi salvati localmente in work/tmp/acquisition-226-250/validator-before.txt e validator-after.txt.
- SHA256 dell’output baseline (e post se identico): `9d0cc059564cb3994d1792d796b84fa0155f80c7e46d8334050df41d67814b91`.
- Composizione: 836 disallineamenti storici (418 VIDEO_INDEX + 418 QUEUE), 3 divergenze frozen storiche rispetto a v1.0, 2 warning sulla nomenclatura dei contatori STATUS. Nessuna riparazione fuori scope.
- `git diff --check` pre e finale, anche rispetto alla base: superato.
- Frozen, merenda/, catalog.json, VIDEO_INDEX.md, QUEUE.md e classificatore invariati rispetto alla base. Nessuna .review.md nuova. Nessuno stato/categoria semantica modificato.
- Diff degli asset limitato ai 25 ID vincolanti; nessun nuovo asset 251+. 25 commit individuali verificati prima del commit finale, ognuno pushato; handoff pubblicato sul medesimo branch. Nessun merge su main.

## Handoff

Agente richiesto: **CHATGPT**. Checkpoint 225 FASE 14 completato; revisione semantica **226–250**, primo **226 — m53_BsS_x8U**. Semantica ancora ferma a 225. Prossimo checkpoint Claude dopo il completamento semantico del 250: **FASE 14 + FASE 15**. Classificazione futura invariata: 6 C, 10 A, 9 B; completezza tecnica uguale per tutti.
