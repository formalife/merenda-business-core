# Checkpoint 125 — handoff a Claude Code

## Stato

Primi 125 contenuti della queue processati semanticamente:

- 121 `STUDIATO`
- 4 `ESCLUSO` dalla dottrina attiva
- 343 ancora da processare
- corpus completo: NO

Questo checkpoint richiede **soltanto FASE 14 — refactor KB**.  
La fase 15 non è dovuta: il prossimo audit globale della tassonomia resta al contenuto 150.

## Evoluzione del batch 101–125

Il batch ha consolidato soprattutto marketing operativo, progettazione dell'offerta e rapporto fra marketing e numeri aziendali, senza creare una pagina per ogni contenuto.

### Domanda, canali e comunicazione

Sono stati consolidati o precisati:

- relazione fra posizionamento, domanda e pre-educazione;
- ricerca delle lamentele e delle frizioni reali del mercato;
- trigger concreti che rendono un bisogno prioritario;
- timing della domanda e finestre in cui aumentare intensità/messaggio;
- complementarità fra canali online/offline invece della scelta astratta “uno contro l'altro”;
- livelli di consapevolezza e domanda di ricerca;
- costruzione della comunicazione a partire dall'azione finale desiderata;
- necessità di guadagnare attenzione nei contesti one-to-many.

### Offerta, acquisizione e continuità

Sono stati consolidati:

- velocità di risposta ai lead come processo operativo;
- promesse misurabili e verificabili;
- lancio iniziale come ciclo di feedback e costruzione di prova;
- quattro gate di prequalificazione;
- front-end come degustazione del portafoglio;
- seconda vendita come soglia da progettare;
- continuità naturale del bisogno e meccanismi che aiutano il cliente a tornare;
- prima transazione come ingresso in un “marketing di secondo livello”, nel quale esperienza, servizio e back-end devono trasformare la vendita in relazione.

### Casi applicativi

I contenuti su funnel dentistico, espansione dello studio dentistico e lancio ristorante sono stati trattati come casi/applicazioni, senza trasformare automaticamente dettagli settoriali in regole universali.

### Business — cassa, cash flow e capacità di finanziare il marketing

I due contenuti sulla gestione in crisi e la lunga lezione sul lancio hanno ampliato `merenda/09_business/numeri-cassa-e-crescita.md`.

Principi consolidati:

- distinguere cassa reale, crediti e promesse di pagamento;
- riserve di cassa come capacità di sopravvivenza e cash flow come stabilità;
- controllo del burn rate;
- scenari prudenziali e rendiconto finanziario previsionale su base settimanale, con monitoraggio ravvicinato in forte incertezza;
- cash flow operativo come risorsa da leggere prima di decidere quanto investire in marketing;
- riduzione dei tempi di incasso;
- gestione dell'inventario come trade-off fra costo unitario e liquidità immobilizzata;
- negoziazione dei tempi di pagamento ai fornitori senza distruggere relazioni strategiche;
- uso delle risorse liberate da costi/ciclo di cassa per finanziare test marketing sostenibili;
- crescita economica non equivalente a crescita dimensionale.

Le affermazioni sanitarie, le previsioni contingenti sulla crisi COVID e i dettagli datati non necessari al framework non sono stati consolidati.

### Mercato — rendere operativa l'appropriatezza del cliente

Aggiornato `merenda/01_mercato/appropriatezza-clienti.md` con il materiale 2022, subordinato al modello più recente del 2025.

Aggiunti:

- criteri minimi di accettazione dell'ordine/cliente;
- possibilità per controllo finanziario/operativo di fermare vendite economicamente distruttive;
- necessità di sostituire domanda inappropriata con domanda migliore tramite marketing;
- principio che spendere acquisizione per clienti in perdita amplifica il danno.

Le generalizzazioni del 2022 su fasce di reddito non sono diventate regole universali: prevalgono margine, LTV, costi reali e dati.

## Documenti da controllare nella FASE 14

Controllare soprattutto:

- crescita di `merenda/09_business/numeri-cassa-e-crescita.md` e possibile sovrapposizione con `patrimonializzazione-e-reinvestimento.md` e `scalabilita-e-operativita.md`;
- crescita di `merenda/03_offerta/front-end-e-back-end.md` dopo i contenuti su degustazione, seconda vendita, continuità e marketing post-prima-vendita;
- confine fra `appropriatezza-clienti.md`, target e clienti alto-spendenti dopo l'aggiunta dei criteri di accettazione;
- eventuale ridondanza fra livelli di consapevolezza, gerarchia della domanda e front-end;
- routing dei casi dentistici/ristorazione e degli esempi settoriali;
- README / INDEX, link e anchor;
- token footprint dei documenti cresciuti nel batch.

Non introdurre nuova dottrina.

## Regole da preservare

- MERGE, NON APPEND.
- Formalife resta fuori.
- Materiale più recente prevale.
- Guest content non viene attribuito a Frank.
- Non trasformare ogni video in una pagina autonoma.
- `sources/transcripts/` resta archivio; `merenda/` resta prodotto vivo.
- Nessuna modifica ai file congelati.
- Nessuna fase 15 a questo checkpoint.

## Dopo Claude

Primo contenuto pendente dopo il checkpoint:

`dwfknCGx8UI` — *MARKETING | Diventare il punto di riferimento per il tuo Settore [Jay Abraham]* — `04_marketing`.

Il transcript tecnico di `dwfknCGx8UI` non risulta presente al momento della preparazione del checkpoint.

Dopo la FASE 14, se gli asset del nuovo batch 126–150 non sono disponibili, richiedere CODEX per l'acquisizione tecnica; altrimenti restituire il controllo a CHATGPT.

## Esito FASE 14

Refactor eseguito da Claude Code. Ambito: intera `merenda/` (35 file di contenuto + 11 README + INDEX, 40 file `.md` in totale).

### Controlli eseguiti

- Lettura integrale di tutti i documenti delle 11 sezioni (`00_fondamenti` → `10_casi_studio`), non solo delle aree segnalate dal checkpoint.
- Controllo programmatico di tutti i link relativi e degli anchor interni su tutta `merenda/` (nessun errore).
- Controllo dei file orfani (nessun file di contenuto non referenziato da un README o da un altro documento).
- Verifica di coerenza fra `merenda/INDEX.md`, i README di sezione e i file realmente presenti.
- Verifica puntuale delle aree A–E indicate dal checkpoint 125 (numeri/cassa/patrimonializzazione/scalabilità; front-end e continuità; appropriatezza clienti; consapevolezza/domanda; routing dei casi applicativi).
- Verifica dell'assenza reale del transcript di `dwfknCGx8UI` e conferma dell'assenza degli asset per l'inizio del batch 126–150.

### Esito per area

- **Business (numeri-cassa-e-crescita, patrimonializzazione-e-reinvestimento, scalabilita-e-operativita):** confini concettuali già netti e non sovrapposti (cassa/incassi/ROI vs reinvestimento patrimoniale vs scalabilità/delega). Cross-link reciproci già presenti. Nessuno split o merge necessario.
- **Offerta (front-end-e-back-end.md):** il documento resta un unico documento coerente (progettazione del profitto → marketing di secondo livello → degustazione del portafoglio → progettazione del secondo acquisto → continuità → esempi/esercizio). Nessuna separazione concettuale abbastanza forte da giustificare uno split.
- **Mercato (appropriatezza-clienti.md, clienti-altospendenti.md, clienti-identificabili-e-target.md):** il materiale 2022 resta correttamente subordinato al modello 2025 (margine, LTV, costi occulti, dati); nessuna generalizzazione su fasce di reddito trasformata in regola universale.
- **Consapevolezza/domanda/front-end:** `gerarchia-domanda-e-canali.md`, `information-marketing.md` e `front-end-e-back-end.md` coprono livelli diversi e complementari (canale/timing → piramide di impegno del prospect → funzione del front-end); i rimandi incrociati esistenti sono sufficienti.
- **Casi applicativi (10_casi_studio):** contengono solo testimonianze/casi con numeri attribuiti ai relatori; la dottrina generale che ne deriva è già consolidata nei documenti di sezione (posizionamento, business), non duplicata nei casi.

### Modifiche effettuate

- `merenda/03_offerta/README.md`: corretto il testo del link a `front-end-e-back-end.md` da "Front-end e back-end" a "Front-end e monetizzazione successiva", per farlo coincidere con il titolo reale del documento (già usato correttamente in tutti gli altri rimandi della KB).

Nessun file creato, eliminato o spostato. Nessun altro contenuto riscritto.

### Aree verificate e lasciate invariate perché complementari

Tutte le aree segnalate dal checkpoint 125 (A–E) sono state controllate e giudicate già ben strutturate: le sovrapposizioni osservate sono complementarità funzionali (fonti diverse che trattano lo stesso argomento da angolazioni diverse, con rimandi reciproci già presenti), non duplicazioni da consolidare.

### Punti da monitorare ai prossimi checkpoint

- `merenda/03_offerta/offerta-a-risposta-diretta.md` (367 righe) e `merenda/03_offerta/prezzo-premium-e-percezione-del-valore.md` (371 righe) restano i documenti più lunghi della KB; oggi ogni sezione è ancorata a una fonte specifica e resta leggibile, ma se il batch 126–150 aggiunge ulteriore materiale su offerta/prezzo vale la pena rivalutare se emerge un confine concettuale più netto (es. offerta vs pricing vs obiezioni) da separare.
- Continuare a verificare che il materiale su casi applicativi (dentistico, ristorazione, ecc.) resti confinato a `10_casi_studio` quando arriva nuovo contenuto settoriale nel batch 126–150.

### Conferme

- Nessuna nuova dottrina introdotta: nessun contenuto esterno al canale `@FrankMerendaTV` è stato aggiunto.
- FASE 15 non eseguita.
- Nessun file elencato in `system/FROZEN_FILES.md` è stato modificato.
- Nessuna modifica a `sources/queue/QUEUE.md`, `sources/catalog.json`, `sources/VIDEO_INDEX.md` o ai transcript grezzi.
- `python3 scripts/validate_project.py` eseguito dopo il refactor: stesse anomalie preesistenti già documentate prima di questo checkpoint (confronto dei file congelati con il tag `v1.0`; disallineamenti d'ordine fra catalogo, VIDEO_INDEX e queue). Nessuna nuova anomalia introdotta dalla FASE 14.
- Controllo link/anchor su tutta `merenda/`: 0 errori su 40 file.
