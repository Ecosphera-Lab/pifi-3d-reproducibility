#!/usr/bin/env python3
"""PIFI-3D split AB/BC annular-offset generalization v0.1.

Family
------
n = 4q, q >= 2.

AA is gauge-fixed to
    A_i, X_i ~ Y_i, Y_{i-delta},     delta != 0 mod n.

AB and BC get independent annular offsets:
    Z_i ~ A_i, A_{i+cAB}, B_i, B_{i+cAB},
    W_i ~ B_i, B_{i+cBC}, C_i, C_{i+cBC}.

Simple-graph admissibility:
    delta != 0,
    cAB != 0,
    cBC != 0,
    cBC != n/2.

Main routed theorem
-------------------
Define
    s = 2(delta + cAB + cBC) mod n.

With frame entries
    L_j = W_j -> B_j,
    R_j = W_j -> B_{j+cBC},

HT+ has
    L_j -> L_{j-s}                       through C3,
except when j-(s-cBC) is cardinal, where
    L_j -> R_{j+n/2-(s-cBC)}             through C6;

    R_j -> R_{j+n/2+s}                   through C20,
except when j+s is cardinal, where
    R_j -> L_{j+n/2+s-cBC}               through C6.

After reduction mod q and translations
    x = j-(s-cBC) on L,
    y = j+s       on R,
the system is exactly canonical A(q,s).

Hence the current routed terminal quotient still retains only ONE affine
combination:
    s = 2(delta+cAB+cBC).

Microscopic graph invariants
----------------------------
AB-only component count:
    hAB = gcd(n,cAB).

Let dBC = gcd(n,cBC).  Before cardinal C identifications the BC-only
subgraph has dBC components.  The identifications C0~C_{n/2} and
C_q~C_{3q} are either internal to components (if dBC | n/2), or merge
two independent pairs.  Thus
    hBC = dBC                         if dBC | n/2,
          dBC - 2                     otherwise.

So cAB and cBC are independently visible in the labelled graph even
when routed future data is identical.

Default regression
------------------
1) exhaustive HT+ macro: q=2..6, all admissible triples
       22790 cases.
2) exhaustive full future/census: q=2..4, all triples, both chiralities
       9308 cases.
3) representative full future/census: q=2..8, one per
       (q,s,hAB,hBC), both chiralities
       1310 classes / 2620 cases.
"""

from __future__ import annotations

import argparse
import json
import math
from collections import Counter, defaultdict
from pathlib import Path


def primitive(word):
    n = len(word)
    for d in range(1, n + 1):
        if n % d == 0 and all(word[i] == word[i % d] for i in range(n)):
            return word[:d]
    return word


def minrot(word):
    t = tuple(word)
    return min(t[i:] + t[:i] for i in range(len(t)))


def exact_kmin(roots):
    symbols = {}
    for root in roots:
        for x in root:
            if x not in symbols:
                symbols[x] = chr(len(symbols) + 1)

    coded = [[symbols[x] for x in root] for root in roots]
    max_period = max(map(len, coded))
    bound = 2 * max_period + 1

    phases = []
    for root in coded:
        p = len(root)
        base = "".join(root)
        repeated = base * ((bound + p - 1) // p + 2)
        phases.extend(repeated[s:s + bound] for s in range(p))

    phases.sort()
    max_lcp = 0

    for a, b in zip(phases, phases[1:]):
        k = 0
        while k < bound and a[k] == b[k]:
            k += 1
        max_lcp = max(max_lcp, k)

    assert max_lcp < bound
    return max_lcp + 1


def build(n, delta, c_ab, c_bc, sign):
    assert n % 4 == 0 and n >= 8

    delta %= n
    c_ab %= n
    c_bc %= n

    assert delta != 0
    assert c_ab != 0
    assert c_bc != 0
    assert c_bc != n // 2

    q = n // 4
    seam = {0, q, 2 * q, 3 * q}

    def M(i):
        return i % n

    def qv(v):
        if v in ("C0", f"C{2*q}"):
            return "Dx"
        if v in (f"C{q}", f"C{3*q}"):
            return "Dy"
        return v

    edges = []

    def add(u, v, fam):
        edges.append((qv(u), qv(v), fam))

    for i in range(n):
        # OA
        add("O", f"X{i}", "OA")
        add(f"X{i}", f"A{i}", "OA")

        # AA
        for off in (0, delta):
            add(f"A{i}", f"Y{M(i-off)}", "AA")
            add(f"X{i}", f"Y{M(i-off)}", "AA")

        # AB with c_ab
        add(f"A{i}", f"Z{i}", "AB")
        add(f"Z{i}", f"B{M(i+c_ab)}", "AB")
        add(f"A{M(i+c_ab)}", f"Z{i}", "AB")
        add(f"Z{i}", f"B{i}", "AB")

        # AC
        add(f"A{i}", f"B{i}", "AC")
        add(f"B{i}", f"C{i}", "AC")

        # BC with c_bc
        add(f"B{i}", f"W{i}", "BC")
        add(f"W{i}", f"C{M(i+c_bc)}", "BC")
        add(f"B{M(i+c_bc)}", f"W{i}", "BC")
        add(f"W{i}", f"C{i}", "BC")

    assert len(edges) == 16 * n

    adj = defaultdict(list)
    pair_eid = {}

    for eid, (u, v, fam) in enumerate(edges):
        assert (u, v) not in pair_eid, (n, delta, c_ab, c_bc, u, v)
        adj[u].append((eid, v))
        adj[v].append((eid, u))
        pair_eid[(u, v)] = eid
        pair_eid[(v, u)] = eid

    degree = {v: len(rows) for v, rows in adj.items()}

    assert len(adj) == 7 * n - 1
    assert Counter(degree.values()) == Counter({
        3: n - 4,
        4: 4 * n,
        6: 2 * n + 2,
        n: 1,
    })

    def eid(v, w):
        return pair_eid[(v, qv(w))]

    rot = {"O": [eid("O", f"X{i}") for i in range(n)]}

    for i in range(n):
        rot[f"X{i}"] = [
            eid(f"X{i}", f"Y{M(i-delta)}"),
            eid(f"X{i}", "O"),
            eid(f"X{i}", f"Y{i}"),
            eid(f"X{i}", f"A{i}"),
        ]

        rot[f"Y{i}"] = [
            eid(f"Y{i}", f"X{i}"),
            eid(f"Y{i}", f"X{M(i+delta)}"),
            eid(f"Y{i}", f"A{M(i+delta)}"),
            eid(f"Y{i}", f"A{i}"),
        ]

        rot[f"Z{i}"] = [
            eid(f"Z{i}", f"A{i}"),
            eid(f"Z{i}", f"A{M(i+c_ab)}"),
            eid(f"Z{i}", f"B{M(i+c_ab)}"),
            eid(f"Z{i}", f"B{i}"),
        ]

        rot[f"W{i}"] = [
            eid(f"W{i}", f"B{i}"),
            eid(f"W{i}", f"B{M(i+c_bc)}"),
            eid(f"W{i}", f"C{M(i+c_bc)}"),
            eid(f"W{i}", f"C{i}"),
        ]

        rot[f"A{i}"] = [
            eid(f"A{i}", f"Y{M(i-delta)}"),
            eid(f"A{i}", f"Z{M(i-c_ab)}"),
            eid(f"A{i}", f"B{i}"),
            eid(f"A{i}", f"Z{i}"),
            eid(f"A{i}", f"Y{i}"),
            eid(f"A{i}", f"X{i}"),
        ]

        rot[f"B{i}"] = [
            eid(f"B{i}", f"Z{M(i-c_ab)}"),
            eid(f"B{i}", f"A{i}"),
            eid(f"B{i}", f"Z{i}"),
            eid(f"B{i}", f"W{i}"),
            eid(f"B{i}", f"C{i}"),
            eid(f"B{i}", f"W{M(i-c_bc)}"),
        ]

    for i in range(n):
        if i not in seam:
            rot[f"C{i}"] = [
                eid(f"C{i}", f"B{i}"),
                eid(f"C{i}", f"W{i}"),
                eid(f"C{i}", f"W{M(i-c_bc)}"),
            ]

    rot["Dx"] = [
        eid("Dx", "B0"),
        eid("Dx", "W0"),
        eid("Dx", f"W{M(-c_bc)}"),
        eid("Dx", f"B{2*q}"),
        eid("Dx", f"W{2*q}"),
        eid("Dx", f"W{M(2*q-c_bc)}"),
    ]

    rot["Dy"] = [
        eid("Dy", f"B{q}"),
        eid("Dy", f"W{q}"),
        eid("Dy", f"W{M(q-c_bc)}"),
        eid("Dy", f"B{3*q}"),
        eid("Dy", f"W{3*q}"),
        eid("Dy", f"W{M(3*q-c_bc)}"),
    ]

    assert set(rot) == set(adj)

    darts = []
    did = {}
    uv_did = {}

    for e, (u, v, fam) in enumerate(edges):
        for x, y in ((u, v), (v, u)):
            k = len(darts)
            darts.append((e, x, y))
            did[(e, x, y)] = k
            uv_did[(x, y)] = k

    assert len(darts) == 32 * n

    P = [0] * len(darts)

    for k, (e, u, v) in enumerate(darts):
        R = rot[v]
        p = R.index(e)
        d = len(R)

        if d % 2 == 0:
            j = (p + d // 2) % d
        else:
            j = (p + (1 if sign == "+" else -1)) % d

        ne = R[j]
        x, y, _ = edges[ne]
        w = y if x == v else x
        P[k] = did[(ne, v, w)]

    assert len(set(P)) == len(P)

    entry = {}
    for k in range(n):
        entry[uv_did[(f"W{k}", f"B{k}")]] = ("L", k)
        entry[uv_did[(f"W{k}", f"B{M(k+c_bc)}")]] = ("R", k)

    return {
        "n": n,
        "q": q,
        "delta": delta,
        "c_ab": c_ab,
        "c_bc": c_bc,
        "edges": edges,
        "degree": degree,
        "darts": darts,
        "P": P,
        "uv_did": uv_did,
        "entry": entry,
    }


def macro_transition(G, layer, j):
    n = G["n"]
    c_bc = G["c_bc"]

    if layer == "L":
        cur = G["uv_did"][(f"W{j}", f"B{j}")]
    else:
        cur = G["uv_did"][(f"W{j}", f"B{(j+c_bc)%n}")]

    steps = 0

    while True:
        cur = G["P"][cur]
        steps += 1
        if cur in G["entry"]:
            return G["entry"][cur], steps


def h_bc_formula(n, c_bc):
    d = math.gcd(n, c_bc)
    return d if (n // 2) % d == 0 else d - 2


def invariant_parameters(n, delta, c_ab, c_bc):
    q = n // 4
    lam = (delta + c_ab + c_bc) % (n // 2)
    s = (2 * (delta + c_ab + c_bc)) % n
    g = math.gcd(q, s)
    m = q // g
    return {
        "lambda": lam,
        "s": s,
        "g": g,
        "m": m,
        "h_AB": math.gcd(n, c_ab),
        "h_BC": h_bc_formula(n, c_bc),
    }


def predicted(n, delta, c_ab, c_bc):
    q = n // 4
    p = invariant_parameters(n, delta, c_ab, c_bc)

    s = p["s"]
    g = p["g"]
    m = p["m"]

    if g == 1:
        Q = 32 * q
        periods = [8, 32 * m - 8]
    elif m == 1:
        Q = 52
        periods = [8, 12, 12, 20]
    else:
        Q = 32 * (m + 1)
        periods = [8, 12, 20, 32 * m - 8]

    if m == 1:
        kmin = 13
    elif g == 1 and m == 2:
        kmin = 25
    elif g == 1:
        kmin = 20 * m - 29
    else:
        kmin = 20 * m - 9

    dL = math.gcd(n, s)
    hitL = dL // math.gcd(dL, q)
    cL = dL - hitL
    lenL = 12 * n // dL

    dR = math.gcd(n, n // 2 + s)
    hitR = dR // math.gcd(dR, q)
    cR = dR - hitR
    lenR = 20 * n // dR

    cM = 4 if m % 2 else 2
    baseM = 32 * m - 8
    lenM = baseM if m % 2 else 2 * baseM

    hist = Counter({8: 4})
    if cL:
        hist[lenL] += cL
    if cR:
        hist[lenR] += cR
    hist[lenM] += cM

    return {
        **p,
        "Q": Q,
        "periods": periods,
        "k_min": kmin,
        "cycle_histogram": hist,
    }


def family_component_count(G, family):
    adj = defaultdict(set)
    vertices = set()

    for u, v, fam in G["edges"]:
        if fam != family:
            continue
        adj[u].add(v)
        adj[v].add(u)
        vertices.add(u)
        vertices.add(v)

    seen = set()
    count = 0

    for start in vertices:
        if start in seen:
            continue

        count += 1
        seen.add(start)
        stack = [start]

        while stack:
            x = stack.pop()
            for y in adj[x]:
                if y not in seen:
                    seen.add(y)
                    stack.append(y)

    return count


def verify_macro_formula(G):
    n = G["n"]
    q = G["q"]
    delta = G["delta"]
    c_ab = G["c_ab"]
    c_bc = G["c_bc"]

    seam = {0, q, 2 * q, 3 * q}
    p = invariant_parameters(n, delta, c_ab, c_bc)
    s = p["s"]

    for j in range(n):
        got, steps = macro_transition(G, "L", j)

        if (j - (s - c_bc)) % n in seam:
            want = ("R", (j + n // 2 - (s - c_bc)) % n)
        else:
            want = ("L", (j - s) % n)

        assert got == want, ("L", n, delta, c_ab, c_bc, s, j, got, want)
        assert steps == 12

        got, steps = macro_transition(G, "R", j)

        if (j + s) % n in seam:
            want = ("L", (j + n // 2 + s - c_bc) % n)
            want_steps = 12
        else:
            want = ("R", (j + n // 2 + s) % n)
            want_steps = 20

        assert got == want, ("R", n, delta, c_ab, c_bc, s, j, got, want)
        assert steps == want_steps

    assert family_component_count(G, "AB") == p["h_AB"]
    assert family_component_count(G, "BC") == p["h_BC"]


def analyze(G):
    darts = G["darts"]
    P = G["P"]
    edges = G["edges"]
    degree = G["degree"]

    def terminal(k):
        e, u, v = darts[k]
        return f"{edges[e][2]}|{degree[u]}|{degree[v]}"

    seen = set()
    cycles = []

    for start in range(len(darts)):
        if start in seen:
            continue

        cyc = []
        x = start

        while x not in seen:
            seen.add(x)
            cyc.append(x)
            x = P[x]

        assert x == start
        cycles.append(cyc)

    classes = {}

    for cyc in cycles:
        root = primitive([terminal(x) for x in cyc])
        key = (len(root), minrot(root))
        classes[key] = classes.get(key, 0) + 1

    roots = [list(key[1]) for key in classes]

    return {
        "cycle_histogram": Counter(map(len, cycles)),
        "primitive_periods": sorted(key[0] for key in classes),
        "future_states": sum(key[0] for key in classes),
        "k_min": exact_kmin(roots),
    }


def verify_full_case(n, delta, c_ab, c_bc, sign):
    G = build(n, delta, c_ab, c_bc, sign)
    got = analyze(G)
    pred = predicted(n, delta, c_ab, c_bc)

    assert got["cycle_histogram"] == pred["cycle_histogram"]
    assert got["primitive_periods"] == pred["periods"]
    assert got["future_states"] == pred["Q"]
    assert got["k_min"] == pred["k_min"]

    assert family_component_count(G, "AB") == pred["h_AB"]
    assert family_component_count(G, "BC") == pred["h_BC"]


def admissible_triples(n):
    for delta in range(1, n):
        for c_ab in range(1, n):
            for c_bc in range(1, n):
                if c_bc == n // 2:
                    continue
                yield delta, c_ab, c_bc


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--macro-q-max", type=int, default=6)
    ap.add_argument("--full-q-max", type=int, default=4)
    ap.add_argument("--representative-q-max", type=int, default=8)
    ap.add_argument(
        "--output",
        type=Path,
        default=Path("docs/results/pifi_3d_tn_split_annular_offset_v0_1.json"),
    )
    args = ap.parse_args()

    macro_cases = 0
    for q in range(2, args.macro_q_max + 1):
        n = 4 * q
        for delta, c_ab, c_bc in admissible_triples(n):
            G = build(n, delta, c_ab, c_bc, "+")
            verify_macro_formula(G)
            macro_cases += 1

    exhaustive_full_cases = 0
    for q in range(2, args.full_q_max + 1):
        n = 4 * q
        for delta, c_ab, c_bc in admissible_triples(n):
            for sign in ("+", "-"):
                verify_full_case(n, delta, c_ab, c_bc, sign)
                exhaustive_full_cases += 1

    reps = {}
    for q in range(2, args.representative_q_max + 1):
        n = 4 * q
        for delta, c_ab, c_bc in admissible_triples(n):
            p = invariant_parameters(n, delta, c_ab, c_bc)
            key = (q, p["s"], p["h_AB"], p["h_BC"])
            reps.setdefault(key, (delta, c_ab, c_bc))

    representative_full_cases = 0
    for (q, s, h_ab, h_bc), triple in sorted(reps.items()):
        n = 4 * q
        delta, c_ab, c_bc = triple
        for sign in ("+", "-"):
            verify_full_case(n, delta, c_ab, c_bc, sign)
            representative_full_cases += 1

    # Independent microscopic witnesses at n=12, all with s=6.
    witnesses = [
        (1, 1, 1),
        (1, 3, 5),
        (1, 5, 3),
        (1, 4, 4),
    ]

    witness_rows = []
    for delta, c_ab, c_bc in witnesses:
        p = predicted(12, delta, c_ab, c_bc)
        assert p["s"] == 6
        assert p["Q"] == 52
        assert p["k_min"] == 13
        witness_rows.append({
            "delta": delta,
            "c_AB": c_ab,
            "c_BC": c_bc,
            "s": p["s"],
            "h_AB": p["h_AB"],
            "h_BC": p["h_BC"],
            "Q": p["Q"],
            "k_min": p["k_min"],
        })

    assert witness_rows[0]["h_AB"] != witness_rows[1]["h_AB"]
    assert witness_rows[0]["h_BC"] != witness_rows[2]["h_BC"]

    result = {
        "schema": "pifi.3d.tn_split_annular_offset.v0.1",
        "status": "STRONG PASS — SPLIT AB/BC OFFSETS STILL COLLAPSE MACROSCOPICALLY",
        "macro": {
            "lambda": "delta+c_AB+c_BC mod n/2",
            "s": "2(delta+c_AB+c_BC) mod n",
            "reduction": "canonical A(q,s)",
            "Q52": "q divides 2(delta+c_AB+c_BC)",
        },
        "microscopic": {
            "h_AB": "gcd(n,c_AB)",
            "h_BC": "d_BC if d_BC divides n/2, else d_BC-2; d_BC=gcd(n,c_BC)",
            "witnesses_n12": witness_rows,
        },
        "regression": {
            "macro_q_range": [2, args.macro_q_max],
            "macro_cases": macro_cases,
            "macro_mismatches": 0,
            "exhaustive_full_q_range": [2, args.full_q_max],
            "exhaustive_full_chirality_cases": exhaustive_full_cases,
            "exhaustive_full_mismatches": 0,
            "representative_q_range": [2, args.representative_q_max],
            "representative_classes": len(reps),
            "representative_full_chirality_cases": representative_full_cases,
            "representative_full_mismatches": 0,
        },
        "interpretation": [
            "c_AB and c_BC are independently visible in the labelled graph.",
            "The current routed terminal quotient does not retain them independently.",
            "At macro/future level delta,c_AB,c_BC collapse to lambda=delta+c_AB+c_BC.",
        ],
    }

    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(
        json.dumps(result, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )

    print("PIFI-3D SPLIT AB/BC ANNULAR-OFFSET GATE: STRONG PASS")
    print(f"macro cases: {macro_cases}")
    print(f"exhaustive full chirality cases: {exhaustive_full_cases}")
    print(f"representative classes: {len(reps)}")
    print(f"representative full chirality cases: {representative_full_cases}")
    print("mismatches: 0")
    print("s = 2(delta+c_AB+c_BC) mod n")
    print("routed system still retains one affine combination only")


if __name__ == "__main__":
    main()
