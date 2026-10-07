#!/usr/bin/env python3
"""PIFI-3D final classification / necessity-sufficiency control v0.1.

This is a closing stress test. It introduces no new model parameters.

It cross-checks the frozen chain:

  full 32n-dart graph
    -> exact split-annular macro theorem
    -> component-aware terminal future
    -> 2n-state component-orbit predictor
    -> affine placement class
    -> CRT / prime-power placement signature.

The control intentionally mixes:
- small exhaustive-anchor sizes;
- prime q;
- prime-power q;
- highly composite / gcd-rich q;
- adversarial offsets forcing s=0, s=2, s=n/2 and seam-adjacent cases;
- both chiralities HT+ / HT-.

Precise logic boundaries:
1. CRT signature <=> diagonal U(n)-orbit is tested as a necessity-and-
   sufficiency statement.
2. Equal CRT placement class => equal component-colour future language is
   tested as a sufficiency statement.
3. The converse "same future language => same CRT class" is NOT assumed:
   accidental future-language degeneracies are counted and reported.
4. Full graph refined observation is compared directly to the independent
   component-orbit predictor on HT+.
5. HT- is checked against the same coarse theorem and against HT+ refined
   Q/period/k_min invariants.

If all asserted checks pass, this research branch should be frozen.
"""

from __future__ import annotations

import argparse
import importlib.util
import json
import math
from collections import defaultdict
from pathlib import Path


HERE = Path(__file__).resolve().parent


def load(name, filename):
    spec = importlib.util.spec_from_file_location(name, HERE / filename)
    mod = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(mod)
    return mod


split = load(
    "split_annular",
    "verify_pifi_3d_tn_split_annular_offset_v0_1.py",
)
refined = load(
    "refined_terminal",
    "verify_pifi_3d_refined_terminal_injectivity_v0_1.py",
)
orbit = load(
    "component_orbit",
    "verify_pifi_3d_refined_quotient_component_orbit_v0_1.py",
)
affine = load(
    "affine_gauge",
    "verify_pifi_3d_component_placement_affine_gauge_v0_1.py",
)
crt = load(
    "crt_prime_power",
    "verify_pifi_3d_crt_prime_power_placement_v0_1.py",
)


Q_GROUPS = {
    "small_anchor": [2, 3, 4],
    "prime_q": [5, 7, 11, 13, 17, 19],
    "prime_power_q": [8, 9, 16, 25, 27],
    "gcd_rich_q": [6, 12, 18, 24, 30],
}


def valid_triple(n, t):
    d, a, b = t
    return (
        1 <= d < n
        and 1 <= a < n
        and 1 <= b < n
        and b != n // 2
    )


def force_delta(n, c_ab, c_bc, target_sum):
    """Choose delta so delta+c_ab+c_bc == target_sum mod n."""
    d = (target_sum - c_ab - c_bc) % n
    return d if d != 0 else None


def adversarial_triples(q, limit=14):
    n = 4 * q

    pairs = [
        (1, 1),
        (2 if n > 2 else 1, 1),
        (q, 1),
        (1, q),
        (q, max(1, q - 1)),
        (n // 2, 1),
        (q, n // 2 - 1),
        (max(1, n // 4), n // 2 + 1),
        (n - 1, n - 1),
    ]

    # Add gcd-rich divisors when available.
    for k in (3, 5, 6, 8):
        if n % k == 0:
            pairs.append((n // k, max(1, n // k - 1)))

    out = []
    seen = set()

    for c_ab, c_bc in pairs:
        if not (1 <= c_ab < n and 1 <= c_bc < n):
            continue
        if c_bc == n // 2:
            continue

        deltas = [
            1,
            n - 1,
            force_delta(n, c_ab, c_bc, 0),          # s=0
            force_delta(n, c_ab, c_bc, 1),          # s=2
            force_delta(n, c_ab, c_bc, n // 4),     # s=n/2
            force_delta(n, c_ab, c_bc, q + 1),
        ]

        for delta in deltas:
            if delta is None:
                continue
            t = (delta, c_ab, c_bc)
            if valid_triple(n, t) and t not in seen:
                seen.add(t)
                out.append(t)
                if len(out) >= limit:
                    return out

    return out


def all_control_cases(limit_per_q=14):
    rows = []
    seen_q = set()

    for group, qs in Q_GROUPS.items():
        for q in qs:
            if q in seen_q:
                continue
            seen_q.add(q)
            for t in adversarial_triples(q, limit=limit_per_q):
                rows.append((group, q, 4 * q, t))

    return rows


def refined_direct(G):
    return refined.analyze_observation(
        G,
        lambda GG, d: refined.component_token(GG, d, mode="both"),
    )


def exact_pair_key(n, triple):
    delta, c_ab, c_bc = triple
    s, rho, d_ab, d_bc = crt.placement_pair(n, delta, c_ab, c_bc)
    psi = crt.local_prime_power_invariant(s, rho, n, d_ab)
    return (n, d_ab, d_bc, psi)


def check_full_graph_chain(cases):
    summary = {
        "cases": 0,
        "chirality_cases": 0,
        "macro_cases_HT_plus": 0,
        "coarse_full_cases": 0,
        "refined_full_vs_orbit_cases_HT_plus": 0,
        "refined_chirality_cases": 0,
        "mismatches": 0,
        "by_group": defaultdict(int),
        "s_zero_cases": 0,
        "s_two_cases": 0,
        "s_halfturn_cases": 0,
        "max_n": 0,
    }

    crt_to_future = {}
    future_to_crt = defaultdict(set)

    for group, q, n, triple in cases:
        delta, c_ab, c_bc = triple
        p = split.invariant_parameters(n, delta, c_ab, c_bc)
        s = p["s"]

        summary["cases"] += 1
        summary["by_group"][group] += 1
        summary["max_n"] = max(summary["max_n"], n)
        summary["s_zero_cases"] += int(s == 0)
        summary["s_two_cases"] += int(s == 2 % n)
        summary["s_halfturn_cases"] += int(s == n // 2)

        # Full graph HT+ -> exact macro transition theorem + component counts.
        Gp = split.build(n, delta, c_ab, c_bc, "+")
        split.verify_macro_formula(Gp)
        summary["macro_cases_HT_plus"] += 1

        # Coarse theorem on both chiralities.
        split.verify_full_case(n, delta, c_ab, c_bc, "+")
        split.verify_full_case(n, delta, c_ab, c_bc, "-")
        summary["coarse_full_cases"] += 2

        # Refined full graph HT+ vs independent 2n-state component-orbit predictor.
        direct_p = refined_direct(Gp)
        pred = orbit.component_orbit_predictor(n, delta, c_ab, c_bc)

        assert direct_p["Q"] == pred["Q"], (n, triple, "Q")
        assert direct_p["periods"] == pred["periods"], (n, triple, "periods")
        assert direct_p["signature"] == pred["signature"], (
            n, triple, "signature"
        )
        summary["refined_full_vs_orbit_cases_HT_plus"] += 1

        # Refined chirality stability.
        Gm = split.build(n, delta, c_ab, c_bc, "-")
        direct_m = refined_direct(Gm)

        assert (
            direct_p["Q"],
            direct_p["periods"],
            direct_p["k_min"],
        ) == (
            direct_m["Q"],
            direct_m["periods"],
            direct_m["k_min"],
        ), (n, triple, "refined chirality")
        summary["refined_chirality_cases"] += 2

        # CRT class is sufficient for component-colour future language.
        ck = exact_pair_key(n, triple)
        colour_sig = affine.gauge_future_signature(n, delta, c_ab, c_bc)[
            "signature"
        ]

        if ck in crt_to_future:
            assert crt_to_future[ck] == colour_sig, (n, triple, "CRT sufficiency")
        else:
            crt_to_future[ck] = colour_sig

        future_to_crt[(n, colour_sig)].add(ck)

        summary["chirality_cases"] += 2

    accidental = [
        {
            "n": key[0],
            "crt_classes": len(vals),
        }
        for key, vals in future_to_crt.items()
        if len(vals) > 1
    ]

    summary["distinct_CRT_classes_in_control"] = len(crt_to_future)
    summary["future_language_cross_CRT_collisions"] = len(accidental)
    summary["future_language_cross_CRT_collision_examples"] = accidental[:12]
    summary["by_group"] = dict(summary["by_group"])

    return summary


def generic_crt_controls():
    """Independent explicit-unit-orbit checks outside the original family."""
    moduli = [
        8, 12, 16, 20, 24, 28, 32, 36, 40, 48,
        60, 64, 72, 80, 96, 100, 108, 120,
    ]

    comparisons = 0
    inv_to_orbit = {}
    orbit_to_inv = {}

    for n in moduli:
        ds = set(crt.divisors(n))
        # Emphasize divisors carrying prime-power depth.
        for d in ds:
            candidate_s = {
                0, 1, 2 % n, n // 2, n - 1,
            }
            for p, e in crt.factor(n):
                candidate_s.add((p ** max(0, e - 1)) % n)
                candidate_s.add((2 * p ** max(0, e - 1)) % n)

            candidate_rho = {0}
            if d > 1:
                candidate_rho |= {1, d - 1}
                for p, f in crt.factor(d):
                    candidate_rho.add((p ** max(0, f - 1)) % d)
                    candidate_rho.add((3 * p ** max(0, f - 1)) % d)

            for s in sorted(candidate_s):
                for rho in sorted(candidate_rho):
                    inv = crt.local_prime_power_invariant(s, rho, n, d)
                    orb = crt.explicit_unit_orbit(s, rho, n, d)
                    k = (n, d, inv)
                    ko = (n, d, orb)

                    if k in inv_to_orbit:
                        assert inv_to_orbit[k] == orb
                    else:
                        inv_to_orbit[k] = orb

                    if ko in orbit_to_inv:
                        assert orbit_to_inv[ko] == inv
                    else:
                        orbit_to_inv[ko] = inv

                    comparisons += 1

    # Re-run the earlier exhaustive anchor to catch general regressions.
    anchor = crt.verify_generic_pair_theorem(64)

    return {
        "adversarial_moduli": moduli,
        "sampled_pair_checks": comparisons,
        "sampled_signature_orbit_mismatches": 0,
        "exhaustive_anchor": anchor,
    }


def mandatory_anchor_checks():
    # Original PIFI must remain exactly the frozen 52-state object.
    anchors = {}

    for sign in ("+", "-"):
        G = split.build(12, 1, 1, 1, sign)
        coarse = split.analyze(G)
        refined_res = refined_direct(G)

        assert coarse["future_states"] == 52
        assert coarse["k_min"] == 13
        assert coarse["primitive_periods"] == [8, 12, 12, 20]

        assert refined_res["Q"] == 52
        assert refined_res["k_min"] == 13
        assert refined_res["periods"] == [8, 12, 12, 20]

        anchors[sign] = {
            "Q_coarse": 52,
            "Q_refined": 52,
            "k_min": 13,
            "periods": [8, 12, 12, 20],
        }

    # Earlier counterexamples must remain alive.
    A = orbit.component_orbit_predictor(24, 1, 7, 6)
    B = orbit.component_orbit_predictor(24, 1, 5, 8)
    assert A["Q"] == 192
    assert B["Q"] == 312

    # Earlier CRT witnesses.
    assert (
        crt.local_prime_power_invariant(10, 1, 12, 3)
        == crt.local_prime_power_invariant(2, 2, 12, 3)
    )
    assert (
        crt.local_prime_power_invariant(10, 1, 12, 3)
        != crt.local_prime_power_invariant(2, 1, 12, 3)
    )
    assert (
        crt.local_prime_power_invariant(2, 2, 16, 8)
        != crt.local_prime_power_invariant(2, 6, 16, 8)
    )

    return {
        "original_PIFI": anchors,
        "placement_counterexample_Q": [192, 312],
        "CRT_witnesses": "PASS",
    }


def extended_arithmetic_controls():
    """No full graph: larger prime/prime-power/composite placement checks."""
    qs = [31, 32, 37, 41, 49, 60]
    rows = []
    total = 0

    for q in qs:
        n = 4 * q
        local = set()

        # Use adversarial family points only; full enumeration would be cubic.
        triples = adversarial_triples(q, limit=24)
        for t in triples:
            old = crt.old_affine_key(n, *t)
            new = crt.crt_key(n, *t)

            # Directly verify the CRT key's local signature agrees with
            # the explicit canonical U(n)-orbit used by the old classifier.
            s, rho, d_ab, d_bc = crt.placement_pair(n, *t)
            assert old == (
                n,
                d_ab,
                d_bc,
                crt.canonical_orbit_pair(s, rho, n, d_ab),
            )
            assert new == (
                n,
                d_ab,
                d_bc,
                crt.local_prime_power_invariant(s, rho, n, d_ab),
            )

            local.add(new)
            total += 1

        rows.append({
            "q": q,
            "n": n,
            "triples": len(triples),
            "CRT_classes": len(local),
        })

    return {
        "q_values": qs,
        "cases": total,
        "per_q": rows,
        "mismatches": 0,
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--limit-per-q", type=int, default=14)
    ap.add_argument(
        "--output",
        type=Path,
        default=Path(
            "artifacts/final_classification_control/"
            "pifi_3d_final_classification_control_v0_1.json"
        ),
    )
    args = ap.parse_args()

    cases = all_control_cases(limit_per_q=args.limit_per_q)

    anchors = mandatory_anchor_checks()
    graph_chain = check_full_graph_chain(cases)
    generic_crt = generic_crt_controls()
    extended = extended_arithmetic_controls()

    result = {
        "schema": "pifi.3d.final_classification_control.v0.1",
        "date": "2026-10-06",
        "status": "FINAL CONTROL PASS",
        "scope": {
            "new_parameters": False,
            "purpose": (
                "adversarial cross-check of the frozen graph -> macro -> "
                "component orbit -> affine/CRT classification chain"
            ),
        },
        "case_groups": Q_GROUPS,
        "anchors": anchors,
        "full_graph_chain": graph_chain,
        "generic_CRT_control": generic_crt,
        "extended_arithmetic_control": extended,
        "necessity_sufficiency_boundary": {
            "CRT_vs_diagonal_unit_orbit": "NECESSARY AND SUFFICIENT",
            "CRT_placement_class_to_component_colour_future": "SUFFICIENT",
            "component_colour_future_to_CRT_class": (
                "NOT ASSUMED; accidental language degeneracies are reported"
            ),
            "full_graph_HTplus_to_component_orbit_predictor": "EXACT ON CONTROL SET",
            "HTplus_vs_HTminus": (
                "same coarse Q/period/k_min and same refined Q/period/k_min "
                "on control set"
            ),
        },
        "final_verdict": (
            "FREEZE MATHEMATICAL BRANCH if this JSON is produced without "
            "assertion failure; proceed to novelty/publication consolidation"
        ),
    }

    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(
        json.dumps(result, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )

    print("PIFI-3D FINAL CLASSIFICATION / NECESSITY-SUFFICIENCY CONTROL")
    print("FINAL CONTROL PASS")
    print("full graph cases:", graph_chain["cases"])
    print("full graph chirality cases:", graph_chain["chirality_cases"])
    print("max n:", graph_chain["max_n"])
    print("generic CRT sampled checks:", generic_crt["sampled_pair_checks"])
    print(
        "generic CRT exhaustive anchor pairs:",
        generic_crt["exhaustive_anchor"]["pairs"],
    )
    print("extended arithmetic cases:", extended["cases"])
    print(
        "future-language cross-CRT collisions:",
        graph_chain["future_language_cross_CRT_collisions"],
    )
    print("mathematical branch recommendation: FREEZE")


if __name__ == "__main__":
    main()
