# PROJECT STATUS

## Stato generale

ACTIVE — fasi 1–6 complete; primi 50 contenuti processati semanticamente; checkpoint 50 completato (fase 14 + fase 15 eseguite da Claude Code).

## Fase corrente

**CHECKPOINT 50 COMPLETATO.** Refactor KB (fase 14) e audit tassonomia (fase 15) eseguiti. Corpus non ancora completo: si riprende l'ingestione dal video 51 della queue corretta.

Esito dettagliato in `reviews/CHECKPOINT_050.md`.

## Corpus

- Video individuati: 468
- Contenuti processati: 50
- STUDIATO / integrati nella KB: 46
- ESCLUSO dalla dottrina attiva: 4
- Da processare: 418
- Corpus completo: NO

Contenuti esclusi finora:

- `Wk1Se1AeInw` — Jay Abraham;
- `5gKmC-QQlhA` — Laura Ries;
- `r8wi8vzz61w` — Al Ries;
- `TXGgnHLVhvA` — Dan Kennedy.

Sono contenuti ospite senza intervento sostanziale di Frank da consolidare nella dottrina attiva.

## Workflow attivo — v1.1

- CODEX / locale: acquisizione tecnica a batch.
- CHATGPT: revisione semantica e fasi 8–13 sui video acquisiti.
- CLAUDE CODE: fase 14 ogni 25 contenuti; fase 14 + fase 15 ogni 50; fasi 16–22 a corpus completo.

## Checkpoint

- Ultimo refactor KB completato: 50
- Refactor KB richiesto ora: NO
- Ultimo audit tassonomia: 50
- Audit tassonomia richiesto ora: NO
- Prossimo checkpoint dopo questo: 75 (fase 14); 100 (fase 14 + fase 15)
- Checkpoint Claude richiesto: NO

Handoff dettagliato: `reviews/CHECKPOINT_050.md`.

## Agente richiesto

**CHATGPT**

## Next Action

Codex deve acquisire il prossimo batch tecnico a partire dal primo video non completato della queue corretta (vedi sotto), preferibilmente ordine 51–75, poi restituire il controllo a ChatGPT (fasi 8–13) tramite `STATUS.md`.

## Prossimo contenuto dopo il checkpoint

`AAiq6RnCysE` — *Come comprano i ricchi? [Quelli veri]* (`01_mercato`).

Asset tecnici: NON PRESENTI.

Nota: `bHxjwGQQoUw` (precedente "prossimo video") ha già un'acquisizione tecnica parziale (`info.json` + `it-orig.json3`) da un batch precedente; dopo il riordino della fase 15 si trova più avanti nella queue (categoria `04_marketing`). Il lavoro parziale resta valido e verrà riutilizzato quando toccherà il suo turno.

## Blocchi / intervento umano

Nessun blocco semantico aperto sui primi 50 contenuti.

Note tecniche già risolte nel batch 26–50:

- due lezioni Ries senza transcript italiano sono state classificate come contenuti ospite ed escluse dalla dottrina attiva;
- il transcript Ferrero `GsmDyZQeYUM` è stato recuperato dal JSON3 italiano dopo l'errore di conversione;
- la lezione Dan Kennedy è stata identificata ed esclusa dalla dottrina attiva.

Esito fase 14 + fase 15 (checkpoint 50): vedi `reviews/CHECKPOINT_050.md`. Riclassificati 40/418 video non ancora studiati dal bucket generico `04_marketing` verso categorie più precise; riordinata l'intera coda non ancora studiata secondo la sequenza tematica dichiarata in `sources/queue/QUEUE.md`, con gli Shorts posposti ai video lunghi entro ciascuna categoria. Nessun video già `STUDIATO`/`ESCLUSO` è stato toccato.
