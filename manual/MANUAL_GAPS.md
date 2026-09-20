# Manual Gaps Register

## Scopo

Questo registro contiene i gap che possono impedire al publishing layer di diventare un manuale autosufficiente per un lettore principiante.

Un gap non implica automaticamente che manchi dottrina.

Classificazione obbligatoria:

- **EDITORIAL GAP** — la conoscenza esiste ma è dispersa, duplicata o non sequenziata per insegnarla;
- **CURRICULUM GAP** — la conoscenza esiste ma la tassonomia corrente la colloca troppo tardi/presto rispetto ai prerequisiti;
- **DOCTRINAL GAP** — il doctrine layer corrente non contiene abbastanza conoscenza per sostenere una spiegazione affidabile;
- **PROVENANCE GAP** — manca tracciabilità sufficiente per verificare una sintesi;
- **CASE GAP** — manca materiale applicativo sufficiente per insegnare o verificare il trasferimento del concetto.

Regola: tentare prima la soluzione editoriale quando la conoscenza esiste già. Non modificare `merenda/` o riaprire acquisizione per risolvere un problema che è soltanto di sintesi.

---

# Gap attivi

## G-001 — Processo di vendita end-to-end

**Priorità: P1**  
**Tipo: EDITORIAL GAP; possibile DOCTRINAL GAP già noto**  
**Stato: OPEN**

### Evidenza

La sezione vendita dispone di nodi su:

- prequalifica;
- speed-to-lead;
- decisori;
- diagnosi e consulenza;
- follow-up;
- script;
- role-play;
- controllo della rete vendita.

Il semantic audit ha già rilevato che manca un singolo nodo capace di rispondere a:

**come si conduce una vendita dall'inizio alla fine secondo questo sistema?**

### Impatto sul manuale

Un principiante non deve essere costretto a ricostruire la sequenza da quattro file diversi.

### Azione prevista

In Fase 2 estrarre tutte le unità della vendita e costruire una sequenza candidata end-to-end nel publishing layer.

Solo se restano buchi reali dopo la sintesi, valutare separatamente un intervento canonico.

---

## G-002 — Libreria casi didattici insufficiente

**Priorità: P1**  
**Tipo: CASE GAP**  
**Stato: OPEN**

### Evidenza

`merenda/10_casi_studio/` contiene due casi sostanziali. Esistono inoltre esempi dispersi dentro nodi specialistici.

### Impatto sul manuale

Un manuale teorico-operativo completo richiede esempi locali e casi end-to-end per mostrare trasferimento fra mercato, posizionamento, offerta, acquisizione, vendita, economics e capacità.

### Azione prevista

Durante il crosswalk:

1. marcare ogni esempio/caso già presente nei nodi;
2. distinguere esempi da preservare concettualmente da aneddoti non necessari;
3. creare una case inventory;
4. progettare casi sintetici originali dove manca un esempio didattico, senza inventare “evidenza” fattuale.

---

## G-003 — Doctrine/provenance map per il backend editoriale

**Priorità: P1**  
**Tipo: PROVENANCE GAP / EDITORIAL INFRASTRUCTURE**  
**Stato: OPEN**

### Evidenza

La provenance esiste nel source layer e nelle review, ma non esiste ancora una mappa compatta principle → canonical node → provenance treatment utile alla costruzione del manuale.

### Impatto sul manuale

Il testo finale deve essere source-agnostic, ma il lavoro editoriale deve evitare di:

- attribuire implicitamente tutto a un singolo autore;
- perdere evoluzioni temporali;
- fondere caveat incompatibili;
- trasformare una sintesi in fonte primaria.

### Azione prevista

Integrare provenance e temporal caveat nel semantic crosswalk solo al livello necessario per verificabilità. Non replicare l'intero source registry.

### Evidenza emersa in Fase 2

`MRC-036 — Proof by Refusal` conferma che alcuni principi utili al manuale provengono da fonti assimilate e richiedono provenance backend esplicita anche se la prosa finale è agnostica.

---

## G-004 — Sintesi organica della costruzione del brand

**Priorità: P2**  
**Tipo: EDITORIAL GAP**  
**Stato: OPEN**

### Evidenza

Esistono nodi autonomi su:

- autorità;
- prova sociale;
- PR/earned media;
- reputazione/crisis management;
- community/fan.

Manca una sequenza didattica unica che spieghi come questi elementi si concatenano e come si distinguono.

### Azione prevista

Costruire nel publishing layer una sequenza candidata, da verificare semanticamente, del tipo:

**posizionamento → autorità/credibilità → acquisizione → esperienza → reputazione/prova → memoria → advocacy/community.**

La sequenza è una working synthesis, non ancora una regola canonica autonoma.

---

## G-005 — Voice of Customer / ricerca di mercato

**Priorità: P2**  
**Tipo: EDITORIAL GAP, con possibile residuo DOCTRINAL GAP**  
**Stato: IN SYNTHESIS**

### Evidenza iniziale

Il semantic audit segnala che le tecniche esistono ma sono disperse fra:

- analisi dei clienti migliori;
- complaint mining;
- testimonianze;
- query e intento;
- competitor;
- storia di acquisto;
- segmentazione e appropriatezza.

### Evidenza dopo `01_mercato`

Il crosswalk mercato ha consolidato una base sostanziale di input per la ricerca:

- clienti migliori e peggiori;
- margine, frequenza, recency, LTV e cost-to-serve;
- alternative attuali e storia d'acquisto;
- soddisfazione e volontà di cambiare;
- dialogo mentale/linguaggio quando osservabile;
- capacità di acquisto;
- fit e capacità di implementazione;
- risultati ottenuti;
- dimensione, identificabilità, raggiungibilità e trend della domanda.

Riferimenti: `MRC-015`, `MRC-017…MRC-022`, `MRC-031…MRC-035`, `MRC-052…MRC-053`.

### Gap residuo

La sezione non fornisce ancora da sola un processo completo per:

1. definire quali domande di ricerca servono;
2. scegliere e combinare fonti;
3. condurre e analizzare interviste;
4. estrarre linguaggio e pattern senza sovrappesare singoli casi;
5. distinguere frequenza, intensità e valore economico del segnale;
6. sintetizzare gli insight in target, problema, offerta, prova e messaggio;
7. validare la sintesi con comportamento e numeri.

### Impatto sul manuale

Il lettore non può ricevere soltanto la regola “capisci il mercato”: deve avere un processo per raccogliere evidenza senza confondere opinioni del founder e comportamento del cliente.

### Azione prevista

Continuare la sintesi durante `02_posizionamento`, `04_marketing`, `07_copy_comunicazione`, `08_brand` e i nodi che contengono complaint/query/testimonianze. Dopo il cross-section pass decidere se il processo è costruibile interamente nel publishing layer o se resta un doctrinal gap preciso.

---

## G-006 — Economics fondamentali collocati troppo tardi per il curriculum

**Priorità: P1**  
**Tipo: CURRICULUM GAP**  
**Stato: OPEN — EVIDENZA RAFFORZATA**

### Evidenza

La sede specialistica principale di CAC, margine, LTV, payback, cassa e crescita è `09_business/numeri-cassa-e-crescita.md`.

Tuttavia gli stessi concetti sono prerequisiti per comprendere:

- cliente economicamente desiderabile;
- appropriatezza;
- pricing;
- front-end/back-end;
- canali;
- acquisizione;
- retention;
- capacità e scala.

Il crosswalk `01_mercato` rafforza il punto: `MRC-005`, `MRC-024`, `MRC-025`, `MRC-027`, `MRC-035` e `MRC-047` richiedono margine, LTV, cost-to-serve, capacità e payback già per scegliere il mercato e il cliente.

### Azione prevista

Nel curriculum separare almeno:

1. economics fondamentali introdotti presto;
2. economics avanzati/cassa/crescita trattati più avanti.

Non duplicare la teoria: usare introduzione progressiva e una casa primaria chiara.

---

## G-007 — Glossario e linguaggio per principianti

**Priorità: P2**  
**Tipo: EDITORIAL GAP**  
**Stato: OPEN**

### Evidenza

La KB presuppone spesso familiarità con termini quali CAC, LTV, payback, front-end, back-end, direct response, awareness, funnel, positioning, referral, RFM, cost-to-serve e altri.

### Impatto sul manuale

Un lettore nuovo può capire la frase senza capire il modello.

### Azione prevista

Il semantic crosswalk deve marcare i termini che richiedono una prima definizione. Il curriculum dovrà impedire l'uso non spiegato del gergo e la release finale includerà un glossario.

---

## G-008 — Ciclo post-vendita distribuito fra più sezioni

**Priorità: P2**  
**Tipo: EDITORIAL / CURRICULUM GAP**  
**Stato: OPEN**

### Evidenza

Il valore post-vendita è distribuito fra:

- `05_acquisizione/referral-e-soddisfazione.md`;
- `04_marketing/riattivazione-clienti.md`;
- `08_brand/testimonianze-e-prova-sociale.md`;
- `08_brand/reputazione-e-crisis-management.md`;
- `09_business/retention-onboarding-e-customer-success.md`;
- `03_offerta/front-end-e-back-end.md`.

`MRC-046…MRC-051` aggiungono una dipendenza importante: la retention va letta rispetto alla durata naturale della relazione e alla rotazione delle coorti, non come permanenza infinita del singolo cliente.

### Impatto sul manuale

Senza un disegno unitario, retention, seconda vendita, referral, reputazione, riattivazione e sostituzione delle coorti rischiano di sembrare tattiche separate invece di un ciclo economico unico.

### Azione prevista

Nel crosswalk mappare il customer lifecycle completo e assegnare una casa primaria ai concetti, mantenendo richiami applicativi nelle sezioni pertinenti.

---

# Gap chiusi

Nessuno al momento.

---

# Regola di aggiornamento

Ogni gap deve terminare in uno dei seguenti stati:

- `OPEN`;
- `IN SYNTHESIS`;
- `RESOLVED EDITORIALLY`;
- `ESCALATED TO DOCTRINE REVIEW`;
- `DEFERRED WITH REASON`.

Non chiudere un gap perché “abbiamo scritto qualcosa”. Chiuderlo solo quando il relativo requisito didattico o conoscitivo è verificabilmente soddisfatto.
