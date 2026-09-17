# Merenda Knowledge Base — Index

Questa è la porta di ingresso della Knowledge Base canonica centrata sulla dottrina di Frank Merenda.

## Stato

La fase video generalista è sufficientemente satura dopo la revisione semantica dei contenuti 1–313.

Il corpus source-agnostic attualmente disponibile è stato processato fino a `FM-SRC-0166`; non esistono fonti pending nel registry corrente.

La tassonomia a 11 sezioni resta stabile come doctrine layer. I contenuti residui del corpus YouTube non devono essere acquisiti automaticamente: una riapertura è ammessa solo per una nuova fonte realmente disponibile o per colmare un gap concreto e nominabile.

## Confine della provenance

La KB è **Merenda-centered**, ma il corpus corrente comprende anche estensioni assimilate semanticamente per istruzione esplicita dell'utente.

Il layer `sources/merenda-sources/collections.json` distingue almeno:

- `MERENDA_PRIMARY` — fonte direttamente attribuibile a Frank Merenda;
- `ASSIMILATED_AS_MERENDA_BY_USER` — autore reale preservato nella provenance, contenuto autorizzato dall'utente a entrare nel doctrine layer;
- `DEFERRED_EXTERNAL_GENERAL_UPDATE` — materiale esterno che non entra automaticamente nella KB.

Marketing Automation Facile / Moreno Bonechi e jAI Premium / Jay Abraham, Max Bernstein, Michael Simmons sono esempi di fonti assimilate già presenti nel corpus corrente.

**Regola obbligatoria:** una fonte assimilata non deve essere descritta o citata come se Frank Merenda avesse formulato direttamente quel principio. La provenance reale resta parte della conoscenza.

Nuova conoscenza esterna non viene fusa automaticamente nel doctrine layer. Richiede una decisione esplicita di scope o resta fuori dalla KB canonica.

## Ingresso operativo per l’AI

Quando la richiesta parte da un **problema concreto di business**, non scegliere subito una sezione per somiglianza superficiale.

Usare prima:

1. **[Decision Router](DECISION_ROUTER.md)** — localizza il primo livello rotto, controlla almeno un livello a monte e instrada verso i nodi canonici corretti.
2. **[Sistema operativo Merenda](00_fondamenti/sistema-operativo-merenda.md)** — mostra l’ordine causale complessivo della dottrina e le dipendenze fra i livelli.
3. Aprire quindi il README e i nodi specialistici della sezione indicata dal routing.

Il Decision Router risponde a **“dato questo problema, dove devo guardare per primo?”**. Il Sistema operativo risponde a **“come è organizzato l’intero sistema?”**.

## Routing tematico

- [00 — Fondamenti](00_fondamenti/README.md)
- [01 — Mercato](01_mercato/README.md)
- [02 — Posizionamento](02_posizionamento/README.md)
- [03 — Offerta](03_offerta/README.md)
- [04 — Marketing](04_marketing/README.md)
- [05 — Acquisizione](05_acquisizione/README.md)
- [06 — Vendita](06_vendita/README.md)
- [07 — Copy e comunicazione](07_copy_comunicazione/README.md)
- [08 — Brand](08_brand/README.md)
- [09 — Business](09_business/README.md)
- [10 — Casi studio](10_casi_studio/README.md)

## Regola di navigazione

Per una domanda puramente tematica, aprire il README della sezione pertinente e poi soltanto i file specifici necessari.

Per una diagnosi, una strategia o una richiesta operativa, passare prima dal [Decision Router](DECISION_ROUTER.md). Non saltare direttamente alla tattica proposta dall’utente se un problema a monte può spiegarne il sintomo.

Quando un documento di sintesi semplifica un principio, prevale sempre il nodo specialistico più preciso, contestuale o temporalmente aggiornato.

Quando un principio deriva da una fonte assimilata, prevale inoltre la **provenance reale**: compatibilità con la KB non equivale ad attribuzione a Frank.

La struttura può essere modificata in futuro solo quando un nuovo gap reale lo richiede; non va riorganizzata per inseguire completezza numerica o quantità di fonti.

Per lo stato di maturità corrente e i gap residui, vedere [FINAL SEMANTIC AUDIT](../reviews/FINAL_SEMANTIC_AUDIT.md).
