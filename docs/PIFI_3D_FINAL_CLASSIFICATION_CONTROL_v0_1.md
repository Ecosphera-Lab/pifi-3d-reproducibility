# PIFI-3D — FINAL CLASSIFICATION / NECESSITY-SUFFICIENCY CONTROL v0.1

**Date:** 2026-10-06  
**Branch:** \`agent/pifi-3d-final-classification-control-v01\`  
**Verdict:** **FINAL CONTROL PASS — FREEZE MATHEMATICAL BRANCH**

## 1. Purpose

This stage introduces no new graph parameter and no new observation rule.

Its only purpose is to attempt to break the already frozen chain

\[
\text{full graph}
\to
\text{macro theorem}
\to
\text{refined terminal observation}
\to
\text{component-orbit predictor}
\to
\text{affine placement class}
\to
\text{CRT / prime-power classifier}.
\]

The control deliberately includes:

- small anchor sizes;
- prime \(q\);
- prime-power \(q\);
- highly composite / gcd-rich \(q\);
- forced \(s=0\);
- forced \(s=2\);
- forced half-turn \(s=n/2\);
- offsets adjacent to the excluded BC half-turn seam;
- both HT+ and HT−.

The stage also separates clearly what is necessary-and-sufficient from what is only sufficient.

---

## 2. Frozen chain under test

The split-annular family is

\[
\mathcal T_{n;\delta,c_{AB},c_{BC}},
\qquad
n=4q.
\]

The already proved macro shift is

\[
\boxed{
s=2(\delta+c_{AB}+c_{BC})\pmod n.
}
\]

The coarse routed system reduces to

\[
\mathcal A(q,s).
\]

The refined observation adds exact AB/BC component labels.

The refined quotient is predicted without full graph traversal by the component-orbit formula

\[
\boxed{
Q_{\rm comp}
=
8+
\sum_{[W]}
|\operatorname{prim}(W)|.
}
\]

The affine placement invariant is

\[
\Theta=
(n,d_{AB},d_{BC},[(s,\rho)]_{U(n)}),
\]

with

\[
d_{AB}=\gcd(n,c_{AB}),
\]

\[
d_{BC}=\gcd(n,c_{BC}),
\]

\[
\rho=c_{BC}\pmod{d_{AB}}.
\]

Finally the diagonal unit orbit is classified prime by prime by

\[
\boxed{
\Psi=
\{(a_p,b_p,m_p,r_p)\}_{p\mid n}.
}
\]

---

## 3. Full-graph adversarial control

The final full-graph control used the following \(q\)-groups.

### Small anchors

\[
q\in\{2,3,4\}.
\]

### Prime q

\[
q\in\{5,7,11,13,17,19\}.
\]

### Prime-power q

\[
q\in\{8,9,16,25,27\}.
\]

### GCD-rich / highly composite q

\[
q\in\{6,12,18,24,30\}.
\]

For each size, deterministic adversarial triples were generated from:

- first-neighbor offsets;
- large gcd offsets;
- \(c_{AB}=n/2\);
- \(c_{BC}=n/2\pm1\);
- near-maximal offsets;
- values chosen to force special macro shifts.

Total full graph parameter cases:

\[
\boxed{152}.
\]

Maximum tested graph size:

\[
\boxed{n=120}.
\]

Among these cases:

\[
\boxed{40}
\]

had

\[
s=0,
\]

\[
\boxed{21}
\]

had

\[
s=2,
\]

and

\[
\boxed{20}
\]

had

\[
s=n/2.
\]

---

## 4. Full graph → macro theorem

For every one of the 152 HT+ graphs, the frame-entry transitions were traced directly on the full \(32n\)-dart routed graph.

They were compared with the frozen split-annular macro theorem.

Checked:

\[
L_j
\]

regular and seam transitions,

\[
R_j
\]

regular and seam transitions,

exact frame lengths

\[
12,\ 12,\ 20,
\]

and the graph component formulas

\[
h_{AB}=\gcd(n,c_{AB})
\]

and the previously derived BC component formula.

Result:

\[
\boxed{152/152\text{ PASS}}.
\]

Mismatches:

\[
\boxed0.
\]

---

## 5. Coarse future classification on both chiralities

Every adversarial parameter case was then tested for both

\[
HT+
\]

and

\[
HT-.
\]

Total coarse full-graph chirality cases:

\[
\boxed{304}.
\]

For every case the full graph result was compared with the exact \(\mathcal A(q,s)\) prediction for:

- routed cycle histogram;
- primitive terminal periods;
- \(Q\);
- exact \(k_{\min}\).

Result:

\[
\boxed{304/304\text{ PASS}}.
\]

Mismatches:

\[
\boxed0.
\]

---

## 6. Full refined graph → component-orbit predictor

For every HT+ adversarial case, the refined future language was computed in two completely different ways.

### Method A — full graph

Use all

\[
32n
\]

routed darts and the exact component-aware terminal alphabet.

### Method B — component-orbit theorem

Use only the

\[
2n
\]

macro frame states and the analytic component placement laws.

The comparison was made on the entire primitive cyclic future signature, not only on \(Q_{\rm comp}\).

Total:

\[
\boxed{152}
\]

independent comparisons.

For every case:

- primitive decorated future signature matched;
- primitive-period multiset matched;
- \(Q_{\rm comp}\) matched.

Result:

\[
\boxed{152/152\text{ PASS}}.
\]

Mismatches:

\[
\boxed0.
\]

---

## 7. Refined chirality control

For all 152 parameter triples the exact refined observation was also computed on HT−.

Thus there were

\[
\boxed{304}
\]

refined chirality instances.

For every triple,

\[
HT+
\]

and

\[
HT-
\]

agreed in:

\[
Q_{\rm comp},
\]

primitive-period multiset,

and

\[
k_{\min,\rm comp}.
\]

Result:

\[
\boxed{304/304\text{ PASS}}.
\]

Mismatches:

\[
\boxed0.
\]

This control does not claim literal equality of oriented future words under chirality reversal; it confirms equality of the quotient invariants used in this branch.

---

## 8. Original PIFI anchor

The original point remains

\[
n=12,
\qquad
(\delta,c_{AB},c_{BC})=(1,1,1).
\]

For HT+:

\[
\boxed{
Q_{\rm coarse}=52,
\qquad
Q_{\rm comp}=52,
\qquad
k_{\min}=13,
}
\]

with primitive periods

\[
\boxed{
8,\ 12,\ 12,\ 20.
}
\]

For HT− exactly the same values were recovered.

Thus the original PIFI result survives every refinement and every final control layer used in this branch.

---

## 9. Frozen negative anchors also survive

The earlier placement counterexample remains intact.

At

\[
n=24,
\]

\[
(\delta,c_{AB},c_{BC})=(1,7,6)
\]

gives

\[
\boxed{Q_{\rm comp}=192},
\]

whereas

\[
(1,5,8)
\]

gives

\[
\boxed{Q_{\rm comp}=312}.
\]

So the final control did not accidentally erase the previously established need for component-placement information.

The three CRT witnesses also remain unchanged:

\[
(10,1)\sim(2,2)
\quad
\text{in }\mathbb Z_{12}\times\mathbb Z_3,
\]

while

\[
(10,1)\not\sim(2,1),
\]

and

\[
(2,2)\not\sim(2,6)
\quad
\text{in }\mathbb Z_{16}\times\mathbb Z_8.
\]

---

## 10. CRT necessity-and-sufficiency control

The strongest exact iff statement in the final chain is:

\[
\boxed{
\Psi(s,\rho)=\Psi(s',\rho')
\iff
(s,\rho),(s',\rho')
\text{ lie in the same diagonal }U(n)\text{-orbit}.
}
\]

This was rechecked independently by explicit unit-orbit enumeration.

### Generic exhaustive anchor

For

\[
n=2,\ldots,64,
\]

every divisor

\[
d\mid n,
\]

and every pair

\[
(s,\rho)\in\mathbb Z_n\times\mathbb Z_d
\]

were compared.

Total:

\[
\boxed{146965}
\]

pairs.

Both implications were tested:

\[
\text{same CRT signature}
\Rightarrow
\text{same unit orbit},
\]

and

\[
\text{same unit orbit}
\Rightarrow
\text{same CRT signature}.
\]

Mismatches:

\[
\boxed0.
\]

### Additional larger moduli

A separate adversarial sample was run on

\[
n=
8,12,16,20,24,28,32,36,40,48,60,64,72,80,96,100,108,120.
\]

Additional sampled pair comparisons:

\[
\boxed{4335}.
\]

Mismatches:

\[
\boxed0.
\]

Therefore the CRT classification remains a genuine necessity-and-sufficiency theorem for the affine placement orbit.

---

## 11. CRT class → future language: sufficiency

Inside the final full-graph control set there were

\[
\boxed{122}
\]

distinct CRT placement classes.

Whenever two tested triples had the same CRT class, their component-colour future signatures agreed.

Within-CRT-class signature splits:

\[
\boxed0.
\]

Thus on the final control set:

\[
\boxed{
\text{same CRT placement class}
\Rightarrow
\text{same component-colour future language}.
}
\]

This is exactly the direction required for the placement taxonomy to be a valid predictor.

---

## 12. The converse is false and is not part of the theorem

The final control deliberately did **not** assume

\[
\text{same future language}
\Rightarrow
\text{same CRT placement class}.
\]

In fact, in the adversarial control set there were

\[
\boxed{33}
\]

component-colour future-language signatures shared by more than one CRT placement class after component-label renaming.

This is not a failure of the placement theorem.

It means:

\[
\boxed{
\text{affine placement equivalence is finer than accidental future-language equality}.
}
\]

Therefore the exact logical boundary is:

\[
\boxed{
\text{CRT class}
\Rightarrow
\text{same gauge-colour future language}
}
\]

but not universally the converse.

This is the final necessity/sufficiency boundary of the branch.

---

## 13. Extended out-of-range arithmetic controls

A final larger-size arithmetic stress sample used

\[
q=
31,32,37,41,49,60,
\]

corresponding to

\[
n=
124,128,148,164,196,240.
\]

For each size, 24 deterministic adversarial triples were checked.

Total:

\[
\boxed{144}
\]

additional placement cases.

The old explicit unit-orbit representation and the new CRT representation agreed throughout.

Mismatches:

\[
\boxed0.
\]

This extends the arithmetic control beyond the sizes used in the earlier family censuses.

---

## 14. GitHub Actions note

A dedicated workflow was added:

\[
\texttt{.github/workflows/pifi\_3d\_final\_classification\_control\_v0\_1.yml}.
\]

GitHub created run

\[
\boxed{37503671127}
\]

but the job ended before any step started:

- runner id: \(0\);
- recorded steps: \(0\).

Therefore that GitHub Actions run is **not counted as a mathematical failure or pass**.

The numerical final-control results recorded here come from the independently executed verifier logic in the assistant runtime.

The workflow remains in the branch as a reproducibility entry point for a later runner-enabled execution.

---

## 15. Final logical status

The branch now contains the following controlled statements.

### Exact / controlled

\[
\boxed{
s=2(\delta+c_{AB}+c_{BC})\pmod n
}
\]

for the split-annular macro system.

The coarse future quotient is classified by the frozen \(\mathcal A(q,s)\) theorem.

The component-aware refined future is exactly reproduced by the \(2n\)-state component-orbit construction.

The affine placement system is classified by

\[
(n,d_{AB},d_{BC},[(s,\rho)]_{U(n)}).
\]

The diagonal unit orbit is classified iff by the CRT data

\[
\{(a_p,b_p,m_p,r_p)\}_{p\mid n}.
\]

### Explicitly not claimed

The CRT placement class is not claimed to be necessary for every equality of future languages.

No claim of literature novelty is made by this final control.

No physical interpretation of the arithmetic invariants is promoted beyond the geometric links already separately proved.

---

## 16. Final verdict

No asserted link in the frozen mathematical chain broke under the final adversarial control.

Therefore the correct branch-level verdict is

\[
\boxed{
\textbf{FINAL CONTROL PASS}.
}
\]

And the correct research action is now

\[
\boxed{
\textbf{FREEZE THIS MATHEMATICAL BRANCH}.
}
\]

The next stage should not add more wiring parameters.

It should be:

\[
\boxed{
\text{SPECIALIST NOVELTY / LITERATURE AUDIT}
}
\]

followed by publication-grade consolidation of:

- theorem statements;
- proof boundaries;
- reproducibility scripts;
- public snapshot;
- manuscript structure.
