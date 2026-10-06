#!/usr/bin/env python3
"""PIFI-3D CRT / prime-power placement classification gate v0.1.

Classifies the remaining diagonal unit orbit

    [(s,rho)]_{U(n)}

from the affine-placement theorem, where rho lives modulo d=d_AB and d|n.

Prime-power theorem
-------------------
Write

    n = product_p p^e_p,
    d = product_p p^f_p,   0 <= f_p <= e_p.

For one prime p define truncated valuations

    a_p = min(v_p(s), e_p),
    b_p = min(v_p(rho), f_p).

If a_p<e_p and b_p<f_p, put

    m_p = min(e_p-a_p, f_p-b_p)

and define the relative unit ratio

    r_p =
      (rho / p^b_p) * (s / p^a_p)^(-1)
      mod p^m_p.

If one coordinate is zero at that prime, m_p=0 and no ratio is needed.

Then two pairs (s,rho) and (s',rho') are in the same diagonal U(n)-orbit
iff for every p|n they have the same

    (a_p,b_p,m_p,r_p).

Thus the finite orbit search chi is replaced exactly by a CRT tuple of
p-adic valuations plus one relative unit ratio on each common nonzero
prime-power layer.

The proof works uniformly for p=2; there is no exceptional 2-adic case.

Regression defaults
-------------------
1. Generic theorem: all n=2..64, all d|n, all (s,rho) in Z_n x Z_d.
   146965 pairs.  CRT signatures and explicit U(n) orbits are bijective.
2. PIFI family q=2..8: all 70574 admissible triples.
   Old affine classes = CRT classes = 862, with a one-to-one map.
3. Extended PIFI family q=2..12: 349294 triples -> 2665 CRT placement classes.
"""

from __future__ import annotations

import argparse
import json
import math
from collections import defaultdict
from pathlib import Path


def factor(n):
    out = []
    m = n
    p = 2
    while p * p <= m:
        if m % p == 0:
            e = 0
            while m % p == 0:
                m //= p
                e += 1
            out.append((p, e))
        p = 3 if p == 2 else p + 2
    if m > 1:
        out.append((m, 1))
    return out


def units(n):
    return [u for u in range(n) if math.gcd(u, n) == 1]


def divisors(n):
    return [d for d in range(1, n + 1) if n % d == 0]


def exponent_in_divisor(d, p):
    f = 0
    while d % p == 0:
        d //= p
        f += 1
    return f


def truncated_vp_residue(x, p, e):
    mod = p ** e
    x %= mod
    if x == 0:
        return e
    a = 0
    while x % p == 0:
        x //= p
        a += 1
    return a


def local_prime_power_invariant(s, rho, n, d):
    """Complete CRT invariant for diagonal U(n) action on Z_n x Z_d."""
    out = []

    for p, e in factor(n):
        f = exponent_in_divisor(d, p)
        a = truncated_vp_residue(s, p, e)

        if f == 0:
            out.append({
                "p": p, "e": e, "f": 0,
                "a": a, "b": 0, "m": 0, "ratio": None,
            })
            continue

        b = truncated_vp_residue(rho, p, f)

        if a < e and b < f:
            m = min(e - a, f - b)
            mod = p ** m
            s_unit = (s // (p ** a)) % mod
            r_unit = (rho // (p ** b)) % mod
            ratio = (r_unit * pow(s_unit, -1, mod)) % mod
        else:
            m = 0
            ratio = None

        out.append({
            "p": p, "e": e, "f": f,
            "a": a, "b": b, "m": m, "ratio": ratio,
        })

    return tuple(
        (r["p"], r["e"], r["f"], r["a"], r["b"], r["m"], r["ratio"])
        for r in out
    )


def explicit_unit_orbit(s, rho, n, d):
    return tuple(sorted({
        (u * s % n, u * rho % d)
        for u in units(n)
    }))


def canonical_orbit_pair(s, rho, n, d):
    return min(explicit_unit_orbit(s, rho, n, d))


def verify_generic_pair_theorem(n_max):
    total = 0

    for n in range(2, n_max + 1):
        for d in divisors(n):
            inv_to_orbit = {}
            orbit_to_inv = {}

            for s in range(n):
                for rho in range(d):
                    inv = local_prime_power_invariant(s, rho, n, d)
                    orb = explicit_unit_orbit(s, rho, n, d)

                    if inv in inv_to_orbit:
                        assert inv_to_orbit[inv] == orb, (n, d, s, rho)
                    else:
                        inv_to_orbit[inv] = orb

                    if orb in orbit_to_inv:
                        assert orbit_to_inv[orb] == inv, (n, d, s, rho)
                    else:
                        orbit_to_inv[orb] = inv

                    total += 1

    return {
        "n_range": [2, n_max],
        "pairs": total,
        "signature_to_orbit_mismatches": 0,
        "orbit_to_signature_mismatches": 0,
    }


def admissible_triples(n):
    for delta in range(1, n):
        for c_ab in range(1, n):
            for c_bc in range(1, n):
                if c_bc == n // 2:
                    continue
                yield delta, c_ab, c_bc


def placement_pair(n, delta, c_ab, c_bc):
    s = (2 * (delta + c_ab + c_bc)) % n
    d_ab = math.gcd(n, c_ab)
    d_bc = math.gcd(n, c_bc)
    rho = c_bc % d_ab
    return s, rho, d_ab, d_bc


def old_affine_key(n, delta, c_ab, c_bc):
    s, rho, d_ab, d_bc = placement_pair(n, delta, c_ab, c_bc)
    chi = canonical_orbit_pair(s, rho, n, d_ab)
    return (n, d_ab, d_bc, chi)


def crt_key(n, delta, c_ab, c_bc):
    s, rho, d_ab, d_bc = placement_pair(n, delta, c_ab, c_bc)
    psi = local_prime_power_invariant(s, rho, n, d_ab)
    return (n, d_ab, d_bc, psi)


def verify_family_bijection(q_max):
    total = 0
    old_classes = set()
    crt_classes = set()
    old_to_crt = {}
    crt_to_old = {}

    for q in range(2, q_max + 1):
        n = 4 * q

        for triple in admissible_triples(n):
            old = old_affine_key(n, *triple)
            crt = crt_key(n, *triple)

            if old in old_to_crt:
                assert old_to_crt[old] == crt
            else:
                old_to_crt[old] = crt

            if crt in crt_to_old:
                assert crt_to_old[crt] == old
            else:
                crt_to_old[crt] = old

            old_classes.add(old)
            crt_classes.add(crt)
            total += 1

    assert len(old_classes) == len(crt_classes)

    return {
        "q_range": [2, q_max],
        "triples": total,
        "old_affine_classes": len(old_classes),
        "crt_classes": len(crt_classes),
        "bijection_mismatches": 0,
    }


def extended_family_census(q_max):
    total = 0
    classes = set()
    per_n = {}

    for q in range(2, q_max + 1):
        n = 4 * q
        local = set()
        count = 0

        for triple in admissible_triples(n):
            key = crt_key(n, *triple)
            local.add(key)
            classes.add(key)
            count += 1

        per_n[str(n)] = {
            "triples": count,
            "crt_classes": len(local),
        }
        total += count

    return {
        "q_range": [2, q_max],
        "triples": total,
        "crt_classes": len(classes),
        "per_n": per_n,
    }


def witnesses():
    # Previous n=12 affine equivalence:
    # (s,rho,d) = (10,1,3) and (2,2,3).
    A = local_prime_power_invariant(10, 1, 12, 3)
    B = local_prime_power_invariant(2, 2, 12, 3)
    assert A == B

    # Previous gcd-only failure:
    # (10,1) and (2,1) have same simple gcd data but different p=3 ratio.
    C = local_prime_power_invariant(2, 1, 12, 3)
    assert A != C

    # Prime-power witness showing the ratio can require modulus p^m, m>1.
    P1 = local_prime_power_invariant(2, 2, 16, 8)
    P2 = local_prime_power_invariant(2, 6, 16, 8)
    assert P1 != P2

    return {
        "n12_affine_equivalence": {
            "pair_A": [10, 1],
            "pair_B": [2, 2],
            "d": 3,
            "same_CRT_signature": True,
            "local_explanation": (
                "at p=3 both have a=b=0 and relative ratio 1 mod 3"
            ),
        },
        "n12_gcd_only_failure": {
            "pair_A": [10, 1],
            "pair_B": [2, 1],
            "d": 3,
            "same_simple_gcd_data": True,
            "same_CRT_signature": False,
            "local_explanation": (
                "at p=3 the relative ratios are 1 and 2 mod 3"
            ),
        },
        "n16_prime_power_ratio": {
            "pair_A": [2, 2],
            "pair_B": [2, 6],
            "d": 8,
            "same_valuations": True,
            "same_CRT_signature": False,
            "local_explanation": (
                "at p=2: a=b=1, m=2, ratios are 1 and 3 mod 4"
            ),
        },
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--generic-n-max", type=int, default=64)
    ap.add_argument("--family-bijection-q-max", type=int, default=8)
    ap.add_argument("--extended-q-max", type=int, default=12)
    ap.add_argument(
        "--output",
        type=Path,
        default=Path(
            "docs/results/pifi_3d_crt_prime_power_placement_v0_1.json"
        ),
    )
    args = ap.parse_args()

    generic = verify_generic_pair_theorem(args.generic_n_max)
    family = verify_family_bijection(args.family_bijection_q_max)
    extended = extended_family_census(args.extended_q_max)
    w = witnesses()

    result = {
        "schema": "pifi.3d.crt_prime_power_placement.v0.1",
        "date": "2026-10-06",
        "status": "STRONG PASS — COMPLETE CRT / PRIME-POWER CLASSIFICATION",
        "theorem": {
            "action": "(s,rho) -> (u*s mod n, u*rho mod d), u in U(n), d|n",
            "local_data": {
                "a_p": "min(v_p(s),e_p)",
                "b_p": "min(v_p(rho),f_p)",
                "m_p": "min(e_p-a_p,f_p-b_p) when both coordinates are nonzero",
                "r_p": "(rho/p^b_p)*(s/p^a_p)^(-1) mod p^m_p",
            },
            "criterion": (
                "same global U(n)-orbit iff all local "
                "(a_p,b_p,m_p,r_p) agree"
            ),
            "CRT": "global orbit is the product of the local prime-power orbits",
        },
        "regression": {
            "generic_pair_theorem": generic,
            "PIFI_family_bijection": family,
            "extended_family_census": extended,
        },
        "witnesses": w,
        "interpretation": [
            "The finite unit-orbit search chi is eliminated exactly.",
            "Valuations alone are insufficient whenever both coordinates survive at the same prime.",
            "The only extra datum is a relative unit ratio modulo the overlap p^m.",
            "The theorem works without an exceptional p=2 branch.",
        ],
        "next_gate": (
            "FINAL CLASSIFICATION / NECESSITY-SUFFICIENCY CONTROL: "
            "integrate the CRT placement signature with the component-orbit "
            "predictor and stress-test the full chain against graph routing."
        ),
    }

    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(
        json.dumps(result, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )

    print("PIFI-3D CRT / PRIME-POWER PLACEMENT GATE: STRONG PASS")
    print(generic)
    print(family)
    print(extended)
    print("finite unit-orbit search: ELIMINATED")
    print("p-adic valuation + relative-unit taxonomy: COMPLETE")


if __name__ == "__main__":
    main()
