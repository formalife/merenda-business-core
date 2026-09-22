# Capitolo 16 — Funnel e database

I capitoli precedenti hanno risolto tre problemi diversi. Abbiamo definito quale prova serve perché una promessa sia credibile, distinto gli stati della domanda e valutato come raggiungerli attraverso canali diretti o accessi presi in prestito. A questo punto il problema cambia ancora: **che cosa succede dopo che una persona entra nel sistema?**

Un'impresa può generare traffico, lead, richieste e perfino appuntamenti e perdere comunque gran parte del valore creato se non ricorda chi ha davanti, che cosa è già successo e quale passo abbia senso adesso. Il funnel serve a governare questo movimento. Il database serve a conservarne la memoria.

Questa distinzione è importante perché molti sistemi vengono progettati al contrario. Prima si compra un software, poi si disegna una sequenza di email, poi si decide quali tag assegnare. Il risultato è spesso un'automazione molto precisa di un processo che non è mai stato definito. Una persona riceve messaggi non più pertinenti, un cliente continua a essere trattato come prospect, un interesse forte rimane fermo in una sequenza lenta, un lead inadatto viene passato comunque alla vendita.

Il principio di questo capitolo è più semplice: **prima definire gli stati e le decisioni; poi usare database, regole e automazione per renderli eseguibili**.

## 16.1 Stati della relazione

Un funnel non è, prima di tutto, una successione di pagine. È una rappresentazione del modo in cui cambia la relazione tra impresa e persona.

Lo stesso individuo può essere sconosciuto al sistema, poi identificarsi, consumare un contenuto, chiedere informazioni, risultare economicamente inadatto, tornare mesi dopo, entrare in trattativa, acquistare o non acquistare. Trattarlo sempre come «lead» nasconde differenze che cambiano il lavoro da fare.

Uno **stato della relazione** è utile quando permette di rispondere a tre domande:

1. che cosa sappiamo con sufficiente affidabilità su questa persona e sulla relazione;
2. quale azione è appropriata adesso;
3. quale evento dovrebbe modificare il percorso successivo.

Il nome preciso degli stati dipende dal business. Non esiste una tassonomia universale che ogni CRM debba copiare. In un sistema di acquisizione, però, può essere utile distinguere almeno:

| Stato operativo | Che cosa sappiamo | Lavoro successivo possibile |
| --- | --- | --- |
| Non identificato | Ha incontrato un messaggio o un canale, ma non possediamo ancora una relazione utilizzabile | Ottenere una risposta osservabile senza presumere interesse commerciale |
| Contatto identificato | Possediamo dati utilizzabili e una ragione lecita per ricontattarlo | Capire problema, consapevolezza, interesse e prossimo passo |
| Prospect ingaggiato | Ha compiuto comportamenti che indicano attenzione rilevante | Aumentare comprensione, prova e pertinenza; raccogliere segnali più forti |
| Opportunità da qualificare | Ha espresso una richiesta o un'intenzione abbastanza forte da meritare una verifica | Accertare fit, capacità, timing, processo decisionale e livello di preparazione |
| Opportunità pronta per la vendita | I prerequisiti minimi per impiegare tempo commerciale costoso sono soddisfatti | Assegnare owner e passare alla conversazione commerciale con contesto sufficiente |
| Non pronto / non adatto adesso | Il passo commerciale non ha senso in questo momento | Fallback coerente: educazione, attesa, disqualifica, altro percorso o chiusura |
| Cliente | È avvenuta una transazione | Uscire dal funnel di acquisizione di quella vendita ed entrare nel percorso cliente pertinente |

Questa tabella non è una pipeline obbligatoria. Serve a mostrare la logica: **lo stato deve cambiare la decisione**. Se due etichette producono esattamente lo stesso trattamento, probabilmente una delle due non serve. Se invece persone molto diverse finiscono sotto la stessa etichetta e ricevono lo stesso messaggio, la segmentazione è troppo povera.

Lo stato della relazione non coincide con il **livello di consapevolezza** visto nel Capitolo 13. Una persona può essere nel database da mesi e conoscere ancora poco la categoria. Un'altra può entrare oggi e sapere già esattamente quale soluzione vuole. Una variabile descrive la storia con l'impresa; l'altra descrive che cosa la persona comprende rispetto al problema, alla soluzione, al prodotto e al brand.

Non coincide nemmeno con la **sorgente**. Due lead provenienti dallo stesso canale possono avere stati diversi. Una ricerca molto specifica può produrre un prospect vicino alla decisione; un'altra ricerca può essere esplorativa. Allo stesso modo, un referral e una lead da advertising possono arrivare allo stesso livello di preparazione. L'origine è un dato utile, ma non decide da sola il percorso.

### ERRORE FREQUENTE — Usare eventi tecnici come se fossero stati commerciali

Apertura di un'email, click, download, visita a una pagina o avvio di un video sono segnali. Non dimostrano automaticamente volontà di comprare.

Il problema nasce quando l'automazione trasforma un evento facilmente misurabile in una conclusione molto più forte: «ha cliccato, quindi è caldo»; «ha scaricato il report, quindi vuole un preventivo»; «ha visto una pagina prezzi, quindi va chiamato immediatamente».

Un evento tecnico può aumentare o diminuire la probabilità di un certo stato, ma deve essere interpretato nel contesto. Una richiesta esplicita, una risposta qualificante, il completamento di più passaggi coerenti o una domanda concreta hanno normalmente più peso di un singolo click. Il sistema deve usare i segnali come **evidenza graduata**, non come etichette assolute.

## 16.2 Funnel lineari e percorsi adattivi

Una sequenza lineare segue prevalentemente il tempo. Una persona entra, riceve il messaggio A, poi B, poi C, poi una proposta. Questo modello può essere sufficiente quando il pubblico è relativamente omogeneo, il percorso è corto e i comportamenti intermedi non cambiano molto la decisione successiva.

Il limite emerge quando il comportamento reale diverge dalla sequenza prevista. Alcune persone capiscono più velocemente, altre hanno bisogno di tornare indietro, altre ancora esprimono interesse forte prima che la sequenza sia terminata. Se il sistema ignora questi segnali per rispettare il calendario, il funnel diventa una gabbia.

Un **percorso adattivo** aggiunge una regola: il prossimo passo dipende non soltanto dal tempo trascorso, ma anche dallo stato e dai comportamenti osservati.

La struttura diventa:

**segnale → interpretazione dello stato → routing → azione successiva → nuovo segnale → nuovo stato.**

Il vantaggio non è la sofisticazione tecnologica. È la capacità di evitare due sprechi opposti.

Il primo è **rallentare chi è pronto**. Se una persona chiede una demo, risponde con un problema preciso, dichiara un timing ravvicinato e possiede i requisiti economici, obbligarla a ricevere altre due settimane di nurturing perché «la sequenza prevede così» aggiunge attrito. Il sistema dovrebbe poter accelerare.

Il secondo è **spingere troppo avanti chi non è pronto**. Se una proposta diretta non genera risposta, una delle ipotesi da verificare è che il prospect non abbia ancora scelto la categoria di soluzione, non comprenda bene il problema o non percepisca il bisogno come prioritario. In quel caso può essere utile ridurre la directness e tornare a un contenuto precedente, invece di ripetere la stessa offerta con maggiore pressione.

Questo backtracking non va applicato automaticamente a ogni mancata conversione. Il problema può essere prezzo, prova, timing, fit, esperienza, presa in carico o semplice assenza di domanda. Il punto è mantenere aperta una diagnosi: **la mancata risposta può indicare che abbiamo presunto uno stato più avanzato di quello reale**.

### ESEMPIO SVOLTO — Tre persone entrano dallo stesso form, ma non dovrebbero seguire lo stesso percorso

Un'impresa B2B utilizza un modulo per richiedere un approfondimento. Tre persone lo compilano nello stesso giorno.

La prima scarica il materiale e non compie altre azioni. Non ha indicato una scadenza e non ha risposto alla domanda sul problema specifico. Il sistema la mantiene in un percorso educativo leggero e prova a raccogliere un segnale più informativo.

La seconda indica che il contratto con il fornitore attuale scade entro sessanta giorni, descrive un problema concreto e chiede di capire tempi e costi. Qui il segnale è più forte. Dopo una verifica minima di fit, viene aperta un'opportunità e assegnato un contatto umano.

La terza dichiara un problema reale ma un ordine di grandezza economico incompatibile con l'offerta. Non viene inviata comunque al venditore «perché magari chiude». Riceve invece un percorso alternativo o viene disqualificata in modo coerente, a seconda di ciò che l'impresa può realmente servire.

La sorgente è identica. Il form è identico. Cambiano **stato, evidenza e prossimo passo**. Questo è il lavoro del routing.

I percorsi adattivi richiedono anche fallback espliciti. Ogni passaggio importante dovrebbe rispondere almeno a:

- qual è l'obiettivo;
- quale stato o evento fa entrare la persona;
- quale azione viene eseguita;
- chi ne è responsabile quando serve una persona;
- entro quale finestra dovrebbe avvenire;
- quale outcome ci aspettiamo;
- che cosa succede se quell'outcome non avviene;
- in quale stato si entra dopo.

Senza fallback il diagramma descrive soltanto il percorso ideale. Il business reale, invece, è pieno di persone che non aprono, non rispondono, rimandano, cambiano priorità, non si presentano o non sono adatte. Il funnel deve sapere anche dove vanno loro.

## 16.3 Database e memoria commerciale

Il database è ciò che permette al sistema di non ricominciare da zero a ogni contatto.

Una lista di email è già più utile di nessuna memoria, ma non è ancora una memoria commerciale sufficiente. Un database operativo dovrebbe conservare il minimo contesto necessario a capire **chi è questa persona, che cosa è successo, che cosa è ancora aperto e che cosa ha senso fare dopo**.

Le informazioni pertinenti possono includere, a seconda del business e delle autorizzazioni disponibili:

- dati identificativi e contatti utilizzabili;
- origine della relazione;
- stato corrente;
- acquisti e date;
- richieste, conversazioni e appuntamenti;
- problemi o bisogni dichiarati;
- contenuti o passaggi rilevanti completati;
- condizioni commerciali già discusse;
- decisori e stakeholder noti;
- timing, scadenze o trigger;
- assistenza, reclami o questioni aperte;
- owner interno;
- prossima azione prevista;
- esiti precedenti e motivo della chiusura quando noto.

Il criterio non è raccogliere più dati possibile. È raccogliere **dati che cambiano una decisione**.

Se un campo non modifica segmentazione, priorità, contenuto, qualifica, servizio, follow-up o misurazione, potrebbe essere solo attrito. La profilazione progressiva è spesso più sensata di un modulo iniziale infinito: chiedere una informazione quando diventa utile al percorso e quando il valore ricevuto giustifica lo sforzo richiesto.

Il database deve inoltre distinguere stati che, se compressi, distruggono informazione. Un lead che ha soltanto lasciato i dati non è equivalente a chi ha già svolto una vera trattativa e non ha comprato. Un acquirente di un'offerta d'ingresso non è equivalente a un cliente che ha già comprato più volte. Un cliente inattivo non è equivalente a chi ha cancellato per una cattiva esperienza.

Queste differenze cambiano il motivo per cui l'impresa può ricontattare la persona e il tipo di proposta coerente.

### IN PRATICA — Il database deve poter rispondere a una domanda operativa

Un CRM utile non è quello con più campi compilati. È quello che permette a una persona del team, o a un sistema automatizzato ben governato, di rispondere rapidamente:

**«Qual è il prossimo passo sensato per questo contatto, sulla base di ciò che sappiamo davvero?»**

Se per trovare la risposta bisogna cercare in email private, messaggi personali, fogli separati e memoria del venditore, il database non sta svolgendo il proprio lavoro. Se invece il CRM conserva centinaia di campi ma nessuno sa quale decisione producano, la complessità è soltanto amministrativa.

La memoria commerciale ha anche un valore diagnostico. Permette di contare quante persone restano ferme in ciascuno stato, quanto tempo vi rimangono, dove si concentrano le perdite e quali segmenti meritano campagne diverse. Senza memoria, ogni mese sembra nuovo e la stessa domanda viene pagata più volte.

## 16.4 Segnali, routing e fallback

Il **routing** è la regola che collega uno stato alla prossima azione. Non coincide con l'invio di una lead a un venditore. Può significare mostrare un contenuto diverso, chiedere una informazione, attivare un reminder, assegnare un task, cambiare ritmo di comunicazione, mettere in pausa una sequenza o dichiarare che non esiste alcuna azione utile per ora.

Per progettare il routing servono segnali abbastanza affidabili. Una gerarchia semplice può distinguere:

- **segnali deboli** — esposizione, visita, apertura, click isolato;
- **segnali medi** — consumo sostanziale di contenuto, ritorni ripetuti, risposta a domande di profilazione, comparazione esplicita;
- **segnali forti** — richiesta di contatto, domanda su prezzo o tempi, dichiarazione di un problema attuale, scadenza, disponibilità economica, coinvolgimento del decisore;
- **eventi decisivi** — acquisto, rifiuto esplicito, disqualifica, cancellazione, chiusura della trattativa.

La gerarchia precisa dipende dal business. Serve a evitare che il sistema reagisca allo stesso modo a comportamenti con significato molto diverso.

Una regola di routing dovrebbe essere leggibile in linguaggio operativo, per esempio:

**se** il prospect ha dichiarato un problema coerente, timeframe inferiore a novanta giorni e ordine di grandezza economico compatibile, **allora** crea opportunità, assegna owner e richiedi presa in carico entro la finestra stabilita; **se** manca il timeframe, raccoglilo prima; **se** il budget è incompatibile, attiva il percorso alternativo o chiudi.

Questa forma costringe a esplicitare ciò che molte automazioni lasciano implicito.

| Elemento | Domanda da risolvere |
| --- | --- |
| Stato di ingresso | Che cosa deve essere già vero perché la regola si applichi? |
| Segnale | Quale evento osservabile modifica la nostra valutazione? |
| Interpretazione | Che cosa possiamo concludere e che cosa no? |
| Azione | Qual è il passo successivo proporzionato? |
| Owner | Chi risponde del passaggio se richiede intervento umano? |
| Finestra | Entro quando l'azione deve avvenire? |
| Outcome | Quale risultato osservabile definisce il successo del passaggio? |
| Fallback | Che cosa succede se il risultato non avviene? |
| Stato successivo | Dove viene registrata la persona dopo l'esito? |

Il fallback è particolarmente importante perché protegge dall'illusione del funnel perfetto. Se una persona non risponde a un invito, il sistema deve sapere se attendere, cambiare messaggio, ridurre frequenza, usare un altro mezzo, creare un task umano o terminare la sequenza. «Continua a mandare email per sempre» non è una strategia di fallback.

Anche il **tempo** è un segnale. Un comportamento che ieri indicava interesse può perdere significato dopo mesi di inattività. Una scadenza che si avvicina può aumentare la priorità. Per questo gli stati dovrebbero poter cambiare non soltanto quando accade qualcosa, ma anche quando non accade nulla entro una finestra rilevante.

## 16.5 Automazione e intelligenza artificiale

L'automazione diventa utile quando riduce lavoro ripetitivo senza rendere invisibili le decisioni.

Prima di automatizzare un passaggio devono essere definiti almeno:

**stato → trigger → azione → owner → dati necessari → eccezione → escalation → misura.**

Se questi elementi non sono chiari, il software non risolve il problema. Lo rende più veloce e più difficile da vedere.

Le automazioni tradizionali sono adatte quando le regole sono stabili: inviare un reminder, aggiornare uno stato dopo un acquisto, creare un task, interrompere una sequenza, assegnare una lead in base a territorio o prodotto, notificare un ritardo. L'intelligenza artificiale può aggiungere capacità dove serve interpretare testo, sintetizzare conversazioni, recuperare contesto o preparare una risposta.

Ma un sistema customer-facing non dovrebbe essere progettato partendo dal modello. Deve partire dalla **conoscenza che l'impresa è autorizzata a usare e dalle decisioni che il sistema è autorizzato a prendere**.

Per un assistente che parla con prospect o clienti servono almeno quattro strati.

Il primo è la **conoscenza verificabile**: prodotti, condizioni, posizionamento, criteri di fit, processi, prove, limiti e informazioni aggiornate. Se la base è incoerente, l'AI può soltanto produrre incoerenza in forma più fluida.

Il secondo è il **contesto cliente**: stato della relazione, acquisti, richieste, condizioni già concordate, problemi aperti e altri dati pertinenti e utilizzabili. Senza memoria, una risposta formalmente corretta può essere commercialmente sbagliata.

Il terzo sono le **policy di risposta**: che cosa può spiegare, che cosa può stimare, quali promesse non può fare, quando deve chiedere dati aggiuntivi, quando deve fermarsi e passare a una persona.

Il quarto è l'**osservazione**: conversazioni riviste, errori classificati, nuove domande aggiunte alla base di conoscenza, regole corrette quando il comportamento reale mostra un difetto.

### ERRORE FREQUENTE — Automatizzare l'ambiguità

Un'impresa riceve richieste da un form, ma nessuno ha deciso quali lead meritino priorità, quali dati servano per qualificarle e chi debba prenderle in carico. La soluzione scelta è «mettere un'AI che risponde subito».

Il tempo di risposta può migliorare, ma l'ambiguità resta. L'assistente può rispondere rapidamente a persone che non sono in target, creare aspettative economiche errate, promettere tempi non autorizzati o non riconoscere quando una conversazione richiede un umano.

La sequenza corretta è l'opposto: prima definire la decisione, poi delegare al software le parti ripetibili. L'AI è un moltiplicatore di un sistema informativo e operativo. Se il sistema è buono può aumentare velocità e coerenza; se è confuso può moltiplicare errori con grande efficienza.

Questo capitolo non sostituisce il tema più ampio dell'automazione organizzativa che verrà affrontato nella Parte VII. Qui interessa soltanto il suo ruolo nell'acquisizione: **ricordare stato e contesto, eseguire regole, ridurre ritardi e passare alla persona giusta quando la decisione supera i confini autorizzati**.

## 16.6 Prequalifica e passaggio alla vendita

Il funnel di acquisizione termina bene quando consegna alla vendita un'opportunità abbastanza informata e abbastanza appropriata da giustificare il costo del contatto umano.

Prequalificare non significa chiudere la vendita prima del venditore. Significa evitare che il venditore debba ricostruire ogni volta informazioni che il sistema poteva ottenere, spiegare o filtrare a monte.

Quattro risultati sono particolarmente utili.

Il primo è la **premotivazione**. Il prospect dovrebbe avere una ragione per valutare proprio questa impresa e non arrivare alla conversazione convinto che tutti i fornitori siano intercambiabili. Posizionamento, prova, materiali e informazioni standardizzabili dovrebbero fare una parte di questo lavoro prima dell'appuntamento.

Il secondo è la **compatibilità economica**. Non è sempre necessario pubblicare il prezzo preciso, soprattutto nelle offerte progettuali, ma il prospect dovrebbe avere aspettative ragionevoli sull'ordine di grandezza. Se pensa di spendere un terzo di ciò che il business può accettare, la trattativa è partita troppo presto.

Il terzo riguarda **processo e potere decisionale**. Chi usa, chi paga, chi autorizza e chi può bloccare? Se la decisione richiede più stakeholder, il sistema dovrebbe almeno provare a renderlo visibile prima che la trattativa arrivi alla proposta finale.

Il quarto è il **timeframe**. Una persona può essere perfettamente in target e non poter comprare oggi. Contratti in corso, budget, cicli di approvvigionamento e altre priorità possono rendere il bisogno reale ma non immediato. Il sistema deve distinguere «non ora» da «non interessato» e preservare la relazione quando l'economia lo giustifica.

A questi quattro elementi va aggiunto un criterio più generale: **fit operativo**. Alcuni clienti sono economicamente capaci ma richiedono condizioni, personalizzazioni o rischi che rendono la vendita indesiderabile. La prequalifica deve quindi proteggere non soltanto il tempo del venditore, ma anche il sistema a valle.

Quando i prerequisiti sono soddisfatti, il passaggio alla vendita deve essere concreto. Non basta cambiare uno stato nel CRM. Servono almeno:

- owner della presa in carico;
- tempo atteso di risposta;
- contesto raccolto finora;
- motivo della richiesta;
- stato e segnali osservati;
- aspettative economiche note;
- timing;
- stakeholder conosciuti;
- materiali già fruiti quando rilevanti;
- prossima azione concordata.

La velocità conta soprattutto quando il prospect ha appena espresso un'intenzione forte. Una richiesta lasciata ferma per ore o giorni può perdere priorità e rende inutile parte del lavoro di acquisizione già pagato. Il principio non è inseguire ogni click in tempo reale, ma **ridurre intenzionalmente il tempo tra un segnale commerciale forte e la presa in carico coerente**.

Per vendite semplici, il percorso può concludersi senza interazione umana. Per decisioni complesse, invece, testo e automazione non sostituiscono necessariamente una conversazione sincrona. Diagnosi, dubbi, stakeholder e trade-off possono richiedere una persona capace di adattare l'approfondimento in tempo reale.

Il confine va scelto in base al lavoro che rimane da fare, non in base all'ideologia «self-service sempre» o «venditore sempre».

### STRUMENTO OPERATIVO — Mappa stati, routing e handoff

| Campo | Che cosa registrare |
| --- | --- |
| Stato | Situazione operativa corrente della relazione |
| Evidenza dello stato | Quali fatti o comportamenti giustificano la classificazione |
| Consapevolezza | Problema, soluzione, prodotto, brand o altra dimensione utile |
| Segnale recente | Evento che può cambiare priorità o percorso |
| Intento / timing | Quanto è vicino e attuale il bisogno dichiarato o osservato |
| Dati mancanti | Informazioni che cambierebbero davvero la decisione successiva |
| Azione successiva | Passo proporzionato allo stato corrente |
| Owner | Persona o sistema responsabile |
| Finestra | Entro quando deve accadere |
| Outcome atteso | Risultato osservabile del passaggio |
| Fallback | Azione se l'outcome non avviene |
| Stato successivo | Come verrà riclassificata la persona |
| Condizione di handoff | Requisiti minimi per passare a vendita o altro reparto |
| Contesto da trasferire | Informazioni che il nuovo owner deve ricevere |
| Automazione ammessa | Parti eseguibili senza giudizio umano aggiuntivo |
| Escalation | Condizioni che richiedono intervento umano |
| Metrica | Tempo di attraversamento, conversione, perdita, CAC o altra misura pertinente |

La mappa obbliga a separare ciò che il sistema sa da ciò che sta inferendo. Un routing senza evidenza è una supposizione automatizzata. Un handoff senza contesto costringe il venditore a ricominciare. Un fallback assente crea lead «parcheggiate» che il CRM conserva ma nessuno governa.

### VERIFICA NELLA TUA AZIENDA — Il tuo funnel sa che cosa deve succedere dopo?

Scegli una sola offerta importante e ricostruisci il percorso reale di trenta-cinquanta contatti recenti, includendo sia chi ha comprato sia chi si è fermato. Non partire dal diagramma teorico: parti da ciò che è realmente successo.

1. Elenca gli stati che oggi il team usa, formalmente o nella pratica. Elimina quelli che non cambiano nessuna decisione e separa quelli che contengono persone con bisogni operativi diversi.
2. Per ciascuno stato, identifica l'evidenza che lo giustifica. Cerca etichette costruite su un singolo click o su impressioni non verificabili.
3. Confronta sorgente e stato. Verifica se il sistema tratta automaticamente tutti i contatti di un canale nello stesso modo anche quando comportamento e consapevolezza differiscono.
4. Individua il passaggio con più persone ferme o perse. Prima di comprare altro traffico, formula almeno una ipotesi sulla causa del blocco e una misura per verificarla.
5. Controlla il database. Per dieci contatti scelti a caso, una persona diversa dal proprietario della relazione riesce a capire cosa è successo, che cosa è aperto e quale passo sia previsto?
6. Elenca i tre segnali che attivano un routing importante. Per ciascuno, verifica se il significato commerciale attribuito è proporzionato all'evidenza reale.
7. Scegli un percorso senza risposta e scrivi il fallback. Se oggi il fallback è «resta nella sequenza», decidi quando cambiare ritmo, percorso, owner o quando chiudere.
8. Audit dell'automazione: per ogni azione automatica rilevante, scrivi stato, trigger, dati necessari, eccezione ed escalation. Se uno di questi elementi manca, l'automazione sta compensando una regola non definita.
9. Verifica l'handoff alla vendita. Le opportunità arrivano con premotivazione, ordine di grandezza economico, timeframe e stakeholder sufficientemente chiari? Quanto tempo passa tra un segnale forte e la presa in carico?
10. Scegli un solo collo di bottiglia e correggilo prima di aggiungere nuove sequenze, nuovi tag o nuovo traffico. Definisci metrica, periodo di osservazione e condizione di revisione.

L'output utile è un sistema in cui ogni contatto possiede uno stato comprensibile, ogni stato ha un prossimo passo, ogni passaggio ha un fallback e la vendita riceve opportunità con abbastanza contesto da non dover ricostruire il marketing da zero.

Con questo capitolo si chiude la Parte IV. La prova ha reso credibile la proposta; la mappa della domanda ha distinto chi era pronto da chi richiedeva educazione; canali e partnership hanno definito come ottenere accesso; funnel e database hanno trasformato quell'accesso in un movimento governabile verso la vendita.

La Parte V cambierà livello ancora una volta. Una opportunità informata non è ancora una decisione. Dovremo costruire l'argomentazione commerciale, trasformarla in comunicazione persuasiva e condurre una vendita consulenziale senza usare il copy o il venditore per nascondere difetti rimasti a monte.
