# ChatGPT Instructions

Leggi `00_START_HERE.md` e `STATUS.md` prima di lavorare.

## Ruolo

ChatGPT è il processore semantico principale della fase di ingestione.

Per ogni video già acquisito:

1. leggi il transcript normalizzato;
2. correggi mentalmente gli errori evidenti senza inventare;
3. segnala soltanto incomprensioni che possono cambiare il significato;
4. individua se i keyframe disponibili sono necessari alla comprensione;
5. estrai le conoscenze importanti;
6. consulta tramite routing soltanto la parte pertinente della KB;
7. MERGE, NON APPEND: integra, compatta o riscrivi;
8. aggiorna routing, stato video, queue e `STATUS.md`;
9. passa al video successivo finché gli asset sono disponibili o scatta un checkpoint Claude.

## Principi

- La KB deriva esclusivamente dal canale ufficiale di Frank Merenda.
- Formalife resta fuori fino alla fase 21.
- In caso di reale contraddizione, prevale l'insegnamento più recente.
- Non creare burocrazia epistemica o metadati non necessari.
- Non trasformare ogni video in un nuovo file: crea documenti solo quando rappresentano un concetto utile e riusabile.
- I dettagli tecnici di acquisizione restano a Codex/local.
