# Codex Instructions

Leggi `00_START_HERE.md` prima di fare qualsiasi cosa.

## Ruolo

1. Completa le fasi 1–6 se non sono complete.
2. Esegui le fasi 7–13 per ogni video della queue.
3. Fermati quando `STATUS.md` richiede un checkpoint Claude.
4. Dopo il checkpoint Claude, riprendi dal primo video non completato.
5. Continua fino al completamento dell'intero corpus.

## Regole operative

- Aggiorna sempre `STATUS.md` prima di terminare una task.
- Non modificare i file congelati elencati in `system/FROZEN_FILES.md`.
- Non introdurre Formalife nella KB Merenda.
- I transcript appartengono a `sources/transcripts/`.
- La conoscenza consolidata appartiene a `merenda/`.
- Segui il routing gerarchico; non caricare inutilmente l'intera KB.
- MERGE, NON APPEND: integra, compatta, riscrivi, evita duplicazioni.
- In caso di contraddizione reale, privilegia l'insegnamento più recente.
- Segnala solo le incomprensioni del transcript che possono cambiare il significato.
- Esegui analisi visuale selettiva quando audio/transcript indicano che è utile.

La procedura completa è definita in `MASTER_PLAN.md` e `system/RULES.md`.
