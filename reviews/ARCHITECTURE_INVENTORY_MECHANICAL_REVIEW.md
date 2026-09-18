# Architecture Inventory — Mechanical Review

Data: 2026-09-18
Fonte: artifact CI generato da `scripts/build_architecture_inventory.py`
Stato: REVIEWED MECHANICALLY / SEMANTIC FILTER REQUIRED

## 1. Numeri di base

La scansione corrente di `merenda/**/*.md` rileva:

- **60** file Markdown totali;
- **47** nodi canonici non-README, esclusi `INDEX.md` e `DECISION_ROUTER.md`;
- circa **636.551 byte** di doctrine layer Markdown;
- **0** link locali rotti;
- **0** nodi canonici senza incoming link;
- **0** nodi completamente privi di visibilità di routing, considerando anche i README di sezione;
- **605** heading candidati come non esplicitamente visibili nel control plane/README secondo euristica meccanica.

L'ultimo numero NON significa che esistano 605 gap di routing. È un upper bound rumoroso da filtrare semanticamente.

## 2. Conclusione meccanica principale

La KB non soffre di isolamento strutturale dei file.

Il problema non è:

> "esistono documenti che nessuno collega".

Il problema plausibile è:

> **un file può essere raggiungibile ma contenere molte unità semantiche che il routing di alto livello non rende scopribili nel caso giusto.**

Questa distinzione rafforza la scelta di una Retrieval Map a livello `path + anchor`.

---

# 3. Nodi-hub più densi

| Nodo | Dimensione | Incoming link | Lettura architetturale |
|---|---:|---:|---|
| `09_business/numeri-cassa-e-crescita.md` | ~43 KB | 29 | hub economico molto ampio; alto rischio di over-retrieval |
| `02_posizionamento/differenziazione-operativa.md` | ~26 KB | 25 | hub centrale di posizionamento; molte sotto-regole |
| `08_brand/autorita-e-marketing.md` | ~19 KB | 22 | prova/autorità attraversano più fasi del sistema |
| `03_offerta/offerta-a-risposta-diretta.md` | ~19 KB | 19 | offerta come hub trasversale |
| `06_vendita/prequalifica-follow-up-decisori.md` | ~24 KB | 17 | più stadi vendita nello stesso nodo |
| `04_marketing/gerarchia-domanda-e-canali.md` | ~18 KB | 17 | contiene molti concetti di domanda/canale non deducibili dal titolo |
| `03_offerta/front-end-e-back-end.md` | ~18 KB | 17 | economics e monetizzazione successiva molto interconnessi |
| `01_mercato/appropriatezza-clienti.md` | ~11 KB | 16 | cliente, economics, selezione e provenance mista |
| `09_business/scalabilita-e-operativita.md` | ~21 KB | 13 | capacità, processi e dipendenze operative |
| `03_offerta/prezzo-premium-e-percezione-del-valore.md` | ~19 KB | 12 | molte leve e caveat pricing nello stesso file |

## Implicazione

I nodi più centrali sono spesso anche tra i più lunghi.

Quindi un'architettura che aumenta recall semplicemente caricando sempre tutti gli hub rischia di degradare la precisione del contesto.

La progressive disclosure non è un'ottimizzazione cosmetica: è necessaria per mantenere alto segnale nei nodi più centrali.

---

# 4. File assenti dal Decision Router

La scansione rileva **12** nodi canonici non nominati direttamente dal `DECISION_ROUTER.md`:

1. `01_mercato/clienti-altospendenti.md`
2. `01_mercato/clienti-identificabili-e-target.md`
3. `02_posizionamento/esempi-di-differenziazione.md`
4. `04_marketing/eventi-proprietari-vip-experience.md`
5. `04_marketing/test-creativita-annunci.md`
6. `05_acquisizione/partnership-distribuzione-e-combinazioni.md`
7. `07_copy_comunicazione/checklist-risposta-diretta.md`
8. `07_copy_comunicazione/priorita-azione-e-inerzia.md`
9. `08_brand/pr-earned-media-e-notiziabilita.md`
10. `08_brand/reputazione-e-crisis-management.md`
11. `10_casi_studio/focalizzazione-funnel-e-capacita.md`
12. `10_casi_studio/motoargento-focalizzazione.md`

L'assenza dal Router non è automaticamente un difetto: alcuni nodi devono essere specialistici e recuperati solo dopo routing.

Diventa però un rischio quando il nodo contiene un concetto capace di cambiare la diagnosi prima che il router sappia di doverlo aprire.

Esempi già confermati:

- `clienti-identificabili-e-target.md` → user vs payer; clienti a scadenza;
- `priorita-azione-e-inerzia.md` → trigger reale prima del copy;
- `partnership-distribuzione-e-combinazioni.md` → partner win / endorsement economics;
- `clienti-altospendenti.md` → capacità economica != propensione a spendere.

Questi concetti sono ora coperti da eval specifici.

---

# 5. File visibili solo dal README di sezione

Sei nodi risultano assenti sia dal Router sia dal Sistema Operativo/Index e vengono scoperti dal percorso di sezione:

- `04_marketing/eventi-proprietari-vip-experience.md`
- `04_marketing/test-creativita-annunci.md`
- `07_copy_comunicazione/checklist-risposta-diretta.md`
- `07_copy_comunicazione/priorita-azione-e-inerzia.md`
- `10_casi_studio/focalizzazione-funnel-e-capacita.md`
- `10_casi_studio/motoargento-focalizzazione.md`

Questo non richiede di inserire tutti e sei nel Router.

Richiede che una mappa semantica sappia quando recuperarli senza aspettare che l'agente esplori manualmente ogni README.

I primi quattro sono candidati particolarmente interessanti perché governano azioni operative ricorrenti.

---

# 6. Section-level retrieval: evidenza quantitativa

L'euristica meccanica ha segnalato **605 heading** che non risultano ripetuti esplicitamente nei control layer/README pertinenti.

Il numero è volutamente sovrainclusivo. Tuttavia mostra la sproporzione fra:

- poche decine di route di alto livello;
- centinaia di unità semantiche interne.

Esempi ad alta leva già revisionati semanticamente:

### `clienti-identificabili-e-target.md`

- `clienti-a-scadenza-la-relazione-può-avere-una-durata-naturale`
- `consumare-non-significa-comprare`
- `progettare-la-campagna-su-più-assi-relazione-consapevolezza-profilo-directness`
- `profilare-solo-ciò-che-cambia-una-decisione`

### `appropriatezza-clienti.md`

- `whale-curve-individuare-la-coda-di-clienti-che-erode-il-profitto`
- `trasformare-lappropriatezza-in-criteri-di-accettazione`
- `concentrare-le-risorse-sui-prospect-migliori-quando-sono-limitate`
- `proof-by-refusal-uno-standard-diventa-più-credibile-quando-costa-davvero-sostenerlo`

### `gerarchia-domanda-e-canali.md`

- `quando-i-vincoli-restringono-lacquisizione-aumenta-il-peso-della-relazione`
- `la-domanda-ha-anche-una-dimensione-temporale`
- `la-profondità-del-funnel-dipende-anche-da-urgenza-e-bisogno-di-informazione`
- `volume-di-ricerca-e-intento-sono-cose-diverse`
- `con-intermediari-servono-sell-in-e-sell-through`

### `priorita-azione-e-inerzia.md`

- `prima-del-copy-trovare-il-trigger-reale-che-rende-il-bisogno-prioritario`
- `progettare-a-ritroso-dalla-call-to-action`
- `inerzia-prima-del-cambiamento`
- `mappare-le-conseguenze-reali-prima-di-scrivere`

## Implicazione

Non ha senso promuovere tutti questi heading nella mappa.

Il criterio deve essere:

> **una entry merita di entrare nella Retrieval Map quando può cambiare routing, diagnosi, evidenza richiesta, ordine causale, provenance o decisione.**

---

# 7. Stato eval dopo il mechanical review

La suite è stata estesa fino a **30 casi**.

I nuovi casi R026–R030 esercitano specificamente nodi con bassa visibilità nel control plane:

- trigger/priorità prima del copy;
- partnership economics;
- high spender: capacità vs propensione;
- testing creativo da winner/evidenza;
- eventi proprietari come asset a risposta misurabile.

Questo trasforma l'inventory in regression coverage anziché in una lista passiva di osservazioni.

---

# 8. Decisione architetturale confermata

L'evidenza meccanica supporta la seguente architettura candidata:

**Router compatto → Doctrine/Retrieval Map → anchor/contesto locale → eventuale espansione al nodo completo.**

Non supporta invece, allo stato attuale:

- espandere il Router con centinaia di casi;
- spezzare automaticamente tutti i file lunghi;
- introdurre GraphRAG come prerequisito;
- caricare tutti i nodi-hub ad ogni diagnosi.

La prossima misura utile è verificare se la seed Retrieval Map passa la CI e poi aumentare la coverage delle entry in funzione degli eval, non della quantità di heading.
