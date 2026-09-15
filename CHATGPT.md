# ChatGPT Instructions

Leggi 00_START_HERE.md e STATUS.md prima di lavorare.

## Stato corrente

La fase video generalista Merenda è chiusa per saturazione a 313. Se sources/queue/ACQUISITION_CLOSED.md esiste, ChatGPT non deve continuare sui residui 314+ salvo decisione esplicita dell'utente su un gap specifico.

Il progetto continua però con nuove fonti Merenda source-agnostic registrate in sources/merenda-sources/.

## Ruolo

ChatGPT è il processore semantico principale.

Per ogni nuova fonte Merenda:

1. verifica provenienza, autore/speaker e data quando disponibili;
2. acquisisci o usa il contenuto effettivo della fonte senza ricostruirlo dalla memoria;
3. leggi/ascolta integralmente la parte rilevante;
4. usa analisi visuale soltanto quando visuali, tabelle, diagrammi o slide aggiungono informazione;
5. distilla proposizioni, causalità, prescrizioni, condizioni, eccezioni, esempi, metriche e sequenze;
6. consulta la parte pertinente della KB;
7. valuta dedup, estensione o nuovo framework;
8. applica la prevalenza temporale solo in caso di vera incompatibilità;
9. MERGE, NOT APPEND: integra, compatta o riscrivi la KB;
10. assegna Weighted Novelty 0, 1 o 2;
11. crea la review canonica e aggiorna sources/merenda-sources/catalog.json;
12. aggiorna STATUS.md e valida il progetto.

## Principi

- La KB rappresenta la dottrina Merenda, non ciò che altri pensano di Merenda.
- Il formato della fonte non cambia la metodologia semantica.
- Formalife resta fuori dalla KB Merenda.
- Fonti esterne non-Merenda restano fuori da merenda/.
- In caso di reale contraddizione, prevale l'insegnamento Merenda più recente.
- Non trasformare esempi, numeri o provocazioni in regole generali.
- Canonizza il principio, non la provocazione.
- Non creare un nuovo file per ogni fonte.
- Le nuove fonti devono guadagnarsi il proprio posto nella KB tramite provenienza → comprensione → confronto → novelty → prevalenza → merge → verifica.
