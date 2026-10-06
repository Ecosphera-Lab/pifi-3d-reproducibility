# Reproducing PIFI-3D family classification v0.6

## Environment

- Python 3.11 or newer
- no third-party Python package is required by the frozen v0.6 verifier chain

## One-command reproduction

From repository root:

```bash
python run_all.py
```

This executes, in order:

1. split AB/BC annular-offset theorem;
2. refined terminal / quotient-injectivity gate;
3. exact component-orbit quotient predictor;
4. component-placement affine-gauge classification;
5. CRT / prime-power placement classification;
6. final necessity/sufficiency control.

Outputs are written under `reproduced/`.

## Individual commands

```bash
python tools/verify_pifi_3d_tn_split_annular_offset_v0_1.py
python tools/verify_pifi_3d_refined_terminal_injectivity_v0_1.py
python tools/verify_pifi_3d_refined_quotient_component_orbit_v0_1.py
python tools/verify_pifi_3d_component_placement_affine_gauge_v0_1.py
python tools/verify_pifi_3d_crt_prime_power_placement_v0_1.py
python tools/verify_pifi_3d_final_classification_control_v0_1.py
```

## Frozen anchor

For the original PIFI point

[
n=12,\quad
(\delta,c_{AB},c_{BC})=(1,1,1),
]

the expected values are

[
Q_{\rm coarse}=Q_{\rm comp}=52,
\qquad
k_{\min}=13,
]

with primitive periods

[
8,12,12,20.
]

## Manuscript

```bash
cd paper
latexmk -pdf -file-line-error -halt-on-error -interaction=nonstopmode main.tex
```

## Claim boundary

A successful reproduction certifies the frozen finite/combinatorial claims in
the tested scopes. It does not establish publication priority, physical
continuum validity, or novelty of standard mathematical machinery.
