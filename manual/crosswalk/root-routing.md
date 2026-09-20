# Crosswalk — Root routing e governance semantica

## Scope

File coperti:

- `merenda/INDEX.md`
- `merenda/DECISION_ROUTER.md`

Stato: **COMPLETE — first semantic pass**.

Questi file non sono la sede primaria dei principi specialistici. Il loro valore editoriale è insegnare **come diagnosticare e in quale ordine decidere**, oltre a preservare regole di navigazione e provenance. Quando una formulazione entra in conflitto con un nodo specialistico più preciso o recente, prevale il nodo specialistico.

---

# A. Metodo diagnostico

## RTR-001 — Cercare il primo punto economicamente o strategicamente rotto

**Tipo:** PRINCIPLE / DECISION_RULE  
**Ruolo candidato:** PRIMARY  
**Fonte:** `DECISION_ROUTER.md`

### Unità di conoscenza

Davanti a un problema di business non si parte dalla tattica richiesta. Si localizza il primo punto a monte che può spiegare il risultato mancante e che blocca valore, margine o avanzamento della relazione.

### Il lettore deve saper fare

Trasformare una richiesta tattica in una diagnosi del sistema prima di prescrivere un intervento.

### Prerequisiti

Comprensione del business come catena causale.

### Influenza a valle

Tutto il metodo diagnostico del manuale.

---

## RTR-002 — Risalire almeno un livello a monte

**Tipo:** PROCEDURE / CAUSAL_RULE  
**Ruolo candidato:** PRIMARY  
**Fonte:** `DECISION_ROUTER.md`

### Unità di conoscenza

Il luogo in cui compare il problema non coincide necessariamente con la causa. Prima di correggere un sintomo bisogna controllare almeno un livello precedente della catena.

### Esempi

- pochi lead può dipendere da traffico, ma anche da posizionamento o offerta;
- bassa chiusura può dipendere dal venditore, ma anche da prequalifica o prova;
- churn può dipendere dal follow-up, ma prima ancora dall'esperienza reale.

---

## RTR-003 — Separare causa, amplificatore e sintomo

**Tipo:** DEFINITION / DIAGNOSTIC_RULE  
**Ruolo candidato:** PRIMARY  
**Fonte:** `DECISION_ROUTER.md`

### Unità di conoscenza

Una tattica può essere un amplificatore invece che la causa del problema. Ads, funnel, venditori e crescita possono aumentare il volume di un difetto già presente.

### Il lettore deve saper fare

Classificare ciò che osserva come causa, amplificatore o sintomo prima di decidere dove intervenire.

---

## RTR-004 — Definire il risultato economico mancante prima della soluzione

**Tipo:** PROCEDURE / METRIC  
**Ruolo candidato:** PRIMARY  
**Fonte:** `DECISION_ROUTER.md`

### Unità di conoscenza

Ogni diagnosi deve partire da quattro elementi: risultato atteso, risultato osservato, metrica e conseguenza economica. Una richiesta come “serve più marketing” non è ancora una diagnosi.

### Output operativo

Un gap osservabile espresso in termini di valore, margine, cassa, conversione, retention o capacità.

---

## RTR-005 — Mercato e cliente sono gate, non semplici capitoli

**Tipo:** GATE / DEPENDENCY  
**Ruolo candidato:** SUPPORTING  
**Fonte:** `DECISION_ROUTER.md`

### Unità di conoscenza

Prima di costruire macchina commerciale e tattiche bisogna verificare domanda, raggiungibilità, capacità di acquisto e qualità economica del cliente. Un problema a valle non merita investimento se il mercato o il cliente sono sbagliati.

### Casa primaria futura

Mercato / economics del cliente.

---

## RTR-006 — Controllare il valore già posseduto prima di comprare nuova domanda

**Tipo:** DECISION_RULE / DEPENDENCY  
**Ruolo candidato:** SUPPORTING  
**Fonte:** `DECISION_ROUTER.md`

### Unità di conoscenza

Quando il problema è ricavi o clienti, il controllo iniziale riguarda normalmente clienti attivi, seconda vendita, referral, clienti fermi e opportunità non convertite prima di aumentare l'acquisizione fredda.

### Casa primaria futura

Domanda / customer lifecycle / acquisition economics.

---

## RTR-007 — Un collo di bottiglia alla volta

**Tipo:** DECISION_RULE / PROCEDURE  
**Ruolo candidato:** PRIMARY  
**Fonte:** `DECISION_ROUTER.md`

### Unità di conoscenza

Se più parti sono deboli, cambiare tutto insieme riduce capacità di apprendimento e rende difficile attribuire i risultati. Si sceglie il primo collo di bottiglia economicamente rilevante e si interviene lì.

### Dipendenze

RTR-001…RTR-004.

---

## RTR-008 — Ogni intervento deve produrre evidenza

**Tipo:** PROCEDURE / METRIC  
**Ruolo candidato:** PRIMARY  
**Fonte:** `DECISION_ROUTER.md`

### Unità di conoscenza

Un intervento operativo deve dichiarare almeno: ipotesi, azione, risposta o avanzamento atteso, metrica, finestra/quantità di evidenza e criterio di mantenimento, modifica o stop.

### Influenza a valle

Testing, marketing, funnel, vendita, operations e scala.

---

## RTR-009 — Standardizzare dopo la prova; scalare dopo economics e capacità

**Tipo:** GATE / CAUSAL_RULE  
**Ruolo candidato:** PRIMARY  
**Fonte:** `DECISION_ROUTER.md`

### Unità di conoscenza

Prima si dimostra che un meccanismo funziona, poi lo si rende ripetibile. La scala arriva soltanto se margine, cassa, payback e capacità reggono l'aumento di volume.

### Caveat

“Funziona” non significa soltanto produce lead o fatturato; deve produrre un risultato economicamente sostenibile.

---

# B. Ordine decisionale

## RTR-010 — Sequenza causale end-to-end

**Tipo:** SYNTHESIS / DEPENDENCY  
**Ruolo candidato:** PRIMARY  
**Fonte:** `DECISION_ROUTER.md`; coerente con `00_fondamenti/sistema-operativo-merenda.md`

### Unità di conoscenza

La sequenza generale di diagnosi è:

**mercato → cliente appropriato → posizionamento → offerta → autorità/prova → domanda/canale → acquisizione/pre-educazione → vendita → esperienza → retention/referral → economics/capacità → reinvestimento → espansione.**

Non è una pipeline rigida: i feedback a valle possono richiedere correzioni a monte.

### Uso editoriale

Architettura del prerequisite graph, non necessariamente indice letterale del manuale.

---

## RTR-011 — Il canale o lo strumento non è il punto di partenza

**Tipo:** ERROR_PATTERN / DECISION_RULE  
**Ruolo candidato:** SUPPORTING  
**Fonte:** `DECISION_ROUTER.md`

### Unità di conoscenza

Domande come “quale social?”, “quale funnel?”, “quale software?” o “scrivimi il copy” devono essere precedute dalla verifica dei prerequisiti strategici che rendono lo strumento razionale.

### Casa primaria futura

Fondamenti / applicazioni tattiche.

---

## RTR-012 — Strategia interna, strumenti esterni

**Tipo:** PRINCIPLE / ERROR_PATTERN  
**Ruolo candidato:** SUPPORTING  
**Fonte:** `DECISION_ROUTER.md`

### Unità di conoscenza

Agenzie, software e AI possono accelerare esecuzione e analisi, ma non possono sostituire la responsabilità di definire mercato, posizione, economia, criterio di successo e trade-off.

### Casa primaria futura

Fondamenti / organizzazione.

---

## RTR-013 — La matrice dei sintomi è un'applicazione, non nuova dottrina

**Tipo:** PROCEDURE / REFERENCE  
**Ruolo candidato:** SUPPORTING  
**Fonte:** `DECISION_ROUTER.md`

### Unità di conoscenza

I router per sintomi — pochi clienti, pochi lead, bassa chiusura, sconti, churn, poca cassa, dipendenza dal fondatore, espansione — mostrano come riusare lo stesso metodo causale in problemi diversi. Non devono diventare capitoli duplicati: sono materiale da trasformare in una matrice diagnostica o esercizi applicativi.

---

# C. Navigazione e provenance

## RTR-014 — La tassonomia della KB non è il curriculum

**Tipo:** CAVEAT / REFERENCE  
**Ruolo candidato:** REFERENCE  
**Fonte:** `INDEX.md`

### Unità di conoscenza

Le 11 sezioni correnti sono stabili come doctrine layer e routing, ma non vincolano l'ordine pedagogico del manuale.

### Implicazione editoriale

Il curriculum deve seguire prerequisiti cognitivi e causalità, non la struttura delle cartelle.

---

## RTR-015 — Nodo specialistico prevale sulla sintesi

**Tipo:** CAVEAT / PROVENANCE  
**Ruolo candidato:** REFERENCE  
**Fonte:** `INDEX.md`; `DECISION_ROUTER.md`

### Unità di conoscenza

Router e sintesi semplificano. Se un nodo specialistico contiene una formulazione più precisa, contestuale o recente, quella formulazione governa il significato finale.

### Implicazione editoriale

Ogni sintesi del manuale deve poter essere ricondotta ai nodi specialistici primari.

---

## RTR-016 — Provenance reale anche in un manuale source-agnostic

**Tipo:** PROVENANCE / CAVEAT  
**Ruolo candidato:** REFERENCE  
**Fonte:** `INDEX.md`

### Unità di conoscenza

Il corpus contiene fonti primarie e fonti assimilate. La compatibilità con il sistema non modifica l'autore reale. Il manuale reader-facing può essere agnostico, ma il backend deve preservare la distinzione necessaria a evitare falsa attribuzione e fusioni scorrette.

---

## RTR-017 — Nuova acquisizione di conoscenza solo per gap nominabile

**Tipo:** GATE / GOVERNANCE  
**Ruolo candidato:** REFERENCE  
**Fonte:** `INDEX.md`

### Unità di conoscenza

Un corpus già sufficientemente saturo non va esteso per quantità. Nuove fonti si acquisiscono quando esiste una fonte realmente disponibile o un gap concreto che impedisce una decisione o una spiegazione affidabile.

### Implicazione editoriale

Il manuale non deve diventare infinito per inseguire completezza numerica.

---

# D. Sintesi di sezione

Unità create: **17** (`RTR-001…RTR-017`).

Destinazione prevalente:

- metodo diagnostico e ordine decisionale → futuro modulo fondativo/metodologico;
- router per sintomi → strumenti diagnostici, esercizi o appendice;
- tassonomia/provenance/governance → backend editoriale, non prosa reader-facing autonoma.

Finding: i due file root sono **coperti** ma non introducono una nuova materia specialistica da aggiungere al curriculum. `DECISION_ROUTER.md` comprime il metodo di diagnosi; `INDEX.md` governa navigazione, precedence e provenance.
