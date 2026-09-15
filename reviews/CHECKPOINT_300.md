# Checkpoint 300 — pre-handoff ChatGPT — FASE 14 + FASE 15 richieste

Stato semantico raggiunto sul branch `semantic-276-300`, costruito dalla HEAD tecnica `7a2afa3d0641a1e15481c71bd95d45d65aeab615` del branch `acquisition-276-300`.

Questo documento è il **pre-handoff del checkpoint 300**. La revisione semantica 276–300 è completa; Claude Code deve ancora eseguire **FASE 14 + FASE 15**. Nessun contenuto 301+ è stato processato semanticamente.

## Stato al raggiungimento della soglia 300

- Video individuati: **468**
- Contenuti processati semanticamente: **300**
- STUDIATO: **294**
- ESCLUSO: **6**
- DA STUDIARE: **168**
- Batch 276–300: **25/25 STUDIATO**
- Nuovi ESCLUSO: **0**
- Review 276–300: **25/25**
- Primo contenuto non processato nella nuova queue: **301 — `asMedYJtd4I` — “CONCORRENZA SLEALE dei dipendenti?”**

## Base tecnica

- branch: `acquisition-276-300`
- base: `81b0829bf99427ae5c46db8f33346fdab3d6c8ef`
- HEAD tecnica: `7a2afa3d0641a1e15481c71bd95d45d65aeab615`
- 25/25 ACQUIRED e transcript utilizzabili
- manuali / automatici it-orig: **2 / 23**
- ASR / NO_IT / errori finali / pending: **0 / 0 / 0 / 0**
- coverage: **98,89–100%**
- keyframe: **25 su 7 video**
- validator tecnico prima/dopo: **842 / 842 identico**
- nessun asset nuovo 301+

## Esito semantico 276–300

### Novelty binaria

- **Incrementali: 13/25 = 52%**
- **Deduplicati/confermativi: 12/25 = 48%**

Incrementali: 276, 277, 278, 283, 284, 285, 289, 291, 294, 295, 296, 297, 298.

Deduplicati/confermativi: 279, 280, 281, 282, 286, 287, 288, 290, 292, 293, 299, 300.

### Weighted Novelty

| Peso | Significato | N | Punti |
|---|---|---:|---:|
| 2 | nuovo framework/nodo sostanziale | 4 | 8 |
| 1 | estensione realmente utile | 9 | 9 |
| 0 | conferma/dedup | 12 | 0 |
| **Totale** |  | **25** | **17/50** |

Peso 2:
- 276 — copy come traduzione del posizionamento + temperatura/sorgente;
- 284 — reputazione e crisis management;
- 291 — customer-first/customer-success operating loop;
- 296 — replicabilità del sistema prima di franchising/nuova unità.

Il 283 è peso 1, non 2, per evitare doppio conteggio: introduce molte procedure retention/onboarding, ma viene consolidato nello stesso nodo la cui formulazione principale più recente è il 291.

## Routing finale

| Categoria | N |
|---|---:|
| 00_fondamenti | 1 |
| 01_mercato | 0 |
| 02_posizionamento | 1 |
| 03_offerta | 2 |
| 04_marketing | 1 |
| 05_acquisizione | 0 |
| 06_vendita | 2 |
| 07_copy_comunicazione | 6 |
| 08_brand | 2 |
| 09_business | 10 |
| 10_casi_studio | 0 |
| **Totale** | **25** |

## Nuovi nodi KB

1. `merenda/07_copy_comunicazione/copy-posizionamento-e-temperatura-traffico.md`
2. `merenda/08_brand/reputazione-e-crisis-management.md`
3. `merenda/09_business/retention-onboarding-e-customer-success.md`

### Copy: posizionamento → sorgente → linguaggio

276 diventa la fonte principale del nuovo nodo. La regola:

**posizionamento/decisione strategica → copy → adattamento a sorgente e dialogo mentale → risposta misurabile.**

277 aggiunge l'esercizio vendita parlata → trascrizione → audit degli argomenti. 280 conferma il quadro ma non aggiunge dottrina. Numeri fissi di varianti e linguaggio allarmistico non vengono canonizzati.

278 aggiorna separatamente `priorita-azione-e-inerzia.md` con:

**problema reale → conseguenze reali a valle → stato desiderato → soluzione → CTA.**

### Reputazione e crisi

284 crea il primo nodo dedicato al crisis management:

**stakeholder map → pre-mortem → stop alla risposta impulsiva → fatti/responsabilità → rimedio → correzione sistemica.**

Percentuali, provocazioni e pseudo-scuse non diventano regole.

285 aggiunge al nodo autorità il rischio reputazionale bidirezionale delle associazioni/partnership.

### Retention e customer success

283 + 291 vengono fusi, non duplicati.

291 (25 giugno 2025) è la fonte principale:

**feedback → desideri/miglioramenti + frizioni → prodotto/processo → esperienza → nuova misura.**

283 aggiunge CRM, onboarding, follow-up d'uso, supporto che risale alle cause, feedback e quality review.

Il principio generale più recente del 27 novembre 2025 già presente in `marketing-first.md` resta prevalente: l'esperienza reale è parte del marketing.

## Altre integrazioni

- 289 → `preventivo-consulenza-diagnosi.md`: misure/test validi possono sostenere la diagnosi; esplicito rifiuto della pseudo-scienza.
- 294 → `numeri-cassa-e-crescita.md`: mappa picchi/valli di capacità per stagione/mese/settimana/giorno.
- 295 → `scalabilita-e-operativita.md`: stress test dei single point of failure e piano B.
- 296 → `espansione-nicchie-e-multibrand.md`: checklist di replicabilità prima di franchising/nuova sede.
- 297 → `marketing-del-personale.md`: progettare ruoli stretti e allenabili prima del recruiting.
- 298 → `numeri-cassa-e-crescita.md`: leve per anticipare/stabilizzare cash flow.

## Prevalenza temporale e deduplicazioni importanti

- 281: brand vs categoria già meglio coperto dall'architettura brand successiva.
- 282: test/garanzia per brand debole già coperti dalle fonti offerta del maggio 2026.
- 286: authority + qualification già coperti da fonti vendita/brand successive.
- 287: struttura sales letter già nella checklist DR e nell'offerta.
- 288: market-message-media e continuità marketing-vendita già distribuiti nei nodi canonici.
- 290: “plug and play” assorbito da “facile da accettare”.
- 292: LTV + payback/cassa già esplicitamente canonizzati e aggiornati nel 2026.
- 293: responsabilità strategica non delegabile già in marketing-first; la customer experience del novembre 2025 è più recente.
- 299: ATV/LTV/LT gross margin/CAC/payback già nel nodo numeri; soglie 3:1 e 30 giorni non sono universali e non prevalgono sulle fonti successive.
- 300: diagramma non interamente visibile nei keyframe; nessuna parte assente viene ricostruita. Le fonti 2024–2025 su ruoli/scalabilità sono più recenti.

## Valutazione della riprioritizzazione

Il batch ottimizzato produce **52% di contenuti incrementali**, contro **44%** del batch 251–275.

Questo indica che la riprioritizzazione ha recuperato information gain. Tuttavia Weighted Novelty **17/50** mostra che la maggior parte del valore nuovo è composta da estensioni, non da nuovi grandi framework.

La raccomandazione pre-FASE15 è quindi:

**non fermare ancora la KB Merenda, ma non tornare alla coda sequenziale.**

Dopo FASE 15, se la tassonomia conferma questi risultati, ha senso un ulteriore batch **TARGETED/adattivo** concentrato sui gap rimasti, non sui prossimi 25 storici.

Claude deve poter modificare questa raccomandazione se il refactor globale mostra che una parte della novelty è in realtà duplicata altrove.

## Handoff — CLAUDE CODE

Checkpoint richiesto: **300 — FASE 14 + FASE 15**.

Claude deve:

1. eseguire FASE 14 su tutta la KB con MERGE, NOT APPEND;
2. eseguire FASE 15 sull'intera tassonomia dopo 300 contenuti;
3. controllare in particolare i tre nuovi nodi e i loro confini;
4. verificare che customer success non duplichi marketing-first, riattivazione o referral;
5. verificare che crisis management resti distinto da PR/autorità;
6. verificare che il nuovo nodo copy non duplichi checklist, gerarchia domanda/canali o testing creatività;
7. controllare i nuovi inserimenti in numeri/cassa, scalabilità, espansione e recruiting;
8. rivalutare saturazione e Information Priority dei 168 residui alla luce della KB post-refactor;
9. stabilire se procedere con un altro batch TARGETED o restringere ulteriormente ai gap;
10. non acquisire né processare semanticamente 301+;
11. non modificare i file frozen;
12. verificare validator, link, ancore, orfani e contaminazione Formalife;
13. trasformare questo file da pre-handoff a report definitivo del checkpoint 300.

**Prossimo agente: CLAUDE CODE.**
