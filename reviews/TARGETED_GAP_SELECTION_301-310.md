# Selezione gap mirati 301–310 — post checkpoint 300

Data operativa: 15 settembre 2026.

Base canonica: `91a07e2cc81d58cbc135e2e0bdb89f2d1d514d0f` — checkpoint 300 chiuso con decisione **B — continuare Merenda solo su gap mirati**.

Questo documento non modifica la Information Priority dei 168 residui. Esegue una **seconda selezione interna ai 59 TARGETED** per scegliere un micro-batch che massimizzi information gain atteso. Nessun contenuto 301+ viene acquisito o studiato in questa fase.

## Decisione

Dimensione ottimale: **10 contenuti**.

Perché 10 e non 25:

- MUST STUDY residui = 0;
- Weighted Novelty dell'ultimo batch = 17/50 = 34%;
- i TARGETED rimasti sono per lo più B e concentrati in aree già dense;
- 10 contenuti bastano per testare sei gap operativi e quattro case-probe senza impegnarsi in un altro ciclo lungo;
- dopo la semantica 301–310 si misura di nuovo la Weighted Novelty e si decide se aprire una seconda micro-selezione.

La selezione usa cinque fattori: **gap coverage, temporal precedence, specificità del meccanismo, trasferibilità, costo/rischio di dedup**. Lo score 0–100 è un indice di triage, non una misura di verità dottrinale.

## Micro-batch selezionato — nuove posizioni logiche 301–310

| Nuova pos. | Vecchia pos. | ID | Area | Data | Durata | Classe | Score | Novelty attesa | Titolo | Perché ora |
|---:|---:|---|---|---|---:|:---:|---:|:---:|---|---|
| 301 | 310 | `GFrT89AGv50` | 09_business | n/d | 17:55 | B | 92 | 2 | A Practical Guide to Exiting: How to Prepare Your Business and Turn It Into a Gold Mine | Gap netto su exit readiness e preparazione alla cessione: la KB parla di trasferibilità, ma non possiede ancora un framework dedicato a rendere l'impresa vendibile e valorizzabile. |
| 302 | 364 | `rEtbwMHdJcM` | 10_casi_studio | 2025-04-09 | 62:41 | B | 90 | 2 | Le Iene and the Roberto Re Case: How to Protect Yourself and Your Company? | Caso del 9 aprile 2025, successivo al nodo crisis management basato sul 2023: alto valore come test di prevalenza temporale e applicazione reputazionale reale. |
| 303 | 324 | `phMz5WxmXRo` | 09_business | n/d | 3:07 | B | 88 | 2 | MARKETING \ &#124; Come gestire il Marketing nell'azienda di Famiglia | Governance/marketing nell'azienda familiare non ha un nodo dedicato; può introdurre confini fra proprietà, ruoli, decisione strategica e gestione operativa. |
| 304 | 325 | `49CpCqYaXFA` | 09_business | n/d | 1:56 | B | 84 | 1 | FONDI DI INVESTIMENTO \ &#124; Perchè NON devono entrare in azienda | Ingresso di fondi/investitori è un gap sul capitale e sul controllo societario: patrimonializzazione tratta reinvestimento interno, non ancora governance dell'equity esterno. |
| 305 | 306 | `RM9YvT6K9IQ` | 09_business | n/d | 4:24 | B | 83 | 1 | How to Choose the Right EMPLOYEES to Grow Your Business | Dopo recruiting e role design resta un gap su criteri/metodo di selezione prima dell'ingresso; video breve, costo di revisione basso. |
| 306 | 326 | `8uQMbmRHUmk` | 09_business | n/d | 3:30 | B | 82 | 1 | COLLABORATORE DANNOSO \ &#124; Eliminare le mele marce in Azienda | Può completare la gestione del personale sul lato performance/cultura/offboarding, distinto dal solo recruiting e dal turnover commerciale. |
| 307 | 308 | `eGt2WUGelbU` | 10_casi_studio | n/d | 2:49 | A | 80 | 1 | INCASSI STELLARI di una Clinica Medica grazie al MARKETING di Metodo Merenda | Caso clinica medica, vecchia classe A e video molto breve: probe efficiente su marketing di servizi professionali ad alta fiducia e capacità di trasferire la dottrina. |
| 308 | 357 | `LtFeqet7OFc` | 10_casi_studio | 2025-09-03 | 23:26 | B | 79 | 1 | GELATERIA WALLY MILAN \ &#124; The Brutal Truth About the Ice Cream You Eat Every Day | Contenuto datato 3 settembre 2025, il più recente fra i TARGETED: probe di prevalenza temporale su focus, categoria, prodotto ed esperienza. |
| 309 | 358 | `dftLQTuK0cY` | 10_casi_studio | 2025-08-20 | 25:21 | B | 78 | 1 | CAMMI GOMME PIACENZA: The Tire Dealer That Doesn't Look Like a Tire Dealer | Caso 20 agosto 2025 su un servizio locale/commodity: utile per stress-testare differenziazione e positioning in un mercato apparentemente poco differenziabile. |
| 310 | 340 | `wDRHWHNHP5c` | 10_casi_studio | 2025-08-06 | 18:59 | B | 77 | 1 | EUROPA 92 a Modena: Il Ristorante Di Pavarotti Dove I Food Blogger Non Entrano | Caso 6 agosto 2025: verifica recente del rapporto fra autorità, reputazione, marketing e domanda in un'attività locale. |

### Composizione

- **6 gap/probe operativi:** exit/cessione, crisis update, azienda familiare, capitale esterno, selezione personale, collaboratore dannoso.
- **4 case-probe:** clinica medica, Gelateria Wally, Cammi Gomme, Europa 92/Pavarotti.
- prior Weighted Novelty attesa: **13/20**. È soltanto una previsione; la metrica reale verrà assegnata da ChatGPT dopo lettura integrale dei transcript.

## Tier di riserva

I seguenti 12 rimangono TARGETED ma non entrano nel primo micro-batch. Sono i primi candidati se il 301–310 produce novelty sufficiente:

| ID | Score | Titolo | Motivo del rinvio |
|---|---:|---|---|
| `-HLNTlFhGW8` | 74 | Come Espandere il Tuo Business con 2 Regole Semplici ma Potenti | Possibile estensione delle regole di espansione, ma il nodo è diventato molto denso dopo 296; utile solo come seconda linea. |
| `H23lJVsXUjo` | 73 | FRANCHISING \ &#124; Svelati TUTTI i retroscena di Posta Power dal CDA Metodo Merenda | Caso franchising lungo e potenzialmente ricco, ma precedente al framework 2024 già integrato; alto costo e rischio dedup. |
| `4i7ISpIeXNw` | 72 | After-Sales Support: How Follow-Up Determines Your Brand's Fate | After-sales era un gap forte prima di 283/291; ora customer success lo copre ampiamente, quindi resta solo come verifica mirata. |
| `5aI9CBLFH1k` | 71 | [Professional Sales] The lever of public recognition | Riconoscimento pubblico può aggiungere un dettaglio sugli incentivi, ma rete vendita contiene già premi, contest e recognition. |
| `Nk5BZqfkO-A` | 70 | Il Sistema Di Offerte Spilla Soldi Mai Rivelato Dalle Big Company | Potenziale meccanismo di architettura offerte; se il primo batch rende bene può stress-testare il nodo offerta già molto maturo. |
| `-6TU0HZ8cQo` | 69 | Come Rendere La Tua Azienda Ricca e Inattaccabile Dai Concorrenti | Possibile contributo su moat/resilienza competitiva, ma titolo ampio e rischio di ricombinare principi già presenti. |
| `RNsDovlfwK8` | 68 | L'unico Sistema Valido E Testato Per Guidare Un'Azienda Che Guadagna Davvero | Potenziale operating system d'impresa; molto ampio, quindi utile solo se emergono gap dopo il mini-batch. |
| `jI___z2yDMM` | 67 | How to Market Your Business Even If You Have Little Money | Marketing con poco capitale può estendere partire-da-zero/budget, ma le basi bootstrap sono già coperte. |
| `wg3tWYf6iho` | 66 | #11 Controversial Truths to Scale Your Business Fast | Scaling può contenere regole specifiche, ma l'area scalabilità è già densa; lungo e ad alto rischio di conferma. |
| `nn33VweEdB0` | 65 | Come Trasformare Una Clinica Estetica In Un Business Milionario Grazie Al Marketing | Caso clinica estetica lungo: settore vicino ai servizi professionali, ma viene dopo il probe più economico eGt2WUGelbU. |
| `A9aD8P9W6BM` | 64 | I SEGRETI DEL BRAND POSITIONING \ &#124; Creare Campagne Online di Successo [Case History] | Case positioning molto breve e a basso costo, ma posizionamento è già una delle aree più mature. |
| `S6XcqyhsjGw` | 63 | DON PEPPINU: Gelato Verace \ &#124; How to Create a Category and Dominate the Market [VLOG] | Caso creazione categoria potenzialmente utile, ma alta probabilità di confermare focus/category già canonici. |

## Classificazione completa dei 59 TARGETED

| Vecchia pos. | ID | Area | Classe | Data | Durata | Tier | Score | Titolo | Razionale |
|---:|---|---|:---:|---|---:|---|---:|---|---|
| 310 | `GFrT89AGv50` | 09_business | B | n/d | 17:55 | SELECTED | 92 | A Practical Guide to Exiting: How to Prepare Your Business and Turn It Into a Gold Mine | Gap netto su exit readiness e preparazione alla cessione: la KB parla di trasferibilità, ma non possiede ancora un framework dedicato a rendere l'impresa vendibile e valorizzabile. |
| 364 | `rEtbwMHdJcM` | 10_casi_studio | B | 2025-04-09 | 62:41 | SELECTED | 90 | Le Iene and the Roberto Re Case: How to Protect Yourself and Your Company? | Caso del 9 aprile 2025, successivo al nodo crisis management basato sul 2023: alto valore come test di prevalenza temporale e applicazione reputazionale reale. |
| 324 | `phMz5WxmXRo` | 09_business | B | n/d | 3:07 | SELECTED | 88 | MARKETING \ &#124; Come gestire il Marketing nell'azienda di Famiglia | Governance/marketing nell'azienda familiare non ha un nodo dedicato; può introdurre confini fra proprietà, ruoli, decisione strategica e gestione operativa. |
| 325 | `49CpCqYaXFA` | 09_business | B | n/d | 1:56 | SELECTED | 84 | FONDI DI INVESTIMENTO \ &#124; Perchè NON devono entrare in azienda | Ingresso di fondi/investitori è un gap sul capitale e sul controllo societario: patrimonializzazione tratta reinvestimento interno, non ancora governance dell'equity esterno. |
| 306 | `RM9YvT6K9IQ` | 09_business | B | n/d | 4:24 | SELECTED | 83 | How to Choose the Right EMPLOYEES to Grow Your Business | Dopo recruiting e role design resta un gap su criteri/metodo di selezione prima dell'ingresso; video breve, costo di revisione basso. |
| 326 | `8uQMbmRHUmk` | 09_business | B | n/d | 3:30 | SELECTED | 82 | COLLABORATORE DANNOSO \ &#124; Eliminare le mele marce in Azienda | Può completare la gestione del personale sul lato performance/cultura/offboarding, distinto dal solo recruiting e dal turnover commerciale. |
| 308 | `eGt2WUGelbU` | 10_casi_studio | A | n/d | 2:49 | SELECTED | 80 | INCASSI STELLARI di una Clinica Medica grazie al MARKETING di Metodo Merenda | Caso clinica medica, vecchia classe A e video molto breve: probe efficiente su marketing di servizi professionali ad alta fiducia e capacità di trasferire la dottrina. |
| 357 | `LtFeqet7OFc` | 10_casi_studio | B | 2025-09-03 | 23:26 | SELECTED | 79 | GELATERIA WALLY MILAN \ &#124; The Brutal Truth About the Ice Cream You Eat Every Day | Contenuto datato 3 settembre 2025, il più recente fra i TARGETED: probe di prevalenza temporale su focus, categoria, prodotto ed esperienza. |
| 358 | `dftLQTuK0cY` | 10_casi_studio | B | 2025-08-20 | 25:21 | SELECTED | 78 | CAMMI GOMME PIACENZA: The Tire Dealer That Doesn't Look Like a Tire Dealer | Caso 20 agosto 2025 su un servizio locale/commodity: utile per stress-testare differenziazione e positioning in un mercato apparentemente poco differenziabile. |
| 340 | `wDRHWHNHP5c` | 10_casi_studio | B | 2025-08-06 | 18:59 | SELECTED | 77 | EUROPA 92 a Modena: Il Ristorante Di Pavarotti Dove I Food Blogger Non Entrano | Caso 6 agosto 2025: verifica recente del rapporto fra autorità, reputazione, marketing e domanda in un'attività locale. |
| 311 | `-HLNTlFhGW8` | 09_business | A | n/d | 15:34 | RESERVE | 74 | Come Espandere il Tuo Business con 2 Regole Semplici ma Potenti | Possibile estensione delle regole di espansione, ma il nodo è diventato molto denso dopo 296; utile solo come seconda linea. |
| 341 | `H23lJVsXUjo` | 10_casi_studio | A | 2023-10-14 | 99:48 | RESERVE | 73 | FRANCHISING \ &#124; Svelati TUTTI i retroscena di Posta Power dal CDA Metodo Merenda | Caso franchising lungo e potenzialmente ricco, ma precedente al framework 2024 già integrato; alto costo e rischio dedup. |
| 318 | `4i7ISpIeXNw` | 06_vendita | A | n/d | n/d | RESERVE | 72 | After-Sales Support: How Follow-Up Determines Your Brand's Fate | After-sales era un gap forte prima di 283/291; ora customer success lo copre ampiamente, quindi resta solo come verifica mirata. |
| 327 | `5aI9CBLFH1k` | 06_vendita | B | n/d | 12:37 | RESERVE | 71 | [Professional Sales] The lever of public recognition | Riconoscimento pubblico può aggiungere un dettaglio sugli incentivi, ma rete vendita contiene già premi, contest e recognition. |
| 344 | `Nk5BZqfkO-A` | 09_business | B | n/d | 25:40 | RESERVE | 70 | Il Sistema Di Offerte Spilla Soldi Mai Rivelato Dalle Big Company | Potenziale meccanismo di architettura offerte; se il primo batch rende bene può stress-testare il nodo offerta già molto maturo. |
| 346 | `-6TU0HZ8cQo` | 09_business | B | n/d | 20:50 | RESERVE | 69 | Come Rendere La Tua Azienda Ricca e Inattaccabile Dai Concorrenti | Possibile contributo su moat/resilienza competitiva, ma titolo ampio e rischio di ricombinare principi già presenti. |
| 347 | `RNsDovlfwK8` | 09_business | B | n/d | 39:16 | RESERVE | 68 | L'unico Sistema Valido E Testato Per Guidare Un'Azienda Che Guadagna Davvero | Potenziale operating system d'impresa; molto ampio, quindi utile solo se emergono gap dopo il mini-batch. |
| 335 | `jI___z2yDMM` | 09_business | B | n/d | 17:35 | RESERVE | 67 | How to Market Your Business Even If You Have Little Money | Marketing con poco capitale può estendere partire-da-zero/budget, ma le basi bootstrap sono già coperte. |
| 361 | `wg3tWYf6iho` | 09_business | B | n/d | 67:31 | RESERVE | 66 | #11 Controversial Truths to Scale Your Business Fast | Scaling può contenere regole specifiche, ma l'area scalabilità è già densa; lungo e ad alto rischio di conferma. |
| 363 | `nn33VweEdB0` | 10_casi_studio | B | n/d | 67:33 | RESERVE | 65 | Come Trasformare Una Clinica Estetica In Un Business Milionario Grazie Al Marketing | Caso clinica estetica lungo: settore vicino ai servizi professionali, ma viene dopo il probe più economico eGt2WUGelbU. |
| 365 | `A9aD8P9W6BM` | 10_casi_studio | B | n/d | 2:43 | RESERVE | 64 | I SEGRETI DEL BRAND POSITIONING \ &#124; Creare Campagne Online di Successo [Case History] | Case positioning molto breve e a basso costo, ma posizionamento è già una delle aree più mature. |
| 366 | `S6XcqyhsjGw` | 10_casi_studio | B | n/d | 11:50 | RESERVE | 63 | DON PEPPINU: Gelato Verace \ &#124; How to Create a Category and Dominate the Market [VLOG] | Caso creazione categoria potenzialmente utile, ma alta probabilità di confermare focus/category già canonici. |
| 307 | `Cc5IllVUUy4` | 09_business | A | n/d | 2:47 | HOLD | 57 | AGENZIA DI MARKETING \ &#124; Perchè NON puoi delegare il Marketing | Marketing generalista: la KB è già molto densa; serve prima esaurire gap più specifici. |
| 302 | `7khsng5QpSs` | 09_business | B | 2024-08-20 | 4:42 | HOLD | 54 | How to Double Your Company's Results in Just 6 Months | TARGETED valido ma con information gain atteso inferiore ai gap selezionati; tenuto in HOLD per rivalutazione dopo il batch. |
| 319 | `bfH2NqlcGzw` | 09_business | B | 2024-04-06 | 1:50 | HOLD | 54 | LE TRUFFE per FARE SOLDI con gli E-Commerce Automatizzati | Tema e-commerce/scam contingente: trasferibilità inferiore rispetto ai gap strutturali selezionati. |
| 301 | `asMedYJtd4I` | 09_business | B | n/d | 1:47 | HOLD | 52 | CONCORRENZA SLEALE dei dipendenti? | TARGETED valido ma con information gain atteso inferiore ai gap selezionati; tenuto in HOLD per rivalutazione dopo il batch. |
| 320 | `KvISQI3qS5w` | 09_business | B | n/d | 2:46 | HOLD | 52 | CREATING AN E-COMMERCE \ &#124; The best way NOT to sell | Tema e-commerce/scam contingente: trasferibilità inferiore rispetto ai gap strutturali selezionati. |
| 321 | `lV-ZZx5T5L4` | 09_business | B | n/d | 4:23 | HOLD | 52 | 3 Mistakes to Avoid to Build a Successful Business | TARGETED valido ma con information gain atteso inferiore ai gap selezionati; tenuto in HOLD per rivalutazione dopo il batch. |
| 303 | `wqo0CMzCsYY` | 09_business | B | 2024-05-28 | 2:24 | HOLD | 51 | The ONE RULE to apply to become a MILLIONAIRE ENTREPRENEUR | Tema business ampio/personale: bassa specificità del meccanismo e alta probabilità di ricombinare principi già canonizzati. |
| 304 | `O5YdmHmfnAw` | 09_business | B | 2024-04-09 | 4:28 | HOLD | 51 | La TUA VITA è un INFERNO e non riesci a GUADAGNARE come vorresti? | Tema business ampio/personale: bassa specificità del meccanismo e alta probabilità di ricombinare principi già canonizzati. |
| 312 | `KhWKRvXYNFk` | 06_vendita | A | n/d | 3:40 | HOLD | 51 | [Tecniche per la Vendita Professionale] Simbolismo e Autorità | Vendita è area satura; nessun gap abbastanza distinto da giustificare il primo micro-batch. |
| 330 | `8E8Cj1F0V9M` | 09_business | B | n/d | 11:35 | HOLD | 50 | Amazon is no longer an e-commerce site: it's now 100% Merenda Method | Tema e-commerce/scam contingente: trasferibilità inferiore rispetto ai gap strutturali selezionati. |
| 332 | `i2_3ygDL148` | 09_business | B | n/d | 12:40 | HOLD | 50 | SALES TECHNIQUES \ &#124; What does it mean to be a Salesperson in a company? | TARGETED valido ma con information gain atteso inferiore ai gap selezionati; tenuto in HOLD per rivalutazione dopo il batch. |
| 333 | `JFb67cV2HfE` | 09_business | B | n/d | 17:39 | HOLD | 50 | Perché La Tua Azienda Non Cresce? Scopri L’errore Che Ti Costa Milioni! | TARGETED valido ma con information gain atteso inferiore ai gap selezionati; tenuto in HOLD per rivalutazione dopo il batch. |
| 334 | `9UxJuYEpf30` | 09_business | B | n/d | 15:39 | HOLD | 50 | Making Money with Your Business? Discover 2 Skills That Make a Difference | TARGETED valido ma con information gain atteso inferiore ai gap selezionati; tenuto in HOLD per rivalutazione dopo il batch. |
| 336 | `e0dqAD4ySaA` | 09_business | B | n/d | 11:52 | HOLD | 50 | How to build a successful business with MARKETING | Marketing generalista: la KB è già molto densa; serve prima esaurire gap più specifici. |
| 339 | `d7H5vX6zPQM` | 09_business | B | n/d | 13:24 | HOLD | 50 | HOW TO DO BUSINESS IN ITALY [and not in the USA] | TARGETED valido ma con information gain atteso inferiore ai gap selezionati; tenuto in HOLD per rivalutazione dopo il batch. |
| 343 | `jZ8iQZq-kP0` | 09_business | B | n/d | 20:29 | HOLD | 50 | HOW TO MARKET your company [Part 2] | TARGETED valido ma con information gain atteso inferiore ai gap selezionati; tenuto in HOLD per rivalutazione dopo il batch. |
| 348 | `DA_NpLZLn9U` | 09_business | B | n/d | 34:05 | HOLD | 50 | 3 Cose Da Cambiare Subito Per Creare Un’Azienda Che Genera Ricchezza | TARGETED valido ma con information gain atteso inferiore ai gap selezionati; tenuto in HOLD per rivalutazione dopo il batch. |
| 349 | `8u-1Ffgv4Gc` | 09_business | B | n/d | 55:23 | HOLD | 50 | La Mappa Del Marketing Per Generare Ricchezza e Solidità in Azienda | Marketing generalista: la KB è già molto densa; serve prima esaurire gap più specifici. |
| 351 | `ERpAPQPX9J0` | 09_business | B | n/d | 20:36 | HOLD | 50 | 5 Marketing Strategies to Get Your Business Off the Ground | Marketing generalista: la KB è già molto densa; serve prima esaurire gap più specifici. |
| 352 | `UD34Yfw_efE` | 09_business | B | n/d | 21:58 | HOLD | 50 | COME FARE MARKETING per la propria azienda [Parte 3] | Marketing generalista: la KB è già molto densa; serve prima esaurire gap più specifici. |
| 353 | `wGgXryNPbxg` | 09_business | B | n/d | 21:37 | HOLD | 50 | COME FARE MARKETING per la propria azienda [Parte 1] | Marketing generalista: la KB è già molto densa; serve prima esaurire gap più specifici. |
| 354 | `RlgpRIc7ljc` | 09_business | B | n/d | 22:11 | HOLD | 50 | Aumentare il fatturato della tua Azienda \ &#124; Il vero segreto | TARGETED valido ma con information gain atteso inferiore ai gap selezionati; tenuto in HOLD per rivalutazione dopo il batch. |
| 355 | `3vfZIcsrilc` | 09_business | B | n/d | 32:05 | HOLD | 50 | MARKETING \ &#124; 3 Azioni fondamentali per la tua Azienda | Marketing generalista: la KB è già molto densa; serve prima esaurire gap più specifici. |
| 322 | `jm6CRgEbWpE` | 09_business | B | n/d | 3:19 | HOLD | 49 | Quali abilità servono per diventare un imprenditore di successo? | Tema business ampio/personale: bassa specificità del meccanismo e alta probabilità di ricombinare principi già canonizzati. |
| 323 | `zDEL2i541CA` | 09_business | B | n/d | 1:53 | HOLD | 49 | INFLAZIONE \ &#124; Dove deve INVESTIRE un imprenditore per proteggere l'azienda | Tema business ampio/personale: bassa specificità del meccanismo e alta probabilità di ricombinare principi già canonizzati. |
| 350 | `UNsFL0TyO5Q` | 09_business | B | n/d | 2:43 | HOLD | 49 | Come investire i soldi della liquidità aziendale | Tema business ampio/personale: bassa specificità del meccanismo e alta probabilità di ricombinare principi già canonizzati. |
| 328 | `eGC1td6H3yE` | 09_business | B | n/d | 16:04 | HOLD | 47 | The #1 Marketing Investment to Get Excited Customers Who Only Talk About You | Tema business ampio/personale: bassa specificità del meccanismo e alta probabilità di ricombinare principi già canonizzati. |
| 329 | `_GL-3a90TJQ` | 09_business | B | 2023-10-05 | 5:50 | HOLD | 47 | Il MIGLIOR INVESTIMENTO per diventare ricchi | Tema business ampio/personale: bassa specificità del meccanismo e alta probabilità di ricombinare principi già canonizzati. |
| 331 | `VW36EYJReRU` | 09_business | B | n/d | 10:39 | HOLD | 47 | HOW TO BECOME A successful ENTREPRENEUR at 18? | Tema business ampio/personale: bassa specificità del meccanismo e alta probabilità di ricombinare principi già canonizzati. |
| 337 | `feaFaTbIP6s` | 09_business | B | n/d | 16:48 | HOLD | 47 | I VERI nemici dell’imprenditore [Che non vedi] | Tema business ampio/personale: bassa specificità del meccanismo e alta probabilità di ricombinare principi già canonizzati. |
| 338 | `jJszWli8eu8` | 09_business | B | n/d | 19:11 | HOLD | 47 | Entrepreneurship: 5 reasons not to start a business @FranchinoErCriminale | Tema business ampio/personale: bassa specificità del meccanismo e alta probabilità di ricombinare principi già canonizzati. |
| 342 | `kI5CD1rmIRg` | 06_vendita | B | n/d | 1:25 | HOLD | 47 | Vendita Professionale - Come identificare la voce narrante per scrivere un libro in Azienda? | Vendita è area satura; nessun gap abbastanza distinto da giustificare il primo micro-batch. |
| 345 | `JyGh1R6O3hg` | 09_business | B | n/d | 24:13 | HOLD | 47 | I 3 Investimenti Top Dei Ricchi Per Far Crescere Il Tuo Business | Tema business ampio/personale: bassa specificità del meccanismo e alta probabilità di ricombinare principi già canonizzati. |
| 356 | `pjrMVek56EU` | 09_business | B | n/d | 24:14 | HOLD | 47 | WHERE TO INVEST TODAY to make your business successful | Tema business ampio/personale: bassa specificità del meccanismo e alta probabilità di ricombinare principi già canonizzati. |
| 359 | `dFuZc7rFwgE` | 06_vendita | A | n/d | 76:56 | HOLD | 47 | Le TECNICHE DI VENDITA per diventare un Venditore di Successo | Vendita è area satura; nessun gap abbastanza distinto da giustificare il primo micro-batch. |
| 362 | `AZYdLrjgvK0` | 09_business | B | n/d | 9:54 | HOLD | 47 | Where NOT to Invest Your Money If You Want to Start a Business [That Won't Fail Immediately] | Tema business ampio/personale: bassa specificità del meccanismo e alta probabilità di ricombinare principi già canonizzati. |
| 360 | `7EY0X8kMJ0o` | 09_business | B | n/d | 69:11 | HOLD | 44 | 🔴 Direct Response Marketing: The Technique That Made Great Entrepreneurs Rich | Tema business ampio/personale: bassa specificità del meccanismo e alta probabilità di ricombinare principi già canonizzati. |

## Regola di stop dopo 301–310

Dopo la revisione semantica dei 10 contenuti:

- **Weighted Novelty ≥ 50%** o almeno 2 nuovi framework peso 2 → valutare una seconda micro-selezione dai RESERVE;
- **Weighted Novelty 25–50%** → proseguire solo sui singoli gap che restano aperti;
- **Weighted Novelty < 25%** e nessuna prevalenza temporale significativa → considerare la KB Merenda sostanzialmente satura e preparare il passaggio allo strato esterno/evidence.

La novelty binaria resta informativa ma la decisione usa soprattutto la metrica pesata.

## Invarianti

- righe 1–300 della queue byte-invariate;
- stessi 168 ID residui, nessun duplicato/perdita;
- tutti i 168 restano DA STUDIARE;
- nessun catalog/VIDEO_INDEX/KB/frozen modificato;
- nessun transcript o review 301+ creato;
- `RESIDUAL_REPRIORITIZATION_301-468.md` resta il report FASE15 storico e non viene sovrascritto.
