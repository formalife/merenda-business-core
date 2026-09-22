# Sandler Integration — Merge Gate — 2026-09-22

## Scopo

Questo documento governa l'ultimo gate prima del merge della PR `#16` (`integrate-sandler-v1` → `main`).

La doctrine, il routing semantico e il manuale hanno già superato i gate statici. Il residuo non è editoriale: è **comportamentale**.

La domanda da chiudere è doppia:

1. la nuova doctrine/routing sales porta il modello ai gate corretti sui casi R031–R041?;
2. il `REASONING_KERNEL.md` promosso preserva la stessa disciplina del full control plane sui medesimi casi?

Il merge resta chiuso finché entrambe le domande non hanno evidenza sufficiente.

---

# 1. Stato statico già richiesto

Prima del test comportamentale devono essere verdi sulla head testata:

- `scripts/validate_project.py`;
- `scripts/validate_routing_evals.py`;
- `scripts/validate_architecture_holdout.py`;
- `scripts/validate_retrieval_map.py`;
- `scripts/validate_semantic_gold_v2.py`;
- static routing addressability;
- build structural/semantic indexes;
- Reasoning Kernel validator;
- compile dei runner di Architecture Review;
- dry-run `scripts/run_sandler_integration_ab_host.py --validate-only`.

La manual revalidation vive in:

- `manual/PHASE5_SALES_REVALIDATION_2026-09-22.md`.

Verdict manuale corrente: **PASS — nessun gap P0/P1**.

---

# 2. Suite congelata

Casi:

- `R031` — pipeline bassa / outbound prematuro;
- `R032` — meeting senza outcome / closing aggressivo;
- `R033` — surface problem → demo prematura;
- `R034` — Pain forte / Budget ignoto;
- `R035` — referente entusiasta / Decision opaca;
- `R036` — over-presentation / Fulfillment;
- `R037` — tattica conversazionale resa universale;
- `R038` — silenzio post-proposta / cadence universale;
- `R039` — seller conosce lo script ma evita domande difficili;
- `R040` — team sotto quota / aumento uniforme activity;
- `R041` — cliente soddisfatto / upsell automatico.

Source of truth:

- `evals/routing/cases_phase6.jsonl`;
- `evals/routing/semantic_gold_phase6.jsonl`.

Non modificare case o gold dopo avere visto i trace, salvo errore dimostrabile dell'eval. In quel caso il cambio va documentato e l'intera suite va rigenerata.

---

# 3. Configurazioni A/B

Runner:

```bash
python3 scripts/run_sandler_integration_ab_host.py --validate-only
python3 scripts/run_sandler_integration_ab_host.py
```

Il runner usa la stessa doctrine specialistica e lo stesso retrieval architecture A3 in entrambe le varianti.

Differenza controllata:

- `sandler_a3_full` → cinque control-plane completi;
- `sandler_a3_kernel` → `REASONING_KERNEL.md` promosso.

Il kernel testato è quello operativo root, non il vecchio draft `reviews/drafts/COMPACT_REASONING_KERNEL_V1.md`.

Ogni caso usa un processo Codex isolato; gold/review non entrano nello sterile workspace.

Output principali sotto `/tmp/formalife-sandler-integration-ab`:

- `full/holdout-trace.jsonl`;
- `kernel/holdout-trace.jsonl`;
- `full/semantic-score.json`;
- `kernel/semantic-score.json`;
- `semantic-ab-summary.json`;
- `sandler-blind-answer-bundle.jsonl`;
- `sandler-blind-mapping.json`.

**Non rivelare il mapping A/B prima del judgment delle risposte.**

---

# 4. Gate deterministico di retrieval

Per entrambe le configurazioni:

- 11 casi presenti;
- `cases_full_verified_recall = 11/11`;
- nessuna semantic unit `required` mancante;
- nessun canonical pointer verso routing alias legacy;
- nessuna contamination da gold/review.

La precisione è diagnostica, non un hard gate autonomo.

Una semantic unit opzionale o un upstream realmente necessario possono essere corretti. L'over-retrieval diventa failure solo se diluisce materialmente diagnosi, priorità o risposta.

---

# 5. Gate comportamentale blinded

Prima di rivelare il mapping, giudicare A e B per ciascun caso contro `required_checks`, `forbidden_shortcuts`, provenance e expected behavior.

Per il PASS di una configurazione su un caso:

- tutti i `required_checks` materialmente soddisfatti;
- nessun `forbidden_shortcut` attivato;
- `provenance_error = false`;
- nessuna unsupported inference che cambi materialmente la decisione;
- nessuna tattica prematura;
- nessun founder-accommodation failure;
- `material_failure = false`.

Differenze di stile o formulazione non bloccano il gate.

## Gate finale richiesto

**FULL: 11/11 PASS senza material failure.**  
**KERNEL: 11/11 PASS senza material failure.**

Il kernel non deve essere promosso/modificato per ottenere una risposta “più completa”; deve cambiare solo se la compressione perde disciplina decisionale necessaria.

---

# 6. Matrice diagnostica dei failure

## A. Full FAIL + Kernel FAIL sullo stesso caso

Prima ipotesi:

- routing/map;
- canonical node;
- gold troppo grossolano/errato;
- synthesis/application failure condivisa.

**Non modificare il kernel come prima risposta.**

Correggere la causa comune, poi rigenerare entrambe le varianti.

## B. Full PASS + Kernel FAIL

Questo è l'unico scenario che può mettere in discussione il kernel.

Prima di editarlo verificare:

1. quali semantic unit sono state selezionate;
2. quali sono state canonicalmente verificate;
3. se il kernel ha saltato un prerequisito nonostante semantic routing sufficiente;
4. se il full control plane ha fornito una disciplina realmente assente dal kernel;
5. se la differenza è materialmente ripetibile e non puro wording/stocasticità.

Possibili classificazioni:

- kernel routing cue missing;
- kernel causal rule missing;
- bootstrap dilution/selection difference;
- correct retrieval, bad synthesis non causato dal kernel.

Solo una omissione causale/materiale giustifica un kernel change.

## C. Full FAIL + Kernel PASS

Il merge resta chiuso.

Non usare il successo del kernel per ignorare il failure full. Isolare se il full bootstrap ha introdotto dilution oppure se il run è anomalo. Un asymmetric material failure va spiegato prima del merge.

## D. Full PASS + Kernel PASS

**Nessun kernel change.**

La specialist doctrine rimane più precisa e continua a prevalere sul kernel.

---

# 7. Regole di rerun

Se cambia uno fra:

- doctrine sales/acquisition/lifecycle coinvolta;
- semantic map;
- semantic gold;
- `REASONING_KERNEL.md`;
- runner/retrieval logic;

la suite R031–R041 deve essere rigenerata sulla nuova head.

Un rerun mirato può servire per diagnosi, ma il merge richiede alla fine un pass completo A/B sulla head finale.

---

# 8. Condizione di merge

La PR può passare da draft a ready e poi essere mergiata solo quando:

1. CI statico è verde sulla head finale;
2. dry-run A/B è verde;
3. full = 11/11 required semantic recall + 11/11 behavioral PASS;
4. kernel = 11/11 required semantic recall + 11/11 behavioral PASS;
5. provenance failures = 0;
6. material failures = 0;
7. eventuali correzioni successive sono state incluse in un ultimo full rerun;
8. il mapping A/B è rivelato solo dopo il judgment congelato.

Fino ad allora:

**KEEP PR #16 DRAFT — DO NOT MERGE.**
