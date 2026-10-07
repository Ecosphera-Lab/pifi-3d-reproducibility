#!/usr/bin/env python3
"""PIFI-3D refined quotient closed-form / component-orbit gate v0.1.

This gate removes full-dart graph traversal from Q_comp computation.

For the split-annular family T_{n;delta,cAB,cBC}, the routed macro
permutation on frame-entry states is already known exactly.  The only
new information in O_comp is the AB/BC component label carried by each
AB/BC dart.  Those labels are affine functions of the macro entry index.

This gives an exact arithmetic component-orbit formula:

    Q_comp = 8 + sum_{[W] in P_comp} |W|,

where P_comp is the set of distinct cyclic primitive words obtained by
concatenating analytically decorated C3/C6/C20 frame words around the
cycles of the affine macro permutation sigma.

No 32n-dart graph is required to evaluate the predictor.

Important result:
Q_comp is NOT a function of (n,s,h_AB,h_BC) alone.  Component placement
matters.  At n=24, two systems with the same
    s=4, (h_AB,h_BC)=(1,6)
have Q_comp=312 and Q_comp=192.

Regression:
- exact predictor vs full graph O_comp signature for every admissible
  triple q=2..4: 4654/4654 PASS (HT+);
- arithmetic-only component-orbit sweep q=2..8: 70574 cases;
- frozen witness decompositions for 52,84,96,128,184,248,192,312.
"""

from __future__ import annotations

import argparse
import importlib.util
import json
import math
from collections import defaultdict
from pathlib import Path


HERE = Path(__file__).resolve().parent
REF_PATH = HERE / "verify_pifi_3d_refined_terminal_injectivity_v0_1.py"

spec = importlib.util.spec_from_file_location("refined_gate", REF_PATH)
ref = importlib.util.module_from_spec(spec)
assert spec.loader is not None
spec.loader.exec_module(ref)

base = ref.base


def core_A():
    return [
        ("AB", 6, 4), ("AB", 4, 6),
        ("AA", 6, 4), ("AA", 4, 4), ("AA", 4, 4), ("AA", 4, 6),
        ("AB", 6, 4), ("AB", 4, 6),
        ("BC", 6, 4), ("BC", 4, 3), ("BC", 3, 4), ("BC", 4, 6),
    ]


def core_S():
    return [
        ("AB", 6, 4), ("AB", 4, 6),
        ("AA", 6, 4), ("AA", 4, 4), ("AA", 4, 4), ("AA", 4, 6),
        ("AB", 6, 4), ("AB", 4, 6),
        ("BC", 6, 4), ("BC", 4, 6), ("BC", 6, 4), ("BC", 4, 6),
    ]


def core_B(n):
    return [
        ("AB", 6, 4), ("AB", 4, 6),
        ("AA", 6, 4), ("AA", 4, 4), ("AA", 4, 4), ("AA", 4, 6),
        ("AB", 6, 4), ("AB", 4, 6),
        ("BC", 6, 4), ("BC", 4, 3),
        ("AC", 3, 6), ("AC", 6, 6),
        ("OA", 6, 4), ("OA", 4, n), ("OA", n, 4), ("OA", 4, 6),
        ("AC", 6, 6), ("AC", 6, 3),
        ("BC", 3, 4), ("BC", 4, 6),
    ]


def core_U(n):
    return [
        ("OA", 6, 4, "none", 0),
        ("OA", 4, n, "none", 0),
        ("OA", n, 4, "none", 0),
        ("OA", 4, 6, "none", 0),
        ("AC", 6, 6, "none", 0),
        ("AC", 6, 6, "none", 0),
        ("AC", 6, 6, "none", 0),
        ("AC", 6, 6, "none", 0),
    ]


def invariant_parameters(n, delta, c_ab, c_bc):
    q = n // 4
    s = (2 * (delta + c_ab + c_bc)) % n
    return {
        "q": q,
        "s": s,
        "g": math.gcd(q, s),
        "h_AB": math.gcd(n, c_ab),
        "h_BC": ref.h_pair(n, c_ab, c_bc)[1],
    }


def macro_step(n, delta, c_ab, c_bc, state):
    q = n // 4
    seam = {0, q, 2 * q, 3 * q}
    s = (2 * (delta + c_ab + c_bc)) % n
    layer, j = state

    if layer == "L":
        if (j - (s - c_bc)) % n in seam:
            return ("R", (j + n // 2 - (s - c_bc)) % n), "S"
        return ("L", (j - s) % n), "A"

    if (j + s) % n in seam:
        return ("L", (j + n // 2 + s - c_bc) % n), "S"
    return ("R", (j + n // 2 + s) % n), "B"


def component_maps(n, c_ab, c_bc):
    d_ab = math.gcd(n, c_ab)
    d_bc, bc_map = ref.bc_component_map(n, c_bc)

    def alpha(i):
        return i % d_ab

    def kappa(i):
        return bc_map[i % d_bc]

    return alpha, kappa


def decorate(core, ab1, ab2, bc1, bc2, alpha, kappa):
    ab_labels = [alpha(ab1), alpha(ab1), alpha(ab2), alpha(ab2)]
    bc_labels = [kappa(bc1), kappa(bc1), kappa(bc2), kappa(bc2)]

    ia = 0
    ib = 0
    out = []

    for fam, du, dv in core:
        if fam == "AB":
            out.append((fam, du, dv, "ABcomp", ab_labels[ia]))
            ia += 1
        elif fam == "BC":
            out.append((fam, du, dv, "BCcomp", bc_labels[ib]))
            ib += 1
        else:
            out.append((fam, du, dv, "none", 0))

    assert ia == 4
    assert ib == 4
    return out


def decorated_block(n, delta, c_ab, c_bc, state):
    layer, j = state
    s = (2 * (delta + c_ab + c_bc)) % n
    dest, kind = macro_step(n, delta, c_ab, c_bc, state)
    alpha, kappa = component_maps(n, c_ab, c_bc)

    if layer == "L":
        ab1 = (j - c_ab) % n
        ab2 = (j - 2 * c_ab - 2 * delta) % n
        bc1 = (j - (s - c_bc)) % n
        bc2 = dest[1]
        core = core_S() if kind == "S" else core_A()
    else:
        ab1 = (j + c_bc) % n
        ab2 = (j + c_bc + c_ab + 2 * delta) % n
        bc1 = (j + s - c_bc) % n
        bc2 = dest[1]
        core = core_S() if kind == "S" else core_B(n)

    return dest, decorate(core, ab1, ab2, bc1, bc2, alpha, kappa)


def macro_cycles(n, delta, c_ab, c_bc):
    states = [("L", j) for j in range(n)] + [("R", j) for j in range(n)]
    perm = {
        st: macro_step(n, delta, c_ab, c_bc, st)[0]
        for st in states
    }

    seen = set()
    cycles = []

    for start in states:
        if start in seen:
            continue

        cyc = []
        x = start

        while x not in seen:
            seen.add(x)
            cyc.append(x)
            x = perm[x]

        assert x == start
        cycles.append(cyc)

    return cycles


def component_orbit_predictor(n, delta, c_ab, c_bc):
    classes = {}

    for cyc in macro_cycles(n, delta, c_ab, c_bc):
        word = []

        for state in cyc:
            _, block = decorated_block(n, delta, c_ab, c_bc, state)
            word.extend(block)

        root = base.primitive(word)
        key = (len(root), base.minrot(root))
        classes[key] = classes.get(key, 0) + 1

    u = core_U(n)
    u_key = (8, base.minrot(u))
    classes[u_key] = classes.get(u_key, 0) + 1

    return {
        "Q": sum(key[0] for key in classes),
        "periods": sorted(key[0] for key in classes),
        "signature": tuple(sorted(classes.keys(), key=repr)),
        "class_count": len(classes),
    }


def verify_full_graph_equivalence(q_max):
    cases = 0

    for q in range(2, q_max + 1):
        n = 4 * q

        for delta, c_ab, c_bc in base.admissible_triples(n):
            G = base.build(n, delta, c_ab, c_bc, "+")
            direct = ref.analyze_observation(
                G,
                lambda GG, d: ref.component_token(GG, d, mode="both"),
            )
            pred = component_orbit_predictor(n, delta, c_ab, c_bc)

            assert pred["Q"] == direct["Q"], (n, delta, c_ab, c_bc)
            assert pred["periods"] == direct["periods"], (n, delta, c_ab, c_bc)
            assert pred["signature"] == direct["signature"], (
                n, delta, c_ab, c_bc
            )

            cases += 1

    return cases


def arithmetic_sweep(q_max):
    cases = 0
    values = set()

    for q in range(2, q_max + 1):
        n = 4 * q

        for delta, c_ab, c_bc in base.admissible_triples(n):
            p = component_orbit_predictor(n, delta, c_ab, c_bc)
            values.add(p["Q"])
            cases += 1

    return cases, sorted(values)


def witness(n, triple):
    delta, c_ab, c_bc = triple
    inv = invariant_parameters(n, *triple)
    pred = component_orbit_predictor(n, *triple)

    return {
        "n": n,
        "delta": delta,
        "c_AB": c_ab,
        "c_BC": c_bc,
        "s": inv["s"],
        "h_AB": inv["h_AB"],
        "h_BC": inv["h_BC"],
        "Q_comp": pred["Q"],
        "periods": pred["periods"],
        "sum_check": sum(pred["periods"]),
    }


def verify_frozen_witnesses():
    rows = [
        witness(12, (1, 1, 1)),
        witness(12, (1, 5, 3)),
        witness(12, (1, 3, 5)),
        witness(12, (1, 4, 4)),
        witness(16, (1, 4, 7)),
        witness(16, (1, 8, 3)),
        witness(24, (1, 7, 6)),
        witness(24, (1, 5, 8)),
    ]

    assert [r["Q_comp"] for r in rows] == [
        52, 84, 96, 184, 128, 248, 192, 312
    ]

    # Same n,s,h pair but different refined quotient:
    a = rows[-2]
    b = rows[-1]
    assert (a["n"], a["s"], a["h_AB"], a["h_BC"]) == (
        b["n"], b["s"], b["h_AB"], b["h_BC"]
    ) == (24, 4, 1, 6)
    assert a["Q_comp"] == 192
    assert b["Q_comp"] == 312

    return rows


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--full-q-max", type=int, default=4)
    ap.add_argument("--arithmetic-q-max", type=int, default=8)
    ap.add_argument(
        "--output",
        type=Path,
        default=Path(
            "docs/results/pifi_3d_refined_quotient_component_orbit_v0_1.json"
        ),
    )
    args = ap.parse_args()

    full_cases = verify_full_graph_equivalence(args.full_q_max)
    arithmetic_cases, q_values = arithmetic_sweep(args.arithmetic_q_max)
    witnesses = verify_frozen_witnesses()

    result = {
        "schema": "pifi.3d.refined_quotient_component_orbit.v0.1",
        "date": "2026-10-06",
        "status": "STRONG PASS — EXACT COMPONENT-ORBIT FORMULA",
        "formula": (
            "Q_comp = 8 + sum over distinct cyclic primitive decorated "
            "macro-orbit words of their primitive lengths"
        ),
        "macro_shift": "s=2(delta+c_AB+c_BC) mod n",
        "component_maps": {
            "AB": "alpha(i)=i mod gcd(n,c_AB)",
            "BC": (
                "kappa(i)=canonical class of i mod gcd(n,c_BC) after "
                "C0~C_{n/2}, C_q~C_{3q}"
            ),
        },
        "block_index_laws": {
            "L": {
                "AB": ["j-c_AB", "j-2c_AB-2delta"],
                "BC": ["j-(s-c_BC)", "destination index"],
            },
            "R": {
                "AB": ["j+c_BC", "j+c_BC+c_AB+2delta"],
                "BC": ["j+s-c_BC", "destination index"],
            },
        },
        "witnesses": witnesses,
        "no_h_only_formula_witness": {
            "common": {
                "n": 24,
                "s": 4,
                "h_AB": 1,
                "h_BC": 6,
            },
            "case_A": {
                "triple": [1, 7, 6],
                "Q_comp": 192,
                "periods": [8, 36, 60, 88],
            },
            "case_B": {
                "triple": [1, 5, 8],
                "Q_comp": 312,
                "periods": [8, 20, 20, 20, 20, 24, 24, 88, 88],
            },
            "conclusion": (
                "Q_comp is not a function of (n,s,h_AB,h_BC) alone; "
                "component-label placement is essential."
            ),
        },
        "regression": {
            "full_graph_q_range": [2, args.full_q_max],
            "full_graph_exact_signature_cases": full_cases,
            "full_graph_mismatches": 0,
            "arithmetic_q_range": [2, args.arithmetic_q_max],
            "arithmetic_cases": arithmetic_cases,
            "distinct_Q_comp_values": q_values,
        },
        "interpretation": [
            "The refined quotient is exactly computable from the 2n-state affine macro permutation plus component label maps; full dart routing is unnecessary.",
            "The numbers 52,84,96,128,184,192,248,312 are sums of primitive component-decorated macro-orbit periods.",
            "Component counts alone do not determine Q_comp; phase placement of labels along C3/C6/C20 blocks is an essential invariant.",
        ],
    }

    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(
        json.dumps(result, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )

    print("PIFI-3D REFINED QUOTIENT COMPONENT-ORBIT GATE: STRONG PASS")
    print(f"full graph exact signature cases: {full_cases}")
    print(f"arithmetic-only cases: {arithmetic_cases}")
    print("full graph mismatches: 0")
    print("Q_comp is NOT determined by (n,s,h_AB,h_BC) alone")
    print("component placement is required")


if __name__ == "__main__":
    main()
