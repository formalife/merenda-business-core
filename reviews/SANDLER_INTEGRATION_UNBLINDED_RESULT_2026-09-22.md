# Sandler Integration — Unblinded Behavioral Result — 2026-09-22

## Stato

**UNBLINDED — MERGE GATE STILL CLOSED**

Judgment blinded congelato in:

- `reviews/SANDLER_INTEGRATION_BLINDED_JUDGMENT_2026-09-22.md`
- `reviews/SANDLER_INTEGRATION_BLINDED_JUDGMENT_2026-09-22.jsonl`

Suite testata: `R031–R041`  
Head su cui sono stati generati i trace: `21081371299f4bcbcc47227be7e9ded9c6373abd`

## Mapping rilevante dopo unblinding

- R033: A = `sandler_a3_full`, B = `sandler_a3_kernel`
- R041: A = `sandler_a3_full`, B = `sandler_a3_kernel`

Gli unici due material failure del judgment blinded erano R033-B e R041-B.

Quindi:

- **FULL = 11/11 behavioral PASS**
- **KERNEL = 9/11 behavioral PASS**
- FULL material failures = 0
- KERNEL material failures = 2
- provenance failures = 0 per entrambe le configurazioni

## Gate deterministico già noto

Entrambe le configurazioni avevano:

- required semantic recall = 1.0000
- full recall cases = 11/11

Precisione diagnostica:

- FULL = 0.6126
- KERNEL = 0.6318

La precisione più alta del Kernel non compensa i due failure comportamentali: il problema non è quantità di retrieval ma applicazione/causal discipline.

## Failure 1 — R033 Kernel

Caso: surface problem → demo prematura.

Il Kernel:

- riconosce e approfondisce il Pain;
- ma autorizza poi una demo selettiva senza rendere necessari anche Budget e Decision prima del Fulfillment.

Judgment congelato:

- `premature_tactic = true`
- `material_failure = true`
- `failure_category = CORRECT_RETRIEVAL_BAD_SYNTHESIS`

Il Full passa lo stesso caso.

## Failure 2 — R041 Kernel

Caso: cliente soddisfatto → upsell automatico.

Il Kernel:

- distingue soddisfazione da valore realizzato;
- richiede un nuovo bisogno reale;
- ma passa dalla nuova opportunity alla proposta senza rendere esplicito il rientro nella qualification commerciale completa, inclusi investimento/risorse e decision process.

Judgment congelato:

- `premature_tactic = true`
- `material_failure = true`
- `failure_category = CORRECT_RETRIEVAL_BAD_SYNTHESIS`

Il Full passa lo stesso caso.

## Interpretazione provvisoria

Questo è esattamente lo scenario `FULL PASS + KERNEL FAIL` previsto dal merge gate.

**Non basta però per modificare immediatamente `REASONING_KERNEL.md`.**

Prima va verificato sui trace dei due casi:

1. quali semantic unit il Kernel ha selezionato;
2. quali unit sono state canonicalmente verificate;
3. se Pain/Budget/Decision e lifecycle→requalification erano effettivamente presenti nel contesto letto;
4. quali control-plane cues il Full ha applicato e il Kernel no;
5. se la differenza è spiegata da bootstrap compression oppure da synthesis stochastic failure non strutturale.

Solo se emerge una omissione causale ripetibile del Kernel è autorizzato un kernel change.

## Decisione corrente

- doctrine specialistica: **non modificare**
- semantic map: **non modificare ancora**
- manuale: **non modificare**
- `REASONING_KERNEL.md`: **HOLD — trace diagnosis required**
- PR #16: **KEEP DRAFT — DO NOT MERGE**

Qualunque modifica successiva a doctrine/map/kernel/runner richiederà un nuovo full A/B completo sulla head finale.
