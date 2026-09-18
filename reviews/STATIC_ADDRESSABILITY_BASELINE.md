# Static Routing Addressability Baseline

Data: 2026-09-18
Stato: COMPLETE MECHANICAL BASELINE — NOT BEHAVIORAL PERFORMANCE

## Scopo

Misurare quanto i nodi richiesti dai 30 gold case siano **esplicitamente indirizzabili** dal control plane corrente e quanto la draft Doctrine/Retrieval Map aumenti questa copertura.

Questa misura NON dimostra che il modello recupererà davvero il nodo, lo leggerà correttamente o produrrà una buona decisione. Misura soltanto una proprietà architetturale: il nodo è esplicitamente rappresentato nei meccanismi di routing disponibili?

Script:

`scripts/score_static_routing_coverage.py`

---

## Baseline Router corrente

Su 30 casi:

- explicit node references nel Router corrente: **35**;
- mean current Router direct recall: **82,8%**;
- casi con full direct recall dal Router corrente: **19/30**.

Questo mostra che il Router corrente è già utile e copre bene molti sintomi frequenti, ma lascia una coda di casi in cui almeno un nodo gold decisivo non è esplicitamente indirizzato.

---

## Checkpoint Router + Map — Phase 4

Prima delle ultime tre entry:

- mean combined Router + Map direct recall: **96,1%**;
- casi con full direct recall: **27/30**.

I tre gap residui erano:

- **R013** — `FORMALIFE_REBUILD_PROTOCOL.md`;
- **R016** — `05_acquisizione/partnership-distribuzione-e-combinazioni.md`;
- **R023** — `07_copy_comunicazione/checklist-risposta-diretta.md`.

Sono stati chiusi solo dopo review semantica, non per inseguire il numero.

Entry aggiunte:

- `ZERO_BASED.REBUILD_PROTOCOL`;
- `DISTRIBUTION.PARTNER_EXECUTION`;
- `DIRECT_RESPONSE.MEASURABLE_NEXT_ACTION`.

---

## Checkpoint Router + Map — Phase 5

CI run verificato:

- Retrieval Map: **PASS — 30 entry**;
- eval linkage coverage: **30/30 = 100%**;
- mean Map direct recall isolata: **53,3%**;
- mean combined Router + Map direct recall: **100%**;
- casi con full direct recall Router + Map: **30/30**.

La Map non è progettata per sostituire il Router o duplicare tutti i path necessari. Per questo il recall isolato della Map non è una metrica obiettivo. Il confronto utile è:

**current Router: 82,8% mean direct recall / 19 di 30 casi completi**

vs

**current Router + Map: 100% mean direct recall / 30 di 30 casi completi**.

Di nuovo: **addressability ≠ behavioral retrieval**.

---

## Blind spot resi esplicitamente indirizzabili

Fra i casi in cui il Router corrente non nominava direttamente almeno un nodo gold ma la Map chiude il gap:

- **R003** — user vs payer;
- **R008** — customer expiry;
- **R009** — target identifiability nella scelta canale;
- **R013** — zero-based rebuild protocol;
- **R016** — partnership/distribution execution;
- **R023** — measurable next action/direct response;
- **R026** — trigger/priorità prima del copy;
- **R027** — partnership economics;
- **R028** — high spender: capacità vs propensione;
- **R029** — creative testing da winner;
- **R030** — event response asset.

Questi casi supportano direttamente la diagnosi di discoverability sub-file / specialist-node.

---

## Decisione architetturale a questo gate

**Fermare l'espansione della Map guidata dagli eval.**

Il fatto che la static addressability raggiunga 30/30 elimina il motivo di aggiungere altre entry soltanto per coverage della suite corrente.

Nuove entry da questo punto devono entrare solo se:

- emergono failure comportamentali;
- un nuovo caso reale rende visibile un gap;
- una review semantica identifica un principio high-leverage non rappresentato.

Questo evita overfitting e crescita burocratica della metadata.

---

## Ipotesi da testare ora

La Map sembra avere valore potenziale come:

- rete di sicurezza sui blind spot;
- routing section-level;
- causal expansion;
- provenance carrier;
- evidence sufficiency layer.

L'ipotesi sperimentale è:

> **il Router corrente, senza essere ancora riscritto, migliora materially il retrieval e la diagnosi quando viene affiancato dalla Retrieval Map.**

Questa ipotesi non è ancora dimostrata.

---

## Gate successivo

Passare alla **behavioral baseline isolata**:

1. `current`;
2. `current_plus_map`.

Il modello sotto test non deve vedere il gold.

Asset pronti:

- `evals/routing/RUN_PROTOCOL.md`;
- `scripts/export_routing_eval_prompts.py`;
- `scripts/score_routing_run.py`;
- `reviews/CODEX_ROUTING_BASELINE_TASK.md`.

Misurare:

- required-node recall osservato;
- relevant retrieval precision;
- over-retrieval;
- upstream/required check recall;
- unsupported inference;
- premature tactic rate;
- provenance accuracy;
- founder accommodation failure.

Solo dopo questo confronto si decide se adottare la Map nel control plane e se esiste ancora un problema che giustifica Router v2.
