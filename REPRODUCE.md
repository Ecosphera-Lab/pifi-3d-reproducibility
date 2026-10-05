# Reproducing the PIFI-3D finite results

## Environment

Recommended:

- Python 3.11 or newer
- SymPy
- NetworkX

Install dependencies:

```bash
python -m pip install -r requirements.txt
```

## Core geometry

```bash
python tools/verify_pifi_3d_replay_cross_consistency_v0_1.py
```

Expected core geometry includes:

- 85 active geometric vertices;
- 192 active split edges;
- periodic quotient 83V/192E;
- degree histogram (8d_3+48d_4+26d_6+d_{12}).

## Geometry-to-grammar

Run in order:

```bash
python tools/verify_pifi_3d_geometry_to_grammar_g1_oa_block_v0_1.py
python tools/verify_pifi_3d_geometry_to_grammar_g2_radial_v0_1.py
python tools/verify_pifi_3d_geometry_to_grammar_g3_bc_core_v0_1.py
python tools/verify_pifi_3d_geometry_to_grammar_g4_tangential_frame_v0_1.py
```

Expected:

- G1: unique OA block (O);
- G2: exactly (U,R3);
- G3: exactly (C3,C6,C20);
- G4: one 10-terminal tangential frame (T(C)).

## Conceptual quotient

```bash
python tools/verify_pifi_3d_conceptual_derivation_v0_1.py
```

Expected:

[
52=8+12+12+20,qquad k_{min}=13.
]

## Radial-shell family theorem

```bash
python tools/verify_pifi_3d_family_persistent_concurrency_v0_1.py
python tools/verify_pifi_3d_family_split_rotation_stability_v0_1.py
```

Expected:

- all 85 active concurrences persist symbolically;
- the PIFI point lies in a nonempty open split/rotation realization chamber.

The theorem proves an open neighborhood of ((1/2,sqrt3/2)). It does **not** yet prove that all (0<a<b<1) belongs to one chamber.

## Full publication evidence

```bash
python tools/verify_pifi_3d_publication_evidence_v0_2.py
```

## Controls

The heavier control scripts are intentionally separate because they take longer:

```bash
python tools/explore_pifi_3d_novelty_control_routing_full_scorecard_v0_1.py
python tools/explore_pifi_3d_novelty_control_routed_voltage_conjugacy_v0_1.py
python tools/explore_pifi_3d_non_conjugate_isosignature_search_v0_1.py
```

Frozen result JSONs are under `docs/results/`.

## Manuscript

LaTeX source:

`paper/pifi_3d/main.tex`

Typical build:

```bash
cd paper/pifi_3d
latexmk -pdf main.tex
```

The interactive geometry supplement is in `paper/pifi_3d/supplement/`.
