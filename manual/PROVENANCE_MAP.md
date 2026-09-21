# Provenance Map — backend editoriale del manuale

## Scopo

Questa mappa chiude il **provenance/temporal pass** della Fase 2.

Il manuale reader-facing resta source-agnostic. Questo file esiste per impedire che la voce unitaria del manuale cancelli:

- autore reale delle fonti assimilate;
- evoluzioni temporali;
- caveat che rendono una regola condizionale;
- differenza fra fonte primaria e sintesi editoriale.

Non replica il source registry. Registra solo i punti che possono cambiare il significato della sintesi.

Classi:

- **MERENDA PRIMARY** — principio sostenuto direttamente dal corpus primario;
- **ASSIMILATED** — contenuto ammesso nel doctrine layer per istruzione esplicita dell'utente, con autore reale preservato;
- **SYNTHESIS** — relazione costruita collegando più nodi, non attribuibile a una singola fonte;
- **TEMPORAL PRECEDENCE** — una formulazione più recente limita o supera un assoluto storico.

---

# 1. Regole generali

## P-001 — Compatibilità non equivale ad attribuzione

Un principio proveniente da Moreno Bonechi, Jay Abraham, Michael Simmons, Max Bernstein o altra fonte assimilata può essere usato nel manuale se fa parte del doctrine layer corrente, ma il backend non deve descriverlo come formulazione originaria di Frank Merenda.

Reader-facing: voce unitaria.  
Backend: autore/provenance reale preservata.

---

## P-002 — Sintesi editoriale non diventa retroattivamente fonte primaria

Sequenze come vendita end-to-end, costruzione del brand, lifecycle e Voice of Customer possono essere ricostruite da più nodi. Il manuale può insegnarle come sistema unico, ma il backend le classifica come **SYNTHESIS**.

---

## P-003 — Esempi e numeri restano contestuali

Percentuali, durate, benchmark e risultati raccontati nei casi o nelle fonti non diventano soglie universali salvo esplicita canonizzazione. Il manuale deve trasferire il meccanismo, non l'aneddoto numerico.

---

# 2. Temporal precedence da preservare

## P-010 — Cold outreach

**Tema:** contatto a freddo.  
**Trattamento:** TEMPORAL PRECEDENCE.

Il materiale 2015 presenta una prescrizione forte contro l'impatto indiscriminato a freddo. Il materiale 2024 ricomprende i contatti a freddo tra le modalità praticabili.

**Regola manuale:** il freddo non è vietato universalmente; deve essere progettato, misurato e coerente con target/economics. La prequalifica e la preparazione della trattativa restano valide.

Nodi: `04_marketing/quattro-modalita-e-ritmo.md`; `06_vendita/prequalifica-follow-up-decisori.md`.

---

## P-011 — Front-end

**Tema:** prezzo basso vs barriera di ingresso.  
**Trattamento:** TEMPORAL PRECEDENCE.

Formulazioni storiche possono associare il front-end a prezzo basso o break-even. Il chiarimento 2025 lo definisce più precisamente come **riduzione della barriera d'ingresso**, ottenibile anche con porzione di servizio, prova, garanzia o altra riduzione del rischio.

Nodi: OFF-022 e cluster front-end.

---

## P-012 — Premium pricing

**Tema:** “prezzo premium” come prezzo numericamente sempre più alto.  
**Trattamento:** TEMPORAL / CONTEXT.

La regola finale non è alzare sempre il numero. La differenziazione può sostenere un premium quando willingness-to-pay, conversione, margine e economics lo consentono.

Nodi: `03_offerta/prezzo-premium-e-percezione-del-valore.md`.

---

## P-013 — Social e piattaforme

**Tema:** priorità del social.  
**Trattamento:** TEMPORAL PRECEDENCE.

Il materiale 2022 distingue strategie organiche e produzione contenuti; il materiale successivo rende prevalente il controllo della domanda diretta/attiva prima di assumere che il social sia il primo canale.

Nodi: MKT demand/channel.

---

## P-014 — Materiale fisico / analogico

**Tema:** superiorità del fisico.  
**Trattamento:** CONTEXT.

Le fonti storiche attribuiscono forte importanza a pacchi, lettere e materiali fisici. La regola canonica finale è scegliere il formato che migliora consumo, fiducia e avanzamento rispetto al costo; il fisico è implementazione, non obbligo.

Nodi: `05_acquisizione/information-marketing.md`.

---

## P-015 — Family brand ed estensioni

**Tema:** architettura di marca.  
**Trattamento:** TEMPORAL PRECEDENCE.

Formulazioni storiche più assolute sulle estensioni sono subordinate ai nodi più recenti che distinguono focus del singolo brand, multibrand, category context e casi in cui l'estensione può essere gestita consapevolmente.

Nodi: POS-037…POS-050; BUS-099…BUS-103.

---

## P-016 — Testo asincrono vs conversazione sincrona

**Tema:** vendita consulenziale via messaggi.  
**Trattamento:** CONTEXT.

Il materiale 2024 critica la sostituzione automatica della conversazione con messaggi nei cicli complessi. La regola finale non vieta chat/email/self-service: preserva il punto sincrono quando diagnosi e decisione interattiva ne beneficiano.

Nodo: `06_vendita/prequalifica-follow-up-decisori.md`.

---

## P-017 — Paura, aggressività e direct response

**Tema:** stile comunicativo.  
**Trattamento:** TEMPORAL / ETHICAL CAVEAT.

Materiale storico può usare formulazioni aggressive. Il corpus recente conserva solo conseguenze reali, urgenza autentica e proof supportabile. Direct response è struttura di risposta, non tono urlato.

Nodi: `07_copy_comunicazione/priorita-azione-e-inerzia.md`; `checklist-risposta-diretta.md`; `scrittura-sales-letter-e-argomentazione.md`.

---

# 3. Assimilated source map — concetti sensibili

## P-020 — Proof by Refusal

**Provenance:** ASSIMILATED.  
**Unità:** MRC-036.

Uso manuale: il rifiuto di clienti non appropriati può diventare segnale di standard e selettività quando è reale. Non attribuire automaticamente il framework a Merenda.

---

## P-021 — Rendere visibile/nominare un processo reale

**Provenance:** ASSIMILATED contribution integrato nel positioning.  
**Unità:** POS-022/POS-023.

Uso manuale: un processo reale può diventare più comprensibile e memorabile se reso visibile e nominato; il naming non crea differenza se la sostanza non esiste.

---

## P-022 — Bundle come riduzione del costo cognitivo / prova sufficientemente lunga

**Provenance:** ASSIMILATED contributions.  
**Unità:** OFF-007/OFF-029.

Uso manuale: integrare come meccanismi di offerta, mantenendo il caveat economico e senza trasformare esempi della fonte in soglie universali.

---

## P-023 — AI + memoria commerciale

**Provenance:** ASSIMILATED — Moreno Bonechi / Marketing Automation Facile.  
**Nodi:** `05_acquisizione/database-email-e-sequenze.md`.

Concetti inclusi:

- customer context prima del modello;
- segmentazione dinamica;
- assistente customer-facing governato come ruolo commerciale;
- next-best-offer da pattern reali;
- contesto d'uso come trigger con minimizzazione del dato.

Uso manuale: insegnare prima il sistema informativo e la policy; l'AI è applicazione, non principio generatore.

---

## P-024 — CRM come inventory di campagne

**Provenance:** MERENDA PRIMARY storico con sintesi moderna.  
**Nodo:** `05_acquisizione/database-email-e-sequenze.md`.

Le 16 campagne sono checklist operativa, non tassonomia obbligatoria del manuale. La casa primaria resta state segmentation / next action.

---

## P-025 — Referral attribution

**Provenance:** ASSIMILATED — Moreno Bonechi.  
**Nodo:** `05_acquisizione/referral-e-soddisfazione.md`.

Uso manuale: referral come coorte misurabile; preservare separazione fra meccanica referral primaria e strato di attribution assimilato.

---

## P-026 — Lock-and-Key / partnership complementare

**Provenance:** ASSIMILATED — Jay Abraham, Michael Simmons, Max Bernstein.  
**Nodo:** `05_acquisizione/partnership-distribuzione-e-combinazioni.md`.

Uso manuale: distinguere accesso transazionale da integrazione strutturale di asset complementari.

---

## P-027 — Endorsement economics

**Provenance:** ASSIMILATED — Jay Abraham, Michael Simmons, Max Bernstein.  
**Unità:** ACQ-063.

Uso manuale: trust transfer + host economics + performance alignment, mantenendo la reputazione dell'host come vincolo.

---

## P-028 — Sales handoff, lost-reason quality e pipeline age

**Provenance:** ASSIMILATED — Moreno Bonechi.  
**Nodi:** `06_vendita/prequalifica-follow-up-decisori.md`; `follow-up-lead-non-convertiti.md`.

Concetti:

- non far ripetere dati già forniti;
- separare fatti, ipotesi e domande;
- lost reason con evidenza/condizione di rientro;
- pipeline letta per età, ultima attività, qualità della qualifica e next step.

Uso manuale: integrare nel sales operating system, non presentarli come citazioni personali.

---

## P-029 — Review request trigger

**Provenance:** ASSIMILATED — Moreno Bonechi.  
**Nodo:** `08_brand/testimonianze-e-prova-sociale.md`.

Uso manuale: risultato positivo verificato → richiesta tempestiva → link → reminder non invasivo; non manipolare la recensione.

---

# 4. Business layer — assimilated extensions

## P-030 — Growth levers / clienti × valore × frequenza

**Provenance:** ASSIMILATED — Jay Abraham, Michael Simmons, Max Bernstein.  
**Nodo:** `09_business/numeri-cassa-e-crescita.md`.

Uso: strumento diagnostico moltiplicativo; nessun target percentuale fisso.

---

## P-031 — Allowable Acquisition Cost

**Provenance:** ASSIMILATED — Jay Abraham, Max Bernstein, Michael Simmons.  
**Nodo:** `09_business/numeri-cassa-e-crescita.md`.

Uso: tetto di acquisizione derivato dal valore economico atteso, riserva per delivery/risk/profit e payback; non spendere automaticamente tutto l'LTV.

---

## P-032 — Yield Gap

**Provenance:** ASSIMILATED — Jay Abraham, Michael Simmons, Max Bernstein.  
**Nodo:** `09_business/scalabilita-e-operativita.md`.

Uso: confrontare costo di delega con valore della capacità liberata; non canonizzare classi monetarie o moltiplicatori della fonte.

---

## P-033 — Process-to-Product

**Provenance:** ASSIMILATED — Jay Abraham, Max Bernstein, Michael Simmons.  
**Nodo:** `09_business/scalabilita-e-operativita.md`.

Uso: know-how tacito → processo trasferibile → prova → possibile prodotto/licenza; richiede domanda reale.

---

## P-034 — Capacity Access

**Provenance:** ASSIMILATED — Jay Abraham, Max Bernstein, Michael Simmons.  
**Nodo:** `09_business/scalabilita-e-operativita.md`.

Uso: build/buy/access della capacità; controllare qualità, dipendenza e rischio prima di scalare.

---

## P-035 — Automate normal / escalate exception; process-first; owner/handoff/checkpoint

**Provenance:** ASSIMILATED — Moreno Bonechi / MAF.  
**Nodo:** `09_business/scalabilita-e-operativita.md`.

Uso: processo prima del software, criteri stabili automatizzati/delegati, eccezioni escalated, owner esplicito del flusso.

---

## P-036 — Governance dei fornitori come sistema unico

**Provenance:** ASSIMILATED — Moreno Bonechi.  
**Nodo:** `09_business/scalabilita-e-operativita.md`.

Uso: outcome comune, attribution leggibile, messaging comune, confini e owner end-to-end.

---

## P-037 — Customer effort

**Provenance:** ASSIMILATED — Moreno Bonechi.  
**Nodo:** `09_business/retention-onboarding-e-customer-success.md`.

Uso: la complessità interna non deve essere trasferita al cliente; base operativa condivisa fra reparti.

---

## P-038 — Retention trigger automation e post-success next offer

**Provenance:** ASSIMILATED — MAF + jAI.  
**Nodo:** `09_business/retention-onboarding-e-customer-success.md`.

Uso: eventi/date/stati generano task; automazione evita dimenticanza, persona interpreta. Offerta successiva dopo risultato reale quando esiste bisogno pertinente.

---

## P-039 — Domanda non servita come dato

**Provenance:** ASSIMILATED — Moreno Bonechi.  
**Nodo:** `09_business/numeri-cassa-e-crescita.md`.

Uso: venduto + richiesta non servita + alternative → decisione di assortimento/capacità.

---

## P-040 — Rendimento delle spese discrezionali e capitale operativo nascosto

**Provenance:** ASSIMILATED — jAI.  
**Nodo:** `09_business/numeri-cassa-e-crescita.md`.

Uso: leggere spesa come capacità/capitale impiegato quando causalmente attribuibile; prepayment, terms, idle capacity e barter sono famiglie di opzioni, non prescrizioni automatiche.

---

# 5. Sintesi editoriali da etichettare come SYNTHESIS nel backend

## S-001 — Processo vendita end-to-end

Fonti: SAL-001…SAL-071 + offer/acquisition prerequisites.  
Stato: SYNTHESIS editoriale; nessun doctrinal gap sostanziale rilevato.

---

## S-002 — Costruzione del brand

Sequenza candidata:

**posizione → authority/credibility/proof → esperienza → reputazione → memoria → advocacy/community.**

Fonti: POS-057; BRD-001…BRD-058; customer success.

---

## S-003 — Customer lifecycle

Sequenza candidata:

**durata/frequenza naturale → acquisto → onboarding → uso/risultato → next offer/continuity → segnali di deviazione → intervento → riattivazione/referral/uscita naturale.**

Fonti: MRC-046…051; OFF-033…044; MKT-050…056; ACQ states; BUS-035…047.

---

## S-004 — Voice of Customer / market research

Fonti: mercato, positioning, query/intent, database, sales feedback, copy input, reviews/testimonials.

Stato: SYNTHESIS da formalizzare in Fase 4; il cross-section pass non mostra la necessità di attribuirla a una singola fonte.

---

# 6. Esito del provenance pass

La tracciabilità è sufficiente per procedere al curriculum senza replicare il source registry.

**G-003 può essere marcato `RESOLVED EDITORIALLY`**: esiste ora una mappa compatta dei punti in cui provenance e temporalità possono cambiare il significato della sintesi.

Il vincolo resta permanente: ogni nuova unità proveniente da fonte assimilata o ogni nuova precedence rilevante deve aggiornare questa mappa quando entra nel manuale.
