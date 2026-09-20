# Manual Project Status

## Stato generale

**ACTIVE — FASE 1 / ARCHITECTURE REVIEW E CORPUS INVENTORY**

Il publishing layer è stato inizializzato e la roadmap è attiva.

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

## Completato

- baseline iniziale verificato;
- governance frozen verificata;
- `manual/README.md` creato;
- `manual/ROADMAP.md` creato;
- `manual/STATUS.md` creato;
- `manual/MANUAL_CONTRACT.md` avviato.

## Fase attiva

### Fase 1 — Architecture Review e corpus inventory

Obiettivo immediato: costruire un censimento esaustivo dei file rilevanti e assegnare a ciascuno un ruolo editoriale.

## Next Action

1. censire ricorsivamente `merenda/`;
2. registrare per ogni file path, sezione, tipo e ruolo editoriale;
3. includere documenti root/audit/provenance che cambiano l'interpretazione del corpus;
4. creare `manual/CORPUS_INVENTORY.md`;
5. creare la prima versione di `manual/MANUAL_GAPS.md`;
6. verificare il gate della Fase 1.

## Blocchi

Nessun blocco corrente.

## Regola di handoff

Chiunque riprenda questo lavoro deve leggere, nell'ordine:

1. `manual/ROADMAP.md`;
2. questo file;
3. `manual/MANUAL_CONTRACT.md`;
4. gli output della fase attiva;
5. solo dopo i nodi canonici necessari.

Al termine deve aggiornare questo file con fase corrente e prossima azione.
