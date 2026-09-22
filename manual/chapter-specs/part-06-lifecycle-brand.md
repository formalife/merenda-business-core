# Chapter Specs — Parte VI: Mantenere la promessa e costruire valore nel tempo

---

# Capitolo 25 — Onboarding e customer success

## Domanda

Come faccio sì che la promessa commerciale diventi valore reale e non una vendita isolata, senza perdere nel passaggio ciò che il cliente ha davvero comprato?

## Learning outcome

Il lettore sa progettare il passaggio vendita→delivery/customer success, onboarding, first value, monitoraggio uso/frizioni e feedback loop; sa inoltre distinguere supporto reattivo da gestione proattiva del valore e del rischio.

## Prerequisiti

Capp. 11–13, 17 e 23; comprensione del customer state Cap. 17.

## Concetti obbligatori

- Post-Sell immediato della trattativa ≠ customer success continuativo;
- handoff strutturato sales→delivery/customer success;
- trasferire il **perché dell'acquisto**, non solo ordine/contratto;
- risultato/successo atteso dal buyer economico;
- come il successo verrà misurato;
- problema di business da risolvere;
- rischi di adozione/change management/politica interna già noti;
- tipping point che ha prodotto la decisione;
- promesse/condizioni rilevanti già concordate;
- customer experience come marketing operativo;
- onboarding come prevenzione del churn evitabile;
- aspettative/regole/primi passi;
- time-to-first-value;
- usage/inactivity/friction signals;
- support ticket ≠ ciclo chiuso;
- problem → cause → process/product correction;
- customer-facing staff trained on customer outcome;
- customer service reattivo vs customer success/account management proattivo;
- valore realizzato ≠ firma del contratto;
- criteria di successo da ricontrollare nel tempo;
- technical signal vs service communication vs sales opportunity;
- support→sales routing with exclusion rules;
- retention triggers as dates/states;
- automation remembers, human interprets;
- customer effort: client should not integrate departments;
- post-purchase confirmation/buyer's remorse reduction;
- facts vs AI inference in service-to-sales handoff;
- review di valore come strumento di allineamento, non rituale a calendario fisso;
- cadence della review dipendente dal ritmo di cambiamento/valore del cliente.

## Causalità centrale

**decisione commerciale → handoff del contesto causale → onboarding → uso → valore/frizione → correzione/review → esperienza reale → retention/proof/nuova evidenza.**

La vendita crea un commitment; il customer success deve trasformarlo in valore osservabile.

## Decision framework

### Handoff card post-vendita

1. che cosa significa successo per il cliente?;
2. come lo misureremo?;
3. quale problema/obiettivo ha giustificato l'acquisto?;
4. quali stakeholder contano?;
5. quali rischi di adozione o vincoli interni conosciamo?;
6. che cosa ha fatto scattare la decisione?;
7. quali promesse/condizioni non devono andare perse?;
8. chi possiede il prossimo passo?.

### Customer-success map

1. promise made;
2. first expected outcome;
3. steps/data/resources needed;
4. owner;
5. signals of correct use;
6. friction signals;
7. support/escalation;
8. process feedback;
9. success criteria/review;
10. success confirmation;
11. possible next need or risk.

### Value review

- le priorità sono cambiate?;
- stiamo consegnando il valore promesso?;
- quali attriti/rischi sono emersi?;
- stakeholder o metriche sono cambiati?;
- esiste un nuovo bisogno reale o soltanto desiderio del seller di espandere?.

## Metriche/evidenza

activation/first-value time, usage/completion, success-criteria attainment, support volume/repeat causes, customer effort proxies, outcome evidence, churn/renewal risk signals, response to check-ins/reviews, handoff completeness, repeated-context requests, adoption blockers.

## Errori da prevenire

- handoff = email inoltrata o solo contratto;
- onboarding = welcome email;
- ticket closed = problem solved systemically;
- firma = valore realizzato;
- customer success = supporto reattivo;
- tecnico forzato a vendere ogni segnale;
- automatismo commerciale durante complaint/open issue;
- review trimestrale trattata come cadenza universale;
- marketing promise unknown to operations;
- client repeatedly explaining the same context;
- nuova opportunità dichiarata tale prima di verificarne bisogno e fit.

## Esempi/casi

SC-004 onboarding/usage-risk section. WOW box as historical physical implementation, not requirement. Microcaso di deal chiuso con obiettivo economico chiaro che viene perso in un handoff puramente amministrativo.

## Backend sources

BUS-035…BUS-047; BUS-108…BUS-111; FND experience; P-037/P-038; `crosswalk/09_business.md`; `crosswalk/09_business_integration_2026-09-22.md`; SAL-093 bridge from Post-Sell.

## Collegamento

Prepara Cap. 26: soltanto dopo aver definito valore atteso, segnali e rischio ha senso progettare continuità, account growth, riattivazione o uscita.

## Definition first-use

onboarding, customer success, customer service vs customer success, handoff, customer effort, value review.

## Criteri di completezza

Il lettore sa disegnare un handoff che conserva il contesto causale della vendita e un sistema customer-success con first-value condition, success criteria, risk signals, review e feedback loop all'operating system.

---

# Capitolo 26 — Il customer lifecycle completo e la crescita dell'account

## Domanda

Che cosa dovrebbe accadere dopo il primo acquisto e come distinguo continuità sana, expansion, inattività, recupero e uscita naturale?

## Learning outcome

Il lettore sa modellare l'intera relazione dal primo acquisto a seconda vendita, account growth, continuità, riattivazione o uscita, partendo da durata/frequenza naturali e da valore realmente realizzato; sa riconoscere quando un nuovo bisogno deve rientrare nella normale qualification commerciale.

## Prerequisiti

Capp. 6, 8, 12, 17, 23, 25.

## Concetti obbligatori

- natural relationship duration;
- natural purchase/service frequency;
- cohort rotation;
- first transaction vs customer relationship;
- second sale/back-end;
- next-best-offer based on real need/pattern;
- continuity/subscription only when justified;
- expected behavior vs observed behavior;
- trigger before disappearance;
- active / at-risk / inactive / churned / recovery states;
- reactivation distinct from retention;
- win-back after explicit cancellation distinct from inactivity;
- replace churn vs stability vs growth;
- payer/user/need changes over lifecycle;
- offer after verified value when useful;
- exit can be natural and appropriate;
- portfolio account strategy: proteggere relazioni valide, conquistare nuovi account, recuperare relazioni perse, espandere account esistenti;
- portfolio logic ≠ sequenza cronologica obbligatoria;
- account growth nasce da valore realizzato + nuova evidenza;
- segnali di expansion: nuovo use case, team, executive, budget, problema o obiettivo;
- satisfaction ≠ automatic upsell permission;
- expansion opportunity ≠ vendita già qualificata;
- nuova opportunità → torna a problema, investimento/risorse e decision process;
- customer success può generare intelligence/accesso, non certificare il close;
- review di valore come luogo possibile di emersione del nuovo bisogno, non unico momento consentito;
- Keep-first o altre priorità contestuali non diventano regole universali.

## Causalità centrale

**valore realizzato + comportamento/stato + nuova evidenza → retention/next need/expansion/recovery route; se emerge una vera opportunità commerciale → nuova qualification → proposta coerente.**

La relazione esistente abbassa alcuni attriti ma non elimina la necessità di verificare il nuovo problema e il nuovo processo decisionale.

## Decision framework

### Lifecycle map

1. expected duration/frequency;
2. onboarding/first value;
3. active-state signals;
4. success criteria e valore realizzato;
5. next need/offer timing;
6. at-risk signals;
7. retention action;
8. inactive threshold;
9. reactivation route;
10. explicit-loss/win-back route;
11. natural exit;
12. cohort replacement need.

### Account-growth gate

Prima di trattare un segnale come expansion:

1. il valore originario è stato realizzato abbastanza?;
2. esiste un nuovo bisogno/use case concreto?;
3. chi lo ha espresso o quale evidenza lo mostra?;
4. riguarda lo stesso stakeholder o un nuovo buying group?;
5. esistono risorse/budget plausibili?;
6. come verrà presa la nuova decisione?;
7. è appropriato vendere ora o esiste un problema/complaint da risolvere prima?.

Se il gate passa, l'opportunità rientra nel processo commerciale del Cap. 23.

### Portfolio review

Per ogni account/relazione chiedere:

- va protetto?;
- esiste crescita reale da qualificare?;
- è perso ma recuperabile?;
- è sano ma naturalmente vicino alla fine del bisogno?;
- quale comportamento/evidenza cambia la categoria?.

## Metriche/evidenza

retention, churn by reason, repeat rate, frequency, time-to-second-purchase, reactivation rate, renewal, expansion pipeline qualified vs raw signals, expansion revenue/margin, LTV/payback supporting, outcome/satisfaction, cohort replacement, risk signals, multi-threading/stakeholder coverage where relevant.

## Errori da prevenire

- retention = keep forever;
- every customer should subscribe;
- generic reactivation campaign to all inactive states;
- buying more new leads while avoidable churn is high;
- offer next product before first value;
- happy customer = automatic upsell;
- service signal = opportunity already qualified;
- customer success = ottavo step della vendita;
- expansion senza nuovo Pain/investment/decision process;
- portfolio framework trattato come pipeline cronologica;
- treating natural exit as failure.

## Esempi/casi

SC-004 main case; Maccheroni as real partial lifecycle; expected-frequency reactivation mini-case; microcaso cliente soddisfatto che apre un nuovo use case ma richiede un nuovo decision-maker e nuovo budget.

## Backend sources

G-008 synthesis; MRC-046…MRC-051; OFF-033…OFF-044; MKT-050…MKT-056; ACQ state model; BUS-035…BUS-047; BUS-110…BUS-113; PROVENANCE_MAP S-003; SAL qualification supporting.

## Collegamento

Prepara Cap. 27: una relazione con valore verificato può generare referral e proof. Cap. 30 quantificherà l'economia della relazione; Cap. 23 governa qualsiasi nuova opportunity che richieda una decisione commerciale vera.

## Definition first-use

retention, churn, riattivazione, account growth/expansion; cohort only intuitive unless advanced metric needed.

## Criteri di completezza

Il lettore sa disegnare stati post-sale con expected behavior, triggers and routes, distinguere natural exit da preventable churn e spiegare quando un segnale di crescita account deve essere trasformato in una nuova opportunità da qualificare invece che in un upsell automatico.

---

# Capitolo 27 — Referral, testimonianze e review come flywheel

## Domanda

Come trasformo un risultato reale in nuova fiducia e nuova domanda senza aspettare il passaparola spontaneo?

## Learning outcome

Il lettore sa progettare referral e proof collection around verified customer success, protecting promoter reputation and traceability.

## Prerequisiti

Capp. 14, 25–26.

## Concetti obbligatori

### Referral

- satisfied customer is prerequisite, not sufficient condition;
- promoter lends trust and risks reputation;
- explicit ask at appropriate moment;
- make introduction easy;
- materials/tools for referral;
- incentive when economically and legally appropriate;
- benefit for referred party when coherent;
- referral attribution as cohort;
- track referrer→customer→value→decay;
- events/bring-someone as possible mechanism.

### Testimonials/reviews

- testimonial from real experience;
- ask specific questions;
- who speaks / purpose / order / placement / frequency / media / format;
- affinity/relevance;
- procrastination proof where real;
- request review after verified positive experience;
- proof library;
- ethical editing/approval.

## Causalità centrale

**real result → timely proof/referral request → trust transferred → new qualified attention → new experience → more proof.**

## Decision framework

Referral:

1. who achieved a real result?;
2. when is satisfaction strongest/most concrete?;
3. who might they know?;
4. how to make intro easy/safe?;
5. incentive/risk reversal needed?;
6. how to track economics?.

Proof:

1. what claim/objection needs evidence?;
2. which customer is most relevant?;
3. what specific experience/result?;
4. what format?;
5. where will it be used?;
6. consent/accuracy?.

## Metriche/evidenza

referral source/value, referral conversion, promoter activity/decay, review volume/quality/relevance, testimonial coverage by objection, downstream conversion where traceable.

## Errori da prevenire

- “happy clients will refer naturally”;
- generic “give me five names” pressure;
- promoter reputation ignored;
- testimonial = praise;
- fake/edited misleading review;
- reward that destroys margin/compliance;
- review requested before solving complaint.

## Esempi/casi

SC-004 proof after verified result; microcase promoter risk + strong risk reversal; testimonial “I wish I had acted sooner” only when real.

## Backend sources

`05_acquisizione/referral-e-soddisfazione.md`; BRD-014…BRD-025; P-025/P-029; BUS customer success.

## Collegamento

Prepara Cap. 28: public proof and reputation can amplify both positive and negative system outcomes.

## Definition first-use

referral; testimonial vs review distinction if useful.

## Criteri di completezza

Il lettore sa specify a referral moment, a referral mechanism and a proof collection brief tied to a specific claim/objection.

---

# Capitolo 28 — Reputazione e crisi

## Domanda

Come proteggo fiducia e continuità quando il sistema sbaglia o una decisione diventa pubblicamente contestata?

## Learning outcome

Il lettore sa mappare stakeholder/rischi, fare pre-mortem, coordinare verifica e risposta e distinguere comunicazione dalla correzione sistemica.

## Prerequisiti

Capp. 25–27; authority/proof Cap. 14.

## Concetti obbligatori

- reputation beyond customers;
- stakeholder mapping;
- pre-mortem;
- plausible negative readings vs material risk;
- strategy before impulsive response;
- temporary holding statement when needed;
- recognize → assume appropriate responsibility → remedy → system correction;
- pseudo-apology risk;
- root process/incentive/control cause;
- legal/comms coordination when applicable;
- fanbase response may differ from neutral/public/media;
- third-party proof after crisis supports a position, doesn't create it;
- association/partner reputational risk;
- internal controls as prevention, detailed Cap. 33.

## Causalità centrale

**operational reality → stakeholder interpretation → reputation; credible recovery requires factual remedy + systemic correction, not copy alone.**

## Decision framework

Pre-crisis:

1. stakeholders;
2. plausible harms/interpretations;
3. material risks;
4. owners/escalation;
5. proceed/modify/stop.

During crisis:

1. stop impulsive response;
2. verify facts;
3. define responsibility;
4. coordinate legal/operations/comms;
5. remedy;
6. communicate by stakeholder;
7. fix system;
8. monitor evidence.

## Metriche/evidenza

incident volume/severity, recurring cause, complaints, stakeholder response, operational correction completion; avoid vanity sentiment score as sole truth.

## Errori da prevenire

- reply while emotionally activated;
- blame one person without system fix;
- apologize without remedy;
- assume fanbase = market;
- third-party badge without specific position;
- controversy as default branding strategy.

## Esempi/casi

Synthetic operational error → public complaint → process fix. SC-006 can be referenced for reputation accumulation, not crisis.

## Backend sources

BRD-037…BRD-044; internal control node supporting; P-003/P-017 caveats.

## Collegamento

Prepares Cap. 29: brand memory is cumulative and includes how promises and failures are handled.

## Definition first-use

reputazione; stakeholder if not yet defined; pre-mortem.

## Criteri di completezza

Il lettore sa produce a one-page crisis pre-mortem and explain why communication without operational remedy is insufficient.

---

# Capitolo 29 — Come si accumula davvero un brand

## Domanda

Quando una posizione diventa memoria, preferenza e appartenenza invece di restare una campagna?

## Learning outcome

Il lettore sa ricomporre positioning, authority/proof, experience, reputation, repeated meaning and advocacy into a causal model of brand accumulation.

## Prerequisiti

Capp. 9–10, 14, 25–28.

## Concetti obbligatori

- brand ≠ logo/notoriety;
- declared positioning vs real mental association;
- position → acquisition → experience → relationship → memory;
- personality/point of view in domain;
- recurring true stories;
- documented transformation cases;
- fan/promoter distinct from satisfied customer;
- shared vocabulary that names real concepts;
- principles/standards;
- philosophical contrast against methods/practices, not persons;
- community after substance;
- audience/views vs customer base;
- launch curiosity as finite;
- history and word-of-mouth as accumulated asset;
- authority/reputation/real-world word of mouth reinforce each other;
- association risk.

## Causalità centrale

**distinct meaning × proof × repeated experience × reputation × time → memory/preference/advocacy.**

Formula is didactic, not numeric.

## Decision framework

Brand accumulation audit:

1. what should we mean?;
2. what real difference supports it?;
3. what proof makes it credible?;
4. does experience confirm it?;
5. what does market say unprompted?;
6. what stories/language/standards repeat it?;
7. what behaviors show memory/advocacy?;
8. where is the gap between declared and real brand?.

## Metriche/evidenza

repeat purchase where natural, referral, spontaneous reason-for-choice, search/reputation evidence, proof volume/relevance, community engagement only as supporting—not customer value substitute.

## Errori da prevenire

- branding before difference;
- views/followers counted as customers;
- community as substitute for product;
- slogans treated as brand creation;
- manufactured stories/vocabulary;
- controversial personality without strategic relevance.

## Esempi/casi

SC-006 main synthetic case; real examples from positioning only as microboxes.

## Backend sources

G-004 synthesis; BRD-001…BRD-058; POS-057; BUS experience; PROVENANCE_MAP S-002.

## Collegamento

Closes Part VI. Prepares Part VII: now value creation and customer relationship can be quantified more deeply and scaled.

## Definition first-use

brand complete definition, advocacy, brand community.

## Criteri di completezza

Il lettore sa explain why a brand cannot be produced directly by communication and can map the evidence that its desired meaning is or is not accumulating.