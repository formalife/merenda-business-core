# Acquisition Progress

- Branch: `acquisition-251-275`
- Base canonica: `e75aeca6b76f2e94678608dd90a2e550d7d486db`
- FASE 7 completata: **251–275**, esattamente **25 tentati / 25 ACQUIRED / 25 transcript utilizzabili**.
- Italiani manuali: **0**; automatici originali: **25**; fallback ASR: **0**.
- NO_IT_TRANSCRIPT: **0**; ERROR finali: **0**; PENDING: **0**.
- **25 commit individuali + 1 commit globale di handoff**, tutti sul branch tecnico, nessun merge su main.
- Semantica invariata: **250 processati / 244 STUDIATO / 6 ESCLUSO / 218 DA STUDIARE**. Nessuna review o revisione semantica.
- Classificazione futura invariata: A 257/262/270, B gli altri 22, C 0; qualità tecnica uniforme.

## Procedura e provenienza

Letta la governance e verificati checkpoint 250 e classificazione residua. Eseguiti fetch, switch main, pull --ff-only, status e rev-parse: base esatta e working tree pulito. Branch nuovo creato direttamente dalla base, pubblicato senza sovrascritture. Nessun asset del batch era già presente. Confrontati tutti i 25 ID e il loro ordine con QUEUE.md e con la selezione dello script; primo 251 ellOvKnIOqk, ultimo 275 jIVCaEJe9RU.

Eseguito `python3 scripts/ingest_video.py --acquire --count 25 --commit-each --push-each --continue-on-error`. 25 acquisizioni e push riusciti; nessun errore/retry di acquisizione. Avvisi impersonation yt-dlp non bloccanti. `next-batch.txt` applicato nel commit globale per rispettare il working tree pulito iniziale richiesto dallo script; contiene esattamente i 25 URL canonici. Nessuna modifica agli script o a classify().

Verificati per 25/25: ID, URL watch, titolo ricevuto, channel e uploader_id @FrankMerendaTV, channel URL e channel ID UCaAzr7bvYcZRfGR8EyBynOA, data pubblicazione YYYYMMDD e durata positiva. Metadata ridotti dal workflow senza URL multimediali firmati. subtitle_languages e automatic_caption_languages conservano la provenienza: nessuna traccia italiana manuale; preferita auto it-orig. Tutte le 25 coppie it/it-orig erano strutturalmente identiche: mantenuto solo it-orig, copie it recuperabili nei commit individuali. Rimossi solo spazi finali dal JSON3 verificando uguaglianza dei dati. Nessuna riscrittura, correzione del parlato o degli offset.

Log integrali locali: `work/tmp/acquisition-251-275/ingest.log`, `frames-*.log`, `verify.py`, `checks.json`, `visual-signals.txt`, `validator-before.txt`, `validator-after.txt`. Fonte unica: video ufficiali; nessuna fonte semantica esterna consultata.

## Verifica per contenuto

Eventi = tutti gli eventi JSON3; segmenti = eventi con testo non vuoto normalizzato. Gli altri sono eventi vuoti/controllo conservati nel JSON3, non testo perso. Confronto completo di ogni segmento, testo, ordine e timestamp Markdown (secondo intero per convenzione) contro JSON3 in millisecondi: 25/25 OK, zero perdite o duplicazioni introdotte, zero righe consecutive identiche con stesso timestamp. Tutti gli eventi hanno timestamp ordinati e non negativi e durate non negative.

Copertura = (min(fine ultimo evento testuale, durata metadata) − inizio primo evento testuale) / durata metadata. Misura l’intervallo esterno, non le pause interne né l’accuratezza audio/semantica. Delta fine = fine traccia − durata metadata; valori negativi sono code non coperte. Nessun riallineamento intuitivo.

| Pos. | ID | Stato / traccia | Pubblicazione | Durata s | Eventi / segmenti | Intervallo s | Copertura | Delta fine s | JSON3↔MD | Keyframe / segnali |
|---:|---|---|---|---:|---:|---|---:|---:|---|---|
| 251 | `ellOvKnIOqk` | ACQUIRED / auto it-orig | 20240829 | 420 | 418 / 209 | 0.000–422.080 | 100.00% | +2.080 | OK | Nessun segnale visuale esplicito rilevato. |
| 252 | `rI00A_jHqz8` | ACQUIRED / auto it-orig | 20240726 | 278 | 224 / 112 | 0.120–275.360 | 99.01% | -2.640 | OK | Nessun segnale visuale esplicito rilevato. |
| 253 | `-_oOcTQgkcY` | ACQUIRED / auto it-orig | 20240724 | 5521 | 5750 / 2875 | 0.080–5515.560 | 99.90% | -5.440 | OK | Rinvio 1:07:26 al quadrante: 3 campioni, dati non inquadrati; limite documentato. |
| 254 | `P_LavmWySLs` | ACQUIRED / auto it-orig | 20240702 | 425 | 414 / 207 | 0.080–425.729 | 99.98% | +0.729 | OK | Nessun segnale visuale esplicito rilevato. |
| 255 | `an5eXiIyyiA` | ACQUIRED / auto it-orig | 20240613 | 901 | 898 / 449 | 0.000–902.000 | 100.00% | +1.000 | OK | Menzioni generiche nel contesto; nessun rinvio concreto da estrarre. |
| 256 | `wDPyGhkY_CA` | ACQUIRED / auto it-orig | 20240611 | 1000 | 1022 / 511 | 0.160–1000.039 | 99.98% | +0.039 | OK | Menzioni generiche nel contesto; nessun rinvio concreto da estrarre. |
| 257 | `oefQwsBIUc0` | ACQUIRED / auto it-orig | 20240603 | 1531 | 1584 / 792 | 0.120–1531.279 | 99.99% | +0.279 | OK | Menzioni generiche nel contesto; nessun rinvio concreto da estrarre. |
| 258 | `jzQcezkw8_o` | ACQUIRED / auto it-orig | 20240531 | 1003 | 1040 / 520 | 0.000–1003.070 | 100.00% | +0.070 | OK | Rinvio 00:52 alla piramide: 1 frame. |
| 259 | `5-UeSJzSvos` | ACQUIRED / auto it-orig | 20240520 | 257 | 178 / 89 | 0.000–243.680 | 94.82% | -13.320 | OK | Rinvii 00:18 e 03:53 ai risultati: 2 frame. |
| 260 | `XDnktZGk-ZM` | ACQUIRED / auto it-orig | 20240326 | 414 | 356 / 178 | 0.120–415.520 | 99.97% | +1.520 | OK | Rinvio 03:25 al target scritto: 1 frame. |
| 261 | `A4I-A5hldQw` | ACQUIRED / auto it-orig | 20240210 | 2179 | 1950 / 975 | 0.000–2181.240 | 100.00% | +2.240 | OK | Rinvii 03:24, 12:03, 14:22, 17:23, 21:16: 9 campioni; tabella leggibile solo a 724 s. |
| 262 | `RExoYxfxFWQ` | ACQUIRED / auto it-orig | 20231218 | 198 | 170 / 85 | 0.120–189.319 | 95.56% | -8.681 | OK | Nessun segnale visuale esplicito rilevato. |
| 263 | `HJBySYV6HjA` | ACQUIRED / auto it-orig | 20230828 | 231 | 180 / 90 | 0.179–221.599 | 95.85% | -9.401 | OK | Menzioni generiche nel contesto; nessun rinvio concreto da estrarre. |
| 264 | `9FpKpV15B_4` | ACQUIRED / auto it-orig | 20230601 | 2262 | 1964 / 982 | 0.120–2262.320 | 99.99% | +0.320 | OK | Menzioni generiche nel contesto; nessun rinvio concreto da estrarre. |
| 265 | `imdxn91jLik` | ACQUIRED / auto it-orig | 20230409 | 1342 | 1256 / 628 | 0.900–1341.380 | 99.89% | -0.620 | OK | Menzioni generiche nel contesto; nessun rinvio concreto da estrarre. |
| 266 | `NB9g-DhSj-4` | ACQUIRED / auto it-orig | 20230402 | 967 | 832 / 416 | 0.659–966.620 | 99.89% | -0.380 | OK | Menzioni generiche nel contesto; nessun rinvio concreto da estrarre. |
| 267 | `Vqn55dABlHQ` | ACQUIRED / auto it-orig | 20230321 | 4481 | 3915 / 1957 | 0.840–4482.199 | 99.98% | +1.199 | OK | Rinvii 00:40 e 07:22: 2 frame. |
| 268 | `IGR6IPPvY3Q` | ACQUIRED / auto it-orig | 20230309 | 1287 | 1062 / 531 | 0.000–1286.419 | 99.95% | -0.581 | OK | Rinvii 19:00 e 20:32: 2 frame lavagna. |
| 269 | `9YoGG3UT1Yc` | ACQUIRED / auto it-orig | 20230306 | 1760 | 1490 / 745 | 0.179–1760.179 | 99.99% | +0.179 | OK | Menzioni generiche nel contesto; nessun rinvio concreto da estrarre. |
| 270 | `21iVqc13KoE` | ACQUIRED / auto it-orig | 20230220 | 807 | 692 / 346 | 0.060–807.139 | 99.99% | +0.139 | OK | Menzioni generiche nel contesto; nessun rinvio concreto da estrarre. |
| 271 | `D96IKTeUfK4` | ACQUIRED / auto it-orig | 20230213 | 1234 | 1038 / 519 | 0.120–1233.980 | 99.99% | -0.020 | OK | Rinvio allo schema 01:47, contesto 00:50–02:20: 2 frame. |
| 272 | `NyH30NE16_0` | ACQUIRED / auto it-orig | 20230206 | 1000 | 856 / 428 | 0.240–999.740 | 99.95% | -0.260 | OK | Menzioni generiche nel contesto; nessun rinvio concreto da estrarre. |
| 273 | `0QpK3scgm4c` | ACQUIRED / auto it-orig | 20230116 | 1069 | 902 / 451 | 0.120–1068.860 | 99.98% | -0.140 | OK | Menzioni generiche nel contesto; nessun rinvio concreto da estrarre. |
| 274 | `G4j1zImJq8I` | ACQUIRED / auto it-orig | 20230116 | 1239 | 1170 / 585 | 0.240–1238.720 | 99.96% | -0.280 | OK | Menzioni generiche nel contesto; nessun rinvio concreto da estrarre. |
| 275 | `jIVCaEJe9RU` | ACQUIRED / auto it-orig | 20230116 | 1492 | 1372 / 686 | 0.420–1492.280 | 99.97% | +0.280 | OK | Menzioni generiche nel contesto; nessun rinvio concreto da estrarre. |

## Titoli ricevuti da YouTube

Corrispondenza certificata tramite ID; le differenze localizzate rispetto alla queue sono conservate nei metadata senza alterare il titolo canonico della queue.

| Pos. | ID | Titolo metadata | Confronto queue/catalogo |
|---:|---|---|---|
| 251 | `ellOvKnIOqk` | La Tecnica Di Vendita #1 Per Una Rete Vendita Da Record | Diverso/localizzato; stesso ID verificato |
| 252 | `rI00A_jHqz8` | Il Potere Del Marketing: +50% di Vendite Per Un'Azienda Farmaceutica di Successo | Identico |
| 253 | `-_oOcTQgkcY` | Le Migliori TECNICHE DI VENDITA su Internet | Diverso/localizzato; stesso ID verificato |
| 254 | `P_LavmWySLs` | Come Vendere Qualsiasi Cosa Con La "Parola Segreta" Di Frank Merenda | Diverso/localizzato; stesso ID verificato |
| 255 | `an5eXiIyyiA` | Come Creare Annunci ad Alta Conversione [Che Vendono] | Diverso/localizzato; stesso ID verificato |
| 256 | `wDPyGhkY_CA` | Le 3 Opzioni dell'UPSELLING per far Esplodere il Fatturato Senza Trovare Nuovi Clienti | Diverso/localizzato; stesso ID verificato |
| 257 | `oefQwsBIUc0` | RETE VENDITA: Come Raddoppiare le Vendite in 5 Step [Mai svelati] | Identico |
| 258 | `jzQcezkw8_o` | Come Gestire una Rete Vendita al Top | Diverso/localizzato; stesso ID verificato |
| 259 | `5-UeSJzSvos` | Da Estetista a Imprenditrice: Le Tecniche di Vendita che portano al Successo | Identico |
| 260 | `XDnktZGk-ZM` | Come Vendere Di Più? Impara dal Metodo Spilla-Soldi delle Chiese Americane | Diverso/localizzato; stesso ID verificato |
| 261 | `A4I-A5hldQw` | VENDERE di più grazie alle PR - [ Live Fabio e Riccardo Biancolini] | Identico |
| 262 | `RExoYxfxFWQ` | TECNICHE DI VENDITA &#124; Script e Processi per diventare un VENDITORE PROFESSIONISTA | Identico |
| 263 | `HJBySYV6HjA` | Chiudere le TRATTATIVE di VENDITA grazie all'Autorità | Diverso/localizzato; stesso ID verificato |
| 264 | `9FpKpV15B_4` | COME VENDERE DI PIÙ - Cattura l’attenzione dei tuoi clienti | Identico |
| 265 | `imdxn91jLik` | Come creare una rete vendita performante | Diverso/localizzato; stesso ID verificato |
| 266 | `NB9g-DhSj-4` | Come vendere di più creando affinità e fiducia con i clienti | Identico |
| 267 | `Vqn55dABlHQ` | Come VENDERE di più ai tuoi clienti attivi | Diverso/localizzato; stesso ID verificato |
| 268 | `IGR6IPPvY3Q` | Come vendere di più al giusto Target &#124; I 7 tipi di clienti [Parte 2] | Diverso/localizzato; stesso ID verificato |
| 269 | `9YoGG3UT1Yc` | Come vendere di più al giusto Target &#124; I 7 tipi di clienti [Parte 1] | Diverso/localizzato; stesso ID verificato |
| 270 | `21iVqc13KoE` | Come vendere di più utilizzando gli script di vendita | Identico |
| 271 | `D96IKTeUfK4` | Come vendere di più grazie al dialogo mentale | Diverso/localizzato; stesso ID verificato |
| 272 | `NyH30NE16_0` | Come vendere di più grazie ai 5 livelli di chiarezza | Diverso/localizzato; stesso ID verificato |
| 273 | `0QpK3scgm4c` | Come Vendere di più e con maggior frequenza [Parte 3] | Identico |
| 274 | `G4j1zImJq8I` | Come Vendere di più e con maggior frequenza [Parte 2] | Identico |
| 275 | `jIVCaEJe9RU` | Come Vendere di più e con maggior frequenza [Parte 1] | Identico |

## Limiti temporali

- 252 `rI00A_jHqz8`: ultimi 2.640 s fuori traccia, copertura 99.01%. Nessuna perdita nella conversione; eventuale parlato nella coda non verificato con ascolto.
- 253 `-_oOcTQgkcY`: ultimi 5.440 s fuori traccia, copertura 99.90%. Nessuna perdita nella conversione; eventuale parlato nella coda non verificato con ascolto.
- 259 `5-UeSJzSvos`: ultimi 13.320 s fuori traccia, copertura 94.82%. Nessuna perdita nella conversione; eventuale parlato nella coda non verificato con ascolto.
- 262 `RExoYxfxFWQ`: ultimi 8.681 s fuori traccia, copertura 95.56%. Nessuna perdita nella conversione; eventuale parlato nella coda non verificato con ascolto.
- 263 `HJBySYV6HjA`: ultimi 9.401 s fuori traccia, copertura 95.85%. Nessuna perdita nella conversione; eventuale parlato nella coda non verificato con ascolto.
- Sforamenti positivi fino a **2,240 s** (261); mantenuti i valori originali. Tutti gli scostamenti, compresi quelli minori, sono nella tabella.
- Utilizzabilità tecnica dei 25 transcript confermata; nessuna certificazione della precisione del riconoscimento automatico o della sincronizzazione audio integrale.

## Keyframe candidati

**22 PNG su 8 video**, tutti estratti con `scripts/extract_keyframes.py --youtube`, decodificati e ispezionati. Scaricati soltanto estratti selettivi di 2 secondi, mai video integrali. Il nome file indica il secondo iniziale dell’estratto; il frame è a circa +1 s. Campioni adiacenti aggiunti solo quando il primo non inquadrava la visuale. Nessun errore finale ffmpeg/download. Immagini descritte tecnicamente, senza interpretazione semantica.

| Pos. | File in sources/transcripts/ID-frames/ | Contenuto tecnico |
|---:|---|---|
| 253 | `-_oOcTQgkcY-4030.png` | Relatore e schermo nero con logo; nessun quadrante dati visibile. |
| 253 | `-_oOcTQgkcY-4056.png` | Relatore e schermo nero con logo; nessun quadrante dati visibile. |
| 253 | `-_oOcTQgkcY-4068.png` | Relatore e schermo nero con logo; nessun quadrante dati visibile. |
| 258 | `jzQcezkw8_o-54.png` | Piramide blu: quattro etichette colorate leggibili (incentivi, norma, performance review, turnover). |
| 259 | `5-UeSJzSvos-18.png` | Tabella con piani accettati, incassato e backend, importi cerchiati; bordi parzialmente tagliati. |
| 259 | `5-UeSJzSvos-235.png` | Relatori e porzione di tabella 2023/2024 con contatti raccolti; resto fuori campo. |
| 260 | `XDnktZGk-ZM-207.png` | Slide Saddleback Sam con figura centrale, frecce ed etichette in inglese leggibili. |
| 261 | `A4I-A5hldQw-205.png` | Relatore davanti a fotografie; tabella insetti non inquadrata. |
| 261 | `A4I-A5hldQw-215.png` | Relatore davanti a fotografie; tabella insetti non inquadrata. |
| 261 | `A4I-A5hldQw-724.png` | Tabella Insetto / Sistema associato con cinque righe e nomi prodotto leggibili. |
| 261 | `A4I-A5hldQw-850.png` | Primo piano del relatore; slide fuori campo. |
| 261 | `A4I-A5hldQw-862.png` | Primo piano del relatore; slide fuori campo. |
| 261 | `A4I-A5hldQw-1030.png` | Primo piano del relatore; slide fuori campo. |
| 261 | `A4I-A5hldQw-1043.png` | Primo piano del relatore; slide fuori campo. |
| 261 | `A4I-A5hldQw-1276.png` | Primo piano del relatore; email fuori campo. |
| 261 | `A4I-A5hldQw-1285.png` | Primo piano del relatore; email fuori campo. |
| 267 | `Vqn55dABlHQ-70.png` | Slide La realtà sui clienti oggi, cinque colonne con percentuali, testi e loghi leggibili. |
| 267 | `Vqn55dABlHQ-444.png` | Primo piano del relatore; immagine del limone sullo sfondo, nessun diagramma leggibile. |
| 268 | `IGR6IPPvY3Q-1142.png` | Lavagna con linea orizzontale, divisioni ed etichette manoscritte; lato destro parzialmente coperto. |
| 268 | `IGR6IPPvY3Q-1233.png` | Lavagna più ravvicinata, etichette e cerchio aggiunto; parte destra coperta dal relatore. |
| 271 | `D96IKTeUfK4-73.png` | Lavagna con freccia diagonale verso A; punto iniziale parzialmente coperto dal logo. |
| 271 | `D96IKTeUfK4-145.png` | Lavagna intera con punto iniziale, freccia e A cerchiata; slide superiore tagliata. |

Limiti: il quadrante citato nel 253 non compare nei tre campioni; nel 261, oltre alla tabella a 724 s, i rinvii a slide/email restano fuori campo anche nei campioni adiacenti. Non si presume che i dati assenti siano stati recuperati. ChatGPT può richiedere un ulteriore punto preciso se necessario. Nel 259 una tabella è tagliata: il frame iniziale conserva altri importi leggibili. Nel 267 il rinvio al limone non produce uno schema aggiuntivo. Nessuna scansione frame per frame.

## Validazione e invarianti

- Validator prima/dopo: **842 warning storici, output integrale identico**, exit 1 storico; nessuna nuova anomalia attribuibile al batch. 836 mismatch indice/queue, 3 divergenze frozen storiche rispetto a v1.0, 3 mismatch contatori STATUS. Nessuna correzione fuori scope.
- SHA256 baseline: `5dc3f10e05da70edad694a7974f70968bf2a53570c72008ea06b09121af3d54c`.
- `git diff --check` prima e dopo, anche contro la base: pulito. Frozen, merenda/, review, catalog.json, VIDEO_INDEX.md, QUEUE.md e classificatore invariati rispetto alla base. Nessuna .review.md nuova. Stati/categorie semantiche invariati.
- Diff limitato a STATUS, report tecnico, next-batch e asset dei 25 ID. Nessun nuovo asset per 276, 277 o successivi. Nessun merge su main. Working tree pulito e HEAD locale uguale al remoto verificati dopo il push finale.

## Handoff

Agente richiesto: **CHATGPT**. Prossima azione: revisione semantica **251–275**, fasi 8–13, iniziando da **251 ellOvKnIOqk**. Semantica ancora ferma a 250. Prossimo checkpoint Claude: **275 — FASE 14**, dopo il completamento semantico. Prossimo audit tassonomia: **300 — FASE 14 + FASE 15**. STOP tecnico a 275.
