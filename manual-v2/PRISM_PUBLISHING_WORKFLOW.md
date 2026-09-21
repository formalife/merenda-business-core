# Prism / LaTeX Publishing Workflow — Manual V2

Status: **CANDIDATE WORKFLOW — FOUNDER REVIEW PENDING**  
Date: 2026-09-21

## Goal

Use Prism/LaTeX to produce a high-quality, reproducible book layout without allowing the publishing environment to become a second source of truth for manuscript content.

---

# Canonical boundary

## GitHub

Canonical for:

- manuscript content;
- editorial architecture;
- decisions;
- doctrine fidelity;
- prose revisions;
- version history;
- audit state.

## Prism / LaTeX

Publishing environment for:

- typography;
- page geometry;
- visual hierarchy;
- formula layout;
- tables;
- figures/charts;
- cross-references;
- glossary/index/bibliography machinery;
- print/PDF generation;
- production QA.

Prism must not silently become the canonical manuscript.

---

# Normal flow

1. Freeze a manuscript revision in GitHub.
2. Export/transform selected reader-facing content into the LaTeX publishing project.
3. Compile in Prism or a compatible local/CI LaTeX environment.
4. Perform editorial/visual QA on the PDF.
5. Classify findings:
   - layout-only;
   - visual asset;
   - content/editorial.
6. Layout-only findings remain in publishing source.
7. Content/editorial findings are fixed first in canonical GitHub manuscript.
8. Re-export/reconcile the publishing project.
9. Recompile and visually verify.

---

# Golden prototype

A Prism-importable LaTeX prototype has been built outside the canonical manuscript to test the production system.

It uses:

- pdfLaTeX-compatible TeX Live packages;
- 170 × 240 mm two-sided page geometry;
- Libertinus Serif body typography;
- Source Sans Pro navigation typography;
- `tcolorbox` components;
- TikZ diagrams;
- PGFPlots quantitative charts;
- chapter-local figure numbering;
- print-style recto chapter openings.

The prototype is intentionally self-contained so it can be imported into Prism as a folder/ZIP.

---

# Versioning discipline

Before full publishing production:

- tag/freeze the approved manuscript baseline;
- version the LaTeX template separately from the manuscript;
- record which manuscript commit a PDF release was built from;
- never reconcile manuscript differences manually from memory;
- do not make large content rewrites only inside Prism.

Recommended release metadata:

- manuscript commit SHA;
- publishing-template version/commit;
- build date;
- PDF checksum;
- QA result.

---

# Variant strategy

Prefer one semantic publishing source with controlled output variants rather than separate manually edited books.

Potential variants:

- print edition: recto Parts/Chapters, intentional blank versos;
- PDF/tablet edition: optional reduction of intentional blank pages;
- future ePub: content-first conversion, not fixed-layout PDF extraction.

Do not optimize the LaTeX source so heavily for print that the semantic structure becomes unusable for other formats.

---

# Founder gate

Do not migrate the full manual into the publishing layer until the Golden Production Test receives founder approval.

If approved:

1. freeze `EDITORIAL_DESIGN_BIBLE.md` as CURRENT;
2. promote the LaTeX template to production infrastructure;
3. define manuscript→LaTeX transformation rules;
4. resume Golden C under the approved content model;
5. begin full production waves only after Golden C also passes its content gate.
