# Acquisition Progress

Ultimo aggiornamento: 2026-09-15T10:32:17.323415+00:00

Batch: 3 video
Completati tecnicamente: 3/3

| # | Video ID | Titolo | Stato | Nota |
|---:|---|---|---|---|
| 1 | -6TU0HZ8cQo | Come Rendere La Tua Azienda Ricca e Inattaccabile Dai Concorrenti | ACQUIRED | Metadata + transcript Markdown disponibili. |
| 2 | Nk5BZqfkO-A | Il Sistema Di Offerte Spilla Soldi Mai Rivelato Dalle Big Company | ACQUIRED | Metadata + transcript Markdown disponibili. |
| 3 | RNsDovlfwK8 | L'unico Sistema Valido E Testato Per Guidare Un'Azienda Che Guadagna Davvero | ACQUIRED | Metadata + transcript Markdown disponibili. |

## Dettaglio fase 7 — final probe 311–313

Branch: `acquisition-final-probe-311-313`. Canale verificato per tutti e tre: `UCaAzr7bvYcZRfGR8EyBynOA`.

| ID | Sottotitoli | Provenienza | Segmenti MD | Durata info.json | Ultimo timestamp MD | ASR | Errori | Keyframe |
|---|---|---|---|---|---|---|---|---|
| -6TU0HZ8cQo | nessuna traccia manuale; `it-orig` disponibile | auto (it-orig) | 586 | 1249s | 00:20:34 | non necessario | nessuno | nessuno acquisito (nessuna decisione semantica in questa fase) |
| Nk5BZqfkO-A | nessuna traccia manuale; `it-orig` disponibile | auto (it-orig) | 604 | 1540s | 00:25:36 | non necessario | nessuno | nessuno acquisito |
| RNsDovlfwK8 | nessuna traccia manuale; `it-orig` disponibile | auto (it-orig) | 850 | 2356s | 00:39:01 | non necessario | nessuno | nessuno acquisito |

Nessuna traccia sottotitoli "manuale" risultava disponibile per nessuno dei tre (`subtitle_languages` vuoto in tutti e tre gli `info.json`); usata `it-orig` (automatic caption in lingua originale) come da regola di fallback. Nessuna ASR necessaria perché `it-orig` era utilizzabile in tutti e tre i casi.

Coverage/delta: per tutti e tre il timestamp finale del transcript Markdown è entro pochi secondi dalla durata dichiarata in `info.json` (outro musicale finale), nessun gap significativo rilevato.

Keyframe: non estratti in questa fase — la selezione richiede analisi semantica del contenuto (slide/tabelle/grafici/schemi), riservata alla fase 8–13 (ChatGPT).

Validator: baseline 841 righe (`/tmp/validator-before-311-313.txt`, atteso 842 — scostamento di 1 riga preesistente, non causato da questa acquisizione); post-acquisizione confrontato in `STATUS.md`.
