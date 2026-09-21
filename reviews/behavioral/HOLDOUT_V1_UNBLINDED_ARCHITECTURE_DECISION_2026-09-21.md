# Holdout v1 — Unblinded Architecture Decision

Date: 2026-09-21
Status: FROZEN AFTER BLIND JUDGMENT

## Evidence order

1. Six-case holdout H001–H006 was frozen before execution.
2. Both variants were run on the same prompts with no holdout gold in the sterile workspace.
3. A/B identity was randomized per case.
4. Answers were judged blind before the mapping was revealed.
5. Blind result: A = 18/18 required checks, B = 18/18; 6/6 full-pass cases for both; zero material decision inversions, forbidden shortcuts, unsupported inference or premature tactics.
6. Only after that judgment was frozen was the mapping revealed.

## Unblinded mapping

| Case | A | B |
|---|---|---|
| H001 | full bootstrap | Compact Reasoning Kernel |
| H002 | Compact Reasoning Kernel | full bootstrap |
| H003 | full bootstrap | Compact Reasoning Kernel |
| H004 | full bootstrap | Compact Reasoning Kernel |
| H005 | full bootstrap | Compact Reasoning Kernel |
| H006 | full bootstrap | Compact Reasoning Kernel |

Because both blind variants scored 18/18, the unblinded result is:

- **A3 + full bootstrap: 18/18 required checks, 6/6 full-pass.**
- **A3 + Compact Reasoning Kernel v1: 18/18 required checks, 6/6 full-pass.**
- **Observed decision-fidelity delta on holdout: 0.**

## Context economics

Reported paired-run means:

- full bootstrap architecture: **120,116 reconstructed chars/case**;
- Compact Kernel architecture: **34,288 reconstructed chars/case**;
- total-context delta: **−71.5%**.

The prior zero-Codex setup validation measured the fixed control plane itself at:

- five full control-plane files: **89,192 chars**;
- Compact Reasoning Kernel v1: **11,324 chars**;
- kernel/full fixed-control ratio: **0.127**;
- fixed-bootstrap reduction: **~87.3%**.

These reconstructed-character measures are instrumentation proxies, not billed-token measurements, but the difference is large enough to be architecturally material.

## Decision

**ADOPT the Compact Reasoning Kernel v1 as the current control-plane candidate for strategic/diagnostic bootstrap on the Architecture Review branch.**

Operational meaning:

1. Default strategic/diagnostic bootstrap becomes `REASONING_KERNEL.md`, not the five full control-plane documents.
2. Canonical specialist doctrine remains authoritative and is retrieved progressively for material decisions.
3. The full `LAYER1_CONTRACT.md`, `FORMALIFE_REBUILD_PROTOCOL.md`, `MERENDA_MODE.md`, `merenda/DECISION_ROUTER.md` and `merenda/00_fondamenti/sistema-operativo-merenda.md` remain canonical governance/reference documents and fallback material; they are not deleted.
4. The compact semantic index remains a routing signal, not an exclusive filter.
5. Structural discovery remains the recall safety net.
6. Do not run the 30 development cases merely to improve confidence cosmetically. They remain a regression suite for future material architecture changes.
7. Do not further compress the kernel without a new paired evaluation; the validated artifact should be changed only when the expected gain is material.

## What this result does and does not prove

It is strong evidence that the validated hierarchical retriever + Compact Kernel preserves decision quality on a blind six-case holdout while materially reducing context consumption.

It does not prove universal equivalence for every future business question. Residual risk should be managed operationally through:

- specialist-doctrine retrieval for material decisions;
- explicit fallback to full control-plane documents when the kernel is insufficient;
- logging new failure classes as future regression cases;
- re-running expensive evaluation only after material architecture changes.

## Next architecture work

No more Codex-heavy retrieval tuning is justified now.

Highest-value remaining work is non-Codex stabilization:

1. promote the validated kernel to the root control plane;
2. update startup/ChatGPT routing to use progressive disclosure;
3. keep full control-plane documents as fallback/audit references;
4. resolve the historical/current governance conflict in frozen files as a separate explicitly authorized cleanup;
5. after merge, update Layer 2 bootstrap references so Formalife operational chats use the compact bootstrap by default.
