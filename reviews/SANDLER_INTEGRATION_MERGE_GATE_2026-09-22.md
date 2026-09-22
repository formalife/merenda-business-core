# Sandler Integration — Merge Gate — 2026-09-22

## Scopo

Questo documento governa l'ultimo gate prima del merge della PR `#16` (`integrate-sandler-v1` → `main`).

La doctrine, il routing semantico e il manuale hanno già superato i gate statici. Il residuo è comportamentale: verificare che la nuova doctrine/routing sales porti il modello ai gate corretti e che il `REASONING_KERNEL.md` preservi la disciplina necessaria rispetto al full control plane.

---

# 1. Stato statico richiesto

Prima di qualunque behavioral test devono essere verdi sulla head testata:

- `scripts/validate_project.py`;
- `scripts/validate_routing_evals.py`;
- `scripts/validate_architecture_holdout.py`;
- `scripts/validate_retrieval_map.py`;
- `scripts/validate_semantic_gold_v2.py`;
- static routing addressability;
- build structural/semantic indexes;
- Reasoning Kernel validator;
- compile dei runner;
- dry-run `scripts/run_sandler_integration_ab_host.py --validate-only` oppure, per rerun mirato, lo stesso comando con `--cases`.

Manual revalidation: `manual/PHASE5_SALES_REVALIDATION_2026-09-22.md` — PASS, nessun gap P0/P1.

---

# 2. Suite Phase 6

Casi canonici:

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

Case/gold non vanno modificati dopo avere visto i trace salvo errore dimostrabile dell'eval. Ogni correzione deve essere documentata con causa e impatto.

---

# 3. Configurazioni A/B

Runner completo:

```bash
python3 scripts/run_sandler_integration_ab_host.py --validate-only
python3 scripts/run_sandler_integration_ab_host.py
```

Runner mirato:

```bash
python3 scripts/run_sandler_integration_ab_host.py --cases R033,R041 --validate-only
python3 scripts/run_sandler_integration_ab_host.py --cases R033,R041
```

Differenza controllata:

- `sandler_a3_full` → cinque control-plane completi;
- `sandler_a3_kernel` → `REASONING_KERNEL.md` promosso.

Doctrine specialistica, semantic routing, model, effort e isolamento restano identici. Full e Kernel devono sempre usare lo stesso insieme di casi.

**Non rivelare il mapping A/B prima del judgment delle risposte.**

---

# 4. Gate deterministico di retrieval

Per ogni caso effettivamente eseguito e per entrambe le configurazioni:

- required semantic recall completo;
- nessuna semantic unit `required` mancante;
- nessun canonical pointer verso routing alias legacy;
- nessuna contamination da gold/review.

La precisione è diagnostica, non hard gate autonomo. Over-retrieval è failure solo se degrada materialmente diagnosi, priorità o risposta.

---

# 5. Gate comportamentale blinded

Prima di rivelare il mapping, giudicare A e B per ogni caso eseguito contro `required_checks`, `forbidden_shortcuts`, provenance ed expected behavior.

PASS per una configurazione/caso richiede:

- tutti i required checks materialmente soddisfatti;
- nessun forbidden shortcut;
- `provenance_error = false`;
- nessuna unsupported inference materialmente decisiva;
- nessuna tattica prematura;
- nessun founder-accommodation failure;
- `material_failure = false`.

Differenze stilistiche non bloccano il gate.

---

# 6. Matrice diagnostica

## A. Full FAIL + Kernel FAIL

Prima ipotesi: routing/map, canonical node, gold troppo grossolano o synthesis failure condivisa. Non modificare il kernel come prima risposta.

## B. Full PASS + Kernel FAIL

È l'unico scenario che può mettere in discussione il kernel. Prima di editarlo verificare semantic units selezionate/verificate, prerequisiti saltati, differenze del full control plane e ripetibilità materiale.

## C. Full FAIL + Kernel PASS

Il gate resta chiuso finché il failure full non è spiegato.

## D. Full PASS + Kernel PASS

Nessun kernel change. Specialist doctrine continua a prevalere sul kernel.

---

# 7. Regole di rerun proporzionate all'impatto

Il behavioral rerun deve essere proporzionato alla superficie realmente cambiata.

## Rerun completo obbligatorio

Rieseguire tutta R031–R041 su Full + Kernel quando cambia uno fra:

- doctrine sales/acquisition/lifecycle con impatto trasversale;
- `REASONING_KERNEL.md`;
- retrieval logic/runner semantics;
- semantic map con dipendenze trasversali non circoscrivibili;
- case/gold multipli tali da rendere incerto l'impact boundary.

## Rerun mirato ammesso

È sufficiente un rerun mirato Full + Kernel quando **tutte** queste condizioni sono vere:

1. la correzione è localizzata a casi identificabili;
2. doctrine specialistica e kernel non sono cambiati;
3. retrieval engine/runner semantics non sono cambiati, salvo supporto neutro per il filtro casi;
4. CI/validator statici dell'intera suite restano verdi;
5. i casi non coinvolti avevano già PASS comportamentale senza material/provenance failure;
6. il rerun include sia Full sia Kernel sugli stessi casi impattati;
7. il judgment del rerun resta blinded fino al freeze dei giudizi.

Se il rerun mirato produce un failure inatteso o suggerisce impatto più ampio, si espande il perimetro o si torna al rerun completo.

### Applicazione corrente

La correzione post-unblinding del 2026-09-22 riguarda esclusivamente:

- `R033`: rendere semanticamente obbligatoria la sequenza Pain → Budget → Decision → Fulfillment prima di demo/proposta;
- `R041`: rendere esplicito che una nuova opportunity di account growth rientra in Pain → Budget → Decision prima della proposta.

Doctrine e `REASONING_KERNEL.md` sono invariati; i validator dell'intera suite sono verdi. Quindi il rerun richiesto è **R033 + R041, Full + Kernel = 4 run**.

---

# 8. Condizione di merge

Per questa integrazione la PR può passare da draft a ready e poi essere mergiata quando:

1. CI statico è verde sulla head finale;
2. dry-run mirato R033,R041 è verde;
3. Full passa R033 e R041 con required semantic recall completo e zero material/provenance failure;
4. Kernel passa R033 e R041 con required semantic recall completo e zero material/provenance failure;
5. i precedenti PASS R031,R032,R034–R040 restano validi perché nessuna doctrine/kernel/retrieval logic pertinente è stata modificata;
6. il mapping del rerun mirato viene rivelato solo dopo judgment congelato;
7. se il rerun mirato evidenzia nuova superficie d'impatto, il gate si riallarga prima del merge.

Fino ad allora:

**KEEP PR #16 DRAFT — DO NOT MERGE.**
