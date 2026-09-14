# Checkpoint 250 — pre-handoff ChatGPT — FASE 14 + FASE 15 dovute

Stato semantico raggiunto sul branch `semantic-226-250` a partire dalla HEAD tecnica `c579de5e5ecf56bf19dd2b5d36a72df33ef80752`.

Questo documento è il **pre-handoff a Claude Code**. Il checkpoint 250 non è definitivo finché Claude non ha eseguito **FASE 14 + FASE 15**, validato il progetto e aggiornato questo report/STATUS con l'esito del refactor e dell'audit tassonomico.

Nessun contenuto 251+ è stato processato semanticamente. Nessun file frozen è stato modificato.

## Stato al raggiungimento della soglia 250

- Video individuati: **468**
- Contenuti processati semanticamente: **250**
- `STUDIATO`: **244**
- `ESCLUSO`: **6**
- `DA STUDIARE`: **218**
- Corpus completo: **NO**
- Batch 226–250: **25/25 STUDIATO**
- Nuovi ESCLUSO nel batch: **0**
- Review 226–250: **25/25**

Primo contenuto ancora non processato: **251 — `ellOvKnIOqk` — “The #1 Sales Technique for a Record-Breaking Sales Team”**.

## Base tecnica 226–250

Handoff Codex:

- branch: `acquisition-226-250`
- base: `da0a20c00882f287674635109e625fef47f23408`
- HEAD tecnica: `c579de5e5ecf56bf19dd2b5d36a72df33ef80752`
- tentati / acquisiti / transcript utilizzabili: **25 / 25 / 25**
- automatiche italiane / manuali: **25 / 0**
- ASR / NO_IT_TRANSCRIPT / errori finali / pending: **0 / 0 / 0 / 0**
- 23 nuovi download; 232 e 233 avevano già metadata/JSON3 nella base
- 9 keyframe su 4 video, ispezionati nella fase tecnica
- validator tecnico prima/dopo: **841 warning identici**
- `git diff --check`: superato
- frozen, KB e semantica invariati nella fase tecnica

Limiti tecnici documentati da Codex:

- 227: copertura temporale transcript **95,51%**
- 228: copertura temporale transcript **92,79%**
- piccoli sforamenti timestamp fino a **2,360 s**, senza correzioni arbitrarie

La revisione semantica non ha basato nuove regole sulle code non coperte di 227/228.

## Esito semantico 226–250

### Novelty globale

- **Incrementali: 16/25 = 64%**
- **Deduplicati/confermativi: 9/25 = 36%**
- Nessun nuovo ESCLUSO

Incrementali:

- 229 — `7zRyOC3Z0lM`
- 232 — `MwNCMJE8sRk`
- 233 — `g-VOlvqnL_8`
- 234 — `ggJnCJCXIO4`
- 235 — `KZ78VhszH_o`
- 236 — `3ZNE75sPen8`
- 237 — `lwuJ6MYETUw`
- 238 — `T5ccJyQqX9c`
- 240 — `dYMeQuuT8QY`
- 241 — `8XduYN366z0`
- 242 — `rcVXvepx-l8`
- 243 — `gcQKKrbZW28`
- 245 — `Zzh6PXGTmD0`
- 247 — `V8CVwcH5rwA`
- 248 — `r649dAXopLM`
- 250 — `uOu65O88jrU`

Deduplicati/confermativi:

- 226, 227, 228, 230, 231, 239, 244, 246, 249

### Novelty per categoria finale

| Categoria | Video | Incrementali | Yield |
|---|---:|---:|---:|
| 01_mercato | 1 | 1 | 100% |
| 03_offerta | 1 | 1 | 100% |
| 04_marketing | 3 | 1 | 33% |
| 05_acquisizione | 2 | 0 | 0% |
| 06_vendita | 8 | 5 | 63% |
| 07_copy_comunicazione | 3 | 2 | 67% |
| 08_brand | 5 | 4 | 80% |
| 09_business | 2 | 2 | 100% |
| **Totale** | **25** | **16** | **64%** |

Il dato conferma l'ipotesi del checkpoint 200 che le aree meno sature — soprattutto vendita, copy e brand — potessero avere yield più alto, ma il campione resta troppo piccolo per trasformarlo da solo in regola frozen.

## Routing finale 226–250

| Categoria | N |
|---|---:|
| 01_mercato | 1 |
| 02_posizionamento | 0 |
| 03_offerta | 1 |
| 04_marketing | 3 |
| 05_acquisizione | 2 |
| 06_vendita | 8 |
| 07_copy_comunicazione | 3 |
| 08_brand | 5 |
| 09_business | 2 |
| 10_casi_studio | 0 |

Il routing finale diverge fortemente dalla categoria preliminare della coda, come previsto dal workflow: la classificazione semantica finale prevale.

## Integrazioni principali

### 229 — conversione economica oltre il primo front-end

Aggiornato `merenda/03_offerta/front-end-e-back-end.md`.

La fonte del 16 dicembre 2025 distingue la prima transazione dalla conversione economica completa quando il front-end lavora a break-even/perdita: vendere il front-end non significa ancora aver recuperato CAC e prodotto il margine progettato.

La terminologia “unconverted lead” non viene trasformata in definizione contabile/giuridica di cliente.

### 232 + 238 — follow-up dei lead non convertiti

Creato `merenda/06_vendita/follow-up-lead-non-convertiti.md`.

La procedura integra:

- raccolta dati;
- scelta canali;
- ragione concreta del ricontatto;
- rapidità sui lead caldi;
- sequenza preparata;
- politica dell'offerta;
- angolo del messaggio;
- quattro livelli 2025: materiale immediato, sequenza multicanale, presenza continuativa, intervento umano della vendita.

### 233 — preventivo come diagnosi/consulenza

Creato `merenda/06_vendita/preventivo-consulenza-diagnosi.md`.

Principio:

**problema → analisi → diagnosi → prescrizione/offerta**

La consulenza a pagamento resta una scelta di modello, non un obbligo universale.

### 234 — ordine delle leve di crescita

Aggiornato `merenda/09_business/numeri-cassa-e-crescita.md`.

Gerarchia 2025:

1. retention;
2. referral;
3. focus/valore;
4. processi vendita;
5. conversione;
6. valore transazione;
7. frequenza;
8. solo dopo, più lead.

Il modello è una gerarchia diagnostica, non un divieto di acquisizione finché i primi sette punti non sono perfetti.

### 235 — single point of failure

Aggiornato `merenda/09_business/scalabilita-e-operativita.md`.

Generalizzato il rischio della dipendenza da “uno”:

- una sola fonte acquisizione;
- un solo venditore;
- una sola persona chiave;
- una sola sede/infrastruttura critica.

La resilienza operativa non contraddice il focus di posizionamento.

### 236 — checklist di risposta diretta

Creato `merenda/07_copy_comunicazione/checklist-risposta-diretta.md`.

Le 22 tattiche della fonte sono state astratte in criteri durevoli:

- CTA;
- beneficio;
- livello di educazione;
- offerta/incentivo;
- facilità di risposta;
- percorso autonomo/umano;
- tracciabilità;
- coerenza con posizionamento.

Numero verde, coupon e altre implementazioni storiche non diventano requisiti universali.

### 237 + 248 — testimonianze e prova sociale

Creato `merenda/08_brand/testimonianze-e-prova-sociale.md`.

Framework:

- chi parla;
- scopo;
- ordine;
- posizione;
- frequenza/varietà;
- media;
- formato.

Aggiunta l'applicazione specializzata 2024 “avrei voluto farlo prima” per documentare, quando reale, il costo dell'attesa e contrastare la procrastinazione.

### 240 — bisogno tecnico vs stato desiderato

Aggiornato `merenda/07_copy_comunicazione/priorita-azione-e-inerzia.md`.

Struttura:

**bisogno tecnico → conseguenza desiderata → stato futuro percepito come migliore**

La trasformazione non autorizza promesse irrealistiche o scorciatoie false.

### 241 — brand community e fan

Creato `merenda/08_brand/brand-community-e-fan.md`.

Sette elementi:

1. personalità riconoscibile;
2. storie ricorrenti;
3. casi di trasformazione;
4. clienti promotori;
5. vocabolario condiviso;
6. principi non negoziabili;
7. contrasto filosofico.

Le analogie religiose/cultuali della fonte sono state neutralizzate in concetti di brand/community.

### 242 — capacità, volontà e percezione del valore

Aggiornato `merenda/01_mercato/clienti-altospendenti.md`.

Separati tre problemi:

1. capacità economica;
2. propensione/priorità di spesa;
3. comprensione della differenza che giustifica il premium.

Il modello delle “sei personalità” non è trattato come tassonomia scientifica rigida.

### 243 — eventi proprietari / VIP experience

Creato `merenda/04_marketing/eventi-proprietari-vip-experience.md`.

L'evento viene trattato come asset commerciale integrato:

**invito → esperienza → dati → offerta → follow-up**

Guest star, limousine e altri esempi estremi restano esempi, non requisiti.

### 245 — due livelli di fiducia

Aggiornato `merenda/08_brand/autorita-e-marketing.md`.

Nelle decisioni complesse il prospect deve fidarsi:

1. del fornitore;
2. della propria capacità di prendere una decisione corretta e difendibile.

Per i contatti più freddi/rischiosi, la prova va introdotta prima nel messaggio. Le fonti 2026 già presenti restano prevalenti.

### 247 — diagnosi standardizzata, prescrizione personalizzata

Aggiornato `merenda/06_vendita/prequalifica-follow-up-decisori.md`.

Principio:

**stesso metodo di analisi → evidenze diverse → prescrizione diversa**

Uno script è una coreografia diagnostica minima, non una lettura meccanica identica per ogni cliente.

### 250 — canale sincrono nei cicli consulenziali

Aggiornato `merenda/06_vendita/prequalifica-follow-up-decisori.md`.

Il marketing può standardizzare informazioni e preparazione; nei cicli complessi, voce/video/incontro conservano una funzione interattiva che non va sostituita automaticamente con lunghi scambi asincroni.

Non viene consolidato un divieto universale di WhatsApp/email: testo/chat restano appropriati per coordinamento, documenti, reminder, follow-up e vendite semplici.

## Correzione interna importante: RFM nel 239

Durante la revisione del 239 era stata inizialmente riconosciuta come nuova l'applicazione RFM alla riattivazione.

Il cross-check completo ha mostrato che **RFM era già canonico in `merenda/01_mercato/appropriatezza-clienti.md`**.

Correzione effettuata prima della chiusura del batch:

- il 239 è classificato **Novelty: no**;
- la duplicazione è stata rimossa;
- `riattivazione-clienti.md` conserva soltanto un rinvio operativo al nodo canonico RFM;
- nessun secondo framework RFM rimane attivo.

Questo è coerente con **MERGE, NOT APPEND**.

## Prevalenza temporale rilevante: video 249

Il video 249 (16 ottobre 2024) presenta fra le tecniche di urgenza anche scarsità “artificiale”.

La KB **non** adotta questa formulazione perché il materiale più recente 2025 già canonico in `offerta-a-risposta-diretta.md` richiede che urgenza/scarsità abbiano una ragione reale e non diventino finzione permanente.

Il 249 è quindi deduplicato senza modifica KB.

## Nuovi nodi KB creati nel batch

1. `merenda/04_marketing/eventi-proprietari-vip-experience.md`
2. `merenda/06_vendita/follow-up-lead-non-convertiti.md`
3. `merenda/06_vendita/preventivo-consulenza-diagnosi.md`
4. `merenda/07_copy_comunicazione/checklist-risposta-diretta.md`
5. `merenda/08_brand/brand-community-e-fan.md`
6. `merenda/08_brand/testimonianze-e-prova-sociale.md`

Tutti sono collegati dai rispettivi README già nel branch semantico.

## A/B/C — verifica empirica del batch 226–250

Classificazione pre-esistente del checkpoint 225:

- **A:** 10 contenuti → **8/10 incrementali = 80%**
- **B:** 9 contenuti → **7/9 incrementali = 78%**
- **C:** 6 contenuti → **1/6 incrementale = 17%**

Il singolo C incrementale è **229**, short pubblicato il 16 dicembre 2025, successivo a materiale già canonico sul front-end.

Conferme:

1. C resta **FAST REVIEW, mai SKIP**.
2. La regola manuale di promozione per recenza introdotta al checkpoint 225 è giustificata dal caso 229.
3. A ha alto yield nel batch, ma B è quasi equivalente: la distinzione A/B merita verifica in FASE 15 prima di qualsiasi modifica della logica.
4. Il campione non giustifica da solo modifiche ai file frozen.

## Verifica branch semantico

Confronto HEAD tecnica `c579de5e5...` → HEAD semantica pre-handoff:

- **25 commit avanti**
- **0 indietro**
- **25 review .review.md aggiunte**
- catalog/index/queue aggiornati soltanto per 226–250
- nessun contenuto 251+ modificato semanticamente
- nessun file frozen modificato
- nessun nuovo ESCLUSO

Contatori verificati direttamente su `sources/catalog.json`:

- STUDIATO **244**
- ESCLUSO **6**
- DA STUDIARE **218**
- totale **468**

## Validazione e limiti prima di Claude

La fase tecnica aveva validato **841 warning identici** prima/dopo acquisizione.

Il connettore GitHub usato da ChatGPT non può eseguire `python3 scripts/validate_project.py` sul working tree remoto. Per questo **non viene dichiarato un validator post-semantico ineseguito**.

Prima della FASE 14/15 Claude deve:

1. eseguire il validator e registrare la baseline reale;
2. eseguire `git diff --check`;
3. verificare link interni/orfani sull'intera KB;
4. verificare assenza di contaminazione Formalife;
5. verificare frozen;
6. confrontare warning prima/dopo refactor/audit.

La verifica remota di ChatGPT conferma comunque:

- 25 commit semantici esatti;
- 25 review;
- nessun frozen nel diff;
- nessun asset/review 251+ nel diff;
- solo KB, README e indici attesi modificati.

## Focus obbligatori per FASE 14 al checkpoint 250

Claude deve rileggere l'intera KB e controllare in particolare:

1. **06_vendita**, ora cresciuta molto: confine fra `prequalifica-follow-up-decisori.md`, `follow-up-lead-non-convertiti.md` e `preventivo-consulenza-diagnosi.md`; verificare se la sezione necessita ulteriore split o se i tre nodi sono già sufficientemente distinti.
2. **08_brand**: confine fra `autorita-e-marketing.md`, `testimonianze-e-prova-sociale.md` e `brand-community-e-fan.md`.
3. **07_copy_comunicazione**: rapporto fra `checklist-risposta-diretta.md` e `priorita-azione-e-inerzia.md`.
4. **04_marketing**: evento proprietario vs riattivazione/referral; evitare duplicazioni.
5. **03_offerta**: integrare correttamente la definizione economica 2025 del front-end con le fonti 2025 già presenti.
6. **RFM**: confermare un solo nodo canonico in `appropriatezza-clienti.md` e solo rinvii applicativi altrove.
7. **prevalenza temporale**: confermare che il 249 non reintroduca scarsità artificiale contro la formulazione 2025 più recente.

## Focus obbligatori per FASE 15 al checkpoint 250

Audit tassonomico completo, con particolare attenzione a:

- crescita di `06_vendita`;
- espansione reale di `07_copy_comunicazione` e `08_brand`;
- categoria finale molto diversa dalla categoria preliminare della coda;
- yield A/B quasi identico nel batch;
- C ancora basso ma non nullo per effetto della recenza;
- valutare se il classifier v1.1 necessita modifiche oppure se i dati sono ancora insufficienti;
- verificare eventuali file troppo grandi, categorie troppo larghe, overlap o nodi da rinominare/spostare;
- nessun cambiamento tassonomico puramente cosmetico.

## Handoff

- Corpus completo: **NO**
- Agente richiesto: **CLAUDE CODE**
- Checkpoint richiesto: **250**
- Fasi dovute: **FASE 14 + FASE 15**
- Nessuna elaborazione 251+ prima della conclusione del checkpoint.
- Dopo Claude, il prossimo agente previsto è **CODEX** per l'acquisizione tecnica 251–275, salvo diversa decisione esplicita risultante dall'audit.
