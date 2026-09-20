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

La scelta del target non può poggiare solo su descrizioni o interviste: deve combinare comportamento, economics, alternative, storia d'acquisto, risultati, raggiungibilità e trend. Complaint mining e test “perché hai scelto noi?” entrano nella sintesi VoC.

### D-009 — Front-end definito dalla barriera, non dal prezzo

**Stato: PROVISIONAL / SUPPORTATO DA PREVALENZA 2025**

Nel futuro manuale il front-end va insegnato come **riduzione della barriera d'ingresso**. Può usare prezzo, porzione di servizio, prova, garanzia o altra forma di risk reversal. Non va insegnato come sinonimo di forte sconto.

## Completato

### Fase 0 — DONE

- baseline iniziale verificato;
- governance frozen verificata;
- control plane `manual/` creato.

### Fase 1 — DONE

- 60/60 file sotto `merenda/` censiti;
- corpus interpretativo/provenance separato;
- inventario e gap register creati;
- gate Fase 1 soddisfatto.

### Fase 2 — progress corrente

- `00_fondamenti`: **3/3 file**, FND-001…FND-060 — 60 unità;
- `01_mercato`: **5/5 file**, MRC-001…MRC-053 — 53 unità;
- `02_posizionamento`: **4/4 file**, POS-001…POS-057 — 57 unità;
- `03_offerta`: **4/4 file**, OFF-001…OFF-071 — 71 unità;
- totale first-pass: **241 unità semantiche**;
- G-005 Voice of Customer: `IN SYNTHESIS`;
- G-006 economics early-curriculum: evidenza forte e ripetuta;
- G-008 lifecycle: rafforzato da durata naturale, seconda transazione, continuità e back-end;
- G-001 vendita: offerta e price argumentation devono essere standardizzate prima della trattativa.

Coverage Fase 2: **16/60 file; 4/11 sezioni**.

## Fase attiva

### Fase 2 — Semantic decomposition e KB-to-Manual Crosswalk

Obiettivo: estrarre da ogni nodo canonico ciò che il lettore deve imparare e saper fare, indipendentemente dalla struttura originale dei file.

## Ordine di lavorazione corrente

1. `00_fondamenti` — DONE;
2. `01_mercato` — DONE;
3. `02_posizionamento` — DONE;
4. `03_offerta` — DONE;
5. `04_marketing` — NEXT;
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

Decomporre `04_marketing` in `manual/crosswalk/04_marketing.md`, con focus su:

1. gerarchia della domanda e livelli di consapevolezza;
2. domanda posseduta, attiva e latente;
3. scelta canale subordinata a intento, target ed economics;
4. quattro modalità di marketing e ritmo;
5. continuità e frequenza di contatto;
6. riattivazione della base esistente;
7. testing creatività e isolamento delle variabili;
8. complessità utile vs moltiplicazione prematura delle variabili;
9. eventi/VIP experience come canale/asset quando pertinenti;
10. dipendenze da posizionamento, offerta, capacity ed economics.

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
