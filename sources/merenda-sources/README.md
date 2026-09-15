# Merenda Sources — source-agnostic layer

Questa cartella registra le nuove fonti Merenda successive alla chiusura del corpus YouTube storico.

Non sostituisce sources/catalog.json e non converte retroattivamente i 468 video. I due sistemi restano distinti.

## Registry

Il registry canonico è catalog.json.

Ogni record usa un ID stabile nel formato:

FM-SRC-0001

Gli ID sono progressivi, non vengono riutilizzati e non dipendono dal formato della fonte.

Campi canonici:

- id
- type
- title
- author_or_speaker
- source_ref
- published_date
- acquired_date
- origin
- status
- normalized_path
- review_path
- category
- weighted_novelty
- notes

Tipi ammessi:

video, audio, podcast, interview, article, blog, newsletter, webpage, pdf, document, transcript, webinar, course, post, other.

Stati ammessi:

DA STUDIARE, STUDIATO, ESCLUSO.

published_date può essere null quando non è determinabile in modo affidabile. category e weighted_novelty restano null finché la fonte non è stata studiata.

## Layout per-source

Quando servono asset locali:

sources/merenda-sources/FM-SRC-0001/

Dentro la cartella possono comparire, secondo necessità:

- original.* — copia tecnica dell'originale, soltanto quando appropriato;
- content.md — testo o transcript normalizzato usato per la review;
- metadata.json — metadata tecnici aggiuntivi se realmente utili;
- visual/ — solo visuali indispensabili alla comprensione;
- review.md — review canonica della fonte.

Non tutti questi file sono obbligatori. Il registry deve però puntare al materiale effettivamente usato.

## Workflow

Per ogni fonte:

1. verifica provenienza e attribuzione;
2. registra la fonte;
3. rendi disponibile il contenuto rilevante in forma analizzabile;
4. leggi/ascolta integralmente la parte rilevante;
5. usa visuali solo quando aggiungono informazione;
6. confronta con la KB pertinente;
7. classifica come dedup, estensione o nuovo framework;
8. applica la prevalenza temporale quando necessaria;
9. MERGE, NOT APPEND;
10. assegna Weighted Novelty 0, 1 o 2;
11. crea review.md;
12. aggiorna registry e STATUS.md;
13. esegui il validator.

## Separazione concettuale

merenda/ contiene soltanto la dottrina consolidata.

sources/merenda-sources/ contiene provenienza, materiale tecnico e review delle nuove fonti Merenda.

Fonti non-Merenda, ricerca esterna ed Evidence KB non entrano in questa cartella come se fossero dottrina Merenda.


## Collezioni di fonti

Quando l'utente fornisce un archivio, un sito o una serie, l'archivio non viene trattato come una singola fonte semantica.

Le collezioni sono registrate separatamente in `collections.json`; ogni articolo, episodio o documento che viene realmente studiato riceve invece il proprio ID `FM-SRC-NNNN` in `catalog.json`.

Il campo `treatment` di una collezione distingue:

- `MERENDA_PRIMARY` — materiale direttamente attribuibile a Frank Merenda;
- `ASSIMILATED_AS_MERENDA_BY_USER` — autore reale preservato nella provenance, ma contenuto trattato come corpus Merenda per esplicita istruzione dell'utente;
- `DEFERRED_EXTERNAL_GENERAL_UPDATE` — materiale tenuto fuori dalla Merenda KB e rimandato a una fase successiva.

La provenance reale non viene mai falsificata anche quando l'utente autorizza l'assimilazione semantica.
