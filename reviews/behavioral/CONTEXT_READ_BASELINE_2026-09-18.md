# Context Read Baseline — Behavioral A/B

Date: 2026-09-18
Status: COMPLETE
Baseline commit tested: `4506e67e812c4e3270c4446d58f6a3d8c3934e82`
Measurement source: frozen behavioral workspaces and completed `EVAL_READER` commands under `/tmp/formalife-routing-baseline`.

## Measurement boundary

This report reconstructs the text returned by successful `EVAL_READER` operations during the frozen behavioral baseline.

It includes:

- control-plane files read through the evaluation reader;
- Retrieval Map metadata reads;
- specialist doctrine reads;
- other repository text read through the evaluation reader.

It does **not** claim exact API-billed model tokens. System prompt, tool protocol text, command/result wrappers, repository list output and other model runtime tokens are outside this deterministic reconstruction.

Eight failed/incomplete command variants were skipped and are not counted as successful context consumption.

## Aggregate result

| Metric | `current` | `current_plus_map` | Delta plus-map vs current |
|---|---:|---:|---:|
| Cases | 30 | 30 | — |
| Mean read operations | 15.20 | 15.67 | +0.47 |
| Mean reconstructed chars/case | 130,511 | 137,128 | **+6,617 (+5.1%)** |
| Mean reconstructed words/case | 17,766 | 17,222 | **−544 (−3.1%)** |
| Mean control-plane chars/case | 92,751 | 91,985 | −766 (−0.8%) |
| Mean routing-metadata chars/case | 0 | 17,337 | +17,337 |
| Mean specialist-doctrine chars/case | 27,136 | 20,589 | **−6,546 (−24.1%)** |
| Mean other chars/case | 10,625 | 7,217 | **−3,407 (−32.1%)** |

Total reconstructed category chars across all 30 cases:

| Category | `current` | `current_plus_map` |
|---|---:|---:|
| control plane | 2,782,525 | 2,759,546 |
| routing metadata | 0 | 520,107 |
| specialist doctrine | 814,071 | 617,678 |
| other | 318,736 | 216,512 |

## Interpretation

### RESULT 1 — The Map improves selectivity but is currently too expensive as a runtime representation

`current_plus_map` reduces specialist-doctrine reading by **196,393 chars across 30 cases (−24.1%)** and reduces `other` reading by **102,224 chars (−32.1%)**.

This is consistent with the semantic unblinding result: the Map acts as a useful precision / discovery signal.

However, the current experiment exposes the Map as relatively large JSON shards. Routing metadata adds **520,107 chars** across 30 cases, more than the specialist/other context savings it creates. Net reconstructed context therefore rises by **198,511 chars**, or about **5.1%**.

### RESULT 2 — Do not load the full Map at runtime

The economic failure is not that causal routing metadata has no value. The failure is the delivery mechanism: loading broad Map shards before knowing the exact semantic candidates is too expensive.

Prototype A should therefore make the Map **addressable**, not globally preloaded.

The intended pattern is:

`compact semantic index → candidate IDs → fetch only selected routing entries → canonical section → conditional expansion`.

### RESULT 3 — Bootstrap tax dominates the measured context

The control plane contributes roughly **92k reconstructed characters per case** in both configurations. This is materially larger than specialist doctrine and routing metadata separately.

The current test was intentionally designed with the full bootstrap fixed, so this does not invalidate the retrieval comparison. It does establish that the later Compact Reasoning Kernel experiment has potentially large economic upside.

Do not optimize bootstrap before Prototype A is stable: otherwise retrieval quality and bootstrap effects become confounded.

### RESULT 4 — Character and word metrics diverge

`current_plus_map` uses about **5.1% more characters** but **3.1% fewer words** overall.

This indicates that exact token economics cannot be inferred reliably from characters alone. The next behavioral harness should also capture model-reported input/cached/output tokens when available.

For architecture work, reconstructed chars/words remain useful as deterministic attribution metrics: they tell us *which layer* consumed the context.

## Decision

### DECISION — Prototype A must not preload the Retrieval Map

Map v1 remains useful experimental routing metadata, but Prototype A must access entries selectively.

### DECISION — Prototype A context target

Before testing a Compact Reasoning Kernel, Prototype A should target:

- semantic required-check recall ≥ strongest baseline observed (`95/96` on this suite);
- no material/epistemic regression;
- specialist-doctrine reads ≤ `current_plus_map` baseline where possible;
- routing metadata substantially below the current **17,337 chars/case** mean;
- total non-bootstrap reconstructed context no greater than `current` unless semantic fidelity materially improves.

The full-bootstrap control-plane cost remains fixed during this comparison.

## Next action

1. complete manually reviewed semantic-unit gold v2;
2. build an addressable compact semantic index from curated Map metadata + Structural Index;
3. implement Hierarchical Retriever Prototype A without embeddings;
4. instrument per-entry metadata reads, section reads and expansions;
5. A/B against frozen `current` and `current_plus_map` behavioral baselines;
6. only after retriever stabilization, test Compact Reasoning Kernel against the ~92k chars/case bootstrap tax.
