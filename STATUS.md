# PROJECT STATUS

## Stato generale

**MERENDA VIDEO PHASE CLOSED — KB SUFFICIENTEMENTE SATURA.**

La fase di acquisizione e revisione video è chiusa al contenuto **313**. Il lock operativo è attivo in `sources/queue/ACQUISITION_CLOSED.md`.

## Contatori canonici

- Video individuati: 468
- Video completati: 307
- Video esclusi: 6
- Video rimanenti: 155
- Processati semanticamente: 313

I 155 residui (posizioni 314–468) sono **intenzionalmente non processati**. Non costituiscono un backlog da completare.

## Final probe 311–313

- 3/3 STUDIATO
- peso 2: **0**
- peso 1: **2**
- peso 0: **1**
- Weighted Novelty: **2/6 = 33,3%**
- nuovi framework: **0**

Report canonico: `reviews/MERENDA_SATURATION_313.md`.

## Chiusura acquisizione

**STOP acquisizione Merenda.**

Garanzie operative:

- `sources/queue/ACQUISITION_CLOSED.md` presente;
- `sources/queue/next-batch.txt` vuoto;
- `scripts/ingest_video.py` termina se il lock è presente;
- nessun 314+ deve essere acquisito per completezza;
- una riapertura richiede decisione esplicita dell'utente su un gap concreto e nominabile.

Primo residuo archiviato: posizione **314**, `asMedYJtd4I`.

## Integrità finale

- 313 contenuti processati = 313 file `.review.md`;
- nessuna review semantica 314+;
- nessun `STUDIATO` senza transcript Markdown;
- queue coerente con catalogo per ID, categoria e stato;
- VIDEO_INDEX riallineato al catalogo per ID, categoria e stato;
- file frozen non modificati dalla finalizzazione;
- Merenda KB resta separata da qualsiasi futura evidence base esterna.

Audit di chiusura: `reviews/VIDEO_PHASE_CLOSURE_AUDIT_313.md`.

## Source of Truth

La Merenda KB è ora il **doctrine layer stabile**.

Architettura successiva:

1. **Merenda KB** — dottrina sorgente;
2. **Evidence / External KB** — evidenze indipendenti;
3. **Strategy layer** — decisioni applicative dopo confronto e critica.

Nessuna fonte esterna deve essere inserita retroattivamente dentro `merenda/`.

## Checkpoint

- ultimo FASE 14 + 15: **300**
- final probe di saturazione: **313**
- chiusura video hardenizzata: **313**
- nessun checkpoint video ulteriore richiesto

## Next Action

**CHATGPT — solo dopo conferma del validator locale, progettare lo strato Evidence / External KB.**
