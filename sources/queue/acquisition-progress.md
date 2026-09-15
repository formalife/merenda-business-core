# Acquisition Progress

## Esito — batch ottimizzato 276–300

- Branch: `acquisition-276-300`.
- Base canonica verificata: `81b0829bf99427ae5c46db8f33346fdab3d6c8ef` — Reprioritize residual queue by information gain.
- HEAD dopo i 25 commit individuali: `dbf86f10bf77afb0e54de6662741d1030c424ca7`.
- HEAD di handoff: il commit finale che contiene questa versione del report, successivo alla HEAD sopra; ricavabile con `git log -1 --format=%H -- sources/queue/acquisition-progress.md` sul branch tecnico. SHA finale comunicata anche nel report di chiusura.
- **25 tentati / 25 ACQUIRED / 25 transcript utilizzabili**.
- **2 italiani manuali / 23 automatici it-orig / 0 ASR / 0 NO_IT_TRANSCRIPT / 0 ERROR finali / 0 PENDING**.
- 24 acquisizioni nuove; asset del **279 6sNjbCGzd2A** già versionati nella base, riutilizzati e verificati integralmente. La dichiarazione precedente di assenza di tutti gli asset 276+ non corrispondeva al tree reale.
- **25 commit individuali + 1 commit globale di verifica, visuali e handoff**; push progressivi, nessun merge su main.
- Semantica invariata: **275 processati / 269 STUDIATO / 6 ESCLUSO / 193 DA STUDIARE**. Tutti i 25 restano DA STUDIARE.

## Procedura e ordine canonico

Lette le istruzioni iniziali, governance, checkpoint 275, nuova riprioritizzazione, README script, queue e report tecnico precedente. Fetch, switch main, pull --ff-only: working tree pulito e HEAD == origin/main == base richiesta. Creato e pubblicato il branch tecnico direttamente dalla base.

Verificati programmaticamente i primi 25 DA STUDIARE di QUEUE.md rispetto alla lista esplicita dell'utente; verificata anche la selezione effettuata tramite stati del catalogo in ordine queue. Primo pendente dello script: **KipX0tAAWr4**; ultimo del batch: **Fo8PB_7fE60**. Fonte operativa: `reviews/RESIDUAL_REPRIORITIZATION_276-468.md`; vecchia classificazione solo storica. Nessun riordino o riallineamento.

Eseguito il workflow canonico:
`python3 scripts/ingest_video.py --acquire --count 25 --commit-each --push-each --continue-on-error`.
Il primo avvio sandbox è fallito sul primo video per DNS e indice Git non scrivibile, prima di qualsiasi commit. Conservato il log; ripristinato solo il report generato da quel tentativo e rilanciato con autorizzazione di rete/Git. Il rilancio ha completato 25/25 con push individuali, senza ERROR o NO_IT. Avvisi yt-dlp impersonation non bloccanti. Anche il primo tentativo keyframe 280 è stato bloccato dal DNS sandbox e poi completato con autorizzazione.

`next-batch.txt` contiene esattamente i 25 URL nel nuovo ordine, applicati dopo il workflow per rispettare il requisito di working tree pulito iniziale. STOP assoluto a 300.

## Metadata e provenienza sottotitoli

Verificati per **25/25**: ID, titolo ricevuto non vuoto, URL watch esatto, channel non vuoto, channel_id **UCaAzr7bvYcZRfGR8EyBynOA**, channel_url ufficiale, uploader_id **@FrankMerendaTV**, data di pubblicazione e durata positiva. I metadata sono ridotti ai campi operativi senza URL multimediali firmati.

La disponibilità è attestata nei campi `subtitle_languages` e `automatic_caption_languages` dei metadata:
- **289 fpX3evEGoHY e 290 kGEOki4orFg**: traccia italiana manuale `it` presente, preferita alla automatica; rigenerato il Markdown direttamente da quella traccia e corretta solo l'etichetta di provenienza. Punteggiatura e frasi sono quelle della fonte manuale, non correzioni di Codex.
- Altri **23**: nessuna traccia italiana manuale indicata; conservato `it-orig` automatico.
- Le 23 coppie automatiche it/it-orig risultavano strutturalmente identiche: eliminata soltanto la copia it. Le due automatiche alternative ai manuali restano recuperabili nei commit individuali, senza duplicazione nel tree finale.
- Rimossi spazi finali dal contenitore JSON3, verificando uguaglianza dei dati prima/dopo. Nessuna modifica al testo o agli offset della traccia selezionata.
- Per il 279 metadata e traccia provengono dall'acquisizione storica già in Git (commit `0395bd2`); il workflow li ha riusati, senza nuovo download. Verifica tecnica attuale completa.

## Verifica per contenuto

Eventi = tutti gli eventi JSON3; segmenti = eventi con testo non vuoto dopo la sola normalizzazione degli spazi. Eventi vuoti/di controllo conservati nei JSON3.

Verificati integralmente: timestamp di tutti gli eventi non negativi e ordinati, durate non negative, offset dei frammenti non negativi, ordine dei segmenti, testo e timestamp Markdown contro JSON3. **25/25 OK**, nessuna perdita o duplicazione introdotta; nessuna riga consecutiva identica con stesso timestamp. Markdown al secondo intero per convenzione del converter; JSON3 conserva i millisecondi. Questi controlli non certificano l'accuratezza del parlato.

Copertura = (min(fine ultimo evento testuale, durata metadata) − inizio primo evento testuale) / durata metadata × 100. È l'intervallo esterno, non la somma delle durate né una verifica delle pause interne.
Delta fine = fine ultimo evento testuale − durata metadata; negativo = coda non coperta. Nessun riallineamento arbitrario.

| Pos. | ID | Stato / traccia | Pubblicazione | Durata s | Eventi / segmenti | Primo–fine ultimo s | Copertura | Delta fine s | JSON3↔MD | Rinvii visuali |
|---:|---|---|---|---:|---:|---|---:|---:|---|---|
| 276 | `KipX0tAAWr4` | ACQUIRED / auto it-orig | 20230314 | 3154 | 2770 / 1385 | 0.960–3154.040 | 99.97% | +0.040 | OK | Lavagna 06:24 e pacco mostrato 32:50. |
| 277 | `iuly2QEl9no` | ACQUIRED / auto it-orig | 20190812 | 1294 | 1054 / 527 | 2.720–1295.169 | 99.79% | +1.169 | OK | Nessun rinvio visuale concreto da estrarre rilevato. |
| 278 | `DTIhYJnLyGs` | ACQUIRED / auto it-orig | 20190822 | 850 | 690 / 345 | 0.000–851.040 | 100.00% | +1.040 | OK | Nessun rinvio visuale concreto da estrarre rilevato. |
| 279 | `6sNjbCGzd2A` | ACQUIRED / auto it-orig | 20220819 | 469 | 436 / 218 | 0.000–468.080 | 99.80% | -0.920 | OK | Nessun rinvio visuale concreto da estrarre rilevato. |
| 280 | `nKOvJg4lq6k` | ACQUIRED / auto it-orig | 20220715 | 5599 | 5377 / 2688 | 4.584–5601.024 | 99.92% | +2.024 | OK | Slide 27:36, esempi mostrati 40:38–47:09. |
| 281 | `eBvEH3TPqSA` | ACQUIRED / auto it-orig | 20230627 | 802 | 668 / 334 | 0.000–798.630 | 99.58% | -3.370 | OK | Nessun rinvio visuale concreto da estrarre rilevato. |
| 282 | `9lPjA4n3UB4` | ACQUIRED / auto it-orig | 20230202 | 1172 | 1010 / 505 | 0.240–1172.440 | 99.98% | +0.440 | OK | Nessun rinvio visuale concreto da estrarre rilevato. |
| 283 | `DcnlHK3p9u8` | ACQUIRED / auto it-orig | 20250206 | 1059 | 1118 / 559 | 0.080–1059.040 | 99.99% | +0.040 | OK | Nessun rinvio visuale concreto da estrarre rilevato. |
| 284 | `DgbZMAqw4NY` | ACQUIRED / auto it-orig | 20231213 | 2577 | 2156 / 1078 | 0.000–2579.240 | 100.00% | +2.240 | OK | Nessun rinvio visuale concreto da estrarre rilevato. |
| 285 | `N547HVgrQmk` | ACQUIRED / auto it-orig | 20221204 | 626 | 448 / 224 | 3.380–625.459 | 99.37% | -0.541 | OK | Nessun rinvio visuale concreto da estrarre rilevato. |
| 286 | `Hs8y1wNyamo` | ACQUIRED / auto it-orig | 20221115 | 1372 | 1174 / 587 | 0.179–1371.500 | 99.95% | -0.500 | OK | Nessun rinvio visuale concreto da estrarre rilevato. |
| 287 | `7tWAsKiB0-Q` | ACQUIRED / auto it-orig | 20220823 | 301 | 292 / 146 | 0.000–300.230 | 99.74% | -0.770 | OK | Nessun rinvio visuale concreto da estrarre rilevato. |
| 288 | `qX8bJHUIDjI` | ACQUIRED / auto it-orig | 20220805 | 1905 | 1534 / 767 | 4.190–1904.690 | 99.76% | -0.310 | OK | Triangolo 17:09; pagine 19:51 e 21:02. |
| 289 | `fpX3evEGoHY` | ACQUIRED / manuale it | 20171201 | 234 | 48 / 48 | 1.620–235.320 | 99.31% | +1.320 | OK | Nessun rinvio visuale concreto da estrarre rilevato. |
| 290 | `kGEOki4orFg` | ACQUIRED / manuale it | 20171113 | 165 | 42 / 42 | 0.940–165.660 | 99.43% | +0.660 | OK | Nessun rinvio visuale concreto da estrarre rilevato. |
| 291 | `Ldy_Av2G1SA` | ACQUIRED / auto it-orig | 20250625 | 4379 | 4270 / 2135 | 0.280–4380.010 | 99.99% | +1.010 | OK | Nessun rinvio visuale concreto da estrarre rilevato. |
| 292 | `GUolZGprkP8` | ACQUIRED / auto it-orig | 20220716 | 122 | 96 / 48 | 0.840–121.489 | 98.89% | -0.511 | OK | Nessun rinvio visuale concreto da estrarre rilevato. |
| 293 | `GdSf3-b_aIQ` | ACQUIRED / auto it-orig | 20250604 | 3756 | 3586 / 1793 | 0.240–3756.449 | 99.99% | +0.449 | OK | Schema animato 49:16–52:03. |
| 294 | `oqoMqLQl9G4` | ACQUIRED / auto it-orig | 20250311 | 4658 | 4216 / 2108 | 0.080–4658.069 | 100.00% | +0.069 | OK | Nessun rinvio visuale concreto da estrarre rilevato. |
| 295 | `5FEOsDJ5HAU` | ACQUIRED / auto it-orig | 20241211 | 1332 | 1236 / 618 | 0.040–1332.650 | 100.00% | +0.650 | OK | Nessun rinvio visuale concreto da estrarre rilevato. |
| 296 | `yZsBzaiH_Ic` | ACQUIRED / auto it-orig | 20241127 | 1479 | 1422 / 711 | 0.040–1479.269 | 100.00% | +0.269 | OK | Nessun rinvio visuale concreto da estrarre rilevato. |
| 297 | `2tWslHOkxIc` | ACQUIRED / auto it-orig | 20241115 | 777 | 718 / 359 | 0.240–777.149 | 99.97% | +0.149 | OK | Nessun rinvio visuale concreto da estrarre rilevato. |
| 298 | `v2LEVo40O_w` | ACQUIRED / auto it-orig | 20240814 | 1490 | 1468 / 734 | 0.040–1487.760 | 99.85% | -2.240 | OK | Schema quadranti 04:12 e rinvio conclusivo 23:24. |
| 299 | `dt5NN20BeOY` | ACQUIRED / auto it-orig | 20240730 | 6395 | 6438 / 3219 | 0.040–6388.880 | 99.90% | -6.120 | OK | Slide e formule 04:03, 24:46, 29:16, esempio 49:31. |
| 300 | `Fo8PB_7fE60` | ACQUIRED / auto it-orig | 20221017 | 863 | 734 / 367 | 0.120–862.639 | 99.94% | -0.361 | OK | Organigramma circolare 00:35, 06:27 e 10:53. |

## Titoli metadata rispetto alla queue

Corrispondenza certificata tramite ID; differenze di lingua, testo o Unicode conservate nei metadata senza modificare la queue.

| Pos. | ID | Titolo ricevuto | Confronto queue |
|---:|---|---|---|
| 276 | `KipX0tAAWr4` | Perchè il COPYWRITING parte dal tuo posizionamento [Corso Completo] | Diverso/localizzato; stesso ID verificato |
| 277 | `iuly2QEl9no` | Ghiaccio agli Eschimesi - Copywriting a Risposta Diretta [Parte 1] | Diverso/localizzato; stesso ID verificato |
| 278 | `DTIhYJnLyGs` | Ghiaccio agli Eschimesi - Copywriting a Risposta Diretta [Parte 2] | Diverso/localizzato; stesso ID verificato |
| 279 | `6sNjbCGzd2A` | Come creare una Call to Action Efficace | Diverso/localizzato; stesso ID verificato |
| 280 | `nKOvJg4lq6k` | COPYWRITING: Cos'é Oggi il Copy a Risposta Diretta | Identico |
| 281 | `eBvEH3TPqSA` | Marketing a risposta diretta &#124; Qual è la differenza tra brand e categoria? | Diverso/localizzato; stesso ID verificato |
| 282 | `9lPjA4n3UB4` | Come trovare Clienti senza un brand forte | Diverso/localizzato; stesso ID verificato |
| 283 | `DcnlHK3p9u8` | Come Tenere I Clienti Incollati Al Tuo Brand (E Proteggerti dai Competitor) | Identico |
| 284 | `DgbZMAqw4NY` | REPUTAZIONE DEL BRAND &#124; Come EVITARE ERRORI e gestire la crisi | Identico |
| 285 | `N547HVgrQmk` | Proteggere il BRAND da Joint Venture nocive | Identico |
| 286 | `Hs8y1wNyamo` | IL PROCESSO DI VENDITA ideale per generare clienti in TARGET | Diverso/localizzato; stesso ID verificato |
| 287 | `7tWAsKiB0-Q` | MARKETING &#124; La struttura a forma di Lettera di Vendita in busta | Diverso/localizzato; stesso ID verificato |
| 288 | `qX8bJHUIDjI` | Strategie di Marketing &#124; I 3 Step di Dan Kennedy per aumentare le vendite | Diverso/localizzato; stesso ID verificato |
| 289 | `fpX3evEGoHY` | [Tecniche di Vendita] Come vendere fornendo la prova | Identico |
| 290 | `kGEOki4orFg` | [Tecniche di Vendita] Perchè utilizzare il sistema Plug and Play | Identico |
| 291 | `Ldy_Av2G1SA` | 🔴 Crescita Aziendale: Come Portare la Tua PMI da Zero al Successo (Strategia Completa 2025) | Diverso/localizzato; stesso ID verificato |
| 292 | `GUolZGprkP8` | BUDGET per MARKETING &#124; Come capire quanto investire per il Paccone? | Identico |
| 293 | `GdSf3-b_aIQ` | 🔴 Perché Delegare il Marketing Strategico è il Tuo ERRORE Più Costoso | Diverso/localizzato; stesso ID verificato |
| 294 | `oqoMqLQl9G4` | Come Rendere Il Tuo Business Stagionale Una Fonte Di Reddito Costante | Diverso/localizzato; stesso ID verificato |
| 295 | `5FEOsDJ5HAU` | Come Affrontare Una Crisi Aziendale E Trasformarla In Opportunità In 5 Semplici Passi | Diverso/localizzato; stesso ID verificato |
| 296 | `yZsBzaiH_Ic` | Franchising: Opportunità o Trappola? Come Espandere La Tua Azienda Senza Farti Male | Identico |
| 297 | `2tWslHOkxIc` | Seleziona i Collaboratori Perfetti: 2 Tecniche Provate per Imprenditori di Successo | Identico |
| 298 | `v2LEVo40O_w` | Come Generare Flusso di Cassa In Anticipo Nella Tua Azienda | Identico |
| 299 | `dt5NN20BeOY` | 7 Numeri Che Devi Conoscere Per Far Decollare La Tua Azienda | Diverso/localizzato; stesso ID verificato |
| 300 | `Fo8PB_7fE60` | COME FARE IMPRESA &#124; L’organigramma di un’azienda moderna | Diverso/localizzato; stesso ID verificato |

## Copertura e limiti temporali

- 279 `6sNjbCGzd2A`: coda non coperta **0.920 s**, copertura 99.80%.
- 281 `eBvEH3TPqSA`: coda non coperta **3.370 s**, copertura 99.58%.
- 285 `N547HVgrQmk`: coda non coperta **0.541 s**, copertura 99.37%.
- 286 `Hs8y1wNyamo`: coda non coperta **0.500 s**, copertura 99.95%.
- 287 `7tWAsKiB0-Q`: coda non coperta **0.770 s**, copertura 99.74%.
- 288 `qX8bJHUIDjI`: coda non coperta **0.310 s**, copertura 99.76%.
- 292 `GUolZGprkP8`: coda non coperta **0.511 s**, copertura 98.89%.
- 298 `v2LEVo40O_w`: coda non coperta **2.240 s**, copertura 99.85%.
- 299 `dt5NN20BeOY`: coda non coperta **6.120 s**, copertura 99.90%.
- 300 `Fo8PB_7fE60`: coda non coperta **0.361 s**, copertura 99.94%.

Copertura minima **98.89%**, massima **100%**; sforamento massimo **+2.240 s**. Anche gli inizi non coperti sono espliciti nella tabella. Nessuna perdita nella conversione: eventuale parlato nelle code non verificato con ascolto; nessun testo inventato o ASR aggiunto per pareggiare la durata metadata.

## Keyframe selettivi

**25 PNG su 7 video**, tutti ispezionati.

| Pos. | File sotto sources/transcripts/ID-frames/ | Contenuto tecnico |
|---:|---|---|
| 276 | `KipX0tAAWr4-510.png` | Lavagna con piccola sequenza manoscritta e frecce; testi secondari minuti. |
| 276 | `KipX0tAAWr4-1974.png` | Pacco aperto con libri e magazine; lavagna parzialmente coperta dal relatore. |
| 280 | `nKOvJg4lq6k-1658.png` | Slide con tre loghi leggibili: Gmail, Google Ads, Facebook ads. |
| 280 | `nKOvJg4lq6k-2444.png` | Slide esempio con una prima riga di testo leggibile. |
| 280 | `nKOvJg4lq6k-2612.png` | Stessa slide con due righe di testo leggibili. |
| 280 | `nKOvJg4lq6k-2770.png` | Stessa slide completa di tre righe di esempio, leggibili. |
| 280 | `nKOvJg4lq6k-2830.png` | Ritorno alla slide con i tre loghi; non contiene le tre headline. |
| 288 | `qX8bJHUIDjI-1032.png` | Slide 5, triangolo Message / Market / Media completo e leggibile. |
| 288 | `qX8bJHUIDjI-1195.png` | Slide 7, pagina testuale in inglese con neretti e sottolineature leggibili. |
| 288 | `qX8bJHUIDjI-1265.png` | Relatore sul palco; pagina citata fuori campo. |
| 288 | `qX8bJHUIDjI-1285.png` | Secondo campione dello stesso rinvio: relatore; pagina ancora fuori campo. |
| 293 | `GdSf3-b_aIQ-2960.png` | Primo stato della slide animata: solo blocco Prodotto o servizio. |
| 293 | `GdSf3-b_aIQ-3120.png` | Schema completo con blocchi colorati, frecce e testi leggibili. |
| 298 | `v2LEVo40O_w-260.png` | Titolo I Quadranti del Cash Flow; nessun diagramma in questo campione. |
| 298 | `v2LEVo40O_w-300.png` | Slide introduttiva con tre punti testuali leggibili. |
| 298 | `v2LEVo40O_w-1395.png` | Slide Conclusione con elenco testuale leggibile; nessun quadrante geometrico. |
| 299 | `dt5NN20BeOY-235.png` | Lavagna con ruoli manoscritti; slide sul bordo sinistro quasi interamente fuori campo. |
| 299 | `dt5NN20BeOY-245.png` | Lavagna e relatore; slide ATV tagliata sul bordo sinistro. |
| 299 | `dt5NN20BeOY-1486.png` | Slide della formula LTGM con ARPU, margine lordo e churn, interamente leggibile. |
| 299 | `dt5NN20BeOY-1770.png` | Esempio numerico proiettato: 100, 70%, 5%, 1400 leggibili; bordo superiore tagliato. |
| 299 | `dt5NN20BeOY-2960.png` | Relatore e lavagna; slide sul bordo sinistro quasi interamente fuori campo. |
| 299 | `dt5NN20BeOY-2975.png` | Slide negozio arredamento con 200 e 150 leggibili; testo destro tagliato. |
| 300 | `Fo8PB_7fE60-42.png` | Organigramma circolare dietro al relatore; visibile solo la parte inferiore. |
| 300 | `Fo8PB_7fE60-389.png` | Primo piano: ruota ancora tagliata, porzioni di etichette visibili. |
| 300 | `Fo8PB_7fE60-649.png` | Primo piano: organigramma ancora incompleto in inquadratura. |

Nessuna scansione frame-per-frame. Estratti di 2 secondi con `scripts/extract_keyframes.py --youtube`, frame a circa +1 s rispetto al timestamp nel nome. PNG decodificati e ispezionati. Campioni aggiuntivi solo sui medesimi rinvii quando la slide era incompleta, fuori campo o tagliata. Descrizioni soltanto tecniche, nessuna interpretazione semantica. Le menzioni generiche di grafica, pagine web, formule verbali o dimostrazioni ipotetiche non hanno attivato acquisizioni indiscriminate.

Limiti specifici:
- 276: parte della lavagna è minuta o coperta; non viene certificata la leggibilità di ogni annotazione.
- 288: pagina citata a 21:02 non recuperata nei due campioni 1265/1285; triangolo e pagina precedente recuperati. Eventuale ulteriore punto preciso può essere richiesto da ChatGPT.
- 298: i campioni del rinvio ai quadranti mostrano slide testuali, non una matrice grafica completa; non si presume di aver recuperato un diagramma assente.
- 299: slide ATV e parte dell'esempio finale restano fuori campo/tagliate; formula LTGM recuperata integralmente e relativo esempio numerico leggibile.
- 300: organigramma mai interamente visibile nei tre punti selezionati; conservati i campioni e segnalato il limite, senza ricostruirne le parti assenti.

## Validazione e invarianti

- Validator prima/dopo: **842 / 842**, output integrale identico, exit 1 storico. Composizione: 836 `Ordine/stato incoerente`, 3 `File congelato modificato`, 3 `Contatore STATUS errato`. Nessuna correzione fuori scope.
- SHA256 baseline: `5dc3f10e05da70edad694a7974f70968bf2a53570c72008ea06b09121af3d54c`.
- `git diff --check` pulito, anche sul delta completo dalla base.
- Diff dalla base vuoto per MASTER_PLAN.md, system/RULES.md, system/PHASES.md, system/HANDOFFS.md, system/FROZEN_FILES.md e merenda/.
- Invariati anche review esistenti, catalog.json, VIDEO_INDEX.md, QUEUE.md, scripts/classify_residual.py, riprioritizzazione e tutti gli script versionati.
- Nessuna nuova `.review.md`; nessun contenuto marcato STUDIATO o ESCLUSO; nessuna categoria modificata.
- Delta limitato a STATUS.md, acquisition-progress.md, next-batch.txt e asset dei soli 25 ID autorizzati. Nessun nuovo asset del nuovo 301 o successivi.
- Chiusura Git: 26 commit dalla base, nessun merge, working tree pulito e HEAD locale == origin/acquisition-276-300 dopo il push finale; SHA finale riportata nella consegna.

Log e verifiche riproducibili locali: `work/tmp/acquisition-276-300/` (ingest.log, ingest-sandbox.log, verify.py, checks.json, visual-signals.txt, frames-*.log, validator-before.txt e validator-after.txt). I log grezzi con URL temporanei restano locali, fuori dal tree versionato.

## Handoff

**FASE 7 — batch ottimizzato 276–300 completata.**

**Semantica ferma a 275. Nessun contenuto marcato STUDIATO o ESCLUSO.**

**Prossimo agente: CHATGPT.**

**Prossima azione: revisione semantica 276–300, fasi 8–13 + Weighted Novelty.** Primo: 276 KipX0tAAWr4; ultimo: 300 Fo8PB_7fE60.

**Prossimo checkpoint Claude: 300 — FASE 14 + FASE 15.**

Nessuna revisione semantica iniziata. Nessun batch successivo deciso: la decisione dopo 300 dipenderà dalla Weighted Novelty misurata da ChatGPT.
