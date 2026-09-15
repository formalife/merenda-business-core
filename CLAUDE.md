# Claude Code Instructions

Leggi `00_START_HERE.md` prima di fare qualsiasi cosa.

## Stato corrente

La fase video Merenda è chiusa per saturazione a 313. I 155 residui non equivalgono a un corpus da completare automaticamente. Se `sources/queue/ACQUISITION_CLOSED.md` esiste, non richiedere nuovi batch e non interpretare `DA STUDIARE` come autorizzazione a proseguire.

## Ruolo durante l'ingestione

- Ogni 25 video completati: esegui fase 14.
- Ogni 50 video completati: esegui fase 14 e poi fase 15.
- Dopo il checkpoint, se il corpus non è completo:
  - restituisci il controllo a `CHATGPT` se gli asset del prossimo video sono già acquisiti;
  - altrimenti richiedi `CODEX` per il prossimo batch tecnico.

## Ruolo dopo il completamento del corpus

Esegui in ordine le fasi 16–22.

## Regole operative

- Aggiorna sempre `STATUS.md` prima di terminare una task.
- Non modificare i file congelati elencati in `system/FROZEN_FILES.md`.
- Durante i refactor usa la KB come materiale principale; consulta transcript grezzi solo quando serve a risolvere un problema specifico.
- Mantieni la KB semplice, gerarchica, leggibile e token-efficient.
- Non introdurre Formalife nella KB Merenda.
- Formalife entra soltanto dalla fase 21.
- MERGE, NON APPEND.

La procedura completa è definita in `MASTER_PLAN.md` e `system/RULES.md`.
