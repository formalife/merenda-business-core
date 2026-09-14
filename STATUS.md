# PROJECT STATUS

## Stato generale

ACTIVE — fasi 1–6 complete; contenuti **1–225 processati semanticamente**. Batch 201–225 completato; checkpoint **225 raggiunto**. Corpus ancora incompleto.

## Fase corrente

Checkpoint **225 — FASE 14 dovuta**. Revisione semantica 201–225 completata su branch `semantic-201-225`.

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

Nota workflow: il 225 era classificato C/FAST perché short ma ha prodotto novità prevalente del 2025. C resta fast review, mai skip; la recenza va rivalutata nel classifier.

## Workflow attivo — v1.1

- CODEX: acquisizione tecnica e supporto meccanico.
- CHATGPT: revisione semantica e fasi 8–13.
- CLAUDE CODE: FASE 14 ogni 25; FASE 14 + 15 ogni 50.
- Classificazione A/B/C: strumento di priorità/profondità, non sostituisce la revisione completa di ogni contenuto.
- Nessuna modifica al workflow frozen.

## Checkpoint

- Ultimo refactor KB completato: **200**
- Ultimo audit tassonomia completato: **200**
- Refactor KB dovuto: **225 — FASE 14**
- Audit tassonomia dovuto: **250 — FASE 14 + FASE 15**
- Checkpoint Claude richiesto ora: **SÌ**
- Report checkpoint corrente: `reviews/CHECKPOINT_225.md`

## Agente richiesto

**CLAUDE CODE**

## Next Action

Eseguire **FASE 14 al checkpoint 225** sulla KB completa, partendo da `reviews/CHECKPOINT_225.md`.

Claude deve:

1. eseguire validator e `git diff --check` localmente prima del refactor;
2. rileggere tutta `merenda/`;
3. verificare merge/split/overlap/link/orfani/gerarchia con particolare attenzione ai cinque file KB modificati nel batch;
4. controllare la prevalenza della fonte recente 225 sul front-end;
5. valutare il falso negativo A/B/C del 225 e l'eventuale aggiornamento del classifier non-frozen;
6. non eseguire FASE 15;
7. non processare contenuti 226+;
8. rieseguire validator e `git diff --check` dopo le modifiche;
9. aggiornare questo STATUS e `reviews/CHECKPOINT_225.md` da pre-handoff a report definitivo.

## Validazione e limiti

- Baseline validator certa pre-semantica: **841 warning storici**, identici al checkpoint 200.
- Il connettore GitHub usato da ChatGPT non esegue il validator sul working tree locale: Claude deve verificare baseline e post-refactor.
- Diff semantico puro dal commit tecnico: **25 commit**, **25 review**, 5 file KB modificati, nessun frozen.
- **218 — `JQXoKKwneBQ`**: testo semanticamente utilizzabile; timestamp/visuali nella parte disallineata non usati come evidenza precisa.
- Nessun contenuto 226+ processato semanticamente.
