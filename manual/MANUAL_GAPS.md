# Manual Gaps Register

## Scopo

Questo registro contiene i gap che possono impedire al publishing layer di diventare un manuale autosufficiente per un lettore principiante.

Un gap non implica automaticamente che manchi dottrina.

Classificazione obbligatoria:

- **EDITORIAL GAP** — conoscenza presente ma dispersa, duplicata o non sequenziata;
- **CURRICULUM GAP** — conoscenza presente ma collocata male rispetto ai prerequisiti;
- **DOCTRINAL GAP** — conoscenza canonica insufficiente;
- **PROVENANCE GAP** — tracciabilità insufficiente per verificare una sintesi;
- **CASE GAP** — materiale applicativo insufficiente.

Regola: tentare prima la soluzione editoriale quando la conoscenza esiste già. Non modificare `merenda/` o riaprire acquisizione per risolvere un problema soltanto di sintesi.

---

# Gap attivi

## G-001 — Processo di vendita end-to-end

**Priorità: P1**  
**Tipo: EDITORIAL GAP; possibile residuo DOCTRINAL GAP**  
**Stato: IN SYNTHESIS**

### Evidenza

La sezione vendita contiene prequalifica, speed-to-lead, decisori, diagnosi, follow-up, script, role-play e controllo, ma manca una singola sequenza canonica end-to-end.

Le sezioni già decomposte aggiungono prerequisiti che la futura sintesi vendita deve incorporare:

- `OFF-021` — offerta largamente standardizzata prima della trattativa;
- `OFF-060` — marketing e vendita devono argomentare lo stesso valore/prezzo;
- `MKT-040` — script, training e pre-educazione riducono la variabilità umana;
- `MKT-042` — marketing, vendita e follow-up sono un sistema integrato;
- `MKT-068` — la vendita end-to-end non può iniziare dalla sola conversazione commerciale.

### Requisito del manuale

Il lettore deve poter seguire una sequenza completa dall'ingresso dell'opportunità alla decisione/follow-up, distinguendo ciò che deve essere già risolto da marketing/offerta da ciò che appartiene al venditore.

### Azione

Decomporre `06_vendita`, costruire una sequenza candidata e verificare se restano buchi reali prima di qualunque review canonica.

---

## G-002 — Libreria casi didattici insufficiente

**Priorità: P1**  
**Tipo: CASE GAP**  
**Stato: IN SYNTHESIS**

### Evidenza

`merenda/10_casi_studio/` contiene due casi sostanziali, ma molti esempi utili sono dispersi nei nodi. `02_posizionamento` ha già prodotto `POS-051…POS-055` come primi elementi di case inventory.

### Azione

Continuare a marcare esempi/casi durante il crosswalk; nel pass dedicato distinguere:

1. casi reali sufficientemente verificabili;
2. esempi illustrativi non utilizzabili come prova;
3. casi sintetici originali da costruire soltanto per didattica, dichiarandoli come tali.

---

## G-003 — Doctrine/provenance map per il backend editoriale

**Priorità: P1**  
**Tipo: PROVENANCE GAP / EDITORIAL INFRASTRUCTURE**  
**Stato: IN SYNTHESIS**

### Evidenza

Il source layer conserva la provenance, ma il manuale necessita di una mappa compatta principio → nodo canonico → trattamento/provenienza/caveat temporale.

Il crosswalk ha già identificato casi che richiedono esplicita cautela:

- `MRC-036` — Proof by Refusal, fonte assimilata;
- `POS-022/POS-023` — rendere visibile/nominare un processo reale, contributo assimilato;
- `OFF-007/OFF-029` — bundle come riduzione del costo cognitivo e prova sufficientemente lunga, fonti assimilate;
- `POS-044` — family brand storico esplicitamente superseded;
- `OFF-022` — front-end come riduzione della barriera, prevalenza 2025;
- `MKT-018/MKT-020/MKT-027` — vecchi assoluti sui canali/cold/social subordinati alla formulazione più recente.

### Azione

Continuare a registrare solo provenance e temporalità necessarie alla verifica. La mappa compatta verrà consolidata nel cross-section pass.

---

## G-004 — Sintesi organica della costruzione del brand

**Priorità: P2**  
**Tipo: EDITORIAL GAP**  
**Stato: IN SYNTHESIS**

### Evidenza

Esistono nodi separati su autorità, prova sociale, PR, reputazione e community. `POS-057` chiarisce però il prerequisito: il brand non sostituisce il posizionamento; deve costruirsi sopra un significato distinto. `OFF-047/OFF-063` mostrano poi come autorità, esperienza e prova sostengano willingness-to-pay.

### Sequenza candidata da verificare

**posizione/significato → autorità/credibilità → acquisizione → esperienza/risultato → prova/reputazione → memoria → advocacy/community.**

### Azione

Validare e completare questa sintesi durante `08_brand`, senza trattarla ancora come regola canonica autonoma.

---

## G-005 — Voice of Customer / ricerca di mercato

**Priorità: P2**  
**Tipo: EDITORIAL GAP, con possibile residuo DOCTRINAL GAP**  
**Stato: IN SYNTHESIS**

### Evidenza disponibile finora

`01_mercato` fornisce:

- clienti migliori/peggiori;
- margine, frequenza, recency, LTV, cost-to-serve;
- alternative e storia di acquisto;
- soddisfazione e volontà di cambiare;
- capacità di acquisto e fit;
- risultati/implementazione;
- dimensione, identificabilità, raggiungibilità e trend della domanda.

`02_posizionamento` aggiunge:

- `POS-005/POS-006` — complaint mining delle alternative → redesign;
- `POS-031` — domanda non suggerita “perché hai scelto noi?” per testare la posizione percepita.

`04_marketing` aggiunge:

- `MKT-012` — volume di ricerca distinto dall'intento;
- `MKT-013/MKT-014` — timing e trigger della domanda;
- `MKT-050…MKT-053` — comportamento atteso vs inattività;
- `MKT-066` — includere cause di mancato ritorno.

### Gap residuo

Manca ancora una procedura unica per:

1. definire le domande di ricerca;
2. scegliere e combinare fonti;
3. condurre/analizzare interviste;
4. estrarre linguaggio e pattern senza sovrappesare singoli casi;
5. distinguere frequenza, intensità e valore economico del segnale;
6. trasformare insight in target, problema, offerta, prova e messaggio;
7. validare con comportamento e numeri.

### Azione

Continuare la sintesi in acquisizione, copy e brand; decidere solo dopo il cross-section pass se resta un doctrinal gap nominabile.

---

## G-006 — Economics fondamentali collocati troppo tardi per il curriculum

**Priorità: P1**  
**Tipo: CURRICULUM GAP**  
**Stato: CONFIRMED — DA RISOLVERE IN FASE 3**

### Evidenza cumulativa

Gli economics sono prerequisiti già prima di `09_business`:

- mercato/cliente: `MRC-005`, `MRC-024…MRC-027`, `MRC-035`, `MRC-047`;
- posizionamento: `POS-024`, `POS-026`, `POS-049`;
- offerta: `OFF-005`, `OFF-015`, `OFF-033…OFF-035`, `OFF-061…OFF-065`;
- marketing: `MKT-003`, `MKT-024`, `MKT-028…MKT-030`, `MKT-057`, `MKT-067`.

### Decisione editoriale già sostenuta

Il curriculum dovrà distinguere:

1. **economics fondamentali presto** — margine, CAC, LTV, payback, cost-to-serve, capacità, break-even essenziale;
2. **economics avanzati più avanti** — cassa, struttura, reinvestimento, capacità e crescita.

Non duplicare la teoria: introdurre progressivamente e rinviare alla casa specialistica.

---

## G-007 — Glossario e linguaggio per principianti

**Priorità: P2**  
**Tipo: EDITORIAL GAP**  
**Stato: OPEN**

Termini già emersi che richiedono definizione prima dell'uso: CAC, LTV, payback, cost-to-serve, RFM, front-end, back-end, upsell, cross-sell, risk reversal, direct response, awareness, intent, funnel, positioning, referral, sell-in, sell-through, exploitation/exploration.

### Azione

Continuare a marcare termini; il curriculum deve impedire gergo anticipato e la release finale avrà glossario.

---

## G-008 — Ciclo post-vendita distribuito fra più sezioni

**Priorità: P2**  
**Tipo: EDITORIAL / CURRICULUM GAP**  
**Stato: IN SYNTHESIS**

### Evidenza cumulativa

- `MRC-046…MRC-051` — durata naturale, rotazione coorti, payer/user, picchi di esperienza;
- `OFF-033…OFF-044` — conversione economica, back-end, seconda transazione, ricorrenza e recupero opportunità;
- `MKT-001…MKT-003` — priorità alla domanda già posseduta;
- `MKT-050…MKT-056` — frequenza attesa, trigger CRM e riattivazione;
- `MKT-065` — lifecycle fondato su durata/frequenza naturale → comportamento atteso → deviazione → intervento.

### Impatto

Retention non può essere insegnata come semplice “tenere il cliente per sempre”. Il sistema deve distinguere relazione naturalmente breve, seconda vendita, continuità, inattività, riattivazione, referral e sostituzione delle coorti.

### Azione

Completare con `05_acquisizione`, `08_brand` e `09_business`, quindi assegnare una casa primaria al customer lifecycle.

---

# Gap chiusi

Nessuno. G-006 è confermato ma si chiuderà soltanto quando il curriculum lo risolverà effettivamente.

---

# Regola di aggiornamento

Stati ammessi:

- `OPEN`;
- `IN SYNTHESIS`;
- `CONFIRMED — DA RISOLVERE IN FASE 3`;
- `RESOLVED EDITORIALLY`;
- `ESCALATED TO DOCTRINE REVIEW`;
- `DEFERRED WITH REASON`.

Non chiudere un gap perché “abbiamo scritto qualcosa”. Chiuderlo solo quando il requisito didattico o conoscitivo è verificabilmente soddisfatto.
