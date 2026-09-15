# PROJECT STATUS

## Stato generale

ACTIVE — fasi 1–6 complete; contenuti **1–300 processati semanticamente**. Il batch ottimizzato **276–300 è chiuso semanticamente** sul branch `semantic-276-300`. Il checkpoint **300 richiede ora CLAUDE CODE — FASE 14 + FASE 15**. Corpus Merenda ancora non dichiarato completo.

## Fase corrente

Revisione semantica **276–300 completata da ChatGPT**: 25/25 review, 25/25 STUDIATO, nessun nuovo ESCLUSO.

Weighted Novelty del batch:

- peso 2: **4**
- peso 1: **9**
- peso 0: **12**
- totale pesato: **17/50**
- contenuti realmente incrementali: **13/25 = 52%**

Il batch conferma che la riprioritizzazione per information gain ha ancora rendimento sufficiente, ma non autorizza a processare automaticamente tutti i residui: la decisione successiva spetta al checkpoint 300 dopo FASE 14 + FASE 15.

## Corpus

- Video individuati: **468**
- Contenuti processati semanticamente: **300**
- STUDIATO / integrati o deduplicati: **294**
- ESCLUSO dalla dottrina attiva: **6**
- Da processare: **168**
- Corpus completo: NO
- 301 — `asMedYJtd4I` resta **DA STUDIARE**
- Nessun contenuto 301+ processato semanticamente in questo batch

## Nuovi nodi canonici

1. `merenda/07_copy_comunicazione/copy-posizionamento-e-temperatura-traffico.md`
2. `merenda/08_brand/reputazione-e-crisis-management.md`
3. `merenda/09_business/retention-onboarding-e-customer-success.md`

Altri contenuti incrementali sono stati fusi nei nodi esistenti secondo MERGE, NOT APPEND.

## Novelty recente

- Batch 226–250: **16/25 = 64%**
- Batch 251–275: **11/25 = 44%**
- Batch ottimizzato 276–300: **13/25 = 52%**, Weighted Novelty **17/50**

L'information gain è risalito rispetto al batch precedente, ma una parte rilevante del materiale selezionato resta già assorbita da fonti più recenti. Il prossimo passo non è ancora un nuovo batch: prima va eseguito l'audit globale del checkpoint 300.

## Validazione attesa

La baseline tecnica era **842 warning storici**: 836 `Ordine/stato incoerente`, 3 `File congelato modificato`, 3 `Contatore STATUS errato`.

La revisione semantica aggiorna stato/categoria per ID senza riallineare fuori scope l'ordine storico di catalogo/VIDEO_INDEX/queue. I file frozen non vengono modificati.

## Workflow attivo

- CODEX: acquisizione tecnica.
- CHATGPT: revisione semantica e fasi 8–13.
- CLAUDE CODE: FASE 14 ogni 25; FASE 14 + FASE 15 ogni 50.
- A/B/C = profondità di review.
- Information Priority = ordine adattivo di acquisizione.
- C = FAST REVIEW, mai SKIP.

## Checkpoint

- Ultimo refactor KB completato: **275 — FASE 14**
- Ultimo audit tassonomia completato: **250 — FASE 15**
- Soglia semantica raggiunta: **300**
- Checkpoint richiesto ora: **CLAUDE CODE — FASE 14 + FASE 15**

## Agente richiesto

**CLAUDE CODE**

## Next Action

Eseguire il checkpoint **300 — FASE 14 + FASE 15**.

Claude deve refactorare la KB con MERGE, NOT APPEND, auditare tassonomia e saturazione residua, verificare in particolare i tre nuovi nodi del batch e stabilire se il rendimento **13/25 = 52%, Weighted 17/50** giustifica un altro batch TARGETED o se conviene restringere ulteriormente ai gap.

**Non acquisire né processare semanticamente 301+ durante il checkpoint.**
