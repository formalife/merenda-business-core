# Checkpoint 050 — handoff a Claude Code

## Stato

Primi 50 contenuti della queue processati:

- 46 `STUDIATO`
- 4 `ESCLUSO` dalla dottrina attiva
- 418 ancora da processare
- corpus completo: NO

Contenuti esclusi:

- `Wk1Se1AeInw` — lezione di Jay Abraham senza intervento sostanziale di Frank;
- `5gKmC-QQlhA` — lezione di Laura Ries;
- `r8wi8vzz61w` — lezione di Al Ries;
- `TXGgnHLVhvA` — lezione di Dan Kennedy.

Il batch tecnico 26–50 è stato completamente risolto. Il transcript Ferrero `GsmDyZQeYUM`, inizialmente fallito in conversione, è stato recuperato dal JSON3 italiano. Nessun blocco semantico aperto.

## Obiettivo del checkpoint

Eseguire, in quest'ordine:

1. **FASE 14 — Refactor KB**
2. **FASE 15 — Audit globale della tassonomia**

Non introdurre nuova conoscenza e non modificare file congelati.

## Cambiamenti principali del batch 26–50

### Posizionamento e architettura brand

Sono stati consolidati:

- estensioni di linea e architettura del brand;
- spin-off e brand separati;
- sell-in vs domanda reale del cliente finale;
- gestione economica della rifocalizzazione;
- commodity differenziate attraverso target/problema/servizio;
- fase di decollo vs fase in quota;
- quattro filtri del focus: domanda, differenza reale, marginalità, scalabilità.

Contraddizione importante già risolta con la regola “il materiale più recente prevale”:

- nel 2016 Frank usava il concetto di *family brand*;
- il 15 gennaio 2024 lo rifiuta esplicitamente come guida operativa;
- la KB attiva mantiene la formulazione 2024 e tratta quella 2016 come superseded.

File principali cresciuti:

- `merenda/02_posizionamento/differenziazione-operativa.md`
- `merenda/02_posizionamento/estensioni-di-linea-e-architettura-brand.md`
- `merenda/02_posizionamento/esempi-di-differenziazione.md`

### Offerta e pricing

Creato e sviluppato:

- `merenda/03_offerta/offerta-a-risposta-diretta.md`

Aggiornati in profondità:

- `merenda/03_offerta/prezzo-premium-e-percezione-del-valore.md`
- `merenda/03_offerta/front-end-e-back-end.md`

Concetti consolidati:

- offerta come richiesta di risposta misurabile;
- “più che gratis”;
- esca/front-end distinta dalla monetizzazione backend;
- garanzia come trasferimento del rischio;
- diagnosi dell'offerta dai risultati del funnel;
- upsell, cross-sell e recupero del quasi-acquisto;
- prezzo testato per cluster;
- sweet spot prezzo/margine/clienti;
- ammiraglia e offerta VIP;
- pricing situazionale;
- pre-motivazione del price gap;
- evitare l'auto-sconto del venditore.

Le formulazioni assolute più vecchie sul prezzo sono già subordinate al materiale 2024–2025, che richiede target corretto, capacità di spesa, differenziazione e test economici.

### Mercato, vendita e numeri

Creato:

- `merenda/01_mercato/quattro-domande-prima-di-lanciare.md`

La checklist distingue:

1. domanda/problema reale;
2. raggiungibilità del target;
3. capacità di acquisto;
4. trend del mercato.

È volutamente distinta dai quattro filtri del focus di posizionamento.

Aggiornati anche:

- `merenda/06_vendita/prequalifica-follow-up-decisori.md`
- `merenda/09_business/numeri-cassa-e-crescita.md`
- `merenda/00_fondamenti/marketing-first.md`

## Punti da controllare nella fase 14

Controllare soprattutto:

- sovrapposizioni tra `00_fondamenti` e `04_marketing`;
- confine tra `01_mercato` e `02_posizionamento`;
- confine tra `03_offerta`, `05_acquisizione` e `06_vendita`;
- duplicazioni tra i numerosi principi su focus, pricing e front-end;
- dimensione dei file maggiormente cresciuti;
- routing dei README e di `merenda/INDEX.md`;
- link interni e anchor;
- separazione tra principi ed esempi/casi.

Preservare il contenuto sostanziale: refactor significa migliorare gerarchia, routing e consumo token, non riscrivere liberamente la dottrina.

## Punti da controllare nella fase 15

La tassonomia iniziale era volutamente provvisoria.

Dopo 50 contenuti, verificare se:

- le categorie attuali restano adeguate;
- i confini tra sezioni devono cambiare;
- alcuni file meritano spostamento/ridenominazione;
- la queue futura deve essere riordinata per aumentare qualità e coerenza del learning path;
- la classificazione preliminare molto ampia `04_marketing` dei video successivi va raffinata.

Claude può riordinare **solo i contenuti non ancora processati**.

## Regole da preservare

- MERGE, NON APPEND.
- Formalife resta completamente fuori dalla KB.
- Materiale più recente prevale in caso di contraddizione reale.
- Guest content non viene attribuito a Frank.
- Nessuna nuova burocrazia, claim database o schema complesso.
- `sources/transcripts/` resta archivio; `merenda/` resta il prodotto vivo.
- Ottimizzare routing e consumo token.
- Non modificare file congelati.

## Dopo Claude

Il prossimo contenuto non processato è:

`bHxjwGQQoUw` — *Can an SME WIN ON THE MARKET and beat the giants in its sector?*

Gli asset tecnici del video 51 **non sono presenti** nel repository.

Dopo fase 14 + fase 15, se il corpus resta incompleto, impostare:

`Agente richiesto: CODEX`

e richiedere l'acquisizione tecnica del prossimo batch, idealmente video 51–75, quindi restituire il controllo a ChatGPT per le fasi 8–13.
