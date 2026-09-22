# RULES

## 1. Fonte ammessa e provenance

La Knowledge Base è **Merenda-centered**, ma non è più limitata esclusivamente ai contenuti del canale YouTube ufficiale `@FrankMerendaTV`.

Le fonti entrano nel doctrine layer in due modi distinti:

1. **MERENDA PRIMARY** — contenuti direttamente attribuibili a Frank Merenda;
2. **ASSIMILATED** — fonti, autori o doctrine esterne che il founder autorizza esplicitamente a fondere nella KB perché aumentano completezza, precisione o operatività del sistema.

Per ogni fonte assimilata è obbligatorio:

- preservare l'autore/provenance reale;
- non attribuire a Frank ciò che proviene da altri;
- integrare semanticamente nel nodo canonico pertinente, evitando sezioni-parcheggio per autore quando non servono;
- distinguere, quando materialmente utile, fra insegnamento Merenda, insegnamento assimilato e sintesi della KB;
- applicare `MERGE, NOT APPEND`: la fonte esterna non genera automaticamente una dottrina parallela.

Una nuova fonte esterna non entra automaticamente nella KB. Serve una decisione esplicita di scope del founder oppure deve restare `DEFERRED_EXTERNAL_GENERAL_UPDATE` / fuori dal doctrine layer.

Formalife resta esclusa come fonte dottrinale automatica: i risultati Layer 2 possono evidenziare gap, ma richiedono una review Layer 1 separata prima di diventare principio generale.

Conoscenze tecniche generali del modello possono essere usate per eseguire il lavoro tecnico, non per arricchire artificialmente la dottrina senza provenance.

## 2. Semplicità della KB

La KB deve essere principalmente Markdown leggibile da una persona.

Evitare schemi burocratici, campi ridondanti, stati epistemici complessi e strutture tecniche che non migliorano concretamente l'uso della KB.

## 3. Merge, non append

Una nuova fonte non genera automaticamente un nuovo documento.

Prima di aggiungere contenuto:

1. individuare la sezione pertinente;
2. leggere solo ciò che serve;
3. integrare la nuova conoscenza;
4. eliminare ridondanze;
5. riscrivere quando una formulazione nuova è migliore;
6. preservare la provenance quando cambia l'autorità o il significato del claim.

Una doctrine assimilata può giustificare un refactor strutturale quando colma un gap sistemico o rende il dominio più coerente, ma il risultato finale deve essere una KB unica e navigabile, non due sistemi affiancati.

## 4. Insegnamenti più recenti e conflitti fra fonti

Quando due insegnamenti Merenda sono realmente incompatibili, privilegiare quello più recente.

Quando un insegnamento Merenda e una fonte assimilata differiscono:

1. non applicare automaticamente la regola temporale fra autori diversi;
2. confrontare scope, causalità, condizioni, evidenza e funzione nel sistema;
3. mantenere entrambi solo se descrivono condizioni realmente diverse;
4. se serve una riconciliazione, marcarla come **SYNTHESIS** invece di attribuirla a una singola fonte;
5. se il conflitto resta materiale e irrisolto, dichiararlo e non nasconderlo.

Il contenuto Merenda precedente chiaramente superseded può essere spostato in `archive/superseded/` se vale la pena conservarlo, ma non deve rimanere nella KB attiva come regola concorrente.

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

In questi casi analizzare keyframe pertinenti e integrare l'informazione nella comprensione della fonte.

## 8. Formalife separata

Formalife non deve comparire nella KB Merenda come fonte di doctrine né influenzarne automaticamente struttura o contenuti.

Formalife può mettere alla prova Layer 1 e rendere visibile un gap. La promozione di una lezione Formalife a doctrine generale richiede una review Layer 1 separata ed esplicita.

## 9. Routing token-efficient

Per consultare la KB seguire sempre il percorso minimo necessario:

1. `REASONING_KERNEL.md` per task strategico/diagnostico;
2. routing semantico/strutturale pertinente;
3. `merenda/INDEX.md` e README della sezione quando serve espansione;
4. file o sezione canonica specifica necessaria.

Non leggere l'intera KB se non richiesto da una fase di audit/refactor.

Non leggere transcript grezzi salvo ingestione o necessità specifica.

La doctrine specialistica più precisa o contestuale prevale sempre sul kernel e sui documenti di routing.

## 10. Stato del progetto

`STATUS.md` è il segnalibro operativo.

Prima di terminare qualsiasi task sostanziale, aggiornarlo con:

- stato corrente;
- prossima azione;
- checkpoint;
- blocchi o richieste di intervento umano quando esistono.

Non usarlo come diario storico: Git conserva la storia.

## 11. File congelati

Non modificare i file elencati in `system/FROZEN_FILES.md` senza autorizzazione esplicita dell'utente.

Quando il founder autorizza una modifica a un file congelato, limitare il cambiamento allo scope approvato e verificare la coerenza con gli altri file di governo.
