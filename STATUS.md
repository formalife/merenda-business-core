# PROJECT STATUS

## Stato generale

ACTIVE — fasi 1–6 complete; contenuti **1–225 processati semanticamente**. Checkpoint **225 completato (FASE 14 eseguita da Claude Code)**. Corpus ancora incompleto.

## Fase corrente

**FASE 7 — batch tecnico 226–250 completato: 25/25 utilizzabili per la revisione.** Nessuna FASE 8–13 eseguita da Codex, nessuna integrazione KB o review semantica. Branch `acquisition-226-250`, base `da0a20c00882f287674635109e625fef47f23408`; 25 commit individuali e 1 handoff finale, senza merge su main.

## Corpus

- Video individuati: 468
- Contenuti processati semanticamente: **225**
- STUDIATO / integrati o deduplicati: **219**
- ESCLUSO dalla dottrina attiva: **6**
- Da processare: **243**
- Corpus completo: NO
- Batch tecnico 226–250: **25/25** metadata, JSON3 e Markdown verificati
- Elaborazione semantica 226–250: **0/25**
- Review create nel batch: **0**
- Tracce: **25 automatiche italiane originali**, 0 manuali
- Transcript mancanti / NO_IT_TRANSCRIPT: **0**
- Fallback ASR: **0**
- Errori finali tecnici: **0**
- Pending tecnici: **0**
- Keyframe candidati: **9 su 4 video** (235, 236, 241, 247)

## Workflow attivo — v1.1

- CODEX: acquisizione tecnica e supporto meccanico.
- CHATGPT: revisione semantica e fasi 8–13.
- CLAUDE CODE: FASE 14 ogni 25; FASE 14 + 15 ogni 50.
- Classificazione A/B/C invariata; medesima completezza tecnica per tutte le classi.
- Per i C/short, verificare la recenza durante la revisione secondo il checkpoint 225; date ufficiali conservate nei metadata di tutti i 25 contenuti. Nessuna promozione o modifica al classificatore durante questo batch.
- Nessuna modifica ai file frozen, alla KB, al catalogo, all’indice video o alla queue canonica.

## Checkpoint

- Ultimo refactor KB completato: **225 — FASE 14**
- Ultimo audit tassonomia completato: **200**
- Prossimo checkpoint Claude: **250 — FASE 14 + FASE 15**, dopo il completamento semantico
- Checkpoint Claude richiesto ora: **NO**
- Report checkpoint corrente: `reviews/CHECKPOINT_225.md`

## Agente richiesto

**CHATGPT**

## Next Action

Verificare l’handoff tecnico sul branch `acquisition-226-250`, quindi revisione semantica **226–250** (fasi 8–13). Primo contenuto: **226 — `m53_BsS_x8U`**. Asset pronti in `sources/transcripts/`; report completo in `sources/queue/acquisition-progress.md`. Nessun contenuto 251+ acquisito in questa task.

## Validazione e limiti

- Validator prima/dopo: **841 warning storici identici**, confronto integrale senza differenze; nessuna nuova anomalia. `git diff --check` superato.
- 25/25 metadata del canale ufficiale e corrispondenza JSON3↔Markdown verificati; nessuna correzione inventata.
- 232/233 avevano già metadata/JSON3 nella base: riutilizzati e completati con Markdown. Gli altri 23 sono nuovi download. Tutti e 25 persistiti individualmente.
- 227: copertura intervallo 95,51%, coda fuori dalla traccia 4,559 s; ultimo evento [musica]. 228: copertura 92,79%, coda fuori dalla traccia 6,720 s, non verificata tramite ascolto. Testo disponibile conservato integralmente. Nessun offset/taglio; piccoli sforamenti fino a 2,360 s documentati nel report.
- Limite storico **218 — `JQXoKKwneBQ`** invariato: timestamp/visuali nella parte disallineata non costituiscono evidenza precisa.
- Nessun blocco tecnico residuo. Eventuali ulteriori verifiche audio/visuali emerse durante la semantica possono essere richieste a Codex secondo `system/HANDOFFS.md`.
