# Checkpoint 075 — handoff a Claude Code

## Stato

Primi 75 contenuti della queue processati:

- 71 `STUDIATO`
- 4 `ESCLUSO` dalla dottrina attiva
- 393 ancora da processare
- corpus completo: NO

Questo checkpoint richiede **soltanto FASE 14 — refactor KB**.  
La fase 15 non è dovuta: il prossimo audit globale della tassonomia resta al contenuto 100.

## Cambiamenti principali del batch 51–75

### 01_mercato — clienti alto-spendenti

Creato:

- `merenda/01_mercato/clienti-altospendenti.md`

Principi consolidati:

- “alto-spendente” è relativo al business, non una soglia patrimoniale assoluta;
- referenza diretta / entourage;
- emulazione dei pari;
- anticipazione/status;
- necessità di avere realmente livelli premium/VIP da acquistare;
- accesso, servizio, comodità ed esperienza superiore prima dello sconto;
- verifica del bacino locale prima di aprire una sede di nicchia.

### 09_business — patrimonializzazione

Creato:

- `merenda/09_business/patrimonializzazione-e-reinvestimento.md`

Il video `AG7Gi9sPBRs`, inizialmente classificato in mercato, è stato riclassificato in business.

Sono stati consolidati soltanto gli insegnamenti aziendali:

- reinvestire in marketing, vendita, persone, R&D, sistemi e capacità;
- non estrarre troppo presto risorse per consumo personale;
- aumentare il valore/capacità dell'impresa;
- ridurre progressivamente la dipendenza dal lavoro operativo del fondatore;
- diversificare il rischio dopo aver costruito il core.

Le percentuali di asset allocation personale NON sono state consolidate perché Frank dichiara esplicitamente nel video di non essere un esperto finanziario.

### 02_posizionamento — materiale recente e Shorts

Il blocco 56–73 conteneva molti Shorts/conferme.

Per rispettare MERGE, NON APPEND, 18 contenuti hanno prodotto soltanto tre aggiornamenti canonici sostanziali:

1. **focus “sole vs raggio laser”** — materiale del 25 febbraio 2026:
   una PMI non batte il gigante copiandone l'ampiezza; concentra risorse su un campo più stretto;

2. **richiesta sistematica di sconto come segnale diagnostico** — 9 dicembre 2025:
   distinta dalla scontistica progettata dall'azienda; indica possibile commodity/comparabilità;

3. **estensione di linea non è un interruttore acceso/spento** — 6 febbraio 2024:
   può indebolire la posizione senza far fallire automaticamente un'impresa forte; se il core perde identità, rifocalizzare.

Gli altri Shorts/casi sono stati registrati nelle rispettive review come conferme o esempi senza duplicare la KB.

Il video `D3Mz_7WOuvU` è stato riclassificato in `10_casi_studio` perché è una testimonianza/caso applicativo.

### 08_brand — recensioni come vantaggio relativo

Il video `ldXZUf-mKSU` del 12 maggio 2026 è stato riclassificato da offerta a brand.

Aggiornato `merenda/08_brand/autorita-e-marketing.md`:

- confrontare la propria prova sociale con quella del competitor;
- costruire una superiorità visibile di recensioni/testimonianze;
- il riferimento “10x” è trattato come obiettivo aggressivo, non soglia scientifica;
- riutilizzare le prove in preventivi, cataloghi e materiali prima del prezzo.

### 03_offerta — offerta contro il leader

Aggiornato `merenda/03_offerta/offerta-a-risposta-diretta.md` con il materiale del 5 maggio 2026:

- il leader parte con un vantaggio di sicurezza percepita;
- il piccolo può compensare con un bundle realmente più vantaggioso;
- l'offerta può costare di più se riduce abbastanza rischio/attrito e aumenta valore utile;
- percezione e numeri devono essere entrambi corretti;
- offerte largamente standardizzate dall'azienda, con adattamento controllato da parte del venditore.

## Punti da controllare nella fase 14

Controllare soprattutto:

- se i due nuovi documenti (`clienti-altospendenti.md`, `patrimonializzazione-e-reinvestimento.md`) sono ben collegati e nel posto giusto;
- eventuale sovrapposizione tra clienti alto-spendenti e pricing premium;
- eventuale sovrapposizione tra patrimonializzazione e `numeri-cassa-e-crescita.md`;
- crescita di `prezzo-premium-e-percezione-del-valore.md`, `autorita-e-marketing.md` e `offerta-a-risposta-diretta.md`;
- routing README / INDEX;
- link e anchor interni;
- eventuali esempi che possono essere spostati senza alterare il contenuto sostanziale.

Non introdurre nuova dottrina.

## Regole da preservare

- MERGE, NON APPEND.
- Formalife resta fuori.
- Materiale più recente prevale.
- Guest content non viene attribuito a Frank.
- Non trasformare ogni Short in una pagina autonoma.
- `sources/transcripts/` resta archivio; `merenda/` resta prodotto vivo.
- Nessuna modifica ai file congelati.
- Nessuna fase 15 a questo checkpoint.

## Dopo Claude

Primo contenuto pendente:

`h-ngxN8kYPc` — *Why Customers Don't Buy From You (It's Not the Price's Fault)* — `03_offerta`.

Gli asset tecnici dei video 76–79 non risultano ancora presenti su `main`.

Alcuni contenuti più avanti nella queue hanno già asset acquisiti durante il precedente batch parallelo; il nuovo `scripts/ingest_video.py` segue comunque la queue canonica e riutilizza gli asset esistenti.

Dopo il refactor:
- se gli asset 76–100 non sono ancora stati acquisiti, richiedere CODEX/script locale;
- se sono già presenti, restituire direttamente il controllo a CHATGPT.

## Esito FASE 14 (eseguita da Claude Code)

Verifica completata su tutta la KB (`merenda/`, 32 file). Nessuna nuova dottrina introdotta, nessun file congelato modificato.

Controlli eseguiti:

- **Duplicazioni/sovrapposizioni segnalate nel checkpoint**: `clienti-altospendenti.md` vs `prezzo-premium-e-percezione-del-valore.md` e `patrimonializzazione-e-reinvestimento.md` vs `numeri-cassa-e-crescita.md` — verificate: contenuto complementare, correttamente collegato tramite `## Collegamenti`, nessuna duplicazione da correggere.
- **Dimensione file**: nessun file supera dimensioni ingestibili; `offerta-a-risposta-diretta.md` (343 righe) e `prezzo-premium-e-percezione-del-valore.md` (371 righe) sono i più grandi e in crescita, ma restano organizzati per sotto-sezioni tematiche coerenti. Da tenere sotto osservazione nei prossimi checkpoint, senza splitting forzato ora.
- **Routing/INDEX/README**: `merenda/INDEX.md` e tutti gli 11 README di sezione risultano coerenti con i file effettivamente presenti.
- **Link interni e anchor**: verifica programmatica su tutti i 32 file — 0 link rotti, 0 anchor non risolvibili.
- **Struttura interna**: trovati e corretti 2 file in cui la sezione `## Collegamenti` non era in coda al documento (contenuto aggiunto in batch successivi dopo la sezione collegamenti anziché prima):
  - `merenda/08_brand/autorita-e-marketing.md` — spostata `## Collegamenti` in fondo al file, dopo `## Come il cliente costruisce una decisione` e `## Brand e passaparola si rafforzano`. Nessun contenuto modificato o rimosso, solo riordino.
  - `merenda/10_casi_studio/motoargento-focalizzazione.md` — stesso tipo di correzione, spostata `## Collegamenti` dopo `## Rivenditore e vincoli del fornitore`.

Nessun'altra frammentazione, ridenominazione di sezione o spostamento file è risultata necessaria a questo checkpoint.

Fase 15 NON eseguita, come richiesto.
