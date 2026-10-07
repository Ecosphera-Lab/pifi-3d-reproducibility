# PIFI-3D Reproducibility Package

Public reproducibility snapshot for the manuscript

**An Exactly Solvable Family of Routed Rotation Systems with Observation-Dependent Future Quotients**

Author: **Maks Katsubo**  
Organization: **Ecosphera-Lab**

## What this release contains

This v0.6 snapshot is intentionally narrow. It reproduces the frozen family-classification chain

[
\mathcal T_{n;\delta,c_{AB},c_{BC}}
\to
s=2(\delta+c_{AB}+c_{BC})
\to
\mathcal A(q,s)
\to
(Q,k_{\min},\text{routing census})
]

followed by

[
\text{component-aware observation}
\to
\text{decorated macro orbits}
\to
\text{affine placement}
\to
\text{CRT prime-power classification}.
]

The original PIFI point is

[
n=12,\qquad
(\delta,c_{AB},c_{BC})=(1,1,1),
]

with

[
Q=52,\qquad k_{\min}=13,
]

and primitive periods (8,12,12,20).

## Repository layout

- `paper/` — consolidated LaTeX manuscript v0.6;
- `tools/` — frozen exact verifiers;
- `results/` — frozen machine-readable certificates;
- `docs/` — theorem/audit documents;
- `run_all.py` — one-command reproduction chain;
- `CLAIM_BOUNDARY.md` — exact scope and nonclaims;
- `PUBLIC_RELEASE_MANIFEST_v0_6.json` — release whitelist.

## Quick reproduction

Python 3.11+ is recommended.

```bash
python run_all.py
```

The verifier chain is standard-library Python only. Each newly produced certificate is strictly parsed and checked before the runner can report PASS.

For manuscript compilation:

```bash
cd paper
latexmk -pdf -file-line-error -halt-on-error -interaction=nonstopmode main.tex
```

## Novelty boundary

The general machinery of rotation systems, symbolic/future equivalence,
primitive cyclic words, affine actions and CRT is established prior art.

The candidate contribution is the **exact solvability and integrated arithmetic
classification of the explicitly defined routed family**.

Current wording:

> **Not located in the targeted prior-art pass; not yet a global novelty claim.**

See `docs/PIFI_3D_SPECIALIST_NOVELTY_LITERATURE_AUDIT_v0_1.md`.

## Release status

**v0.6 publication-grade consolidation candidate.**

This branch is intended to be validated from a clean checkout before merge/tag.
