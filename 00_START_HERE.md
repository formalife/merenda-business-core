# START HERE

Questo repository è **Merenda Business Core**, il **Layer 1** del sistema operativo aziendale.

Contiene doctrine canonica, routing e disciplina decisionale. Formalife vive nel Layer 2 e non deve contaminare automaticamente la dottrina.

## Stato operativo

- corpus YouTube storico: 468 individuati, 313 processati semanticamente, 155 residui intenzionali;
- source-agnostic: 166 fonti registrate e 166 studiate;
- Architecture Review: hierarchical retrieval + Compact Reasoning Kernel validati su blind holdout;
- control plane operativo candidato: `REASONING_KERNEL.md`;
- doctrine canonica: `merenda/`;
- stato corrente: `STATUS.md`.

Se esiste `sources/queue/ACQUISITION_CLOSED.md`, non riaprire automaticamente la vecchia acquisizione YouTube.

## Startup per task strategici o diagnostici

**Non precaricare più i cinque full control-plane documents.**

Usa progressive disclosure:

1. `STATUS.md` per stato e decisioni architetturali correnti;
2. `REASONING_KERNEL.md` come bootstrap decisionale compatto;
3. compact semantic index / routing metadata quando disponibili;
4. sezione canonica specialistica minima pertinente;
5. structural search / parent-child expansion se serve recall;
6. full specialist node solo quando la sezione non basta;
7. full control-plane documents soltanto come fallback, audit o verifica di governance.

La doctrine specialistica prevale sempre sul kernel quando è più recente, precisa o contestuale.

Il kernel non sostituisce la KB: evita di caricare in anticipo governance e sintesi ridondanti.

## Startup per Formalife / Layer 2

Per un task Formalife sostanziale:

1. leggere live `formalife/formalife-company-os/PROJECT_BOOTSTRAP.md`;
2. leggere `formalife/formalife-company-os/LAYER1_REF.md`;
3. leggere i file Layer 2 pertinenti;
4. usare `REASONING_KERNEL.md` come bootstrap Layer 1;
5. recuperare solo i nodi specialistici Layer 1 necessari alla decisione.

Principio: **ripartire da zero nelle decisioni, non da zero nella conoscenza.**

I full file `LAYER1_CONTRACT.md`, `FORMALIFE_REBUILD_PROTOCOL.md`, `MERENDA_MODE.md`, `merenda/DECISION_ROUTER.md` e `merenda/00_fondamenti/sistema-operativo-merenda.md` restano riferimenti canonici e fallback, non preload operativo predefinito.

## Startup per governance, corpus e nuove fonti

Quando il task riguarda acquisizione, provenance, consolidamento della KB o governance del repository, il percorso è diverso. Leggere solo ciò che è pertinente fra:

- `MASTER_PLAN.md`;
- `system/RULES.md`;
- `system/FROZEN_FILES.md`;
- `STATUS.md`;
- `reviews/FINAL_SEMANTIC_AUDIT.md`;
- `sources/merenda-sources/README.md`;
- full control-plane documents se il task li coinvolge direttamente.

I file frozen non devono essere modificati senza autorizzazione esplicita.

## Provenance

Il layer source-agnostic distingue almeno:

- `MERENDA_PRIMARY` — materiale direttamente attribuibile a Frank Merenda;
- `ASSIMILATED_AS_MERENDA_BY_USER` — materiale di altro autore assimilato per istruzione esplicita, mantenendo l'autore reale;
- `DEFERRED_EXTERNAL_GENERAL_UPDATE` — materiale esterno non promosso automaticamente nel doctrine layer.

Una fonte assimilata può contribuire alla KB quando l'assimilazione è esplicitamente autorizzata, ma non va mai falsamente attribuita a Frank.

Formalife evidence resta Layer 2 salvo separata revisione dottrinale.

## Regole decisionali operative

Per problemi reali non aprire il file che sembra più vicino al sintomo e non partire dalla tattica richiesta.

Il pattern è:

**outcome economico → localizzazione del sintomo → almeno un livello a monte → primo collo di bottiglia → doctrine specialistica minima → evidenza/test → metrica → next decision.**

Domanda guida:

**Cosa deve essere vero prima che questa tattica abbia senso?**

Classificare correttamente:

- FACT;
- ASSET;
- CONSTRAINT;
- HYPOTHESIS;
- LEGACY DECISION;
- OBSERVATION;
- OPEN QUESTION.

Non convertire silenziosamente hypothesis in fact o legacy decision in constraint.

## Ruoli

### ChatGPT

- processore semantico e adviser strategico;
- usa il kernel per bootstrap e recupera doctrine specialistica progressivamente;
- preserva provenance e temporal precedence;
- aggiorna la KB con `MERGE, NOT APPEND` quando esplicitamente autorizzato;
- non trasferisce automaticamente risultati Formalife nel Layer 1.

### Codex / strumenti locali

- acquisizione tecnica, normalizzazione, transcript, visuali selettive, validation e harness;
- non riapre i 155 residui YouTube senza autorizzazione;
- non esegue merge semantico salvo istruzione esplicita.

## Criterio finale

Il progetto non ottimizza per quantità di documenti letti né completezza numerica del corpus.

Ottimizza per:

**decision fidelity + doctrine pertinente + provenance + context efficiency + verificabilità.**
