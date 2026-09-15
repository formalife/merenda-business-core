# MERENDA YOUTUBE ACQUISITION CLOSED

Stato: **LOCKED**

Data chiusura: 2026-09-15.
Checkpoint semantico finale: **313**.
Decisione: **KB video Merenda sufficientemente satura**.

Questo file è un lock operativo deliberato del corpus YouTube storico.

Finché esiste:

- non acquisire automaticamente video 314+;
- non usare il primo DA STUDIARE come next action;
- non creare batch YouTube per completezza;
- scripts/ingest_video.py deve terminare prima di selezionare un video;
- sources/queue/next-batch.txt deve restare vuoto.

I 155 residui sono un archivio intenzionale, non un backlog.

Questo lock **non blocca** nuove fonti Merenda source-agnostic fornite o autorizzate dall'utente. Tali fonti devono essere gestite separatamente in sources/merenda-sources/ e non devono modificare i contatori del corpus YouTube storico.

## Come si riapre il corpus YouTube residuo

Solo dopo una decisione esplicita dell'utente su un gap concreto e nominabile:

1. documentare il gap e la ragione della riapertura;
2. aggiornare STATUS.md;
3. scegliere soltanto i video pertinenti al gap;
4. rimuovere questo lock in un commit dedicato;
5. popolare next-batch.txt soltanto con il micro-batch autorizzato.

La semplice presenza di contenuti residui non è una ragione valida per riaprire l'acquisizione.
