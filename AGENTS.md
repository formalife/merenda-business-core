# Codex Instructions

Leggi `00_START_HERE.md` prima di fare qualsiasi cosa.

## Stato corrente

La fase di acquisizione video Merenda è chiusa. Se `sources/queue/ACQUISITION_CLOSED.md` esiste, Codex **non deve acquisire altri video**, anche se la queue contiene residui `DA STUDIARE`. Le capacità sotto restano valide solo se `STATUS.md` autorizza esplicitamente una riapertura.

## Ruolo

Codex è principalmente il livello tecnico locale del progetto.

1. Completa le fasi 1–6 se non sono complete.
2. Acquisisci asset video solo quando `STATUS.md` lo autorizza esplicitamente e il lock di acquisizione è stato rimosso; non consumare automaticamente i residui della queue.
3. Esegui la fase 7 e il supporto meccanico necessario alle fasi 8 e 10.
4. Non consumare contesto per distillare o riscrivere la Knowledge Base, salvo istruzione esplicita.
5. Quando il batch è pronto, aggiorna `STATUS.md` indicando `CHATGPT` come agente richiesto.
6. Se ChatGPT segnala un asset mancante o una verifica locale necessaria, acquisiscilo e restituisci il controllo a ChatGPT.

## Regole operative

- Aggiorna sempre `STATUS.md` prima di terminare una task.
- Non modificare i file congelati elencati in `system/FROZEN_FILES.md`.
- Non introdurre Formalife nella KB Merenda.
- I transcript appartengono a `sources/transcripts/`.
- Conserva i file grezzi necessari alla verifica, ma evita duplicazioni inutili.
- L'acquisizione anticipata non equivale a video completato.
- Il video diventa `STUDIATO` solo dopo il merge semantico eseguito dal processore indicato in `STATUS.md`.
- Usa analisi visuale selettiva: estrai keyframe pertinenti, non il video frame per frame.

La procedura completa è definita in `MASTER_PLAN.md` e `system/RULES.md`.
