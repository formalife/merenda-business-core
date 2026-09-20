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

### D-008 — Ricerca di mercato come evidenza multi-fonte

**Stato: PROVISIONAL / DA VALIDARE NEL CROSS-SECTION PASS**

La sezione mercato conferma che la scelta del target non può poggiare solo su descrizioni o interviste: deve combinare comportamento, economics, alternative attuali, storia d'acquisto, risultati, raggiungibilità e trend. Il processo VoC completo resta da sintetizzare.

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
- `01_mercato` decomposto: **5/5 file covered**;
- create **53 unità semantiche MRC-001…MRC-053**;
- totale first-pass: **113 unità semantiche**;
- G-005 Voice of Customer portato a `IN SYNTHESIS`;
- G-006 economics early-curriculum rafforzato;
- aggiunta la durata naturale della relazione come dipendenza del lifecycle e degli economics.

Coverage Fase 2: **8/60 file; 2/11 sezioni**.

## Fase attiva

### Fase 2 — Semantic decomposition e KB-to-Manual Crosswalk

Obiettivo: estrarre da ogni nodo canonico ciò che il lettore deve imparare e saper fare, indipendentemente dalla struttura originale dei file.

## Ordine di lavorazione corrente

1. `00_fondamenti` — DONE;
2. `01_mercato` — DONE;
3. `02_posizionamento` — NEXT;
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

Decomporre `02_posizionamento` in `manual/crosswalk/02_posizionamento.md`, con focus su:

1. differenza reale vs claim;
2. focus e categoria;
3. meccanismo/metodo/processo come fonti di differenziazione;
4. quattro filtri per scegliere il focus di decollo;
5. difendibilità e percorso finanziabile;
6. rischio di diluizione da estensioni;
7. family brand vs multibrand e prevalenza temporale;
8. casi/esempi di differenziazione;
9. dipendenze da mercato, economics, offerta e copy;
10. segnali utili a G-005 ricerca e a G-004 brand.

## Gap aperti prioritari

- G-001 — vendita end-to-end — P1;
- G-002 — libreria casi — P1;
- G-003 — doctrine/provenance map — P1;
- G-006 — economics da introdurre prima nel curriculum — P1.

G-005 è `IN SYNTHESIS`. Gli altri gap restano registrati in `manual/MANUAL_GAPS.md`.

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
7. il file crosswalk della sezione attiva e quelli precedenti quando serve per dedup;
8. solo dopo i nodi canonici necessari.

Al termine deve aggiornare questo file con fase corrente e prossima azione.
