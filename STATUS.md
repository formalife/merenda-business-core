# PROJECT STATUS

## Stato generale

**MERENDA BUSINESS CORE — LAYER 1 OPERATIONAL. ARCHITECTURE REVIEW VALIDATED; MANUAL PUBLISHING PROJECT ACTIVE.**

Il repository svolge due funzioni distinte:

1. **Layer 1 canonico** — doctrine, routing, diagnosi e disciplina decisionale sotto `merenda/`;
2. **publishing layer derivato** — progetto manuale sotto `manual/`, che non prevale mai sulla doctrine canonica.

La doctrine sotto `merenda/` e `merenda/DECISION_ROUTER.md` non è stata modificata dalla Architecture Review.

La fase YouTube generalista resta chiusa a 313 contenuti processati semanticamente. Il corpus source-agnostic corrente resta 166/166 studiato. I 155 residui YouTube sono intenzionali e non costituiscono backlog automatico.

---

## Priorità operative correnti

### 1. Architecture Review Layer 1 — VALIDATED / ADOPTION

La nuova architettura strategico-diagnostica candidata è:

**`REASONING_KERNEL.md` → compact semantic routing → semantic entry selettive → sezione canonica minima → sufficiency check → structural/parent expansion → full-node fallback.**

Decision record:

`reviews/behavioral/HOLDOUT_V1_UNBLINDED_ARCHITECTURE_DECISION_2026-09-21.md`

### 2. Manual publishing project — ACTIVE

Publishing layer:

`manual/`

Control plane editoriale:

- `manual/README.md`
- `manual/ROADMAP.md`
- `manual/STATUS.md`
- `manual/MANUAL_CONTRACT.md`

La priorità editoriale corrente richiesta dal founder resta il progetto manuale. Il suo avanzamento dettagliato è governato da `manual/STATUS.md`; il root `STATUS.md` non duplica più contatori editoriali che possono diventare rapidamente stale.

`manual/` è derivato: non diventa doctrine canonica e non modifica `merenda/` per esigenze puramente editoriali.

---

## Architecture Review — risultato finale

### Behavioral baseline congelata

| Configurazione | Required-check recall | Material inversions |
|---|---:|---:|
| `current` | 93/96 = 96.875% | 0 |
| `current_plus_map` | 95/96 = 98.958% | 0 |

File-level recall storico è stato declassato come metrica primaria perché penalizzava retrieval semanticamente corretto a livello sub-file.

### Context baseline

| Metrica media/caso | `current` | `current_plus_map` |
|---|---:|---:|
| reconstructed chars | 130,511 | 137,128 |
| control-plane chars | 92,751 | 91,985 |
| specialist doctrine | 27,136 | 20,589 |

Finding: il bootstrap/control plane era il costo dominante.

### Structural + semantic retrieval

- Structural Index: 60 documenti, 912 sezioni, schema 1.1;
- semantic registry runtime: 42 semantic units;
- semantic Map/index = precision signal, non filtro esclusivo;
- structural discovery = recall safety net;
- file ≠ unità primaria di retrieval;
- Router v2 non necessario;
- embeddings/reranking/GraphRAG non giustificati dai failure osservati.

### Prototype A3 development stabilization

Smoke A3:

- semantic verified recall: 0.9444;
- focused precision: 0.8889;
- answer-only: 18/19 required checks;
- 0 material inversions;
- mean reconstructed context: 110,373 chars/case;
- specialist doctrine: 6,580 chars/case.

Focused gate R020+R027:

- retrieval recall 1.0000;
- precision 0.9000;
- answer-only 7/7;
- 0 material inversions.

I 30 development cases restano regression suite, non holdout indipendente.

### Blind Architecture Holdout v1 — PASS

Sei casi nuovi / 18 required checks, senza nuove semantic unit create per il holdout.

Blind judgment congelato prima del mapping:

| Variant | Required checks | Full-pass | Material inversions |
|---|---:|---:|---:|
| A | 18/18 | 6/6 | 0 |
| B | 18/18 | 6/6 | 0 |

Dopo unblinding:

- A3 + five-file full bootstrap: **18/18**;
- A3 + Compact Reasoning Kernel: **18/18**;
- observed fidelity delta: **0**.

Context economics paired holdout:

- full architecture: **120,116 chars/case**;
- compact-kernel architecture: **34,288 chars/case**;
- delta: **−71.5%**.

Fixed bootstrap validation senza Codex:

- five full control-plane files: **89,192 chars**;
- compact kernel: **11,324 chars**;
- riduzione: **~87.3%**.

---

## Control plane corrente candidato

Operational artifact:

`REASONING_KERNEL.md`

Regole:

1. strategic/diagnostic startup: kernel compatto, non preload dei cinque full control-plane file;
2. doctrine specialistica canonica prevale sempre quando più recente/precisa/contestuale;
3. full control-plane documents restano governance/reference/fallback;
4. progressive disclosure fino alla sezione minima sufficiente;
5. non comprimere ulteriormente il kernel senza nuova paired evaluation con expected gain materiale;
6. nuova CI `Validate Reasoning Kernel` impedisce drift semantico silenzioso rispetto al corpo v1 behaviorally validated.

Entry point aggiornati:

- `00_START_HERE.md`
- `CHATGPT.md`

---

## Manual publishing layer

Il progetto editoriale sotto `manual/` prosegue separatamente dall'Architecture Review.

Regole di separazione:

- `merenda/` resta l'unico doctrine layer canonico;
- `manual/` organizza e insegna la doctrine, non la riscrive implicitamente;
- gap editoriali non giustificano automaticamente nuova acquisizione o nuove regole canoniche;
- crosswalk, curriculum, glossary, case inventory e provenance map restano publishing assets derivati.

Per lo stato esatto e il prossimo passo del manuale, leggere sempre `manual/STATUS.md` live.

---

## Contatori canonici — corpus YouTube storico

- Video individuati: 468
- Video completati: 307
- Video esclusi: 6
- Video rimanenti: 155
- Processati semanticamente: 313

I 155 residui sono intenzionali e non costituiscono backlog automatico.

## Contatori canonici — source-agnostic

- Nuove fonti Merenda registrate: 166
- Nuove fonti Merenda studiate: 166
- Nuove fonti Merenda escluse: 0
- Nuove fonti Merenda da processare: 0

Trattamenti rilevanti:

- `MERENDA_PRIMARY`
- `ASSIMILATED_AS_MERENDA_BY_USER`
- `DEFERRED_EXTERNAL_GENERAL_UPDATE`

La provenance reale non viene mai falsificata.

---

## Invarianti Layer 1

- `merenda/` resta doctrine canonica;
- `manual/` resta publishing layer derivato;
- Formalife resta Layer 2, non doctrine;
- una fonte assimilata non viene attribuita a Frank;
- `MERGE, NOT APPEND` resta la regola di consolidamento;
- lock YouTube attivo;
- file frozen invariati salvo autorizzazione esplicita;
- risultati Formalife non diventano automaticamente principi generali.

---

## Next actions

### Architecture

- merge della Architecture Review dopo riallineamento con `main`;
- poi merge della PR Layer 2 che aggiorna `PROJECT_BOOTSTRAP.md` e `LAYER1_REF.md`;
- infine aggiornare le ChatGPT Project Instructions con `formalife/formalife-company-os/PROJECT_INSTRUCTIONS_V2.md`.

Non sono giustificati altri test Codex-heavy prima di una modifica architetturale materiale o di un nuovo failure reale.

### Manual

Proseguire secondo `manual/STATUS.md` e `manual/ROADMAP.md`, preservando la separazione doctrine/publishing.
