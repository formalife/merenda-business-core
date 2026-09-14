# PROJECT STATUS

## Stato generale

ACTIVE — fasi 1–6 complete; contenuti 1–200 processati semanticamente; batch 176–200 completato; checkpoint 200 raggiunto. Corpus ancora incompleto.

## Fase corrente

**Batch semantico 176–200: 25/25 completato.** Tutti i transcript tecnici del batch erano utilizzabili; create 25 review semantiche e aggiornati catalogo, VIDEO_INDEX e QUEUE. Checkpoint **200 — FASE 14 + FASE 15** ora dovuto.

## Corpus

- Video individuati: 468
- Contenuti processati semanticamente: 200
- STUDIATO / integrati o deduplicati: 194
- ESCLUSO dalla dottrina attiva: 6
- Da processare: 268
- Corpus completo: NO
- Batch tecnico 176–200: 25/25 utilizzabili
- Elaborazione semantica 176–200: 25/25
- Transcript mancanti nel batch: 0
- Fallback ASR nel batch: 0
- Errori finali tecnici: 0
- Blocchi semantici aperti: 0

## Rendimento marginale batch 176–200

- Video con conoscenza incrementale integrata: **8/25 (32%)**
- Video studiati ma deduplicati/non incrementali: **17/25 (68%)**
- Shorts 176–184: **0/9 incrementali**
- Video 185–200: **8/16 incrementali (50%)**

Il dato è un campione operativo, non una regola universale. Al checkpoint 200 va usato per valutare una priorità differenziata dei contenuti 201–468 senza saltare la revisione semantica di alcun video.

## Workflow attivo — v1.1

- CODEX / strumenti locali: acquisizione tecnica a batch e sincronizzazione meccanica.
- CHATGPT: revisione semantica e fasi 8–13.
- CLAUDE CODE: FASE 14 ogni 25; FASE 14 + 15 ogni 50.

## Checkpoint

- Ultimo refactor KB completato: **175**
- Ultimo audit tassonomia completato: **150**
- Refactor KB dovuto ora: **200 — FASE 14**
- Audit tassonomia dovuto ora: **200 — FASE 15**
- Checkpoint Claude richiesto ora: **YES**
- Documento checkpoint corrente: `reviews/CHECKPOINT_200.md`

## Agente richiesto

**CLAUDE CODE**

## Next Action

Eseguire sullo stato canonico del repository il checkpoint **200 — FASE 14 + FASE 15**:

1. rilettura/refactor globale della KB secondo FASE 14;
2. audit della tassonomia secondo FASE 15;
3. controllo specifico delle integrazioni 176–200 e dei due nuovi nodi di `05_acquisizione`;
4. valutazione del novelty yield 176–200 e della priorità dei contenuti 201–468;
5. esecuzione dei validator locali e documentazione di baseline/anomalie;
6. aggiornamento di `reviews/CHECKPOINT_200.md` e `STATUS.md`.

Non processare semanticamente contenuti 201+ durante il checkpoint.

Dopo FASE 14 + 15, se gli asset 201–225 non sono già presenti, passare a CODEX per l'acquisizione tecnica del batch successivo.

## Validazione e blocchi

- Branch tecnico origine batch: `acquisition-176-200`; HEAD tecnico: `448e9e2c136fbdb3ccbbf53e19486b0e61a15948`.
- Branch semantico: `semantic-176-200`.
- 25/25 contenuti 176–200 risultano `STUDIATO`.
- 25 review `.review.md` create.
- 25 commit semantici individuali, uno per video, prima del commit globale di handoff.
- File frozen non modificati dal batch semantico.
- KB modificata soltanto dove la conoscenza era incrementale; due nuovi nodi creati in `05_acquisizione`.
- Ultimo validator locale noto prima del batch semantico: 841 segnalazioni, baseline già documentata al checkpoint 175/acquisizione 176–200. Il validator deve essere rieseguito da Claude sul checkpoint 200; non assumere che il totale debba restare identico dopo l'avanzamento degli stati.
- Nessun contenuto 201+ studiato o acquisito in questo batch.
