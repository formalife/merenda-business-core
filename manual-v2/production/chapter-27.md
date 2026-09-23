# Capitolo 27 — Capacità e colli di bottiglia

Il Capitolo 26 ha mostrato che una crescita economicamente valida può richiedere cassa prima di produrne. Anche quando quel fabbisogno è finanziato, rimane un secondo limite: **la quantità di lavoro che il sistema riesce davvero a completare nel tempo disponibile**.

La capacità riguarda persone, macchine, spazi, mezzi, slot, sistemi e infrastrutture che trasformano domanda in lavoro completato. Non coincide con il numero di ore teoricamente presenti in calendario e non si misura soltanto contando quante risorse possiede l'impresa. Una struttura può avere molto personale e poca capacità utile se una fase critica rallenta tutto il flusso; può invece crescere senza aggiungere struttura se libera tempo, riduce rilavorazioni o accede a capacità esterna nei punti giusti.

Il tema diventa particolarmente importante quando aumenta la domanda. Finché il volume è basso, inefficienze e dipendenze possono restare nascoste. Quando il carico cresce, compaiono attese, arretrati, straordinari, ritardi, qualità instabile e promesse commerciali sempre più difficili da rispettare. In queste condizioni aggiungere clienti può peggiorare il risultato anche se ogni cliente, preso singolarmente, sembra profittevole.

Per governare la capacità servono cinque passaggi. Prima occorre distinguere la capacità teorica da quella realmente utilizzabile. Poi bisogna capire che cosa accade quando l'utilizzo si avvicina ai limiti e la variabilità crea code. A quel punto diventa possibile identificare il vero collo di bottiglia, valutare il costo opportunità della risorsa scarsa e decidere infine se conviene costruire nuova capacità, comprarla o accedervi senza possederla.

Il principio che attraversa il capitolo è semplice: **la capacità va letta come una proprietà del sistema, non come la somma delle ore occupate nei singoli reparti**. Il risultato economico dipende dal lavoro completato e consegnato, non dal fatto che ogni risorsa appaia sempre satura.

## 27.1 Capacità disponibile e capacità utile

La capacità teorica è il massimo che una risorsa potrebbe produrre in condizioni ideali. La capacità pratica è ciò che può essere ragionevolmente usato tenendo conto di manutenzione, setup, pause, formazione, variazioni normali, attività amministrative, assenze e altri vincoli inevitabili. Per prendere decisioni operative è quasi sempre la seconda misura a essere utile.

Una macchina disponibile otto ore al giorno non produce necessariamente otto ore di output. Un consulente con quaranta ore contrattuali non può dedicarle tutte ai clienti se deve preparare il lavoro, documentarlo, partecipare a riunioni e gestire eccezioni. Una sala operatoria, una linea di confezionamento o un team di installazione hanno analoghi tempi non direttamente produttivi. Ignorare questi elementi rende la capacità più grande sulla carta di quanto sia nella realtà.

La misura di base è l'utilizzo della capacità pratica:

**utilizzo = capacità effettivamente usata / capacità pratica disponibile.**

La formula è un indicatore operativo, non una legge secondo cui un valore più alto sia sempre migliore. Prima di calcolarla bisogna definire l'unità corretta. In alcuni contesti sarà l'ora di un tecnico, in altri il numero di appuntamenti, le ore macchina, i metri quadrati di magazzino, le consegne giornaliere o i posti disponibili. La stessa impresa può avere più unità di capacità, ma la decisione richiede di identificare quella pertinente al flusso che si sta studiando.

Supponiamo che un team disponga di 200 ore settimanali nominali. Dopo aver considerato attività obbligatorie non erogative, manutenzione del sistema, riunioni indispensabili e una normale quota di variabilità, la capacità pratica scende a 160 ore. Se in una settimana vengono realmente assorbite 136 ore da lavori pertinenti, l'utilizzo non è 136/200, ma 136/160, cioè l'85%. Il primo denominatore descrive l'organico; il secondo descrive meglio la capacità su cui il management può realmente contare.

Questa distinzione diventa ancora più importante nei servizi, dove una parte del lavoro non è visibile al cliente. Un'ora di consulenza può richiedere preparazione, follow-up e registrazione. Un intervento tecnico può includere viaggio, caricamento, controllo e chiusura. Misurare soltanto il tempo in presenza del cliente può far apparire disponibile una capacità che è già assorbita da attività necessarie all'erogazione.

Oltre all'utilizzo serve osservare il **throughput**, cioè il numero di unità, lavori o clienti effettivamente completati in un periodo:

**throughput = lavori completati / periodo di tempo.**

Il throughput protegge da un errore comune: confondere lavoro iniziato con lavoro prodotto. Se un reparto apre cento pratiche e ne completa sessanta, il sistema non ha prodotto cento unità. Le quaranta rimanenti sono lavoro in corso che occupa spazio, attenzione, capitale o tempo futuro. In molti sistemi aumentare il numero di attività avviate senza aumentare il throughput peggiora semplicemente la coda.

La capacità utile deve quindi essere collegata al risultato finale. Una risorsa può essere molto occupata e contribuire poco al flusso se produce lavoro che attende altrove, genera rilavorazioni o alimenta una fase già satura. Al contrario, una piccola quota di capacità libera può avere valore perché assorbe urgenze, variazioni e picchi senza trasformarli subito in ritardi.

### ERRORE FREQUENTE — Trattare la capacità teorica come capacità vendibile

Se il commerciale promette ogni ora nominale del calendario, il sistema finisce per impegnare anche il tempo necessario a gestire setup, imprevisti, qualità e coordinamento. Il problema emerge in ritardo: prima sotto forma di straordinari e recuperi informali, poi come code e consegne mancate.

La correzione non consiste nel gonfiare arbitrariamente un «buffer». Serve misurare quanta capacità viene realmente persa o assorbita dalle attività inevitabili e usare quella evidenza per definire la capacità pratica. Solo da lì ha senso decidere quanto volume aggiuntivo è realmente vendibile.

## 27.2 Utilizzo, code e picchi

In un sistema perfettamente uniforme, con domanda costante e tempi identici, avvicinarsi al 100% di utilizzo sarebbe relativamente semplice da gestire. Le imprese reali funzionano diversamente. Gli arrivi variano, alcune attività durano più del previsto, una macchina si ferma, un cliente rimanda, un fornitore consegna tardi, una pratica richiede una verifica supplementare. Quando la capacità libera è quasi nulla, queste variazioni non vengono assorbite: diventano coda.

Per questo un utilizzo molto alto non è automaticamente sinonimo di efficienza. In un servizio con domanda variabile, saturare ogni agenda può aumentare i tempi di attesa più velocemente di quanto aumenti il lavoro completato. In produzione può accumulare semilavorati davanti alla fase più lenta. In assistenza può trasformare ogni urgenza in un'interruzione di altri lavori, allungando ulteriormente le scadenze.

La coda è informazione. Può essere espressa come numero di ordini in attesa, ticket non chiusi, progetti aperti, giorni prima del primo slot disponibile o valore del lavoro in corso. Una coda che cresce stabilmente indica che, su quell'orizzonte, il carico in entrata supera la capacità di completamento del sistema. Se oscilla ma torna normalmente a livelli bassi, può invece riflettere picchi temporanei assorbiti da una capacità adeguata.

Il problema non si risolve misurando soltanto la media. Un'azienda può avere domanda media di ottanta unità al giorno e capacità pratica di cento, ma ricevere centotrenta ordini il lunedì e sessanta negli altri giorni. La media suggerisce molto margine; l'esperienza del cliente del lunedì può raccontare il contrario. Capacità e domanda devono quindi essere lette anche nella loro distribuzione nel tempo: giorno, settimana, mese, stagione o fascia oraria, a seconda del modello.

I picchi possono essere gestiti in modi diversi. In alcuni casi conviene creare flessibilità di orario o capacità temporanea. In altri è possibile spostare la domanda con prenotazioni, finestre di consegna, prezzi, incentivi o priorità. A volte la soluzione è ridurre la variabilità interna: standardizzare una preparazione, eliminare rilavorazioni o separare casi semplici e complessi. Non esiste una risposta unica perché la natura del picco determina la leva utile.

Anche la capacità libera ha quindi un valore economico. Non significa mantenere persone o macchine inattive senza ragione. Significa riconoscere che una quota di margine operativo può proteggere velocità, affidabilità e qualità quando la domanda e i tempi non sono perfettamente prevedibili. La capacità in eccesso è costosa; la saturazione totale può esserlo altrettanto attraverso ritardi, straordinari, errori e opportunità perse.

### ESEMPIO NUMERICO — Perché il 100% di utilizzo può peggiorare il servizio

Consideriamo un team che ha una capacità pratica di 100 ore a settimana. In condizioni normali riceve lavoro per circa 85 ore e riesce a completarlo nello stesso periodo. Le 15 ore residue assorbono variazioni, richieste urgenti e attività che occasionalmente durano più del previsto.

Il management decide di «eliminare l'inefficienza» e vende sistematicamente 100 ore di lavoro ogni settimana. Se i tempi effettivi restassero identici alle stime, il sistema potrebbe reggere. Basta però che una settimana richieda 108 ore perché 8 ore passino alla settimana successiva. Se quella successiva è già venduta per 100 ore, la coda diventa 8 ore prima ancora di ricevere un nuovo imprevisto.

Dopo quattro settimane con piccoli scostamenti, il team può trovarsi con decine di ore arretrate pur avendo un utilizzo apparentemente eccellente. Il dato che conta non è soltanto quante ore sono state occupate, ma se il throughput, i tempi di consegna e la qualità sono rimasti coerenti con la promessa al cliente.

La conclusione non è fissare un utilizzo massimo universale. La quota di capacità da lasciare libera dipende da variabilità, possibilità di spostare la domanda, costo del ritardo e facilità di aggiungere capacità in modo temporaneo. Il controllo corretto collega utilizzo, coda, lead time e throughput.

### IN PRATICA — Seguire insieme carico, coda e tempo di attraversamento

Per la fase operativa più importante, osserva nello stesso cruscotto almeno quattro misure: carico in entrata, capacità pratica, lavoro in coda e lavoro completato. Se il carico cresce ma il throughput non cambia, la crescita sta entrando nel sistema più rapidamente di quanto il sistema riesca a trasformarla in risultato.

Aggiungi il tempo medio o mediano di attraversamento quando è rilevante. Una coda può rimanere numericamente stabile ma diventare più lenta se aumenta la complessità dei casi. Il numero di lavori aperti e il tempo necessario a chiuderli raccontano due aspetti diversi dello stesso vincolo.

## 27.3 Il collo di bottiglia

Un collo di bottiglia è la risorsa, la fase o la regola che limita il throughput dell'intero sistema nel periodo considerato. Non è necessariamente il reparto più costoso, quello con più persone o quello che si lamenta di più. È il punto oltre il quale il sistema non riesce a far passare più risultato senza modificare quel vincolo o il modo in cui viene utilizzato.

Il segnale più evidente è spesso una coda persistente davanti a una fase e capacità inutilizzata o intermittente subito dopo. Immaginiamo un processo con tre fasi che possono completare rispettivamente 12, 8 e 11 unità all'ora. Se la domanda è sufficiente, la seconda fase limita il flusso a circa 8 unità l'ora. Far lavorare la prima fase più velocemente non aumenta il throughput finale: crea soltanto più lavoro in attesa davanti alla seconda.

Questo esempio mostra perché l'ottimizzazione locale può peggiorare il sistema. Un responsabile della prima fase può vantare più produttività perché produce dodici unità l'ora, ma quattro di quelle unità ogni ora si accumulano in coda. Il costo può apparire come spazio, scorte, coordinamento, rischio di errore o lead time. La prestazione locale è migliorata; il risultato complessivo no.

Per identificare il vincolo conviene seguire il flusso reale e non partire dall'organigramma. Dove si accumula lavoro? Quale fase è costantemente piena? Quale risorsa, se perdesse un'ora, ridurrebbe direttamente il numero di unità completate? Quale fase, se guadagnasse capacità, permetterebbe davvero al sistema di produrre di più? Queste domande aiutano a distinguere un collo di bottiglia da una semplice inefficienza.

Una volta individuato il vincolo, la prima leva non è sempre comprare nuova capacità. Occorre prima proteggere la capacità già esistente. Se una risorsa critica perde tempo in attività che potrebbero essere svolte altrove, in attese evitabili, cambi di priorità continui o rilavorazioni, parte del collo di bottiglia è auto-creata. Liberare un'ora della risorsa vincolante può valere più che liberarne dieci in una fase con capacità abbondante.

Questo cambia anche le priorità organizzative. Le attività a monte dovrebbero alimentare il vincolo con il lavoro corretto, nella sequenza corretta e con gli input necessari. Le attività a valle dovrebbero essere pronte a riceverne l'output. Se il vincolo resta fermo perché manca un materiale, un'autorizzazione o un'informazione che poteva essere preparata prima, il sistema perde capacità che non può recuperare semplicemente facendo correre più velocemente altre persone.

Il collo di bottiglia non è necessariamente permanente. Se viene elevata la capacità della fase più lenta, il vincolo può spostarsi. Anche un cambiamento nel mix di prodotti, nella domanda o nei requisiti di qualità può creare un nuovo limite. Per questo la diagnosi va ripetuta dopo ogni intervento importante: **un sistema senza vincoli non esiste; cambia il punto che limita il risultato**.

La stessa logica vale per risorse meno visibili. Un fondatore che deve approvare ogni preventivo, un unico tecnico capace di risolvere i casi complessi, una sala con pochi slot o un software che consente soltanto un certo numero di elaborazioni possono tutti diventare vincoli. Il criterio non è se la risorsa sia umana o tecnica, ma se la sua capacità limita il flusso economicamente utile.

### ERRORE FREQUENTE — Aggiungere capacità dove è più facile invece che dove serve

Quando un reparto è sotto pressione, la risposta intuitiva è spesso assumere persone nella funzione che appare più occupata o comprare l'attrezzatura che crea più fastidio operativo. Se quella funzione non limita il throughput, il costo fisso aumenta senza migliorare il risultato finale.

Prima di aggiungere struttura, verifica quale fase sta realmente limitando il flusso e se la capacità esistente del vincolo viene usata per il lavoro a più alto valore. La domanda corretta non è «dove siamo più impegnati?», ma «dove un'unità aggiuntiva di capacità cambierebbe davvero il numero di lavori completati o il valore prodotto?».

## 27.4 Costo opportunità della capacità

Quando una risorsa non è scarsa, molte decisioni possono essere prese guardando la contribuzione totale del cliente, del prodotto o del progetto. Quando quella risorsa diventa il vincolo, il criterio cambia: due lavori con lo stesso margine possono avere valore molto diverso se consumano quantità differenti della capacità che limita il sistema.

Una misura utile è la contribuzione per unità di capacità vincolante:

**contribuzione per unità vincolante = margine di contribuzione / unità di capacità scarsa consumate.**

L'unità può essere un'ora di tecnico, un'ora macchina, uno slot di consulenza, un posto in magazzino, una tratta di consegna o qualunque risorsa che stia realmente limitando il flusso. La misura è utile solo se quella capacità è davvero il vincolo. Applicarla a una risorsa abbondante produce una precisione apparente senza valore decisionale.

Consideriamo due tipi di progetto. Il progetto A lascia 5.000 euro di contribuzione e richiede 50 ore della risorsa vincolante. Il progetto B lascia 3.600 euro ma richiede soltanto 20 ore della stessa risorsa. Il primo genera più contribuzione per progetto; il secondo genera più contribuzione per ora vincolante:

- progetto A: 5.000 / 50 = **100 euro per ora vincolante**;
- progetto B: 3.600 / 20 = **180 euro per ora vincolante**.

Se la domanda supera la capacità e le altre condizioni sono comparabili, riempire il vincolo con progetti A può produrre meno contribuzione totale nel mese rispetto a un mix che usa più progetti B. Il prezzo o il fatturato del singolo lavoro non bastano quindi a definire la priorità quando la capacità scarsa è il vero limite.

Da qui nasce il costo opportunità della capacità: usare una risorsa scarsa per un'attività significa rinunciare alla migliore alternativa realistica che quella stessa risorsa avrebbe potuto servire. In forma gestionale, il costo opportunità può essere stimato come la contribuzione della migliore alternativa fattibile che viene spostata o rifiutata.

Non si tratta di un costo contabile osservato in fattura. È una stima per decidere. Se un'ora del collo di bottiglia può generare 180 euro di contribuzione con il miglior lavoro disponibile, usarla per un lavoro che ne genera 70 ha un costo economico anche se quel lavoro resta positivo in termini assoluti. In periodi di capacità abbondante lo stesso progetto potrebbe invece essere perfettamente razionale, perché non sposterebbe nessuna alternativa migliore.

Questa logica evita anche un errore nei clienti «grandi». Un cliente può generare ricavi elevati e assorbire una quota sproporzionata di progettazione, assistenza, personalizzazione o gestione. Se quella attività usa la capacità che limita la crescita, il cliente deve essere valutato anche per contribuzione per unità vincolante. Il fatturato da solo può nascondere il vero costo di opportunità.

La capacità scarsa può essere gestita non soltanto scegliendo cosa accettare. Può cambiare il prezzo, la priorità, il livello di servizio o la finestra temporale. Un lavoro urgente che occupa il collo di bottiglia in un momento di saturazione ha un costo diverso dallo stesso lavoro eseguito in una settimana con capacità libera. La politica commerciale può quindi aiutare a distribuire la domanda e a far pagare, quando il mercato lo consente, il consumo di capacità particolarmente preziosa.

### ESEMPIO SVOLTO — Scegliere il mix quando le ore critiche sono limitate

Supponiamo che un'impresa disponga di 160 ore mensili della risorsa che rappresenta il collo di bottiglia. Può servire due famiglie di lavori:

| Dato | Lavoro A | Lavoro B |
| --- | ---: | ---: |
| Contribuzione per lavoro | €5.000 | €3.600 |
| Ore della risorsa vincolante | 50 | 20 |
| Contribuzione per ora vincolante | €100 | €180 |

Se l'impresa accetta tre lavori A, usa 150 ore e genera 15.000 euro di contribuzione. Se dispone di sufficiente domanda per il lavoro B, otto lavori B usano le stesse 160 ore e generano 28.800 euro di contribuzione.

Questo non dimostra che il lavoro B sia «migliore» in assoluto. Potrebbero esistere differenze di rischio, domanda, tempi di pagamento, qualità strategica del cliente o uso di altre risorse. Dimostra che, **quando quelle 160 ore sono il vincolo**, la contribuzione per ora critica diventa una misura necessaria per costruire il mix.

Se il vincolo viene eliminato e le ore diventano abbondanti, la priorità può cambiare. La misura va quindi collegata alla condizione che la rende utile, non trasformata in una classifica permanente dei prodotti.

## 27.5 Costruire, comprare o accedere alla capacità

Quando il vincolo è stato verificato e la domanda economicamente valida supera in modo persistente la capacità, l'impresa deve decidere come aumentarla. La risposta più costosa consiste nel comprare immediatamente asset fissi: assumere, aprire spazi, acquistare macchine o costruire infrastrutture. A volte è la scelta corretta, ma dovrebbe competere con alternative più flessibili.

La prima opzione è **costruire capacità interna**. Significa assumere e formare persone, acquistare macchine, ampliare spazi o creare un reparto. Questa scelta aumenta controllo e può ridurre il costo unitario quando il volume è stabile e sufficiente. In cambio richiede capitale, tempo di implementazione e un impegno che continua anche quando la domanda scende. La nuova struttura aumenta inoltre il punto di pareggio e deve essere sostenuta economicamente dopo il picco che ha motivato l'investimento.

La seconda opzione è **comprare capacità come servizio**. Outsourcing, subfornitura, lavoro specialistico esterno, cloud, logistica terza o altre forme contrattuali permettono di trasformare parte del costo fisso in costo variabile. L'impresa guadagna flessibilità, ma rinuncia a una quota di controllo e deve governare qualità, tempi, sicurezza, dati, responsabilità e dipendenza dal fornitore.

La terza opzione è **accedere a capacità che esiste già senza possederla**. Una partnership può rendere utilizzabile personale, macchine, mezzi, spazi, distribuzione o infrastrutture che un'altra organizzazione non sfrutta completamente. L'obiettivo non è necessariamente acquistare una prestazione standardizzata; può essere costruire un accordo che garantisca accesso alla capacità quando serve, con priorità, standard e condizioni definite.

Questa possibilità cambia la domanda d'investimento. Prima di chiedersi quanto costa possedere una nuova risorsa, conviene chiedersi se l'impresa ha davvero bisogno della proprietà o soltanto del controllo affidabile dell'output. In molti casi il vantaggio economico nasce dalla disponibilità della capacità, non dal titolo di proprietà dell'asset.

L'accesso esterno non è però capacità gratuita. Introduce rischi di disponibilità, qualità, responsabilità, riservatezza e reputazione. Un partner che ha capacità oggi potrebbe non averla nel picco successivo; una subfornitura di bassa qualità può danneggiare il marchio dell'impresa che ha venduto la promessa al cliente. Gli accordi devono quindi definire almeno standard, volumi, tempi, controllo, escalation e condizioni di continuità.

Prima di scegliere fra costruire, comprare o accedere, è utile verificare anche se il vincolo può essere ridotto senza aggiungere capacità. Eliminare lavoro inutile, trasferire attività semplici fuori dalla risorsa critica, standardizzare input, ridurre rilavorazioni, migliorare programmazione e spostare domanda fuori dai picchi possono liberare output a costo inferiore. Aggiungere capacità a un processo che spreca il vincolo rende più grande lo spreco.

La scelta dovrebbe confrontare almeno cinque dimensioni: costo totale, velocità di attivazione, reversibilità, controllo e rischio di continuità. Un asset interno può essere più conveniente su un orizzonte lungo ma troppo lento per un picco imminente. Un fornitore esterno può essere perfetto per validare la domanda, ma troppo fragile se quella capacità diventa strategica e non sostituibile. Un accordo di accesso può offrire flessibilità, ma richiedere governance più rigorosa di un semplice acquisto.

Esiste infine una conseguenza strategica. Se l'impresa impara a orchestrare in modo affidabile una rete di capacità esterna, quell'accesso può diventare un asset. Invece di possedere tutte le risorse necessarie, controlla un sistema che le rende disponibili. Ma questa leva esiste soltanto dopo aver provato che qualità, tempi e responsabilità sono governabili; trasformare una dipendenza non controllata in una promessa commerciale amplifica il rischio anziché creare scalabilità.

### IN PRATICA — Testare l'accesso prima del capex irreversibile

Se la domanda aggiuntiva è recente o ancora incerta, prova prima a coprire una parte del picco con capacità temporanea o esterna, mantenendo gli stessi standard di qualità e misurando costo, lead time, errori e margine. Il test produce due informazioni: se la domanda è abbastanza stabile da meritare nuova struttura e se l'accesso esterno è una soluzione sostenibile anche oltre il test.

Questo approccio non vieta l'investimento interno. Riduce il rischio di costruire capacità permanente sulla base di un picco temporaneo o di un forecast ancora debole.

### STRUMENTO OPERATIVO — Scheda capacità e collo di bottiglia

| Campo | Che cosa registrare |
| --- | --- |
| Flusso osservato | Processo, linea, servizio o percorso operativo da analizzare |
| Unità di output | Lavoro, cliente, ordine, intervento o altra unità completata |
| Periodo | Giorno, settimana, mese o altro intervallo coerente con il flusso |
| Capacità teorica | Massimo nominale prima di pause, setup, manutenzione e variabilità |
| Capacità pratica | Capacità realisticamente disponibile nel periodo |
| Carico in entrata | Domanda o lavoro che entra nel sistema nel periodo |
| Utilizzo | Capacità usata / capacità pratica disponibile |
| Throughput | Unità effettivamente completate nel periodo |
| Coda / WIP | Lavoro in attesa o in corso non ancora completato |
| Tempo di attraversamento | Tempo dalla presa in carico al completamento o consegna |
| Picco rilevante | Giorno, fascia o stagione in cui il carico supera la media |
| Fase vincolante | Risorsa, fase o regola che limita il throughput corrente |
| Unità della capacità scarsa | Ora tecnica, ora macchina, slot, spazio, tratta o altra unità pertinente |
| Perdita evitabile sul vincolo | Attese, rilavorazioni, setup, attività trasferibili o interruzioni |
| Contribuzione per unità vincolante | Margine di contribuzione / unità di capacità scarsa consumate |
| Migliore alternativa spostata | Lavoro economicamente migliore che la capacità occupata impedisce di servire |
| Costo opportunità stimato | Contribuzione della migliore alternativa fattibile rinunciata |
| Leva senza nuova capacità | Riduzione carico, standardizzazione, programmazione, pricing o trasferimento attività |
| Opzione build | Investimento, tempo di attivazione, costi fissi, controllo e capacità aggiunta |
| Opzione buy | Fornitore/outsourcing, costo variabile, SLA, qualità e dipendenze |
| Opzione access | Partnership/piattaforma/rete, disponibilità, priorità e regole di controllo |
| Rischio di continuità | Single point of failure, sostituibilità e piano alternativo |
| Metrica primaria | Throughput, lead time, contribuzione, qualità o altra misura da migliorare |
| Condizione di revisione | Quando elevare il vincolo, cambiare mix, aggiungere capacità o fermare l'investimento |

La scheda serve a evitare che la decisione sulla capacità parta direttamente da una richiesta di assunzione o da un preventivo per un nuovo asset. Prima rende visibile il flusso, poi verifica il vincolo, quindi confronta il valore della capacità aggiuntiva con le alternative disponibili.

### VERIFICA NELLA TUA AZIENDA — Dove si ferma oggi il flusso?

Scegli un percorso operativo che incide direttamente su ricavi, esperienza del cliente o margine e ricostruiscilo su un periodo recente sufficientemente rappresentativo.

1. Definisci l'unità di output e misura quante unità vengono davvero completate nel periodo. Non usare soltanto lavoro aperto, ore registrate o attività iniziate.
2. Per le fasi principali stima la capacità pratica, non quella nominale. Esplicita quali tempi rendono indisponibile una parte della capacità teorica.
3. Confronta carico, capacità, coda e tempo di attraversamento. Individua il punto in cui il lavoro si accumula in modo persistente o da cui dipende direttamente il throughput finale.
4. Sul vincolo, misura quanta capacità viene persa in attese, rilavorazioni, setup, attività trasferibili o interruzioni. Prova prima a recuperare quella capacità.
5. Se la domanda supera ancora il vincolo, calcola la contribuzione per unità di capacità scarsa dei principali tipi di lavoro. Verifica se il mix attuale usa la risorsa critica per le opportunità economicamente migliori.
6. Costruisci almeno tre opzioni: capacità interna, acquisto esterno e accesso tramite partner o infrastruttura già esistente. Confronta costo totale, tempo, reversibilità, qualità e rischio di continuità.
7. Definisci una metrica e una condizione di revisione. Se l'intervento non aumenta throughput o non riduce la coda senza peggiorare qualità e margine, non ha risolto il vincolo che dichiarava di affrontare.

L'output utile è una mappa nella quale domanda, capacità pratica, coda, vincolo e valore economico della risorsa scarsa sono collegati. A quel punto l'impresa può distinguere una vera necessità di nuova capacità da una saturazione creata da priorità, variabilità o processo.

Una volta localizzato il vincolo, la domanda successiva è come rendere il lavoro più ripetibile senza irrigidire ciò che richiede giudizio. Il Capitolo 28 entrerà nei processi, nei controlli e nell'automazione: strumenti che producono leva solo dopo che il flusso da governare è stato definito.
