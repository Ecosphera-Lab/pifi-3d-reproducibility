# PIFI-3D Reproducibility Package

Public reproducibility package for the research manuscript

**From PIFI Geometry to a 52-State Future Quotient: A C4-Equivariant Routed-Voltage Construction**

Author: **Maks Katsubo**  
Organization: **Ecosphera-Lab**

## Purpose

This repository is the curated public reproducibility release for the finite mathematical claims of the PIFI-3D study. It is intentionally narrower than the private research repository.

The main proof chain is

[
	ext{geometry}
	o
	ext{exact split / local rotation system}
	o
O,U,R3,C3,C6,C20,T(C)
	o
8,12,12,20
	o
52
	o
	ext{fiber-return / voltage / }V_4
	o
	ext{finite controls}.
]

The current manuscript also proves a local family theorem: after scale normalization, the PIFI realization lies inside a nonempty open two-parameter radial-shell realization chamber with the same labelled split rotation system and the same decorated routed dynamics.

## Claim boundary

This package supports exact finite claims for the frozen construction and its proved local radial-shell realization family.

It does **not** claim:

- a continuum physical law;
- global uniqueness among all routed-voltage systems;
- that the full parameter domain `0 < a < b < 1` is one realization chamber;
- novelty of standard voltage/gain graph, automata, switching, or graph-cohomological machinery;
- publication priority.

## Layout

- `paper/` — manuscript source, bibliography, figures and supplements.
- `results/` — frozen machine-readable certificates.
- `audits/` — human-readable derivation and claim-boundary audits.
- `tools/` — exact verifier and dependency scripts.
- `visualizations/` — canonical geometric source.
- `REPRODUCE.md` — commands and expected outputs.
- `CITATION.cff` — citation metadata.

## Release status

**v0.5 family-generalization candidate.**

The broader research repository remains private. This repository contains only material needed to inspect and reproduce the paper's finite mathematical claims.
