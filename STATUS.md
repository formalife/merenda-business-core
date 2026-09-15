# PROJECT STATUS

## Stato generale

**MERENDA SOURCE-AGNOSTIC PHASE ACTIVE — BATCH 001 STUDIED; VIDEO PHASE LOCKED.**

La fase video generalista è chiusa per saturazione al contenuto 313. Il lock operativo resta attivo in sources/queue/ACQUISITION_CLOSED.md e continua a impedire l'acquisizione automatica dei residui 314–468.

La Knowledge Base Merenda può ora essere ampliata con nuove fonti di Frank Merenda indipendentemente dal formato, usando il nuovo layer sources/merenda-sources/.

## Contatori canonici — corpus YouTube storico

- Video individuati: 468
- Video completati: 307
- Video esclusi: 6
- Video rimanenti: 155
- Processati semanticamente: 313

I 155 residui sono intenzionalmente non processati e non costituiscono backlog.

## Contatori canonici — nuove fonti Merenda

- Nuove fonti Merenda registrate: 40
- Nuove fonti Merenda studiate: 40
- Nuove fonti Merenda escluse: 0
- Nuove fonti Merenda da processare: 0

Questi contatori sono separati dal corpus YouTube storico.

## Source layer

Registry canonico nuove fonti:

sources/merenda-sources/catalog.json

Convenzione per-source:

sources/merenda-sources/FM-SRC-0001/

Ogni fonte può conservare, quando appropriato:

- originale o riferimento stabile;
- contenuto normalizzato analizzabile;
- review canonica;
- metadata e limiti di provenienza.

Non è obbligatorio archiviare integralmente materiale protetto quando basta un riferimento stabile più il contenuto necessario alla verifica.

## Invarianti

- merenda/ resta l'unica KB canonica della dottrina Merenda;
- le nuove fonti non vengono aggiunte automaticamente come nuovi nodi: MERGE, NOT APPEND;
- il lock YouTube resta attivo;
- sources/catalog.json, VIDEO_INDEX.md e queue storica non vengono riconvertiti;
- i cinque file frozen restano invariati;
- nessuna Evidence / External KB viene mescolata dentro merenda/;
- Formalife resta fuori dalla fase di costruzione della dottrina.

## Provenienza e review

Ogni nuova fonte processata deve avere provenance sufficiente, contenuto analizzabile, review, Weighted Novelty e routing finale.

In caso di reale incompatibilità fra fonti Merenda, prevale l'insegnamento più recente dopo aver distinto contraddizione, evoluzione, restringimento, ampliamento e differenza di contesto.

## Validator

Comando canonico:

python3 scripts/validate_project.py

Il validator continua a certificare gli invarianti del corpus video storico e, in aggiunta, controlla il nuovo registry source-agnostic.

## Next Action

**CHATGPT — fase newest-first del Substack ufficiale 2026 sostanzialmente saturata; passare a gap-driven audit di fmerenda 2025, Marketing Rodeo e archivi storici, integrando solo concetti assenti o formulazioni temporalmente rilevanti.**

Non acquisire video residui 314+.

Non creare ancora Evidence / External KB.

Non applicare ancora la dottrina a Formalife.
