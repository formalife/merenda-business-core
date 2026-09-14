# PROJECT STATUS

## Stato generale

ACTIVE — fasi 1–6 complete; contenuti 1–175 processati semanticamente; checkpoint 175 (FASE 14) completato; acquisizione tecnica 176–200 completata. Corpus ancora incompleto.

## Fase corrente

**Batch tecnico 176–200: 25/25 acquisiti, con transcript italiani utilizzabili.** Metadata, JSON3 e Markdown normalizzati verificati. Un frame candidato controllato, con nota tecnica. Elaborazione semantica ancora ferma a 175; nessuna fase 8–13 eseguita in questa acquisizione.

## Corpus

- Video individuati: 468
- Contenuti processati semanticamente: 175
- STUDIATO / integrati nella KB: 169
- ESCLUSO dalla dottrina attiva: 6
- Da processare: 293
- Corpus completo: NO
- Batch tecnico 176–200: 25/25 utilizzabili
- Elaborazione semantica 176–200: 0/25
- Transcript mancanti: 0
- Fallback ASR nel batch 176–200: 0
- Errori finali: 0
- Pending tecnici: 0
- Blocchi semantici residui dal batch precedente: 0

## Workflow attivo — v1.1

- CODEX / strumenti locali: acquisizione tecnica a batch e sincronizzazione meccanica.
- CHATGPT: revisione semantica e fasi 8–13.
- CLAUDE CODE: FASE 14 ogni 25; FASE 14 + 15 ogni 50.

## Checkpoint

- Ultimo refactor KB completato: **175**
- Ultimo audit tassonomia completato: 150
- Prossimo checkpoint dopo il completamento semantico: **200 — FASE 14 + FASE 15**
- Checkpoint Claude richiesto ora: **NO**
- Documento checkpoint corrente: `reviews/CHECKPOINT_175.md`

Al checkpoint 200 verrà valutato anche il rendimento marginale della KB e la priorità dei contenuti 201–468, per decidere se proseguire con ingestione approfondita uniforme o con processamento differenziato in base alla novelty.

Questo è soltanto un promemoria operativo: nessun cambio di strategia implementato ora.

## Agente richiesto

**CHATGPT**

## Next Action

Iniziare l'elaborazione semantica del batch 176–200 dal video **176 — aQ5V7845jX4**, usando gli asset in `sources/transcripts/` e il report `sources/queue/acquisition-progress.md`. La necessità finale di ulteriori visuali va valutata durante la revisione ChatGPT.

Procedere sui 25 asset acquisiti fino al checkpoint **200 — FASE 14 + FASE 15**. L'acquisizione anticipata non equivale a studio.

## Validazione e blocchi

- Branch tecnico: `acquisition-176-200`; base `d5e87844a7cd17529ff7c6eb189ea1da7cb3f14e`.
- 25 ID esatti verificati sulle posizioni 176–200; provenienza ufficiale, integrità JSON3, copertura temporale e corrispondenza segmento per segmento con il Markdown confermate.
- 24 transcript automatici italiani e 1 manuale italiano (`TF9UGPSLxSw`); nessun fallback ASR.
- 18 errori transitori di rete del sandbox nel primo passaggio, risolti integralmente con il successivo passaggio autorizzato. Nessun blocco tecnico aperto.
- Un frame di `6tgz9aFzyNE` verificato in seguito alla citazione di una slide: mostra il relatore, senza slide leggibile. Nota nella relativa cartella `-frames`.
- Alcuni asset grezzi parziali risultavano già tracciati nella base; verificati e completati, come documentato nel report tecnico.
- Nessun contenuto 201+ acquisito in questo batch.
- KB, file congelati, catalogo, VIDEO_INDEX, QUEUE e stati semantici invariati; nessun `.review.md` creato.
- Validator: 841 segnalazioni, identiche alla baseline (836 disallineamenti ordine/stato, 3 divergenze storiche frozen rispetto al tag v1.0, 2 warning contatori STATUS). Nessuna nuova anomalia.
- `git diff --check`: superato anche rispetto alla base.
- Tracciabilità: 25 commit individuali di acquisizione più 1 commit globale di handoff. Nessun merge in main.
