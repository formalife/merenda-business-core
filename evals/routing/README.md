# Routing & Retrieval Eval Suite

## Scopo

Questa suite misura la capacità di un agente di usare Merenda Business Core come sistema decisionale, non come semplice raccolta di testi.

Gli eval vivono fuori da `merenda/`: **non sono dottrina**. Possono includere casi sintetici, casi avversariali e casi anonimizzati derivati dall'uso operativo. Servono a verificare se il sistema recupera e applica correttamente la dottrina canonica.

## Unità di valutazione

Ogni record di `cases.jsonl` rappresenta un caso decisionale.

Campi minimi:

- `id`: identificatore stabile;
- `title`: titolo leggibile;
- `prompt`: input dell'utente/founder;
- `case_type`: categoria operativa;
- `required_nodes`: nodi canonici che devono essere consultati;
- `optional_nodes`: nodi utili ma non indispensabili;
- `required_checks`: verifiche causali/epistemiche che devono comparire nel ragionamento;
- `forbidden_shortcuts`: conclusioni o tattiche premature che costituiscono failure;
- `expected_behavior`: cosa deve fare l'agente prima di prescrivere;
- `provenance_checks`: eventuali vincoli di attribuzione;
- `notes`: note per il reviewer.

I path in `required_nodes` e `optional_nodes` sono relativi alla root della repository.

## Cosa misura la baseline

La baseline non richiede una risposta verbatim. Valuta il processo decisionale.

### Routing Recall

`required_nodes_retrieved / required_nodes_total`

Un caso può essere considerato fallito anche con una risposta plausibile se il sistema ha saltato un nodo indispensabile e ha raggiunto la conclusione per conoscenza generale o fortuna.

### Upstream Recall

Percentuale dei `required_checks` a monte effettivamente verificati prima della tattica.

### Retrieval Precision

Contesto pertinente recuperato rispetto al contesto totale recuperato. La metrica va interpretata insieme al recall: minimizzare token saltando conoscenza necessaria non è successo.

### Doctrine Fidelity

La diagnosi e la prescrizione devono essere riconducibili ai nodi canonici recuperati.

### Unsupported Inference Rate

Penalizza conversioni non autorizzate come:

- HYPOTHESIS → FACT;
- OBSERVATION → FACT generalizzato;
- LEGACY DECISION → CONSTRAINT;
- RECOMMENDATION → DECISION;
- singola vendita/opportunità → prova sufficiente di mercato.

### Premature Tactic Rate

Penalizza ads, funnel, copy, pricing, hiring, automazione, espansione o scala prescritti prima dei prerequisiti richiesti dal caso.

### Provenance Accuracy

Quando un principio proviene da una fonte assimilata, non deve essere attribuito direttamente a Frank Merenda.

## Livelli di severità

- `P0`: omissione che può invertire la decisione o falsificare la dottrina/provenance;
- `P1`: omissione che degrada materialmente diagnosi, economics o sequenza;
- `P2`: omissione utile ma non decisiva.

La severità viene aggiunta progressivamente ai casi quando il benchmark sarà stabilizzato.

## Regola di review

Un evaluator non deve chiedersi soltanto "la risposta è buona?".

Deve chiedersi:

1. quale informazione era necessaria per poter prendere la decisione?
2. il sistema è andato a prenderla?
3. ha controllato il primo prerequisito a monte plausibile?
4. ha distinto fatti, ipotesi e osservazioni?
5. ha evitato di compensare un retrieval incompleto con conoscenza generale?
6. ha formulato il test/minimo prossimo passo invece di inventare certezza?

## Evoluzione prevista

La suite parte con casi manuali gold. Successivamente potrà includere:

- expected anchors/sections;
- score automatici di retrieval;
- trace grading;
- regression tests per modifiche a Router/Doctrine Map;
- casi blind non usati durante il refactor.

Le modifiche architetturali vengono adottate solo se migliorano gli eval rispetto alla baseline.
