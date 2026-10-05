# PIFI-3D Reproducibility Package

Public reproducibility package for the manuscript

**From PIFI Geometry to a 52-State Future Quotient: A C4-Equivariant Routed-Voltage Construction**

Author: **Maks Katsubo**  
Organization: **Ecosphera-Lab**

## Purpose

This is a curated public release for the finite mathematical claims of the PIFI-3D study. The broader research repository remains private.

The principal chain is

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

The current manuscript also proves that the exact PIFI realization is not isolated: after scale normalization it belongs to a nonempty open two-parameter radial-shell realization chamber with the same labelled split rotation system and the same decorated routed dynamics.

## Current public-release state

The repository currently contains the public metadata and a **strict whitelist synchronizer**.

The scientific files are intentionally copied from the private research tree only through:

- `PUBLIC_RELEASE_MANIFEST.txt`
- `sync_public_release.ps1`

This makes accidental publication of unrelated private project material much less likely.

After the whitelist sync, the scientific tree preserves the source paths expected by the verifiers:

- `paper/pifi_3d/` — manuscript, figures and visual supplements;
- `docs/results/` — frozen machine-readable certificates;
- `docs/research/pifi_2d_square_ca/` — selected human-readable audits/theorems;
- `tools/` — exact verifier and control scripts;
- `visualizations/v13_r90_validation/` — canonical geometry source.

See `REPRODUCE.md` for execution order.

## Claim boundary

This package supports exact finite claims for the frozen construction and its proved local radial-shell realization family.

It does **not** claim:

- a continuum physical law;
- global uniqueness among all routed-voltage systems;
- that the full parameter domain `0 < a < b < 1` is one realization chamber;
- novelty of standard voltage/gain graph, automata, switching, or graph-cohomological machinery;
- publication priority.

## Local safe sync

The source working tree must be on:

`agent/pifi-3d-manuscript-v05-family`

Then run the included PowerShell script with the private and public repository paths. It copies only files listed in `PUBLIC_RELEASE_MANIFEST.txt`.

Before pushing, always inspect:

```powershell
git status
```

No file outside the whitelist should appear.

## Release status

**v0.5 family-generalization candidate.**
