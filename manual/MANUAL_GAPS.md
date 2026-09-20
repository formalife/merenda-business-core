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

Audit di riferimento: `manual/PHASE2_AUDIT.md`.

---

# Gap attivi

## G-002 — Libreria casi didattici insufficiente

**Priorità: P1**  
**Tipo: CASE GAP**  
**Stato: OPEN — CLOSURE PLAN DEFINED**

### Evidenza

Il case inventory ha identificato casi reali utilizzabili — Il Muratore Bergamasco, Studio Di Caprio, Maccheroni, MotoArgento, Il Toro e vari micro-esempi — ma la copertura end-to-end resta debole per:

- Voice of Customer;
- pricing/economics;
- vendita completa;
- customer lifecycle;
- brand accumulation;
- founder independence/transferability.

### Piano di chiusura

`manual/CASE_INVENTORY.md` definisce 6 casi sintetici candidati. Devono essere esplicitamente didattici e non presentati come evidenza fattuale.

### Condizione di chiusura

Chapter specs e curriculum dispongono di almeno un esempio/caso adeguato per ogni blocco fondamentale.

---

## G-005 — Voice of Customer / ricerca di mercato

**Priorità: P2**  
**Tipo: EDITORIAL GAP**  
**Stato: IN SYNTHESIS — NO DOCTRINAL ESCALATION AFTER PHASE 2**

### Evidenza consolidata

La conoscenza necessaria è distribuita fra:

- comportamento/economics clienti (`01_mercato`);
- complaint mining e positioning perception (`02_posizionamento`);
- query, intent, timing e inattività (`04_marketing`);
- database, conversazioni, contesto d'uso e query indirette (`05_acquisizione`);
- criteri decisionali, lost reasons e feedback vendita (`06_vendita`);
- output linguistici necessari al copy (`07_copy_comunicazione`);
- review, testimonial, reputazione e ragioni della scelta (`08_brand`).

### Gap residuo

Manca un'unica procedura beginner-safe per:

1. definire la decisione che la ricerca deve informare;
2. scegliere campioni/fonti;
3. raccogliere comportamento, linguaggio e contesto;
4. condurre interviste senza suggerire la risposta;
5. distinguere fatto, interpretazione, frequenza, intensità e valore economico;
6. triangolare fonti;
7. trasformare pattern in target/problema/alternative/trigger/proof/message;
8. validare la sintesi con comportamento e numeri.

### Condizione di chiusura

Creare e auditare una sintesi editoriale che copra questi passaggi senza introdurre nuova dottrina non supportata. Se non è possibile, solo allora escalare a doctrine review.

---

## G-006 — Economics fondamentali collocati troppo tardi

**Priorità: P1**  
**Tipo: CURRICULUM GAP**  
**Stato: CONFIRMED — DA RISOLVERE IN FASE 3**

### Evidenza

Market selection, customer quality, offer, pricing, channels, sales structure e scale usano già:

- margine;
- CAC;
- LTV;
- payback;
- cost-to-serve;
- break-even;
- capacità;
- timing della cassa.

La casa specialistica completa resta `09_business`, ma il lettore non può incontrare queste idee per la prima volta a valle.

### Decisione editoriale

Il curriculum deve separare:

1. **economic literacy minima all'inizio** — ricavi vs margine vs cassa, CAC, LTV, payback, cost-to-serve, capacità;
2. **economics avanzati più avanti** — cohorts, cash conversion cycle, working capital, reserves, capital allocation, capacity economics e growth.

### Condizione di chiusura

`MANUAL_CURRICULUM.md` introduce e definisce gli economics minimi prima della selezione di mercato/cliente e impedisce gergo economico anticipato.

---

## G-007 — Glossario e linguaggio per principianti

**Priorità: P2**  
**Tipo: EDITORIAL GAP**  
**Stato: OPEN**

Termini da governare almeno al first use:

CAC, LTV, payback, contribution margin, cost-to-serve, RFM, front-end, back-end, upsell, cross-sell, risk reversal, direct response, awareness, intent, funnel, positioning, referral, sell-in, sell-through, working capital, cash conversion cycle.

### Piano

La Fase 3 deve associare ogni termine al primo capitolo in cui viene definito. La release finale includerà glossario, ma il glossario non deve essere una scusa per usare gergo non spiegato nel testo.

---

# Gap risolti editorialmente

## G-001 — Processo di vendita end-to-end

**Priorità: P1**  
**Tipo: EDITORIAL GAP**  
**Stato: RESOLVED EDITORIALLY — 2026-09-20**

### Evidenza di chiusura

`06_vendita` produce SAL-001…SAL-071 e una sequenza completa:

**handoff/preparazione → prequalifica → presa in carico → diagnosi → criteri decisionali → prescrizione/prova → proposta/prezzo → verifica delle certezze → decisione → follow-up/no-sale classification → feedback/review.**

Marketing, offer e proof restano prerequisiti, non parti da reinventare durante la call.

### Vincolo residuo

La chapter spec dovrà preservare varianti self-service/simple sale e non trasformare lo script in formula universale.

---

## G-003 — Doctrine/provenance map

**Priorità: P1**  
**Tipo: PROVENANCE GAP / EDITORIAL INFRASTRUCTURE**  
**Stato: RESOLVED EDITORIALLY — 2026-09-20**

### Evidenza di chiusura

Creato `manual/PROVENANCE_MAP.md`, con:

- regole primary/assimilated/synthesis;
- temporal precedence;
- cluster MAF/Bonechi;
- cluster jAI/Jay Abraham-Michael Simmons-Max Bernstein;
- sintesi editoriali da non retro-attribuire.

La mappa è compatta e non replica il source registry.

---

## G-004 — Sintesi organica della costruzione del brand

**Priorità: P2**  
**Tipo: EDITORIAL GAP**  
**Stato: RESOLVED EDITORIALLY — 2026-09-20**

### Evidenza di chiusura

`08_brand`, `PRIMARY_HOME_MAP.md` e `DEPENDENCY_MAP.md` supportano la sequenza:

**posizione/significato → authority/credibility/proof → esperienza reale → reputazione → memoria → advocacy/community.**

### Decisione didattica

Il brand non sarà necessariamente un unico blocco: authority/proof serve prima di acquisition/sales; reputation/community viene approfondita dopo delivery/customer success.

---

## G-008 — Ciclo post-vendita distribuito fra più sezioni

**Priorità: P2**  
**Tipo: EDITORIAL / CURRICULUM GAP**  
**Stato: RESOLVED EDITORIALLY — 2026-09-20**

### Evidenza di chiusura

La sintesi integra:

- durata/frequenza naturale della relazione;
- onboarding e first value;
- uso/supporto/feedback;
- seconda vendita/back-end/continuità;
- comportamento atteso vs deviazione;
- trigger di retention/riattivazione;
- referral/proof;
- uscita naturale e sostituzione delle coorti.

### Casa primaria

Customer lifecycle in Business/customer success, con state-machine mechanics da Acquisition e procedure specialistiche richiamate nei nodi pertinenti.

---

# History sintetica

- Fase 1: G-001…G-008 aperti come gap iniziali/strutturali.
- Fase 2 first pass: vendita, brand e lifecycle si sono dimostrati ricostruibili senza nuova dottrina.
- Cross-section pass 2026-09-20: G-001, G-003, G-004 e G-008 chiusi editorialmente; G-005 resta sintesi; G-006 passa formalmente alla Fase 3; G-002/G-007 restano editoriali.

---

# Regola di aggiornamento

Stati ammessi:

- `OPEN`;
- `IN SYNTHESIS`;
- `CONFIRMED — DA RISOLVERE IN FASE 3`;
- `RESOLVED EDITORIALLY`;
- `ESCALATED TO DOCTRINE REVIEW`;
- `DEFERRED WITH REASON`.

Non chiudere un gap perché esiste un documento. Chiuderlo solo quando il relativo requisito didattico o conoscitivo è verificabilmente soddisfatto.