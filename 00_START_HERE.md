# START HERE

Questo repository serve a costruire e mantenere una Knowledge Base viva e gerarchica **centrata sulla dottrina di Frank Merenda**.

La fase storica basata sul canale YouTube ufficiale è chiusa per saturazione al contenuto 313. Il corpus source-agnostic attualmente disponibile è stato processato fino a `FM-SRC-0166` e il checkpoint semantico finale del corpus corrente è documentato in `reviews/FINAL_SEMANTIC_AUDIT.md`.

Formalife non deve entrare nella Knowledge Base e non deve influenzarne l'interpretazione.

## Stato operativo corrente

Il corpus YouTube storico resta congelato nei suoi invarianti:

- 468 video catalogati;
- 313 processati semanticamente;
- 307 STUDIATO;
- 6 ESCLUSO;
- 155 residui intenzionali.

Se esiste `sources/queue/ACQUISITION_CLOSED.md`, non avviare la vecchia acquisizione generalista, non eseguire `ingest_video.py` e non prendere il primo pendente della queue. Il lock riguarda il corpus YouTube storico.

Il layer source-agnostic vive in `sources/merenda-sources/`. Non va interpretato come se ogni record fosse necessariamente una fonte direttamente attribuibile a Frank Merenda.

Il campo `treatment` delle collezioni distingue:

- `MERENDA_PRIMARY` — materiale direttamente attribuibile a Frank Merenda;
- `ASSIMILATED_AS_MERENDA_BY_USER` — materiale di altro autore assimilato semanticamente per istruzione esplicita dell'utente, preservando sempre l'autore reale;
- `DEFERRED_EXTERNAL_GENERAL_UPDATE` — materiale esterno non inserito automaticamente nel doctrine layer.

Marketing Automation Facile / Moreno Bonechi e jAI Premium / Jay Abraham, Max Bernstein, Michael Simmons sono collezioni assimilate già presenti nel corpus corrente. I loro contributi non devono essere falsamente attribuiti a Frank.

Gli asset tecnici, quando conservati, vivono sotto `sources/merenda-sources/<SOURCE_ID>/`; la conoscenza consolidata continua invece a vivere in `merenda/`.

## Prima di fare qualsiasi lavoro

Leggi, nell'ordine:

1. `MASTER_PLAN.md`
2. `system/RULES.md`
3. `STATUS.md`
4. `reviews/FINAL_SEMANTIC_AUDIT.md` per conoscere lo stato di maturità, le correzioni temporali e i gap residui
5. `merenda/DECISION_ROUTER.md` quando il task richiede diagnosi, strategia, priorità o una decisione operativa
6. `merenda/00_fondamenti/sistema-operativo-merenda.md` quando serve comprendere le dipendenze complessive della dottrina
7. `sources/merenda-sources/README.md` quando il task riguarda provenance o una nuova fonte

`STATUS.md` è la fonte operativa corrente. I documenti frozen restano governance storica e non vanno modificati senza autorizzazione esplicita.

## Come usare la KB per problemi reali

Per richieste come:

- “non arrivano clienti”;
- “le lead non convertono”;
- “chiedono solo il prezzo”;
- “la vendita non chiude”;
- “i clienti non tornano”;
- “il fatturato cresce ma manca cassa”;
- “l’operatività non regge la crescita”;

non aprire direttamente il file che sembra più vicino al sintomo.

Usare il [Decision Router](merenda/DECISION_ROUTER.md) per:

1. definire l’outcome mancante;
2. localizzare il livello in cui il problema appare;
3. controllare almeno un livello a monte;
4. distinguere causa da amplificatore;
5. individuare il primo collo di bottiglia;
6. aprire i nodi canonici nell’ordine corretto;
7. formulare un test e una metrica prima di scalare.

Il [Sistema operativo Merenda](merenda/00_fondamenti/sistema-operativo-merenda.md) descrive invece l’architettura end-to-end del sistema. I due layer sono complementari: **architettura causale + routing diagnostico**.

## Ruoli

### Codex / strumenti locali

- Gestisce acquisizione tecnica, normalizzazione, trascrizione, estrazione selettiva di visuali e verifiche meccaniche.
- Non riapre i 155 video residui salvo autorizzazione esplicita su un gap nominabile.
- Per nuove fonti usa il formato tecnico più semplice adatto alla fonte.
- Non esegue il merge semantico nella KB salvo istruzione esplicita.

### ChatGPT

- È il processore semantico principale.
- Per richieste operative usa il Decision Router prima di proporre tattiche.
- Verifica provenienza, autore reale e trattamento della fonte.
- Legge o ascolta integralmente la parte rilevante della fonte.
- Distingue principi, esempi, tattiche, numeri e linguaggio provocatorio.
- Confronta la fonte con la KB pertinente.
- Applica `MERGE, NOT APPEND`.
- Risolve eventuali conflitti temporali privilegiando l'insegnamento Merenda più recente quando esiste una vera incompatibilità tra fonti Merenda.
- Non attribuisce a Frank un principio proveniente da una fonte assimilata di altro autore.
- Aggiorna review, registry, KB e STATUS quando il task riguarda nuove fonti autorizzate.

### Claude Code

Resta disponibile per revisioni strutturali e checkpoint quando richiesto esplicitamente. Non esiste più una cadenza automatica legata al numero di video.

## Regola fondamentale

I file elencati in `system/FROZEN_FILES.md` non devono essere modificati senza autorizzazione esplicita dell'utente.

Il progetto non ottimizza più per completezza numerica del corpus. Ottimizza per conoscenza utile, minima ridondanza, tracciabilità, corretta prevalenza temporale, provenance reale, routing decisionale e semplicità strutturale.

Nuova acquisizione va riaperta soltanto quando esiste una nuova fonte realmente disponibile, un'assimilazione esplicitamente autorizzata o un gap canonico concreto e nominabile.
