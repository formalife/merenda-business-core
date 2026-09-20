# Manual Audit — Fase 7

Data: 2026-09-20  
Branch auditato: `manual-drafting-2026-09-20`

## Verdetto

**PASS — nessun finding P0/P1 aperto.**

Il draft completo soddisfa il gate della Fase 7. Restano finding **P2 editoriali**, da chiudere nella Fase 8 senza riaprire l'architettura o la dottrina.

## Scope verificato

Draft reader-facing:

1. `manual/draft/part-01-fondamenti.md` — Capp. 1–4;
2. `manual/draft/part-02-mercato.md` — Capp. 5–8;
3. `manual/draft/part-03-posizionamento-offerta.md` — Capp. 9–13;
4. `manual/draft/part-04-domanda-acquisizione.md` — Capp. 14–19;
5. `manual/draft/part-05-copy-vendita.md` — Capp. 20–24;
6. `manual/draft/part-06-lifecycle-brand.md` — Capp. 25–29;
7. `manual/draft/part-07-economics-organizzazione.md` — Capp. 30–35;
8. `manual/draft/part-08-crescita-capstone.md` — Capp. 36–39.

Riferimenti di controllo:

- `MANUAL_CONTRACT.md`;
- `MANUAL_CURRICULUM.md`;
- `BEGINNER_GLOSSARY.md`;
- otto chapter specs;
- mini-audit locali svolti durante il drafting;
- nodi canonici live riletti prima di ogni blocco sostanziale.

---

# 1. Coverage

## Esito

**PASS**

Conteggio diretto dei capitoli nel draft:

- Parte I: 4;
- Parte II: 4;
- Parte III: 5;
- Parte IV: 6;
- Parte V: 5;
- Parte VI: 5;
- Parte VII: 6;
- Parte VIII: 4.

Totale: **39/39**.

Non emerge nessun capitolo mancante rispetto al curriculum approvato.

Gli otto blocchi coprono l'intera catena causale prevista:

**fondamenti → mercato/cliente → positioning/offerta → fiducia/domanda/acquisition → copy/vendita → lifecycle/brand → economics/organizzazione → bootstrap/reinvestimento/espansione/diagnosi.**

---

# 2. Doctrine fidelity e temporal precedence

## Esito

**PASS**

Le principali aree sensibili a formulazioni storiche più rigide sono state controllate e risultano nella versione attiva/condizionale.

### Front-end

Il draft definisce il front-end come **riduzione della barriera complessiva del primo sì**, non come sinonimo di prezzo basso o sottocosto.

### Pricing premium

Il draft non insegna “prezzo sempre più alto”. Premium pricing deriva da target, differenza, prova, offer e willingness-to-pay; il prezzo viene testato su conversione, margine, qualità, capacità e cassa.

### Cold outreach

Il contatto a freddo è trattato come modalità praticabile quando target, economics e processo lo rendono appropriato; non è vietato per principio né elevato a default.

### Focus

Focus non viene trasformato nella regola “una sola SKU”. È soprattutto concentrazione del significato e dell'acquisizione, con possibilità di catalogo/back-end coerenti.

### Line extension / multibrand

L'estensione non è trattata come fallimento automatico; viene valutata rispetto a significato, core, economics e complessità. Nuove categorie possono richiedere brand distinti.

### Vendita

Objection handling e looping restano diagnostici; non vengono trasformati in pressione. Il processo può concludersi correttamente con un non-fit/no-sale.

### Lifecycle

Retention non equivale a “tenere tutti per sempre”. Il draft distingue durata naturale, churn evitabile, riattivazione, riconquista e uscita naturale.

### Scale

La crescita è subordinata a unit economics, payback, cassa, capacità, processi e persone; non viene trattata come puro aumento di domanda.

### Expansion

Una nuova geografia/categoria riapre market research, competitive map e positioning; la fama del core o il co-branding non vengono trattati come proprietà automatica della nuova posizione.

---

# 3. Causalità e prerequisite order

## Esito

**PASS**

La progressione globale preserva i prerequisiti essenziali.

Punti particolarmente riusciti:

- economics minimi nel Cap. 2 prima di target, prezzo e canali;
- VoC nel Cap. 7 prima di positioning e copy;
- differenziazione prima della comunicazione;
- offer prima dell'acquisition massiva;
- authority/proof prima della richiesta di fiducia costosa;
- domanda/awareness/intent prima del canale;
- database/state prima del funnel adattivo;
- handoff/prequalifica prima della diagnosi commerciale;
- onboarding e first value prima della retention;
- unit economics/cash/capacity prima dell'organizzazione e della scala;
- core evidence prima di reinvestimento/espansione;
- Cap. 39 converte infine l'ordine pedagogico in sistema diagnostico ricorsivo.

Non emergono tattiche importanti insegnate prima del prerequisito che le rende razionali.

---

# 4. Beginner clarity e first-use terminology

## Esito

**PASS CON P2 DA COPY-EDIT**

Il draft generalmente definisce i concetti al primo uso e usa progressive disclosure correttamente. La Parte VII aumenta in modo coerente la complessità dopo che il lettore possiede già il vocabolario economico di base.

Restano però alcuni attriti terminologici.

### P2-T01 — Inglesismi non necessari

Particolarmente concentrati nelle Parti VII–VIII:

- `unit economics`;
- `CAC fully loaded`;
- `cohort economics`;
- `allowable acquisition cost`;
- `margin leakage`;
- `capacity economics`;
- `ownership`;
- `recruiting`;
- `asset-light`;
- `Capital Allocation Memo`;
- `Expansion Gate`;
- `Stageability`;
- `anti-pattern`;
- diversi nomi dei canvas.

Decisione Fase 8: mantenere l'inglese solo quando è realmente utile come termine di mercato; altrimenti usare l'italiano come forma principale e, se necessario, l'inglese tra parentesi al primo uso.

### P2-T02 — `B2B` usato prima di una definizione esplicita

Nella Parte II compaiono più esempi B2B. Per un lettore davvero beginner-first conviene espandere il primo uso in “business-to-business (B2B), cioè vendite fra imprese”. Stessa regola per eventuale B2C.

### P2-T03 — `escalation` anticipata

Il termine compare in esempi del Cap. 9 e nelle mappe dei Capp. 25/28, mentre la definizione editoriale completa vive nel Cap. 33.

Decisione Fase 8: nei capitoli precedenti usare una formula comune (“passaggio a un responsabile/livello superiore quando il caso esce dallo standard”) oppure definire localmente in linguaggio semplice.

### P2-T04 — `advocacy` nel Cap. 29

Il concetto è corretto ma l'inglese compare nel modello di accumulo del brand senza una definizione locale abbastanza visibile.

Decisione: usare “raccomandazione/difesa spontanea” nel testo principale e lasciare `advocacy` come termine secondario, se utile.

### P2-T05 — Micro-gergo di copy/operations

Parole come `claim`, `tagline`, `trade-off`, `headline`, `pitch`, `backlog`, `throughput`, `skill gap`, `behavior issue` sono comprensibili a un lettore di settore ma non necessarie per l'apprendimento del modello.

Decisione: tradurre o definire al primo uso significativo.

---

# 5. Reader-facing agnosticism e provenance

## Esito

**PASS CON UN P2 EDITORIALE**

Controllo testuale sul draft completo:

- nessuna occorrenza reader-facing di `Frank`;
- nessuna occorrenza reader-facing di `Merenda`;
- nessuna attribuzione personale delle regole;
- nessun blocco di fonte/provenance incorporato nella prosa;
- i casi sintetici sono presentati come fittizi/didattici;
- i numeri illustrativi non vengono elevati a benchmark universali.

### P2-A01 — Espressione editoriale nel Cap. 20

Compare:

> “torna alla casa primaria del problema”

“Casa primaria” appartiene alla logica editoriale della primary-home map e non serve al lettore.

Correzione Fase 8:

> “torna alla decisione a monte che manca”

oppure equivalente reader-facing.

### P2-A02 — Formulazione troppo vicina a catchphrase

Nel Cap. 38 compare il titolo:

> “Replicare successo, non povertà”

Il significato è corretto, ma la Fase 8 dovrebbe riscriverlo in formulazione più neutra/originale, per esempio:

> “Espandere un core che ha già dimostrato di reggere”

Il problema è editoriale/provenance, non dottrinale.

---

# 6. Operational usability

## Esito

**PASS**

Ogni parte contiene artefatti applicativi sufficienti a trasformare teoria in decisione.

Esempi:

- gate di mercato;
- scheda cliente desiderabile;
- Market Evidence Map;
- Decision Map;
- positioning hypothesis;
- Offer Canvas;
- Customer Journey Economics Map;
- Price Test Canvas;
- matrice affermazione→prova;
- Channel Decision Canvas;
- State Card;
- Funnel Node Card;
- Partnership Canvas;
- pre-copy brief;
- Handoff Card;
- Qualification Gate;
- Customer Success Map;
- Lifecycle Map;
- Referral & Proof Canvas;
- Brand Accumulation Audit;
- Cohort Economics Canvas;
- Cash Map;
- Capacity Map;
- Workflow Spec;
- Role Scorecard;
- Dependency Map;
- prototipo economico minimo;
- Capital Allocation Memo;
- Expansion Gate;
- router diagnostici finali.

La quantità è elevata ma segue la progressione del curriculum e non richiede che il lettore usi tutto contemporaneamente.

### P2-O01 — Uniformare la nomenclatura degli strumenti

`Map`, `Canvas`, `Card`, `Memo`, `Gate`, `Audit`, `Spec` vengono usati con logiche vicine ma non ancora editorialmente standardizzate.

Fase 8 deve decidere una tassonomia semplice, per esempio:

- **Mappa** per rappresentare uno stato/sistema;
- **Scheda** per raccogliere input operativi;
- **Gate** solo per verifiche sì/no;
- **Memo** solo per decisioni di allocazione capitale;
- **Audit** per controllo ex post.

---

# 7. Economic grounding

## Esito

**PASS**

Il manuale non usa vanity metric come criteri finali e collega sistematicamente le decisioni a:

- margine;
- CAC;
- payback;
- LTV;
- cost-to-serve;
- cassa;
- capacity;
- qualità economica del cliente.

Particolarmente importante: LTV non viene usato come scusa per ignorare il payback e il Cap. 31 distingue profitto, cassa, capitale circolante e cash-conversion timing.

### P2-E01 — Investimento come spesa con ritorno causale

La chapter spec del Cap. 30 richiede esplicitamente la disciplina “una risorsa/spesa è investimento solo quando esiste un ritorno causale plausibile e misurabile”.

Il draft insegna il principio in modo molto forte nel Cap. 37 (`Il prossimo euro deve avere un lavoro`) e lo applica nei Capp. 32–35. Nel Cap. 30, però, il principio è più implicito.

Non è un gap di manuale, ma una lieve deviazione dalla spec locale.

Correzione Fase 8: inserire nel Cap. 30 un breve ponte di 2–4 paragrafi o un richiamo esplicito; mantenere la primary home operativa dell'allocazione nel Cap. 37.

---

# 8. Redundancy e primary-home discipline

## Esito

**PASS**

Le ripetizioni osservate sono prevalentemente **functional redundancy**:

- “più traffico può amplificare un difetto” compare nei fondamenti, funnel, lifecycle e capstone perché svolge una funzione diagnostica diversa;
- CAC/LTV/payback vengono introdotti nel Cap. 2 e approfonditi nel Cap. 30 senza duplicare lo stesso livello di dettaglio;
- brand compare nel Cap. 10 come architettura/focus e nel Cap. 29 come sintesi di accumulo;
- referral viene richiamato nelle parti di domanda/database e sviluppato integralmente nel Cap. 27;
- process/automation compare prima come caveat e diventa teoria completa nel Cap. 33.

Non emerge nessun blocco che richieda merge distruttivo o rimozione di un capitolo.

### P2-R01 — Ridurre alcune ripetizioni formulaiche in copy-edit

Formule come:

- “non è X, è Y”;
- “non significa…”;
- “la domanda corretta è…”;
- “la sequenza è…”

sono pedagogicamente utili ma molto frequenti. La voce risulta coerente, però può diventare meccanica su centinaia di pagine.

Fase 8: variare ritmo e struttura senza perdere precisione causale.

---

# 9. Case ed evidence discipline

## Esito

**PASS**

- i casi sintetici sono riconoscibili come tali;
- i numeri sono dichiarati illustrativi o usati per mostrare una relazione matematica;
- gli outlier testimonial vengono trattati come outlier;
- nessun caso storico viene usato come prova universale;
- il Cap. 13 evita di dichiarare automaticamente vincitore il prezzo che converte meno ma produce più contribution nel caso sintetico;
- il Cap. 36 distingue interesse gratuito da domanda economica;
- il Cap. 39 mostra un esito possibile, non una legge.

Non emerge un problema P0/P1 di evidence inflation.

---

# 10. Cross-reference e integrazione globale

## Esito

**PASS CON P2**

La struttura usa correttamente i capitoli precedenti come prerequisiti e il Cap. 39 fornisce otto router per sintomo:

1. troppo pochi clienti;
2. troppo poche lead;
3. bassa conversione commerciale;
4. pressione sul prezzo/sconti;
5. churn alto;
6. cassa debole;
7. fondatore indispensabile;
8. desiderio di espansione.

Questo chiude correttamente il passaggio da curriculum lineare a sistema diagnostico.

### P2-X01 — Uniformare forma delle cross-reference

Nel draft convivono:

- “nel Capitolo X”;
- “più avanti”;
- nomi di strumenti già introdotti;
- alcuni riferimenti impliciti.

Fase 8: mantenere cross-reference esplicite solo quando aiutano realmente la navigazione, con formato coerente.

---

# Finding register finale

| ID | Priorità | Tema | Stato | Azione Fase 8 |
|---|---|---|---|---|
| P2-T01 | P2 | Inglesismi diffusi | OPEN | italianizzare/definire |
| P2-T02 | P2 | B2B/B2C first use | OPEN | espandere primo uso |
| P2-T03 | P2 | escalation anticipata | OPEN | tradurre/definire localmente |
| P2-T04 | P2 | advocacy | OPEN | usare italiano come forma principale |
| P2-T05 | P2 | micro-gergo copy/operations | OPEN | semplificare/definire |
| P2-A01 | P2 | “casa primaria” reader-facing | OPEN | riscrivere |
| P2-A02 | P2 | catchphrase Cap. 38 | OPEN | riscrivere titolo/formulazione |
| P2-O01 | P2 | Map/Canvas/Card/Memo/Gate naming | OPEN | standardizzare tassonomia |
| P2-E01 | P2 | investimento causale più esplicito in Cap. 30 | OPEN | aggiungere ponte breve |
| P2-R01 | P2 | ritmo/formule ripetitive | OPEN | prose pass |
| P2-X01 | P2 | cross-reference form | OPEN | uniformare |

**P0 aperti: 0**  
**P1 aperti: 0**  
**P2 aperti: 11**

---

# Gate Fase 7

Il gate richiede:

> nessun finding P0/P1 aperto.

**Gate soddisfatto.**

La Fase 7 può essere dichiarata **DONE / PASS**.

La Fase 8 non deve ridisegnare il curriculum. Deve trasformare un draft dottrinalmente completo in un master editoriale coerente:

**terminologia → voce → cross-reference → strumenti → esercizi/casi → glossario/indice → pulizia backend → master finale.**
