# Manual Publishing Layer

## Purpose

Questa directory contiene il **publishing layer** derivato da Merenda Business Core.

Il suo scopo è trasformare la Knowledge Base canonica in un manuale teorico-operativo studiabile da un lettore che parte senza conoscenze pregresse di marketing.

Il publishing layer **non è doctrine layer canonico**.

- `merenda/` resta l'unica sede canonica della dottrina.
- `manual/` organizza, comprime, sequenzia e riscrive la conoscenza per finalità didattiche.
- Una formulazione nel manuale non prevale mai su un nodo canonico più preciso o più recente.

## Reader-facing rule

Il manuale finale deve essere agnostico rispetto alla provenienza personale della KB:

- non cita Frank Merenda;
- non parla di “dottrina Merenda”, “KB”, “Layer 1” o fonti interne;
- parla in voce autoriale diretta, come se l'autore stesse presentando il proprio sistema;
- non attribuisce a un singolo autore materiale che deriva da fonti assimilate differenti;
- non riproduce passaggi distintivi o lunghi estratti delle fonti: sintetizza e riscrive la conoscenza.

La provenance reale resta invece preservata **nel backend editoriale** quando serve a verificare origine, temporalità, conflitti e copertura.

## Bootstrap obbligatorio per ogni task sul manuale

Prima di lavorare sul manuale:

1. leggere `manual/ROADMAP.md`;
2. leggere `manual/STATUS.md`;
3. leggere `manual/MANUAL_CONTRACT.md`;
4. rileggere i file canonici necessari alla fase o al capitolo corrente;
5. usare la versione live di `main` come fonte corrente, registrando un nuovo baseline quando una fase sostanziale inizia.

Prima di terminare un task:

1. aggiornare `manual/STATUS.md`;
2. aggiornare `manual/ROADMAP.md` solo se cambia realmente lo stato di una fase, un gate o la sequenza;
3. non lasciare decisioni strutturali importanti soltanto in chat.

## Source-of-truth hierarchy per il manuale

In caso di conflitto:

1. nodo canonico specialistico corrente in `merenda/`;
2. chiarimento temporale/provenance corrente;
3. `merenda/DECISION_ROUTER.md` e `merenda/00_fondamenti/sistema-operativo-merenda.md` come sintesi;
4. `reviews/FINAL_SEMANTIC_AUDIT.md` per gap e stato del corpus;
5. artefatti editoriali in `manual/`;
6. chat.

## Regola di separazione

Un problema editoriale non autorizza automaticamente una modifica della dottrina canonica.

Se il lavoro sul manuale rende visibile un vero gap del doctrine layer:

1. registrarlo in `manual/MANUAL_GAPS.md`;
2. distinguere gap editoriale da gap dottrinale;
3. correggere il publishing layer se basta una sintesi editoriale;
4. trattare un'eventuale modifica di `merenda/` come lavoro canonico separato e verificato.

## Obiettivo operativo

Il risultato non deve essere una raccolta riordinata di file esistenti.

La pipeline è:

**KB canonica → inventario semantico → crosswalk → curriculum → gap closure → chapter specs → riscrittura autoriale → audit → manuale finale.**
