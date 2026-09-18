# Architecture Inventory — Initial Findings

Data: 2026-09-18
Stato: ACTIVE / PRELIMINARY
Scope: control plane e retrieval del Layer 1. Nessuna modifica dottrinale in questo documento.

## Executive diagnosis

La KB canonica non appare carente di conoscenza. Il rischio principale è la **retrievability**: conoscenza corretta e ad alta leva può essere presente nel doctrine layer ma non essere recuperata sistematicamente perché il control plane opera soprattutto per file, sintomo e categoria.

La diagnosi provvisoria è:

> **La struttura semantica della KB è più ricca della struttura di routing che la espone all'agente.**

Questo crea un failure mode pericoloso: una risposta può sembrare coerente e competente pur avendo omesso il principio che avrebbe cambiato la diagnosi.

---

# 1. Finding P0 — Governance attiva storicamente incoerente

## Evidenza

`system/RULES.md` conserva la regola storica secondo cui la KB deve derivare esclusivamente dal canale YouTube ufficiale e non deve incorporare altri marketer.

Lo stato corrente documentato in:

- `00_START_HERE.md`
- `STATUS.md`
- `merenda/INDEX.md`
- `reviews/FINAL_SEMANTIC_AUDIT.md`

riconosce invece fonti source-agnostic e collezioni assimilate autorizzate, con provenance reale preservata.

`CHATGPT.md` conserva inoltre formulazioni storiche che dicono che fonti esterne non-Merenda restano fuori da `merenda/`, mentre il doctrine layer corrente contiene estensioni assimilate esplicitamente autorizzate.

## Rischio

Un agente che legge i file di governo può ricevere contemporaneamente istruzioni incompatibili sulla provenance e sul perimetro del doctrine layer.

Questo non è un problema di contenuto dottrinale: è un problema di **instruction precedence non esplicitata a sufficienza**.

## Decisione provvisoria

Non modificare ancora i frozen file. Prima della chiusura della Architecture Review deve però esistere una soluzione esplicita di supersession/governance che renda impossibile interpretare come contemporaneamente correnti regole di epoche diverse.

---

# 2. Finding P0 — Nessuna baseline precedente sulla qualità del retrieval

## Evidenza

`scripts/validate_project.py` verifica principalmente:

- invarianti frozen;
- cataloghi e queue;
- provenance tecnica delle fonti;
- link locali;
- contatori e lock.

Non misura se, dato un caso reale, l'agente recupera i nodi decisivi prima di formulare la diagnosi.

Il progetto aveva quindi una review semantica della KB, ma non una regression suite per il comportamento di retrieval/routing.

## Intervento già avviato

Creati:

- `evals/routing/README.md`
- `evals/routing/cases.jsonl`
- `scripts/validate_routing_evals.py`

La regola operativa diventa **eval first, refactor second**.

---

# 3. Finding P1 — Il Decision Router svolge troppe funzioni contemporaneamente

## Evidenza

`merenda/DECISION_ROUTER.md` contiene nello stesso documento:

- invarianti dottrinali;
- ordine generale di diagnosi;
- procedura obbligatoria;
- router per sintomo;
- router per richieste tipiche all'AI;
- regole finali di priorità;
- template operativo.

## Rischio

Il router diventa abbastanza lungo da duplicare parte della dottrina, ma resta inevitabilmente incompleto rispetto ai nodi specialistici.

Aggiungere ulteriori casi/sintomi al router aumenta manutenzione e ridondanza senza garantire coverage dei concetti specialistici.

## Decisione provvisoria

Non ampliare il router corrente. Il candidato Router v2 dovrà essere più corto e delegare la conoscenza specifica a una Retrieval Map e ai nodi canonici.

---

# 4. Finding P1 — Routing file-level insufficiente

## Evidenza diretta

### `01_mercato/clienti-identificabili-e-target.md`

Il nome del file suggerisce identificabilità/target, ma il nodo contiene anche concetti ad alta leva come:

- livello di consapevolezza applicato alla priorità commerciale;
- storia d'acquisto / alternativa corrente;
- clienti con durata naturale della relazione;
- distinzione utilizzatore vs pagatore/decisore;
- campagna progettata su relazione × consapevolezza × profilo × directness.

Due failure reali o plausibili già incluse negli eval:

- caso B2B con pagatore diverso dagli utenti;
- caso retention in cui il cliente può essere naturalmente "a scadenza".

Questi concetti non sono deducibili in modo affidabile dal nome del file.

### `01_mercato/appropriatezza-clienti.md`

Oltre all'appropriatezza economica contiene:

- criteri di accettazione/rifiuto;
- RFM;
- allocazione concentrata su coorti finite;
- whale curve / profitto cumulativo per cliente;
- Proof by Refusal assimilata con provenance distinta.

Anche qui il path non rappresenta tutta la superficie semantica instradabile.

### `04_marketing/gerarchia-domanda-e-canali.md`

Il nodo contiene, oltre alla gerarchia domanda/canali:

- timing del bisogno;
- profondità del funnel rispetto a urgenza e quantità di informazione;
- distinzione volume di ricerca vs intento;
- complementarità online/offline;
- sell-in e sell-through con intermediari;
- ruolo dei social come strumento, non default.

## Rischio

La scelta del file giusto non garantisce che l'agente individui il **passaggio giusto dentro il file**. Se il retrieval carica solo abstract/README o usa nomi di file come proxy del contenuto, può mancare il principio decisivo.

## Decisione provvisoria

La Retrieval Map deve supportare almeno `canonical_path + anchor/heading`, non solo `canonical_path`.

---

# 5. Finding P1 — Nodi molto grandi rendono costoso il fallback "leggi tutto il file"

## Evidenza meccanica già verificata

Esempi:

- `09_business/numeri-cassa-e-crescita.md` — circa 43 KB;
- `00_fondamenti/sistema-operativo-merenda.md` — circa 29 KB;
- `02_posizionamento/differenziazione-operativa.md` — circa 26 KB;
- `06_vendita/prequalifica-follow-up-decisori.md` — circa 24 KB;
- `05_acquisizione/information-marketing.md` — circa 22 KB;
- `07_copy_comunicazione/scrittura-sales-letter-e-argomentazione.md` — circa 22 KB;
- `09_business/scalabilita-e-operativita.md` — circa 21 KB;
- `03_offerta/offerta-a-risposta-diretta.md` e vari nodi brand/posizionamento — circa 18–20 KB.

## Rischio

Il fallback "apri l'intero nodo specialistico" migliora recall ma può peggiorare:

- precisione del contesto;
- attenzione del modello;
- token cost;
- probabilità di mescolare eccezioni o sotto-casi non pertinenti.

## Decisione provvisoria

Usare progressive disclosure:

1. mappa/abstract ad alto segnale;
2. anchor/heading candidato;
3. espansione locale sufficiente a preservare contesto e caveat;
4. intero file solo quando realmente necessario.

---

# 6. Finding P1 — Il router manuale non può essere l'unico meccanismo di discovery

## Evidenza

Il Router corrente gestisce bene molti sintomi frequenti, ma una lista manuale di sintomi non può enumerare in modo robusto tutti i casi generabili dalla combinazione di:

- stadio della relazione;
- mercato/segmento;
- user vs payer;
- consapevolezza;
- alternativa corrente;
- urgenza/timing;
- economics;
- vincoli;
- delivery/capacità;
- provenance/evoluzione temporale.

## Rischio

Quando il prompt non assomiglia a uno dei sintomi previsti, l'agente torna a similarity matching o intuizione generale.

## Decisione provvisoria

Il Router v2 deve trasformare il caso in una rappresentazione diagnostica e interrogare una mappa dei principi; non deve tentare di riconoscere ogni problema come frase pre-enumerata.

---

# 7. Finding P1 — Retrieval causale necessario oltre al retrieval semantico

## Evidenza

La KB stessa impone dipendenze a monte:

- mercato/cliente prima della tattica;
- posizionamento prima del copy;
- offerta prima dell'amplificazione;
- domanda posseduta prima della nuova acquisizione;
- economics/capacità prima della scala.

Un sistema che recupera solo i testi semanticamente simili alla domanda può recuperare, per esempio, advertising quando l'errore è nel mercato o nel posizionamento.

## Decisione provvisoria

La Retrieval Map deve codificare relazioni causali come:

- `upstream`
- `must_read_with`
- `evidence_required`
- `downstream`

La similarity search futura, se introdotta, deve essere un segnale complementare e non il governatore della diagnosi.

---

# 8. Finding P1 — La provenance deve essere proprietà del retrieval, non nota a piè pagina

## Evidenza

Il doctrine layer corrente contiene:

- MERENDA_PRIMARY;
- ASSIMILATED_AS_MERENDA_BY_USER;
- SYNTHESIS.

Un esempio concreto è `Proof by Refusal` dentro `appropriatezza-clienti.md`: il concetto è semanticamente integrato ma non attribuibile direttamente a Frank Merenda.

## Rischio

Se il retrieval restituisce il passaggio senza metadata di provenance, la risposta può attribuire a Frank un principio assimilato.

## Decisione provvisoria

La Retrieval Map deve portare `provenance_class` a livello di principio/entry quando necessario, non solo a livello di file.

---

# 9. Finding P1 — Vendita: contenuto forte, orchestrazione frammentata

## Evidenza

`reviews/FINAL_SEMANTIC_AUDIT.md` aveva già identificato la vendita end-to-end come P1. La sezione `06_vendita/` contiene nodi separati per:

- prequalifica/follow-up/decisori;
- diagnosi e prescrizione;
- rete vendita/script/training/controllo;
- follow-up dei non convertiti.

Il Router può elencare i nodi, ma manca una casa canonica unica del processo end-to-end.

## Rischio

Nei casi di conversione vendita l'agente può sovrappesare il nodo semanticamente più vicino al sintomo e saltare uno stadio precedente.

## Decisione provvisoria

Il futuro nodo end-to-end già previsto dal Semantic Audit resta utile, ma la sua creazione deve essere trattata come consolidamento separato dalla Retrieval Map.

---

# 10. Finding P2 — Casi studio insufficienti per robusto reasoning analogico

## Evidenza meccanica

`10_casi_studio/` contiene oggi solo due casi canonici oltre al README:

- `focalizzazione-funnel-e-capacita.md`;
- `motoargento-focalizzazione.md`.

Il Semantic Audit aveva già classificato l'espansione selettiva dei casi come P1.

## Rischio

La dottrina astratta è ricca, ma l'agente dispone di pochi esempi canonici strutturati per confrontare situazioni reali senza inventare analogie.

## Decisione provvisoria

Non blocca la Retrieval Map, ma resta un upgrade ad alta leva dopo il control plane.

---

# 11. Finding tecnico — Non assumere full-text search esterna come rete di sicurezza

Durante la Architecture Review, il connector GitHub disponibile al Project ha restituito zero risultati anche per termini verificati come presenti nei file canonici.

Questo comportamento può dipendere dall'indicizzazione/tooling e non viene trattato come difetto intrinseco della repository.

Conseguenza architetturale: il sistema non deve richiedere una full-text search perfetta per compensare metadata di routing incompleti.

---

# 12. Intervento tecnico in corso

È stato aggiunto `scripts/build_architecture_inventory.py` per generare in modo ripetibile:

- inventario dei file Markdown canonici;
- dimensioni e line count;
- heading/anchor;
- local links;
- incoming links;
- routing visibility;
- candidati heading non visibili nei control layer;
- riferimenti rotti.

La CI della branch di review è configurata per produrre un artifact `architecture-inventory` con output JSON e Markdown.

Questo report è **meccanico**: i candidati trovati devono essere sottoposti a review semantica prima di diventare entry della Retrieval Map.

---

# 13. Next decision block

Prima di modificare il Router:

1. completare/ottenere l'inventory meccanico;
2. review semantica dei candidati hidden concepts;
3. estendere la eval suite con casi che esercitano i blind spot trovati;
4. definire schema della `Doctrine/Retrieval Map v1`;
5. popolare la mappa sui principi high-leverage;
6. misurare current Router + map;
7. soltanto dopo progettare Router v2.

## Criterio di stop

Non aggiungere metadata per ogni paragrafo della KB.

La mappa deve coprire ciò che cambia realmente:

- diagnosi;
- ordine causale;
- evidenza richiesta;
- decisione;
- eccezione/evoluzione;
- provenance.
