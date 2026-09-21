# Capitolo 25 — Economia del cliente

Acquisire un cliente ha un costo. Servirlo ne ha un altro. Il valore economico che la relazione genera arriva nel tempo e dipende da più variabili: prezzo, margine, frequenza di acquisto, durata della relazione, costi di assistenza, resi, personalizzazioni, sconti, tempi di incasso e molte altre caratteristiche del modello di business.

Per questo il fatturato non basta a descrivere quanto vale un cliente. Anche il costo di acquisizione, preso da solo, è insufficiente. Due clienti possono costare entrambi 1.800 euro da acquisire e produrre risultati molto diversi perché uno attiva rapidamente, usa il servizio in modo standard e rimane a lungo, mentre l'altro richiede molto supporto, genera più eccezioni o abbandona presto.

L'economia del cliente studia questa relazione in modo più completo. Il suo obiettivo non è attribuire a ogni persona un valore perfettamente preciso, cosa che spesso sarebbe impossibile, ma capire se l'acquisizione di determinati clienti crea abbastanza contribuzione, in tempi compatibili con la cassa e con un livello di incertezza accettabile.

In questo capitolo useremo sei strumenti collegati. Le **unit economics** descrivono l'economia fondamentale della singola unità di vendita o relazione. L'**analisi per coorti** permette di confrontare gruppi di clienti nel tempo senza nascondere differenze importanti dentro una media. Il **lifetime value** stima il valore economico atteso della relazione. Il **payback** misura quanto tempo occorre per recuperare il costo di acquisizione. Il **costo massimo di acquisizione** traduce l'economia del cliente in una soglia decisionale specifica per l'impresa. Il **costo marginale di acquisizione**, infine, serve a capire se il prossimo incremento di spesa mantiene ancora un'economia accettabile.

Questi strumenti vanno letti insieme. Nessun rapporto sintetico sostituisce il giudizio sul modello del business, sul tempo necessario a recuperare il denaro e sulla qualità delle ipotesi utilizzate.

## 25.1 Unit economics

Le unit economics partono da una domanda semplice: quanto valore economico produce l'unità fondamentale che stiamo vendendo?

L'unità può essere un ordine, un cliente, un abbonamento, un progetto, una camera occupata, una consegna o qualsiasi altra grandezza abbia senso nel modello specifico. La scelta dell'unità è importante perché i numeri devono essere collegati a una decisione reale. In un ecommerce può essere utile analizzare il singolo ordine e poi la relazione complessiva con il cliente. In un software in abbonamento, invece, il cliente o l'account è spesso l'unità più utile.

Il primo passaggio consiste nel separare i ricavi da ciò che rimane dopo i costi che variano direttamente con la vendita o con l'erogazione. Questa differenza è il **margine di contribuzione**.

> **Margine di contribuzione = ricavi − costi variabili attribuibili**

Se un servizio fattura 480 euro al mese e richiede mediamente 120 euro di infrastruttura, assistenza e altri costi variabili direttamente legati all'account, il margine di contribuzione mensile è 360 euro.

Quel valore non è ancora profitto. Deve contribuire a recuperare i costi di acquisizione, sostenere la struttura, finanziare investimenti e, solo dopo, generare utile per l'impresa. La distinzione è importante perché un cliente può produrre molto fatturato e lasciare poca contribuzione se richiede un livello elevato di servizio o di personalizzazione.

Il secondo elemento fondamentale è il **costo di acquisizione cliente**, spesso indicato con la sigla CAC (*customer acquisition cost*). Per essere utile nelle decisioni, il CAC deve includere il perimetro di costi realmente necessario per portare un nuovo cliente fino all'acquisto.

> **CAC = costi attribuibili di acquisizione e vendita / nuovi clienti acquisiti**

Il numeratore può comprendere pubblicità, produzione delle campagne, agenzie, strumenti, materiali, eventi, tempo commerciale, commissioni e altre risorse direttamente utilizzate per trasformare opportunità in clienti. Il perimetro preciso varia da impresa a impresa, ma deve essere dichiarato e abbastanza completo da rendere sensato il confronto.

Un costo per lead basso non implica automaticamente un CAC basso. Un canale può produrre contatti economici e, nello stesso tempo, richiedere molte ore di vendita per arrivare al contratto. Un altro canale può generare meno lead, apparentemente più costosi, ma portare persone già informate e più semplici da convertire. Se si misura soltanto il costo iniziale della pubblicità, la differenza resta nascosta.

> **ESEMPIO NUMERICO — Economia elementare di un account**
>
> Supponiamo che un software in abbonamento abbia:
>
> - prezzo mensile: **€480**;
> - costi variabili mensili attribuibili all'account: **€120**;
> - contribuzione mensile: **€360**;
> - CAC completo: **€1.800**.
>
> La prima fattura da €480 non recupera il costo sostenuto per acquisire il cliente. Anche dopo aver sottratto i costi variabili, i €360 di contribuzione del primo mese coprono soltanto una parte dei €1.800 investiti nell'acquisizione. Il resto dovrà essere recuperato attraverso la contribuzione dei mesi successivi.

L'esempio introduce già una seconda dimensione del problema: il tempo. Prima di affrontarla, però, dobbiamo capire perché la media di questi valori può essere ingannevole.

## 25.2 Analisi per coorti

Una **coorte** è un gruppo di clienti che condivide una caratteristica utile all'analisi e viene osservato nel tempo. La caratteristica può essere il mese di acquisizione, il canale, il segmento, la versione dell'offerta, il venditore, il tipo di onboarding o un'altra variabile che possa influenzare l'economia della relazione.

L'analisi per coorti serve soprattutto a evitare che una media nasconda gruppi molto diversi. Un CAC medio di 1.800 euro può sembrare stabile mentre alcuni segmenti costano 1.200 euro e altri 2.500. Due canali possono avere lo stesso costo per cliente ma produrre comportamenti di retention differenti. Due gruppi con lo stesso prezzo possono richiedere livelli di assistenza molto diversi.

La divisione in coorti non deve diventare un esercizio di segmentazione infinita. Ha senso separare i gruppi quando la distinzione può cambiare una decisione: quanto spendere, quale segmento servire, quale onboarding usare, quale prezzo applicare o quale parte del prodotto modificare.

Consideriamo ora due coorti di cento clienti ciascuna, acquisite allo stesso costo.

> **ESEMPIO SVOLTO — Due coorti con lo stesso CAC**
>
> Dati comuni:
>
> - 100 nuovi account per coorte;
> - CAC per account: **€1.800**;
> - costo totale di acquisizione per coorte: **€180.000**;
> - prezzo: **€480/mese**;
> - contribuzione normale per account attivo: **€360/mese**.
>
> La Coorte A raggiunge 90 account attivi nel primo mese e richiede €9.000 di lavoro aggiuntivo di onboarding. La Coorte B raggiunge 65 account attivi e richiede €25.000 di onboarding aggiuntivo.
>
> Nel primo mese la Coorte A produce 90 × €360 = €32.400 di contribuzione ricorrente. Sottraendo i €9.000 di onboarding extra restano **€23.400**.
>
> La Coorte B produce 65 × €360 = €23.400; sottraendo €25.000 di onboarding extra, il primo mese chiude a **−€1.600** di contribuzione.

![Figura 25.1 — Due coorti con lo stesso CAC possono avere un punto di partenza economico diverso](figures/figure-25-1-same-cac-different-start.svg)

Il CAC non è sbagliato: entrambe le coorti sono costate 1.800 euro per cliente acquisito. Semplicemente non descrive ciò che accade dopo la vendita. La differenza di attivazione e di lavoro necessario per rendere operativo il cliente cambia l'economia della relazione fin dall'inizio.

Questa osservazione è particolarmente utile quando un'impresa serve segmenti diversi con la stessa offerta. Un segmento può apparire molto attraente per prezzo o dimensione del contratto e rivelarsi meno interessante dopo aver incluso tempi di implementazione, richieste di supporto, personalizzazioni o tasso di abbandono.

La coorte diventa quindi un ponte tra acquisizione e post-vendita. Permette di chiedere non soltanto quanto è costato ottenere il cliente, ma che cosa è successo a quel gruppo dopo l'ingresso.

## 25.3 Lifetime value

Il **lifetime value**, o LTV, cerca di rappresentare il valore economico generato da un cliente durante l'intera relazione con l'impresa.

Per decisioni economiche è più utile ragionare sulla contribuzione che sul fatturato. Parlare di “cliente da 10.000 euro” perché nel corso degli anni ha generato 10.000 euro di ricavi dice poco se 7.000 euro sono stati assorbiti da prodotto, assistenza, logistica o altri costi incrementali.

Una forma generale del concetto è:

> **LTV economico = contribuzione attesa lungo la relazione − costi incrementali futuri non già inclusi**

La formula va interpretata con cautela perché il termine “attesa” contiene quasi tutta la difficoltà. Quando la relazione non è ancora conclusa, una parte del lifetime value è necessariamente una stima. La qualità di quella stima dipende da quantità e stabilità dei dati disponibili.

Se possediamo dodici mesi di comportamento di una coorte, possiamo descrivere con buona precisione la contribuzione osservata in quei dodici mesi. Per stimare i tre anni successivi dobbiamo invece fare ipotesi su retention, prezzi, costi di servizio, espansione degli account, sconti, cambi di prodotto e altri fattori.

È quindi utile distinguere sempre tra:

- **valore osservato in un orizzonte definito**;
- **valore futuro modellato**.

Questa distinzione evita di usare una previsione ottimistica per giustificare oggi costi di acquisizione che le coorti reali non hanno ancora dimostrato di sostenere.

Un indicatore molto diffuso è il rapporto tra LTV e CAC. Può essere utile come sintesi, ma non esiste una soglia universale che valga per ogni business. Due imprese con lo stesso rapporto possono avere tempi di recupero molto diversi, livelli di rischio diversi e disponibilità di cassa completamente differenti.

Per questo il rapporto LTV:CAC dovrebbe essere letto come un segnale riassuntivo, non come un semaforo automatico. Prima di decidere quanto investire servono anche il payback, la qualità delle coorti e la capacità finanziaria dell'impresa.

## 25.4 Payback avanzato

Il **payback** misura il tempo necessario affinché la contribuzione cumulata recuperi il costo sostenuto per acquisire il cliente o la coorte.

Nei modelli molto regolari si può ottenere una stima dividendo il CAC per la contribuzione periodica. Quando però attivazione, churn, costi di onboarding o utilizzo cambiano nel tempo, l'approccio più informativo consiste nel seguire direttamente la contribuzione cumulata della coorte.

Il criterio è:

> **Il payback viene raggiunto nel primo periodo in cui la contribuzione cumulata osservata è almeno pari al costo di acquisizione.**

Torniamo alle due coorti precedenti. Seguendo mese per mese gli account attivi, la Coorte A arriva a una contribuzione cumulata di circa €173.160 al sesto mese e supera i €180.000 di costo di acquisizione nel settimo. La Coorte B, invece, alla fine del dodicesimo mese ha prodotto circa €169.760 e non ha ancora recuperato il costo iniziale.

![Figura 25.2 — Il payback si osserva quando la contribuzione cumulata supera il costo di acquisizione](figures/figure-25-2-cohort-payback.svg)

| Metrica osservata | Coorte A | Coorte B |
|---|---:|---:|
| Nuovi account acquisiti | 100 | 100 |
| CAC per account | €1.800 | €1.800 |
| Account attivati nel mese 1 | 90 | 65 |
| Onboarding extra mese 1 | €9.000 | €25.000 |
| Account attivi nel mese 12 | 69 | 29 |
| Contribuzione cumulata a 12 mesi | €329.760 | €169.760 |
| CAC recuperato entro 12 mesi | Sì | No |
| Payback osservato | Mese 7 | Oltre il mese 12 |

Il payback aggiunge una dimensione che l'LTV, da solo, può nascondere: **quando** il valore arriva.

Questa differenza ha conseguenze finanziarie. Se un'impresa paga oggi per acquisire un cliente e recupera il denaro in sette mesi, deve finanziare sette mesi di distanza. Se il recupero richiede quattordici mesi, la crescita assorbe capitale per un periodo molto più lungo. Due clienti con lo stesso valore finale possono quindi avere un impatto molto diverso sulla cassa.

Nel capitolo successivo analizzeremo in dettaglio il ciclo di cassa. Qui è sufficiente osservare che un buon valore futuro non rende irrilevante il tempo necessario a recuperare l'investimento.

## 25.5 Costo massimo di acquisizione

Dopo aver compreso contribuzione, coorti, LTV e payback, l'impresa può affrontare una domanda più utile del semplice “qual è il nostro CAC?”: **quanto possiamo permetterci di pagare per acquisire un certo tipo di cliente?**

La risposta non arriva da un benchmark universale. Dipende dalla contribuzione che il cliente può generare, dall'orizzonte temporale scelto, dal margine che l'impresa vuole lasciare alla struttura e al profitto, dalla disponibilità di cassa e dal livello di rischio accettabile.

Per questo il costo massimo sostenibile di acquisizione è una **regola decisionale**. Una possibile forma è:

> **CAC massimo sostenibile = contribuzione nell'orizzonte scelto − contribuzione richiesta a struttura/profitto − margine di sicurezza per rischio e cassa**

Le componenti della formula non sono costanti naturali: alcune dipendono da scelte manageriali.

> **ESEMPIO NUMERICO — Costruire una soglia di acquisizione**
>
> La Coorte A dell'esempio precedente ha prodotto nei primi dodici mesi €329.760 di contribuzione complessiva, cioè **€3.297,60 per account acquisito**.
>
> Supponiamo che l'impresa voglia riservare:
>
> - €700 per contribuire a struttura e profitto;
> - €400 come margine di sicurezza per rischio e fabbisogno di cassa.
>
> La soglia diventa:
>
> **€3.297,60 − €700 − €400 = €2.197,60**
>
> In termini operativi, l'impresa potrebbe arrotondare la propria soglia a circa **€2.200** per clienti con economia simile a quella osservata.

Il risultato non significa che 2.200 euro sia un CAC “giusto” in assoluto. Se aumentano i costi di servizio, la soglia scende. Se la contribuzione migliora, può salire. Se l'impresa ha poca cassa o grande incertezza, può decidere di mantenere un margine di sicurezza maggiore.

Questa è la ragione per cui le soglie economiche devono essere costruite sui numeri e sulle condizioni dell'impresa, non copiate da un benchmark esterno.

## 25.6 Costo marginale e leve di crescita

Il CAC storico descrive ciò che l'impresa ha già acquistato. Quando si decide se aumentare la spesa serve invece stimare il **CAC marginale**, cioè il costo dei clienti prodotti dal prossimo incremento di investimento.

> **CAC marginale = spesa incrementale di acquisizione / clienti incrementali prodotti da quella spesa**

Supponiamo che il prossimo blocco di acquisizione richieda 130.000 euro addizionali e sia previsto generare 50 nuovi clienti. Il CAC marginale atteso è:

> **€130.000 / 50 = €2.600**

Se la soglia costruita per quel tipo di cliente è circa €2.200, il nuovo blocco non rispetta le condizioni economiche definite dall'impresa. Questo non obbliga automaticamente a fermare ogni crescita. Indica che, con quelle ipotesi, bisogna modificare qualcosa: costo di acquisizione, conversione, prezzo, onboarding, retention, mix di clienti o dimensione del blocco.

Qui entra in gioco l'**analisi di sensibilità**. Un modello è utile soprattutto quando mostra quali variabili possono cambiare la decisione.

Supponiamo che il prossimo gruppo di clienti richieda 600 euro in più di onboarding e assistenza iniziale per account. A parità di tutto il resto, la contribuzione a dodici mesi scenderebbe da €3.297,60 a circa €2.697,60 per cliente acquisito.

Usando la stessa regola decisionale:

> **€2.697,60 − €700 − €400 = €1.597,60**

A quel punto persino il vecchio CAC medio di €1.800 supererebbe la soglia.

Il costo di acquisizione non è cambiato; è cambiata l'economia del cliente. Questa è una delle ragioni per cui le leve di crescita non possono essere analizzate separatamente. Prezzo, conversione, attivazione, costi di servizio, retention, frequenza e acquisizione interagiscono.

Lo stesso ragionamento vale nei business senza abbonamento. Consideriamo un ecommerce in cui il primo ordine lascia 32 euro di contribuzione prima dell'acquisizione e il CAC è 24 euro. Due gruppi di clienti possono avere la stessa economia del primo ordine ma frequenze di riacquisto molto diverse. Per confrontarli bisogna osservare contribuzione cumulata, tempi degli ordini successivi, costi delle promozioni e capitale immobilizzato nelle scorte. Una formula di churn tipica di un software in abbonamento sarebbe poco adatta; il principio economico, invece, rimane lo stesso.

L'economia del cliente serve quindi a collegare acquisizione e crescita alla realtà della relazione. Il CAC indica quanto abbiamo pagato per ottenere il cliente. La contribuzione indica quanto valore economico rimane mentre lo serviamo. Le coorti mostrano differenze che le medie possono nascondere. L'LTV estende l'analisi lungo la relazione, distinguendo dati osservati e previsioni. Il payback aggiunge il tempo. Il costo massimo di acquisizione trasforma questi elementi in una regola aziendale. Il CAC marginale verifica infine se la crescita successiva mantiene ancora l'economia desiderata.

Resta un problema che questi numeri non risolvono da soli. Un cliente può essere economicamente conveniente e, nello stesso tempo, mettere sotto pressione la cassa se pubblicità, venditori, inventario, onboarding o fornitori vengono pagati molto prima che la contribuzione rientri. Il Capitolo 26 affronta precisamente questo tema: il rapporto tra profitto, capitale circolante e velocità con cui il denaro attraversa l'impresa.
