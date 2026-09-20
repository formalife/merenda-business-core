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
**Stato: OPEN**

### Evidenza

Il semantic audit segnala che le tecniche esistono ma sono disperse fra:

- analisi dei clienti migliori;
- complaint mining;
- testimonianze;
- query e intento;
- competitor;
- storia di acquisto;
- segmentazione e appropriatezza.

### Impatto sul manuale

Il lettore non può ricevere soltanto la regola “capisci il mercato”: deve avere un processo per raccogliere evidenza senza confondere opinioni del founder e comportamento del cliente.

### Azione prevista

Prima tentare una sintesi completa con il corpus esistente. Se mancano passaggi indispensabili, classificare precisamente ciò che manca prima di valutare nuova acquisizione.

---

## G-006 — Economics fondamentali collocati troppo tardi per il curriculum

**Priorità: P1**  
**Tipo: CURRICULUM GAP**  
**Stato: OPEN**

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

La KB presuppone spesso familiarità con termini quali CAC, LTV, payback, front-end, back-end, direct response, awareness, funnel, positioning, referral e altri.

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

### Impatto sul manuale

Senza un disegno unitario, retention, seconda vendita, referral, reputazione e riattivazione rischiano di sembrare tattiche separate invece di un ciclo economico unico.

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
