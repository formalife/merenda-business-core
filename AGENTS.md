# Codex Instructions

Leggi 00_START_HERE.md e STATUS.md prima di fare qualsiasi cosa.

## Stato corrente

La fase di acquisizione video generalista Merenda è chiusa. Se sources/queue/ACQUISITION_CLOSED.md esiste, Codex non deve acquisire altri video dalla queue storica, anche se contiene residui DA STUDIARE.

Questo lock non impedisce l'acquisizione tecnica di nuove fonti Merenda source-agnostic esplicitamente fornite o autorizzate dall'utente.

## Ruolo

Codex è principalmente il livello tecnico locale del progetto.

Per una nuova fonte Merenda:

1. identifica il formato e la provenienza;
2. conserva l'originale soltanto quando appropriato e utile alla verifica;
3. produce il contenuto normalizzato più affidabile possibile;
4. per audio/video genera transcript temporizzato quando serve;
5. estrae visuali soltanto quando cambiano o completano il significato;
6. registra gli asset nella convenzione sources/merenda-sources/<SOURCE_ID>/;
7. non esegue il merge semantico nella KB salvo istruzione esplicita;
8. restituisce il controllo al processore semantico.

## Regole operative

- Aggiorna STATUS.md quando il task modifica lo stato operativo.
- Non modificare i file congelati elencati in system/FROZEN_FILES.md.
- Non introdurre Formalife nella KB Merenda.
- Non forzare articoli, PDF o audio dentro sources/transcripts/.
- Non riaprire automaticamente i 155 video residui.
- Non creare un ingestor generico complesso finché i formati reali non dimostrano che serve.
- Mantieni gli asset tecnici minimali, verificabili e senza duplicazioni inutili.
- L'acquisizione tecnica non equivale a fonte STUDIATO.
