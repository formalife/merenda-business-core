# Architecture Holdout v1 — Paired Generalization + Bootstrap Test

Date: 2026-09-20
Status: FROZEN BEFORE MODEL RUN

## Objective

Spend the next Codex credits only on information that can materially change the architecture decision.

The 30-case development suite is now primarily a regression suite because it informed semantic gold and multiple Prototype A patches. It remains useful later, but it is not the highest-information next test.

Holdout v1 therefore tests two unresolved questions at once:

1. **Generalization** — does Prototype A3 work on new cases that did not guide A1/A2/A3 tuning?
2. **Bootstrap compression** — can a compact reasoning kernel replace the five full control-plane reads without a material loss of decision fidelity?

## Cost design

Six new cases are run under two architectures:

- `holdout_a3_full` — A3 retrieval discipline + the existing five-file full bootstrap;
- `holdout_a3_kernel` — the same A3 retrieval discipline + `COMPACT_REASONING_KERNEL_V1.md` as the only fixed reasoning bootstrap.

Total planned model calls: **12**.

This is deliberately smaller than a 30-case regression run while answering a more valuable architectural question.

## Freeze rules

Before the first model call:

- holdout prompts and required checks are committed;
- Compact Reasoning Kernel v1 is committed;
- no new semantic units are added for the holdout cases;
- the current semantic registry, runtime patches, Structural Index and A3 discipline remain unchanged;
- both variants use the same model and reasoning effort;
- specialist doctrine under `merenda/` is identical in both variants.

No architecture patch may be made between the full-bootstrap and compact-kernel variants.

## Holdout composition

`evals/routing/holdout_v1.jsonl`

The six cases intentionally exercise doctrine not used as the direct tuning target of A1/A2/A3:

- crisis response vs internal control;
- earned media / notiziability;
- internal controls and segregation;
- current front-end doctrine and economics;
- customer-facing AI governance and deep-section retrieval;
- single-point-of-failure resilience vs retention of a high-value person.

The holdout does not add semantic registry entries before testing. Structural discovery must provide the safety net when the compact semantic map does not already expose the needed concept.

## Blind judgment

After both variants complete, the harness creates:

- `holdout-blind-answer-bundle.jsonl`
- `holdout-blind-mapping.json`

Per case, full vs kernel is randomly assigned to A/B locally at runtime.

Judgment order:

1. upload/judge only the blind answer bundle;
2. freeze required-check, shortcut, provenance and material-decision judgments;
3. only then reveal the A/B mapping;
4. only after unblinding inspect retrieval traces and context decomposition.

The mapping file must not be uploaded before blind judgment is frozen.

## Primary acceptance logic

The compact kernel is a viable replacement candidate only if, on the frozen holdout:

- it introduces **zero material decision inversions** relative to doctrine;
- it introduces no systematic epistemic/provenance regression;
- required-check fidelity is comparable to the full-bootstrap A3 variant;
- the retrieval architecture still finds specialist doctrine without depending on holdout-specific semantic entries;
- fixed control-plane context falls materially below the ~89k chars/case observed in Prototype A3.

Exact permanent thresholds are not defined from six cases. The test is a gate for whether kernel compression deserves broader regression testing.

## Decision after the test

If A3 fails badly on new cases under both bootstraps, stop kernel work and fix retrieval/generalization first.

If full A3 generalizes but kernel materially degrades reasoning, keep full bootstrap temporarily and redesign the kernel offline before spending more model calls.

If both generalize and kernel preserves fidelity while cutting context materially, freeze the retriever/kernel pair and use the existing 30 cases as a final regression suite only when the expected information value justifies the additional cost.

Do not tune on individual holdout cases and then continue calling the same set a holdout. Any post-holdout patch converts these six cases into regression cases; a future generalization test must use new frozen cases.
