# Checkpoint 150 — FASE 14 + FASE 15 (Claude Code)

## Verifica iniziale

- Branch: `main`. Working tree pulito prima di iniziare.
- HEAD iniziale: `097592fcdabd14e207d4e61636d5e6daa2640aaf` — coincide con lo SHA atteso indicato nell'istruzione.
- `git fetch origin` eseguito: `main` locale coincideva esattamente con `origin/main` (nessun fast-forward necessario, nessuna divergenza).

## Stato del corpus all'apertura del checkpoint

- Video individuati: 468
- Processati semanticamente: 150 (144 `STUDIATO`, 6 `ESCLUSO`)
- Da studiare: 318
- Batch 126–150: 25/25 completato (22 transcript da YouTube + 3 fallback ASR locali: `jcVKVKvy78k`, `joY6sigynis`, `ijVoIMF_gn8`)
- Corpus completo: NO

Questo checkpoint richiede FASE 14 + FASE 15 (soglia dei 50). Nessun contenuto 151+ è stato acquisito, letto semanticamente o marcato `STUDIATO`/`ESCLUSO` in questo checkpoint.

---

## FASE 14 — Refactor globale della KB

### Ambito

Lettura integrale di tutta `merenda/`: 35 file di contenuto + 11 README di sezione + `INDEX.md` (47 file `.md`), con attenzione particolare alle integrazioni del batch 126–150 elencate nell'istruzione (marketing del proprio settore, Sisma/ragione sociale vs brand, owned/known demand, quantità/qualità lead/capacità di chiusura, autorità/credibilità/fiducia, information marketing lungo il ciclo cliente, materiali per decisori diversi, direct response come funzione distributiva, sell-in/sell-through).

### Verifica delle integrazioni 126–150

Tutti i temi elencati nell'istruzione sono stati rintracciati e risultano già correttamente fusi (MERGE, non append) nei documenti pertinenti dal lavoro di ingestione di ChatGPT, senza duplicazioni:

- **Marketing del proprio settore come competenza dell'imprenditore** (`jcVKVKvy78k`) → `00_fondamenti/marketing-first.md` ("Diventare esperti di marketing del proprio settore").
- **Sisma, ragione sociale vs brand focalizzati** (`jcVKVKvy78k`) → `02_posizionamento/estensioni-di-linea-e-architettura-brand.md` ("Ragione sociale e brand di mercato: il caso Sisma").
- **Owned/known demand prima di nuova acquisizione** (`F1seup0MuLk`) → `04_marketing/gerarchia-domanda-e-canali.md` ("Prima della nuova acquisizione: lavorare la domanda già posseduta").
- **Quantità lead / qualità lead / capacità di chiusura** (`VRXyHpVBvAo`) → `06_vendita/prequalifica-follow-up-decisori.md` ("Tre leve per aumentare la produttività commerciale").
- **Autorità / credibilità / fiducia** (`W9IOyR3fsEo`) → `08_brand/autorita-e-marketing.md` ("Autorità, credibilità e fiducia: tre lavori distinti").
- **Information marketing lungo il ciclo cliente** (`joY6sigynis`) → `05_acquisizione/information-marketing.md` ("Information marketing lungo il ciclo cliente").
- **Materiali diversi per decisori diversi** (`joY6sigynis`) → `06_vendita/prequalifica-follow-up-decisori.md` ("Materiali diversi per decisori diversi").
- **Direct response come funzione distributiva della PMI** (`ijVoIMF_gn8`) → `00_fondamenti/marketing-first.md` ("Per una PMI il marketing svolge anche una funzione distributiva").
- **Sell-in / sell-through nei canali intermediati** (`VN1d2qBc0U0`) → `04_marketing/gerarchia-domanda-e-canali.md` ("Con intermediari servono sell-in e sell-through"), con rimando coerente anche in `02_posizionamento/estensioni-di-linea-e-architettura-brand.md` ("Sell-in non significa domanda del cliente finale").

Nessuna di queste integrazioni ha richiesto ricollocazione: la posizione scelta durante l'ingestione era già quella corretta rispetto al resto della KB.

### Duplication audit

Nessuna duplicazione sostanziale trovata: nessun concetto è spiegato due volte in file diversi senza motivo, nessuna vecchia formulazione risulta in conflitto irrisolto con una più recente (la precedenza cronologica è sempre dichiarata esplicitamente nel testo, es. "il materiale più recente prevale"), nessun esempio è stato promosso impropriamente a principio autonomo.

### Problema strutturale trovato e corretto

`merenda/05_acquisizione/information-marketing.md` aveva la sezione `## Collegamenti` inserita a metà documento (dopo la sezione sulla compressione della piramide), seguita da altre due sezioni di contenuto reale ("Il volume della keyword ovvia non misura tutta la domanda" e "Prima saturare un funnel, poi moltiplicarlo") aggiunte evidentemente in un merge successivo senza spostare il blocco dei collegamenti. Corretto spostando `## Collegamenti` in fondo al file, dopo tutte le sezioni di contenuto. Nessun contenuto è stato perso o riscritto, solo riordinato.

### Dimensione e frammentazione dei file

- `merenda/08_brand/autorita-e-marketing.md` è cresciuto molto nel batch 126–150 (assorbendo `W9IOyR3fsEo`) ed è ora il file più lungo della KB (348 righe). È stato valutato per uno split (es. "costruzione dell'autorità" vs "come il cliente costruisce una decisione/reputazione"), ma i due filoni sono strettamente concatenati nella stessa narrazione causale (autorità → credibilità → fiducia → decisione del cliente → passaparola/storia accumulata) e non esiste ancora un confine concettuale abbastanza netto da giustificare due documenti autonomi senza duplicare il framework introduttivo. Nessuno split eseguito; da rivalutare al prossimo checkpoint se il file continua a crescere.
- `merenda/03_offerta/offerta-a-risposta-diretta.md` (367 righe) e `prezzo-premium-e-percezione-del-valore.md` (371 righe), già segnalati al checkpoint 125, non sono cresciuti in questo batch: restano leggibili e ancorati a fonti specifiche. Nessuna azione necessaria.
- Nessun file microscopico o frammentato senza motivo. Nessuna fusione di file necessaria.

### Gerarchia, routing e collegamenti

- Controllo programmatico di tutti i link relativi/anchor su tutta `merenda/`: **0 link rotti** su 47 file (verificato dopo la correzione sopra).
- Controllo file orfani: **nessun file di contenuto non raggiungibile** da un README o da un altro documento della KB.
- `merenda/INDEX.md` e i README di sezione risultano coerenti con i file realmente presenti; nessuna modifica necessaria.

### Confini fra categorie (mercato / posizionamento / offerta / marketing / acquisizione / vendita / copy / brand / business / casi studio)

Verificati punto per punto i confini segnalati come da monitorare nei checkpoint precedenti (numeri/cassa/patrimonializzazione/scalabilità, front-end e continuità, appropriatezza clienti, consapevolezza/domanda/front-end, casi applicativi): restano tutti ben distinti, con sovrapposizioni gestite tramite rimandi incrociati espliciti piuttosto che duplicazione di contenuto. Nessuna azione necessaria oltre a quanto già fatto al checkpoint 125.

### Modifiche effettuate — riepilogo Fase 14

- `merenda/05_acquisizione/information-marketing.md`: spostata la sezione `## Collegamenti` in fondo al documento (fix strutturale, nessuna perdita di contenuto).

Nessun file creato, eliminato, fuso o rinominato. Nessun contenuto riscritto nel merito.

---

## FASE 15 — Audit globale della tassonomia

### Categorie

Rivalutate criticamente le 11 categorie (`00_fondamenti` → `10_casi_studio`) alla luce dei 150 contenuti processati:

- Ogni concetto consolidato nei 150 video trova una collocazione naturale e non ambigua nella tassonomia attuale; non è emerso nessun argomento ricorrente privo di categoria adeguata.
- Non sono stati trovati confini sistematicamente sovrapposti fra categorie (es. marketing vs acquisizione, brand vs posizionamento): dove due categorie toccano lo stesso argomento da angolazioni diverse (es. autorità in `08_brand` richiamata da `04_marketing`, `05_acquisizione`, `06_vendita`, `03_offerta`), la KB usa rimandi incrociati invece di duplicare o richiedere una ricategorizzazione.
- Non sono emerse ragioni sistemiche per unire, dividere o rinominare categorie. La tassonomia a 11 categorie ereditata dai checkpoint precedenti resta adeguata.

**Decisione:** nessuna modifica alla tassonomia delle categorie.

### Queue futura: revisione dei 318 contenuti `DA STUDIARE`

Riletti in ordine tutti i 318 contenuti ancora `DA STUDIARE` (posizioni 151–468 in `sources/queue/QUEUE.md`), con attenzione a titoli che indicano con sufficiente sicurezza un caso/azienda specifico o un tema più preciso del generico `04_marketing`/`06_vendita`, sullo stesso criterio già usato al checkpoint 100.

**9 riclassificazioni applicate** (categoria preliminare, basata solo sul titolo — da confermare in fase di ingestione):

| ID | Titolo | Da | A | Motivo |
|---|---|---|---|---|
| `5awWbxibHIE` | Hiring Mistakes? Frank Merenda Tells You the Brutal TRUTH | 04_marketing | 09_business | Tema HR/assunzioni, non marketing |
| `LMzKVDWrGlk` | The Placement Rule That Brought Skechers to Success #shorts | 04_marketing | 10_casi_studio | Caso Skechers nominato |
| `mkhp-EGSORA` | L'Impero del Miele di Mike's Hot Honey #shorts | 04_marketing | 10_casi_studio | Versione breve di un caso già in 10_casi_studio (`cPDsbG0fZ_I`) |
| `NTy1ZHQ8NYs` | Il più grande FLOP di FERRERO #Shorts | 04_marketing | 10_casi_studio | Caso Ferrero nominato |
| `5XW0s6NizEE` | Il SUCCESSO della URUS #Shorts | 04_marketing | 10_casi_studio | Caso Lamborghini Urus nominato |
| `NCQ1lX3S5wk` | Il Segreto del Gommista di Successo #Shorts | 04_marketing | 10_casi_studio | Coerente con altri casi "gommista" già presenti (`UkzQe2Rpl8Y`, `dftLQTuK0cY`) |
| `AjvfyImTiPI` | All'Antico Vinaio: il "segreto" del suo successo #shorts | 04_marketing | 10_casi_studio | Versione breve di un caso già in 10_casi_studio (`GFPwnUHLQm8`) |
| `aQ5V7845jX4` | Il più Grande Errore di Marketing di Coca Cola #shorts | 04_marketing | 10_casi_studio | Versione breve di un caso già in 10_casi_studio (`h5e1TxDcVV0`) |
| `rI00A_jHqz8` | Il Potere Del Marketing: +50% di Vendite Per Un'Azienda Farmaceutica di Successo | 06_vendita | 10_casi_studio | Caso con risultato numerico specifico, coerente con altri casi già presenti |

Sincronizzati per tutti e 9 gli ID: `sources/catalog.json`, `sources/VIDEO_INDEX.md`, `sources/queue/QUEUE.md` (stesso campo categoria in tutti e tre i file, verificato riga per riga).

**Differenza rispetto al precedente di checkpoint 100:** al checkpoint 100 gli 11 contenuti riclassificati erano stati anche spostati in fondo alla sezione `10_casi_studio` con rinumerazione della coda (101→468). In questo checkpoint i 9 contenuti riclassificati **non sono stati spostati né la coda è stata rinumerata**: restano nella posizione d'ordine originale. Motivo: `scripts/validate_project.py` mostra già 836 righe di disallineamento d'ordine preesistente fra `catalog.json` e `VIDEO_INDEX.md`/`QUEUE.md` (anomalia nota, non introdotta da questo checkpoint — verificato che il conteggio è identico prima e dopo le mie modifiche). Rinumerare l'intera coda in questo contesto avrebbe un rischio concreto di introdurre nuovi errori di sincronizzazione su una base già fragile, per un beneficio puramente estetico (la posizione non influisce sull'ordine di studio effettivo entro il prossimo batch di 25, che rimane comunque il campione delle posizioni 151–175). Si segnala per un futuro checkpoint dedicato la possibilità di una riconciliazione completa dell'ordine fra i tre file.

**Resto della coda (309 contenuti):** riletti tutti i titoli restanti; non sono emersi altri casi di riclassificazione ad alta confidenza basata solo sul titolo. La maggioranza dei contenuti resta correttamente e già distribuita fra `04_marketing` (residuo generico), `05_acquisizione` (funnel/lead generation), `06_vendita` (tecniche di vendita), `08_brand`, `09_business` e un lungo blocco finale di `10_casi_studio` (posizioni 422–468) già consolidato dal checkpoint 100.

### Coerenza meccanica

Verificato che, dopo le modifiche, `catalog.json`, `VIDEO_INDEX.md` e `QUEUE.md` riportano la stessa categoria per tutti e 9 gli ID toccati. Nessun contenuto 151+ marcato `STUDIATO` o `ESCLUSO`. Nessun transcript sorgente modificato.

### Prossimo batch tecnico 151–175

Confermato l'ordine attuale della queue per le posizioni 151–175 (invariato nell'ordinamento, con le correzioni di categoria sopra applicate in-place):

1. `8R8NR6nqhJY` — "I Already Tried It and It Didn't Work" — The Excuse That Kills Your Revenue (04_marketing)
2. `-oYSpJrj024` — The Customer Doesn't Understand Your Quality. And They Never Will (04_marketing)
3. `v6WWqNpNSpE` — The Unfair Advantage You Can Create From Scratch Today (04_marketing)
4. `_6QCnb6Oj1Y` — Customer Lifetime Value: Why Not Knowing This Value Will Set You Back (04_marketing)
5. `Z7FhdrG-fOw` — How to Increase Revenue with Just One Question (04_marketing)
6. `5awWbxibHIE` — Hiring Mistakes? Frank Merenda Tells You the Brutal TRUTH (09_business)
7. `G6j8xbargKY` — Coaches and Trainers for Companies - Be Careful Who You Follow (04_marketing)
8. `LMzKVDWrGlk` — The Placement Rule That Brought Skechers to Success #shorts (10_casi_studio)
9. `-6L9gCbicjk` — Come Capire il Dialogo Mentale di un Cliente? #shorts (04_marketing)
10. `I2RBYMESAsk` — HOW TO FIND CUSTOMERS by giving them a dream shopping experience #shorts (04_marketing)
11. `mkhp-EGSORA` — L'Impero del Miele di Mike's Hot Honey #shorts (10_casi_studio)
12. `NTy1ZHQ8NYs` — Il più grande FLOP di FERRERO #Shorts (10_casi_studio)
13. `5XW0s6NizEE` — Il SUCCESSO della URUS #Shorts (10_casi_studio)
14. `NCQ1lX3S5wk` — Il Segreto del Gommista di Successo #Shorts (10_casi_studio)
15. `AjvfyImTiPI` — All'Antico Vinaio: il "segreto" del suo successo #shorts (10_casi_studio)
16. `qIG_0TMol8s` — Chat GPT: Intelligenza Artificiale come opportunità o minaccia? #shorts (04_marketing)
17. `fpao23ulhkQ` — Why You Shouldn't Spend on Marketing (Unless You Do This First) (04_marketing)
18. `9zvNhQOpRI4` — Is Marketing Important? This Is the Definitive Answer (04_marketing)
19. `oQXsQzrIv2M` — Marketing for Medical Clinics: How to Survive Italian Regulations and Win in the Market (04_marketing)
20. `PKgWYVvme2s` — Customer Experience: The Marketing Secret No One Tells You (04_marketing)
21. `degAX4kvT-0` — Digital Marketing for Typical Products: The Formula for Winning Bundles (04_marketing)
22. `YvfN2NUwXtY` — Marketing per il tuo CENTRO ESTETICO #shorts (04_marketing)
23. `aw3Fu_LTH34` — What does Marketing #shorts mean? (04_marketing)
24. `znVPLom4j70` — Marketing for Dentists | Here's What Happens When a Dentist Does Marketing #shots (04_marketing)
25. `y-8LBcQsS9M` — RESTAURANT MARKETING | Launching a Successful Restaurant (04_marketing)

Il primo pendente della nuova queue resta `8R8NR6nqhJY` (invariato rispetto a prima della FASE 15: la riclassificazione non ha toccato le prime posizioni della coda).

Nessun asset tecnico per 151–175 risulta acquisito al momento di questo checkpoint (`da acquisire` in `VIDEO_INDEX.md`).

---

## Controlli eseguiti prima del commit

1. `python3 scripts/validate_project.py`: stesse anomalie preesistenti già documentate ai checkpoint precedenti — file congelati diversi dal tag `merenda-system-v1.0` (`MASTER_PLAN.md`, `system/HANDOFFS.md`, `system/FROZEN_FILES.md`: divergenza storica pre-esistente, non toccata in questo checkpoint) e disallineamento d'ordine fra `catalog.json`/`VIDEO_INDEX.md`/`QUEUE.md` (836 righe, identico prima e dopo le modifiche di questo checkpoint — verificato con `git stash`). Contatore `STATUS.md` non nel formato esatto atteso dal validator (usa "processati semanticamente"/"STUDIATO"/"ESCLUSO" invece delle etichette letterali "Video completati"/"Video rimanenti" cercate dallo script): anomalia preesistente, non introdotta ora.
2. Link/anchor interni su tutta `merenda/`: 0 rotti su 47 file `.md`.
3. File orfani in `merenda/`: nessuno.
4. Coerenza `catalog.json` ↔ `VIDEO_INDEX.md` ↔ `QUEUE.md` sui 9 ID toccati: categoria identica in tutti e tre i file.
5. Conteggi: `sources/catalog.json` conferma 468 righe totali, 144 `STUDIATO`, 6 `ESCLUSO`, 318 `DA STUDIARE` — invariati rispetto all'apertura del checkpoint (nessuna modifica di stato, solo di categoria).
6. `git diff --check`: nessun conflitto/whitespace error.
7. File congelati (`MASTER_PLAN.md`, `system/RULES.md`, `system/PHASES.md`, `system/HANDOFFS.md`, `system/FROZEN_FILES.md`): non modificati in questo checkpoint.
8. Nessun contenuto 151+ marcato `STUDIATO`/`ESCLUSO`.
9. Nessun asset tecnico 151+ acquisito (nessun file aggiunto in `sources/transcripts/` per ID ≥151).
10. `git status --short` verificato prima del commit finale.

## Anomalie preesistenti (non introdotte da questo checkpoint)

- Divergenza dei file congelati rispetto al tag `merenda-system-v1.0` (nota fin dal checkpoint 125).
- Disallineamento d'ordine fra `catalog.json` e `VIDEO_INDEX.md`/`QUEUE.md` per un ampio numero di righe (836, verificato identico prima/dopo questo checkpoint).
- Le etichette contate da `scripts/validate_project.py` in `STATUS.md` ("Video completati"/"Video rimanenti") non coincidono testualmente con il formato narrativo usato in `STATUS.md` dai checkpoint precedenti.

Nessuna di queste è stata "riparata" in questo checkpoint, come richiesto esplicitamente dall'istruzione (non tentare di correggere automaticamente differenze storiche rispetto al tag v1.0).

## Conferme di governance

- Nessuna conoscenza esterna al canale `@FrankMerendaTV` introdotta.
- Formalife non compare in `merenda/` (verificato con ricerca case-insensitive).
- MERGE, NON APPEND rispettato: nessun nuovo file creato per singoli video; l'unica modifica di contenuto è stata uno spostamento strutturale (Collegamenti) senza alterare il merito.
- Nessun file elencato in `system/FROZEN_FILES.md` modificato.
- Nessun contenuto 151+ acquisito, letto o marcato.
- Fase 15 eseguita come dovuto al checkpoint 150 (ogni 50 video).
