# Manual Corpus Inventory

## Scopo

Questo documento definisce il corpus che deve essere considerato durante la trasformazione della KB in manuale.

Non è ancora il semantic crosswalk: qui classifichiamo **i documenti**. Nella Fase 2 verranno classificate le singole unità di conoscenza contenute nei documenti.

Baseline dottrinale iniziale del progetto manuale:

`93f8eae978fdffb55c5623ae06603e5895b71e11`

## Classificazioni

### Tipo documento

- **DOCTRINE** — nodo specialistico che contiene conoscenza canonica sostanziale.
- **SYNTHESIS** — comprime o collega più nodi canonici senza essere la sede specialistica primaria.
- **ROUTING** — serve principalmente a navigare o diagnosticare dove cercare.
- **CASE/EXAMPLE** — materiale applicativo o casistico.
- **PROVENANCE/AUDIT** — serve a verificare origine, temporalità, copertura o stato.
- **GOVERNANCE** — regola il funzionamento del repository/progetto.

### Disposizione editoriale iniziale

- **PRIMARY** — fonte che deve essere semanticamente decomposta con priorità alta.
- **SUPPORTING** — fonte da usare per relazioni, caveat, procedure o integrazioni.
- **EXAMPLE** — fonte da trasformare in esempio/caso, non in teoria autonoma.
- **REFERENCE** — serve a verificare struttura, routing o provenance, non diventa prosa reader-facing direttamente.
- **EXCLUDED** — non entra nel manuale salvo motivo specifico.

La disposizione è iniziale e potrà cambiare nel crosswalk, ma ogni cambiamento deve essere esplicito.

---

# 1. Corpus canonico: `merenda/`

Totale censito: **60 file**.

## 1.1 Root `merenda/` — 2 file

| Path | Tipo | Disposizione | Nota |
|---|---|---|---|
| `merenda/INDEX.md` | ROUTING | REFERENCE | Porta d'ingresso e tassonomia corrente; non vincola il curriculum finale. |
| `merenda/DECISION_ROUTER.md` | SYNTHESIS / ROUTING | SUPPORTING | Fonte centrale per metodo diagnostico, priorità e sequenza causale. |

## 1.2 `00_fondamenti` — 3 file

| Path | Tipo | Disposizione | Nota |
|---|---|---|---|
| `merenda/00_fondamenti/README.md` | ROUTING | REFERENCE | Sintesi di sezione. |
| `merenda/00_fondamenti/marketing-first.md` | DOCTRINE | PRIMARY | Principio generatore e confini del marketing come progettazione del business. |
| `merenda/00_fondamenti/sistema-operativo-merenda.md` | SYNTHESIS | SUPPORTING | Architettura end-to-end e dipendenze fra livelli. |

## 1.3 `01_mercato` — 5 file

| Path | Tipo | Disposizione | Nota |
|---|---|---|---|
| `merenda/01_mercato/README.md` | ROUTING | REFERENCE | Sintesi di sezione. |
| `merenda/01_mercato/appropriatezza-clienti.md` | DOCTRINE | PRIMARY | Qualità economica del cliente, non solo possibilità di vendita. |
| `merenda/01_mercato/clienti-altospendenti.md` | DOCTRINE | PRIMARY | Segmentazione economica e valore dei clienti ad alta spesa. |
| `merenda/01_mercato/clienti-identificabili-e-target.md` | DOCTRINE | PRIMARY | Identificabilità, target e segmentazione operativa. |
| `merenda/01_mercato/quattro-domande-prima-di-lanciare.md` | DOCTRINE | PRIMARY | Gate di mercato prima di offerta/acquisizione. |

## 1.4 `02_posizionamento` — 4 file

| Path | Tipo | Disposizione | Nota |
|---|---|---|---|
| `merenda/02_posizionamento/README.md` | ROUTING | REFERENCE | Sintesi di sezione. |
| `merenda/02_posizionamento/differenziazione-operativa.md` | DOCTRINE | PRIMARY | Nodo centrale sul posizionamento reale e sulla differenza operativa. |
| `merenda/02_posizionamento/esempi-di-differenziazione.md` | CASE/EXAMPLE | EXAMPLE | Libreria di esempi da rielaborare pedagogicamente. |
| `merenda/02_posizionamento/estensioni-di-linea-e-architettura-brand.md` | DOCTRINE | PRIMARY | Focus, line extension, architettura di marca e prevalenza temporale. |

## 1.5 `03_offerta` — 4 file

| Path | Tipo | Disposizione | Nota |
|---|---|---|---|
| `merenda/03_offerta/README.md` | ROUTING | REFERENCE | Sintesi di sezione. |
| `merenda/03_offerta/front-end-e-back-end.md` | DOCTRINE | PRIMARY | Riduzione della barriera d'ingresso e monetizzazione successiva. |
| `merenda/03_offerta/offerta-a-risposta-diretta.md` | DOCTRINE | PRIMARY | Costruzione dell'offerta e risposta osservabile. |
| `merenda/03_offerta/prezzo-premium-e-percezione-del-valore.md` | DOCTRINE | PRIMARY | Pricing, premium, comparabilità, valore ed economics. |

## 1.6 `04_marketing` — 7 file

| Path | Tipo | Disposizione | Nota |
|---|---|---|---|
| `merenda/04_marketing/README.md` | ROUTING | REFERENCE | Sintesi di sezione. |
| `merenda/04_marketing/complessita-e-riduzione-variabili.md` | DOCTRINE | PRIMARY | Focus, test interpretabili e riduzione delle variabili. |
| `merenda/04_marketing/eventi-proprietari-vip-experience.md` | DOCTRINE / EXAMPLE | SUPPORTING | Evento proprietario ed esperienza come leva di marketing. |
| `merenda/04_marketing/gerarchia-domanda-e-canali.md` | DOCTRINE | PRIMARY | Domanda posseduta, attiva, latente, awareness e scelta canali. |
| `merenda/04_marketing/quattro-modalita-e-ritmo.md` | DOCTRINE | PRIMARY | Modalità di marketing e continuità/ritmo. |
| `merenda/04_marketing/riattivazione-clienti.md` | DOCTRINE | PRIMARY | Recupero di valore già acquisito. |
| `merenda/04_marketing/test-creativita-annunci.md` | DOCTRINE / PROCEDURE | SUPPORTING | Testing di creatività e annunci. |

## 1.7 `05_acquisizione` — 6 file

| Path | Tipo | Disposizione | Nota |
|---|---|---|---|
| `merenda/05_acquisizione/README.md` | ROUTING | REFERENCE | Sintesi di sezione. |
| `merenda/05_acquisizione/database-email-e-sequenze.md` | DOCTRINE | PRIMARY | Database, segmentazione, sequenze, progressive profiling e stato del prospect. |
| `merenda/05_acquisizione/funnel-e-conversione.md` | DOCTRINE | PRIMARY | Funnel come sistema di avanzamento e conversione. |
| `merenda/05_acquisizione/information-marketing.md` | DOCTRINE | PRIMARY | Pre-educazione e information marketing. |
| `merenda/05_acquisizione/partnership-distribuzione-e-combinazioni.md` | DOCTRINE | PRIMARY | Partnership, distribuzione e combinazioni di asset/canali. |
| `merenda/05_acquisizione/referral-e-soddisfazione.md` | DOCTRINE | PRIMARY | Referral progettato e relazione con soddisfazione/esperienza. |

## 1.8 `06_vendita` — 5 file

| Path | Tipo | Disposizione | Nota |
|---|---|---|---|
| `merenda/06_vendita/README.md` | ROUTING | REFERENCE | Sintesi di sezione; conferma struttura oggi frammentata. |
| `merenda/06_vendita/follow-up-lead-non-convertiti.md` | DOCTRINE / PROCEDURE | PRIMARY | Recupero opportunità e disciplina del follow-up. |
| `merenda/06_vendita/prequalifica-follow-up-decisori.md` | DOCTRINE | PRIMARY | Prequalifica, decisori, timing, speed-to-lead e pipeline. |
| `merenda/06_vendita/preventivo-consulenza-diagnosi.md` | DOCTRINE | PRIMARY | Vendita come diagnosi e prescrizione. |
| `merenda/06_vendita/rete-vendita-script-allenamento-e-controllo.md` | DOCTRINE | PRIMARY | Script, role-play, gestione rete e controllo. |

**Finding strutturale:** la conoscenza sostanziale esiste, ma manca una singola sequenza end-to-end canonica. Questo è un gap editoriale P1 e potrebbe anche rappresentare il gap canonico già segnalato dall'audit.

## 1.9 `07_copy_comunicazione` — 5 file

| Path | Tipo | Disposizione | Nota |
|---|---|---|---|
| `merenda/07_copy_comunicazione/README.md` | ROUTING | REFERENCE | Sintesi di sezione. |
| `merenda/07_copy_comunicazione/checklist-risposta-diretta.md` | DOCTRINE / PROCEDURE | SUPPORTING | Checklist operativa per direct response. |
| `merenda/07_copy_comunicazione/copy-posizionamento-e-temperatura-traffico.md` | DOCTRINE | PRIMARY | Prerequisiti strategici e adattamento a intento/awareness. |
| `merenda/07_copy_comunicazione/priorita-azione-e-inerzia.md` | DOCTRINE | PRIMARY | Trigger, priorità, inerzia e movimento verso l'azione. |
| `merenda/07_copy_comunicazione/scrittura-sales-letter-e-argomentazione.md` | DOCTRINE | PRIMARY | Struttura estesa dell'argomentazione e sales letter. |

## 1.10 `08_brand` — 6 file

| Path | Tipo | Disposizione | Nota |
|---|---|---|---|
| `merenda/08_brand/README.md` | ROUTING | REFERENCE | Sintesi di sezione. |
| `merenda/08_brand/autorita-e-marketing.md` | DOCTRINE | PRIMARY | Autorità e riduzione del costo di fiducia. |
| `merenda/08_brand/brand-community-e-fan.md` | DOCTRINE | SUPPORTING | Community, advocacy e fan. |
| `merenda/08_brand/pr-earned-media-e-notiziabilita.md` | DOCTRINE | SUPPORTING | Earned media e notiziabilità. |
| `merenda/08_brand/reputazione-e-crisis-management.md` | DOCTRINE | PRIMARY | Reputazione, esperienza e gestione delle crisi. |
| `merenda/08_brand/testimonianze-e-prova-sociale.md` | DOCTRINE | PRIMARY | Prova sociale e testimonianze. |

**Finding strutturale:** i componenti esistono ma la sequenza complessiva di costruzione del brand non ha ancora una casa sintetica unica. Gap editoriale P2 già coerente con il semantic audit.

## 1.11 `09_business` — 10 file

| Path | Tipo | Disposizione | Nota |
|---|---|---|---|
| `merenda/09_business/README.md` | ROUTING | REFERENCE | Sintesi di sezione. |
| `merenda/09_business/controlli-interni-e-rischio-operativo.md` | DOCTRINE | SUPPORTING | Controlli interni e rischio operativo. |
| `merenda/09_business/espansione-nicchie-e-multibrand.md` | DOCTRINE | PRIMARY | Espansione, nuove nicchie e multibrand. |
| `merenda/09_business/exit-readiness-e-trasferibilita.md` | DOCTRINE | SUPPORTING | Trasferibilità e dipendenza dall'imprenditore. |
| `merenda/09_business/marketing-del-personale.md` | DOCTRINE | SUPPORTING | Attrazione e selezione del personale come problema anche di marketing. |
| `merenda/09_business/numeri-cassa-e-crescita.md` | DOCTRINE | PRIMARY | Economics, CAC, LTV, payback, margine, cassa e crescita. |
| `merenda/09_business/partire-da-zero.md` | DOCTRINE | PRIMARY | Sequenza di apprendimento/validazione per chi parte senza prova. |
| `merenda/09_business/patrimonializzazione-e-reinvestimento.md` | DOCTRINE | SUPPORTING | Reinvestimento e patrimonializzazione. |
| `merenda/09_business/retention-onboarding-e-customer-success.md` | DOCTRINE | PRIMARY | Onboarding, esperienza, retention e customer success. |
| `merenda/09_business/scalabilita-e-operativita.md` | DOCTRINE | PRIMARY | Capacità, standardizzazione, scala e operatività. |

## 1.12 `10_casi_studio` — 3 file

| Path | Tipo | Disposizione | Nota |
|---|---|---|---|
| `merenda/10_casi_studio/README.md` | ROUTING | REFERENCE | Sezione casistica ancora piccola. |
| `merenda/10_casi_studio/focalizzazione-funnel-e-capacita.md` | CASE/EXAMPLE | EXAMPLE | Caso multi-concetto da scomporre o usare end-to-end. |
| `merenda/10_casi_studio/motoargento-focalizzazione.md` | CASE/EXAMPLE | EXAMPLE | Caso di focalizzazione. |

**Finding strutturale:** la libreria casi è troppo piccola per sostenere da sola un manuale didattico completo. Gli esempi dovranno essere estratti anche dai nodi specialistici e, quando necessario, riscritti o creati come esempi sintetici coerenti con la dottrina.

---

# 2. Conteggio per funzione editoriale

Il conteggio documentale iniziale è:

- 11 README di sezione → ROUTING / REFERENCE;
- 2 file root `merenda/` → 1 ROUTING, 1 SYNTHESIS/ROUTING;
- 44 nodi specialistici non-caso → principalmente DOCTRINE;
- 3 file con funzione principalmente CASE/EXAMPLE (`esempi-di-differenziazione.md` + 2 casi studio);
- totale canonico censito → **60 file**.

La Fase 2 potrà mostrare che singoli documenti contengono unità appartenenti a più funzioni. Questo inventario non deve quindi essere usato come sostituto del semantic crosswalk.

---

# 3. Corpus di supporto interpretativo e provenance

Questi file **non sono parte del teaching corpus primario**, ma devono essere consultati quando servono per non interpretare male il doctrine layer.

| Path | Tipo | Disposizione | Funzione |
|---|---|---|---|
| `00_START_HERE.md` | GOVERNANCE | REFERENCE | Stato e bootstrap del repository. |
| `LAYER1_CONTRACT.md` | GOVERNANCE | REFERENCE | Confini e ruolo del doctrine layer. |
| `MERENDA_MODE.md` | GOVERNANCE / SYNTHESIS | REFERENCE | Profilo di ragionamento/comunicazione; non è fonte primaria autonoma di dottrina. |
| `FORMALIFE_REBUILD_PROTOCOL.md` | APPLICATION SYNTHESIS | REFERENCE | Applicazione zero-based a Formalife; utile come controllo di sequenza, non come testo del manuale. |
| `STATUS.md` | GOVERNANCE | REFERENCE | Stato operativo e gap correnti. |
| `reviews/FINAL_SEMANTIC_AUDIT.md` | PROVENANCE/AUDIT | REFERENCE | Coerenza, gap, prevalenza temporale e maturità del corpus. |
| `sources/merenda-sources/README.md` | PROVENANCE | REFERENCE | Regole del source-agnostic layer. |
| `sources/merenda-sources/collections.json` | PROVENANCE | REFERENCE | Distingue collezioni primary, assimilated e deferred. |
| `sources/merenda-sources/catalog.json` | PROVENANCE | REFERENCE | Registry delle fonti source-agnostic. |
| `MASTER_PLAN.md` | GOVERNANCE | EXCLUDED | Processo storico del progetto; non teaching source. |
| `system/RULES.md` | GOVERNANCE | EXCLUDED | Regole operative storiche/frozen; non teaching source. |
| `system/PHASES.md` | GOVERNANCE | EXCLUDED | Workflow interno del progetto. |
| `system/HANDOFFS.md` | GOVERNANCE | EXCLUDED | Handoff fra agenti. |
| `system/FROZEN_FILES.md` | GOVERNANCE | EXCLUDED | Protezione file di sistema. |

## Raw sources e review per-source

Le fonti grezze, transcript e review per-source sotto `sources/` **non vengono enumerati come teaching corpus del manuale**.

Motivo: la dottrina consolidata vive in `merenda/`. Tornare automaticamente alle 313 unità YouTube processate o alle 166 fonti source-agnostic trasformerebbe il progetto manuale in una seconda ingestion completa e romperebbe la regola canonica di consolidamento.

Le fonti originali vengono riaperte solo quando servono per:

- verificare provenance;
- risolvere un conflitto;
- capire un caveat temporale;
- recuperare un esempio utile;
- verificare un possibile gap dottrinale.

---

# 4. Findings della Fase 1 già confermati

## F1 — La tassonomia della KB non è il curriculum

Le 11 sezioni sono efficaci come doctrine/routing layer, ma mescolano livelli diversi dal punto di vista didattico. Per esempio `09_business` contiene sia economics fondamentali sia exit readiness ed espansione, che richiedono prerequisiti molto diversi.

## F2 — Vendita richiede sintesi end-to-end

I quattro nodi specialistici coprono molte componenti, ma non esiste ancora un singolo percorso completo dal pre-ingresso alla decisione e al follow-up.

## F3 — Brand richiede una sequenza unificata

Autorità, prova, reputazione, PR e community sono coperti, ma il lettore principiante non dovrebbe dover ricostruire da solo come si concatenano.

## F4 — Voice of Customer / ricerca non ha casa autonoma

Il gap già segnalato dal semantic audit resta rilevante per un manuale beginner-first: tecniche e segnali sono distribuiti in mercato, testimonianze, query/intento, competitor e clienti migliori.

## F5 — Casi insufficienti come libreria autonoma

La sezione casi studio contiene soltanto due casi sostanziali. Il manuale dovrà costruire una vera strategia esempi/casi usando anche materiale disperso e casi sintetici riscritti.

## F6 — Il manuale deve anticipare gli economics rispetto alla tassonomia attuale

`numeri-cassa-e-crescita.md` vive oggi in `09_business`, ma concetti come margine, CAC, payback, LTV e cost-to-serve sono prerequisiti per capire qualità del cliente, offerta, acquisizione e scala. Nel curriculum almeno una parte degli economics dovrà quindi essere introdotta molto prima della sezione finale sul business.

---

# 5. Gate Fase 1 — stato

### Censimento `merenda/`

**COMPLETO — 60/60 file classificati a livello documentale.**

### Corpus di supporto interpretativo

**COMPLETO a livello di classi di documento.**

### Gap iniziali

**IDENTIFICATI, da formalizzare in `manual/MANUAL_GAPS.md`.**

### Passo successivo

Creare `manual/MANUAL_GAPS.md`, poi chiudere formalmente la Fase 1 e iniziare la semantic decomposition della Fase 2.
