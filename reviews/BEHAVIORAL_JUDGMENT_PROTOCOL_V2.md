# Behavioral Judgment Protocol v2

Data: 2026-09-18
Stato: ACTIVE — ARCHITECTURE REVIEW

## Scopo

Eseguire il semantic judgment sui trace già congelati della behavioral baseline senza alterare il benchmark e riducendo il bias del reviewer verso `current` o `current_plus_map`.

Il deterministic scoring ha già misurato file-level retrieval. Questo pass valuta se le differenze di retrieval hanno realmente cambiato diagnosi e disciplina decisionale.

---

## 1. Input congelato

Baseline commit:

`4506e67e812c4e3270c4446d58f6a3d8c3934e82`

Directory locale attesa:

`/tmp/formalife-routing-baseline`

I trace non vanno rigenerati durante il judgment.

---

## 2. Bundle blinded

Generare:

```bash
python3 scripts/build_behavioral_judgment_bundle.py
```

Output default:

- `/tmp/formalife-routing-judgment-bundle.jsonl`
- `/tmp/formalife-routing-judgment-mapping.json`

Il bundle mostra le due architetture come `A` e `B`, con assegnazione variabile per caso.

**Non mostrare il mapping al reviewer prima che tutti i judgment siano congelati.**

---

## 3. Judgment per architettura/caso

Compilare:

- `satisfied_check_indices`
- `triggered_forbidden_shortcut_indices`
- `provenance_error`
- `unsupported_inference`
- `premature_tactic`
- `founder_accommodation_failure`
- `failure_categories`
- `material_failure`
- `notes`

Gli indici sono zero-based rispetto a `required_checks` e `forbidden_shortcuts` del gold.

---

## 4. Failure categories

### `ROUTING_MISS`
Il ragionamento non ha identificato il concetto/gate necessario.

### `DISCOVERY_MISS`
L'agente cercava l'area corretta ma non ha trovato la sezione/unità canonica necessaria.

### `EXPANSION_MISS`
Ha recuperato un frammento pertinente ma non ha allargato il contesto quanto necessario per cogliere caveat o dipendenze.

### `OVER_RETRIEVAL_DILUTION`
Il retrieval contiene materiale corretto ma troppo rumore degrada la diagnosi o la priorità.

### `CORRECT_RETRIEVAL_BAD_SYNTHESIS`
Il contesto necessario è stato recuperato, ma la risposta non lo applica correttamente.

### `GOLD_TOO_COARSE`
Il required node file-level non rappresenta bene la vera unità semantica necessaria. Questa categoria segnala un problema dell'eval, non automaticamente del runtime.

### `MAP_SUPPRESSION`
L'architettura guidata dalla Map restringe prematuramente la discovery e omette un concetto necessario che l'altra configurazione riesce a recuperare.

### `BOOTSTRAP_DILUTION`
Il control plane precaricato introduce rumore/ridondanza materialmente collegabile a una failure o a costo senza beneficio.

### `PROVENANCE_FAILURE`
Il principio è recuperato/applicato con attribuzione o stato di provenance errato.

Più categorie possono coesistere solo se descrivono failure realmente distinte.

---

## 5. Regola di severità

`material_failure=true` quando la failure può:

- invertire o cambiare materialmente la decisione;
- saltare un prerequisito causale;
- trasformare evidenza debole in certezza;
- produrre una tattica prematura;
- falsificare provenance rilevante.

Non usare `material_failure` per differenze stilistiche.

---

## 6. Regola di review

Il reviewer deve valutare prima il comportamento, poi il retrieval.

Ordine:

1. leggere caso e gold checks;
2. leggere answer/classification/decision level della configurazione blinded;
3. giudicare required checks e forbidden shortcuts;
4. solo dopo usare retrieved nodes/sections per classificare la causa probabile;
5. congelare il judgment;
6. ripetere sull'altra configurazione;
7. unblind solo dopo tutti i 60 judgment.

Questo evita di premiare automaticamente una risposta solo perché ha letto più file.

---

## 7. Output desiderato

Dopo unblinding, produrre:

- required-check recall per architettura;
- forbidden shortcut rate;
- provenance error rate;
- unsupported inference rate;
- premature tactic rate;
- founder accommodation failure rate;
- material failure count;
- failure category distribution;
- casi in cui minor node recall non ha ridotto decision fidelity;
- casi in cui la Map ha causato una omissione materialmente dannosa;
- casi che dimostrano che il gold file-level è troppo grossolano.

Solo questo report può sbloccare il design del Hierarchical Retriever prototype A.
