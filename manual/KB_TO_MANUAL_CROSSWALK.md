# KB-to-Manual Crosswalk — Master Index

## Purpose

Questo è il coverage master della Fase 2.

Il suo compito è garantire che la trasformazione della KB in manuale non perda conoscenza rilevante.

Non definisce ancora l'indice del libro. Le sezioni canoniche vengono usate soltanto come unità di decomposizione controllabile.

## Unità semantica

Ogni unità di conoscenza riceve un ID stabile nel file di sezione.

Tipi ammessi:

- `DEFINITION`
- `PRINCIPLE`
- `CAUSAL_RULE`
- `DECISION_RULE`
- `GATE`
- `PROCEDURE`
- `METRIC`
- `ERROR_PATTERN`
- `CAVEAT`
- `EXAMPLE`
- `CASE`
- `DEPENDENCY`
- `FEEDBACK_LOOP`

Una stessa unità può avere più di un tipo quando necessario, ma va evitata classificazione ridondante.

## Ruolo editoriale candidato

Ogni unità viene inizialmente marcata come:

- `PRIMARY` — probabile casa primaria nel manuale;
- `SUPPORTING` — rafforza un concetto la cui casa primaria sarà altrove;
- `EXAMPLE/CASE` — materiale applicativo;
- `REFERENCE` — utile al backend ma non da trasferire come unità reader-facing autonoma;
- `OPEN` — destinazione ancora da decidere.

La destinazione finale viene fissata soltanto dopo il cross-section deduplication pass e il curriculum.

## Provenance backend

Il crosswalk registra provenance soltanto quando serve per:

- distinguere fonte primaria da sintesi;
- ricordare una prevalenza temporale;
- non perdere un caveat;
- evitare falsa attribuzione.

Non replica il source registry.

## Coverage per sezione

| Sezione | File canonici | Stato semantic decomposition | Crosswalk |
|---|---:|---|---|
| `00_fondamenti` | 3 | COMPLETE | `manual/crosswalk/00_fondamenti.md` |
| `01_mercato` | 5 | NOT STARTED | — |
| `02_posizionamento` | 4 | NOT STARTED | — |
| `03_offerta` | 4 | NOT STARTED | — |
| `04_marketing` | 7 | NOT STARTED | — |
| `05_acquisizione` | 6 | NOT STARTED | — |
| `06_vendita` | 5 | NOT STARTED | — |
| `07_copy_comunicazione` | 5 | NOT STARTED | — |
| `08_brand` | 6 | NOT STARTED | — |
| `09_business` | 10 | NOT STARTED | — |
| `10_casi_studio` | 3 | NOT STARTED | — |
| **Totale** | **60** | **3/60 file covered** | **1/11 sezioni** |

## Pass successivi dopo le 11 sezioni

Quando tutti i file sono decomposti:

1. **semantic deduplication** — unire unità equivalenti senza perdere caveat;
2. **primary-home pass** — assegnare una casa primaria a ogni concetto;
3. **dependency pass** — esplicitare ciò che deve essere compreso prima;
4. **provenance/temporal pass** — verificare i concetti sensibili a evoluzione o assimilazione;
5. **case inventory pass** — mappare esempi e casi disponibili;
6. **gap pass** — aggiornare `manual/MANUAL_GAPS.md`;
7. **coverage audit** — verificare 60/60 file e tutte le unità rilevanti;
8. solo allora passare alla Fase 3 e progettare il curriculum.

## Regola di qualità

Il crosswalk non deve diventare un riassunto dei documenti.

Per ogni unità deve essere possibile rispondere a:

- che cosa deve capire il lettore?;
- che cosa deve saper decidere o fare?;
- da quali prerequisiti dipende?;
- che cosa influenza a valle?;
- quale caveat impedisce di trasformarla in slogan?;
- dove è più probabile che debba vivere nel manuale?
