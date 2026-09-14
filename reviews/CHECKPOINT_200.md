# Checkpoint 200 — FASE 14 + FASE 15 — report definitivo

Eseguito da Claude Code sullo stato canonico `main` allo SHA `a8480238816ec8766fa96ad10c868ac9a2fc026c` ("Prepare checkpoint 200 handoff for Claude").

Nessun contenuto 201+ è stato processato semanticamente durante questo checkpoint. Nessuna acquisizione tecnica è stata eseguita. Nessun file frozen è stato modificato. Formalife non è stata introdotta nella KB.

## Stato al raggiungimento della soglia (invariato rispetto al pre-handoff)

- Video individuati: **468**
- Contenuti processati semanticamente: **200**
- `STUDIATO`: **194**
- `ESCLUSO`: **6**
- `DA STUDIARE`: **268**
- Corpus completo: **NO**

## FASE 14 — Refactor KB

### Metodo

Rilettura completa di tutta `merenda/` (42 file: 11 README + INDEX + 30 documenti di contenuto), non limitata ai file toccati dal batch 176–200:

- dimensione dei file (righe per documento);
- routing INDEX → README di sezione → documento;
- collegamenti interni e file orfani;
- sovrapposizioni segnalate esplicitamente dal pre-handoff:
  - `funnel-e-conversione.md` vs `information-marketing.md` vs `offerta-a-risposta-diretta.md` vs `front-end-e-back-end.md`;
  - `database-email-e-sequenze.md` vs `riattivazione-clienti.md` vs `referral-e-soddisfazione.md`;
  - coesione di `numeri-cassa-e-crescita.md`.

### Esito

**Nessuna modifica strutturale necessaria.** Decisione documentata di NON intervenire, con motivazione:

1. **Nessuna duplicazione reale.** I quattro documenti di acquisizione/offerta coprono territorio distinto e complementare: l'offerta (caratteristiche, elementi, desiderabilità), il sistema front-end/back-end (sequenza degli acquisti nel tempo), il funnel (landing, prova, diagnosi per stadi) e la piramide di information marketing (scala di impegno crescente). Ogni documento rimanda esplicitamente agli altri nella sezione "Collegamenti"; non ci sono paragrafi ridondanti da fondere.
2. **`database-email-e-sequenze.md` non si sovrappone a `riattivazione-clienti.md` o `referral-e-soddisfazione.md`.** Il primo tratta l'infrastruttura dati e la segmentazione per stato della relazione più una sequenza minima di contatto; il secondo (in `04_marketing`) tratta il trigger e la cadenza di ricontatto dei clienti fermi; il terzo tratta specificamente il meccanismo di richiesta/incentivo del passaparola. I tre si linkano a vicenda senza ripetere gli stessi contenuti.
3. **`numeri-cassa-e-crescita.md` (263 righe) resta un nodo coeso**, non sovradimensionato: tutti i paragrafi restano dentro il perimetro "economia del sistema di acquisizione/crescita" (ROI, CAC completo, incasso/margine/recupero CAC, cash flow, LTV, leve di crescita). È il file più lungo di `09_business` ma non anomalo rispetto a `offerta-a-risposta-diretta.md` (419 righe) o `prezzo-premium-e-percezione-del-valore.md` (371 righe), entrambi coerenti nel loro dominio. Nessuno split reale è stato individuato: uno split lungo sotto-argomenti (es. "CAC" vs "cash flow" vs "leve di crescita") avrebbe spezzato relazioni concettuali che il documento stesso collega esplicitamente (es. margine → payback → capacità di scalare), a scapito della comprensione.
4. **Nessun file orfano.** Tutti i 30 documenti di contenuto sono referenziati da almeno un README di sezione o dall'INDEX.
5. **Nessun collegamento rotto.** Il validator non segnala alcun "Link locale rotto".
6. **Nessuna traccia di Formalife nella KB.** Il validator non segnala "Contaminazione KB".
7. **Prevalenza delle fonti recenti già rispettata**: i documenti letti (es. `numeri-cassa-e-crescita.md`, `offerta-a-risposta-diretta.md`, `information-marketing.md`) marcano esplicitamente le fonti come "precedente"/"più recente" quando esistono formulazioni successive, e la KB non presenta regole concorrenti attive.

Non sono stati eseguiti interventi cosmetici (nessuna modifica al solo scopo di ridurre righe o rinominare senza beneficio concreto), in linea con l'indicazione esplicita del pre-handoff.

## FASE 15 — Audit tassonomia

### Metodo

Rilettura della tassonomia a 11 categorie alla luce del corpus accumulato (200/468) e della distribuzione dei 268 contenuti residui per categoria.

Distribuzione dei residui per categoria (da `sources/catalog.json`):

| Categoria | Residui | Note |
|---|---:|---|
| 00_fondamenti | 0 | area satura nel corpus attualmente processato |
| 01_mercato | 0 | area satura |
| 02_posizionamento | 0 | area satura |
| 03_offerta | 0 | area satura |
| 04_marketing | 0 | area satura |
| 05_acquisizione | 31 | |
| 06_vendita | 89 | area più popolosa in coda, KB attuale minima (1 solo documento) |
| 07_copy_comunicazione | 5 | piccolo blocco, alta densità attesa |
| 08_brand | 8 | piccolo blocco, alta densità attesa |
| 09_business | 87 | seconda area più popolosa |
| 10_casi_studio | 48 | area a rischio duplicazione più alto |

### Esito

**Nessuna modifica alla tassonomia.** Le 11 categorie restano valide. Motivazione:

- Le categorie 00–04 non hanno più contenuti residui: sono già state effettivamente sature dai primi 200 video. Non è un segnale che vadano fuse o eliminate — sono la parte più "fondativa" della dottrina e restano la base di riferimento per le categorie a valle.
- Le categorie oggi più sottili (`06_vendita`, `07_copy_comunicazione`, `08_brand`, con un solo documento ciascuna, tranne 08 che ne ha uno) hanno il maggior numero di contenuti ancora da processare proporzionalmente al materiale attuale in KB (`06_vendita`: 89 residui contro 1 documento attuale). Comprimere o rinominare queste categorie ora sarebbe prematuro: la loro apparente "sottigliezza" riflette lo stato di avanzamento dell'ingestione, non un difetto di confine tassonomico. Il Master Plan chiede di intervenire solo quando il beneficio è concreto: qui il beneficio concreto è aspettare che il contenuto arrivi, non anticipare una riorganizzazione.
- Nessuna sovrapposizione di confine è emersa tra le categorie esistenti durante la rilettura. Ogni README di sezione mantiene una distinzione esplicita rispetto alle sezioni limitrofe (es. `05_acquisizione/README.md` distingue esplicitamente da `03_offerta` e `06_vendita`).
- I disallineamenti storici di ordine noti tra `sources/catalog.json`, `sources/VIDEO_INDEX.md` e `sources/queue/QUEUE.md` (le 836 righe "Ordine/stato incoerente" del validator, tutte relative a `QUEUE.md`) non sono stati corretti in questo checkpoint, come richiesto esplicitamente dalla governance ("non correggerli indiscriminatamente... se non richiesto").

### Riclassificazione futura suggerita (non applicata ora)

Quando `06_vendita`, `07_copy_comunicazione` e `08_brand` avranno accumulato più documenti (indicativamente al prossimo audit tassonomia, checkpoint 250), rivalutare se:

- `06_vendita` richiede sotto-articolazione interna (es. preventivi/obiezioni vs gestione rete vendita vs remunerazione) quando avrà più di ~5 documenti;
- `08_brand` e `02_posizionamento` mantengono un confine chiaro anche dopo l'ingresso di più contenuti sull'autorità/reputazione (al momento non c'è sovrapposizione, ma il volume in coda per `08_brand`, per quanto piccolo, tratta reputazione/crisi che confina concettualmente con posizionamento).

Nessuna azione richiesta ora: si tratta di un'osservazione da verificare al prossimo audit, non di una decisione presa in questo checkpoint.

## Verifica specifica delle integrazioni 176–200

- I due nuovi nodi di `05_acquisizione` (`database-email-e-sequenze.md`, `funnel-e-conversione.md`) sono correttamente linkati dal README di sezione e non duplicano contenuto esistente (vedi FASE 14 sopra).
- `front-end-e-back-end.md` e `offerta-a-risposta-diretta.md` (aggiornati nel batch) restano coerenti internamente, con le fonti più recenti (28 maggio 2025, 23 settembre 2025) correttamente integrate senza sovrascrivere formulazioni precedenti ancora valide.
- `numeri-cassa-e-crescita.md` integra correttamente le quattro leve economiche (28 gennaio 2025) mantenendo la struttura precedente su CAC/cash flow.
- `referral-e-soddisfazione.md` integra la sistematizzazione del referral (27 giugno 2024) senza duplicare il contenuto precedente su soddisfazione/NPS.

## Novelty yield 176–200 e valutazione della saturazione

Dato confermato: **8/25 = 32%** di contenuti incrementali nel batch 176–200, con forte differenza tra shorts (176–184: 0/9) e long-form (185–200: 8/16 = 50%).

### Interpretazione per la coda 201–468

Il dato non viene trattato come legge universale (come richiesto esplicitamente dalla governance), ma come **evidenza sufficiente per giustificare una profondità di revisione differenziata**, per le seguenti ragioni:

1. Il campione è piccolo (25 video, 1 categoria dominante — acquisizione/casi studio) e non rappresenta tutte le aree residue.
2. Il segnale "short = meno incrementale" è coerente con l'aspettativa a priori (uno short è quasi sempre un estratto di un video più lungo già in coda o già studiato), ma non deve diventare una regola di esclusione: ogni short resta da processare e può comunque contenere una singola affermazione utile o un aggiornamento di dettaglio.
3. Le aree con **zero residui codificati come "alta densità attesa" dalla governance stessa** (`07_copy_comunicazione`, `08_brand`) sono anche le aree strutturalmente più piccole della KB attuale: qui la priorità "deep" non deriva dal novelty yield osservato (che non è stato misurato per queste aree, essendo praticamente vuote) ma dalla combinazione "poco materiale attuale + alta probabilità dichiarata di densità dottrinale nuova".

## Classificazione strategica A/B/C dei 268 contenuti residui

Prodotto l'artefatto [`reviews/RESIDUAL_CLASSIFICATION_201-468.md`](RESIDUAL_CLASSIFICATION_201-468.md), generato da [`scripts/classify_residual.py`](../scripts/classify_residual.py) (riproducibile, non manuale) a partire da `sources/catalog.json` e nell'ordine reale di `sources/queue/QUEUE.md`.

**Il file non modifica alcuno stato**: tutti i 268 contenuti restano `DA STUDIARE`. È uno strumento di pianificazione per chi eseguirà le fasi 8–13 sui batch successivi.

### Distribuzione risultante

- **A — HIGH PRIORITY / DEEP: 46 (17%)**
- **B — NORMAL / MEDIUM: 159 (59%)**
- **C — FAST REVIEW / HIGH DUPLICATION RISK: 63 (24%)**

Per categoria:

| Categoria | A | B | C | Totale |
|---|---:|---:|---:|---:|
| 05_acquisizione | 2 | 19 | 10 | 31 |
| 06_vendita | 19 | 55 | 15 | 89 |
| 07_copy_comunicazione | 5 | 0 | 0 | 5 |
| 08_brand | 5 | 0 | 3 | 8 |
| 09_business | 12 | 53 | 22 | 87 |
| 10_casi_studio | 3 | 32 | 13 | 48 |

### Criteri applicati (sintesi; dettaglio nel codice sorgente)

- **A**: tutti i video lunghi di `07_copy_comunicazione` e `08_brand` (blocco piccolo, alta densità dichiarata dalla governance); titoli con struttura numerata/framework/checklist ("N passi", "N modi", "checklist", "formula", "sistema"); video di `06_vendita` su aree esplicitamente segnalate come poco sature (preventivi, testimonial, follow-up, script, qualificazione, closing, obiezioni, decisori, provvigioni, rete vendita); video di `09_business` su CAC/LTV/cash flow/organigramma/delega/CRM/exit/franchising/scalabilità/ROI.
- **B**: il resto dei video lunghi senza segnali forti in un senso o nell'altro; casi studio su aziende/PMI specifiche non notissime (probabile consolidamento di dottrina, ma non scontato).
- **C**: contenuti motivazionali/mindset/polemici/truffe/fisco senza trasferibilità dottrinale diretta; live/stream generici senza struttura dichiarata; shorts (default, coerente con 0/9 osservato nel campione); casi studio su grandi brand esterni notissimi (Coca-Cola, Tesla, Nutella, Barilla, Ferragni, Dyson, ecc.), dove è alta la probabilità che il caso illustri principi già consolidati nella KB piuttosto che introdurne di nuovi.

**Importante**: C non significa "salta". Ogni contenuto C deve comunque ricevere transcript, revisione `.review.md`, categoria finale e stato (`STUDIATO` con nota di deduplicazione, oppure `ESCLUSO` con motivazione reale). La differenza rispetto ad A/B è la velocità con cui la deduplicazione può concludersi quando l'evidenza è chiara, non l'assenza di processo.

La classificazione è un'**ipotesi operativa verificata come compatibile con la governance**, non un'esenzione dalla revisione semantica di ogni video (Master Plan, fasi 7–13; PHASES.md; RULES.md §3).

## Proposta di workflow per 201–468 (da autorizzare, non applicata)

Questa sezione propone un affinamento del processo. **Non è stata implementata**: nessun file frozen è stato modificato. Se il proprietario del progetto la approva, dovrà essere recepita esplicitamente in `MASTER_PLAN.md`/`system/RULES.md` con autorizzazione.

1. **Ogni contenuto resta obbligatorio**: nessuno short, stream o caso studio viene saltato. Ognuno riceve categoria finale e stato.
2. **Profondità differenziata per classe**:
   - **A (deep)**: revisione semantica completa come finora, con particolare attenzione a procedure/numeri/framework citati esplicitamente, eventuale analisi visuale selettiva se il transcript segnala slide/numeri/grafici.
   - **B (normal)**: revisione semantica standard, confronto con la KB esistente, merge quando emerge un contributo reale.
   - **C (fast)**: revisione mirata a confermare rapidamente la deduplicazione: leggere il transcript per intero (non saltarlo), verificare in 1-2 passaggi se il contenuto è già coperto, e se sì marcare `STUDIATO` con nota sintetica "confermato/deduplicato rispetto a [documento]" oppure `ESCLUSO` con motivo, senza necessariamente produrre integrazioni KB estese. Se durante la lettura veloce emerge un segnale di novità (numero, procedura, framework non ancora presente), la revisione va **promossa a B o A** immediatamente: la classificazione iniziale è un punto di partenza, non un tetto.
3. **Promozione da FAST a DEEP**: sempre quando il transcript contiene una cifra/percentuale/soglia operativa non ancora in KB, un framework con nome proprio non ancora documentato, o una formulazione che sembra contraddire un principio già consolidato (in quel caso vale comunque la regola "il più recente prevale", ma la contraddizione va comunque documentata nella review).
4. **Fonti più recenti**: quando due contenuti (uno nuovo, uno già in KB) trattano lo stesso punto in modo incompatibile, la KB adotta la formulazione con data di pubblicazione più recente; la precedente viene eventualmente spostata in `archive/superseded/` se ha valore di contesto, altrimenti rimossa dalla KB attiva (RULES.md §4). Questo vale indipendentemente dalla classe A/B/C.
5. **Aree poco sature**: `06_vendita`, `07_copy_comunicazione`, `08_brand` meritano attenzione prioritaria nell'ordine di lavorazione dei prossimi batch, non solo nella profondità — a parità di posizione in coda, se la queue lo consente senza violare l'ordine dichiarato, questi contenuti dovrebbero essere anticipati. Questo checkpoint **non riordina** `QUEUE.md`: la proposta è per l'agente che gestirà i prossimi batch, da valutare esplicitamente.
6. **Evitare falsi negativi di novelty**: la classe C non deve diventare una scusa per una lettura superficiale. Il criterio di uscita rapida da C è "il transcript è stato letto per intero e non contiene nulla che la KB non abbia già", non "il titolo sembrava uno short quindi non serve leggerlo".
7. **Qualità del merge**: resta invariata la regola MERGE, NOT APPEND per ogni classe. La differenza di classe riguarda la velocità con cui si arriva alla decisione "non serve modificare la KB", non un abbassamento dello standard di merge quando serve modificarla.
8. **Batch da 25**: si propone di mantenere batch da 25 per l'acquisizione tecnica (fase 7), ma di permettere che il tempo di elaborazione semantica per batch vari in base alla composizione A/B/C del batch stesso (un batch con molti C può essere elaborato più rapidamente di uno con molti A), senza cambiare la cadenza dei checkpoint.
9. **Checkpoint 25/50**: nessuna modifica proposta. Restano invariati (FASE 14 ogni 25, FASE 14+15 ogni 50), come da `MASTER_PLAN.md` e `00_START_HERE.md`.
10. **Metrica di novelty per categoria**: si propone di aggiungere, ai prossimi checkpoint, il novelty yield calcolato per categoria oltre che globale (es. "novelty yield 06_vendita nel batch X: n/m"), per verificare se le aree oggi previste come "poco sature" confermano effettivamente un yield più alto. Questa è una proposta di reportistica, non richiede modifiche ai file frozen: può essere applicata nei prossimi `STATUS.md`/checkpoint senza autorizzazione aggiuntiva.

## Validazione

### Baseline (prima di qualsiasi modifica di questo checkpoint)

```
python3 scripts/validate_project.py   →  841 segnalazioni (SystemExit)
```

Composizione:

| Tipo | N | Natura |
|---|---:|---|
| `Ordine/stato incoerente: sources/queue/QUEUE.md <id>` | 836 | **Storico/baseline.** Disallineamento noto e documentato tra `catalog.json` e l'ordine/stato riportato in `QUEUE.md`. Esplicitamente escluso dalla correzione in questo checkpoint dalla governance ("non correggerli indiscriminatamente... se non richiesto"). |
| `File congelato modificato: MASTER_PLAN.md` / `system/HANDOFFS.md` / `system/FROZEN_FILES.md` | 3 | **Storico/baseline, non un'anomalia reale.** Il validator confronta il contenuto attuale con il tag Git `merenda-system-v1.0`. `system/FROZEN_FILES.md` documenta esplicitamente che esiste una versione successiva approvata dall'utente, `merenda-system-v1.1` (divisione Codex/ChatGPT/Claude), che ha modificato questi stessi file rispetto a v1.0. Il validator non è stato aggiornato per confrontare contro v1.1. Non è stata apportata alcuna modifica ai file frozen in questo checkpoint. |
| `Contatore STATUS errato: Video completati` / `Video rimanenti` | 2 | **Storico/baseline, drift di nomenclatura.** Il validator cerca le etichette letterali `Video completati` e `Video rimanenti` in `STATUS.md`, che invece usa `Contenuti processati semanticamente` e `Da processare`. Il contenuto numerico di `STATUS.md` è corretto (verificato manualmente contro `catalog.json`); è la corrispondenza testuale letterale attesa dal validator a non coincidere con la nomenclatura corrente di `STATUS.md`. |

### Dopo le modifiche di questo checkpoint

```
python3 scripts/validate_project.py   →  841 segnalazioni (identiche, diff vuoto)
git diff --check                      →  nessun output (nessun conflitto/whitespace)
git status --short                    →  solo i file nuovi di questo checkpoint, prima del commit
```

**Nessuna nuova anomalia introdotta.** Le modifiche di questo checkpoint (due file nuovi in `reviews/` e `scripts/`, aggiornamento di `STATUS.md` e di questo documento) non toccano nessuno dei tre gruppi di warning sopra.

### Controlli aggiuntivi eseguiti

- File frozen (`MASTER_PLAN.md`, `system/RULES.md`, `system/PHASES.md`, `system/HANDOFFS.md`, `system/FROZEN_FILES.md`): **non modificati** in questo checkpoint (confermato da `git status --short` e dal fatto che il validator segnala esattamente gli stessi 3 warning storici pre-esistenti, non uno in più).
- Assenza di Formalife in `merenda/`: confermata (nessun warning "Contaminazione KB").
- Link interni e file orfani: confermati assenti (nessun warning "Link locale rotto"; verifica manuale di tutti i 30 documenti di contenuto contro i rispettivi README).
- Working tree: pulito prima del checkpoint (`nothing to commit`); alla fine del checkpoint contiene solo le modifiche descritte in questo documento, da committare.

## File creati/modificati in questo checkpoint

- **Creato**: `scripts/classify_residual.py` — script riproducibile di classificazione A/B/C.
- **Creato**: `reviews/RESIDUAL_CLASSIFICATION_201-468.md` — artefatto con la classificazione completa dei 268 residui, in ordine di coda.
- **Modificato**: `reviews/CHECKPOINT_200.md` — questo documento (da pre-handoff a report definitivo).
- **Modificato**: `STATUS.md` — stato aggiornato post-checkpoint.
- **Nessuna modifica** a `merenda/` (FASE 14 ha concluso che non serviva alcun intervento strutturale).
- **Nessuna modifica** ai file frozen.

## Stato degli asset tecnici 201–225

Verificato: **nessuno dei 25 contenuti della prossima porzione di coda (`vD7zMl6YXzs` → `WCP26HC6wd0`, tutti in `05_acquisizione`, posizioni 201–225 di `sources/queue/QUEUE.md`) dispone di transcript in `sources/transcripts/`.**

Conforme all'attesa del pre-handoff: nessun asset tecnico 201+ era disponibile all'inizio del checkpoint, e questo checkpoint non ne ha acquisito alcuno (fuori mandato per Claude Code).

## Handoff

- **Corpus completo: NO**
- **Agente richiesto: CODEX**
- **Motivo**: gli asset tecnici (transcript) per la prossima porzione della coda (201–225, blocco `05_acquisizione`) non sono presenti nel repository. ChatGPT non può eseguire le fasi 8–13 senza transcript.
- **Prossima azione per Codex**: acquisizione tecnica del batch 201–225 (fase 7: transcript, eventuale fallback ASR, keyframe candidati dove segnalato), poi restituire il controllo a ChatGPT via `STATUS.md` secondo la procedura standard in `system/HANDOFFS.md`.
- **Primo contenuto non completato**: `vD7zMl6YXzs` — *Marketing Campaigns: Why Cost Per Lead Is Not Enough (And Where You Should Really Invest)*, posizione 201, categoria preliminare `05_acquisizione`, classe strategica **B**.
- **Prossimo checkpoint Claude**: dovuto a 225 (FASE 14) e a 250 (FASE 14 + FASE 15).

## Conferma finale

Nessun contenuto con posizione ≥ 201 è stato processato semanticamente, acquisito tecnicamente, o ha ricevuto una review `.review.md` durante questo checkpoint. La classificazione A/B/C è un artefatto di pianificazione, non un'ingestione.
