# Manual Gaps Register

## Scopo

Questo registro contiene i gap che possono impedire al publishing layer di diventare un manuale autosufficiente per un lettore principiante.

Classificazioni:

- **EDITORIAL GAP** — conoscenza presente ma dispersa/duplicata/non sequenziata;
- **CURRICULUM GAP** — conoscenza presente ma collocata male rispetto ai prerequisiti;
- **DOCTRINAL GAP** — conoscenza canonica insufficiente;
- **PROVENANCE GAP** — tracciabilità insufficiente;
- **CASE GAP** — materiale applicativo insufficiente.

Regola: tentare prima la soluzione editoriale quando la conoscenza esiste già. Non modificare `merenda/` per risolvere problemi di sintesi.

---

# Gap attivi

**Nessun gap P1/P2 attivo che impedisca l'avvio delle chapter specs.**

Restano normali attività di finalizzazione — copy-edit del glossario, selezione definitiva dei casi e controllo chapter-by-chapter — ma non sono più gap strutturali della conoscenza o dell'architettura.

---

# Gap risolti editorialmente

## G-001 — Processo di vendita end-to-end

**Priorità: P1**  
**Tipo: EDITORIAL GAP**  
**Stato: RESOLVED EDITORIALLY — 2026-09-20**

Sequenza consolidata:

**handoff/preparazione → prequalifica → presa in carico → diagnosi → criteri decisionali → prescrizione/prova → proposta/prezzo → verifica delle certezze → decisione → follow-up/no-sale classification → feedback/review.**

Evidenza: `manual/crosswalk/06_vendita.md`; curriculum Capp. 22–24.

---

## G-002 — Libreria casi didattici insufficiente

**Priorità: P1**  
**Tipo: CASE GAP**  
**Stato: RESOLVED EDITORIALLY — 2026-09-20**

### Evidenza di chiusura

`manual/CASE_INVENTORY.md` organizza i casi reali disponibili.

`manual/syntheses/synthetic-cases.md` aggiunge sei casi esplicitamente fittizi e didattici per i blocchi prima scoperti:

- SC-001 — VoC → target → positioning;
- SC-002 — pricing/economics;
- SC-003 — vendita end-to-end;
- SC-004 — customer lifecycle;
- SC-005 — founder dependence/transferability;
- SC-006 — brand accumulation.

I casi sintetici non vengono trattati come prova o benchmark.

---

## G-003 — Doctrine/provenance map

**Priorità: P1**  
**Tipo: PROVENANCE GAP / EDITORIAL INFRASTRUCTURE**  
**Stato: RESOLVED EDITORIALLY — 2026-09-20**

Evidenza: `manual/PROVENANCE_MAP.md`.

La mappa preserva source family, temporal precedence, contributi assimilati e sintesi editoriali senza replicare l'intero source registry.

---

## G-004 — Sintesi organica della costruzione del brand

**Priorità: P2**  
**Tipo: EDITORIAL GAP**  
**Stato: RESOLVED EDITORIALLY — 2026-09-20**

Sintesi:

**posizione/significato → authority/credibility/proof → esperienza reale → reputazione → memoria → advocacy/community.**

Nel curriculum la causalità è distribuita:

- positioning → Capp. 9–10;
- authority/proof → Cap. 14;
- customer experience → Cap. 25;
- referral/reviews → Cap. 27;
- reputation → Cap. 28;
- memory/community → Cap. 29.

---

## G-005 — Voice of Customer / ricerca di mercato

**Priorità: P2**  
**Tipo: EDITORIAL GAP**  
**Stato: RESOLVED EDITORIALLY — 2026-09-20**

### Evidenza di chiusura

Creato `manual/syntheses/voice-of-customer.md`.

La sintesi copre:

1. decisione che la ricerca deve informare;
2. evidence base pre-intervista;
3. selezione dei gruppi da ascoltare;
4. interviste ancorate a eventi e non suggerite;
5. complaint mining;
6. separazione evidenza/interpretazione;
7. frequenza, intensità, valore economico e comportamento;
8. triangolazione;
9. Market Evidence Map;
10. passaggio dalla sintesi al test comportamentale;
11. minimum viable research per chi parte da zero.

Non è emersa necessità di modificare il doctrine layer.

---

## G-006 — Economics fondamentali collocati troppo tardi

**Priorità: P1**  
**Tipo: CURRICULUM GAP**  
**Stato: RESOLVED EDITORIALLY — 2026-09-20**

### Evidenza di chiusura

`manual/MANUAL_CURRICULUM.md` usa progressive disclosure:

- Cap. 2 → ricavi vs margine vs cassa, CAC, LTV, payback, cost-to-serve, break-even, capacità;
- Capp. 30–32 → unit economics avanzati, coorti, cash/working capital e capacity economics.

Il lettore incontra quindi gli economics prima di mercato, cliente, offer, pricing e channel selection senza duplicare integralmente la sezione avanzata.

---

## G-007 — Glossario e linguaggio per principianti

**Priorità: P2**  
**Tipo: EDITORIAL GAP**  
**Stato: RESOLVED EDITORIALLY — 2026-09-20**

### Evidenza di chiusura

`manual/BEGINNER_GLOSSARY.md` contiene:

- termini beginner-critical;
- definizione editoriale;
- first-use chapter;
- regole per acronimi, ambiguità e coerenza terminologica.

`MANUAL_CURRICULUM.md` contiene inoltre la first-use terminology map.

Il copy-edit del glossario in Phase 8 è finalizzazione, non gap strutturale.

---

## G-008 — Ciclo post-vendita distribuito fra più sezioni

**Priorità: P2**  
**Tipo: EDITORIAL / CURRICULUM GAP**  
**Stato: RESOLVED EDITORIALLY — 2026-09-20**

Sintesi:

**durata/frequenza naturale → acquisto → onboarding → uso/risultato → next offer/continuità → comportamento atteso → deviazione → intervento → riattivazione o uscita naturale → referral/proof.**

Casa primaria: customer lifecycle/Business, con state-machine mechanics da Acquisition e procedure specifiche richiamate nei capitoli pertinenti.

---

# History sintetica

- Fase 1: G-001…G-008 identificati come gap iniziali.
- Fase 2: crosswalk completo; G-001, G-003, G-004 e G-008 risolti; G-002/G-005/G-006/G-007 rimasti da chiudere.
- Fase 3: curriculum chiude G-006 e governa first-use terminology.
- Fase 4: sintesi VoC, beginner glossary e casi sintetici chiudono G-002, G-005 e G-007.

---

# Regola di riapertura

Un gap risolto può essere riaperto solo se una chapter spec o il drafting dimostrano uno dei seguenti problemi:

- manca una decision rule necessaria;
- il testo richiede un prerequisito non presente;
- una sintesi non è supportabile dai nodi canonici;
- un esempio non basta a spiegare il trasferimento;
- provenance/temporalità cambia il significato della regola.

Non riaprire gap per aggiungere quantità o dettaglio non necessario.