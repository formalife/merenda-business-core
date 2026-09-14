# PROJECT STATUS

## Stato generale

ACTIVE — fasi 1–6 complete; contenuti **1–225 processati semanticamente**. Checkpoint **225 completato (FASE 14 eseguita da Claude Code)**. Corpus ancora incompleto.

## Fase corrente

Checkpoint **225 — FASE 14 completata**. Nessuna modifica strutturale a `merenda/` è stata necessaria (KB già ben integrata dal batch 201–225). Report definitivo in `reviews/CHECKPOINT_225.md`. FASE 15 non eseguita (non dovuta fino a 250).

## Corpus

- Video individuati: 468
- Contenuti processati semanticamente: **225**
- STUDIATO / integrati o deduplicati: **219**
- ESCLUSO dalla dottrina attiva: **6**
- Da processare: **243**
- Corpus completo: NO
- Batch tecnico 201–225: **25/25 utilizzabili**
- Elaborazione semantica 201–225: **25/25**
- Review 201–225: **25**
- Transcript mancanti nel batch: 0
- Fallback ASR nel batch: 0
- Errori finali tecnici: 0
- Pending tecnici: 0

## Novelty 201–225

- Incrementali: **6/25 = 24%**
- Incrementali: 201 `vD7zMl6YXzs`, 211 `WtyLO1gMqVI`, 212 `TrY_mDjr7I4`, 216 `of0ppir9sq4`, 220 `HwlqYf73Ctk`, 225 `WCP26HC6wd0`
- Deduplicati senza modifica KB: **19/25**
- Nessun nuovo ESCLUSO

Nota workflow: il 225 era classificato C/FAST perché short ma ha prodotto novità prevalente del 2025. C resta fast review, mai skip. La recenza è stata studiata come possibile segnale automatico per il classificatore: `upload_date` in `sources/catalog.json` è assente per 0/46 degli short residui (compreso lo stesso 225), quindi non è utilizzabile come filtro automatico. È stata invece aggiunta a `reviews/RESIDUAL_CLASSIFICATION_201-468.md` e a `scripts/classify_residual.py` una regola esplicita di promozione manuale per recenza durante la FAST REVIEW (verificare la data reale su YouTube, promuovere C→B/A se la data è successiva alla fonte canonica già in KB). Dettagli in `reviews/CHECKPOINT_225.md`.

## Workflow attivo — v1.1

- CODEX: acquisizione tecnica e supporto meccanico.
- CHATGPT: revisione semantica e fasi 8–13.
- CLAUDE CODE: FASE 14 ogni 25; FASE 14 + 15 ogni 50.
- Classificazione A/B/C: strumento di priorità/profondità, non sostituisce la revisione completa di ogni contenuto.
- Nessuna modifica al workflow frozen.

## Checkpoint

- Ultimo refactor KB completato: **225**
- Ultimo audit tassonomia completato: **200**
- Refactor KB dovuto: **250 — FASE 14** (insieme a FASE 15)
- Audit tassonomia dovuto: **250 — FASE 14 + FASE 15**
- Checkpoint Claude richiesto ora: **NO**
- Report checkpoint corrente: `reviews/CHECKPOINT_225.md` (definitivo)

## Agente richiesto

**CODEX**

## Next Action

Acquisizione tecnica del batch **226–250** (fase 7: transcript, eventuale fallback ASR, keyframe candidati dove segnalato). Nessun asset tecnico 226+ è presente in `sources/transcripts/`. Primo contenuto: `226 — m53_BsS_x8U`.

Dopo l'acquisizione, Codex restituisce il controllo a ChatGPT via `STATUS.md` secondo `system/HANDOFFS.md`, per l'elaborazione semantica (fasi 8–13) fino al prossimo checkpoint Claude (dovuto a 250: FASE 14 + FASE 15).

## Validazione e limiti

- Baseline validator certa: **841 warning storici**, identici dal checkpoint 200 al checkpoint 225 (nessuna nuova anomalia).
- Il connettore GitHub usato da ChatGPT non esegue il validator sul working tree locale: Claude verifica baseline e post-refactor a ogni checkpoint.
- Checkpoint 225: nessuna modifica strutturale a `merenda/`; modificati solo `scripts/classify_residual.py` e `reviews/RESIDUAL_CLASSIFICATION_201-468.md` (documentazione della regola di promozione per recenza, nessuna modifica alla logica di classificazione).
- **218 — `JQXoKKwneBQ`**: testo semanticamente utilizzabile; timestamp/visuali nella parte disallineata non usati come evidenza precisa.
- Nessun contenuto 226+ processato semanticamente o acquisito tecnicamente.
