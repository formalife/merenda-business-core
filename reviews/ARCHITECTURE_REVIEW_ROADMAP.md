# Architecture Review Roadmap — Routing, Retrieval, Fidelity

Data avvio: 2026-09-18
Stato: ACTIVE
Branch di lavoro: `architecture-review-routing-v2`

## Obiettivo

Aumentare in modo verificabile la fedeltà con cui un agente usa Merenda Business Core per diagnosi e decisioni reali.

Il target non è far suonare l'agente come Frank Merenda. Il target è fare in modo che, dato un caso concreto, l'agente recuperi sistematicamente la conoscenza canonica necessaria, controlli le dipendenze a monte, distingua provenance e stato epistemico, e produca una decisione coerente con il doctrine layer.

## Diagnosi iniziale

La KB corrente è semanticamente matura. Il collo di bottiglia prioritario è il control plane che collega problema reale → routing → retrieval → diagnosi.

Problemi da verificare e misurare:

1. `DECISION_ROUTER.md` svolge insieme troppe funzioni: principi, procedura, symptom routing, richieste tipiche e template operativo.
2. Il routing è prevalentemente file-level, mentre molti file contengono più unità semantiche ad alta leva.
3. La mappa delle relazioni fra principi non è machine-readable: mancano campi espliciti per upstream dependency, companion node, canonical_for, supersession, provenance e trigger.
4. Il sistema dipende ancora troppo dall'intuizione dell'agente per scoprire nodi non nominati dal router.
5. Il bootstrap carica documenti parzialmente ridondanti e, in alcuni casi, storicamente incompatibili.
6. Il validator corrente verifica soprattutto invarianti strutturali del corpus, non la qualità del retrieval e della diagnosi.
7. La ricerca full-text disponibile attraverso alcuni connector non può essere assunta come affidabile o sufficiente.

## Principi architetturali

- **Eval first.** Nessun refactor importante del Router viene adottato senza una baseline e un confronto misurabile.
- **Progressive disclosure.** Caricare prima una mappa ad alto segnale, poi espandere solo i nodi necessari.
- **Human-readable doctrine, machine-readable routing.** `merenda/` resta il doctrine layer canonico leggibile; eventuali metadata di routing sono derivati e verificabili.
- **Section-level retrieval quando necessario.** Un file può contenere più unità semantiche instradabili.
- **Causal retrieval, non similarity-only retrieval.** Il sistema deve sapere cosa controllare a monte, non soltanto cosa assomiglia linguisticamente alla domanda.
- **Provenance preserved.** MERENDA_PRIMARY, ASSIMILATED e SYNTHESIS non vengono fusi semanticamente in un'unica attribuzione.
- **No architecture by taste.** Ogni modifica deve risolvere failure osservabili nell'eval suite.
- **No premature GraphRAG.** Prima si testa una mappa esplicita leggera; embeddings/vector/graph infrastructure entra solo se il benchmark mostra un gap residuo che la giustifica.

## Metriche principali

### Routing Recall
Percentuale dei nodi/concetti gold indispensabili recuperati per un caso.

### Upstream Recall
Percentuale dei prerequisiti causali gold controllati prima della prescrizione.

### Retrieval Precision
Quota del contesto recuperato realmente pertinente alla decisione.

### Doctrine Fidelity
La conclusione è supportata dai nodi canonici recuperati e non da conoscenza generale sostitutiva.

### Unsupported Inference Rate
Frequenza con cui hypothesis/observation/legacy decision vengono trasformate implicitamente in fact/constraint/decision.

### Provenance Accuracy
Correttezza della distinzione MERENDA_PRIMARY / ASSIMILATED / SYNTHESIS.

### Premature Tactic Rate
Frequenza con cui viene prescritta una tattica senza aver verificato i gate a monte richiesti.

### Founder Accommodation Failure
Frequenza con cui una premessa debole del founder viene accettata invece di essere testata o riclassificata.

## Piano di lavoro

### Fase 1 — Baseline Eval Suite

Deliverable:

- `evals/routing/README.md`
- `evals/routing/cases.jsonl`
- validator meccanico dello schema

Costruire 30–50 casi progressivamente, iniziando da casi ad alta leva e failure già osservati durante l'uso reale.

Ogni caso deve definire almeno:

- prompt/caso;
- nodi indispensabili;
- nodi utili ma opzionali;
- controlli a monte;
- classificazioni epistemiche richieste;
- conclusioni premature vietate;
- comportamento decisionale atteso;
- eventuale provenance check.

Gate: nessun refactor del router prima di una baseline ripetibile.

### Fase 2 — Architecture Inventory

Produrre un inventario completo di:

- file canonici e dimensione;
- heading/anchor semantici;
- link interni;
- concetti ad alta leva;
- provenance;
- supersession/evoluzioni temporali;
- nodi orfani o scarsamente raggiungibili;
- duplicazioni di routing;
- concetti presenti nei nodi ma invisibili in INDEX/README/Router.

Codex è il candidato preferito per la scansione meccanica e la generazione dell'inventario. La validazione semantica resta a ChatGPT/Founder.

### Fase 3 — Doctrine / Retrieval Map v1

Progettare una struttura leggera machine-readable per i principi decisionali ad alta leva.

Campi candidati:

- `id`
- `canonical_path`
- `anchor`
- `canonical_for`
- `use_when`
- `do_not_use_when`
- `upstream`
- `must_read_with`
- `downstream`
- `evidence_required`
- `provenance_class`
- `latest_relevant_source`
- `supersedes`
- `superseded_by`
- `related`

La mappa non sostituisce i file canonici e non deve duplicarne il contenuto sostanziale.

Gate: coverage sufficiente dei gold concept della baseline.

### Fase 4 — Decision Router v2

Obiettivo: rendere il router più piccolo e più propriamente un router.

Responsabilità previste:

1. definire outcome e conseguenza economica;
2. classificare il caso;
3. localizzare il livello dove appare il problema;
4. risalire ai prerequisiti causali;
5. interrogare la Retrieval Map;
6. recuperare i nodi specialistici necessari;
7. verificare sufficienza e provenance;
8. solo dopo formulare diagnosi/test/decisione.

Il Router v2 non deve duplicare la dottrina specialistica.

### Fase 5 — Retrieval Sufficiency Gate

Prima di una decisione sostanziale l'agente deve poter rispondere internamente almeno a:

- ho letto il nodo canonico primario?
- ho controllato il prerequisito a monte più plausibile?
- esiste una eccezione/evoluzione temporale pertinente?
- mi manca un fatto Formalife che potrebbe cambiare la decisione?
- sto usando una fonte assimilata e, se sì, ne preservo la provenance?
- la tattica richiesta è downstream di qualcosa non ancora stabilito?

### Fase 6 — Validator / CI

Estendere i controlli meccanici a:

- schema eval valido;
- path gold esistenti;
- ID univoci;
- routing map senza riferimenti rotti;
- concetti high-leverage senza canonical location;
- metadata stale;
- conflitti espliciti di supersession;
- coverage minima dell'eval suite.

### Fase 7 — A/B Eval

Confrontare almeno:

- architettura corrente;
- current router + retrieval map;
- router v2 + retrieval map.

Adottare una modifica solo se migliora le metriche senza aumentare in modo sproporzionato contesto, complessità o maintenance burden.

## Ruolo di Codex

Codex viene usato come architecture engineer, non come autorità semantica della dottrina.

Task appropriati:

- scandire tutti i Markdown e gli heading;
- costruire graph/link inventory;
- individuare path/anchor orfani;
- generare draft metadata;
- scrivere validator;
- eseguire eval harness;
- produrre diff e report.

Task non delegati autonomamente:

- decidere che cosa Merenda intende;
- fondere dottrina;
- risolvere conflitti semantici;
- promuovere una fonte assimilata a MERENDA_PRIMARY;
- modificare file frozen senza autorizzazione.

## Decisioni congelate durante la review

Fino a evidenza contraria:

- non riaprire il corpus YouTube residuo;
- non fare riscritture massive di `merenda/`;
- non introdurre vector DB / GraphRAG come prerequisito;
- non ampliare `DECISION_ROUTER.md` per coprire ogni possibile sintomo;
- non trattare la maggiore lunghezza del prompt come proxy di maggiore fedeltà.

## Condizione di successo

La review è riuscita quando casi nuovi e non preparati producono in modo ripetibile:

**problema reale → classificazione corretta → retrieval dei principi necessari → controllo upstream → distinzione provenance/evidenza → diagnosi coerente → singolo blocco decisionale utile**, con un tasso di omissione sostanzialmente inferiore alla baseline corrente.
