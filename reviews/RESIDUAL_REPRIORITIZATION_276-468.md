# Riprioritizzazione residua 276–468 — information gain

Data operativa: 15 settembre 2026.

Base canonica: `becb2d6a63cc7943331557f838f91d712c332283` — checkpoint 275 chiuso. Questo documento **non modifica lo stato semantico** dei contenuti: tutti i 193 residui restano `DA STUDIARE` finché non vengono realmente acquisiti e revisionati.

## Perché la coda è stata riprogettata

La coda storica ordinava i residui per sequenza precedente, ma dopo 275 revisioni il valore marginale non è più uniforme. Il novelty yield è passato dal **64% (16/25) nel batch 226–250** al **44% (11/25) nel 251–275**. Inoltre la KB è sbilanciata: vendita è già relativamente densa, mentre copy, brand e alcuni domini business hanno ancora gap evidenti.

La classificazione A/B/C del checkpoint 200 resta utile come **profondità iniziale di revisione**, ma non è più sufficiente come ordine di acquisizione. Viene quindi introdotta una variabile separata: **Information Priority**.

## Information Priority

- **MUST STUDY** — alta probabilità di colmare un gap reale, introdurre un framework distinto o aggiornare una regola importante.
- **TARGETED** — valore potenziale concreto, ma da studiare finché i batch precedenti mostrano novelty sufficiente o quando serve a risolvere un gap specifico.
- **LOW / DEFER** — alta probabilità di conferma, derivazione, caso ridondante, tema già saturo o formato storicamente a basso yield. Non significa esclusione: significa non acquisire automaticamente.

La priorità combina: saturazione della sezione KB, vecchia classe A/B/C, formato, recenza disponibile, presenza di procedure/framework specifici, trasferibilità operativa e sovrapposizione attesa con i nodi già canonici. Lo score usato per ordinare all'interno dei tier è **operativo e non dottrinale**; non sostituisce la revisione semantica.

## Riepilogo

| Priorità | N |
|---|---:|
| MUST STUDY | 15 |
| TARGETED | 76 |
| LOW / DEFER | 102 |
| **Totale** | **193** |

### Per area

| Area | MUST | TARGETED | LOW/DEFER | Totale |
|---|---:|---:|---:|---:|
| 06_vendita | 0 | 10 | 36 | 46 |
| 07_copy_comunicazione | 5 | 0 | 0 | 5 |
| 08_brand | 5 | 0 | 3 | 8 |
| 09_business | 5 | 57 | 25 | 87 |
| 10_casi_studio | 0 | 9 | 38 | 47 |

## Nuovo batch ottimizzato 276–300

Questo batch contiene **tutti i 15 MUST STUDY** più **10 TARGETED** scelti per diversità informativa e copertura dei gap. Composizione: **5 copy + 5 brand + 5 vendita + 10 business**.

| Nuova pos. | Vecchia pos. | ID | Area | Priorità | Titolo |
|---:|---:|---|---|---|---|
| 276 | 323 | `KipX0tAAWr4` | 07_copy_comunicazione | MUST STUDY | Why COPYWRITING starts with your positioning [Full Course] |
| 277 | 325 | `iuly2QEl9no` | 07_copy_comunicazione | MUST STUDY | Ice for the Eskimos - Direct Response Copywriting [Part 1] |
| 278 | 324 | `DTIhYJnLyGs` | 07_copy_comunicazione | MUST STUDY | Ice for the Eskimos - Direct Response Copywriting [Part 2] |
| 279 | 322 | `6sNjbCGzd2A` | 07_copy_comunicazione | MUST STUDY | How to Create an Effective Call to Action |
| 280 | 326 | `nKOvJg4lq6k` | 07_copy_comunicazione | MUST STUDY | COPYWRITING: Cos'é Oggi il Copy a Risposta Diretta |
| 281 | 329 | `eBvEH3TPqSA` | 08_brand | MUST STUDY | Direct Response Marketing \| What's the Difference Between a Brand and a Category? |
| 282 | 330 | `9lPjA4n3UB4` | 08_brand | MUST STUDY | How to Find Clients Without a Strong Brand |
| 283 | 327 | `DcnlHK3p9u8` | 08_brand | MUST STUDY | Come Tenere I Clienti Incollati Al Tuo Brand (E Proteggerti dai Competitor) |
| 284 | 328 | `DgbZMAqw4NY` | 08_brand | MUST STUDY | REPUTAZIONE DEL BRAND \| Come EVITARE ERRORI e gestire la crisi |
| 285 | 331 | `N547HVgrQmk` | 08_brand | MUST STUDY | Proteggere il BRAND da Joint Venture nocive |
| 286 | 276 | `Hs8y1wNyamo` | 06_vendita | TARGETED | THE ideal SALES PROCESS for generating TARGETED clients |
| 287 | 283 | `7tWAsKiB0-Q` | 06_vendita | TARGETED | MARKETING \| The Sales Letter in an Envelope Structure |
| 288 | 285 | `qX8bJHUIDjI` | 06_vendita | TARGETED | Marketing Strategies \| Dan Kennedy's 3 Steps to Increase Sales |
| 289 | 288 | `fpX3evEGoHY` | 06_vendita | TARGETED | [Tecniche di Vendita] Come vendere fornendo la prova |
| 290 | 290 | `kGEOki4orFg` | 06_vendita | TARGETED | [Tecniche di Vendita] Perchè utilizzare il sistema Plug and Play |
| 291 | 357 | `Ldy_Av2G1SA` | 09_business | TARGETED | 🔴 Business Growth: How to Take Your SMB from Zero to Success (Complete 2025 Strategy) |
| 292 | 341 | `GUolZGprkP8` | 09_business | MUST STUDY | BUDGET per MARKETING \| Come capire quanto investire per il Paccone? |
| 293 | 358 | `GdSf3-b_aIQ` | 09_business | TARGETED | 🔴 Why Delegating Strategic Marketing Is Your Most Costly MISTAKE |
| 294 | 359 | `oqoMqLQl9G4` | 09_business | TARGETED | How to Make Your Seasonal Business a Steady Source of Income |
| 295 | 363 | `5FEOsDJ5HAU` | 09_business | TARGETED | How to Tackle a Business Crisis and Turn It Into an Opportunity in 5 Simple Steps |
| 296 | 365 | `yZsBzaiH_Ic` | 09_business | MUST STUDY | Franchising: Opportunità o Trappola? Come Espandere La Tua Azienda Senza Farti Male |
| 297 | 368 | `2tWslHOkxIc` | 09_business | MUST STUDY | Seleziona i Collaboratori Perfetti: 2 Tecniche Provate per Imprenditori di Successo |
| 298 | 373 | `v2LEVo40O_w` | 09_business | MUST STUDY | Come Generare Flusso di Cassa In Anticipo Nella Tua Azienda |
| 299 | 374 | `dt5NN20BeOY` | 09_business | TARGETED | 7 Numbers You Must Know to Make Your Business Take Off |
| 300 | 391 | `Fo8PB_7fE60` | 09_business | MUST STUDY | HOW TO DO BUSINESS \| The organizational chart of a modern company |

Il vecchio primo residuo `Hs8y1wNyamo` non viene scartato: passa alla nuova posizione **286** perché resta informativo, ma non è più il miglior punto di partenza assoluto.

## Regola adattiva dopo il checkpoint 300

Il checkpoint 300 non deve generare automaticamente un nuovo batch cronologico. Misurare invece **Weighted Novelty**:

- **2** = nuovo nodo canonico, nuovo framework importante o modifica sostanziale di una regola;
- **1** = estensione realmente utile di un nodo esistente;
- **0** = conferma/dedup;
- registrare separatamente contraddizioni e prevalenze temporali.

Decisione indicativa dopo 300:

- novelty realmente incrementale **≈40% o più** → continuare con un nuovo batch TARGETED;
- **20–40%** → niente avanzamento sequenziale; acquisire solo gap specifici;
- **<20–25%** senza nuove contraddizioni recenti → considerare la KB Merenda sufficientemente satura e passare allo strato esterno/evidence mantenendo separata la KB Merenda.

## Mapping completo 193 residui

| Nuova pos. | Vecchia pos. | ID | Info priority | Vecchia classe | Area | Titolo | Razionale |
|---:|---:|---|---|:---:|---|---|---|
| 276 | 323 | `KipX0tAAWr4` | MUST STUDY | A | 07_copy_comunicazione | Why COPYWRITING starts with your positioning [Full Course] | Gap strutturale: sezione copy ancora piccola; contenuto core ad alta trasferibilità. |
| 277 | 325 | `iuly2QEl9no` | MUST STUDY | A | 07_copy_comunicazione | Ice for the Eskimos - Direct Response Copywriting [Part 1] | Gap strutturale: sezione copy ancora piccola; contenuto core ad alta trasferibilità. |
| 278 | 324 | `DTIhYJnLyGs` | MUST STUDY | A | 07_copy_comunicazione | Ice for the Eskimos - Direct Response Copywriting [Part 2] | Gap strutturale: sezione copy ancora piccola; contenuto core ad alta trasferibilità. |
| 279 | 322 | `6sNjbCGzd2A` | MUST STUDY | A | 07_copy_comunicazione | How to Create an Effective Call to Action | Gap strutturale: sezione copy ancora piccola; contenuto core ad alta trasferibilità. |
| 280 | 326 | `nKOvJg4lq6k` | MUST STUDY | A | 07_copy_comunicazione | COPYWRITING: Cos'é Oggi il Copy a Risposta Diretta | Gap strutturale: sezione copy ancora piccola; contenuto core ad alta trasferibilità. |
| 281 | 329 | `eBvEH3TPqSA` | MUST STUDY | A | 08_brand | Direct Response Marketing \| What's the Difference Between a Brand and a Category? | Distinzione concettuale potenzialmente canonica fra brand e categoria. |
| 282 | 330 | `9lPjA4n3UB4` | MUST STUDY | A | 08_brand | How to Find Clients Without a Strong Brand | Confine brand-acquisizione utile a chiarire cosa fare senza notorietà. |
| 283 | 327 | `DcnlHK3p9u8` | MUST STUDY | A | 08_brand | Come Tenere I Clienti Incollati Al Tuo Brand (E Proteggerti dai Competitor) | Retention/protezione del brand: area ancora poco sviluppata. |
| 284 | 328 | `DgbZMAqw4NY` | MUST STUDY | A | 08_brand | REPUTAZIONE DEL BRAND \| Come EVITARE ERRORI e gestire la crisi | Gap diretto su reputazione/crisis management, oggi quasi assente nella KB. |
| 285 | 331 | `N547HVgrQmk` | MUST STUDY | A | 08_brand | Proteggere il BRAND da Joint Venture nocive | Rischio/architettura di brand poco coperti; possibile regola operativa distinta. |
| 286 | 276 | `Hs8y1wNyamo` | TARGETED | B | 06_vendita | THE ideal SALES PROCESS for generating TARGETED clients | Processo vendita + target: conserva valore ma va deduplicato contro diagnosi/prequalifica. |
| 287 | 283 | `7tWAsKiB0-Q` | TARGETED | B | 06_vendita | MARKETING \| The Sales Letter in an Envelope Structure | Ponte copy-vendita specifico e poco coperto. |
| 288 | 285 | `qX8bJHUIDjI` | TARGETED | A | 06_vendita | Marketing Strategies \| Dan Kennedy's 3 Steps to Increase Sales | Framework esplicito numerato: alta probabilità di procedura riutilizzabile. |
| 289 | 288 | `fpX3evEGoHY` | TARGETED | B | 06_vendita | [Tecniche di Vendita] Come vendere fornendo la prova | Meccanismo preciso di prova nella vendita; possibile estensione distinta. |
| 290 | 290 | `kGEOki4orFg` | TARGETED | B | 06_vendita | [Tecniche di Vendita] Perchè utilizzare il sistema Plug and Play | Possibile procedura replicabile/standardizzazione da confrontare con script e rete vendita. |
| 291 | 357 | `Ldy_Av2G1SA` | TARGETED | B | 09_business | 🔴 Business Growth: How to Take Your SMB from Zero to Success (Complete 2025 Strategy) | Potenziale estensione operativa; da studiare solo finché il novelty yield resta sufficiente. |
| 292 | 341 | `GUolZGprkP8` | MUST STUDY | B | 09_business | BUDGET per MARKETING \| Come capire quanto investire per il Paccone? | Gap concreto su allocazione del budget marketing. |
| 293 | 358 | `GdSf3-b_aIQ` | TARGETED | A | 09_business | 🔴 Why Delegating Strategic Marketing Is Your Most Costly MISTAKE | Governance della delega: utile ma da deduplicare contro marketing-first/scalabilità. |
| 294 | 359 | `oqoMqLQl9G4` | TARGETED | B | 09_business | How to Make Your Seasonal Business a Steady Source of Income | Problema operativo specifico non ancora ben coperto: stabilizzare domanda/cassa stagionale. |
| 295 | 363 | `5FEOsDJ5HAU` | TARGETED | B | 09_business | How to Tackle a Business Crisis and Turn It Into an Opportunity in 5 Simple Steps | Framework operativo di gestione crisi, poco rappresentato. |
| 296 | 365 | `yZsBzaiH_Ic` | MUST STUDY | A | 09_business | Franchising: Opportunità o Trappola? Come Espandere La Tua Azienda Senza Farti Male | Espansione e controllo del modello: completa il nodo multibrand/scalabilità. |
| 297 | 368 | `2tWslHOkxIc` | MUST STUDY | A | 09_business | Seleziona i Collaboratori Perfetti: 2 Tecniche Provate per Imprenditori di Successo | Selezione/organizzazione persone: completa marketing del personale e scalabilità. |
| 298 | 373 | `v2LEVo40O_w` | MUST STUDY | A | 09_business | Come Generare Flusso di Cassa In Anticipo Nella Tua Azienda | Cash-flow operativo e anticipo incassi: alta utilità decisionale. |
| 299 | 374 | `dt5NN20BeOY` | TARGETED | B | 09_business | 7 Numbers You Must Know to Make Your Business Take Off | Framework numerico/KPI con alta trasferibilità operativa. |
| 300 | 391 | `Fo8PB_7fE60` | MUST STUDY | B | 09_business | HOW TO DO BUSINESS \| The organizational chart of a modern company | Gap organizzativo evidente: organigramma/struttura non hanno ancora un nodo dedicato. |
| 301 | 335 | `asMedYJtd4I` | TARGETED | B | 09_business | CONCORRENZA SLEALE dei dipendenti? | Potenziale estensione operativa; da studiare solo finché il novelty yield resta sufficiente. |
| 302 | 342 | `7khsng5QpSs` | TARGETED | B | 09_business | How to Double Your Company's Results in Just 6 Months | Potenziale estensione operativa; da studiare solo finché il novelty yield resta sufficiente. |
| 303 | 343 | `wqo0CMzCsYY` | TARGETED | B | 09_business | The ONE RULE to apply to become a MILLIONAIRE ENTREPRENEUR | Potenziale estensione operativa; da studiare solo finché il novelty yield resta sufficiente. |
| 304 | 344 | `O5YdmHmfnAw` | TARGETED | B | 09_business | La TUA VITA è un INFERNO e non riesci a GUADAGNARE come vorresti? | Potenziale estensione operativa; da studiare solo finché il novelty yield resta sufficiente. |
| 305 | 378 | `2QG4EBTT0Jk` | TARGETED | B | 09_business | Trasforma La Tua AZIENDA in Una Macchina STAMPA SOLDI [Con 3 Numeri] | Framework numerico/KPI con alta trasferibilità operativa. |
| 306 | 380 | `RM9YvT6K9IQ` | TARGETED | B | 09_business | How to Choose the Right EMPLOYEES to Grow Your Business | Selezione/organizzazione persone: completa marketing del personale e scalabilità. |
| 307 | 400 | `Cc5IllVUUy4` | TARGETED | A | 09_business | AGENZIA DI MARKETING \| Perchè NON puoi delegare il Marketing | Potenziale estensione operativa; da studiare solo finché il novelty yield resta sufficiente. |
| 308 | 441 | `eGt2WUGelbU` | TARGETED | A | 10_casi_studio | INCASSI STELLARI di una Clinica Medica grazie al MARKETING di Metodo Merenda | Caso verticale vicino a Formalife/servizi professionali: utile se produce principi nuovi, non per i numeri. |
| 309 | 340 | `ek1eEIYtgqk` | TARGETED | A | 09_business | MARKETING Investment with a 423% ROI [and 100% Conversion] | Potenziale estensione operativa; da studiare solo finché il novelty yield resta sufficiente. |
| 310 | 364 | `GFrT89AGv50` | TARGETED | B | 09_business | A Practical Guide to Exiting: How to Prepare Your Business and Turn It Into a Gold Mine | Potenziale estensione operativa; da studiare solo finché il novelty yield resta sufficiente. |
| 311 | 369 | `-HLNTlFhGW8` | TARGETED | A | 09_business | Come Espandere il Tuo Business con 2 Regole Semplici ma Potenti | Potenziale estensione operativa; da studiare solo finché il novelty yield resta sufficiente. |
| 312 | 298 | `KhWKRvXYNFk` | TARGETED | A | 06_vendita | [Tecniche per la Vendita Professionale] Simbolismo e Autorità | Vendita è più satura: mantenere solo finché introduce un meccanismo distinto. |
| 313 | 360 | `n25U2m__pnQ` | TARGETED | A | 09_business | Vuoi Guadagnare Di Più? 3 Regole (Testate) Per Riempire Il Tuo Conto Corrente Aziendale | Potenziale estensione operativa; da studiare solo finché il novelty yield resta sufficiente. |
| 314 | 405 | `KxYueziNHXM` | TARGETED | A | 09_business | You Spent €100,000 on CRM and It's Not Working? Here's Why (Frank Merenda Explains) | Tema già presente: utile solo se aggiunge meccanismi nuovi, quindi revisione mirata. |
| 315 | 409 | `upu5iqJUCgk` | TARGETED | A | 09_business | CRM and Customer Segmentation: The System That Separates Rich from Poor Entrepreneurs | Tema già presente: utile solo se aggiunge meccanismi nuovi, quindi revisione mirata. |
| 316 | 414 | `8TqBkL3xrzc` | TARGETED | A | 09_business | 💣 The World's Fastest Delegation Course: Just 1 Rule | Governance della delega: utile ma da deduplicare contro marketing-first/scalabilità. |
| 317 | 418 | `Javgw1LWl24` | TARGETED | A | 09_business | Cosa significa LIFETIME VALUE e perchè è un concetto chiave per l'Azienda #shorts | Tema già presente: utile solo se aggiunge meccanismi nuovi, quindi revisione mirata. |
| 318 | 312 | `4i7ISpIeXNw` | TARGETED | A | 06_vendita | After-Sales Support: How Follow-Up Determines Your Brand's Fate | Formato con yield storico più basso in un'area vendita ormai relativamente satura. |
| 319 | 345 | `bfH2NqlcGzw` | TARGETED | B | 09_business | LE TRUFFE per FARE SOLDI con gli E-Commerce Automatizzati | Bassa trasferibilità o alta probabilità di contenuto polemico/contingente già fuori dai gap prioritari. |
| 320 | 355 | `KvISQI3qS5w` | TARGETED | B | 09_business | CREATING AN E-COMMERCE \| The best way NOT to sell | Potenziale estensione operativa; da studiare solo finché il novelty yield resta sufficiente. |
| 321 | 379 | `lV-ZZx5T5L4` | TARGETED | B | 09_business | 3 Mistakes to Avoid to Build a Successful Business | Potenziale estensione operativa; da studiare solo finché il novelty yield resta sufficiente. |
| 322 | 382 | `jm6CRgEbWpE` | TARGETED | B | 09_business | Quali abilità servono per diventare un imprenditore di successo? | Potenziale estensione operativa; da studiare solo finché il novelty yield resta sufficiente. |
| 323 | 394 | `zDEL2i541CA` | TARGETED | B | 09_business | INFLAZIONE \| Dove deve INVESTIRE un imprenditore per proteggere l'azienda | Potenziale estensione operativa; da studiare solo finché il novelty yield resta sufficiente. |
| 324 | 395 | `phMz5WxmXRo` | TARGETED | B | 09_business | MARKETING \| Come gestire il Marketing nell'azienda di Famiglia | Potenziale estensione operativa; da studiare solo finché il novelty yield resta sufficiente. |
| 325 | 397 | `49CpCqYaXFA` | TARGETED | B | 09_business | FONDI DI INVESTIMENTO \| Perchè NON devono entrare in azienda | Potenziale estensione operativa; da studiare solo finché il novelty yield resta sufficiente. |
| 326 | 399 | `8uQMbmRHUmk` | TARGETED | B | 09_business | COLLABORATORE DANNOSO \| Eliminare le mele marce in Azienda | Potenziale estensione operativa; da studiare solo finché il novelty yield resta sufficiente. |
| 327 | 297 | `5aI9CBLFH1k` | TARGETED | B | 06_vendita | [Professional Sales] The lever of public recognition | Vendita è più satura: mantenere solo finché introduce un meccanismo distinto. |
| 328 | 339 | `eGC1td6H3yE` | TARGETED | B | 09_business | The #1 Marketing Investment to Get Excited Customers Who Only Talk About You | Potenziale estensione operativa; da studiare solo finché il novelty yield resta sufficiente. |
| 329 | 347 | `_GL-3a90TJQ` | TARGETED | B | 09_business | Il MIGLIOR INVESTIMENTO per diventare ricchi | Potenziale estensione operativa; da studiare solo finché il novelty yield resta sufficiente. |
| 330 | 349 | `8E8Cj1F0V9M` | TARGETED | B | 09_business | Amazon is no longer an e-commerce site: it's now 100% Merenda Method | Potenziale estensione operativa; da studiare solo finché il novelty yield resta sufficiente. |
| 331 | 350 | `VW36EYJReRU` | TARGETED | B | 09_business | HOW TO BECOME A successful ENTREPRENEUR at 18? | Potenziale estensione operativa; da studiare solo finché il novelty yield resta sufficiente. |
| 332 | 354 | `i2_3ygDL148` | TARGETED | B | 09_business | SALES TECHNIQUES \| What does it mean to be a Salesperson in a company? | Potenziale estensione operativa; da studiare solo finché il novelty yield resta sufficiente. |
| 333 | 362 | `JFb67cV2HfE` | TARGETED | B | 09_business | Perché La Tua Azienda Non Cresce? Scopri L’errore Che Ti Costa Milioni! | Potenziale estensione operativa; da studiare solo finché il novelty yield resta sufficiente. |
| 334 | 366 | `9UxJuYEpf30` | TARGETED | B | 09_business | Making Money with Your Business? Discover 2 Skills That Make a Difference | Potenziale estensione operativa; da studiare solo finché il novelty yield resta sufficiente. |
| 335 | 377 | `jI___z2yDMM` | TARGETED | B | 09_business | How to Market Your Business Even If You Have Little Money | Potenziale estensione operativa; da studiare solo finché il novelty yield resta sufficiente. |
| 336 | 381 | `e0dqAD4ySaA` | TARGETED | B | 09_business | How to build a successful business with MARKETING | Potenziale estensione operativa; da studiare solo finché il novelty yield resta sufficiente. |
| 337 | 385 | `feaFaTbIP6s` | TARGETED | B | 09_business | I VERI nemici dell’imprenditore [Che non vedi] | Potenziale estensione operativa; da studiare solo finché il novelty yield resta sufficiente. |
| 338 | 386 | `jJszWli8eu8` | TARGETED | B | 09_business | Entrepreneurship: 5 reasons not to start a business @FranchinoErCriminale | Potenziale estensione operativa; da studiare solo finché il novelty yield resta sufficiente. |
| 339 | 389 | `d7H5vX6zPQM` | TARGETED | B | 09_business | HOW TO DO BUSINESS IN ITALY [and not in the USA] | Potenziale estensione operativa; da studiare solo finché il novelty yield resta sufficiente. |
| 340 | 459 | `wDRHWHNHP5c` | TARGETED | B | 10_casi_studio | EUROPA 92 a Modena: Il Ristorante Di Pavarotti Dove I Food Blogger Non Entrano | Caso recente: priorità maggiore solo per possibile prevalenza/aggiornamento. |
| 341 | 461 | `H23lJVsXUjo` | TARGETED | A | 10_casi_studio | FRANCHISING \| Svelati TUTTI i retroscena di Posta Power dal CDA Metodo Merenda | Caso applicativo: studiare solo se serve a validare un gap o una regola ancora incerta. |
| 342 | 299 | `kI5CD1rmIRg` | TARGETED | B | 06_vendita | Vendita Professionale - Come identificare la voce narrante per scrivere un libro in Azienda? | Vendita è più satura: mantenere solo finché introduce un meccanismo distinto. |
| 343 | 348 | `jZ8iQZq-kP0` | TARGETED | B | 09_business | HOW TO MARKET your company [Part 2] | Potenziale estensione operativa; da studiare solo finché il novelty yield resta sufficiente. |
| 344 | 352 | `Nk5BZqfkO-A` | TARGETED | B | 09_business | Il Sistema Di Offerte Spilla Soldi Mai Rivelato Dalle Big Company | Potenziale estensione operativa; da studiare solo finché il novelty yield resta sufficiente. |
| 345 | 361 | `JyGh1R6O3hg` | TARGETED | B | 09_business | I 3 Investimenti Top Dei Ricchi Per Far Crescere Il Tuo Business | Potenziale estensione operativa; da studiare solo finché il novelty yield resta sufficiente. |
| 346 | 367 | `-6TU0HZ8cQo` | TARGETED | B | 09_business | Come Rendere La Tua Azienda Ricca e Inattaccabile Dai Concorrenti | Potenziale estensione operativa; da studiare solo finché il novelty yield resta sufficiente. |
| 347 | 370 | `RNsDovlfwK8` | TARGETED | B | 09_business | L'unico Sistema Valido E Testato Per Guidare Un'Azienda Che Guadagna Davvero | Potenziale estensione operativa; da studiare solo finché il novelty yield resta sufficiente. |
| 348 | 371 | `DA_NpLZLn9U` | TARGETED | B | 09_business | 3 Cose Da Cambiare Subito Per Creare Un’Azienda Che Genera Ricchezza | Potenziale estensione operativa; da studiare solo finché il novelty yield resta sufficiente. |
| 349 | 376 | `8u-1Ffgv4Gc` | TARGETED | B | 09_business | La Mappa Del Marketing Per Generare Ricchezza e Solidità in Azienda | Potenziale estensione operativa; da studiare solo finché il novelty yield resta sufficiente. |
| 350 | 383 | `UNsFL0TyO5Q` | TARGETED | B | 09_business | Come investire i soldi della liquidità aziendale | Potenziale estensione operativa; da studiare solo finché il novelty yield resta sufficiente. |
| 351 | 384 | `ERpAPQPX9J0` | TARGETED | B | 09_business | 5 Marketing Strategies to Get Your Business Off the Ground | Potenziale estensione operativa; da studiare solo finché il novelty yield resta sufficiente. |
| 352 | 387 | `UD34Yfw_efE` | TARGETED | B | 09_business | COME FARE MARKETING per la propria azienda [Parte 3] | Potenziale estensione operativa; da studiare solo finché il novelty yield resta sufficiente. |
| 353 | 388 | `wGgXryNPbxg` | TARGETED | B | 09_business | COME FARE MARKETING per la propria azienda [Parte 1] | Potenziale estensione operativa; da studiare solo finché il novelty yield resta sufficiente. |
| 354 | 390 | `RlgpRIc7ljc` | TARGETED | B | 09_business | Aumentare il fatturato della tua Azienda \| Il vero segreto | Potenziale estensione operativa; da studiare solo finché il novelty yield resta sufficiente. |
| 355 | 392 | `3vfZIcsrilc` | TARGETED | B | 09_business | MARKETING \| 3 Azioni fondamentali per la tua Azienda | Potenziale estensione operativa; da studiare solo finché il novelty yield resta sufficiente. |
| 356 | 393 | `pjrMVek56EU` | TARGETED | B | 09_business | WHERE TO INVEST TODAY to make your business successful | Potenziale estensione operativa; da studiare solo finché il novelty yield resta sufficiente. |
| 357 | 457 | `LtFeqet7OFc` | TARGETED | B | 10_casi_studio | GELATERIA WALLY MILAN \| The Brutal Truth About the Ice Cream You Eat Every Day | Caso recente: priorità maggiore solo per possibile prevalenza/aggiornamento. |
| 358 | 458 | `dftLQTuK0cY` | TARGETED | B | 10_casi_studio | CAMMI GOMME PIACENZA: The Tire Dealer That Doesn't Look Like a Tire Dealer | Caso recente: priorità maggiore solo per possibile prevalenza/aggiornamento. |
| 359 | 286 | `dFuZc7rFwgE` | TARGETED | A | 06_vendita | Le TECNICHE DI VENDITA per diventare un Venditore di Successo | Vendita è più satura: mantenere solo finché introduce un meccanismo distinto. |
| 360 | 353 | `7EY0X8kMJ0o` | TARGETED | B | 09_business | 🔴 Direct Response Marketing: The Technique That Made Great Entrepreneurs Rich | Potenziale estensione operativa; da studiare solo finché il novelty yield resta sufficiente. |
| 361 | 372 | `wg3tWYf6iho` | TARGETED | B | 09_business | #11 Controversial Truths to Scale Your Business Fast | Potenziale estensione operativa; da studiare solo finché il novelty yield resta sufficiente. |
| 362 | 375 | `AZYdLrjgvK0` | TARGETED | B | 09_business | Where NOT to Invest Your Money If You Want to Start a Business [That Won't Fail Immediately] | Potenziale estensione operativa; da studiare solo finché il novelty yield resta sufficiente. |
| 363 | 456 | `nn33VweEdB0` | TARGETED | B | 10_casi_studio | Come Trasformare Una Clinica Estetica In Un Business Milionario Grazie Al Marketing | Caso verticale vicino a Formalife/servizi professionali: utile se produce principi nuovi, non per i numeri. |
| 364 | 460 | `rEtbwMHdJcM` | TARGETED | B | 10_casi_studio | Le Iene and the Roberto Re Case: How to Protect Yourself and Your Company? | Caso recente: priorità maggiore solo per possibile prevalenza/aggiornamento. |
| 365 | 463 | `A9aD8P9W6BM` | TARGETED | B | 10_casi_studio | I SEGRETI DEL BRAND POSITIONING \| Creare Campagne Online di Successo [Case History] | Caso potenzialmente utile come stress-test di categoria/posizionamento. |
| 366 | 467 | `S6XcqyhsjGw` | TARGETED | B | 10_casi_studio | DON PEPPINU: Gelato Verace \| How to Create a Category and Dominate the Market [VLOG] | Caso potenzialmente utile come stress-test di categoria/posizionamento. |
| 367 | 289 | `dHKIWZFBHoA` | LOW / DEFER | B | 06_vendita | [Tecniche di Vendita] Il potere di una parola nella trattativa di vendita | Vendita già densa: alta probabilità di conferma o duplicazione. |
| 368 | 291 | `l4AcZXmUQUs` | LOW / DEFER | B | 06_vendita | [Sales Techniques] The Simple Trick of Scammers | Vendita già densa: alta probabilità di conferma o duplicazione. |
| 369 | 293 | `LAhN97eLwf8` | LOW / DEFER | B | 06_vendita | [Tecniche di Vendita] Parlare di denaro in Italia è un problema | Vendita già densa: alta probabilità di conferma o duplicazione. |
| 370 | 295 | `TRXt5UDCQqM` | LOW / DEFER | B | 06_vendita | SALES TECHNIQUES - The deadly mistake in selling | Vendita già densa: alta probabilità di conferma o duplicazione. |
| 371 | 321 | `eSyOgMr_UWs` | LOW / DEFER | A | 06_vendita | La Vendita Professionale secondo Venditore Vincente #shorts | Formato con yield storico più basso in un'area vendita ormai relativamente satura. |
| 372 | 398 | `KPzMmscoyro` | LOW / DEFER | B | 09_business | MARKETING \| La Bacchetta Magica per Creare Un’Azienda di Successo | Alta probabilità di sovrapposizione o valore marginale basso rispetto ai nodi business esistenti. |
| 373 | 462 | `QoWTlWZnyIQ` | LOW / DEFER | B | 10_casi_studio | How Brand Positioning Makes You UNIQUE in the Market (and Rich) \| VLOG | Caso potenzialmente utile come stress-test di categoria/posizionamento. |
| 374 | 464 | `-1l4to7UBDw` | LOW / DEFER | B | 10_casi_studio | Dan Kennedy's Marketing Strategies for Raising Prices [Case History] | Caso utile a stress-testare pricing premium e prova. |
| 375 | 466 | `YPbOmNqxdmA` | LOW / DEFER | B | 10_casi_studio | Televendite \| Come utilizzare al meglio un Infomercial [Case History] | Caso applicativo con alta probabilità di confermare principi già canonizzati. |
| 376 | 277 | `UAGHHUm8Ncg` | LOW / DEFER | B | 06_vendita | Marketing Strategies \| The 6 Levers to sell more [Part 2] | Vendita già densa: alta probabilità di conferma o duplicazione. |
| 377 | 282 | `VsakZMnjMyo` | LOW / DEFER | A | 06_vendita | MARKETING \| Come creare AUTORITA' per vendere di più | Autorità/affinità/dialogo mentale già coperti da fonti più recenti; probabile dedup. |
| 378 | 292 | `jVM-EVC0Tj4` | LOW / DEFER | B | 06_vendita | Sales Techniques - Fear of the Future | Vendita già densa: alta probabilità di conferma o duplicazione. |
| 379 | 296 | `YD5Slijhu40` | LOW / DEFER | B | 06_vendita | Professional Sales - Competitive Orientation | Vendita già densa: alta probabilità di conferma o duplicazione. |
| 380 | 300 | `FupPXETlhew` | LOW / DEFER | B | 06_vendita | [Sales Techniques] The Basics of Selling - Part 3 | Vendita già densa: alta probabilità di conferma o duplicazione. |
| 381 | 278 | `HrExv7tbcuE` | LOW / DEFER | B | 06_vendita | Marketing Strategies \| The 6 Levers to Sell More [Part 1] | Vendita già densa: alta probabilità di conferma o duplicazione. |
| 382 | 279 | `IN1Rm9HNhSE` | LOW / DEFER | B | 06_vendita | Strategie di MARKETING per fare SOLD OUT e VENDERE Live | Vendita già densa: alta probabilità di conferma o duplicazione. |
| 383 | 280 | `nJmttjxEbG8` | LOW / DEFER | B | 06_vendita | SALES without authority is a discount sale | Autorità/affinità/dialogo mentale già coperti da fonti più recenti; probabile dedup. |
| 384 | 301 | `X7xZyHvQG7M` | LOW / DEFER | B | 06_vendita | [Sales Techniques] The Basics of Selling - Part 2 | Vendita già densa: alta probabilità di conferma o duplicazione. |
| 385 | 302 | `bCfQSlTSHtY` | LOW / DEFER | B | 06_vendita | [Sales Techniques] The Whole Truth About Professional Sales (Part Three) | Vendita già densa: alta probabilità di conferma o duplicazione. |
| 386 | 303 | `Gj9zFPY0NQg` | LOW / DEFER | B | 06_vendita | [Tecniche di vendita] Tutta la verità sulla vendita professionale (Seconda Parte) | Vendita già densa: alta probabilità di conferma o duplicazione. |
| 387 | 304 | `Qfr0lQEiaxU` | LOW / DEFER | B | 06_vendita | [Tecniche di vendita] Tutta la verità sulla vendita professionale (Prima parte) | Vendita già densa: alta probabilità di conferma o duplicazione. |
| 388 | 332 | `16l3EQerKgQ` | LOW / DEFER | C | 08_brand | How to Know if You Have a Strong Brand (or Are Just Another Commodity) | Short probabilmente derivativo rispetto ai nodi brand già maturi. |
| 389 | 333 | `VywpU3-Ll_M` | LOW / DEFER | C | 08_brand | The 2 Conditions That Separate Real Brands from Small Companies \| Frank Merenda | Short probabilmente derivativo rispetto ai nodi brand già maturi. |
| 390 | 334 | `6A1VXELopys` | LOW / DEFER | C | 08_brand | Aumentare il fatturato grazie alla forza del Brand #shorts | Short probabilmente derivativo rispetto ai nodi brand già maturi. |
| 391 | 356 | `IKT-pq1mJc0` | LOW / DEFER | B | 09_business | How to Start a Business from Scratch: 8 Strategies Your Competitors DON'T Know | Alta probabilità di sovrapposizione o valore marginale basso rispetto ai nodi business esistenti. |
| 392 | 406 | `DN2dO1UBRZc` | LOW / DEFER | C | 09_business | Come scegliere i COLLABORATORI GIUSTI #shorts | Selezione/organizzazione persone: completa marketing del personale e scalabilità. |
| 393 | 422 | `UL7p310omY8` | LOW / DEFER | B | 10_casi_studio | Marketing per CENTRI ESTETICI \| Come Raddoppiare il Fatturato in 1 Mese | Caso applicativo con alta probabilità di confermare principi già canonizzati. |
| 394 | 425 | `i_nXlRCdgPA` | LOW / DEFER | B | 10_casi_studio | Medical Clinic's Turnover Doubled Thanks to Merenda Method Marketing | Caso verticale vicino a Formalife/servizi professionali: utile se produce principi nuovi, non per i numeri. |
| 395 | 428 | `hoVoLLL3eZk` | LOW / DEFER | B | 10_casi_studio | From 0 to 464 Orders Thanks to the Sales Techniques of Tana Delle Tigri | Caso applicativo con alta probabilità di confermare principi già canonizzati. |
| 396 | 442 | `UkzQe2Rpl8Y` | LOW / DEFER | B | 10_casi_studio | The Secret to a Successful Tire Shop: How Marketing Changed the Game | Caso applicativo con alta probabilità di confermare principi già canonizzati. |
| 397 | 284 | `0Aj28sGSKkw` | LOW / DEFER | B | 06_vendita | #4 Marketing Strategies to Sell to High-Spendants | Tema clienti alto-spendenti già molto coperto; probabile conferma. |
| 398 | 396 | `uw7ESoevavQ` | LOW / DEFER | B | 09_business | MARKETING\| Come creare un'Azienda Marketing First | Alta probabilità di sovrapposizione o valore marginale basso rispetto ai nodi business esistenti. |
| 399 | 440 | `GFPwnUHLQm8` | LOW / DEFER | B | 10_casi_studio | ALL'ANTICO VINAIO: 5 Key Marketing Strategies for Global Success | Caso applicativo con alta probabilità di confermare principi già canonizzati. |
| 400 | 455 | `jVnCaENbxus` | LOW / DEFER | B | 10_casi_studio | How to Market with a Wonder Package: The Secret to Successful Businesses | Caso applicativo con alta probabilità di confermare principi già canonizzati. |
| 401 | 287 | `-v8fL_RzWKw` | LOW / DEFER | B | 06_vendita | HOW TO SELL TO THE RICH \| Dan Kennedy reveals how to attract wealthy clients | Tema clienti alto-spendenti già molto coperto; probabile conferma. |
| 402 | 294 | `ZsjuqCIaxP4` | LOW / DEFER | B | 06_vendita | Tecniche di Vendita: come vendere ai ricchi | Tema clienti alto-spendenti già molto coperto; probabile conferma. |
| 403 | 337 | `_7CcZG5-Vdc` | LOW / DEFER | C | 09_business | The Rich Mentality: Briatore vs. Sorbillo [Free Training Course] | Alta probabilità di sovrapposizione o valore marginale basso rispetto ai nodi business esistenti. |
| 404 | 346 | `D7_NRV619Pw` | LOW / DEFER | C | 09_business | TASSE MALEDETTE! Come difendersi dalle aggressioni del Fisco? | Bassa trasferibilità o alta probabilità di contenuto polemico/contingente già fuori dai gap prioritari. |
| 405 | 401 | `IabwR13dZK0` | LOW / DEFER | C | 09_business | HOW TO DO BUSINESS IN ITALY - [Italian-Style Business] | Alta probabilità di sovrapposizione o valore marginale basso rispetto ai nodi business esistenti. |
| 406 | 403 | `LEXROXRm4gY` | LOW / DEFER | C | 09_business | MEMBERSHIP \| Come Diventare Imprenditore anche Senza Soldi | Alta probabilità di sovrapposizione o valore marginale basso rispetto ai nodi business esistenti. |
| 407 | 427 | `MHbLVF1ij3M` | LOW / DEFER | B | 10_casi_studio | Record-Breaking Real Estate Agency in Parma: From Frozen Food Seller to Top Performer in 9 Months | Caso applicativo con alta probabilità di confermare principi già canonizzati. |
| 408 | 439 | `60Nu2UhFAJ8` | LOW / DEFER | B | 10_casi_studio | MORTADELLA SHOP - The Marketing Lesson from the Kings of Bologna Station | Caso applicativo con alta probabilità di confermare principi già canonizzati. |
| 409 | 468 | `k-6P-_ZcFwY` | LOW / DEFER | B | 10_casi_studio | Come il MARKETING può far crescere la tua azienda [Case History Dustin Burleson] | Caso applicativo con alta probabilità di confermare principi già canonizzati. |
| 410 | 281 | `6t5_mdsdv9o` | LOW / DEFER | B | 06_vendita | SALES is affinity and mental dialogue with customers | Autorità/affinità/dialogo mentale già coperti da fonti più recenti; probabile dedup. |
| 411 | 317 | `H3d6sJ6_ois` | LOW / DEFER | C | 06_vendita | Commission-Based or Fixed-Wage Salespeople? Frank Merenda Answers | Formato con yield storico più basso in un'area vendita ormai relativamente satura. |
| 412 | 351 | `2DEKsiMb11Y` | LOW / DEFER | C | 09_business | How to Become an Entrepreneur \| and Succeed Even Without Experience | Alta probabilità di sovrapposizione o valore marginale basso rispetto ai nodi business esistenti. |
| 413 | 431 | `nWGgyKZY0bc` | LOW / DEFER | B | 10_casi_studio | Positioning Errors: Mortadella Shop's Lesson for Every Entrepreneur | Caso potenzialmente utile come stress-test di categoria/posizionamento. |
| 414 | 445 | `l6vW1WRrlqQ` | LOW / DEFER | A | 10_casi_studio | Il Metodo CHIARA FERRAGNI: Le Strategie di Marketing della nota Influencer | Caso applicativo con alta probabilità di confermare principi già canonizzati. |
| 415 | 309 | `7OHWKhhvdfk` | LOW / DEFER | C | 06_vendita | WHAT TO SELL TO THE RICH - 7 Ways to Attract a Target Who Wants to Spend! | Formato con yield storico più basso in un'area vendita ormai relativamente satura. |
| 416 | 407 | `GElTJ7sJHhQ` | LOW / DEFER | C | 09_business | Collaborator selection? #shorts | Alta probabilità di sovrapposizione o valore marginale basso rispetto ai nodi business esistenti. |
| 417 | 408 | `F6004PvguF8` | LOW / DEFER | C | 09_business | 90% of Entrepreneurs Don't Understand This Concept | Alta probabilità di sovrapposizione o valore marginale basso rispetto ai nodi business esistenti. |
| 418 | 411 | `_o1n-VE2zfk` | LOW / DEFER | C | 09_business | A Fatal Mistake Entrepreneurs Make: The True Cost of a New Salesperson (It's Not the Salary) | Alta probabilità di sovrapposizione o valore marginale basso rispetto ai nodi business esistenti. |
| 419 | 412 | `vbO0I1bgCWk` | LOW / DEFER | C | 09_business | If You're Afraid of Losing a Customer, You Don't Have a Business — You Have a Prison | Alta probabilità di sovrapposizione o valore marginale basso rispetto ai nodi business esistenti. |
| 420 | 415 | `-GI3yZY-Yio` | LOW / DEFER | C | 09_business | 💲From Employee to Entrepreneur: The Mental Leap That Changes Everything | Alta probabilità di sovrapposizione o valore marginale basso rispetto ai nodi business esistenti. |
| 421 | 417 | `oItk4I50omg` | LOW / DEFER | C | 09_business | Trade Associations: The Fatal Mistake That Kills Your Business [Frank Merenda] | Alta probabilità di sovrapposizione o valore marginale basso rispetto ai nodi business esistenti. |
| 422 | 419 | `iwhtNji1vVA` | LOW / DEFER | C | 09_business | Crea un’Azienda di Successo \| Da dove partire? #Shorts | Alta probabilità di sovrapposizione o valore marginale basso rispetto ai nodi business esistenti. |
| 423 | 420 | `n9L4NSinAXM` | LOW / DEFER | C | 09_business | Da ditta individuale a SRL #shorts #piva #azienda #impresa | Alta probabilità di sovrapposizione o valore marginale basso rispetto ai nodi business esistenti. |
| 424 | 421 | `zLAK2Qm5gLM` | LOW / DEFER | C | 09_business | Gli investimenti fondamentali per un imprenditore #shorts | Alta probabilità di sovrapposizione o valore marginale basso rispetto ai nodi business esistenti. |
| 425 | 434 | `cPDsbG0fZ_I` | LOW / DEFER | B | 10_casi_studio | L'Impero del Miele: Come diventare ricchi con un solo prodotto | Caso applicativo con alta probabilità di confermare principi già canonizzati. |
| 426 | 443 | `KvkF605zLxo` | LOW / DEFER | B | 10_casi_studio | BURGEZ MARKETING: Com'è dal vivo? | Caso applicativo con alta probabilità di confermare principi già canonizzati. |
| 427 | 308 | `rXoHmUGsYww` | LOW / DEFER | C | 06_vendita | DAN KENNEDY e TELEVENDITE - Marketing a Risposta Diretta [Corso] | Formato con yield storico più basso in un'area vendita ormai relativamente satura. |
| 428 | 444 | `9NraLPMJkpQ` | LOW / DEFER | B | 10_casi_studio | Burgez Marketing: La creatività che funziona? | Caso applicativo con alta probabilità di confermare principi già canonizzati. |
| 429 | 465 | `jjriqAHkJYc` | LOW / DEFER | B | 10_casi_studio | TAFFO PUBBLICITÁ \| Una Case History da Studiare | Caso applicativo con alta probabilità di confermare principi già canonizzati. |
| 430 | 305 | `Vi2HZ7k5zWU` | LOW / DEFER | C | 06_vendita | Tecniche di Vendita in Negozio: Come Raddoppiare le Vendite | Formato con yield storico più basso in un'area vendita ormai relativamente satura. |
| 431 | 310 | `bkkDzsBa3YE` | LOW / DEFER | C | 06_vendita | Stop Selling Products: Start Solving Problems (And Sell More) | Formato con yield storico più basso in un'area vendita ormai relativamente satura. |
| 432 | 311 | `68vQ8oZsEtg` | LOW / DEFER | C | 06_vendita | You're Losing Sales Every Day for a Reason They Never Explained to You | Formato con yield storico più basso in un'area vendita ormai relativamente satura. |
| 433 | 313 | `MJWfijvL8H8` | LOW / DEFER | C | 06_vendita | How to Talk to Customers to Really SELL (Without Looking Stupid) | Formato con yield storico più basso in un'area vendita ormai relativamente satura. |
| 434 | 316 | `jEND8wY7cjs` | LOW / DEFER | C | 06_vendita | Selling Homes: Stop Waiting for Clients and Do THIS [Frank Merenda] | Formato con yield storico più basso in un'area vendita ormai relativamente satura. |
| 435 | 319 | `S1UqJocqQUc` | LOW / DEFER | C | 06_vendita | Strategie di Direct Marketing per Vendere nel B2B | Formato con yield storico più basso in un'area vendita ormai relativamente satura. |
| 436 | 320 | `DrjevuNThsI` | LOW / DEFER | C | 06_vendita | Come VENDERE di più e alle TUE CONDIZIONI #shorts | Formato con yield storico più basso in un'area vendita ormai relativamente satura. |
| 437 | 404 | `vr4OJQVgB1k` | LOW / DEFER | C | 09_business | COME NON PAGARE LE TASSE - La vera guida per piccoli imprenditori | Bassa trasferibilità o alta probabilità di contenuto polemico/contingente già fuori dai gap prioritari. |
| 438 | 416 | `WsumrqBrMLU` | LOW / DEFER | C | 09_business | Why Italian Universities Don't Create Entrepreneurs But They Create Employees | Selezione/organizzazione persone: completa marketing del personale e scalabilità. |
| 439 | 423 | `sJ-PgDVRmwY` | LOW / DEFER | B | 10_casi_studio | Luciano Pavarotti's Restaurant in Modena: When Authority Surpasses Marketing | Caso applicativo con alta probabilità di confermare principi già canonizzati. |
| 440 | 424 | `y17XqNh4nww` | LOW / DEFER | B | 10_casi_studio | The Mortadella Shop Marketing Lesson in Bologna | Caso applicativo con alta probabilità di confermare principi già canonizzati. |
| 441 | 426 | `Qk41565Wvqk` | LOW / DEFER | B | 10_casi_studio | Strategic Marketing for Restaurants - Guapo Argentine Restaurant #shorts | Caso applicativo con alta probabilità di confermare principi già canonizzati. |
| 442 | 430 | `yEZJEAiQALo` | LOW / DEFER | B | 10_casi_studio | Why You Shouldn't Create a Generic Brand? The Mortadella Shop Case in Bologna | Caso applicativo con alta probabilità di confermare principi già canonizzati. |
| 443 | 432 | `hBXLN6pzLSU` | LOW / DEFER | B | 10_casi_studio | The One-Flavor Ice Cream Shop: The Business Lesson You Don't Expect | Caso applicativo con alta probabilità di confermare principi già canonizzati. |
| 444 | 453 | `Af9nYsZjjTM` | LOW / DEFER | B | 10_casi_studio | Le vendite record 2023 di LAMBORGHINI bastano per battere FERRARI? | Caso applicativo con alta probabilità di confermare principi già canonizzati. |
| 445 | 306 | `HA8FTIpB9mo` | LOW / DEFER | C | 06_vendita | SELL ME THIS PEN \| The Most Effective Sales Techniques | Formato con yield storico più basso in un'area vendita ormai relativamente satura. |
| 446 | 450 | `trYcsCYjI_s` | LOW / DEFER | B | 10_casi_studio | DUCATI \| Vince nel Marketing come Vince nelle Gare? | Caso applicativo con alta probabilità di confermare principi già canonizzati. |
| 447 | 307 | `V74HGPNrO84` | LOW / DEFER | C | 06_vendita | Cosa Vendere ai Ricchi: L'Ottava Regola | Tema clienti alto-spendenti già molto coperto; probabile conferma. |
| 448 | 315 | `o4Y0uyxzQAM` | LOW / DEFER | C | 06_vendita | Rule #1 for Sales Network Management | Formato con yield storico più basso in un'area vendita ormai relativamente satura. |
| 449 | 318 | `R4koY-hl7TM` | LOW / DEFER | C | 06_vendita | Tecniche di Vendita \| Crea il Test Drive per i Clienti #shorts | Formato con yield storico più basso in un'area vendita ormai relativamente satura. |
| 450 | 338 | `Jubodsxv8aQ` | LOW / DEFER | C | 09_business | ONLINE SCAMS - Where the heck do you invest your money? | Bassa trasferibilità o alta probabilità di contenuto polemico/contingente già fuori dai gap prioritari. |
| 451 | 402 | `mygv4grg_XA` | LOW / DEFER | C | 09_business | MINDSET \| I Segreti della Mente degli Imprenditori di Successo | Bassa trasferibilità o alta probabilità di contenuto polemico/contingente già fuori dai gap prioritari. |
| 452 | 410 | `WD-UPHoqogc` | LOW / DEFER | C | 09_business | Message to the DUBAI SCAM GURUS: Stop SCREWING OVER Entrepreneurs | Bassa trasferibilità o alta probabilità di contenuto polemico/contingente già fuori dai gap prioritari. |
| 453 | 413 | `8KxvTL5qFKU` | LOW / DEFER | C | 09_business | Why Your Business Is Failing (NO, It's Not Taxes' Fault) | Alta probabilità di sovrapposizione o valore marginale basso rispetto ai nodi business esistenti. |
| 454 | 435 | `QlCVKca7Ygk` | LOW / DEFER | C | 10_casi_studio | Come si diventa RICCHI con le sneakers? | Caso applicativo con alta probabilità di confermare principi già canonizzati. |
| 455 | 436 | `h5e1TxDcVV0` | LOW / DEFER | C | 10_casi_studio | Coca Cola: Il Suo Errore Più Grande | Caso applicativo con alta probabilità di confermare principi già canonizzati. |
| 456 | 438 | `d1xejlyQVWM` | LOW / DEFER | C | 10_casi_studio | La Battaglia del Thé | Caso applicativo con alta probabilità di confermare principi già canonizzati. |
| 457 | 447 | `4w9tk1wrjWQ` | LOW / DEFER | C | 10_casi_studio | Il Marketing dei Detersivi: L'errore di Perlana | Caso applicativo con alta probabilità di confermare principi già canonizzati. |
| 458 | 314 | `rt-f18mskYI` | LOW / DEFER | C | 06_vendita | The Real Secret to Selling to Wealthy Customers and Conquering the Market [Frank Merenda] | Tema clienti alto-spendenti già molto coperto; probabile conferma. |
| 459 | 336 | `UZPsGxcC-_0` | LOW / DEFER | C | 09_business | MENTALITÀ VINCENTE \| Dan Kennedy svela i segreti per ottenere Successo | Bassa trasferibilità o alta probabilità di contenuto polemico/contingente già fuori dai gap prioritari. |
| 460 | 437 | `dC6avQzKliQ` | LOW / DEFER | C | 10_casi_studio | Il segreto di TESLA: perché vende 10 volte di più dei colossi dell'Automotive? | Caso applicativo con alta probabilità di confermare principi già canonizzati. |
| 461 | 448 | `IzAwfz5hpI8` | LOW / DEFER | C | 10_casi_studio | Barilla e il suo Marketing: Troppe Estensioni di Linea? | Caso applicativo con alta probabilità di confermare principi già canonizzati. |
| 462 | 449 | `gX9mQAcVsNg` | LOW / DEFER | C | 10_casi_studio | DYSON: il Marketing Vincente che l'ha portato al SUCCESSO | Caso applicativo con alta probabilità di confermare principi già canonizzati. |
| 463 | 451 | `UNT0aSS6wWM` | LOW / DEFER | C | 10_casi_studio | Le strategie di marketing che possono battere Nutella | Caso applicativo con alta probabilità di confermare principi già canonizzati. |
| 464 | 452 | `G3OVBYUpOuo` | LOW / DEFER | C | 10_casi_studio | Qual è il VERO SEGRETO del Marketing della Nutella? | Caso applicativo con alta probabilità di confermare principi già canonizzati. |
| 465 | 433 | `abr257wwW3U` | LOW / DEFER | C | 10_casi_studio | CHIARA FERRAGNI e il caso del PANDORO BALOCCO | Caso applicativo con alta probabilità di confermare principi già canonizzati. |
| 466 | 446 | `RquiibFn3lo` | LOW / DEFER | C | 10_casi_studio | La Pasta Integrale Barilla e il Marketing che NON Funziona | Caso applicativo con alta probabilità di confermare principi già canonizzati. |
| 467 | 454 | `GWpaBmY-h8c` | LOW / DEFER | C | 10_casi_studio | AMAZON SELLER CENTRAL \| Vendere su Amazon conviene alle Aziende Italiane? | Caso applicativo con alta probabilità di confermare principi già canonizzati. |
| 468 | 429 | `AQcmrNLZc2s` | LOW / DEFER | C | 10_casi_studio | The Secret Behind TESLA: Why Does It Sell 10 Times More Than Automotive Giants? | Caso applicativo con alta probabilità di confermare principi già canonizzati. |

## Invarianti

- Nessun contenuto 276+ acquisito in questa riprioritizzazione.
- Nessun transcript o review creato.
- Nessuno stato STUDIATO/ESCLUSO modificato.
- `catalog.json`, `VIDEO_INDEX.md`, KB `merenda/`, classifier e file frozen restano invariati.
- `QUEUE.md` mantiene 1–275 invariati e riordina soltanto le 193 righe `DA STUDIARE`.
- `RESIDUAL_CLASSIFICATION_201-468.md` resta documento storico e non viene sovrascritto.
