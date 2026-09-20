# Manual Project Roadmap

## Objective

Trasformare l'intera conoscenza utile del doctrine layer in un manuale teorico-operativo coerente, progressivo e studiabile da un lettore che parte da zero nel marketing.

Il progetto deve ottimizzare contemporaneamente per:

- completezza semantica;
- ordine pedagogico;
- coerenza causale;
- applicabilità operativa;
- minima ridondanza;
- tracciabilità interna;
- indipendenza della prosa finale dalle fonti personali originarie.

## Non-obiettivi

Il progetto non deve:

- trasformare la tassonomia corrente della KB nell'indice del libro senza riesame;
- fare copy-paste o semplice merge dei nodi;
- perdere provenance o prevalenza temporale nel backend editoriale;
- modificare la dottrina canonica solo per esigenze narrative;
- riempire il manuale di riferimenti interni alla KB;
- sacrificare i prerequisiti per accorciare artificialmente il percorso.

---

# Fase 0 — Control plane e baseline

**Stato: DONE**

## Scopo

Creare una memoria persistente del progetto indipendente dalla chat.

## Output

- `manual/README.md`
- `manual/ROADMAP.md`
- `manual/STATUS.md`
- `manual/MANUAL_CONTRACT.md`
- baseline iniziale del doctrine layer

## Gate di completamento

La roadmap, lo stato e le regole editoriali sono versionati nel repository e ogni task futuro può ripartire da essi.

---

# Fase 1 — Architecture Review e corpus inventory

**Stato: DONE**

## Scopo

Capire esattamente che cosa deve essere trasformato in materiale didattico, senza assumere che ogni file abbia lo stesso ruolo o debba comparire nel manuale.

## Attività

1. censire tutti i nodi canonici in `merenda/`;
2. separare nodi specialistici, sintesi, router, README, casi ed esempi;
3. censire i documenti di governance/provenance che influenzano interpretazione e temporalità;
4. classificare ogni file come:
   - SOURCE OF DOCTRINE;
   - SYNTHESIS;
   - ROUTING/GOVERNANCE;
   - CASE/EXAMPLE;
   - PROVENANCE/AUDIT;
   - NON-MANUAL;
5. individuare duplicazioni controllate, sovrapposizioni e gap già noti;
6. creare un inventario completo e verificabile.

## Output

- `manual/CORPUS_INVENTORY.md`
- `manual/MANUAL_GAPS.md` iniziale
- eventuale aggiornamento del `MANUAL_CONTRACT.md`

## Gate di completamento

Ogni nodo rilevante della KB ha una classificazione editoriale esplicita e non esiste un file canonico non considerato.

**Gate soddisfatto: 60/60 file sotto `merenda/` censiti e classificati; corpus interpretativo/provenance separato; gap iniziali registrati.**

---

# Fase 2 — Semantic decomposition e KB-to-Manual Crosswalk

**Stato: IN PROGRESS**

## Scopo

Trasformare i documenti della KB in unità di conoscenza indipendenti dalla loro collocazione originale.

## Unità da estrarre

- definizioni;
- principi;
- causalità;
- prerequisiti;
- regole decisionali;
- procedure;
- metriche;
- errori tipici;
- eccezioni/caveat;
- esempi;
- casi;
- dipendenze fra concetti.

## Regola

Non si riassume il file. Si estrae **che cosa il lettore deve imparare e saper fare**.

## Struttura operativa scelta

Il crosswalk sarà **modulare per sezione**, con un indice master.

Motivo: un singolo file renderebbe più difficile controllare copertura, review e aggiornamenti. La modularità segue le sezioni della KB soltanto come unità di lavorazione; non implica che il curriculum finale conserverà la stessa tassonomia.

## Output

- `manual/KB_TO_MANUAL_CROSSWALK.md` come indice e coverage master;
- directory `manual/crosswalk/` con un file per sezione canonica;
- mappa dei concetti duplicati con una sola futura casa primaria nel manuale;
- coverage status per ogni nodo canonico.

## Gate di completamento

Ogni unità dottrinale rilevante ha almeno una destinazione editoriale candidata e ogni nodo canonico è marcato come coperto, escluso motivatamente o ancora aperto.

---

# Fase 3 — Curriculum e architettura didattica

**Stato: NOT STARTED**

## Scopo

Definire l'ordine in cui una persona inesperta deve apprendere il sistema.

## Principio

L'indice finale nasce dalle **dipendenze cognitive e causali**, non dalle cartelle correnti della KB.

## Attività

1. definire learning outcomes finali;
2. costruire prerequisite graph;
3. raggruppare le unità semantiche in parti, moduli e capitoli;
4. verificare che ogni capitolo presupponga solo concetti già introdotti;
5. distribuire casi, esercizi ed esempi nel punto in cui servono;
6. evitare capitoli enciclopedici che mescolano livelli differenti.

## Output

- `manual/MANUAL_CURRICULUM.md`
- indice ragionato versione 1;
- prerequisite map;
- coverage check contro il crosswalk.

## Gate di completamento

Il curriculum copre l'intero corpus rilevante senza prerequisiti mancanti e può essere percorso da zero fino alla diagnosi e progettazione end-to-end di un business.

---

# Fase 4 — Gap closure e sintesi mancanti

**Stato: NOT STARTED**

## Scopo

Chiudere i buchi che impedirebbero al manuale di essere realmente autosufficiente.

## Gap iniziali già noti dal semantic audit

- processo vendita end-to-end;
- casi studio organizzati come libreria didattica;
- doctrine/provenance map interna;
- sintesi organica del brand;
- processo Voice of Customer / ricerca di mercato.

## Regola

Prima distinguere:

- **EDITORIAL GAP** — la conoscenza esiste ma è dispersa: si sintetizza nel publishing layer;
- **DOCTRINAL GAP** — la conoscenza canonica non basta: si registra e si valuta separatamente se serva nuovo lavoro sul doctrine layer.

## Output

- `manual/MANUAL_GAPS.md` aggiornato;
- sintesi editoriali necessarie;
- eventuali task canonici separati, solo se realmente indispensabili.

## Gate di completamento

Nessun capitolo fondamentale dipende da conoscenza implicita o dispersa che un principiante non potrebbe ricostruire autonomamente.

---

# Fase 5 — Chapter specs

**Stato: NOT STARTED**

## Scopo

Progettare ogni capitolo prima della prosa lunga.

## Ogni chapter spec deve contenere

- domanda a cui risponde;
- risultato di apprendimento;
- prerequisiti;
- concetti obbligatori;
- principio causale centrale;
- errori da prevenire;
- procedura/decision framework;
- metriche quando pertinenti;
- esempi/casi da usare;
- collegamenti ai capitoli precedenti e successivi;
- fonti canoniche backend;
- criteri di completezza.

## Output

- directory `manual/chapter-specs/`

## Gate di completamento

Ogni capitolo previsto dal curriculum ha una spec approvabile e nessuna unità critica del crosswalk resta senza casa.

---

# Fase 6 — Drafting del manuale

**Stato: NOT STARTED**

## Scopo

Riscrivere l'intero sistema in voce autoriale unitaria.

## Standard di scrittura

Ogni capitolo, salvo eccezioni motivate, deve seguire questa progressione:

1. problema o decisione reale;
2. modello mentale;
3. definizioni;
4. causalità e dipendenze;
5. regole diagnostiche;
6. procedura operativa;
7. errori ed eccezioni;
8. metriche/evidenza;
9. esempio o caso;
10. sintesi applicativa.

## Output

- directory `manual/draft/`

## Gate di completamento

Tutti i capitoli esistono in prima versione e rispettano chapter specs, curriculum e coverage map.

---

# Fase 7 — Audit didattico, dottrinale e operativo

**Stato: NOT STARTED**

## Scopo

Dimostrare che il manuale è corretto e utilizzabile, non soltanto ben scritto.

## Audit obbligatori

### Coverage audit

Ogni conoscenza rilevante della KB è coperta o esclusa motivatamente.

### Doctrine audit

Nessuna semplificazione del manuale contraddice il nodo canonico prevalente.

### Beginner audit

Il testo non presuppone concetti non ancora spiegati.

### Operational audit

Il lettore può trasformare i concetti in decisioni, procedure, test e metriche.

### Redundancy audit

Ogni concetto ha una casa primaria e le ripetizioni residue hanno funzione didattica esplicita.

### Provenance/copyright audit

La prosa finale è realmente riscritta e non presenta come appartenente a un singolo autore ciò che deriva da fonti assimilate diverse.

## Output

- `manual/AUDIT.md`
- backlog di correzione chiuso prima della finalizzazione.

## Gate di completamento

Nessun finding P0/P1 aperto.

---

# Fase 8 — Finalizzazione e release

**Stato: NOT STARTED**

## Scopo

Trasformare il draft validato in un'opera unica e pubblicabile/studiabile.

## Attività

- uniformare terminologia e voce;
- consolidare cross-reference;
- costruire glossario;
- costruire indice analitico;
- finalizzare esercizi/checklist/strumenti;
- finalizzare casi end-to-end;
- rimuovere residue tracce del backend editoriale;
- produrre versione master.

## Output

- `manual/final/`
- release del manuale;
- snapshot della coverage map usata per la release.

## Gate di completamento

Il manuale può essere studiato senza accesso alla KB originale e resta internamente riconducibile alla KB tramite gli artefatti editoriali.

---

# Regola di avanzamento

Una fase passa a `DONE` soltanto quando il suo gate è soddisfatto.

Non iniziare la scrittura massiva dei capitoli per entusiasmo o pressione di velocità se inventario, crosswalk, curriculum e gap closure non sono abbastanza solidi.

La priorità è:

**non perdere conoscenza → non perdere causalità → non perdere il lettore.**
