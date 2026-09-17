# PROJECT STATUS

## Stato generale

**MERENDA KB CONSOLIDATION PHASE — CURRENT KNOWN CORPUS EXHAUSTED; FINAL SEMANTIC AUDIT COMPLETED.**

La fase video generalista è chiusa per saturazione al contenuto 313. Il lock operativo resta attivo in `sources/queue/ACQUISITION_CLOSED.md` e continua a impedire l'acquisizione automatica dei residui 314–468.

Il corpus source-agnostic attualmente disponibile è processato fino a `FM-SRC-0166`: 166 fonti registrate, 166 studiate, 0 pending.

Il checkpoint semantico di maturità è documentato in:

`reviews/FINAL_SEMANTIC_AUDIT.md`

La priorità del progetto non è più accumulare fonti, ma consolidare routing, provenance, sintesi e capacità applicativa della KB.

## Contatori canonici — corpus YouTube storico

- Video individuati: 468
- Video completati: 307
- Video esclusi: 6
- Video rimanenti: 155
- Processati semanticamente: 313

I 155 residui sono intenzionalmente non processati e non costituiscono backlog.

## Contatori canonici — layer source-agnostic

- Fonti registrate: 166
- Fonti studiate: 166
- Fonti escluse: 0
- Fonti da processare: 0

Questi contatori sono separati dal corpus YouTube storico.

Il layer non contiene esclusivamente fonti direttamente attribuibili a Frank Merenda. `sources/merenda-sources/collections.json` distingue il trattamento della fonte.

Categorie operative rilevanti:

- `MERENDA_PRIMARY` — fonte direttamente attribuibile a Frank Merenda;
- `ASSIMILATED_AS_MERENDA_BY_USER` — autore reale preservato, contenuto assimilato semanticamente per istruzione esplicita dell'utente;
- `DEFERRED_EXTERNAL_GENERAL_UPDATE` — materiale non fuso automaticamente nella KB.

Le collezioni Marketing Automation Facile / Moreno Bonechi e jAI Premium / Jay Abraham, Max Bernstein, Michael Simmons sono assimilate per istruzione utente. I relativi principi non devono essere falsamente attribuiti a Frank.

## Source layer

Registry canonico:

`sources/merenda-sources/catalog.json`

Convenzione per-source:

`sources/merenda-sources/FM-SRC-0001/`

Ogni fonte può conservare, quando appropriato:

- originale o riferimento stabile;
- contenuto normalizzato analizzabile;
- review canonica;
- metadata e limiti di provenienza.

Non è obbligatorio archiviare integralmente materiale protetto quando basta un riferimento stabile più il contenuto necessario alla verifica.

## Invarianti

- `merenda/` resta l'unico doctrine layer canonico del progetto;
- la KB è Merenda-centered ma può contenere estensioni assimilate **solo quando lo scope lo autorizza esplicitamente**;
- la provenance reale non viene mai falsificata;
- una fonte assimilata non viene attribuita a Frank soltanto perché è stata integrata nel doctrine layer;
- le nuove fonti non vengono aggiunte automaticamente come nuovi nodi: `MERGE, NOT APPEND`;
- il lock YouTube resta attivo;
- `sources/catalog.json`, `VIDEO_INDEX.md` e queue storica non vengono riconvertiti;
- i cinque file frozen restano invariati;
- ricerca esterna generale non autorizzata non viene mescolata silenziosamente dentro `merenda/`;
- Formalife resta fuori dalla fase di costruzione della dottrina.

## Provenienza e review

Ogni nuova fonte autorizzata deve avere provenance sufficiente, contenuto analizzabile, review, Weighted Novelty e routing finale.

In caso di reale incompatibilità fra fonti direttamente attribuibili a Merenda, prevale l'insegnamento più recente dopo aver distinto contraddizione, evoluzione, restringimento, ampliamento e differenza di contesto.

Per fonti assimilate di altri autori, la compatibilità semantica con la KB non cambia l'attribuzione originaria.

## Validator

Comando canonico:

`python3 scripts/validate_project.py`

Il validator certifica gli invarianti strutturali del corpus storico e del registry source-agnostic. **Non certifica da solo il merito semantico.** Il checkpoint finale in `reviews/FINAL_SEMANTIC_AUDIT.md` documenta la review semantica dell'attuale doctrine layer.

## Gap di consolidamento ancora aperti

Priorità indicate dal checkpoint finale:

1. **P1 — Vendita end-to-end:** sintetizzare i quattro nodi vendita in un processo operativo unico senza duplicarli.
2. **P1 — Casi studio:** ampliare selettivamente la libreria applicativa con casi realmente istruttivi e caveat espliciti.
3. **P1 — Doctrine/provenance map:** rendere leggibile a macchina la casa canonica, la fonte primaria/assimilata e l'eventuale prevalenza temporale dei principi ad alta leva.
4. **P2 — Sintesi brand:** collegare posizionamento, autorità, credibilità, prova, reputazione, memoria e community.
5. **P2 — Voice of Customer / ricerca mercato:** consolidare in un processo autonomo le tecniche oggi distribuite nella KB.
6. **P2 — Hardening Git:** protezione `main`, cleanup branch integrati, eventuale tag/release `merenda-kb-v1.0` dopo i refactor prioritari.

## Next Action

**Consolidamento della KB, non acquisizione generalista.**

Seguire il piano del `FINAL_SEMANTIC_AUDIT.md`, iniziando dai gap P1.

Riaprire l'acquisizione soltanto se:

- viene fornita una nuova fonte realmente disponibile;
- l'utente autorizza esplicitamente una nuova assimilazione;
- emerge un gap canonico concreto che richiede nuova provenance.

Non acquisire automaticamente i video residui 314+.

Non applicare ancora la dottrina a Formalife dentro questa repo.
