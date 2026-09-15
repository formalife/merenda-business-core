# PROJECT STATUS

## Stato generale

ACTIVE — contenuti **1–310 processati semanticamente**. La KB Merenda è in **fase finale di saturazione**.

## Risultato 301–310

- novelty binaria: **7/10 = 70%**
- Weighted Novelty: **9/20 = 45%**
- nuovi framework peso 2: exit readiness; controlli interni/rischio operativo

## Rivalutazione RESERVE post-310

I 12 RESERVE sono stati rivalutati contro la KB aggiornata.

Esito:
- **3 FINAL PROBE**
- **9 DEFER**

Final probe:
1. `-6TU0HZ8cQo` — difendibilità/moat
2. `Nk5BZqfkO-A` — architettura offerte
3. `RNsDovlfwK8` — sistema integrato di governo

Report: `reviews/RESERVE_REASSESSMENT_POST_310.md`.

## Corpus

- totale: **468**
- STUDIATO: **304**
- ESCLUSO: **6**
- DA STUDIARE: **158**
- semanticamente processati: **310**

## Acquisizione tecnica 311–313 (fase 7, final probe)

Branch: `acquisition-final-probe-311-313` (pushato, non mergiato su `main`).

- 3 tentati, 3 ACQUIRED: `-6TU0HZ8cQo`, `Nk5BZqfkO-A`, `RNsDovlfwK8`.
- Channel ID verificato `UCaAzr7bvYcZRfGR8EyBynOA` per tutti e tre.
- Sottotitoli: nessuna traccia manuale disponibile per nessuno dei tre; usata `it-orig` (automatic caption lingua originale) come da fallback. Nessuna ASR necessaria.
- Nessun errore, nessun NO_IT_TRANSCRIPT.
- Coverage/delta: timestamp finale del Markdown entro pochi secondi dalla durata dichiarata in `info.json` per tutti e tre (outro musicale), nessun gap rilevante.
- Keyframe: nessuno estratto — decisione riservata alla revisione semantica (fase 8–13).
- Validator: baseline pre-acquisizione 841 righe (atteso 842, scostamento preesistente di 1 riga non causato da questa fase); nessuna nuova voce di errore rilevante introdotta dall'acquisizione (dettaglio nel diff conservato in `/tmp/validator-before-311-313.txt` / `/tmp/validator-after-311-313.txt`).
- Invarianti rispettati: 1–310 invariati, nessuna modifica a `merenda/`, `.review.md`, `sources/catalog.json`, `sources/VIDEO_INDEX.md`, `sources/queue/QUEUE.md`, `reviews/RESERVE_REASSESSMENT_POST_310.md` o file frozen; nessuna analisi semantica eseguita; nessun video marcato STUDIATO/ESCLUSO; nessun contenuto 314+ toccato.

## Next Action

**Agente richiesto: CHATGPT.**

**Prossima azione: revisione semantica 311–313 + Weighted Novelty finale.**

Dopo la review dei tre:
- se nessun peso 2 e Weighted Novelty ≤2/6 → dichiarare KB Merenda sufficientemente satura e aprire lo strato esterno/evidence;
- se emerge un nuovo framework peso 2 → seguire solo il gap specifico.

**Non acquisire 314+. Non tornare a batch sequenziali.**
