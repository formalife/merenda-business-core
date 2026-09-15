# START HERE

Questo repository serve a costruire una Knowledge Base viva e gerarchica della dottrina di Frank Merenda.

La fase storica basata sul canale YouTube ufficiale è chiusa per saturazione al contenuto 313. Da questo checkpoint il progetto continua in modalità source-agnostic: possono entrare nuove fonti Merenda indipendentemente dal formato, purché la provenienza e l'attribuzione siano verificabili.

Formalife non deve entrare nella Knowledge Base Merenda e non deve influenzarne l'interpretazione.

## Stato operativo corrente

Il corpus YouTube storico resta congelato nei suoi invarianti:

- 468 video catalogati;
- 313 processati semanticamente;
- 307 STUDIATO;
- 6 ESCLUSO;
- 155 residui intenzionali.

Se esiste sources/queue/ACQUISITION_CLOSED.md, non avviare la vecchia acquisizione generalista, non eseguire ingest_video.py e non prendere il primo pendente della queue. Il lock riguarda il corpus YouTube storico e non blocca nuove fonti Merenda source-agnostic.

Le nuove fonti Merenda sono registrate separatamente in sources/merenda-sources/catalog.json. Gli asset tecnici, quando conservati, vivono sotto sources/merenda-sources/<SOURCE_ID>/; la dottrina consolidata continua invece a vivere unicamente in merenda/.

## Prima di fare qualsiasi lavoro

Leggi, nell'ordine:

1. MASTER_PLAN.md
2. system/RULES.md
3. STATUS.md
4. sources/merenda-sources/README.md quando il task riguarda una nuova fonte Merenda

STATUS.md è la fonte operativa corrente. I documenti frozen restano governance storica e non vanno modificati senza autorizzazione esplicita.

## Ruoli

### Codex / strumenti locali

- Gestisce acquisizione tecnica, normalizzazione, trascrizione, estrazione selettiva di visuali e verifiche meccaniche.
- Non riapre i 155 video residui salvo autorizzazione esplicita su un gap nominabile.
- Per le nuove fonti usa il formato tecnico più semplice adatto alla fonte.
- Non esegue il merge semantico nella KB salvo istruzione esplicita.

### ChatGPT

- È il processore semantico principale.
- Verifica provenienza e attribuzione.
- Legge o ascolta integralmente la parte rilevante della fonte.
- Distingue principi, esempi, tattiche, numeri e linguaggio provocatorio.
- Confronta la fonte con la KB pertinente.
- Applica MERGE, NOT APPEND.
- Risolve eventuali conflitti temporali privilegiando l'insegnamento Merenda più recente quando esiste una vera incompatibilità.
- Aggiorna review, registry, KB e STATUS.

### Claude Code

Resta disponibile per revisioni strutturali e checkpoint quando richiesto esplicitamente. Non esiste più una cadenza automatica legata al numero di video.

## Regola fondamentale

I file elencati in system/FROZEN_FILES.md non devono essere modificati senza autorizzazione esplicita dell'utente.

Il progetto non ottimizza più per completezza numerica del corpus YouTube. Ottimizza per conoscenza utile, minima ridondanza, tracciabilità, corretta prevalenza temporale e semplicità strutturale.
