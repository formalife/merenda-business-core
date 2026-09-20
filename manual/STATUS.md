# Manual Project Status

## Stato generale

**ACTIVE — FASE 2 / SEMANTIC DECOMPOSITION E KB-TO-MANUAL CROSSWALK**

Il publishing layer è inizializzato, la Fase 1 è chiusa e il progetto sta trasformando i nodi canonici in unità di conoscenza.

## Baseline iniziale

Doctrine layer baseline all'avvio del progetto manuale:

`93f8eae978fdffb55c5623ae06603e5895b71e11`

Data baseline: 2026-09-20.

Il baseline serve per auditabilità, non per congelare permanentemente il manuale a una versione vecchia. Prima di ogni fase sostanziale va verificato il `main` live.

## Decisioni correnti

### D-001 — Publishing layer separato

**Stato: CURRENT**

Il manuale vive sotto `manual/` e non modifica il ruolo canonico di `merenda/`.

### D-002 — Beginner-first

**Stato: CURRENT**

Il lettore target parte senza conoscenza pregressa strutturata di marketing. Il manuale deve introdurre termini, prerequisiti e causalità prima di richiederne l'uso.

### D-003 — Voce autoriale agnostica

**Stato: CURRENT**

Nel testo reader-facing non compaiono Frank Merenda, la KB, il Layer 1 o classificazioni di provenance. Il testo parla con voce autoriale unitaria.

### D-004 — Provenance preservata nel backend

**Stato: CURRENT**

Origine reale, temporalità e distinzione tra fonte primaria, assimilata e sintesi restano disponibili negli artefatti editoriali quando necessarie alla verifica.

### D-005 — Rewrite, not collage

**Stato: CURRENT**

I nodi canonici sono fonti di conoscenza, non blocchi da concatenare. Il manuale viene riscritto da zero a livello di prosa e architettura.

### D-006 — Nessuna scrittura massiva prima dei gate

**Stato: CURRENT**

Non si avvia la produzione sistematica dei capitoli finché inventario, semantic crosswalk, curriculum e gap closure non raggiungono i gate previsti dalla roadmap.

### D-007 — Crosswalk modulare

**Stato: CURRENT**

La Fase 2 usa un indice master `manual/KB_TO_MANUAL_CROSSWALK.md` e file modulari sotto `manual/crosswalk/`.

Le sezioni della KB vengono usate come unità di lavorazione, non come indice finale del manuale.

## Completato

### Fase 0 — DONE

- baseline iniziale verificato;
- governance frozen verificata;
- `manual/README.md` creato;
- `manual/ROADMAP.md` creato;
- `manual/STATUS.md` creato;
- `manual/MANUAL_CONTRACT.md` creato.

### Fase 1 — DONE

- 60/60 file sotto `merenda/` censiti;
- separati doctrine, synthesis, routing, case/example e reference;
- corpus di supporto interpretativo/provenance definito;
- `manual/CORPUS_INVENTORY.md` creato;
- `manual/MANUAL_GAPS.md` creato;
- gap iniziali classificati;
- gate Fase 1 soddisfatto.

### Fase 2 — progress corrente

- `manual/KB_TO_MANUAL_CROSSWALK.md` creato;
- `00_fondamenti` decomposto: **3/3 file covered**;
- create **60 unità semantiche FND-001…FND-060**;
- marcati principi generativi, gate, feedback loop, economics cross-cutting, diagnostica e caveat temporali;
- confermata la necessità di introdurre la definizione estesa di marketing e una base di economics molto presto nel futuro curriculum.

Coverage Fase 2: **3/60 file; 1/11 sezioni**.

## Fase attiva

### Fase 2 — Semantic decomposition e KB-to-Manual Crosswalk

Obiettivo: estrarre da ogni nodo canonico ciò che il lettore deve imparare e saper fare, indipendentemente dalla struttura originale dei file.

## Ordine di lavorazione corrente

1. `00_fondamenti` — DONE;
2. `01_mercato` — NEXT;
3. `02_posizionamento`;
4. `03_offerta`;
5. `04_marketing`;
6. `05_acquisizione`;
7. `06_vendita`;
8. `07_copy_comunicazione`;
9. `08_brand`;
10. `09_business`;
11. `10_casi_studio`;
12. cross-section deduplication e dependency pass;
13. aggiornamento gap register;
14. verifica gate Fase 2.

L'ordine sopra è **ordine di decomposizione**, non curriculum finale.

## Next Action

Decomporre `01_mercato` in `manual/crosswalk/01_mercato.md`, con focus su:

1. mercato, target e identificabilità;
2. domanda, raggiungibilità e capacità di acquisto;
3. cliente economicamente desiderabile vs semplice buyer;
4. appropriatezza, cost-to-serve, probabilità di successo e LTV;
5. clienti alto-spendenti e comportamento economico;
6. gate prima del lancio;
7. segnali di Voice of Customer già presenti ma dispersi;
8. dipendenze dagli economics fondamentali;
9. duplicazioni con FND-025, FND-032 e FND-042.

## Gap aperti prioritari

- G-001 — vendita end-to-end — P1;
- G-002 — libreria casi — P1;
- G-003 — doctrine/provenance map — P1;
- G-006 — economics da introdurre prima nel curriculum — P1.

Gli altri gap restano registrati in `manual/MANUAL_GAPS.md`.

## Blocchi

Nessun blocco corrente.

## Regola di handoff

Chiunque riprenda questo lavoro deve leggere, nell'ordine:

1. `manual/ROADMAP.md`;
2. questo file;
3. `manual/MANUAL_CONTRACT.md`;
4. `manual/CORPUS_INVENTORY.md`;
5. `manual/MANUAL_GAPS.md`;
6. `manual/KB_TO_MANUAL_CROSSWALK.md`;
7. il file crosswalk della sezione attiva e quello precedente quando serve per dedup;
8. solo dopo i nodi canonici necessari.

Al termine deve aggiornare questo file con fase corrente e prossima azione.
