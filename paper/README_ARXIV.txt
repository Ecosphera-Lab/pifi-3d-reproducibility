PIFI-3D family-classification manuscript v0.6

Title:
An Exactly Solvable Family of Routed Rotation Systems with Observation-Dependent Future Quotients

Author:
Maks Katsubo
Independent researcher

Primary source:
main.tex

Bibliography:
references.bib

Build:
latexmk -pdf -file-line-error -halt-on-error -interaction=nonstopmode main.tex

Scope:
This manuscript is the publication-grade consolidation of the frozen
T_{n;delta,c_AB,c_BC} classification branch. It intentionally omits the
historical order of computational experiments and presents only the logical
chain:

Definition -> Macro Reduction -> Coarse Classification -> PIFI Corollary ->
Information Loss -> Refined Quotient -> Placement -> CRT -> Claim Boundaries.

Novelty boundary:
The underlying machinery from rotation systems, automata/symbolic dynamics,
cyclic words, affine group actions and CRT is standard. The candidate
contribution is the exact solvability and integrated arithmetic classification
of the explicitly defined routed family.

Public release:
Before submission, pair this source with the frozen verifier/result package
listed in docs/publication/pifi_3d/public_release_v0_6/MANIFEST.json.
