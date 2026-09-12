# MASTER PLAN — Merenda Knowledge System

Questo documento definisce il processo ufficiale del progetto.

Non modificarlo senza autorizzazione esplicita dell'utente.

---

## BLOCCO A — Setup iniziale — CODEX

### 1. Crea repository condiviso

Predisporre struttura, Git, file di governo, cartelle operative e stato iniziale.

### 2. Definisci KB e routing iniziali

Creare la tassonomia iniziale della Knowledge Base e il routing gerarchico tramite `merenda/INDEX.md` e README di sezione.

La tassonomia iniziale è provvisoria e potrà essere rifattorizzata durante i checkpoint.

### 3. Scansiona tutto il canale

Censire tutti i video disponibili del canale YouTube ufficiale `@FrankMerendaTV`.

### 4. Crea catalogo completo

Popolare `sources/VIDEO_INDEX.md` con tutti i video individuati e le informazioni operative necessarie.

### 5. Classifica preliminarmente i video

Assegnare a ogni video una categoria preliminare, una priorità iniziale e uno stato.

### 6. Costruisci la roadmap iniziale di apprendimento

Ordinare i video in `sources/queue/QUEUE.md` secondo l'ordine più utile per comprendere progressivamente il sistema di pensiero di Frank Merenda.

---

## BLOCCO B — Ingestion loop — CODEX

Le fasi 7–13 vengono ripetute per ogni video della queue fino al completamento dell'intero corpus.

### 7. Acquisisci il transcript

Acquisire il transcript disponibile. Se non esiste, ricavarlo dall'audio con uno strumento appropriato.

### 8. Correggi e pulisci il transcript

Migliorare punteggiatura, segmentazione e errori evidenti senza inventare contenuti.

### 9. Individua incomprensioni importanti

Quando una porzione importante non è interpretabile con sufficiente sicurezza, segnalarla chiaramente per revisione umana. Non bloccare il resto del video se il problema è locale.

### 10. Esegui analisi visuale selettiva quando necessaria

Usare l'audio/transcript per individuare momenti in cui slide, grafici, schemi, numeri o altri elementi visivi possono contenere informazione importante. Estrarre e analizzare solo i keyframe pertinenti.

### 11. Estrai le conoscenze importanti

Identificare concetti, principi, procedure, esempi, errori, avvertenze, relazioni e insegnamenti utili. Evitare il semplice riassunto cronologico del video.

### 12. Integra / merge / riscrivi la KB

Integrare le nuove conoscenze nella posizione corretta della KB.

Regola principale: MERGE, NON APPEND.

- nuova conoscenza → inserire;
- approfondimento → ampliare;
- spiegazione migliore → riscrivere;
- esempio utile → aggiungere;
- ripetizione → non duplicare;
- contraddizione → privilegiare il contenuto più recente e archiviare il precedente solo se utile.

### 13. Aggiorna indice, collegamenti e passa al video successivo

Aggiornare:

- `merenda/INDEX.md` se necessario;
- collegamenti interni;
- stato del video;
- `STATUS.md`;
- queue.

Dopo ogni video verificare se è scattato un checkpoint Claude.

---

## BLOCCO C — Manutenzione periodica — CLAUDE CODE

### 14. Refactor KB — ogni 25 video completati

Controllare e migliorare:

- duplicazioni;
- file troppo lunghi;
- frammentazione inutile;
- gerarchia;
- routing;
- collegamenti;
- nomi delle sezioni;
- sintesi dei README di sezione.

Conservare il contenuto sostanziale, migliorando l'architettura.

### 15. Audit globale della tassonomia — ogni 50 video completati

Chiedersi se, alla luce delle conoscenze accumulate, la KB verrebbe ancora organizzata nello stesso modo.

Se necessario:

- unire categorie;
- separare categorie;
- rinominare;
- spostare file;
- correggere il learning path;
- riordinare i video non ancora studiati.

Dopo il checkpoint, aggiornare `STATUS.md` e restituire il controllo a Codex, salvo corpus completo.

---

## BLOCCO D — Finalizzazione — CLAUDE CODE

### 16. Conferma completamento del primo passaggio

Verificare che tutti i video previsti siano stati processati o esplicitamente esclusi con motivazione.

### 17. Costruisci le sintesi di alto livello

Creare o consolidare documenti trasversali ad alta compressione, tra cui almeno:

- `merenda/START_HERE.md`
- `merenda/PRINCIPI.md`
- `merenda/METODO.md`
- `merenda/ERRORI_DA_NON_FARE.md`
- `merenda/COME_COSTRUIRE_UN_BUSINESS_DA_ZERO.md`

I documenti devono rimandare alla KB sottostante e non sostituirla.

### 18. Esegui secondo passaggio mirato

Rivedere prioritariamente:

- video fondamentali;
- video vecchi potenzialmente superati;
- video con incomprensioni;
- aree diventate centrali solo più avanti;
- contraddizioni;
- contenuti particolarmente densi.

### 19. Refactor finale

Compattare e riorganizzare l'intera KB affinché sia semplice, coerente, navigabile e token-efficient.

### 20. Congela Merenda KB v1.0

Creare commit e tag Git `merenda-kb-v1.0`.

Da questo punto la KB Merenda diventa la Source of Truth teorica del progetto.

### 21. Introduci i fatti Formalife

Creare una sezione Formalife separata e popolarla con soli fatti correnti e verificabili: asset, persone, competenze, prodotti, numeri, vincoli, risorse, clienti, territorio e altri dati reali.

Non importare automaticamente vecchie strategie o conclusioni.

### 22. Ricostruisci Formalife da zero

Usare:

- Merenda KB v1.0;
- fatti Formalife;

per ricostruire da zero strategia, mercato, posizionamento, offerta, marketing, vendita ed esecuzione.
