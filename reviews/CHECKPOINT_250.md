# Checkpoint 250 — report definitivo — FASE 14 + FASE 15 eseguite

Stato semantico raggiunto sul branch `semantic-226-250` a partire dalla HEAD tecnica `c579de5e5ecf56bf19dd2b5d36a72df33ef80752`, portato su `main` con il commit `c9372ca9cd4ad535d844704caa82a1bae6fe15b7` ("Prepare checkpoint 250 handoff for Claude").

Questo documento è il **report definitivo** del checkpoint 250, eseguito da Claude Code. Le sezioni fino a "Verifica branch semantico" sono il pre-handoff prodotto da ChatGPT/Codex e sono state lasciate invariate perché verificate corrette da Claude. Le sezioni successive (a partire da "FASE 14 — Refactor KB (eseguita da Claude Code)") documentano il lavoro di Claude Code su questo checkpoint.

- SHA iniziale (HEAD all'avvio del checkpoint): `c9372ca9cd4ad535d844704caa82a1bae6fe15b7`
- SHA finale: vedi commit di chiusura di questo checkpoint (successivo a questo documento nella storia di `main`)

Nessun contenuto 251+ è stato processato semanticamente né acquisito tecnicamente durante questo checkpoint. Nessun file frozen è stato modificato.

## Stato al raggiungimento della soglia 250

- Video individuati: **468**
- Contenuti processati semanticamente: **250**
- `STUDIATO`: **244**
- `ESCLUSO`: **6**
- `DA STUDIARE`: **218**
- Corpus completo: **NO**
- Batch 226–250: **25/25 STUDIATO**
- Nuovi ESCLUSO nel batch: **0**
- Review 226–250: **25/25**

Primo contenuto ancora non processato: **251 — `ellOvKnIOqk` — “The #1 Sales Technique for a Record-Breaking Sales Team”**.

## Base tecnica 226–250

Handoff Codex:

- branch: `acquisition-226-250`
- base: `da0a20c00882f287674635109e625fef47f23408`
- HEAD tecnica: `c579de5e5ecf56bf19dd2b5d36a72df33ef80752`
- tentati / acquisiti / transcript utilizzabili: **25 / 25 / 25**
- automatiche italiane / manuali: **25 / 0**
- ASR / NO_IT_TRANSCRIPT / errori finali / pending: **0 / 0 / 0 / 0**
- 23 nuovi download; 232 e 233 avevano già metadata/JSON3 nella base
- 9 keyframe su 4 video, ispezionati nella fase tecnica
- validator tecnico prima/dopo: **841 warning identici**
- `git diff --check`: superato
- frozen, KB e semantica invariati nella fase tecnica

Limiti tecnici documentati da Codex:

- 227: copertura temporale transcript **95,51%**
- 228: copertura temporale transcript **92,79%**
- piccoli sforamenti timestamp fino a **2,360 s**, senza correzioni arbitrarie

La revisione semantica non ha basato nuove regole sulle code non coperte di 227/228.

## Esito semantico 226–250

### Novelty globale

- **Incrementali: 16/25 = 64%**
- **Deduplicati/confermativi: 9/25 = 36%**
- Nessun nuovo ESCLUSO

Incrementali:

- 229 — `7zRyOC3Z0lM`
- 232 — `MwNCMJE8sRk`
- 233 — `g-VOlvqnL_8`
- 234 — `ggJnCJCXIO4`
- 235 — `KZ78VhszH_o`
- 236 — `3ZNE75sPen8`
- 237 — `lwuJ6MYETUw`
- 238 — `T5ccJyQqX9c`
- 240 — `dYMeQuuT8QY`
- 241 — `8XduYN366z0`
- 242 — `rcVXvepx-l8`
- 243 — `gcQKKrbZW28`
- 245 — `Zzh6PXGTmD0`
- 247 — `V8CVwcH5rwA`
- 248 — `r649dAXopLM`
- 250 — `uOu65O88jrU`

Deduplicati/confermativi:

- 226, 227, 228, 230, 231, 239, 244, 246, 249

### Novelty per categoria finale

| Categoria | Video | Incrementali | Yield |
|---|---:|---:|---:|
| 01_mercato | 1 | 1 | 100% |
| 03_offerta | 1 | 1 | 100% |
| 04_marketing | 3 | 1 | 33% |
| 05_acquisizione | 2 | 0 | 0% |
| 06_vendita | 8 | 5 | 63% |
| 07_copy_comunicazione | 3 | 2 | 67% |
| 08_brand | 5 | 4 | 80% |
| 09_business | 2 | 2 | 100% |
| **Totale** | **25** | **16** | **64%** |

Il dato conferma l'ipotesi del checkpoint 200 che le aree meno sature — soprattutto vendita, copy e brand — potessero avere yield più alto, ma il campione resta troppo piccolo per trasformarlo da solo in regola frozen.

## Routing finale 226–250

| Categoria | N |
|---|---:|
| 01_mercato | 1 |
| 02_posizionamento | 0 |
| 03_offerta | 1 |
| 04_marketing | 3 |
| 05_acquisizione | 2 |
| 06_vendita | 8 |
| 07_copy_comunicazione | 3 |
| 08_brand | 5 |
| 09_business | 2 |
| 10_casi_studio | 0 |

Il routing finale diverge fortemente dalla categoria preliminare della coda, come previsto dal workflow: la classificazione semantica finale prevale.

## Integrazioni principali

### 229 — conversione economica oltre il primo front-end

Aggiornato `merenda/03_offerta/front-end-e-back-end.md`.

La fonte del 16 dicembre 2025 distingue la prima transazione dalla conversione economica completa quando il front-end lavora a break-even/perdita: vendere il front-end non significa ancora aver recuperato CAC e prodotto il margine progettato.

La terminologia “unconverted lead” non viene trasformata in definizione contabile/giuridica di cliente.

### 232 + 238 — follow-up dei lead non convertiti

Creato `merenda/06_vendita/follow-up-lead-non-convertiti.md`.

La procedura integra:

- raccolta dati;
- scelta canali;
- ragione concreta del ricontatto;
- rapidità sui lead caldi;
- sequenza preparata;
- politica dell'offerta;
- angolo del messaggio;
- quattro livelli 2025: materiale immediato, sequenza multicanale, presenza continuativa, intervento umano della vendita.

### 233 — preventivo come diagnosi/consulenza

Creato `merenda/06_vendita/preventivo-consulenza-diagnosi.md`.

Principio:

**problema → analisi → diagnosi → prescrizione/offerta**

La consulenza a pagamento resta una scelta di modello, non un obbligo universale.

### 234 — ordine delle leve di crescita

Aggiornato `merenda/09_business/numeri-cassa-e-crescita.md`.

Gerarchia 2025:

1. retention;
2. referral;
3. focus/valore;
4. processi vendita;
5. conversione;
6. valore transazione;
7. frequenza;
8. solo dopo, più lead.

Il modello è una gerarchia diagnostica, non un divieto di acquisizione finché i primi sette punti non sono perfetti.

### 235 — single point of failure

Aggiornato `merenda/09_business/scalabilita-e-operativita.md`.

Generalizzato il rischio della dipendenza da “uno”:

- una sola fonte acquisizione;
- un solo venditore;
- una sola persona chiave;
- una sola sede/infrastruttura critica.

La resilienza operativa non contraddice il focus di posizionamento.

### 236 — checklist di risposta diretta

Creato `merenda/07_copy_comunicazione/checklist-risposta-diretta.md`.

Le 22 tattiche della fonte sono state astratte in criteri durevoli:

- CTA;
- beneficio;
- livello di educazione;
- offerta/incentivo;
- facilità di risposta;
- percorso autonomo/umano;
- tracciabilità;
- coerenza con posizionamento.

Numero verde, coupon e altre implementazioni storiche non diventano requisiti universali.

### 237 + 248 — testimonianze e prova sociale

Creato `merenda/08_brand/testimonianze-e-prova-sociale.md`.

Framework:

- chi parla;
- scopo;
- ordine;
- posizione;
- frequenza/varietà;
- media;
- formato.

Aggiunta l'applicazione specializzata 2024 “avrei voluto farlo prima” per documentare, quando reale, il costo dell'attesa e contrastare la procrastinazione.

### 240 — bisogno tecnico vs stato desiderato

Aggiornato `merenda/07_copy_comunicazione/priorita-azione-e-inerzia.md`.

Struttura:

**bisogno tecnico → conseguenza desiderata → stato futuro percepito come migliore**

La trasformazione non autorizza promesse irrealistiche o scorciatoie false.

### 241 — brand community e fan

Creato `merenda/08_brand/brand-community-e-fan.md`.

Sette elementi:

1. personalità riconoscibile;
2. storie ricorrenti;
3. casi di trasformazione;
4. clienti promotori;
5. vocabolario condiviso;
6. principi non negoziabili;
7. contrasto filosofico.

Le analogie religiose/cultuali della fonte sono state neutralizzate in concetti di brand/community.

### 242 — capacità, volontà e percezione del valore

Aggiornato `merenda/01_mercato/clienti-altospendenti.md`.

Separati tre problemi:

1. capacità economica;
2. propensione/priorità di spesa;
3. comprensione della differenza che giustifica il premium.

Il modello delle “sei personalità” non è trattato come tassonomia scientifica rigida.

### 243 — eventi proprietari / VIP experience

Creato `merenda/04_marketing/eventi-proprietari-vip-experience.md`.

L'evento viene trattato come asset commerciale integrato:

**invito → esperienza → dati → offerta → follow-up**

Guest star, limousine e altri esempi estremi restano esempi, non requisiti.

### 245 — due livelli di fiducia

Aggiornato `merenda/08_brand/autorita-e-marketing.md`.

Nelle decisioni complesse il prospect deve fidarsi:

1. del fornitore;
2. della propria capacità di prendere una decisione corretta e difendibile.

Per i contatti più freddi/rischiosi, la prova va introdotta prima nel messaggio. Le fonti 2026 già presenti restano prevalenti.

### 247 — diagnosi standardizzata, prescrizione personalizzata

Aggiornato `merenda/06_vendita/prequalifica-follow-up-decisori.md`.

Principio:

**stesso metodo di analisi → evidenze diverse → prescrizione diversa**

Uno script è una coreografia diagnostica minima, non una lettura meccanica identica per ogni cliente.

### 250 — canale sincrono nei cicli consulenziali

Aggiornato `merenda/06_vendita/prequalifica-follow-up-decisori.md`.

Il marketing può standardizzare informazioni e preparazione; nei cicli complessi, voce/video/incontro conservano una funzione interattiva che non va sostituita automaticamente con lunghi scambi asincroni.

Non viene consolidato un divieto universale di WhatsApp/email: testo/chat restano appropriati per coordinamento, documenti, reminder, follow-up e vendite semplici.

## Correzione interna importante: RFM nel 239

Durante la revisione del 239 era stata inizialmente riconosciuta come nuova l'applicazione RFM alla riattivazione.

Il cross-check completo ha mostrato che **RFM era già canonico in `merenda/01_mercato/appropriatezza-clienti.md`**.

Correzione effettuata prima della chiusura del batch:

- il 239 è classificato **Novelty: no**;
- la duplicazione è stata rimossa;
- `riattivazione-clienti.md` conserva soltanto un rinvio operativo al nodo canonico RFM;
- nessun secondo framework RFM rimane attivo.

Questo è coerente con **MERGE, NOT APPEND**.

## Prevalenza temporale rilevante: video 249

Il video 249 (16 ottobre 2024) presenta fra le tecniche di urgenza anche scarsità “artificiale”.

La KB **non** adotta questa formulazione perché il materiale più recente 2025 già canonico in `offerta-a-risposta-diretta.md` richiede che urgenza/scarsità abbiano una ragione reale e non diventino finzione permanente.

Il 249 è quindi deduplicato senza modifica KB.

## Nuovi nodi KB creati nel batch

1. `merenda/04_marketing/eventi-proprietari-vip-experience.md`
2. `merenda/06_vendita/follow-up-lead-non-convertiti.md`
3. `merenda/06_vendita/preventivo-consulenza-diagnosi.md`
4. `merenda/07_copy_comunicazione/checklist-risposta-diretta.md`
5. `merenda/08_brand/brand-community-e-fan.md`
6. `merenda/08_brand/testimonianze-e-prova-sociale.md`

Tutti sono collegati dai rispettivi README già nel branch semantico.

## A/B/C — verifica empirica del batch 226–250

Classificazione pre-esistente del checkpoint 225:

- **A:** 10 contenuti → **8/10 incrementali = 80%**
- **B:** 9 contenuti → **7/9 incrementali = 78%**
- **C:** 6 contenuti → **1/6 incrementale = 17%**

Il singolo C incrementale è **229**, short pubblicato il 16 dicembre 2025, successivo a materiale già canonico sul front-end.

Conferme:

1. C resta **FAST REVIEW, mai SKIP**.
2. La regola manuale di promozione per recenza introdotta al checkpoint 225 è giustificata dal caso 229.
3. A ha alto yield nel batch, ma B è quasi equivalente: la distinzione A/B merita verifica in FASE 15 prima di qualsiasi modifica della logica.
4. Il campione non giustifica da solo modifiche ai file frozen.

## Verifica branch semantico

Confronto HEAD tecnica `c579de5e5...` → HEAD semantica pre-handoff:

- **25 commit avanti**
- **0 indietro**
- **25 review .review.md aggiunte**
- catalog/index/queue aggiornati soltanto per 226–250
- nessun contenuto 251+ modificato semanticamente
- nessun file frozen modificato
- nessun nuovo ESCLUSO

Contatori verificati direttamente su `sources/catalog.json`:

- STUDIATO **244**
- ESCLUSO **6**
- DA STUDIARE **218**
- totale **468**

## Verifica iniziale eseguita da Claude Code

- Branch: `main`; working tree pulito prima di iniziare.
- HEAD verificata: `c9372ca9cd4ad535d844704caa82a1bae6fe15b7`, identica a `origin/main` (nessun avanzamento remoto da analizzare).
- Contatori riverificati direttamente su `sources/catalog.json` (non assunti dal report ChatGPT): `STUDIATO=244`, `ESCLUSO=6`, `DA STUDIARE=218`, totale `468` — confermano esattamente i numeri dichiarati nel pre-handoff.
- `sources/queue/QUEUE.md` righe 226–250: tutte `STUDIATO`. Riga 251: `ellOvKnIOqk` — *The #1 Sales Technique for a Record-Breaking Sales Team*, `DA STUDIARE` — confermato come primo residuo.
- `sources/transcripts/*.review.md`: 250 file, coerente con `244 STUDIATO + 6 ESCLUSO`.
- `git diff --check` (stato iniziale): nessun output.

## Baseline tecnica reale (misurata, non assunta)

`python3 scripts/validate_project.py` sulla HEAD iniziale `c9372ca...`: **842 warning** (non 841).

Composizione: 836 `Ordine/stato incoerente` (storico, stesso gruppo del checkpoint 225) + 3 `File congelato modificato` (mismatch v1.0/v1.1, storico) + **3** `Contatore STATUS errato` (al checkpoint 225 erano 2: `Video completati`, `Video rimanenti`).

Causa della terza voce, verificata con `git log -p`: nel commit `c9372ca` (handoff ChatGPT 226→250) la riga `STATUS.md` "- Video individuati: 468" è stata riscritta in "- Video individuati: **468**" (aggiunto il grassetto markdown, coerente con lo stile delle righe adiacenti). Il validator confronta però la stringa letterale `- Video individuati: 468\n`, che con il grassetto non corrisponde più esattamente. Questa non è una nuova anomalia semantica: è la stessa classe di drift di nomenclatura già documentata ai checkpoint 200/225 sulle altre due righe, ora estesa a una terza riga per un motivo di formattazione. Non è stata "forzata" a 841: il valore reale misurato è **842** ed è la baseline di questo checkpoint. Non è stata applicata una correzione a questa riga: è fuori dal perimetro esplicito del checkpoint (refactor KB e audit tassonomia) e correggerla richiederebbe comunque toccare il formato delle altre righe adiacenti in modo non richiesto.

## FASE 14 — Refactor KB (eseguita da Claude Code)

### Metodo

Rilettura reale dell'intera `merenda/` (37 file di contenuto + 11 README + INDEX):

1. lettura integrale di tutti gli 11 README e dell'INDEX per verificare routing;
2. lettura integrale dei sei nuovi nodi del batch 226–250 e di tutti i file dei tre focus esplicitamente richiesti (`06_vendita`, `07_copy_comunicazione`, `08_brand`), incluse le sezioni non modificate dal batch, per giudicare i confini concettuali sull'intero documento e non solo sul diff;
3. lettura integrale dei tre file `03_offerta` per verificare l'integrazione della formulazione 2025 del video 229 (front-end/conversione economica) e l'assenza di scarsità "artificiale" (video 249);
4. lettura integrale di `04_marketing/eventi-proprietari-vip-experience.md` e `riattivazione-clienti.md` e verifica incrociata con `referral-e-soddisfazione.md`;
5. lettura integrale di `01_mercato/appropriatezza-clienti.md` (nodo RFM canonico) e grep di `RFM` su tutta `merenda/` per verificare che non esistano definizioni concorrenti;
6. lettura a campione trasversale di file non toccati dal batch (`01_mercato/clienti-altospendenti.md`, `04_marketing/complessita-e-riduzione-variabili.md`, `04_marketing/gerarchia-domanda-e-canali.md`, `04_marketing/quattro-modalita-e-ritmo.md`, `09_business/README.md`) per verificare che l'assenza di intervento non fosse un artefatto di aver guardato solo i file del batch;
7. verifica automatizzata di link interni rotti e file orfani su tutta `merenda/` (script Python ad hoc, non incluso nel repository perché strumento di verifica una tantum, non parte del sistema).

### Esito per ciascun focus richiesto

1. **06_vendita — confine fra i tre nodi vendita.** Non reggeva pienamente: `prequalifica-follow-up-decisori.md` (293 righe) conteneva, oltre a prequalifica/decisori/follow-up, anche l'intero metodo "diagnosi → prescrizione" (standardizzazione dello script in rete vendita, video 247; vendita consulenziale con autorità, video 245bis/bHxjwGQQoUw e l'aggiornamento più recente 19 maggio 2026 `8R8NR6nqhJY`). Questo è lo stesso metodo già trattato come nodo dedicato in `preventivo-consulenza-diagnosi.md` ("problema → analisi → diagnosi → prescrizione/offerta"). **Modifica applicata**: le due sezioni "Standardizzare la diagnosi, personalizzare la prescrizione" e "Vendita consulenziale: diagnosi, fatti e prescrizione" sono state spostate da `prequalifica-follow-up-decisori.md` a `preventivo-consulenza-diagnosi.md` (nessun contenuto perso o riscritto, solo rilocato). Risultato: `prequalifica-follow-up-decisori.md` 293→225 righe, ora scoped su preparazione/qualificazione pre-trattativa, mappa dei decisori e follow-up nel tempo; `preventivo-consulenza-diagnosi.md` 94→172 righe, ora unica sede del metodo diagnosi→prescrizione (dalla conversione del preventivo, alla standardizzazione in rete vendita, alla forma consulenziale/autorevole). Aggiornati i link incrociati (`08_brand/autorita-e-marketing.md`, i due README di sezione) e aggiunta una sezione "Collegamenti" mancante a `prequalifica-follow-up-decisori.md`. `follow-up-lead-non-convertiti.md` non necessitava modifiche: resta distinto (campagna strutturata di ricontatto dopo un "no", non il metodo diagnostico della trattativa) e già collegato correttamente agli altri due nodi.
2. **08_brand — confine fra i tre nodi.** Confermato che regge: `autorita-e-marketing.md` tratta autorità/fiducia/reputazione (incluso il ruolo competitivo/quantitativo di recensioni e testimonianze come asset di autorità), `testimonianze-e-prova-sociale.md` tratta il mestiere di raccogliere e strutturare una singola testimonianza (le 7 dimensioni), `brand-community-e-fan.md` tratta appartenenza/community/fan. Nessuna duplicazione di contenuto tra i tre: dove si toccano (es. testimonianze come PR) trattano aspetti diversi (quantità/posizionamento competitivo vs. tecnica di raccolta) e si linkano correttamente a vicenda. Nessuna modifica necessaria.
3. **07_copy_comunicazione — checklist vs priorità/azione.** Confermato che regge: `checklist-risposta-diretta.md` è una checklist di QA per materiali (8 controlli), `priorita-azione-e-inerzia.md` tratta la meccanica psicologica di priorità/trigger/stato desiderato. Si linkano correttamente senza duplicare CTA/desiderio/urgenza (questi restano nel documento sull'offerta). Nessuna modifica necessaria.
4. **04_marketing — eventi proprietari vs riattivazione/referral.** Confermato che regge: `eventi-proprietari-vip-experience.md` tratta l'evento come asset di relazione/vendita/riattivazione/referral progettato, senza duplicare la procedura di riattivazione (`riattivazione-clienti.md`, già ridotta al solo rinvio RFM) né quella di referral (`05_acquisizione/referral-e-soddisfazione.md`). I tre documenti si linkano correttamente. Nessuna modifica necessaria.
5. **03_offerta — coerenza formulazione 2025 del front-end (video 229).** Confermato: `front-end-e-back-end.md` contiene la sezione "Non confondere la prima transazione con una conversione economica completa" (fonte 16 dicembre 2025) collocata dopo e dichiarata complementare a "Ridurre la barriera senza svalutare il prodotto principale" (17 novembre 2025); il termine "unconverted lead" è esplicitamente qualificato come terminologia di lavoro del metodo, non definizione contabile/giuridica di cliente, come richiesto. Nessuna modifica necessaria.
6. **RFM — sede canonica unica.** Confermato: unica definizione completa in `01_mercato/appropriatezza-clienti.md#rfm-recenza-frequenza-valore-monetario`; `03_offerta/offerta-a-risposta-diretta.md` e `04_marketing/riattivazione-clienti.md` contengono solo un rinvio/citazione d'uso, nessuna seconda definizione. Verificato via `grep -rl RFM merenda/`: solo questi tre file, coerente con quanto dichiarato per il video 239. Nessuna modifica necessaria.
7. **Prevalenza temporale — video 249.** Confermato: la KB non contiene alcuna menzione di scarsità "artificiale"; `offerta-a-risposta-diretta.md` mantiene la formulazione 2025 ("Urgenza e scarsità funzionano come acceleratori della decisione; non devono diventare finzione permanente"); la review tecnica di 249 (`Q3SCQG-aZSM.review.md`) documenta esplicitamente perché il contenuto è stato deduplicato senza intervento KB. Nessuna modifica necessaria.

### Altre verifiche di FASE 14

- **Link interni**: 0 rotti su tutta `merenda/` (verifica automatizzata, prima e dopo il refactor).
- **File orfani**: 0 — ogni documento di contenuto è referenziato da almeno un README o un altro documento.
- **Dimensione dei file**: nessun altro file fuori scala rispetto alla distribuzione esistente (range 40–419 righe); i file più grandi del batch (`08_brand/autorita-e-marketing.md` 384, `03_offerta/offerta-a-risposta-diretta.md` 419, `03_offerta/prezzo-premium-e-percezione-del-valore.md` 392) erano già di quella dimensione prima del batch 226–250 e restano internamente coerenti (un solo tema, molte fonti cronologiche) — non è stato individuato un confine concettuale reale che ne giustifichi lo split, in linea con l'indicazione di non dividere solo per ridurre le righe.
- **Contaminazione Formalife**: 0 corrispondenze case-insensitive su `merenda/`.
- Non sono stati eseguiti interventi cosmetici: l'unica modifica strutturale (punto 1 sopra) risponde a un confine concettuale reale esplicitamente richiesto dalla governance, non a un obiettivo di riduzione righe.

## FASE 15 — Audit tassonomia (eseguita da Claude Code)

### Dimensione relativa delle categorie (righe di contenuto, esclusi README)

| Categoria | File | Righe |
|---|---:|---:|
| 00_fondamenti | 1 | 228 |
| 01_mercato | 4 | 472 |
| 02_posizionamento | 3 | 669 |
| 03_offerta | 3 | 1030 |
| 04_marketing | 5 | 729 |
| 05_acquisizione | 4 | 623 |
| 06_vendita | 3 | 504 |
| 07_copy_comunicazione | 2 | 359 |
| 08_brand | 3 | 741 |
| 09_business | 6 | 955 |
| 10_casi_studio | 2 | 94 |

Nessuna categoria è anormalmente larga (03_offerta e 09_business sono le più grandi ma con file numericamente pochi e internamente coerenti, non frammentati) né quasi vuota in modo problematico: `10_casi_studio` è piccola perché il routing dei checkpoint 100/150 ha spostato lì solo i titoli con azienda/caso nominato con sicurezza dal titolo, e la maggior parte di quei contenuti è ancora `DA STUDIARE`, non perché la categoria sia mal progettata.

### Routing del batch vs categoria preliminare

Confermato (già segnalato dal pre-handoff): il routing finale 226–250 diverge fortemente dalla categoria preliminare di coda (tutti extra-vendita in origine), ma questo è l'esito atteso del processo — la classificazione semantica finale prevale sempre su quella preliminare da titolo, e non indica un problema di tassonomia.

### 06_vendita, 07_copy_comunicazione, 08_brand — crescita del batch

Le tre sezioni più toccate dal batch restano a 3, 2 e 3 file di contenuto rispettivamente: la crescita è stata assorbita da nodi nuovi e ben delimitati (confermato sopra), non da un unico file che si gonfia indefinitamente. L'unico intervento necessario è stato lo spostamento interno descritto in FASE 14 (punto 1), non uno split/merge di categorie.

### Naming, sottostrutture, split/merge

Nessun nome di categoria risulta fuorviante o sovrapposto rispetto al contenuto effettivamente ospitato. Nessuna categoria ha raggiunto una dimensione o un'eterogeneità interna che giustifichi una sottostruttura (sotto-cartelle). **Decisione: nessuna modifica alla tassonomia a 11 categorie.** Non è un intervento cosmetico saltato per pigrizia: è stata verificata esplicitamente l'assenza di un beneficio netto di navigazione/recupero che giustifichi split, merge o rinomina, come richiesto dalla governance.

### Classificatore A/B/C

Dati del batch 226–250 (dal pre-handoff, riverificati): A 8/10 = 80%, B 7/9 = 78%, C 1/6 = 17%.

Confrontati con il batch precedente (checkpoint 225): A 0/2, B 5/19, C 1/4. La distribuzione A/B tra i due batch **non è stabile** (al checkpoint 225 A ha reso meno di B; qui quasi identico), il che è un argomento in più per **non modificare** la logica del classificatore sulla base di due soli batch consecutivi con andamento opposto. Il caso C→FAST REVIEW (video 229, short 16 dicembre 2025) conferma di nuovo la regola già introdotta al checkpoint 225 (promozione manuale per recenza durante la FAST REVIEW), che resta quindi confermata ma non viene irrigidita in una regola automatica del classificatore, per le stesse ragioni tecniche già documentate al checkpoint 225 (assenza di `upload_date` affidabile per la maggioranza degli short).

**Nessuna modifica a `scripts/classify_residual.py` (funzione `classify()`).** **Modifica applicata**: `reviews/RESIDUAL_CLASSIFICATION_201-468.md` è stato rigenerato eseguendo lo script invariato, per riflettere il naturale avanzamento del corpus (residuo sceso da 243 a 218 dopo il batch 226–250: nuovo riepilogo A=34/218=16%, B=131/218=60%, C=53/218=24%). Verificato via diff che le uniche righe scomparse dall'artefatto sono esattamente le 25 ora `STUDIATO`/confermate del batch appena chiuso; nessun'altra riga ha cambiato classe o motivazione.

## A/B/C — riepilogo empirico

- A: **8/10 incrementali = 80%**
- B: **7/9 incrementali = 78%**
- C: **1/6 incrementale = 17%**
- Novelty globale: **16/25 = 64%**
- C incrementale: video 229 (`7zRyOC3Z0lM`), short del 16 dicembre 2025 — confermato FAST REVIEW, mai SKIP.

## Validator prima/dopo

| Momento | Warning | Note |
|---|---:|---|
| HEAD iniziale `c9372ca...` | **842** | non 841: vedi "Baseline tecnica reale" sopra |
| Dopo FASE 14 + FASE 15 | **842** | diff riga per riga identico alla baseline; nessuna nuova anomalia introdotta |

`git diff --check`: nessun output, prima e dopo.

## File modificati in questo checkpoint

- **Modificato**: `merenda/06_vendita/prequalifica-follow-up-decisori.md` — rimosse le due sezioni sul metodo diagnosi→prescrizione (spostate), aggiunta sezione "Collegamenti" mancante.
- **Modificato**: `merenda/06_vendita/preventivo-consulenza-diagnosi.md` — aggiunte le due sezioni spostate, aggiornato un riferimento interno, aggiornata la sezione "Collegamenti".
- **Modificato**: `merenda/06_vendita/README.md` — descrizione di `preventivo-consulenza-diagnosi.md` aggiornata per riflettere il nuovo perimetro.
- **Modificato**: `merenda/08_brand/autorita-e-marketing.md` — aggiornato un link con ancora che puntava alla sezione spostata.
- **Modificato**: `reviews/RESIDUAL_CLASSIFICATION_201-468.md` — rigenerato (nessuna modifica alla logica).
- **Modificato**: `reviews/CHECKPOINT_250.md` — questo documento, da pre-handoff a report definitivo.
- **Modificato**: `STATUS.md` — stato aggiornato post-checkpoint.
- **Nessun altro file di `merenda/` modificato.**
- **Nessuna modifica ai file frozen.**
- **Nessun file 251+ creato o modificato** (transcript, review, asset).

## Confronto tecnico→semantico→checkpoint (verifica finale)

- Commit ChatGPT/Codex portati su `main` prima di questo checkpoint: 25 (semantici) confermati dal pre-handoff, non ridiscussi.
- Commit di questo checkpoint: refactor mirato `06_vendita` + rigenerazione artefatto classificatore + questo report + `STATUS.md`.
- Nessun file frozen nel diff di questo checkpoint (confermato da `git diff --stat` sui cinque file frozen: vuoto).
- Nessun contenuto con posizione ≥ 251 letto, acquisito, revisionato o integrato durante questo checkpoint.
- Contatori catalogo invariati: **244 STUDIATO + 6 ESCLUSO + 218 DA STUDIARE = 468**.

## Stato finale del corpus

- Video individuati: **468**
- Processati semanticamente: **250**
- STUDIATO: **244**
- ESCLUSO: **6**
- DA STUDIARE: **218**
- Corpus completo: **NO**
- Ultimo refactor KB (FASE 14): **250**
- Ultimo audit tassonomia (FASE 15): **250**

## Handoff

- Corpus completo: **NO**
- Agente richiesto: **CODEX**
- Motivo: gli asset tecnici (transcript) per la prossima porzione della coda (251–275) non sono presenti nel repository; ChatGPT non può eseguire le fasi 8–13 senza transcript.
- Prossima azione per Codex: acquisizione tecnica del batch 251–275, poi restituire il controllo a ChatGPT via `STATUS.md`.
- Primo contenuto non completato: `251 — ellOvKnIOqk — The #1 Sales Technique for a Record-Breaking Sales Team`.
- Prossimo checkpoint Claude: **275 — FASE 14**.
- Prossimo audit tassonomia: **300 — FASE 14 + FASE 15**.

## Conferma finale

Nessun contenuto con posizione ≥ 251 è stato processato semanticamente, acquisito tecnicamente, o ha ricevuto una review `.review.md` durante questo checkpoint. FASE 14 e FASE 15 sono state entrambe eseguite. Nessun file frozen è stato toccato. `merenda/` non contiene riferimenti a Formalife. Link interni e file orfani verificati a 0 su tutta la KB, prima e dopo il refactor.
