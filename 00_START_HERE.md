# START HERE

Questo repository serve a costruire una Knowledge Base viva e gerarchica del pensiero di Frank Merenda usando esclusivamente i contenuti del canale YouTube ufficiale `@FrankMerendaTV`.

Formalife non deve entrare nella Knowledge Base Merenda e non deve influenzarla. Formalife viene introdotta soltanto dalla fase 21.

## Prima di fare qualsiasi lavoro

Leggi, nell'ordine:

1. `MASTER_PLAN.md`
2. `system/RULES.md`
3. `STATUS.md`

Poi esegui esclusivamente la prossima azione indicata in `STATUS.md`, rispettando il ruolo assegnato.

## Ruoli

### Codex / strumenti locali

- Setup iniziale: fasi 1–6.
- Acquisizione tecnica a batch: fase 7 e supporto meccanico alle fasi 8 e 10.
- Recupera metadata, transcript, file normalizzati e keyframe candidati.
- Non esegue il merge semantico nella KB salvo istruzione esplicita.
- Quando gli asset del batch sono pronti, restituisce il controllo a ChatGPT tramite `STATUS.md`.

### ChatGPT

- È il processore semantico principale durante l'ingestione.
- Per ogni video già acquisito esegue la revisione semantica e le fasi 8–13.
- Individua incomprensioni sostanziali, decide quando l'analisi visuale è necessaria, distilla la conoscenza e aggiorna/riscrive la KB.
- Continua sui video già acquisiti fino al checkpoint Claude o fino a quando servono nuovi asset locali.

### Claude Code

- Fase 14 ogni 25 video completati.
- Fasi 14 + 15 ogni 50 video completati.
- Dopo il completamento dell'intero corpus: fasi 16–22.

## Regola fondamentale

I file elencati in `system/FROZEN_FILES.md` definiscono il sistema operativo del progetto e non devono essere modificati senza autorizzazione esplicita dell'utente.

Prima di terminare qualsiasi task, aggiorna sempre `STATUS.md`.
