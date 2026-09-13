# PROJECT STATUS

## Stato generale

ACTIVE — fasi 1–6 complete; primi 125 contenuti processati semanticamente; checkpoint 125 raggiunto. Refactor KB del checkpoint 125 ancora da eseguire.

## Fase corrente

**Checkpoint 125 raggiunto — elaborazione semantica conclusa; richiesta soltanto FASE 14.**

## Corpus

- Video individuati: 468
- Contenuti processati semanticamente: 125
- STUDIATO / integrati nella KB: 121
- ESCLUSO dalla dottrina attiva: 4
- Da processare: 343
- Video completati: 121
- Video rimanenti: 343
- Corpus completo: NO
- Asset tecnici 101–125: ACQUISITI 25/25
- Elaborazione semantica 101–125: 25/25 completati

## Workflow attivo — v1.1

- CODEX / script locale: acquisizione tecnica a batch e sincronizzazione meccanica.
- CHATGPT: revisione semantica e fasi 8–13.
- CLAUDE CODE: fase 14 ogni 25; fase 14 + 15 ogni 50.

## Checkpoint

- Ultimo refactor KB completato: 100
- Ultimo audit tassonomia completato: 100
- Checkpoint raggiunto: 125
- Checkpoint Claude richiesto ora: SÌ
- Refactor richiesto ora: SÌ — FASE 14
- FASE 15 richiesta ora: NO
- Prossimo audit tassonomia: 150

Documento di checkpoint: `reviews/CHECKPOINT_125.md`.

## Integrazione e sincronizzazione 121–125

Branch `semantic-121-125` integrato con fast-forward da `34b1022090fe18378086cb9f2643f06f7605b7b8` a `9068bfa9e9bd9f24b685686e0089d39e8f261d69`, preservando i cinque commit semantici e il commit del checkpoint.

Stato sincronizzato a STUDIATO in catalogo, queue e VIDEO_INDEX per `-GsWbIj44dQ`, `8bQmDJJTEqs`, `nJuSh2u1dOE`, `_zqwnqzzv-4`, `0qipJSkZxmg`; riferimenti alle review nel catalogo secondo la convenzione 116–120. Nessuna modifica aggiuntiva a KB, review, transcript o file congelati. Ordine della queue invariato.

## Agente richiesto

**CLAUDE CODE**

## Next Action

Claude deve:

1. leggere i file canonici, iniziando da `00_START_HERE.md`, `MASTER_PLAN.md`, `system/RULES.md` e `STATUS.md`, poi le istruzioni di ruolo e fase applicabili;
2. leggere `reviews/CHECKPOINT_125.md`;
3. eseguire **soltanto FASE 14 — refactor KB**;
4. non eseguire FASE 15;
5. non introdurre nuova dottrina;
6. aggiornare checkpoint e `STATUS.md`;
7. verificare routing, link e anchor;
8. eseguire commit e push su `origin/main`.

Dopo il refactor, verificare realmente la disponibilità degli asset del prossimo contenuto: richiedere CHATGPT se disponibili, altrimenti CODEX per il batch successivo. Gli asset 126+ non risultano disponibili; il passaggio previsto è quindi a CODEX, da confermare con verifica locale. Non acquisire nuovi video durante il refactor.

## Primo pendente

`dwfknCGx8UI` — *MARKETING | Diventare il punto di riferimento per il tuo Settore [Jay Abraham]* — `04_marketing` — posizione 126 della queue.

Verificata l'assenza di asset `sources/transcripts/dwfknCGx8UI.*` durante questa sincronizzazione. Batch 126–150 non avviato.

## Validazione e blocchi

Controlli meccanici dedicati: contatori 468 / 121 / 4 / 343, primi 125 della queue conclusi, cinque stati coerenti nei tre registri, primo pendente e asset 101–125 verificati. File congelati invariati rispetto al main iniziale; KB e review identiche al branch semantico integrato.

`scripts/validate_project.py` eseguito: NON PASSA per anomalie già presenti prima della sincronizzazione. Confronta i file congelati con il tag v1.0 (MASTER_PLAN.md, system/HANDOFFS.md e system/FROZEN_FILES.md differiscono già nella base) e richiede identico ordine delle righe tra catalogo, VIDEO_INDEX e queue (418 disallineamenti per ciascun confronto già nella base). Nessuna nuova anomalia introdotta; i contatori STATUS richiesti dallo script sono ora presenti. Script e ordinamenti preesistenti lasciati invariati nel perimetro di questo task.

Nessun nuovo blocco semantico segnalato da CODEX; la verifica strutturale non certifica la qualità semantica. FASE 14 e FASE 15 non eseguite in questa sincronizzazione.
