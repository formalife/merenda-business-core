# Routing Eval — Run Protocol

## Scopo

La suite `cases*.jsonl` definisce il **gold standard**. Per misurare un'architettura serve però anche un trace di ciò che l'agente ha realmente recuperato e controllato.

Questo protocollo separa tre oggetti:

1. **case** — il problema dato all'agente;
2. **agent trace** — retrieval e decision path osservato;
3. **judgment** — valutazione rispetto al gold.

Non usare il testo della risposta come unico segnale: un agente può produrre una risposta plausibile pur avendo recuperato i nodi sbagliati.

---

## 1. Regola di isolamento

Per una baseline valida, ogni caso va eseguito in una sessione indipendente o in un contesto azzerato che non contenga:

- gli altri gold case;
- `required_nodes` del caso;
- la soluzione attesa;
- risultati di run precedenti.

L'agente può ricevere soltanto l'architettura che si sta testando e il prompt del caso.

Configurazioni candidate:

- `current` — bootstrap + Router/Sistema Operativo correnti;
- `current_plus_map` — stessa architettura + Retrieval Map;
- `router_v2_plus_map` — futuro Router v2 + Retrieval Map.

---

## 2. Agent trace minimo

Ogni run deve produrre JSONL con un record per caso:

```json
{
  "case_id": "R003",
  "architecture": "current",
  "retrieved_nodes": [
    "merenda/01_mercato/clienti-identificabili-e-target.md"
  ],
  "retrieved_sections": [
    {
      "path": "merenda/01_mercato/clienti-identificabili-e-target.md",
      "anchor": "consumare-non-significa-comprare"
    }
  ],
  "classification": [
    "OBSERVATION",
    "OPEN_QUESTION"
  ],
  "decision_level": "market_customer",
  "answer": "...",
  "trace_notes": "..."
}
```

### `retrieved_nodes`

Solo i file realmente letti/recuperati per il caso, non quelli che l'agente avrebbe potuto leggere.

### `retrieved_sections`

Quando disponibile, registra l'anchor/heading effettivamente recuperato. Questo permette di distinguere `file recall` da `concept recall`.

### `classification`

Classificazioni epistemiche effettivamente usate, se applicabili.

### `decision_level`

Livello del problema identificato dall'agente, ad esempio:

- `outcome`
- `market_customer`
- `positioning`
- `offer`
- `proof_authority`
- `demand_channel`
- `acquisition`
- `sales`
- `delivery_retention`
- `economics_capacity`
- `expansion`

---

## 3. Judgment separato

Il giudizio non deve essere prodotto dallo stesso agente testato senza una seconda verifica.

Formato candidato:

```json
{
  "case_id": "R003",
  "architecture": "current",
  "satisfied_check_indices": [0, 1, 2],
  "triggered_forbidden_shortcut_indices": [],
  "provenance_error": false,
  "unsupported_inference": false,
  "premature_tactic": false,
  "founder_accommodation_failure": false,
  "notes": "..."
}
```

Gli indici sono zero-based rispetto agli array `required_checks` e `forbidden_shortcuts` del gold case.

---

## 4. Metriche deterministiche dal trace

Il scorer può calcolare senza interpretazione semantica:

### Required Node Recall

`required_nodes recuperati / required_nodes gold`

### Relevant Retrieval Precision

Considera rilevanti `required_nodes + optional_nodes`.

`nodi rilevanti recuperati / tutti i nodi recuperati`

### Over-retrieval

Numero di nodi recuperati che non sono né required né optional.

### Section Recall

Disponibile solo quando il gold verrà esteso con anchor obbligatori espliciti.

---

## 5. Metriche dal judgment

### Upstream / Required Check Recall

`satisfied required checks / required checks gold`

### Forbidden Shortcut Rate

Shortcut vietati attivati / shortcut vietati disponibili.

### Provenance Error Rate

Quota dei casi con `provenance_error=true` quando la provenance è materialmente rilevante.

### Unsupported Inference Rate

Quota dei casi in cui l'agente trasforma evidenza debole in fatto/decisione.

### Premature Tactic Rate

Quota dei casi in cui viene prescritta una tattica prima dei gate richiesti.

### Founder Accommodation Failure

Quota dei casi in cui una premessa del founder che il gold richiede di contestare viene invece accettata.

---

## 6. Baseline da eseguire

La prima baseline utile deve confrontare almeno:

1. `current`
2. `current_plus_map`

su tutti i casi disponibili al momento del run.

Non costruire Router v2 prima di avere questo confronto, perché potrebbe emergere che la Retrieval Map da sola risolve una parte significativa del problema.

---

## 7. Ruolo di Codex

Codex è adatto a:

- orchestrare run isolati quando ha accesso al modello/configurazione da testare;
- catturare trace di file letti;
- normalizzare output JSONL;
- eseguire `score_routing_run.py`;
- produrre confronto A/B.

Non deve vedere il gold routing prima di generare il trace del modello testato.

---

## 8. Anti-contaminazione

Il gold standard vive nella stessa repo per auditabilità, ma il runner deve evitare di renderlo disponibile al modello sotto test durante l'esecuzione.

Una baseline in cui il modello legge `cases*.jsonl` completo prima di rispondere è invalida: misurerebbe la capacità di copiare il gold, non il retrieval dell'architettura.
