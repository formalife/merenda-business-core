# PROJECT STATUS

## Stato generale

**MERENDA BUSINESS CORE — LAYER 1 OPERATIONAL. CURRENT KNOWN CORPUS EXHAUSTED; FINAL SEMANTIC AUDIT COMPLETED.**

Il progetto è ora il **Layer 1** del sistema aziendale: doctrine layer, routing decisionale e motore di diagnosi.

Nome canonico del progetto: **Merenda Business Core**.

Nome repository previsto: `merenda-business-core`.

La fase video generalista è chiusa per saturazione al contenuto 313. Il lock operativo resta attivo in `sources/queue/ACQUISITION_CLOSED.md` e continua a impedire l'acquisizione automatica dei residui 314–468.

Il corpus source-agnostic attualmente disponibile è processato fino a `FM-SRC-0166`: 166 fonti registrate, 166 studiate, 0 pending.

Il checkpoint semantico di maturità è documentato in:

`reviews/FINAL_SEMANTIC_AUDIT.md`

La priorità non è più accumulare fonti. Il Layer 1 viene ora usato operativamente per costruire il **Layer 2 Formalife** tramite una ricostruzione zero-based.

Contratto e protocollo:

- `LAYER1_CONTRACT.md`
- `FORMALIFE_REBUILD_PROTOCOL.md`

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

Comando canonico:

`python3 scripts/validate_project.py`

Il validator certifica gli invarianti strutturali del corpus storico e del registry source-agnostic. **Non certifica da solo il merito semantico.** Il checkpoint finale in `reviews/FINAL_SEMANTIC_AUDIT.md` documenta la review semantica dell'attuale doctrine layer.

## Gap di consolidamento ancora aperti

I gap individuati dal checkpoint restano validi, ma non bloccano l'uso operativo della versione corrente:

1. **P1 — Vendita end-to-end**
2. **P1 — Casi studio**
3. **P1 — Doctrine/provenance map**
4. **P2 — Sintesi brand**
5. **P2 — Voice of Customer / ricerca mercato**
6. **P2 — Hardening Git**

Non riaprire questi lavori soltanto per completezza. Possono essere affrontati quando diventano rilevanti durante l'uso reale del Layer 1 o quando saranno disponibili nuove fonti adeguate.

## Next Action

**Costruire il Layer 2 Formalife come ricostruzione zero-based guidata dal Layer 1.**

Sequenza:

1. creare repository separata per Formalife Layer 2;
2. iniziare dalla Fase 0 di `FORMALIFE_REBUILD_PROTOCOL.md`;
3. condurre il founder interview per blocchi decisionali;
4. salvare nel Layer 2 fatti, decisioni, ipotesi, esperimenti e observed reality;
5. interrogare il Layer 1 a ogni gate sostanziale.

Riaprire l'acquisizione Layer 1 soltanto se:

- viene fornita una nuova fonte realmente disponibile;
- l'utente autorizza esplicitamente una nuova assimilazione;
- emerge un gap canonico concreto che richiede nuova provenance.

Non acquisire automaticamente i video residui 314+.
