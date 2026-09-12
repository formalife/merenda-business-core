# RULES

## 1. Fonte ammessa

La Knowledge Base Merenda deve derivare esclusivamente dai contenuti del canale YouTube ufficiale `@FrankMerendaTV`.

Non introdurre nella KB concetti provenienti da:

- altri marketer;
- libri esterni;
- blog esterni;
- memoria generale del modello;
- Formalife;
- precedenti strategie Formalife.

Conoscenze tecniche generali possono essere usate solo per eseguire il lavoro tecnico, non per arricchire artificialmente la dottrina Merenda.

## 2. Semplicità della KB

La KB deve essere principalmente Markdown leggibile da una persona.

Evitare schemi burocratici, campi ridondanti, stati epistemici complessi e strutture tecniche che non migliorano concretamente l'uso della KB.

## 3. Merge, non append

Un nuovo video non genera automaticamente un nuovo documento.

Prima di aggiungere contenuto:

1. individuare la sezione pertinente;
2. leggere solo ciò che serve;
3. integrare la nuova conoscenza;
4. eliminare ridondanze;
5. riscrivere quando una formulazione nuova è migliore.

## 4. Insegnamenti più recenti

Quando due insegnamenti sono realmente incompatibili, privilegiare quello più recente.

Il contenuto precedente può essere spostato in `archive/superseded/` se vale la pena conservarlo, ma non deve rimanere nella KB attiva come regola concorrente.

## 5. Transcript incerti

Correggere automaticamente solo quando il contesto rende la correzione ragionevolmente sicura.

Quando un errore o un'incomprensione riguarda un passaggio importante e non può essere risolto con sufficiente sicurezza, marcarlo chiaramente come `DA VERIFICARE MANUALMENTE` e riportarlo in `STATUS.md` se richiede intervento umano.

## 6. Ospiti

Prestare particolare attenzione a intro, outro e cambi di speaker per evitare di incorporare accidentalmente lunghi interventi di ospiti come insegnamento principale.

Non serve una struttura complessa di speaker attribution: serve attenzione contestuale.

## 7. Analisi visuale selettiva

Non analizzare ogni frame.

Usare transcript/audio per individuare segnali di contenuto visuale importante, per esempio riferimenti a:

- slide;
- grafici;
- schemi;
- tabelle;
- numeri;
- esempi mostrati a schermo;
- elementi che non risultano comprensibili dal solo audio.

In questi casi analizzare keyframe pertinenti e integrare l'informazione nella comprensione del video.

## 8. Formalife separata

Formalife non deve comparire nella KB Merenda né influenzarne struttura o contenuti prima della fase 21.

## 9. Routing token-efficient

Per consultare la KB seguire sempre il percorso minimo necessario:

1. `merenda/INDEX.md`;
2. README della sezione pertinente;
3. file specifici necessari.

Non leggere l'intera KB se non richiesto da una fase di audit/refactor.

Non leggere transcript grezzi salvo ingestione o necessità specifica.

## 10. Stato del progetto

`STATUS.md` è il segnalibro operativo.

Prima di terminare qualsiasi task, aggiornarlo con:

- stato corrente;
- agente richiesto;
- prossima azione;
- checkpoint;
- blocchi o richieste di intervento umano.

Non usarlo come diario storico: Git conserva la storia.

## 11. File congelati

Non modificare i file elencati in `system/FROZEN_FILES.md` senza autorizzazione esplicita dell'utente.
