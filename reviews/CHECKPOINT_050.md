# Checkpoint 050 — esito fase 14 + fase 15 (Claude Code)

## Stato all'ingresso del checkpoint

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

## Esito FASE 14 — Refactor KB

Letta integralmente la KB (11 README + 19 documenti, INDEX.md, ~2.400 righe) e verificati con script i link/anchor interni, l'assenza di file orfani e la copertura di `merenda/INDEX.md`.

Risultato: la KB risultava già in buono stato dal lavoro di ingestione precedente (regola MERGE, NON APPEND applicata correttamente con cross-link invece di duplicazione). Nessuna riscrittura di contenuto sostanziale è stata necessaria. Verifiche puntuali sui punti richiesti:

- **Link interni e anchor**: 0 link rotti, 0 anchor mancanti su tutti i file `merenda/**/*.md` (verifica scriptata).
- **File orfani/routing**: ogni documento è linkato dal README della propria sezione; ogni README è linkato da `merenda/INDEX.md`.
- **Duplicazioni tra i principi ricorrenti** (quattro filtri del focus, family brand, sell-in/sell-through, cavallo di battaglia, folla affamata, "più che gratis", "srotolare il posizionamento", "replicare la povertà"): ciascun concetto ha un'unica spiegazione estesa in un solo file, richiamata altrove solo con link — nessuna duplicazione da correggere.
- **Sovrapposizione `00_fondamenti`/`04_marketing`**: nessuna sovrapposizione reale; `00_fondamenti` resta il corso sui 7 principi, `04_marketing` contiene solo i due documenti tematici propri (complessità/riduzione variabili, quattro modalità/ritmo) più i rimandi incrociati previsti.
- **Confine `01_mercato`/`02_posizionamento`**: le "quattro domande" (mercato) e i "quattro filtri del focus" (posizionamento) restano framework distinti, già disambiguati nel testo e collegati con anchor reciproci.
- **Confine `03_offerta`/`05_acquisizione`/`06_vendita`**: confine coerente (struttura/prezzo dell'offerta vs. contatto/traffico/referral vs. trattativa), ma `05_acquisizione` resta la sezione più scarna (un solo documento nativo) perché pochi video finora processati vi appartengono in modo specifico; aggiunta una riga di chiarimento del confine nel suo README.
- **Dimensione dei file**: nessun file eccessivo. I più cresciuti restano `prezzo-premium-e-percezione-del-valore.md` (350 righe) e `offerta-a-risposta-diretta.md` (290 righe) — da tenere d'occhio ai prossimi checkpoint se continuano a crescere, ma non richiedono split ora.
- **Separazione principi/esempi**: già rispettata (`differenziazione-operativa.md` vs `esempi-di-differenziazione.md`, con richiamo reciproco).

Correzioni minime applicate:

1. `merenda/07_copy_comunicazione/README.md` — rimosso il placeholder "sezione inizialmente vuota", non più coerente con il contenuto già presente (principio su copywriting e price gap).
2. `merenda/05_acquisizione/README.md` — aggiunta una frase di confine rispetto a `03_offerta` e `06_vendita`, data la scarsità di contenuto nativo della sezione.

Nessun contenuto sostanziale modificato o rimosso. Nessun file congelato toccato. Nessuna conoscenza nuova introdotta. Formalife non è comparsa nella KB.

## Esito FASE 15 — Audit globale della tassonomia

Domanda guida: alla luce di 46 video studiati, la KB verrebbe ancora organizzata nello stesso modo?

**Conclusione: sì.** Le 11 categorie restano adeguate al corpus attuale (46/468). Nessuna fusione, separazione o ridenominazione di sezione è risultata necessaria a questo stadio.

### Classificazione preliminare dei contenuti non ancora studiati

Il problema reale individuato riguardava `sources/VIDEO_INDEX.md` e `sources/queue/QUEUE.md`: un blocco di ~103 video non ancora studiati era classificato genericamente come `04_marketing`, mentre molti titoli indicavano con ragionevole sicurezza una categoria più specifica già esistente in tassonomia.

Applicata una riclassificazione conservativa, riproducibile (regole per parole chiave IT/EN sui titoli + una lista esplicita di override per case study aziendali riconoscibili — es. Mortadella Shop, Coca-Cola, Tesla, Nutella, Barilla, Dyson, Ducati, Chiara Ferragni/Balocco), applicata **solo** ai contenuti `DA STUDIARE`:

- 40 video su 418 non ancora studiati sono stati spostati dal bucket generico (o da una categoria palesemente errata) a una categoria più precisa:
  - `10_casi_studio`: +24 (case study aziendali riconoscibili nel titolo)
  - `09_business`: +10 (assunzioni, mentalità imprenditoriale, truffe/investimenti, CRM)
  - `01_mercato`: +3 (segmento clienti alto-spendenti)
  - `07_copy_comunicazione`: +1 (call to action)
  - `05_acquisizione`: +1 (email marketing come canale)
  - `03_offerta`: +1 (garanzia)
- I restanti ~110 video il cui titolo non permette una classificazione più precisa senza vedere il contenuto sono rimasti in `04_marketing`: per regola RULES §5 si corregge solo quando ragionevolmente sicuri; la conferma definitiva avviene alla fase 8+ in ingestione.

### Riordino della queue (solo contenuti non ancora studiati)

I 418 video `DA STUDIARE` (ordine 51–468) sono stati riordinati secondo la sequenza macro già dichiarata in `QUEUE.md` (mercato → posizionamento → offerta → marketing → acquisizione → vendita → comunicazione → brand → business → casi studio), con gli Shorts posposti ai video lunghi **all'interno di ciascuna categoria** (prima erano sparsi fuori sequenza, es. dopo i blocchi `09_business`/`10_casi_studio`).

I 50 video già `STUDIATO`/`ESCLUSO` (ordine 1–50) **non sono stati toccati**: stesso ordine, stessa categoria, stesso stato.

Verifiche di integrità eseguite:

- stessi 468 ID video presenti prima e dopo, nessuna perdita/duplicazione;
- `Ordine` sequenziale 1–468 in entrambi i file;
- `sources/queue/QUEUE.md` e `sources/VIDEO_INDEX.md` perfettamente sincronizzati (stesso ordine, stessa categoria per ogni ID).

`sources/queue/next-batch.txt` **non è stato modificato**: come documentato in `scripts/README.md`, registra un batch già acquisito in passato, non è la queue canonica.

### Effetto sul prossimo video

Il primo video non completato non è più `bHxjwGQQoUw` ma **`AAiq6RnCysE`** — *Come comprano i ricchi? [Quelli veri]* (`01_mercato`). Nessun asset tecnico presente su disco per questo video.

`bHxjwGQQoUw` ha già un'acquisizione tecnica parziale (`info.json` + `it-orig.json3` presenti in `sources/transcripts/`) da un batch precedente; ora si trova più avanti nel blocco `04_marketing` riordinato. Questo lavoro parziale non è perso: verrà riutilizzato quando toccherà il suo turno nella queue corretta.

## Regole preservate

- MERGE, NON APPEND.
- Formalife resta completamente fuori dalla KB.
- Materiale più recente prevale in caso di contraddizione (nessuna nuova contraddizione emersa in questo checkpoint).
- Nessuna nuova burocrazia, claim database o schema complesso introdotto.
- File congelati non toccati.
- Nessuna conoscenza nuova introdotta nella KB: le uniche modifiche a `merenda/` sono le due correzioni di routing/testo elencate sopra.

## Dopo Claude

Il prossimo contenuto non processato è:

`AAiq6RnCysE` — *Come comprano i ricchi? [Quelli veri]* (`01_mercato`).

Asset tecnici: **NON PRESENTI**.

`Agente richiesto: CODEX` per l'acquisizione del prossimo batch tecnico (proposto: ordine 51–75 della queue corretta), poi ritorno a ChatGPT per le fasi 8–13.

Prossimo checkpoint Claude: dopo il video 75 (fase 14).
