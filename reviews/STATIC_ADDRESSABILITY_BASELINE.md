# Static Routing Addressability Baseline

Data: 2026-09-18
Stato: MECHANICAL BASELINE — NOT BEHAVIORAL PERFORMANCE

## Scopo

Misurare quanto i nodi richiesti dai 30 gold case siano **esplicitamente indirizzabili** dal control plane corrente e quanto la draft Doctrine/Retrieval Map aumenti questa copertura.

Questa misura NON dimostra che il modello recupererà davvero il nodo, lo leggerà correttamente o produrrà una buona decisione. Misura soltanto una proprietà architetturale: il nodo è esplicitamente rappresentato nei meccanismi di routing disponibili?

Script:

`scripts/score_static_routing_coverage.py`

## Checkpoint CI — prima di Phase 5

Su 30 casi:

- explicit node references nel Router corrente: **35**;
- mean current Router direct recall: **82,8%**;
- mean Map direct recall isolata: **49,4%**;
- mean combined Router + Map direct recall: **96,1%**;
- casi con full direct recall dal Router corrente: **19/30**;
- casi con full direct recall Router + Map: **27/30**.

La Map non è progettata per sostituire il Router o duplicare tutti i path necessari. Per questo il suo recall isolato non è una metrica obiettivo. Il confronto rilevante è `current` vs `current + map`.

## Blind spot resi indirizzabili dalla Map

Fra i casi in cui il Router corrente non nominava direttamente un nodo gold ma la Map lo rende esplicito:

- **R003** — `clienti-identificabili-e-target.md` per user vs payer;
- **R008** — stesso nodo per customer expiry;
- **R009** — identificabilità del target nella scelta canale;
- **R026** — `priorita-azione-e-inerzia.md`;
- **R027** — `partnership-distribuzione-e-combinazioni.md`;
- **R028** — `clienti-altospendenti.md`;
- **R029** — `test-creativita-annunci.md`;
- **R030** — `eventi-proprietari-vip-experience.md`.

Questi casi supportano direttamente la diagnosi di discoverability sub-file / specialist-node.

## Tre gap rimasti dopo Phase 4

Il confronto statico precedente lasciava tre casi senza full combined recall:

### R013 — zero-based reconstruction

Mancava l'esplicita addressability di `FORMALIFE_REBUILD_PROTOCOL.md`.

Intervento semanticamente giustificato:

`ZERO_BASED.REBUILD_PROTOCOL`.

### R016 — distribuzione tramite intermediari

La Map copriva il principio sell-in/sell-through in `04_marketing`, ma non il nodo specialistico `05_acquisizione/partnership-distribuzione-e-combinazioni.md` richiesto dal gold.

Intervento semanticamente giustificato:

`DISTRIBUTION.PARTNER_EXECUTION`.

### R023 — vanity metrics / direct response

Mancava `07_copy_comunicazione/checklist-risposta-diretta.md`, che governa l'avanzamento osservabile e misurabile.

Intervento semanticamente giustificato:

`DIRECT_RESPONSE.MEASURABLE_NEXT_ACTION`.

Le tre entry sono state aggiunte in `DOCTRINE_RETRIEVAL_MAP_V1_PHASE5.json`. Il prossimo run CI deve verificare se la static addressability combinata raggiunge full coverage dei gold node.

## Perché questa baseline è utile

Il Router corrente non è inutilizzabile: **82,8% di direct recall medio** mostra che copre già bene molti problemi frequenti.

Il problema è la coda di casi nei quali la risposta di alto livello sembra plausibile ma manca un nodo specialistico capace di cambiare la diagnosi.

La Map sembra quindi avere valore soprattutto come:

- rete di sicurezza sui blind spot;
- routing section-level;
- causal expansion;
- provenance carrier;
- evidence sufficiency layer.

Questo supporta l'ipotesi che il primo esperimento corretto sia:

**Router corrente + Retrieval Map**, non una riscrittura immediata del Router.

## Gate successivo

Dopo la CI su Phase 5, passare alla **behavioral baseline isolata**.

La static addressability non autorizza da sola l'adozione della Map. Serve dimostrare che il modello, usando la Map, migliori realmente:

- required-node recall osservato;
- upstream/required check recall;
- retrieval precision;
- unsupported inference;
- premature tactic rate;
- provenance accuracy;
- founder accommodation failure.
