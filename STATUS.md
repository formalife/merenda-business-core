# PROJECT STATUS

## Stato generale

ACTIVE — fasi 1–6 complete; contenuti **1–275 processati semanticamente**. Checkpoint **275 chiuso**. **Batch tecnico ottimizzato 276–300 completato** sul branch `acquisition-276-300`, dalla base canonica `81b0829bf99427ae5c46db8f33346fdab3d6c8ef`. Nessun merge su main. Corpus ancora incompleto.

## Fase corrente

**FASE 7 — acquisizione tecnica 276–300 completata.** 25/25 ACQUIRED, 25 transcript utilizzabili: **2 italiani manuali e 23 automatici it-orig**, nessun fallback ASR, NO_IT_TRANSCRIPT, ERROR finale o PENDING. Metadata del canale ufficiale verificati; confronto integrale JSON3↔Markdown e copertura temporale verificati; keyframe selettivi e limiti nel report tecnico.

Report: `sources/queue/acquisition-progress.md`. `sources/queue/next-batch.txt` contiene esattamente i 25 URL 276–300 nel nuovo ordine.

## Corpus

- Video individuati: **468**
- Contenuti processati semanticamente: **275**
- STUDIATO / integrati o deduplicati: **269**
- ESCLUSO dalla dottrina attiva: **6**
- Da processare: **193**
- Corpus completo: NO
- Batch 276–300 tecnicamente pronto: **25**, ancora tutti **DA STUDIARE**
- **Nessun contenuto marcato STUDIATO o ESCLUSO in questa task. Semantica ferma a 275.**

## Ordine operativo e limite

Fonte operativa: `reviews/RESIDUAL_REPRIORITIZATION_276-468.md`.
Nuovo batch: 15 MUST STUDY + 10 TARGETED, selezione verificata programmaticamente 25/25.
La vecchia `reviews/RESIDUAL_CLASSIFICATION_201-468.md` resta storica.
STOP tecnico a **300**; nessuna acquisizione del nuovo 301 o successivi.

## Validazione

Validator prima/dopo: **842 warning storici**, output identico:
836 `Ordine/stato incoerente`, 3 `File congelato modificato`, 3 `Contatore STATUS errato`.
Nessun riallineamento di catalogo o VIDEO_INDEX. Frozen, KB, review esistenti, queue, riprioritizzazione e script invariati. Nessuna nuova `.review.md`.

## Workflow attivo

- CODEX: acquisizione tecnica e supporto meccanico.
- CHATGPT: revisione semantica e fasi 8–13.
- CLAUDE CODE: FASE 14 ogni 25; FASE 14 + 15 ogni 50.
- L’acquisizione non equivale a completamento semantico.

## Checkpoint

- Ultimo refactor KB completato: **275 — FASE 14**
- Ultimo audit tassonomia completato: **250 — FASE 15**
- Prossimo checkpoint Claude: **300 — FASE 14 + FASE 15**
- Checkpoint Claude richiesto ora: **NO**

## Agente richiesto

**CHATGPT**

## Next Action

**Revisione semantica 276–300, fasi 8–13 + Weighted Novelty.**
Iniziare da **276 — `KipX0tAAWr4`**, terminare con **300 — `Fo8PB_7fE60`**.

La semantica è ancora ferma a **275**. Dopo la revisione, passare a Claude per il checkpoint **300 — FASE 14 + FASE 15**.

Non decidere automaticamente il batch successivo: la decisione dopo 300 dipenderà dalla **Weighted Novelty** misurata nella fase semantica, secondo il report di riprioritizzazione. Nessuna novelty analysis eseguita da Codex.
