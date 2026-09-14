# Checkpoint 150 — handoff a Claude Code

## Stato

Primi 150 contenuti della queue processati semanticamente:

- 144 `STUDIATO`
- 6 `ESCLUSO` dalla dottrina attiva
- 318 ancora da processare
- corpus completo: NO

Questo checkpoint richiede, in ordine:

1. **FASE 14 — Refactor KB**
2. **FASE 15 — Audit globale della tassonomia**

Non introdurre nuova conoscenza. Non introdurre Formalife.

**BLOCCO OPERATIVO:** non acquisire i contenuti 151–175 prima della conclusione della FASE 15.

## Stato Git verificato prima del handoff

Al termine dell'elaborazione semantica del contenuto 150:

- `main` e `semantic-143-150` puntavano entrambi a `097592fcdabd14e207d4e61636d5e6daa2640aaf`;
- il batch 126–150 risultava quindi già integrato in `main`;
- i tre ultimi contenuti sono stati chiusi con commit distinti:
  - 148 `joY6sigynis` → `55a9803d04771a9a4032fa73d26ec87f60cc8bf5`;
  - 149 `ijVoIMF_gn8` → `76019d392b9cf883195d2d612bd31d8689185ad9`;
  - 150 `VN1d2qBc0U0` → `097592fcdabd14e207d4e61636d5e6daa2640aaf`.

Nessuno dei tre commit ha modificato file congelati.

## Evoluzione del batch 126–150

Il batch ha soprattutto consolidato e collegato principi già emersi, aggiungendo pochi incrementi specifici invece di creare documenti per video.

### Relazione cliente, acquisizione e information marketing

Sono stati consolidati:

- stati diversi della relazione cliente/prospect e conseguenze sul lavoro necessario per convertire;
- pacchetto informativo come pre-educazione e filtro, non come formato obbligatorio;
- profondità del funnel calibrata su urgenza, complessità e bisogno di informazione;
- separazione fra canale di scoperta e ambiente della persuasione lunga;
- valore dato prima della trattativa senza trasformare il pre-marketing in consulenza gratuita;
- priorità alla domanda già posseduta o già creata prima di aumentare l'acquisizione;
- misurazione delle varianti in base alla risposta, non al gusto personale.

Il contenuto 148 ha aggiunto in particolare:

- ruoli differenti degli asset informativi lungo il ciclo cliente: acquisizione, referral, riattivazione, filtro/prequalifica;
- necessità di follow-up dopo l'invio del materiale;
- materiali differenziati per stakeholder diversi nelle vendite B2B multi-decisore.

L'integrazione principale è in:

- `merenda/05_acquisizione/information-marketing.md`
- `merenda/06_vendita/prequalifica-follow-up-decisori.md`

### Marketing a risposta diretta e funzione distributiva

Il contenuto 149 ha confermato molti principi già presenti senza creare un secondo decalogo duplicato.

L'incremento mantenuto è che, per una PMI, il direct response svolge anche una funzione distributiva/commerciale: porta la proposta al cliente, chiede un passo misurabile e anticipa parte del lavoro del venditore.

Integrazione principale:

- `merenda/00_fondamenti/marketing-first.md`

### Canali intermediati: sell-in e sell-through

Il contenuto 150 ha aggiunto la distinzione fra:

- **sell-in** verso il partner commerciale;
- **sell-through** verso il cliente finale.

Il principio consolidato è che il produttore non deve limitarsi a conquistare il canale: deve anche sostenere la domanda a valle affinché il prodotto ruoti e generi riordino.

Integrazione principale:

- `merenda/04_marketing/gerarchia-domanda-e-canali.md`

### Posizionamento, brand, autorità e organizzazione

Nel batch sono stati inoltre consolidati:

- specializzazione non equivalente automaticamente a posizionamento;
- creatività subordinata al posizionamento;
- differenziazione importabile da altri settori quando coerente col mercato;
- distinzione fra autorità, credibilità e fiducia;
- autorità basata su esperienza dimostrabile;
- separazione fra azienda e brand focalizzati quando l'espansione richiede promesse/mercati distinti;
- distinzione fra capacità commerciale, qualità dei lead e close rate.

## Punti da controllare in FASE 14

Eseguire audit/refactor globale dell'intera `merenda/`, non soltanto dei file modificati nel batch.

Controllare soprattutto:

1. **Information marketing / acquisizione / vendita**
   - sovrapposizioni fra `information-marketing.md`, `riattivazione-clienti.md`, `referral-e-soddisfazione.md`, `prequalifica-follow-up-decisori.md` e `gerarchia-domanda-e-canali.md`;
   - evitare che acquisizione, referral, riattivazione e filtro finiscano duplicati in più punti;
   - verificare che i materiali multi-decisore restino nel routing corretto.

2. **Direct response**
   - confine fra `marketing-first.md`, `offerta-a-risposta-diretta.md`, documenti di copy e documenti sui canali;
   - mantenere distinta la struttura del direct response dal tono e dal singolo mezzo.

3. **Posizionamento / architettura brand / espansione**
   - confine fra `differenziazione-operativa.md`, `estensioni-di-linea-e-architettura-brand.md` e `espansione-nicchie-e-multibrand.md`;
   - verificare che azienda, brand focalizzati e casi applicativi non vengano confusi.

4. **Autorità, credibilità e fiducia**
   - verificare eventuali ripetizioni fra `autorita-e-marketing.md`, information marketing e prequalifica.

5. **Canali**
   - verificare che sell-in/sell-through, gerarchia della domanda e complementarità dei mezzi restino concetti distinti ma collegati.

6. **Token footprint e file lunghi**
   - `merenda/03_offerta/offerta-a-risposta-diretta.md` ~368 righe;
   - `merenda/03_offerta/prezzo-premium-e-percezione-del-valore.md` ~372 righe;
   - `merenda/08_brand/autorita-e-marketing.md` ~348 righe;
   - `merenda/05_acquisizione/information-marketing.md` ~318 righe.

Valutare split soltanto se emerge un confine concettuale netto. Non frammentare per ridurre artificialmente la lunghezza.

Controllare inoltre INDEX, README, link relativi, anchor e file orfani.

## Punti da controllare in FASE 15

Rivalutare la tassonomia globale alla luce dei primi 150 contenuti.

Verificare:

- se le 11 categorie restano adeguate;
- se il learning path 151–468 è ancora corretto;
- se titoli generici ancora classificati `04_marketing` possono ora essere instradati meglio senza inferire dottrina non acquisita;
- se casi applicativi devono essere spostati più spesso in `10_casi_studio`;
- se i contenuti brevi/Shorts devono restare deprioritizzati rispetto ai long-form;
- se queue, catalogo e VIDEO_INDEX devono essere riallineati dove persistono disallineamenti d'ordine già noti;
- quale deve essere il vero batch tecnico successivo al checkpoint.

Claude può riordinare solo i contenuti non ancora processati. Gli stati dei primi 150 restano definitivi, salvo correzioni strutturali motivate di categoria/routing.

## Verifiche finali già eseguite

Prima di preparare questo checkpoint è stato verificato che:

- `sources/catalog.json` contiene 468 elementi;
- contatori: 144 `STUDIATO`, 6 `ESCLUSO`, 318 `DA STUDIARE`;
- le prime 150 posizioni della queue sono tutte chiuse: 144 `STUDIATO` + 6 `ESCLUSO`;
- posizione 151 pre-audit: `8R8NR6nqhJY` — *"I Already Tried It and It Didn't Work" — The Excuse That Kills Your Revenue*;
- le posizioni 151–175 sono 25 contenuti `DA STUDIARE`;
- nel tree corrente non esiste alcun asset sotto `sources/transcripts/` per i 25 contenuti 151–175;
- tutti i 40 file Markdown sotto `merenda/` sono stati controllati per la stringa `Formalife`: 0 occorrenze;
- i tre commit 148–150 non hanno modificato file congelati;
- il blocco ASR dei contenuti 143/148/149 è risolto tramite fallback locale già presente nel repository.

Le anomalie note di `scripts/validate_project.py` restano quelle preesistenti già documentate: confronto file congelati vs tag v1.0 e disallineamenti d'ordine fra catalogo, VIDEO_INDEX e queue. Non trattarle come regressioni nuove senza verificarne l'origine.

## Regole da preservare

- MERGE, NON APPEND.
- Fonte dottrinale ammessa: solo canale ufficiale `@FrankMerendaTV`.
- Materiale più recente prevale quando esiste incompatibilità reale.
- Guest content non viene attribuito automaticamente a Frank.
- Transcript = archivio; `merenda/` = prodotto vivo.
- Nessun file congelato va modificato.
- Formalife resta completamente fuori dalla KB Merenda fino alla fase 21.
- Nessuna acquisizione 151–175 prima della conclusione della FASE 15.

## Dopo Claude

Al termine della FASE 14 + FASE 15:

1. aggiornare questo checkpoint con l'esito;
2. aggiornare `STATUS.md`;
3. determinare il primo contenuto e il batch successivo usando la queue **post-audit**;
4. se gli asset del nuovo primo contenuto non esistono, richiedere CODEX per la sola acquisizione tecnica del batch deciso;
5. se gli asset esistono già, restituire il controllo a CHATGPT.

Non avviare acquisizione durante il checkpoint.
