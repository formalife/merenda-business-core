# Crosswalk — 01 Mercato

## Scope

File coperti:

- `merenda/01_mercato/README.md`
- `merenda/01_mercato/clienti-identificabili-e-target.md`
- `merenda/01_mercato/appropriatezza-clienti.md`
- `merenda/01_mercato/clienti-altospendenti.md`
- `merenda/01_mercato/quattro-domande-prima-di-lanciare.md`

Stato: **COMPLETE — first semantic pass**.

Nota: il README di sezione è routing/reference e non introduce unità autonome. Le unità sotto consolidano il contenuto dei quattro nodi specialistici. Dove `00_fondamenti` aveva già una sintesi, questa sezione assume la casa primaria del concetto mercato/cliente e lascia il fondamento come orientamento cross-cutting.

---

# A. Validità del mercato prima del prodotto

## MRC-001 — Prima verificare il mercato, poi aggiungere prodotto

**Tipo:** GATE / DECISION_RULE  
**Ruolo candidato:** PRIMARY  
**Fonte canonica:** `quattro-domande-prima-di-lanciare.md`

### Unità di conoscenza

Quando la crescita è debole, aggiungere un prodotto è soltanto una possibile risposta. Prima bisogna verificare se il vincolo reale è domanda, raggiungibilità, capacità di acquisto, debolezza strutturale del mercato, marketing o vendita.

### Il lettore deve saper fare

Trattare “serve un altro prodotto” come ipotesi da verificare, non come diagnosi.

### Dipendenze

FND-022, FND-023, FND-057.

---

## MRC-002 — Domanda reale e sufficiente

**Tipo:** DEFINITION / GATE  
**Ruolo candidato:** PRIMARY

### Unità di conoscenza

Un mercato è più interessante quando esistono persone o aziende che stanno già cercando di risolvere il problema o soddisfare il desiderio. Interesse del founder, competenza tecnica o novità del prodotto non provano da sole la domanda.

### Decisione operativa

Prima di investire chiedere: esiste una quantità economicamente sufficiente di domanda riconoscibile?

### Caveat

Non implica che sia impossibile creare una categoria nuova. Implica che educare un mercato inesistente richiede normalmente più tempo, capitale e rischio, soprattutto per una PMI.

---

## MRC-003 — Identificabilità e raggiungibilità sono parte della qualità del mercato

**Tipo:** GATE / CAUSAL_RULE  
**Ruolo candidato:** PRIMARY

### Unità di conoscenza

Domanda esistente non basta. Bisogna sapere chi sono i potenziali clienti, dove si trovano, quali media o recapiti permettono di raggiungerli e con quale costo.

### Formula operativa

domanda esistente + target identificabile + accesso economicamente sostenibile → mercato acquisibile.

### Collegamenti

FND-010, FND-025, FND-029.

---

## MRC-004 — Il mezzo di raggiungimento è subordinato alla precisione e agli economics

**Tipo:** DECISION_RULE / CAVEAT  
**Ruolo candidato:** SUPPORTING

Online e offline non sono scelte ideologiche. Nel B2B o in cluster facilmente enumerabili, un recapito fisico o un database diretto può essere più preciso di un targeting digitale imperfetto; in altri mercati accade il contrario.

### Il lettore deve saper fare

Scegliere il mezzo in base a raggiungibilità, precisione, costo e funzione, non in base alla moda del canale.

### Dipendenze

MRC-003; prevalenza specialistica futura in `04_marketing`.

---

## MRC-005 — Capacità di acquisto come vincolo strutturale

**Tipo:** GATE / CAUSAL_RULE  
**Ruolo candidato:** PRIMARY

### Unità di conoscenza

Avere il problema o desiderare la soluzione non significa poter sostenere il prezzo necessario a rendere il business profittevole.

### Decisione operativa

Verificare che capacità e disponibilità economica del target siano compatibili con prezzo, margine e modello di erogazione.

### Dipendenze

FND-032, FND-042.

---

## MRC-006 — Capacità economica, propensione a spendere e comprensione del valore sono variabili diverse

**Tipo:** DEFINITION / CAUSAL_RULE  
**Ruolo candidato:** PRIMARY

### Unità di conoscenza

Tre domande diverse non vanno confuse:

1. il prospect può sostenere economicamente l'acquisto?;
2. attribuisce abbastanza priorità alla soluzione da voler spendere?;
3. ha compreso la differenza che giustifica prezzo e condizioni?

Una persona con alta capacità economica può essere price-sensitive in una categoria percepita come commodity; una persona meno abbiente può dare priorità eccezionale a un problema specifico.

### Implicazione

“Non vuole spendere” non identifica automaticamente un problema di reddito, target o pricing.

---

## MRC-007 — Direzione del mercato come variabile di rischio

**Tipo:** DECISION_RULE / CAVEAT  
**Ruolo candidato:** PRIMARY

### Unità di conoscenza

Un cluster in crescita offre normalmente condizioni più favorevoli di uno in contrazione. Un mercato calante non è automaticamente da escludere, ma richiede maggiore cautela e un vantaggio più forte.

### Il lettore deve saper fare

Distinguere domanda attuale da trend della domanda.

---

## MRC-008 — Le quattro verifiche di mercato non provano il successo

**Tipo:** CAVEAT / GATE  
**Ruolo candidato:** PRIMARY

Superare domanda, raggiungibilità, capacità d'acquisto e trend non rende automaticamente vincente il business. Restano da risolvere differenziazione, offerta, marginalità, acquisizione, vendita, delivery e capacità.

### Collegamento

FND-021, FND-025.

---

## MRC-009 — Prima sfruttare meglio il sistema esistente, poi moltiplicare prodotti

**Tipo:** DECISION_RULE / ERROR_PATTERN  
**Ruolo candidato:** PRIMARY

Se il mercato è valido ma la crescita è debole, verificare prima leve sul sistema esistente: metodo, canali, budget dove i numeri reggono, contenuti, front-end/back-end, upsell/cross-sell, continuity e vendita.

### Errore tipico

Aggiungere SKU per compensare un motore commerciale debole.

### Dipendenze

FND-033, FND-060.

---

# B. Identificabilità, target e priorità commerciale

## MRC-010 — Target facilmente identificabile vs target difficile da identificare

**Tipo:** DEFINITION / DECISION_RULE  
**Ruolo candidato:** PRIMARY

### Unità di conoscenza

Alcuni target sono facilmente enumerabili e localizzabili; altri potrebbero includere molte persone ma senza un criterio semplice per trovarle. La difficoltà cambia la priorità del lavoro.

### Priorità

- target identificabile: differenziazione e follow-up diventano spesso il primo problema;
- target sfuggente: prima serve un modo economicamente sostenibile per identificarlo e raggiungerlo.

### Caveat

È una distinzione operativa, non una tassonomia rigida di settori.

---

## MRC-011 — “Tutti possono comprare” non è un target operativo

**Tipo:** ERROR_PATTERN / DECISION_RULE  
**Ruolo candidato:** PRIMARY

### Unità di conoscenza

Una popolazione teoricamente ampia non aiuta a decidere dove investire comunicazione, tempo e budget. Un target utile deve restringere abbastanza il campo da permettere identificazione, messaggio e acquisizione economicamente leggibili.

### Conseguenza

Ampiezza teorica del mercato e acquisibilità del mercato sono concetti diversi.

---

## MRC-012 — Nei mercati già serviti la vendita è spesso sostitutiva

**Tipo:** CAUSAL_RULE / DECISION_RULE  
**Ruolo candidato:** PRIMARY

Quando il prospect usa già una soluzione, la competizione non è contro il “non acquisto” ma contro una alternativa presente. La proposta deve mostrare perché cambiare è razionale per quella situazione.

### Influenza a valle

Posizionamento, prova, switching cost, vendita.

---

## MRC-013 — L'innovazione iniziale non elimina la necessità di difendere la preferenza

**Tipo:** CAUSAL_RULE  
**Ruolo candidato:** SUPPORTING

Un'innovazione può creare temporaneamente spazio competitivo, ma imitazioni e alternative riducono il vantaggio. L'impresa deve costruire ragioni per mantenere la preferenza oltre la novità iniziale.

### Caveat

Qualità, assistenza e sconto generici non costituiscono automaticamente una differenza difendibile.

---

## MRC-014 — Il settore non è ancora il cliente ideale

**Tipo:** DEFINITION / PRINCIPLE  
**Ruolo candidato:** PRIMARY

“Dentisti”, “ristoranti”, “chi vuole dimagrire” o categorie simili non definiscono ancora un cliente ideale. Dentro il target cambiano economia, struttura, prezzo, geografia, desideri, priorità, capacità di spesa e problemi.

### Il lettore deve saper fare

Passare dalla categoria ampia a un profilo decisionale ed economico utilizzabile.

---

## MRC-015 — Il cliente ideale parte come ipotesi e viene corretto dai dati

**Tipo:** PROCEDURE / FEEDBACK_LOOP  
**Ruolo candidato:** PRIMARY

### Procedura

1. descrivere i clienti che si vorrebbe replicare;
2. identificare caratteristiche potenzialmente rilevanti;
3. confrontarle con margine, frequenza, comportamento e risultati reali;
4. correggere progressivamente il profilo.

### Collegamento

FND-049.

---

## MRC-016 — Prima campagna focalizzata, segmenti secondari dopo

**Tipo:** DECISION_RULE  
**Ruolo candidato:** PRIMARY

Quando esistono più segmenti, la prima campagna dovrebbe concentrarsi sul cliente prioritario più desiderabile invece di creare subito un messaggio medio per tutti. Segmenti secondari possono ricevere campagne distinte in seguito.

### Ragione causale

Problemi, linguaggio e dialogo mentale differenti riducono la precisione di un messaggio generalista.

---

# C. Stato decisionale e progettazione della campagna

## MRC-017 — Stesso target non significa stessa maturità decisionale

**Tipo:** PRINCIPLE / CAUSAL_RULE  
**Ruolo candidato:** PRIMARY

Due persone con lo stesso profilo possono trovarsi in stati molto diversi per consapevolezza, storia d'acquisto, soddisfazione e relazione con l'azienda. Il messaggio non va quindi dedotto solo dal segmento anagrafico o professionale.

### Collegamento

FND-034, FND-036.

---

## MRC-018 — Awareness × storia d'acquisto × soddisfazione cambia il lavoro commerciale

**Tipo:** DEPENDENCY / DECISION_RULE  
**Ruolo candidato:** PRIMARY

### Stati esemplificativi

- mai acquistato una soluzione;
- ha acquistato e smesso;
- usa una soluzione ed è aperto;
- usa una soluzione e vuole cambiare;
- usa una soluzione ed è molto soddisfatto.

### Implicazione

Ogni stato richiede quantità diversa di educazione, prova, differenziazione e pressione commerciale.

### Caveat

La scala awareness canonica sarà trattata in `04_marketing`; qui il punto è il suo uso con storia e soddisfazione.

---

## MRC-019 — La priorità commerciale dipende anche dall'alternativa attuale

**Tipo:** DECISION_RULE  
**Ruolo candidato:** PRIMARY

Chi sta cercando attivamente un sostituto è normalmente più vicino a una decisione rispetto a chi è molto soddisfatto della soluzione attuale. Il costo di persuasione atteso deve influenzare la priorità del segmento.

### Errore tipico

Trattare ogni prospect nel target come se fosse ugualmente convertibile.

---

## MRC-020 — Modello multi-asse della campagna

**Tipo:** DEPENDENCY / PROCEDURE  
**Ruolo candidato:** PRIMARY

### Modello

**stato della relazione × livello di consapevolezza × profilo rilevante × grado di directness → campagna → transizione desiderata.**

### Il lettore deve saper fare

Per una campagna dichiarare almeno:

- chi è la persona rispetto all'azienda;
- che cosa sa già;
- quali caratteristiche del profilo cambiano la decisione;
- quanto può essere diretta la comunicazione;
- quale passaggio deve produrre.

### Caveat

Non serve costruire una matrice burocratica di tutte le combinazioni possibili.

---

## MRC-021 — Profilare solo ciò che cambia una decisione

**Tipo:** DECISION_RULE / CAVEAT  
**Ruolo candidato:** PRIMARY

Età, territorio, ruolo, istruzione, cultura o altri dati meritano peso solo se cambiano messaggio, offerta, prova, canale, timing o percorso.

### Errore tipico

Trasformare correlazioni o categorie descrittive in stereotipi senza evidenza comportamentale o economica.

---

## MRC-022 — Cliente ideale = fit + comportamento osservato

**Tipo:** DEFINITION / PRINCIPLE  
**Ruolo candidato:** PRIMARY

Oltre all'economia, il cliente desiderabile deve essere compatibile con problema, soluzione, aspettative, capacità di implementazione e comportamento reale: compra, paga, usa, applica, ottiene risultati, resta e può generare prova.

### Caveat

Questo completa, ma non sostituisce, margine, LTV, RFM e cost-to-serve.

---

# D. Appropriatezza e qualità economica del cliente

## MRC-023 — Appropriatezza come fit bidirezionale

**Tipo:** DEFINITION / PRINCIPLE  
**Ruolo candidato:** PRIMARY

### Unità di conoscenza

La qualità del cliente dipende da quanto quel cliente è adatto all'azienda e da quanto l'azienda è adatta a servirlo bene e profittevolmente.

### Conseguenza

Il problema non è massimizzare il numero di clienti, ma costruire una base che l'impresa sappia servire con buon risultato ed economia.

---

## MRC-024 — Fatturato del cliente ≠ valore economico del cliente

**Tipo:** CAUSAL_RULE / ERROR_PATTERN  
**Ruolo candidato:** PRIMARY

Un cliente può generare ricavi elevati ma poco profitto reale; un altro può spendere meno ma essere più fedele, semplice da servire e profittevole nel tempo.

### Metriche collegate

Margine, spesa annua, LTV, frequenza, recency, cost-to-serve.

### Dipendenze

FND-041, FND-042.

---

## MRC-025 — Il margine reale deve includere i costi occulti della relazione

**Tipo:** DEFINITION / METRIC  
**Ruolo candidato:** PRIMARY

Assistenza sproporzionata, rilavorazioni, solleciti, attrito, tempo del team, ripensamenti e condizioni di pagamento consumano capacità e margine anche quando non sono contabilizzati come costo diretto di prodotto.

### Il lettore deve saper fare

Valutare il contributo economico del cliente includendo il costo di servirlo.

---

## MRC-026 — Una vendita può essere cattiva anche se incassa

**Tipo:** PRINCIPLE / GATE  
**Ruolo candidato:** PRIMARY

La chiusura è economicamente valida solo se coerente con target, capacità di erogazione, regole dell'impresa e interesse di lungo periodo. In alcuni casi l'azienda deve poter rifiutare il cliente.

### Collegamento

FND-055.

---

## MRC-027 — Tradurre l'appropriatezza in criteri di accettazione

**Tipo:** PROCEDURE / GATE  
**Ruolo candidato:** PRIMARY

### Criteri candidati

- margine atteso;
- condizioni e tempi di pagamento;
- rischio di insoluto;
- costo di delivery e assistenza;
- capacità richiesta;
- coerenza con il target e con lo standard operativo.

### Decisione operativa

Definire soglie sotto le quali l'ordine non va accettato o va riprogettato.

---

## MRC-028 — La funzione economica deve poter fermare una vendita distruttiva

**Tipo:** DECISION_RULE / GOVERNANCE  
**Ruolo candidato:** PRIMARY

Gli incentivi alla chiusura commerciale non devono prevalere sull'economia dell'impresa. Chi controlla margine, cassa e rischio deve poter bloccare ordini che aumentano fatturato ma distruggono valore.

### Influenza a valle

Compensation, sales governance, finance, capacity.

---

## MRC-029 — Il marketing deve sostituire domanda cattiva con domanda migliore

**Tipo:** CAUSAL_RULE / PRINCIPLE  
**Ruolo candidato:** PRIMARY

Rifiutare clienti inappropriati senza generare alternative può ridurre soltanto il volume. Il secondo movimento è usare marketing e targeting per aumentare la quota di domanda desiderabile.

### Formula

filtri economici + acquisizione di clienti migliori → libertà di selezione.

---

## MRC-030 — L'offerta e l'esperienza possono favorire auto-selezione

**Tipo:** DECISION_RULE  
**Ruolo candidato:** SUPPORTING

Prodotto, servizio, ambiente, condizioni e comunicazione possono segnalare a chi è adatto il sistema. Il cliente desiderato deve riconoscere valore; chi cerca condizioni incompatibili dovrebbe percepire il mismatch prima possibile.

### Caveat

Non significa creare ostacoli artificiali o esclusività teatrale.

---

## MRC-031 — Segmentare sulla base di evidenza economica, non stereotipi

**Tipo:** PRINCIPLE / CAVEAT  
**Ruolo candidato:** PRIMARY

Caratteristiche demografiche, geografiche, professionali o comportamentali sono utili se correlano con valore, probabilità di acquisto, risultati o cost-to-serve. Non sono criteri universali per conto proprio.

### Domanda guida

Quale cluster produce più valore, resta più a lungo e costa meno da servire?

---

## MRC-032 — RFM come lettura comportamentale del database clienti

**Tipo:** METRIC / PROCEDURE  
**Ruolo candidato:** PRIMARY

### Dimensioni

- Recency: quanto recentemente ha comprato;
- Frequency: quanto spesso compra;
- Monetary: quanto valore monetario genera.

### Funzione

Distinguere clienti responsivi, frequenti e ad alto valore da clienti occasionali o dormienti per progettare campagne differenti.

### Caveat

RFM non sostituisce margine, LTV o costi occulti.

---

## MRC-033 — Abbastanza domanda crea potere di selezione

**Tipo:** CAUSAL_RULE / PRINCIPLE  
**Ruolo candidato:** PRIMARY

Quando la domanda è scarsa, una PMI può sentirsi costretta ad accettare quasi chiunque. Una pipeline più ampia permette di proteggere margine, rifiutare mismatch e servire meglio i clienti appropriati.

### Formula

più domanda qualificata → maggiore possibilità di selezione → migliore economia e delivery.

---

## MRC-034 — Risorse limitate: lavorare una coorte prioritaria finita

**Tipo:** PROCEDURE / DECISION_RULE  
**Ruolo candidato:** PRIMARY

### Sequenza

**evidenze sui clienti migliori → coorte prioritaria finita → concentrazione di contatti/materiali/risorse → misura della risposta e dell'economia → estensione progressiva.**

### Caveat

Il numero della coorte non è universale. Il principio è concentrare pressione sufficiente prima di aprire troppi fronti.

---

## MRC-035 — Whale curve per individuare clienti che erodono profitto

**Tipo:** PROCEDURE / METRIC  
**Ruolo candidato:** PRIMARY

### Procedura

1. stimare profitto reale per cliente includendo cost-to-serve;
2. ordinare i clienti dal più al meno profittevole;
3. calcolare profitto cumulativo;
4. individuare la coda che erode il profitto generato dai clienti migliori;
5. intervenire su prezzo, livello di servizio, condizioni o relazione.

### Caveat

Non assumere le percentuali degli esempi come benchmark universali.

---

## MRC-036 — Proof by Refusal

**Tipo:** PRINCIPLE / EXAMPLE / CAVEAT  
**Ruolo candidato:** SUPPORTING  
**Provenance backend:** fonte assimilata, non attribuire a Merenda nel backend editoriale.

### Unità di conoscenza

Uno standard dichiarato diventa più credibile quando l'impresa sostiene un costo reale per rispettarlo, per esempio rifiutando ricavi incompatibili con interesse del cliente, posizionamento o standard.

### Formula

standard dichiarato → sacrificio osservabile coerente → costo reale → maggiore credibilità.

### Caveat

Rifiuto artificiale, scarsità teatrale o rinuncia economicamente insostenibile non costituiscono prova.

---

# E. Clienti alto-spendenti e architettura di valore

## MRC-037 — Alto-spendente è una categoria relativa al business

**Tipo:** DEFINITION  
**Ruolo candidato:** PRIMARY

Un cliente alto-spendente è chi può e vuole acquistare livelli superiori dell'offerta perché attribuisce valore a una esperienza o servizio più elevato. La soglia economica cambia radicalmente per categoria.

### Caveat

Non equivale automaticamente a patrimonio elevato.

---

## MRC-038 — La propensione premium può essere specifica per categoria

**Tipo:** CAUSAL_RULE / CAVEAT  
**Ruolo candidato:** PRIMARY

Una stessa persona può spendere molto in una categoria e minimizzare il prezzo in un'altra. Il comportamento dipende da priorità, differenza percepita e alternativa, non soltanto dal patrimonio.

### Collegamento

MRC-006.

---

## MRC-039 — Per segmenti filtrati, il network può precedere il contatto diretto

**Tipo:** DECISION_RULE  
**Ruolo candidato:** SUPPORTING

Più il target è protetto da assistenti, consulenti, pari e reti fiduciarie, più una introduzione qualificata può essere efficiente di un approccio standard a freddo.

### Modello

persona fidata → pre-valutazione → introduzione/raccomandazione → fornitore.

---

## MRC-040 — Emulazione dei pari come prova sociale rilevante

**Tipo:** CAUSAL_RULE / EXAMPLE  
**Ruolo candidato:** SUPPORTING

L'adozione da parte di un pari, superiore o soggetto aspirazionale può aumentare desiderabilità anche senza una raccomandazione esplicita.

### Casa specialistica futura

`08_brand` / prova sociale.

---

## MRC-041 — Anticipazione e status possono essere driver di valore

**Tipo:** CAUSAL_RULE / CAVEAT  
**Ruolo candidato:** SUPPORTING

Per alcuni segmenti il valore include essere tra i primi ad accedere, conoscere, provare o possedere. Va trattato come driver possibile, non come motivazione universale.

---

## MRC-042 — Se non esiste un livello superiore, la willingness-to-pay non può esprimersi

**Tipo:** CAUSAL_RULE / DECISION_RULE  
**Ruolo candidato:** PRIMARY

“Voglio clienti migliori” è incoerente se l'offerta termina al livello standard. Per catturare differenze di disponibilità a spendere servono livelli di valore acquistabili.

### Sequenza candidata

entry/basic → livelli intermedi → premium → VIP/top.

### Casa specialistica futura

`03_offerta`; qui resta il nesso mercato-segmento.

---

## MRC-043 — Premium = esperienza superiore, non markup arbitrario

**Tipo:** PRINCIPLE / CAVEAT  
**Ruolo candidato:** SUPPORTING

Priorità, tempo risparmiato, accesso, personalizzazione, consulenza, comodità, servizio ed esclusività possono sostenere livelli superiori. La stessa cosa con prezzo moltiplicato non crea automaticamente valore premium.

### Prevalenza specialistica futura

`03_offerta/prezzo-premium-e-percezione-del-valore.md`.

---

## MRC-044 — Nel premium, accesso e trattamento possono battere lo sconto

**Tipo:** DECISION_RULE  
**Ruolo candidato:** SUPPORTING

Per alcuni clienti premium, accesso riservato, anticipazione, esperienza o trattamento speciale possono generare più valore percepito di una riduzione di prezzo e proteggere meglio il margine.

### Caveat

Non è una regola universale; va verificato il valore percepito reale.

---

## MRC-045 — Una nicchia premium deve essere abbastanza grande nel bacino servito

**Tipo:** GATE / DECISION_RULE  
**Ruolo candidato:** PRIMARY

Una nicchia attraente a livello nazionale può essere troppo piccola per sostenere una sede locale. La geografia deve essere valutata insieme a dimensione della domanda e economics.

### Collegamento

MRC-002, MRC-003, MRC-007.

---

# F. Durata naturale della relazione e ruoli nell'acquisto

## MRC-046 — Alcune relazioni hanno una scadenza naturale

**Tipo:** DEFINITION / CAUSAL_RULE  
**Ruolo candidato:** PRIMARY

Clienti legati a età, fase familiare, percorso educativo, evento una tantum o problema risolto possono uscire dal mercato anche se soddisfatti.

### Implicazione

Churn e retention vanno interpretati rispetto alla durata naturale della relazione appropriata.

---

## MRC-047 — Durata naturale della relazione entra direttamente in CAC, LTV e sostituzione della base

**Tipo:** METRIC / DEPENDENCY  
**Ruolo candidato:** PRIMARY

La prima domanda è: quanto dura mediamente una relazione appropriata? La risposta modifica LTV atteso, payback accettabile e quantità di nuova acquisizione necessaria per sostituire le coorti in uscita.

### Dipendenze

FND-032, FND-042.

---

## MRC-048 — Utilizzatore e pagatore possono essere persone diverse

**Tipo:** DEFINITION / PRINCIPLE  
**Ruolo candidato:** PRIMARY

### Distinzione

- utilizzatore/consumatore: vive l'esperienza;
- pagatore/decisore economico: decide se il valore giustifica la spesa.

### Regola

**esperienza per chi usa + ragione per chi paga → acquisto sostenibile.**

### Implicazione

Prodotto, proof e comunicazione possono dover rispondere a bisogni differenti.

---

## MRC-049 — Un target può restare stabile mentre le coorti ruotano

**Tipo:** PRINCIPLE / CAUSAL_RULE  
**Ruolo candidato:** PRIMARY

Un business non deve necessariamente seguire ogni cliente per tutta la vita. Può mantenere una posizione stabile mentre nuove coorti entrano e quelle precedenti escono naturalmente.

### Formula

target stabile → coorti in entrata/uscita → posizione riconoscibile.

---

## MRC-050 — Seguire il cliente nella fase successiva non giustifica automaticamente un'estensione di categoria

**Tipo:** DECISION_RULE / CAVEAT  
**Ruolo candidato:** PRIMARY

Quando il cliente esce dalla situazione per cui il brand è significativo, la fase successiva va valutata come nuova decisione strategica: offerta distinta, contesto distinto o brand distinto possono essere preferibili all'estensione automatica.

### Casa specialistica futura

`02_posizionamento/estensioni-di-linea-e-architettura-brand.md`.

---

## MRC-051 — Nei rapporti brevi, progettare bene i momenti di picco

**Tipo:** DECISION_RULE / FEEDBACK_LOOP  
**Ruolo candidato:** SUPPORTING

Momenti ad alto valore emotivo o pratico possono aumentare valore percepito, ricordo, referral e reputazione anche quando la relazione è naturalmente breve.

### Caveat

Non significa monetizzare artificialmente ogni momento emotivo; il picco deve rafforzare risultato ed esperienza.

---

# G. Ricerca di mercato e Voice of Customer: ciò che la sezione già fornisce

## MRC-052 — Evidenza mercato da comportamento reale, non solo dichiarazioni

**Tipo:** PRINCIPLE / PROCEDURE  
**Ruolo candidato:** PRIMARY

La sezione fornisce già più sorgenti di evidenza:

- clienti migliori e peggiori;
- margine, frequenza, recency, LTV e cost-to-serve;
- alternative attuali e storia di acquisto;
- soddisfazione e volontà di cambiare;
- linguaggio/dialogo mentale quando osservabile;
- capacità di acquisto;
- risultati ottenuti e capacità di implementazione;
- dimensione, raggiungibilità e trend della domanda.

### Il lettore deve saper fare

Correggere la propria ipotesi di target con comportamento ed economia osservati.

---

## MRC-053 — La sezione mercato non contiene ancora un processo VoC completo

**Tipo:** CAVEAT / GAP  
**Ruolo candidato:** REFERENCE

I segnali necessari esistono, ma sono distribuiti. Questa sezione non fornisce da sola una procedura completa per pianificare interviste, estrarre linguaggio, confrontare fonti, distinguere frequenza da salienza e sintetizzare insight in messaggio/offerta.

### Collegamento gap

G-005 resta aperto e va trattato come **IN SYNTHESIS** durante la Fase 2.

---

# H. Cross-section deduplication notes

## Concetti che da qui assumono casa primaria candidata

- `FND-025 — mercato e cliente prima della campagna` → specificato da MRC-001…MRC-008, MRC-023…MRC-033;
- `FND-049 — database → mercato/offerta` → concretizzato da MRC-015, MRC-032, MRC-035, MRC-052;
- `FND-042 — set minimo di economics` → applicazione specifica al cliente in MRC-024, MRC-025, MRC-047;
- `FND-034 — awareness/directness` → applicazione al target in MRC-017…MRC-020.

## Concetti che restano specialistici altrove

- livelli canonici di awareness → `04_marketing`;
- prezzo premium → `03_offerta`;
- proof/social proof → `08_brand`;
- estensioni di linea → `02_posizionamento`;
- CAC/LTV/payback completi → `09_business`;
- follow-up/prequalifica/decisori → `06_vendita`.

---

# I. Coverage file

| File | Stato | Note |
|---|---|---|
| `README.md` | COVERED | routing/reference, nessuna nuova unità autonoma |
| `clienti-identificabili-e-target.md` | COVERED | target, stato decisionale, scadenza naturale, payer/user, Clientikit |
| `appropriatezza-clienti.md` | COVERED | economics cliente, RFM, whale curve, acceptance criteria, Proof by Refusal |
| `clienti-altospendenti.md` | COVERED | capacità vs propensione, premium segment, network, value ladder |
| `quattro-domande-prima-di-lanciare.md` | COVERED | demand/reachability/purchasing power/trend e gate pre-lancio |

## Esito sezione

- **5/5 file covered**;
- **53 unità semantiche MRC-001…MRC-053**;
- nessun file escluso;
- nessun nuovo doctrinal gap certo emerso;
- G-005 confermato come gap editoriale in sintesi;
- G-006 rafforzato: economics minimi sono prerequisito anche della selezione mercato/cliente.
