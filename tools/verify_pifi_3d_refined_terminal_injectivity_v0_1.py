#!/usr/bin/env python3
"""PIFI-3D refined terminal observation / quotient-injectivity gate v0.1.

This verifier reuses the full split-annular graph/routing generator from
verify_pifi_3d_tn_split_annular_offset_v0_1.py and studies observation
refinements rather than adding another wiring parameter.

Coarse observation (O0):
    edge-family | degree(tail) | degree(head)

Natural component-aware refinements:
    O_AB  : O0 + AB component id on AB darts;
    O_BC  : O0 + BC component id on BC darts;
    O_bin : O0 + one bit (component-zero vs nonzero) on AB/BC darts;
    O_comp: O0 + exact canonical component id on AB/BC darts.

The component ids are derived from the already proved family-restricted
connectivity:
    h_AB = gcd(n,c_AB),
and for BC from the quotient of residues mod gcd(n,c_BC) by the two
cardinal C-pair identifications.

Claims checked:
1. O0 is many-to-one on graph microstructure.
2. O_AB alone cannot recover h_BC; O_BC alone cannot recover h_AB.
3. The natural one-bit O_bin refinement is still not injective.
4. O_comp is injective with respect to (h_AB,h_BC), conditional on
   fixed (n,s), over every admissible triple for q=2..6.
5. The original PIFI point (delta,c_AB,c_BC)=(1,1,1) remains Q=52 and
   k_min=13 under O_comp because both component labels are trivial.
6. Representative refined quotients through q=8 are chirality-stable
   in Q, primitive-period census and k_min.

"Minimal" here means first successful refinement in this frozen natural
refinement lattice; it is not a proof of globally minimal bit encoding
among all conceivable observation alphabets.
"""

from __future__ import annotations

import argparse
import importlib.util
import json
import math
from collections import defaultdict
from pathlib import Path


HERE = Path(__file__).resolve().parent
BASE_PATH = HERE / "verify_pifi_3d_tn_split_annular_offset_v0_1.py"

spec = importlib.util.spec_from_file_location("split_annular", BASE_PATH)
base = importlib.util.module_from_spec(spec)
assert spec.loader is not None
spec.loader.exec_module(base)


def parse_index(vertex: str, prefix: str) -> int:
    assert vertex.startswith(prefix), (vertex, prefix)
    return int(vertex[len(prefix):])


def edge_cell_index(G, edge_id: int, family: str) -> int:
    u, v, fam = G["edges"][edge_id]
    assert fam == family

    if family == "AB":
        z = u if u.startswith("Z") else v
        return parse_index(z, "Z")

    if family == "BC":
        w = u if u.startswith("W") else v
        return parse_index(w, "W")

    raise ValueError(family)


def bc_component_map(n: int, c_bc: int):
    """Canonical residue-component labels after the two C identifications."""
    d = math.gcd(n, c_bc)
    q = n // 4
    parent = list(range(d))

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    def union(a, b):
        a = find(a)
        b = find(b)
        if a == b:
            return
        if a > b:
            a, b = b, a
        parent[b] = a

    union(0, (n // 2) % d)
    union(q % d, (3 * q) % d)

    groups = defaultdict(list)
    for r in range(d):
        groups[find(r)].append(r)

    canonical = {}
    for residues in groups.values():
        label = min(residues)
        for r in residues:
            canonical[r] = label

    return d, canonical


def h_pair(n: int, c_ab: int, c_bc: int):
    h_ab = math.gcd(n, c_ab)
    _, cmap = bc_component_map(n, c_bc)
    h_bc = len(set(cmap.values()))
    return h_ab, h_bc


def coarse_token(G, dart_id: int):
    edge_id, u, v = G["darts"][dart_id]
    fam = G["edges"][edge_id][2]
    return fam, G["degree"][u], G["degree"][v]


def component_token(G, dart_id: int, mode="both", binary=False):
    edge_id, u, v = G["darts"][dart_id]
    fam = G["edges"][edge_id][2]
    core = (fam, G["degree"][u], G["degree"][v])

    if fam == "AB" and mode in ("AB", "both"):
        d = math.gcd(G["n"], G["c_ab"])
        i = edge_cell_index(G, edge_id, "AB")
        label = i % d
        if binary:
            label = int(label != 0)
        return core + ("ABcomp", label)

    if fam == "BC" and mode in ("BC", "both"):
        d, cmap = bc_component_map(G["n"], G["c_bc"])
        i = edge_cell_index(G, edge_id, "BC")
        label = cmap[i % d]
        if binary:
            label = int(label != 0)
        return core + ("BCcomp", label)

    return core + ("none", 0)


def analyze_observation(G, token_fn):
    seen = set()
    classes = {}
    cycles = []

    for start in range(len(G["darts"])):
        if start in seen:
            continue

        cyc = []
        x = start

        while x not in seen:
            seen.add(x)
            cyc.append(x)
            x = G["P"][x]

        assert x == start
        cycles.append(cyc)

        root = base.primitive([token_fn(G, d) for d in cyc])
        key = (len(root), base.minrot(root))
        classes[key] = classes.get(key, 0) + 1

    roots = [list(key[1]) for key in classes]

    return {
        "Q": sum(key[0] for key in classes),
        "periods": sorted(key[0] for key in classes),
        "k_min": base.exact_kmin(roots),
        "class_count": len(classes),
        "signature": tuple(sorted(classes.keys(), key=repr)),
    }


def same_signature(a, b):
    return a["signature"] == b["signature"]


def verify_witness_lattice():
    n = 12
    witnesses = [
        (1, 1, 1),
        (1, 3, 5),
        (1, 5, 3),
        (1, 4, 4),
    ]

    rows = []

    coarse_results = []
    ab_results = []
    bc_results = []
    exact_results = []

    for triple in witnesses:
        G = base.build(n, *triple, "+")
        hp = h_pair(n, triple[1], triple[2])

        coarse = analyze_observation(G, coarse_token)
        ab_only = analyze_observation(
            G, lambda GG, d: component_token(GG, d, mode="AB")
        )
        bc_only = analyze_observation(
            G, lambda GG, d: component_token(GG, d, mode="BC")
        )
        exact = analyze_observation(
            G, lambda GG, d: component_token(GG, d, mode="both")
        )

        coarse_results.append(coarse)
        ab_results.append(ab_only)
        bc_results.append(bc_only)
        exact_results.append(exact)

        rows.append({
            "delta": triple[0],
            "c_AB": triple[1],
            "c_BC": triple[2],
            "h_AB": hp[0],
            "h_BC": hp[1],
            "Q_coarse": coarse["Q"],
            "Q_component": exact["Q"],
            "k_min_component": exact["k_min"],
            "periods_component": exact["periods"],
        })

    # All four have the same coarse future language at s=6.
    assert all(same_signature(coarse_results[0], x) for x in coarse_results[1:])
    assert all(x["Q"] == 52 for x in coarse_results)

    # AB-only cannot see BC-only change:
    # (1,1,1) versus (1,5,3) both have h_AB=1.
    assert same_signature(ab_results[0], ab_results[2])

    # BC-only cannot see AB-only change:
    # (1,1,1) versus (1,3,5) both have h_BC=1.
    assert same_signature(bc_results[0], bc_results[1])

    # Both exact component labels separate all four witnesses.
    assert len({x["signature"] for x in exact_results}) == len(witnesses)

    # Frozen expected Q values.
    assert [x["Q"] for x in exact_results] == [52, 96, 84, 184]
    assert [x["k_min"] for x in exact_results] == [13, 13, 13, 13]

    return rows


def verify_binary_counterexample():
    """A natural one-bit component marker is not enough."""
    n = 16

    case_a = (1, 4, 7)  # h=(4,1), s=8
    case_b = (1, 8, 3)  # h=(8,1), s=8

    G_a = base.build(n, *case_a, "+")
    G_b = base.build(n, *case_b, "+")

    p_a = base.invariant_parameters(n, *case_a)
    p_b = base.invariant_parameters(n, *case_b)

    assert p_a["s"] == p_b["s"] == 8
    assert h_pair(n, case_a[1], case_a[2]) == (4, 1)
    assert h_pair(n, case_b[1], case_b[2]) == (8, 1)

    bin_a = analyze_observation(
        G_a, lambda GG, d: component_token(GG, d, mode="both", binary=True)
    )
    bin_b = analyze_observation(
        G_b, lambda GG, d: component_token(GG, d, mode="both", binary=True)
    )

    assert same_signature(bin_a, bin_b)
    assert bin_a["Q"] == bin_b["Q"] == 116
    assert bin_a["k_min"] == bin_b["k_min"] == 19

    exact_a = analyze_observation(
        G_a, lambda GG, d: component_token(GG, d, mode="both")
    )
    exact_b = analyze_observation(
        G_b, lambda GG, d: component_token(GG, d, mode="both")
    )

    assert not same_signature(exact_a, exact_b)
    assert exact_a["Q"] == 128
    assert exact_b["Q"] == 248

    return {
        "n": n,
        "s": 8,
        "case_A": {
            "delta": 1,
            "c_AB": 4,
            "c_BC": 7,
            "h": [4, 1],
            "Q_binary": 116,
            "Q_exact_component": 128,
        },
        "case_B": {
            "delta": 1,
            "c_AB": 8,
            "c_BC": 3,
            "h": [8, 1],
            "Q_binary": 116,
            "Q_exact_component": 248,
        },
        "binary_signatures_equal": True,
        "exact_component_signatures_equal": False,
    }


def verify_exhaustive_injectivity(q_max: int):
    """No exact-component signature collision across different h-pairs at fixed n,s."""
    total = 0
    collision_count = 0
    same_h_multiple_signatures = 0
    per_n = {}

    for q in range(2, q_max + 1):
        n = 4 * q

        signature_to_h = defaultdict(set)
        h_to_signatures = defaultdict(set)
        local_count = 0

        for delta, c_ab, c_bc in base.admissible_triples(n):
            p = base.invariant_parameters(n, delta, c_ab, c_bc)
            hp = h_pair(n, c_ab, c_bc)

            G = base.build(n, delta, c_ab, c_bc, "+")
            result = analyze_observation(
                G, lambda GG, d: component_token(GG, d, mode="both")
            )

            key = (p["s"], result["signature"])
            signature_to_h[key].add(hp)
            h_to_signatures[(p["s"], hp)].add(result["signature"])

            local_count += 1

        local_collisions = sum(
            1 for hps in signature_to_h.values() if len(hps) > 1
        )
        local_multi = sum(
            1 for sigs in h_to_signatures.values() if len(sigs) > 1
        )

        assert local_collisions == 0

        per_n[str(n)] = {
            "triples": local_count,
            "cross_h_pair_signature_collisions": local_collisions,
            "same_h_pair_multiple_signature_classes": local_multi,
        }

        total += local_count
        collision_count += local_collisions
        same_h_multiple_signatures += local_multi

    return {
        "q_range": [2, q_max],
        "triples": total,
        "cross_h_pair_signature_collisions": collision_count,
        "same_h_pair_multiple_signature_classes": same_h_multiple_signatures,
        "per_n": per_n,
    }


def representative_chirality_regression(q_max: int):
    reps = {}

    for q in range(2, q_max + 1):
        n = 4 * q

        for delta, c_ab, c_bc in base.admissible_triples(n):
            p = base.invariant_parameters(n, delta, c_ab, c_bc)
            hp = h_pair(n, c_ab, c_bc)
            key = (q, p["s"], hp[0], hp[1])
            reps.setdefault(key, (delta, c_ab, c_bc))

    mismatches = 0
    signature_collisions = 0
    plus_map = defaultdict(set)

    for (q, s, h_ab, h_bc), triple in sorted(reps.items()):
        n = 4 * q

        Gp = base.build(n, *triple, "+")
        Gm = base.build(n, *triple, "-")

        rp = analyze_observation(
            Gp, lambda GG, d: component_token(GG, d, mode="both")
        )
        rm = analyze_observation(
            Gm, lambda GG, d: component_token(GG, d, mode="both")
        )

        if (
            rp["Q"],
            rp["periods"],
            rp["k_min"],
        ) != (
            rm["Q"],
            rm["periods"],
            rm["k_min"],
        ):
            mismatches += 1

        plus_map[(q, s, rp["signature"])].add((h_ab, h_bc))

    signature_collisions = sum(
        1 for hps in plus_map.values() if len(hps) > 1
    )

    assert mismatches == 0
    assert signature_collisions == 0

    return {
        "q_range": [2, q_max],
        "representative_classes": len(reps),
        "chirality_cases": 2 * len(reps),
        "Q_period_kmin_chirality_mismatches": mismatches,
        "cross_h_pair_signature_collisions_HT_plus": signature_collisions,
    }


def verify_original_pifi():
    rows = {}

    for sign in ("+", "-"):
        G = base.build(12, 1, 1, 1, sign)
        coarse = analyze_observation(G, coarse_token)
        refined = analyze_observation(
            G, lambda GG, d: component_token(GG, d, mode="both")
        )

        assert h_pair(12, 1, 1) == (1, 1)
        assert coarse["Q"] == refined["Q"] == 52
        assert coarse["k_min"] == refined["k_min"] == 13
        assert coarse["periods"] == refined["periods"] == [8, 12, 12, 20]

        rows[sign] = {
            "Q_coarse": coarse["Q"],
            "Q_refined": refined["Q"],
            "k_min": refined["k_min"],
            "periods": refined["periods"],
        }

    return rows


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--injectivity-q-max", type=int, default=6)
    ap.add_argument("--representative-q-max", type=int, default=8)
    ap.add_argument(
        "--output",
        type=Path,
        default=Path(
            "docs/results/pifi_3d_refined_terminal_injectivity_v0_1.json"
        ),
    )
    args = ap.parse_args()

    witnesses = verify_witness_lattice()
    binary_counterexample = verify_binary_counterexample()
    exhaustive = verify_exhaustive_injectivity(args.injectivity_q_max)
    representative = representative_chirality_regression(
        args.representative_q_max
    )
    original_pifi = verify_original_pifi()

    result = {
        "schema": "pifi.3d.refined_terminal_injectivity.v0.1",
        "date": "2026-10-06",
        "status": "STRONG PASS — COMPONENT-AWARE QUOTIENT RECOVERS LOST MICROSTRUCTURE",
        "observation_lattice": {
            "O0": "family | degree(tail) | degree(head)",
            "O_AB": "O0 plus exact AB component id on AB darts",
            "O_BC": "O0 plus exact BC component id on BC darts",
            "O_bin": "O0 plus one bit: component-zero vs nonzero on AB/BC darts",
            "O_comp": "O0 plus exact canonical AB/BC component id",
        },
        "minimality_status": {
            "AB_only": "FAILS to recover h_BC",
            "BC_only": "FAILS to recover h_AB",
            "one_bit_both": "FAILS; explicit n=16 collision",
            "exact_component_both": "PASSES tested injectivity",
            "claim": (
                "O_comp is the first successful refinement in the frozen "
                "natural refinement lattice; absolute global bit-minimality "
                "over every conceivable alphabet is not claimed."
            ),
        },
        "witnesses_n12_s6": witnesses,
        "binary_counterexample": binary_counterexample,
        "exhaustive_injectivity": exhaustive,
        "representative_chirality": representative,
        "original_PIFI": original_pifi,
        "interpretation": [
            "The coarse future quotient is many-to-one over genuine graph microstructure.",
            "Exact family-component labels are sufficient to recover the pair (h_AB,h_BC) in the tested range at fixed (n,s).",
            "The original PIFI point has h_AB=h_BC=1, so the component labels are trivial and its quotient stays exactly Q=52.",
            "Therefore PIFI's 52 states are not produced merely by forgetting nontrivial AB/BC component identities; no such nontrivial identities exist at the original point.",
            "For deformed templates with the same coarse Q=52, the refined quotient grows and exposes the hidden microstructure.",
        ],
    }

    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(
        json.dumps(result, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )

    print("PIFI-3D REFINED TERMINAL / QUOTIENT-INJECTIVITY GATE: STRONG PASS")
    print(
        "exhaustive exact-component triples:",
        exhaustive["triples"],
    )
    print(
        "cross-h collisions:",
        exhaustive["cross_h_pair_signature_collisions"],
    )
    print(
        "representative chirality cases:",
        representative["chirality_cases"],
    )
    print("original PIFI refined Q: 52")
    print("binary component marker: REJECTED by n=16 counterexample")
    print("exact AB+BC component marker: PASSES tested injectivity")


if __name__ == "__main__":
    main()
