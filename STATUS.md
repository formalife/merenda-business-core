# PROJECT STATUS

## Stato generale

**MERENDA BUSINESS CORE — LAYER 1 OPERATIONAL. CURRENT KNOWN CORPUS EXHAUSTED; FINAL SEMANTIC AUDIT COMPLETED. MANUAL PUBLISHING PROJECT ACTIVE.**

Il progetto resta il **Layer 1** del sistema aziendale: doctrine layer, routing decisionale e motore di diagnosi.

Nome canonico del progetto: **Merenda Business Core**.

Nome repository previsto: `merenda-business-core`.

La fase video generalista è chiusa per saturazione al contenuto 313. Il lock operativo resta attivo in `sources/queue/ACQUISITION_CLOSED.md` e continua a impedire l'acquisizione automatica dei residui 314–468.

Il corpus source-agnostic attualmente disponibile è processato fino a `FM-SRC-0166`: 166 fonti registrate, 166 studiate, 0 pending.

Il checkpoint semantico di maturità è documentato in:

`reviews/FINAL_SEMANTIC_AUDIT.md`

Il Layer 1 resta disponibile per la ricostruzione zero-based di Formalife. La **priorità operativa corrente richiesta dal founder** è però il progetto editoriale sotto `manual/`, che trasforma la KB canonica in un manuale teorico-operativo beginner-first senza modificare il ruolo canonico di `merenda/`.

Contratto e protocollo Layer 1 / Layer 2:

- `LAYER1_CONTRACT.md`
- `FORMALIFE_REBUILD_PROTOCOL.md`

## Progetto manuale attivo

Publishing layer:

`manual/`

Control plane obbligatorio:

- `manual/README.md`
- `manual/ROADMAP.md`
- `manual/STATUS.md`
- `manual/MANUAL_CONTRACT.md`

Stato corrente:

**FASE 2 — SEMANTIC DECOMPOSITION E KB-TO-MANUAL CROSSWALK.**

La Fase 1 ha censito e classificato 60/60 file sotto `merenda/` e ha registrato i gap editoriali iniziali.

Il master crosswalk è stato inizializzato e `00_fondamenti` è completo al primo pass semantico: **3/60 file coperti, 1/11 sezioni, 60 unità semantiche FND-001…FND-060**.

Il publishing layer non è dottrina canonica. `merenda/` resta l'unica sede canonica della dottrina.

## Contatori canonici — corpus YouTube storico

- Video individuati: 468
- Video completati: 307
- Video esclusi: 6
- Video rimanenti: 155
- Processati semanticamente: 313

I 155 residui sono intenzionalmente non processati e non costituiscono backlog.

## Contatori canonici — layer source-agnostic

Le quattro etichette seguenti mantengono il naming storico richiesto dal validator. I contatori includono l'intero layer source-agnostic autorizzato, quindi non implicano che ogni record sia direttamente attribuibile a Frank Merenda.

- Nuove fonti Merenda registrate: 166
- Nuove fonti Merenda studiate: 166
- Nuove fonti Merenda escluse: 0
- Nuove fonti Merenda da processare: 0

Questi contatori sono separati dal corpus YouTube storico.

Il layer non contiene esclusivamente fonti direttamente attribuibili a Frank Merenda. `sources/merenda-sources/collections.json` distingue il trattamento della fonte.

Categorie operative rilevanti:

- `MERENDA_PRIMARY` — fonte direttamente attribuibile a Frank Merenda;
- `ASSIMILATED_AS_MERENDA_BY_USER` — autore reale preservato, contenuto assimilato semanticamente per istruzione esplicita dell'utente;
- `DEFERRED_EXTERNAL_GENERAL_UPDATE` — materiale non fuso automaticamente nella KB.

Le collezioni Marketing Automation Facile / Moreno Bonechi e jAI Premium / Jay Abraham, Max Bernstein, Michael Simmons sono assimilate per istruzione utente. I relativi principi non devono essere falsamente attribuiti a Frank.

## Source layer

Registry canonico:

`sources/merenda-sources/catalog.json`

Convenzione per-source:

`sources/merenda-sources/FM-SRC-0001/`

Ogni fonte può conservare, quando appropriato:

- originale o riferimento stabile;
- contenuto normalizzato analizzabile;
- review canonica;
- metadata e limiti di provenienza.

Non è obbligatorio archiviare integralmente materiale protetto quando basta un riferimento stabile più il contenuto necessario alla verifica.

## Invarianti Layer 1

- `merenda/` resta l'unico doctrine layer canonico del progetto;
- `manual/` è publishing layer derivato e non prevale sulla dottrina canonica;
- la KB è Merenda-centered ma può contenere estensioni assimilate **solo quando lo scope lo autorizza esplicitamente**;
- la provenance reale non viene mai falsificata;
- una fonte assimilata non viene attribuita a Frank soltanto perché è stata integrata nel doctrine layer;
- le nuove fonti non vengono aggiunte automaticamente come nuovi nodi: `MERGE, NOT APPEND`;
- il lock YouTube resta attivo;
- `sources/catalog.json`, `VIDEO_INDEX.md` e queue storica non vengono riconvertiti;
- i cinque file frozen restano invariati;
- ricerca esterna generale non autorizzata non viene mescolata silenziosamente dentro `merenda/`;
- Formalife non entra come dottrina nel Layer 1;
- risultati o esperimenti Formalife non diventano automaticamente principi canonici;
- il Layer 1 può invece interrogare e guidare il Layer 2.

## Modalità Layer 2

Formalife verrà ricostruita secondo modalità **first meeting / zero-based reconstruction** quando il lavoro operativo sul Layer 2 riprende.

Principio:

**ripartire da zero nelle decisioni, non da zero nella conoscenza.**

Gli elementi Formalife vengono classificati come:

- FACT;
- ASSET;
- CONSTRAINT;
- HYPOTHESIS;
- LEGACY DECISION;
- OBSERVATION;
- OPEN QUESTION.

Una decisione esistente non viene trattata automaticamente come vincolo.

Il Layer 1 deve essere libero di mantenere, modificare o scartare prodotti, target, prezzi, canali, processi e offerte esistenti quando la diagnosi lo richiede.

La ricostruzione segue il ciclo:

**domanda → risposta → classificazione → verifica → diagnosi → decisione provvisoria → domanda successiva.**

## Provenienza e review

Ogni nuova fonte autorizzata deve avere provenance sufficiente, contenuto analizzabile, review, Weighted Novelty e routing finale.

In caso di reale incompatibilità fra fonti direttamente attribuibili a Merenda, prevale l'insegnamento più recente dopo aver distinto contraddizione, evoluzione, restringimento, ampliamento e differenza di contesto.

Per fonti assimilate di altri autori, la compatibilità semantica con la KB non cambia l'attribuzione originaria.

## Validator

Comando canonico:

`python3 scripts/validate_project.py`

Il validator certifica gli invarianti strutturali del corpus storico e del registry source-agnostic. **Non certifica da solo il merito semantico.** Il checkpoint finale in `reviews/FINAL_SEMANTIC_AUDIT.md` documenta la review semantica dell'attuale doctrine layer.

## Gap di consolidamento ancora aperti

I gap individuati dal checkpoint restano validi:

1. **P1 — Vendita end-to-end**
2. **P1 — Casi studio**
3. **P1 — Doctrine/provenance map**
4. **P2 — Sintesi brand**
5. **P2 — Voice of Customer / ricerca mercato**
6. **P2 — Hardening Git**

Per il progetto manuale, i primi cinque sono ora esplicitamente tracciati in `manual/MANUAL_GAPS.md` e vengono affrontati prima come gap editoriali quando la conoscenza esiste già.

Non riaprire acquisizione o modificare automaticamente `merenda/` soltanto per risolvere un problema di sintesi editoriale.

## Next Action

**Proseguire la Fase 2 del progetto manuale dalla sezione `01_mercato`.**

Sequenza immediata:

1. leggere i quattro nodi specialistici di `01_mercato` e il README di sezione;
2. creare `manual/crosswalk/01_mercato.md` con ID semantici stabili;
3. coprire identificabilità, domanda, capacità di acquisto, appropriatezza economica, high spender e gate pre-lancio;
4. estrarre i segnali di Voice of Customer dispersi nella sezione;
5. deduplicare localmente contro FND-025, FND-032 e FND-042 senza eliminare i caveat;
6. aggiornare master crosswalk e `manual/STATUS.md`;
7. proseguire poi con `02_posizionamento`.

Dopo tutte le sezioni: eseguire cross-section deduplication, dependency pass e coverage audit prima di progettare il curriculum finale.

La ricostruzione Formalife Layer 2 rimane disponibile come filone separato, ma non è la priorità del task corrente.

Riaprire l'acquisizione Layer 1 soltanto se:

- viene fornita una nuova fonte realmente disponibile;
- l'utente autorizza esplicitamente una nuova assimilazione;
- emerge un gap canonico concreto che richiede nuova provenance.

Non acquisire automaticamente i video residui 314+.
