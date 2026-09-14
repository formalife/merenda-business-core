# Checkpoint 275 — pre-handoff Claude — FASE 14 richiesta

Stato raggiunto da ChatGPT sul branch `semantic-251-275`, costruito dalla HEAD tecnica `d4f1e9ee6271d5a1f7b6849c4e1b8d78635c5bc5` del branch `acquisition-251-275`.

Questo documento è il **pre-handoff del checkpoint 275**. La revisione semantica 251–275 è completa; il checkpoint Claude deve ancora eseguire **FASE 14**. FASE 15 non è dovuta a 275: il prossimo audit tassonomia è a 300.

## Stato al raggiungimento della soglia 275

- Video individuati: **468**
- Contenuti processati semanticamente: **275**
- `STUDIATO`: **269**
- `ESCLUSO`: **6**
- `DA STUDIARE`: **193**
- Corpus completo: **NO**
- Batch 251–275: **25/25 STUDIATO**
- Nuovi ESCLUSO nel batch: **0**
- Review 251–275: **25/25**
- Primo contenuto non processato: **276 — `Hs8y1wNyamo` — “THE ideal SALES PROCESS for generating TARGETED clients”**

## Base tecnica 251–275

Handoff Codex:

- branch: `acquisition-251-275`
- base: `e75aeca6b76f2e94678608dd90a2e550d7d486db`
- HEAD tecnica: `d4f1e9ee6271d5a1f7b6849c4e1b8d78635c5bc5`
- tentati / acquisiti / transcript utilizzabili: **25 / 25 / 25**
- sottotitoli automatici italiani originali / manuali: **25 / 0**
- ASR / NO_IT_TRANSCRIPT / errori finali / pending: **0 / 0 / 0 / 0**
- keyframe: **22 su 8 video**
- validator tecnico prima/dopo: **842 / 842, identico**
- `git diff --check`: pulito
- frozen, KB e semantica invariati nella fase tecnica

Limiti tecnici documentati da Codex:

- code non coperte: 252 **2,640 s**; 253 **5,440 s**; 259 **13,320 s**; 262 **8,681 s**; 263 **9,401 s**;
- sforamenti timestamp positivi fino a **2,240 s**;
- limiti visuali specifici per 253/261 documentati nel report tecnico.

Nessuna nuova regola semantica è stata basata sulle code non coperte.

## Esito semantico 251–275

### Novelty globale

- **Incrementali: 11/25 = 44%**
- **Deduplicati/confermativi: 14/25 = 56%**
- Nessun nuovo ESCLUSO

Incrementali:

- 253 — `-_oOcTQgkcY`
- 254 — `P_LavmWySLs`
- 255 — `an5eXiIyyiA`
- 256 — `wDPyGhkY_CA`
- 257 — `oefQwsBIUc0`
- 258 — `jzQcezkw8_o`
- 261 — `A4I-A5hldQw`
- 264 — `9FpKpV15B_4`
- 266 — `NB9g-DhSj-4`
- 268 — `IGR6IPPvY3Q`
- 270 — `21iVqc13KoE`

Deduplicati/confermativi:

- 251, 252, 259, 260, 262, 263, 265, 267, 269, 271, 272, 273, 274, 275

### Routing finale 251–275

| Categoria | N |
|---|---:|
| 01_mercato | 2 |
| 02_posizionamento | 1 |
| 03_offerta | 1 |
| 04_marketing | 1 |
| 05_acquisizione | 3 |
| 06_vendita | 11 |
| 07_copy_comunicazione | 1 |
| 08_brand | 2 |
| 09_business | 1 |
| 10_casi_studio | 2 |
| **Totale** | **25** |

## Nuovi nodi KB creati

1. `merenda/04_marketing/test-creativita-annunci.md`
2. `merenda/06_vendita/rete-vendita-script-allenamento-e-controllo.md`
3. `merenda/08_brand/pr-earned-media-e-notiziabilita.md`

Tutti sono collegati dai rispettivi README.

## Altri nodi KB modificati

- `merenda/01_mercato/clienti-identificabili-e-target.md`
- `merenda/02_posizionamento/differenziazione-operativa.md`
- `merenda/03_offerta/front-end-e-back-end.md`
- `merenda/03_offerta/prezzo-premium-e-percezione-del-valore.md`
- `merenda/06_vendita/prequalifica-follow-up-decisori.md`
- `merenda/06_vendita/preventivo-consulenza-diagnosi.md`
- `merenda/07_copy_comunicazione/priorita-azione-e-inerzia.md`
- README di `04_marketing`, `06_vendita`, `08_brand`.

## Integrazioni principali

### 253 — sistema operativo della rete vendita

Creato `merenda/06_vendita/rete-vendita-script-allenamento-e-controllo.md`.

Principi integrati:

- script come sequenza di domande e passaggi, non monologo rigido;
- role-play e retraining ricorrenti;
- registrazione/review delle interazioni quando lecita;
- ciclo osservazione → feedback → allenamento → nuova misura;
- preparazione pre-incontro;
- selezione e allenabilità delle persone;
- incentivi e percorso di crescita coerenti con qualità/economia;
- testimonianze anche come materiale interno per sostenere la convinzione della rete.

Il modello “CHIARO” non viene duplicato come secondo processo canonico: i suoi componenti erano già coperti da diagnosi, follow-up e onboarding.

### 254 — trade-off dichiarato e auto-selezione

Aggiornato `merenda/02_posizionamento/differenziazione-operativa.md`.

Principio:

**limite reale dichiarato → maggiore credibilità della promessa → selezione del target compatibile.**

La parola “ma” non viene trattata come formula magica; non si inventano difetti e la dichiarazione non sostituisce la correzione di problemi reali.

### 255 — creative testing senza reset continuo

Creato `merenda/04_marketing/test-creativita-annunci.md`.

Principio:

**winner storico → variazioni controllate → test → selezione → ulteriore sfruttamento + quota separata di sperimentazione.**

Il rapporto 80/20, il numero degli annunci e i formati del 2024 non diventano soglie universali.

### 256 — tre assi di upsell

Aggiornato `merenda/03_offerta/front-end-e-back-end.md` con la tassonomia pratica:

- quantità;
- qualità;
- completezza / feature.

La regola generale più recente del 2025 resta prevalente.

### 257–258 — struttura e performance management della rete vendita

Aggiornato il nodo della rete vendita.

257 aggiunge la protezione del tempo ad alto valore del venditore e la specializzazione progressiva di appointment setting, vendita, supporto e sollecito crediti quando volume ed economics lo giustificano.

258 aggiunge quattro livelli di gestione della performance:

1. norma / standard minimo;
2. incentivi per sovraperformance utile;
3. performance review e retraining;
4. turnover/ricollocazione quando il recupero non funziona.

Il risultato commerciale non viene ridotto al fatturato lordo: mix, qualità contratti, incassi e appropriatezza contano.

### 261 — PR ed earned media

Creato `merenda/08_brand/pr-earned-media-e-notiziabilita.md`.

Procedura:

**credibilità owned → angolo notiziabile → hook/asset → frontman → outreach → earned media → riuso nel marketing.**

Le metriche del caso non diventano benchmark.

### 264 — attenzione che deve essere rinnovata

Aggiornato `merenda/07_copy_comunicazione/priorita-azione-e-inerzia.md`.

Principio:

**aggancio → rilevanza continua → prova nel punto della promessa → passo successivo.**

### 266 — validare prima di prescrivere

Aggiornato `merenda/06_vendita/preventivo-consulenza-diagnosi.md`.

La sequenza aggiunge una componente conversazionale:

**narrazione del cliente → approfondimento → conseguenze pratiche/emotive → validazione dell'esperienza → diagnosi → prescrizione.**

Validare non significa concordare artificialmente con ogni interpretazione del cliente né simulare empatia.

### 268 — consapevolezza × storia di acquisto

Aggiornato `merenda/01_mercato/clienti-identificabili-e-target.md`.

La maturità decisionale viene distinta dal semplice target:

1. non percepisce il problema;
2. percepisce il problema ma dubita della soluzione;
3. confronta approcci;
4. sceglie una famiglia di soluzione;
5. sceglie il fornitore.

La seconda dimensione riguarda la storia di acquisto: mai acquistato / provato e smesso / usa ancora una soluzione, con diverso livello di soddisfazione.

Principio:

**target corretto ≠ stessa maturità decisionale → identificare lo stato → usare messaggio e sforzo commerciale coerenti.**

Il linguaggio della fonte sul “creare terrore” non è canonizzato: si comunicano soltanto conseguenze reali e supportate.

### 270 — learning dip nell'adozione dello script

Aggiornato il nodo della rete vendita.

Quando un venditore abituato all'improvvisazione adotta un processo nuovo, può comparire un calo iniziale di fluidità o performance. Questo non dimostra automaticamente che il metodo sia peggiore.

Sequenza:

**nuovo standard → pratica guidata → possibile disagio/errore iniziale → feedback/ripetizione → nuova misurazione.**

Non è una curva garantita: dopo addestramento sufficiente il metodo va comunque giudicato sui KPI.

## Prevalenza temporale e deduplicazioni rilevanti

- 251 e 262: vecchie formulazioni su script/processo deduplicate rispetto alla dottrina 2025 **diagnosi standardizzata → prescrizione personalizzata** e al nuovo nodo rete vendita.
- 263: autorità nella trattativa già meglio coperta da fonti successive; “l'autorità non negozia” non viene trattato come assoluto.
- 265: “prima sistema, poi più venditori/lead” già consolidato dalla gerarchia di crescita 2024–2025.
- 267: funnel opt-in → materiale → pacco fisico → evento → one-to-one già coperto dai nodi information marketing/database/eventi.
- 269: la piramide early adopter e le percentuali non diventano distribuzione universale; il 268 è la fonte più recente e specifica sulla maturità decisionale.
- 271: journey mentale del 13 febbraio 2023 deduplicato rispetto al modello più recente del 9 marzo 2023 integrato col 268.
- 272: i “5 livelli di chiarezza” sono una sintesi didattica di target, messaggio, prove e processo già canonici.
- 273–275: materiale gennaio 2023 su segmentazione lifecycle e passaggio dal freddo alla lead generation già coperto da fonti successive; il divieto assoluto del freddo è superato dal quadro 2024 sulle quattro modalità di marketing.

## Validazione post-semantica reale

Il validator è stato eseguito realmente sul branch semantico dopo la chiusura 251–275.

Risultato misurato:

- `python3 scripts/validate_project.py`: **842 righe**, exit code 1 per warning storici;
- `Ordine/stato incoerente`: **836**;
- `File congelato modificato`: **3**;
- `Contatore STATUS errato`: **3**;
- totale: **842**, identico alla baseline reale del checkpoint 250;
- `git diff --check` sul delta dal checkpoint 250: **pulito**.

Quindi la revisione 251–275 non ha introdotto alcuna nuova classe o incremento di warning.

I tre warning “File congelato modificato” appartengono al mismatch storico del validator già documentato; il confronto Git effettivo del batch non include modifiche ai file frozen.

## Verifiche di integrità

- 25 review per 251–275: **OK**
- tutti 251–275 `STUDIATO`: **OK**
- 276 ancora `DA STUDIARE`: **OK**
- nessuna review 276+: **OK**
- nessun nuovo `ESCLUSO`: **OK**
- categorie finali riallineate in catalogo, index e queue: **OK**
- frozen effettivamente non modificati nel batch: **OK**
- nessuna contaminazione Formalife nella KB Merenda: **OK**
- workflow temporanei usati solo per sincronizzazione/validazione rimossi dal tree finale: **OK**

## Handoff richiesto — CLAUDE CODE

Prossimo agente: **CLAUDE CODE**.

Prossima azione: **CHECKPOINT 275 — FASE 14**.

Claude deve:

1. rileggere/refactorare strutturalmente l'intera KB secondo FASE 14;
2. controllare in particolare il nuovo nodo denso `06_vendita/rete-vendita-script-allenamento-e-controllo.md` e i suoi confini con `preventivo-consulenza-diagnosi.md` e `prequalifica-follow-up-decisori.md`;
3. controllare `04_marketing/test-creativita-annunci.md` per sovrapposizioni con complessità/test/canali;
4. controllare `08_brand/pr-earned-media-e-notiziabilita.md` rispetto ad `autorita-e-marketing.md`;
5. controllare la nuova sezione consapevolezza/storia acquisto in `01_mercato/clienti-identificabili-e-target.md` rispetto a domanda, trigger, lifecycle e appropriatezza;
6. applicare MERGE, NOT APPEND e rimuovere eventuali duplicazioni reali;
7. preservare la prevalenza delle fonti più recenti;
8. non processare semanticamente alcun contenuto 276+;
9. non modificare i file frozen;
10. rieseguire il validator prima e dopo il refactor e confrontare con la baseline **842 = 836 + 3 + 3**;
11. verificare `git diff --check`, link/orfani e contaminazione Formalife;
12. aggiornare `reviews/CHECKPOINT_275.md` da pre-handoff a report definitivo e `STATUS.md` al termine.

**FASE 15 non è dovuta a 275.** Il prossimo checkpoint con FASE 14 + FASE 15 è **300**.
