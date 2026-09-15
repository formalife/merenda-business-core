# Video Phase Closure Audit — 313

Data: 15 settembre 2026.

## Scopo

Verificare che la fase video Merenda sia realmente chiusa e che il repository non contenga istruzioni operative stale capaci di riavviare accidentalmente l'acquisizione.

## Stato semantico verificato

- corpus catalogato: **468**
- processati semanticamente: **313**
- STUDIATO: **307**
- ESCLUSO: **6**
- residui intenzionali: **155**
- review presenti: **313**
- review mancanti rispetto ai processati: **0**
- review extra su contenuti non processati: **0**
- STUDIATO senza transcript Markdown: **0**
- posizioni queue 1–313 ancora aperte: **0**
- posizioni queue 314–468 già chiuse: **0**

Il primo residuo resta:
- posizione 314
- `asMedYJtd4I`
- stato `DA STUDIARE`

## Residui operativi trovati e corretti

### 1. next-batch stale

Prima dell'audit `sources/queue/next-batch.txt` conteneva ancora i tre URL del final probe 311–313.

Correzione: file svuotato.

### 2. Queue con istruzione di continuazione stale

L'intestazione di `QUEUE.md` diceva ancora di prendere il primo video non completato.

Correzione: intestazione sostituita con lo stato finale di saturazione e divieto di consumo automatico dei residui 314–468.

### 3. Script di ingestione ancora attivo

`scripts/ingest_video.py` avrebbe selezionato il primo residuo 314 se eseguito con `--acquire`.

Correzione:
- creato `sources/queue/ACQUISITION_CLOSED.md`;
- lo script termina immediatamente se il lock esiste.

### 4. VIDEO_INDEX non completamente sincronizzato

Audit per ID contro `sources/catalog.json`:

- **21** mismatch di stato;
- **25** mismatch di categoria.

Correzione: categoria e stato di tutte le 468 righe riallineati al catalogo senza modificare l'ordine storico dell'indice.

### 5. Validator legato all'ordine storico

Il validator precedente confrontava catalogo, queue e VIDEO_INDEX tramite `zip`, generando centinaia di warning quando la queue era stata legittimamente reprioritizzata.

Correzione: il validator ora controlla:
- stesso set di ID;
- unicità/contiguità delle posizioni;
- categoria e stato per ID;
- review esatte per tutti e soli i contenuti processati;
- transcript per tutti gli STUDIATO;
- lock di acquisizione;
- `next-batch.txt` vuoto;
- 1–313 chiusi e 314–468 residui;
- frozen contro il commit semantico finale 313;
- link locali e contaminazione della KB;
- contatori canonici in STATUS.

## File di ingresso aggiornati

Aggiornati per rendere impossibile interpretare i 155 residui come un invito a continuare:

- `00_START_HERE.md`
- `AGENTS.md`
- `CLAUDE.md`
- `CHATGPT.md`
- `scripts/README.md`
- `merenda/INDEX.md`
- `STATUS.md`

## Frozen

Nessuno dei cinque file frozen è stato modificato nella finalizzazione.

Il validator usa come baseline frozen il commit semantico finale:

`e505ba63cc5befd38db11a222c2eb2ffa10fabfa`

## Criterio di riapertura

I video 314–468 possono essere riaperti soltanto se:

1. emerge un gap concreto e nominabile;
2. l'utente autorizza esplicitamente la riapertura;
3. il gap viene documentato;
4. il lock viene rimosso deliberatamente;
5. viene definito un micro-batch specifico.

La completezza numerica 468/468 non è un obiettivo.
