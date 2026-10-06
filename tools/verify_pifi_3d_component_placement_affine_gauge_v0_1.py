#!/usr/bin/env python3
"""PIFI-3D component-placement classification / affine-gauge gate v0.1.

This gate classifies the placement information left over after the exact
component-orbit theorem.

For T_{n;delta,cAB,cBC}, define
    s    = 2(delta+cAB+cBC) mod n,
    dAB  = gcd(n,cAB),
    dBC  = gcd(n,cBC),
    rho  = cBC mod dAB.

After the layer-coordinate gauge
    x = j-(s-cBC) on L,
    y = j+s       on R,
the macro permutation depends only on (n,s), and the component labels in
one frame have the normal form

  AB on L_x:  (x+s-rho, x+rho)
  AB on R_y:  (y-s+rho, y-rho)

  BC on L_x:  (kappa(x), kappa(x))            for C3,
               (kappa(x), kappa(x+n/2))       for C6,
  BC on R_y:  (kappa(y), kappa(y+n/2))        for C20/C6,

where kappa is determined only by (n,dBC) and the two cardinal C-pair
identifications.

Thus the raw placement normal form is
    Pi0 = (n,s,dAB,dBC,rho).

Affine index gauges j -> u*j+t, with u in U(n) and t in the cardinal
subgroup {0,q,2q,3q}, preserve the seam geometry.  After component-label
renaming they act by
    (s,rho) -> (u*s mod n, u*rho mod dAB).

Therefore the finite affine placement class is
    Theta = (n,dAB,dBC, chi),
where
    chi = min_{u in U(n)} (u*s mod n, u*rho mod dAB).

Equivalently dAB=hAB, while dBC is recoverable from
    (hBC, epsBC), epsBC=[dBC divides n/2]:
      dBC=hBC       if epsBC=1,
      dBC=hBC+2     if epsBC=0.

The gate also proves by explicit counterexample that gcd/lcm data alone
do not classify placement: a coupled diagonal unit-orbit residue remains
essential.
"""

from __future__ import annotations

import argparse
import importlib.util
import json
import math
from collections import defaultdict
from pathlib import Path


HERE = Path(__file__).resolve().parent
PREV = HERE / "verify_pifi_3d_refined_quotient_component_orbit_v0_1.py"

spec = importlib.util.spec_from_file_location("component_orbit", PREV)
prev = importlib.util.module_from_spec(spec)
assert spec.loader is not None
spec.loader.exec_module(prev)

base = prev.base
ref = prev.ref


def units(n):
    return [u for u in range(n) if math.gcd(u, n) == 1]


def placement_data(n, delta, c_ab, c_bc):
    s = (2 * (delta + c_ab + c_bc)) % n
    d_ab = math.gcd(n, c_ab)
    d_bc = math.gcd(n, c_bc)
    rho = c_bc % d_ab

    h_bc = ref.h_pair(n, c_ab, c_bc)[1]
    eps_bc = int((n // 2) % d_bc == 0)

    assert d_bc == (h_bc if eps_bc else h_bc + 2)

    return {
        "n": n,
        "s": s,
        "d_AB": d_ab,
        "d_BC": d_bc,
        "rho": rho,
        "h_AB": d_ab,
        "h_BC": h_bc,
        "eps_BC": eps_bc,
    }


def raw_placement_key(n, delta, c_ab, c_bc):
    p = placement_data(n, delta, c_ab, c_bc)
    return (n, p["s"], p["d_AB"], p["d_BC"], p["rho"])


def diagonal_unit_orbit(n, s, d_ab, rho):
    return tuple(sorted({
        (u * s % n, u * rho % d_ab)
        for u in units(n)
    }))


def affine_placement_key(n, delta, c_ab, c_bc):
    p = placement_data(n, delta, c_ab, c_bc)
    chi = min(diagonal_unit_orbit(n, p["s"], p["d_AB"], p["rho"]))
    return (n, p["d_AB"], p["d_BC"], chi)


def taxonomy_key(n, delta, c_ab, c_bc):
    p = placement_data(n, delta, c_ab, c_bc)
    chi = min(diagonal_unit_orbit(n, p["s"], p["d_AB"], p["rho"]))
    return (
        n,
        p["h_AB"],
        p["h_BC"],
        p["eps_BC"],
        chi,
    )


def normalize_component_colors_linear(word):
    maps = {"ABcomp": {}, "BCcomp": {}}
    nxt = {"ABcomp": 0, "BCcomp": 0}
    out = []

    for fam, du, dv, tag, label in word:
        if tag in maps:
            mp = maps[tag]
            if label not in mp:
                mp[label] = nxt[tag]
                nxt[tag] += 1
            label = mp[label]
        else:
            label = 0

        out.append((fam, du, dv, tag, label))

    return tuple(out)


def canonical_component_colored_cycle(word):
    word = list(word)
    return min(
        normalize_component_colors_linear(word[k:] + word[:k])
        for k in range(len(word))
    )


def gauge_future_signature(n, delta, c_ab, c_bc):
    classes = {}

    for cyc in prev.macro_cycles(n, delta, c_ab, c_bc):
        word = []

        for state in cyc:
            _, block = prev.decorated_block(n, delta, c_ab, c_bc, state)
            word.extend(block)

        root = base.primitive(word)
        key = (len(root), canonical_component_colored_cycle(root))
        classes[key] = classes.get(key, 0) + 1

    u = prev.core_U(n)
    ukey = (8, canonical_component_colored_cycle(u))
    classes[ukey] = classes.get(ukey, 0) + 1

    return {
        "Q": sum(key[0] for key in classes),
        "periods": sorted(key[0] for key in classes),
        "signature": tuple(sorted(classes.keys(), key=repr)),
    }


def all_triples(n):
    yield from base.admissible_triples(n)


def verify_raw_normal_form(q_max):
    """Same Pi0 must imply the same component-colour future signature."""
    key_to_signature = {}
    cases = 0
    classes = set()

    for q in range(2, q_max + 1):
        n = 4 * q

        for triple in all_triples(n):
            raw = raw_placement_key(n, *triple)
            sig = gauge_future_signature(n, *triple)["signature"]

            if raw in key_to_signature:
                assert key_to_signature[raw] == sig, (raw, triple)
            else:
                key_to_signature[raw] = sig

            classes.add(raw)
            cases += 1

    return {
        "q_range": [2, q_max],
        "triples": cases,
        "raw_placement_classes": len(classes),
        "within_raw_class_signature_splits": 0,
    }


def verify_affine_gauge(q_max):
    """One representative per raw Pi0; equal affine keys must agree."""
    raw_reps = {}

    for q in range(2, q_max + 1):
        n = 4 * q
        for triple in all_triples(n):
            raw_reps.setdefault(
                raw_placement_key(n, *triple),
                (n, triple),
            )

    affine_to_signature = {}
    affine_classes = set()

    for raw, (n, triple) in raw_reps.items():
        ak = affine_placement_key(n, *triple)
        sig = gauge_future_signature(n, *triple)["signature"]

        if ak in affine_to_signature:
            assert affine_to_signature[ak] == sig, (ak, triple)
        else:
            affine_to_signature[ak] = sig

        affine_classes.add(ak)

    return {
        "q_range": [2, q_max],
        "raw_representatives": len(raw_reps),
        "affine_placement_classes": len(affine_classes),
        "within_affine_class_signature_splits": 0,
    }


def class_count_sweep(q_max):
    triples = 0
    raw = set()
    affine = set()

    for q in range(2, q_max + 1):
        n = 4 * q

        for triple in all_triples(n):
            triples += 1
            raw.add(raw_placement_key(n, *triple))
            affine.add(affine_placement_key(n, *triple))

    return {
        "q_range": [2, q_max],
        "triples": triples,
        "raw_placement_classes": len(raw),
        "affine_placement_classes": len(affine),
    }


def explicit_witnesses():
    n = 12

    # Nontrivial affine-gauge equivalence.
    A = (1, 3, 1)
    B = (5, 3, 5)

    pA = placement_data(n, *A)
    pB = placement_data(n, *B)

    assert raw_placement_key(n, *A) != raw_placement_key(n, *B)
    assert affine_placement_key(n, *A) == affine_placement_key(n, *B)

    sA = gauge_future_signature(n, *A)
    sB = gauge_future_signature(n, *B)

    assert sA["signature"] == sB["signature"]

    # u=5 realizes the diagonal unit action:
    assert (5 * pA["s"]) % 12 == pB["s"]
    assert (5 * pA["rho"]) % pA["d_AB"] == pB["rho"]

    # GCD-only data are insufficient.
    C = (3, 3, 1)
    pC = placement_data(n, *C)
    sC = gauge_future_signature(n, *C)

    gcd_A = (
        n,
        math.gcd(n, pA["s"]),
        pA["d_AB"],
        pA["d_BC"],
        math.gcd(pA["d_AB"], pA["rho"]),
    )
    gcd_C = (
        n,
        math.gcd(n, pC["s"]),
        pC["d_AB"],
        pC["d_BC"],
        math.gcd(pC["d_AB"], pC["rho"]),
    )

    assert gcd_A == gcd_C
    assert sA["Q"] == sC["Q"] == 96
    assert sA["periods"] == sC["periods"] == [8, 88]
    assert sA["signature"] != sC["signature"]
    assert affine_placement_key(n, *A) != affine_placement_key(n, *C)

    # BC seam flag witness from the previous 192/312 counterexample.
    D = (1, 7, 6)
    E = (1, 5, 8)

    pD = placement_data(24, *D)
    pE = placement_data(24, *E)

    assert (
        pD["s"], pD["h_AB"], pD["h_BC"]
    ) == (
        pE["s"], pE["h_AB"], pE["h_BC"]
    ) == (4, 1, 6)

    assert pD["eps_BC"] == 1
    assert pE["eps_BC"] == 0
    assert pD["d_BC"] == 6
    assert pE["d_BC"] == 8

    qD = prev.component_orbit_predictor(24, *D)["Q"]
    qE = prev.component_orbit_predictor(24, *E)["Q"]

    assert qD == 192
    assert qE == 312

    return {
        "affine_equivalence": {
            "n": 12,
            "case_A": {
                "triple": list(A),
                "raw": list(raw_placement_key(n, *A)),
                "Q": sA["Q"],
            },
            "case_B": {
                "triple": list(B),
                "raw": list(raw_placement_key(n, *B)),
                "Q": sB["Q"],
            },
            "unit": 5,
            "same_affine_key": True,
            "same_component_colored_future_signature": True,
        },
        "gcd_only_failure": {
            "n": 12,
            "case_A": {
                "triple": list(A),
                "s": pA["s"],
                "rho": pA["rho"],
            },
            "case_B": {
                "triple": list(C),
                "s": pC["s"],
                "rho": pC["rho"],
            },
            "common_gcd_data": list(gcd_A),
            "common_Q": 96,
            "common_periods": [8, 88],
            "same_signature": False,
            "conclusion": (
                "gcd/lcm-style scalar data alone do not classify placement; "
                "the coupled diagonal unit orbit of (s,rho) is essential"
            ),
        },
        "bc_seam_flag": {
            "n": 24,
            "common": {
                "s": 4,
                "h_AB": 1,
                "h_BC": 6,
            },
            "case_eps_1": {
                "triple": list(D),
                "d_BC": 6,
                "eps_BC": 1,
                "Q_comp": qD,
            },
            "case_eps_0": {
                "triple": list(E),
                "d_BC": 8,
                "eps_BC": 0,
                "Q_comp": qE,
            },
        },
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--raw-q-max", type=int, default=4)
    ap.add_argument("--affine-q-max", type=int, default=5)
    ap.add_argument("--count-q-max", type=int, default=8)
    ap.add_argument(
        "--output",
        type=Path,
        default=Path(
            "docs/results/pifi_3d_component_placement_affine_gauge_v0_1.json"
        ),
    )
    args = ap.parse_args()

    raw_reg = verify_raw_normal_form(args.raw_q_max)
    affine_reg = verify_affine_gauge(args.affine_q_max)
    counts = class_count_sweep(args.count_q_max)
    witnesses = explicit_witnesses()

    result = {
        "schema": "pifi.3d.component_placement_affine_gauge.v0.1",
        "date": "2026-10-06",
        "status": "STRONG PASS — FINITE AFFINE PLACEMENT TAXONOMY",
        "raw_normal_form": {
            "Pi0": "(n,s,d_AB,d_BC,rho)",
            "s": "2(delta+c_AB+c_BC) mod n",
            "d_AB": "gcd(n,c_AB)",
            "d_BC": "gcd(n,c_BC)",
            "rho": "c_BC mod d_AB",
        },
        "gauge_normal_form": {
            "layer_coordinates": {
                "L": "x=j-(s-c_BC)",
                "R": "y=j+s",
            },
            "AB_labels": {
                "L_x": ["x+s-rho", "x+rho"],
                "R_y": ["y-s+rho", "y-rho"],
                "modulus": "d_AB",
            },
            "BC_labels": {
                "L_C3": ["kappa(x)", "kappa(x)"],
                "L_C6": ["kappa(x)", "kappa(x+n/2)"],
                "R_C20_or_C6": ["kappa(y)", "kappa(y+n/2)"],
                "kappa_depends_only_on": "(n,d_BC)",
            },
        },
        "affine_gauge": {
            "group": "cardinal translations semidirect U(n)",
            "unit_action": "(s,rho)->(u*s mod n,u*rho mod d_AB)",
            "class": "Theta=(n,d_AB,d_BC,chi), chi=min_{u in U(n)}(u*s,u*rho)",
        },
        "equivalent_h_taxonomy": {
            "h_AB": "d_AB",
            "eps_BC": "[d_BC divides n/2]",
            "d_BC_from_h_BC_eps": "h_BC if eps_BC=1, else h_BC+2",
            "taxonomy": "(n,h_AB,h_BC,eps_BC,chi)",
        },
        "regression": {
            "raw_normal_form": raw_reg,
            "affine_gauge": affine_reg,
            "class_count": counts,
        },
        "witnesses": witnesses,
        "main_interpretation": [
            "Component placement admits a finite exact affine-gauge taxonomy.",
            "The raw dependence on delta,c_AB,c_BC collapses to d_AB,d_BC and the diagonal unit orbit of (s,rho).",
            "Pure gcd/lcm data are insufficient; one coupled residue-orbit invariant is irreducible in general.",
            "The 192/312 counterexample is explained by the BC seam flag eps_BC, equivalently d_BC=6 versus d_BC=8.",
        ],
        "next_gate": (
            "Derive prime-power / CRT classification of the diagonal unit orbit "
            "chi and decide whether it can be expressed by a finite p-adic "
            "valuation-and-ratio taxonomy."
        ),
    }

    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(
        json.dumps(result, indent=2, ensure_ascii=False) + "\\n",
        encoding="utf-8",
    )

    print("PIFI-3D COMPONENT-PLACEMENT / AFFINE-GAUGE GATE: STRONG PASS")
    print(raw_reg)
    print(affine_reg)
    print(counts)
    print("gcd-only taxonomy: REJECTED")
    print("finite affine placement taxonomy: PASS")


if __name__ == "__main__":
    main()
