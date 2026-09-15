# MERENDA ACQUISITION CLOSED

Stato: **LOCKED**

Data chiusura: 2026-09-15.
Checkpoint semantico finale: **313**.
Decisione: **KB Merenda sufficientemente satura**.

Questo file è un lock operativo deliberato.

Finché esiste:

- non acquisire video 314+;
- non usare il primo `DA STUDIARE` come next action;
- non creare batch Merenda per completezza;
- `scripts/ingest_video.py` deve terminare prima di selezionare un video;
- `sources/queue/next-batch.txt` deve restare vuoto.

I 155 residui sono un archivio intenzionale, non un backlog.

## Come si riapre

Solo dopo una decisione esplicita dell'utente su un **gap concreto e nominabile**:

1. documentare il gap e la ragione della riapertura;
2. aggiornare `STATUS.md`;
3. scegliere soltanto le fonti pertinenti al gap;
4. rimuovere questo lock in un commit dedicato;
5. popolare `next-batch.txt` soltanto con il micro-batch autorizzato.

La semplice presenza di contenuti residui non è una ragione valida per riaprire l'acquisizione.
