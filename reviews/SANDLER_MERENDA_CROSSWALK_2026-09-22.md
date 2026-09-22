# Sandler → Merenda Doctrine Crosswalk

Data: 2026-09-22  
Stato: **DECISION ARTIFACT — PRE-MERGE CROSSWALK**  
Scope: integrazione completa della dottrina Sandler v1.0 nel doctrine layer `merenda/`, senza mantenere una seconda KB operativa o una dipendenza runtime da un repository esterno.

## Decisione founder

La dottrina Sandler acquisita e auditata viene **assimilata integralmente nel Layer 1 Merenda**.

Regole della migrazione:

1. `MERGE, NOT APPEND`;
2. nessun subtree `sandler/` dentro `merenda/`;
3. nessun doppio sistema Merenda/Sandler da consultare in parallelo;
4. la KB finale deve essere autosufficiente;
5. provenance reale preservata quando materialmente utile: un principio Sandler non viene attribuito a Frank Merenda;
6. termini proprietari utili possono restare nominati e attribuiti; metafore o tassonomie ridondanti possono essere assorbite nella formulazione canonica finale;
7. quando Merenda e Sandler coprono lo stesso meccanismo, costruire una sola formulazione canonica;
8. quando differiscono, distinguere scope/condizioni e creare una `SYNTHESIS` solo se la riconciliazione è difendibile;
9. specialist doctrine prima; routing dopo; eval dopo il routing; `REASONING_KERNEL.md` solo se la regressione dimostra un gap reale;
10. `manual/` solo dopo chiusura doctrine/routing/eval.

## Classificazioni usate

- **CONFIRMS** — conferma una regola già presente.
- **DEEPENS** — aggiunge causalità, procedura, boundary o failure modes a un principio già presente.
- **FILLS GAP** — aggiunge una funzione che la KB Merenda non possiede con sufficiente precisione.
- **RECONCILE** — richiede una sintesi esplicita per evitare contraddizioni apparenti.
- **ROUTE ELSEWHERE** — entra nel Layer 1, ma la casa canonica non è `06_vendita`.
- **COMPRESS** — il contenuto viene conservato semanticamente, ma l'etichetta/framework separato non merita una casa autonoma.
- **DO NOT PROMOTE** — dettaglio storico, esempio, soglia o procedura troppo debole per diventare regola canonica.

---

# 1. Architettura finale della vendita

## 1.1 Vendita come diagnosi e prescrizione

**Merenda esistente:** forte. `problema → analisi → diagnosi → prescrizione/offerta`; diagnosi standardizzata e prescrizione personalizzata; approfondimento prima di rispondere; authority/proof come prerequisito alla prescrizione autorevole.

**Sandler:** `Bonding & Rapport → Up-Front Contract → Pain → Budget → Decision → Fulfillment → Post-Sell`; qualification prima della proposta; qualify/disqualify; no come outcome legittimo.

**Classificazione:** `DEEPENS + FILLS GAP`.

**Sintesi finale:** Merenda fornisce il principio generale di diagnosi/prescrizione e il lavoro a monte di marketing/autorità; Sandler fornisce la grammatica operativa della conversazione e i gate che impediscono di trasformare la diagnosi in un preventivo prematuro.

**Casa finale:** `merenda/06_vendita/sistema-vendita-e-qualificazione.md`.

## 1.2 Seven-step Sandler

Il valore da importare è la causalità:

**relazione → accordo sul processo → problema/Pain → investimento → processo decisionale → proposta mirata → decisione/post-sell.**

**Classificazione:** `DEEPENS`.

La KB Merenda non deve diventare un manuale di marchio Sandler. Il seven-step resta attribuibile a Sandler e può essere nominato come origine della struttura, ma la formulazione canonica della KB deve parlare prima di tutto delle funzioni.

**Casa finale:** overview vendita + nodi specialistici.

## 1.3 Submarine / Flywheel

Entrambe sono rappresentazioni della stessa architettura Sandler e non aggiungono un nuovo meccanismo necessario dopo che i gate sono stati assimilati.

**Classificazione:** `COMPRESS`.

Conservare solo il principio utile: il buyer può arrivare con informazioni già disponibili, ma ciò non autorizza a saltare Pain/Investment/Decision prima della proposta; non serve ripetere meccanicamente ciò che è già affidabilmente noto.

**Non creare nodo autonomo Merenda.**

---

# 2. Marketing prequalification vs sales qualification

## 2.1 Prequalifica Merenda

Merenda richiede che marketing/pre-vendita preparino, quando possibile:

- premotivazione e differenza;
- ordine di grandezza economico;
- mappa preliminare di processo/potere decisionale;
- timeframe/urgenza;
- informazione standardizzabile prima del tempo umano costoso.

## 2.2 Qualification Sandler

Sandler richiede che la conversazione commerciale verifichi realmente:

- Pain;
- Budget / Investment / risorse;
- Decision process;
- fit e possibilità di disqualification.

**Classificazione:** `RECONCILE`.

**Sintesi canonica:**

**marketing prequalifica e prepara → sales verifica, corregge e approfondisce → Pain/Investment/Decision qualificano l'opportunità → solo dopo si prescrive/presenta.**

La prequalifica non sostituisce la qualification interattiva. La qualification non giustifica che marketing scarichi sul venditore tutta l'educazione ripetibile.

**Casa finale:** `prequalifica-e-handoff-marketing-vendita.md` + `sistema-vendita-e-qualificazione.md`.

---

# 3. Postura, relazione e controllo del processo

## 3.1 Equal Business Stature

Merenda possiede già authority, autorevolezza, diagnosi e prescrizione; Sandler rende esplicito che il seller non deve diventare subordinato al buyer né dominante.

**Classificazione:** `FILLS GAP + DEEPENS`.

Principio finale:

**autorevolezza ≠ dominanza; parità professionale = diritto/dovere di porre domande difficili, parlare di investimento, chiedere come si decide, dire no e proteggere il processo.**

## 3.2 Seek the truth / No is OK / disqualification

Merenda già rifiuta lead inappropriate e clienti economicamente sbagliati, ma il meccanismo dentro la trattativa è meno formalizzato.

**Classificazione:** `FILLS GAP`.

Principio finale:

**lo scopo della qualification è scoprire la verità dell'opportunità, non produrre un sì a ogni costo.**

Un no pulito può essere economicamente superiore a una proposta inutile, una falsa pipeline o un cliente non appropriato.

## 3.3 Full disclosure / controllo del processo

Merenda prescrive una vendita guidata e autorevole. Sandler chiarisce il boundary:

**controllare il processo, non la persona.**

**Classificazione:** `DEEPENS`.

La fermezza Merenda nella prescrizione resta compatibile se il seller rende esplicito il processo e preserva la libertà reale del buyer di non procedere.

**Casa finale:** `relazione-e-accordi-di-conversazione.md` + overview.

---

# 4. Up-Front Contract e accordi di conversazione

Merenda ha processi, preparazione, live conversation e next step, ma non un framework altrettanto esplicito per eliminare le agende nascoste.

Sandler UFC chiarisce:

- purpose;
- time;
- agenda;
- ruoli/ground rules;
- outcome/next step;
- possibilità reciproca di non procedere.

**Classificazione:** `FILLS GAP`.

## Riconciliazione outcome

- discovery/interazione intermedia → può terminare con next step concreto;
- meeting qualificato di presentazione/decisione → l'outcome deve essere decision-grade, non un nuovo “ci penso” previsto come default.

La logica UFC può essere riconfermata durante il processo senza creare step aggiuntivi.

## Ultimate Contract

Nome e script forte “ask for the order before presentation” restano troppo source-specific per diventare regola universale della KB Merenda.

**Classificazione:** `DO NOT PROMOTE` per il nome/script; `DEEPENS` per il meccanismo.

Importare soltanto:

**prima di distribuire la soluzione in un meeting decisionale, chiarire quale decisione/azione seguirà se la soluzione soddisfa le condizioni già qualificate.**

**Casa finale:** `relazione-e-accordi-di-conversazione.md`.

---

# 5. Pain e diagnosi del problema

Merenda già insegna:

- “dimmi di più” / specificità / durata / tentativi;
- conseguenze pratiche ed emotive;
- validazione dell'esperienza;
- fatti/misure/evidenza;
- diagnosi prima della prescrizione.

Sandler aggiunge:

- Pain come gate formale;
- surface problem ≠ Pain completo;
- Pain Funnel come framework di approfondimento;
- controllo di completezza dell'elenco dei problemi;
- monetizzazione collaborativa dell'impatto;
- distinzione fra Pain reale e Pain abbastanza importante da giustificare cambiamento;
- disqualification se il peso del problema è insufficiente.

**Classificazione:** `CONFIRMS + DEEPENS`.

**Sintesi finale:**

**problema dichiarato → specificità/tentativi/causa → conseguenze pratiche ed emotive → impatto economico quando pertinente → verifica di completezza → decisione se esiste una ragione reale per cambiare.**

Non fabbricare Pain e non gonfiare numeri.

**Casa finale:** `diagnosi-e-pain.md`.

---

# 6. Budget / investimento

Merenda già ha:

- prequalifica economica;
- ordine di grandezza prima della proposta;
- capacità economica ≠ semplice obiezione di prezzo;
- price gap da motivare attraverso differenza/prova/target fit.

Sandler aggiunge la qualification di:

- willingness + ability;
- denaro + tempo + risorse;
- quanto / quando / fonte delle risorse;
- permission-based transition da Pain a Budget;
- bracketing/third-party stories come depth istituzionale;
- disqualification se la realtà economica non regge.

**Classificazione:** `CONFIRMS + DEEPENS`.

**Riconciliazione:** la vecchia retorica “il denaro non è mai un problema” non governa. La formulazione finale è:

**se capacità e priorità esistono, vendita/marketing devono rendere comprensibile il valore dell'investimento; se le risorse necessarie non esistono o non verranno rese disponibili, la presentazione non corregge il problema.**

Bracketing e 70/30 restano strumenti/euristiche, non leggi.

**Casa finale:** `budget-e-investimento.md`.

---

# 7. Decision process e stakeholder

Merenda già possiede:

- prequalifica del potere decisionale;
- necessità di raggiungere chi decide;
- timeframe;
- coinvolgimento di partecipanti pertinenti;
- differenza fra contatto e reale capacità di autorizzazione.

Sandler aggiunge una qualification molto più completa:

- who / when / what / where / why / how;
- authority + criteria + internal path;
- process before people come lente operativa;
- future-decision test;
- re-check quando il processo cambia;
- disqualify/postpone se il percorso resta materialmente opaco.

**Classificazione:** `CONFIRMS + DEEPENS`.

**Casa finale:** `processo-decisionale-e-stakeholder.md`.

---

# 8. Fulfillment / proposta / decisione

Merenda già prescrive:

- diagnosi standardizzata → prescrizione personalizzata;
- preventivo non ridotto a prezzo;
- proposta coerente con diagnosi e valore;
- authority/proof per sostenere la prescrizione;
- tre certezze prodotto / venditore / azienda come lente diagnostica sulle esitazioni.

Sandler aggiunge:

- presentare solo dopo Pain/Budget/Decision;
- proposta come fulfillment del fit già qualificato, non generatrice del fit;
- presentazione selettiva, non feature dump;
- soluzione coerente con problema, risorse e decision process;
- clear yes/no come esito desiderato del decision meeting;
- non usare closing tardivo per compensare qualification debole.

**Classificazione:** `DEEPENS + FILLS GAP`.

**Sintesi finale:**

**la proposta non deve scoprire il caso d'acquisto: deve rendere concreto il caso d'acquisto già diagnosticato e qualificato.**

## Tre certezze vs qualification

Le tre certezze Merenda/Straight Line non sostituiscono Pain/Budget/Decision.

Se, dopo una buona qualification, resta esitazione, possono aiutare a chiedere **quale oggetto di fiducia/prova è ancora insufficiente**. Il loop deve riaprire diagnosi/prova, non diventare pressione ripetuta dopo un no reale.

**Classificazione:** `RECONCILE`.

**Casa finale:** `fulfillment-proposta-decisione-e-post-sell.md`.

---

# 9. Thermometer

La KB Merenda non possiede un readiness check altrettanto formalizzato.

**Classificazione:** `FILLS GAP`.

Importare come tecnica diagnostica cross-process, soprattutto durante Fulfillment:

**presentazione mirata → pausa → readiness esplicita → verbalizzare il gap → chiarire solo ciò che manca / rivalutare fit → stop selling quando il buyer è pronto.**

Guardrail:

- scala 0–10 o 1–10 = convenzione, non sostanza;
- nessuna soglia universale;
- storico `6+ = sold` non promosso;
- numero senza “perché?” non serve;
- non salva qualification debole;
- non serve a spingere lo score verso 10.

**Casa finale:** `tattiche-conversazionali.md`, con pointer da Fulfillment.

---

# 10. Reversing, Negative Reverse, Strip-Lining

## Reversing

Merenda già insegna approfondimento e non saltare alla soluzione. Sandler formalizza:

**non reagire alla superficie → chiarire intento/significato → ascoltare → poi rispondere.**

Statement ≠ obiezione. Evitare mind-reading. Se il buyer ripete legittimamente la domanda dopo il chiarimento, rispondere.

**Classificazione:** `DEEPENS`.

## Negative Reverse

Ridurre pressione introducendo una direzione cautelativa/negativa credibile per rendere reale il no e far emergere la posizione del buyer.

**Classificazione:** `FILLS GAP`.

Guardrail: richiede reale tolleranza del no; non è manipolazione teatrale né una tecnica per combattere un no reale.

## Strip-Lining

Applicazione specifica della logica di riduzione della pressione/movimento opposto.

**Classificazione:** `DEEPENS`, ma comprimere la tassonomia nel nodo tattico; non serve un file autonomo.

Conservare il meccanismo:

- neutro → creare definizione/movimento;
- positivo → rallentare e qualificare l'entusiasmo;
- negativo → non aumentare la contropressione.

Le intensità specifiche di una singola fonte restano esempi, non algoritmo universale.

**Casa finale comune:** `tattiche-conversazionali.md`.

---

# 11. Follow-up: persistenza Merenda vs No-is-OK Sandler

Questa è una riconciliazione materiale.

Merenda considera lead/opportunità non convertite un asset già pagato e prescrive follow-up di lungo periodo, multicanale e legato al timing reale.

Sandler prescrive qualification/disqualification, “No is OK”, clear outcome e chiusura del file quando il fit non esiste.

**Classificazione:** `RECONCILE`.

## Sintesi finale per stato

1. **No esplicito / non-fit qualificato** → chiudere l'opportunità; non inseguire.
2. **Not now / timing / budget non ancora disponibile / ciclo sostitutivo futuro** → relazione/nurture se permesso ed economicamente sensato; non fingere che la trattativa sia attiva.
3. **No-decision dovuto a qualification incompleta** → riaprire il gap se esiste ancora accesso e valore; non mascherarlo come follow-up generico.
4. **Silenzio dopo proposta** → tentativo di closure a bassa pressione; Sandler “voicemail jail” è una possibile procedura specifica, non uno script universale.
5. **Mai realmente raggiunto/qualificato** → non confondere con opportunità qualificata diventata silenziosa.

Questa sintesi integra Merenda, Sandler e il contributo assimilato sulla pipeline già presente.

**Casa finale:** `follow-up-e-pipeline.md`.

---

# 12. Prospecting / outbound

La dottrina Sandler sul prospecting non deve spostare il causal order Merenda.

Merenda governa **se** e **dove** cercare domanda:

- domanda/relazioni già possedute prima quando economicamente sensato;
- target e appropriatezza;
- active vs latent demand;
- canale scelto da economics/intent, non moda.

Sandler approfondisce **come rendere disciplinata l'esecuzione commerciale** una volta che il prospecting/outbound è giustificato:

- activity math / behavior plan;
- Prospecting Plan per fonti e nuove conversazioni;
- ICP e allocazione del tempo;
- Need / Winnable / Want-to-win;
- multi-channel intenzionale;
- role-play;
- call reluctance;
- appointment-first;
- light qualification;
- gatekeeper;
- voicemail-jail.

**Classificazione:** `ROUTE ELSEWHERE + DEEPENS`.

**Casa finale:** `05_acquisizione`, non il cuore del Selling System in `06_vendita`.

Il Cookbook generale va invece alla gestione/performance della rete vendita.

## Gatekeeper

Importare come outline, non come script:

**disarm → parità professionale → contesto vero/diretto → accordo collaborativo → next step senza aggressività.**

Non importare deception/fake familiarity.

## First-touch voicemail

Nessuna formula universale acquisita.

**Classificazione:** `DO NOT INVENT`.

---

# 13. Referral / introduction

Merenda ha già una doctrine forte:

- soddisfazione/risultato reale;
- momento opportuno;
- richiesta esplicita;
- strumenti che rendono semplice presentare;
- protezione della reputazione del referrer;
- incentivi solo se sostenibili;
- attribution e valore economico del referral.

Sandler aggiunge:

- distinzione referral vs introduction;
- specificità della persona da introdurre;
- brainstorming con caratteristiche osservabili;
- permesso prima dell'introduzione;
- non mettere pressione a chi non vuole presentare.

**Classificazione:** `DEEPENS + ROUTE ELSEWHERE`.

**Casa finale:** `merenda/05_acquisizione/referral-e-soddisfazione.md`.

## Timing

Sandler Post-Sell può aprire futuro business/referral; Customer Success collega referral a momenti di valore. Merenda prescrive sia richiesta dopo vendita sia momento di massimo successo/soddisfazione.

**Sintesi:** la firma non crea automaticamente diritto a una referral. Usare il momento in cui fiducia/valore sono sufficienti nel contesto; il risultato realizzato è un trigger particolarmente forte, ma non l'unico possibile.

---

# 14. Post-Sell immediato vs Customer Success

Merenda ha già onboarding, feedback, support, trigger di retention, customer effort e offerta successiva dopo valore.

Sandler distingue bene:

- **Post-Sell immediato** — stabilizzare decisione, ridurre buyer's remorse, chiarire aspettative, risolvere questioni residue, handoff;
- **Customer Success continuativo** — realizzazione di valore, rischio, retention, renewal, expansion, account management.

**Classificazione:** `DEEPENS + RECONCILE`.

## Post-Sell

Da integrare in `06_vendita` come fase immediatamente successiva al sì/handoff.

## Customer Success / account growth

Da integrare in `09_business/retention-onboarding-e-customer-success.md`, non come ottavo step di vendita.

Elementi da importare:

- structured handoff con problema, economic buyer success criteria, metriche e rischi noti;
- valore realizzato presto e con continuità;
- review del valore con cadence coerente con il ritmo reale del cliente, non 90 giorni universali;
- account relationship non single-threaded;
- expansion come estensione di valore/problema reale, non pitch automatico;
- KARE come possibile portfolio lens (Keep / Attain / Recapture / Expand), non processo cronologico.

PACE non viene completato: acronym/procedura non acquisiti.

**Casa finale:** `06_vendita/fulfillment-proposta-decisione-e-post-sell.md` + `09_business/retention-onboarding-e-customer-success.md`.

---

# 15. Performance psychology

## B.A.T. / Success Triangle

Merenda possiede già script, role-play, training, performance review e controllo. Sandler aggiunge un diagnostic framework molto utile:

- Behavior — cosa viene eseguito;
- Attitude — convinzioni/postura che facilitano o bloccano l'esecuzione;
- Technique — come viene eseguito.

**Classificazione:** `FILLS GAP + DEEPENS`.

Uso canonico:

**prima di prescrivere “più training”, identificare se il gap è soprattutto esecuzione, postura o tecnica.**

## Identity / Role

Utile come lente subordinata quando il seller conosce tecnica e comportamento ma non li esegue sotto rifiuto, rischio, executive interaction, Budget o bisogno di approvazione.

**Classificazione:** `DEEPENS`, non framework primario.

Non importare Winner/Loser/At-leaster, fasce numeriche, Wally Weakcloser o pseudo-psicometria.

## Transactional Analysis

Può restare come lente di self-management/comunicazione:

- Critical Parent → rischio di superiorità/giudizio;
- Adapted Child → rischio di subordinazione/approval-seeking;
- Nurturing Parent/Adult → ricettività + oggettività.

**Classificazione:** `DEEPENS / OPTIONAL LENS`.

Non usarla per diagnosi cliniche, non diagnosticare obbligatoriamente il buyer e non trattare rapporti 70/30 come misure empiriche.

**Casa finale:** `psicologia-e-performance-commerciale.md`.

---

# 16. Behavior system / Cookbook / accountability

Merenda già ha KPI, script, review, role-play, manager feedback, standard minimi e performance review.

Sandler aggiunge una catena manageriale forte:

**goal/outcome → rapporti osservati → reverse engineering → comportamento controllabile → frequenza → esecuzione → accountability → outcome → revisione.**

Principio:

**manage behavior, not results** non significa ignorare i risultati; significa non gestire direttamente ciò che non è controllabile. Gli outcome servono a verificare se la ricetta è valida.

**Classificazione:** `DEEPENS`.

Il termine Cookbook può essere conservato come provenance/termine Sandler, ma la casa canonica deve parlare di **behavior plan commerciale**.

**Casa finale:** `rete-vendita-processo-coaching.md`.

---

# 17. Coaching / reinforcement / management

Merenda già possiede:

- role-play;
- recording/review quando lecito;
- observation → feedback → training → re-execution → measurement;
- preparation;
- standards / incentives / review / retraining;
- specialization by economic threshold.

Sandler conferma e approfondisce:

- reinforcement come processo, non evento;
- low-risk practice;
- pre-call planning + post-call debrief;
- coaching nel flow of work;
- behavior/accountability;
- 4-step coaching model existence;
- institutional `Assess → Establish → Define → Execute`;
- pipeline review come coaching, non sola interrogazione/forecast;
- manager accountable per i propri commitment.

**Classificazione:** `CONFIRMS + DEEPENS`.

La KB finale deve evitare di creare un secondo management system. Integrare nel nodo rete vendita esistente rifondato.

Non promuovere:

- cadence universale;
- Four Factors non acquisiti;
- coaching contract non definito;
- tooling AI di prodotto come doctrine permanente.

**Casa finale:** `rete-vendita-processo-coaching.md`.

---

# 18. Matrice case finali

| Area | Casa canonica finale | Decisione |
|---|---|---|
| processo vendita / qualification | `06_vendita/sistema-vendita-e-qualificazione.md` | nuovo nodo, sintesi di governo specialistica |
| marketing → sales handoff | `06_vendita/prequalifica-e-handoff-marketing-vendita.md` | rifusione del nodo Merenda prequalifica |
| rapport / equal stature / UFC | `06_vendita/relazione-e-accordi-di-conversazione.md` | nuovo nodo |
| Pain / diagnosi | `06_vendita/diagnosi-e-pain.md` | rifusione diagnosi Merenda + Pain Sandler |
| Budget | `06_vendita/budget-e-investimento.md` | nuovo nodo |
| Decision | `06_vendita/processo-decisionale-e-stakeholder.md` | nuovo nodo |
| Fulfillment / proposal / close / Post-Sell | `06_vendita/fulfillment-proposta-decisione-e-post-sell.md` | nuovo nodo |
| Reversing / Negative Reverse / Strip-Lining / Thermometer | `06_vendita/tattiche-conversazionali.md` | nuovo nodo unico |
| follow-up / pipeline | `06_vendita/follow-up-e-pipeline.md` | rifusione nodo esistente |
| B.A.T. / I-R / TA | `06_vendita/psicologia-e-performance-commerciale.md` | nuovo nodo |
| rete vendita / behavior plan / coaching | `06_vendita/rete-vendita-processo-coaching.md` | rifusione nodo esistente |
| prospecting / outbound execution | `05_acquisizione/prospecting-e-outbound.md` | nuovo nodo; causal hierarchy Merenda governa |
| referral / introductions | `05_acquisizione/referral-e-soddisfazione.md` | merge nel nodo esistente |
| customer success / account growth | `09_business/retention-onboarding-e-customer-success.md` | merge nel nodo esistente |

## File `06_vendita` legacy

I quattro file attuali non devono restare come case canoniche concorrenti dopo la migrazione:

- `prequalifica-follow-up-decisori.md` → contenuto distribuito fra handoff / Decision / follow-up;
- `preventivo-consulenza-diagnosi.md` → contenuto distribuito fra Pain / Fulfillment / performance;
- `rete-vendita-script-allenamento-e-controllo.md` → `rete-vendita-processo-coaching.md`;
- `follow-up-lead-non-convertiti.md` → `follow-up-e-pipeline.md`.

Eliminare i legacy soltanto dopo aver aggiornato tutti i riferimenti in ingresso e verificato che nessun contenuto unico sia perso.

---

# 19. Principi di precedenza dopo la fusione

La KB finale non userà una regola globale “Merenda vince” o “Sandler vince”.

Ordine per singolo problema:

1. formulazione canonica integrata nel nodo specialistico;
2. fonte più diretta per quel meccanismo, con provenance reale;
3. quando due fonti/autori divergono, scope e condizioni prima della recency cross-author;
4. sintesi KB solo se la relazione fra i due sistemi è esplicitabile senza inventare;
5. dettagli storici/esempi/soglie subordinati.

## Invarianti della doctrine unificata

- marketing prepara; sales verifica;
- diagnosi prima della prescrizione;
- relazione peer-to-peer, non subordinazione né dominanza;
- accordo esplicito sul processo quando la conversazione è materialmente importante;
- Pain / investimento / decision process prima della proposta;
- qualification include disqualification;
- proposal/Fulfillment serve il fit già qualificato;
- un no reale è informazione, non un nemico da sconfiggere;
- follow-up dipende dallo stato reale dell'opportunità, non dalla speranza;
- training = practice + observation + feedback + reinforcement;
- gestire input controllabili, validandoli sugli outcome;
- post-sell immediato e customer success continuativo sono funzioni diverse;
- retention/referral/expansion devono seguire valore e fit, non pressione.

---

# 20. Ordine di implementazione

1. **Governance** — `system/RULES.md` allineato alle fonti assimilate autorizzate.
2. **Crosswalk** — questo documento.
3. **Doctrine specialistica** — creare le nuove case e migrare semanticamente `06_vendita`; integrare `05_acquisizione` e `09_business` dove indicato.
4. **Legacy cleanup** — eliminare/archiviare i quattro nodi vendita vecchi solo dopo link audit e semantic coverage check.
5. **Routing** — README, `merenda/INDEX.md`, semantic/structural routing, poi `DECISION_ROUTER.md` solo dove necessario.
6. **Validation** — validator + broken-link/structural checks.
7. **Behavioral regression** — casi vendita vecchi + nuovi casi di prerequisiti Sandler.
8. **Kernel decision** — modificare `REASONING_KERNEL.md` solo se la specialist doctrine/routing non basta a mantenere decision fidelity.
9. **Final integration checkpoint** — provenance, omissioni, duplicazioni, regressioni.
10. **Manual** — aggiornare publishing layer solo dopo il merge canonico.

## Gate per passare alla doctrine

Crosswalk sufficientemente completo quando ogni macro-meccanismo Sandler ha:

- classificazione;
- casa finale;
- boundary;
- riconciliazione con Merenda quando necessaria;
- decisione esplicita su cosa non promuovere.

**Gate: PASS — doctrine integration may begin.**
