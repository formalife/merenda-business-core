# PROJECT STATUS

## Stato generale

ACTIVE — fasi 1–6 complete; primi 100 contenuti processati semanticamente; checkpoint 100 raggiunto.

## Fase corrente

**CHECKPOINT 100 — richieste FASE 14 + FASE 15 con CLAUDE CODE.**

## Corpus

- Video individuati: 468
- Contenuti processati: 100
- STUDIATO / integrati nella KB: 96
- ESCLUSO dalla dottrina attiva: 4
- Da processare: 368
- Corpus completo: NO

## Workflow attivo — v1.1

- CODEX / script locale: acquisizione tecnica a batch.
- CHATGPT: revisione semantica e fasi 8–13.
- CLAUDE CODE: fase 14 ogni 25; fase 14 + 15 ogni 50.

## Checkpoint

- Ultimo refactor KB completato: 75
- Refactor richiesto ora: **SÌ — fase 14**
- Ultimo audit tassonomia: 50
- Audit tassonomia richiesto ora: **SÌ — fase 15**
- Prossimo checkpoint dopo questo: 125 (fase 14)
- Checkpoint Claude richiesto: **SÌ**

Handoff dettagliato: `reviews/CHECKPOINT_100.md`.

## Agente richiesto

**CLAUDE CODE**

## Next Action

Leggere:

1. `00_START_HERE.md`
2. `CLAUDE.md`
3. `MASTER_PLAN.md`
4. `system/RULES.md`
5. `system/PHASES.md`
6. `system/HANDOFFS.md`
7. `reviews/CHECKPOINT_100.md`
8. `STATUS.md`

Poi eseguire, in ordine:

1. **FASE 14 — refactor KB**
2. **FASE 15 — audit globale della tassonomia**

Non introdurre nuova dottrina.

Al termine:

- aggiornare `reviews/CHECKPOINT_100.md`;
- aggiornare `STATUS.md`;
- verificare routing/link/anchor;
- commit e push su `origin/main`;
- poiché la fase 15 può riordinare la queue, impostare il prossimo agente tecnico solo sulla queue risultante dall'audit.

## Primo pendente prima dell'audit

`zZFg2oM208w` — *Come Fare Marketing: 3 Passi Chiave Per Trovare Clienti Top* — `04_marketing`.

Asset tecnici 101+: non presenti per i primi video controllati.

## Blocchi

Nessun blocco semantico aperto sui primi 100 contenuti.

**Importante:** non avviare acquisizione 101–125 in parallelo prima della conclusione della fase 15.
