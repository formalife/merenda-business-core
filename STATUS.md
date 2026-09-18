# PROJECT STATUS

## Stato generale

**MERENDA BUSINESS CORE — LAYER 1 OPERATIONAL. ARCHITECTURE REVIEW ACTIVE; CURRENT KNOWN CORPUS EXHAUSTED.**

Il progetto è ora il **Layer 1** del sistema aziendale: doctrine layer, routing decisionale e motore di diagnosi.

Nome canonico del progetto: **Merenda Business Core**.

Nome repository previsto: `merenda-business-core`.

La fase video generalista è chiusa per saturazione al contenuto 313. Il lock operativo resta attivo in `sources/queue/ACQUISITION_CLOSED.md` e continua a impedire l'acquisizione automatica dei residui 314–468.

Il corpus source-agnostic attualmente disponibile è processato fino a `FM-SRC-0166`: 166 fonti registrate, 166 studiate, 0 pending.

Il checkpoint semantico di maturità è documentato in:

`reviews/FINAL_SEMANTIC_AUDIT.md`

La priorità corrente è una **Architecture Review di routing, retrieval e fidelity** prima di riprendere l'uso operativo intensivo del Layer 1 su Formalife. La review non riapre il corpus e non modifica automaticamente la dottrina.

Roadmap corrente:

`reviews/ARCHITECTURE_REVIEW_ROADMAP.md`

Branch di lavoro:

`architecture-review-routing-v2`

Contratto e protocollo:

- `LAYER1_CONTRACT.md`
- `FORMALIFE_REBUILD_PROTOCOL.md`

## Architecture Review — stato corrente

Obiettivo: aumentare in modo misurabile la probabilità che un agente recuperi la conoscenza canonica giusta, controlli le dipendenze a monte e distingua correttamente provenance, fatti e ipotesi prima di formulare una decisione.

Decisione metodologica corrente:

**eval prima del refactor.**

Non modificare ancora `merenda/DECISION_ROUTER.md` soltanto per renderlo più completo. Prima costruire una baseline che misuri routing recall, upstream recall, retrieval precision, doctrine fidelity, unsupported inference, premature tactics e provenance accuracy.

Asset creati sul branch di review:

- `evals/routing/README.md`
- `evals/routing/cases.jsonl`
- `scripts/validate_routing_evals.py`

Stato baseline iniziale:

- 15 casi gold creati;
- inclusi casi su domanda posseduta, conversione, user-vs-payer, pricing, nuovi prodotti, cassa, founder dependency, retention naturale, canali, vendita, economics, provenance, sunk cost, lead quality e automazione;
- il caso user-vs-payer è incluso specificamente per testare concetti importanti presenti in sezioni non evidenti dal nome del file.

Prossimo gate:

1. validare meccanicamente la suite;
2. estenderla verso 30–50 casi;
3. produrre l'Architecture Inventory file/heading/link/concept;
4. solo dopo progettare Doctrine/Retrieval Map v1 e Router v2.

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

Formalife verrà ricostruita secondo modalità **first meeting / zero-based reconstruction**.

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

Comandi correnti:

`python3 scripts/validate_project.py`

`python3 scripts/validate_routing_evals.py`

Il validator principale certifica gli invarianti strutturali del corpus storico e del registry source-agnostic. **Non certifica da solo il merito semantico.** Il checkpoint finale in `reviews/FINAL_SEMANTIC_AUDIT.md` documenta la review semantica dell'attuale doctrine layer. Il nuovo validator degli eval controlla schema, ID e path della baseline ma non sostituisce la review semantica dei gold case.

## Gap di consolidamento ancora aperti

I gap individuati dal checkpoint restano validi, ma vengono ora ordinati rispetto alla Architecture Review:

1. **P0 — Routing / retrieval fidelity ed eval harness**
2. **P1 — Doctrine/provenance/retrieval map**
3. **P1 — Vendita end-to-end**
4. **P1 — Casi studio**
5. **P2 — Sintesi brand**
6. **P2 — Voice of Customer / ricerca mercato**
7. **P2 — Hardening Git**

Non riaprire i gap dottrinali soltanto per completezza. La review deve prima stabilire quali gap degradano realmente le decisioni operative.

## Next Action

**Completare la baseline e l'Architecture Inventory prima di modificare il Router.**

Sequenza:

1. eseguire `scripts/validate_routing_evals.py` in un checkout locale/Codex;
2. revisionare semanticamente i primi 15 gold case;
3. estendere la suite a 30–50 casi, includendo blind/adversarial case;
4. usare Codex per inventario completo di file, heading, link e candidati concettuali;
5. identificare concetti ad alta leva presenti nella KB ma invisibili o debolmente raggiungibili dal routing corrente;
6. progettare `Doctrine/Retrieval Map v1`;
7. misurare baseline vs nuova architettura prima di adottare Router v2.

Riaprire l'acquisizione Layer 1 soltanto se:

- viene fornita una nuova fonte realmente disponibile;
- l'utente autorizza esplicitamente una nuova assimilazione;
- emerge un gap canonico concreto che richiede nuova provenance.

Non acquisire automaticamente i video residui 314+.
