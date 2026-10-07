# PIFI-3D — CRT / PRIME-POWER PLACEMENT CLASSIFICATION THEOREM v0.1

**Date:** 2026-10-06  
**Branch:** \`agent/pifi-3d-crt-prime-power-placement-v01\`  
**Verdict:** **STRONG PASS — COMPLETE CRT / PRIME-POWER CLASSIFICATION**

## 1. Goal

The affine-placement theorem reduced the remaining placement information to the diagonal unit orbit

\[
[(s,\rho)]_{U(n)},
\]

where

\[
s\in\mathbb Z_n,
\qquad
\rho\in\mathbb Z_d,
\qquad
d=d_{AB}\mid n,
\]

and

\[
u\in U(n)
\]

acts simultaneously by

\[
(s,\rho)\mapsto
(us\bmod n,\ u\rho\bmod d).
\]

The question was whether the finite search through \(U(n)\) can be eliminated and replaced by compact prime-power data.

The answer is yes.

---

## 2. CRT decomposition

Write

\[
\boxed{
n=\prod_p p^{e_p}
}
\]

and

\[
\boxed{
d=\prod_p p^{f_p},
\qquad
0\le f_p\le e_p.
}
\]

By the Chinese Remainder Theorem,

\[
\mathbb Z_n
\cong
\prod_p \mathbb Z_{p^{e_p}},
\]

\[
\mathbb Z_d
\cong
\prod_p \mathbb Z_{p^{f_p}},
\]

and

\[
U(n)
\cong
\prod_p U(p^{e_p}).
\]

Therefore the diagonal orbit problem separates prime by prime.

Two global pairs are equivalent iff they are equivalent at every prime-power factor.

---

## 3. Local prime-power problem

Fix a prime \(p\).

Let

\[
p^e\parallel n,
\qquad
p^f\parallel d.
\]

For the \(p\)-primary residues define truncated valuations

\[
\boxed{
a=\min(v_p(s),e)
}
\]

and

\[
\boxed{
b=\min(v_p(\rho),f).
}
\]

The convention is:

- \(a=e\) means \(s\equiv0\pmod{p^e}\);
- \(b=f\) means \(\rho\equiv0\pmod{p^f}\).

Multiplication by a unit cannot change either valuation.

So

\[
a,\qquad b
\]

are necessary local invariants.

---

## 4. Relative unit ratio

Suppose both local coordinates are nonzero:

\[
a<e,
\qquad
b<f.
\]

Write

\[
s=p^a s_0,
\qquad
\rho=p^b\rho_0,
\]

with \(s_0,\rho_0\) units.

Define the overlap depth

\[
\boxed{
m=\min(e-a,\ f-b).
}
\]

On this common nonzero layer define

\[
\boxed{
r
=
\rho_0\,s_0^{-1}
\pmod{p^m}.
}
\]

Equivalently,

\[
\boxed{
r
=
\left(\frac{\rho}{p^b}\right)
\left(\frac{s}{p^a}\right)^{-1}
\pmod{p^m}.
}
\]

This ratio is unchanged under the simultaneous multiplication

\[
(s,\rho)\mapsto(us,u\rho)
\]

because the factor \(u\) cancels.

If either coordinate is zero on the local prime-power factor, then

\[
m=0
\]

and no ratio is required.

---

## 5. Prime-power classification theorem

For fixed

\[
p^e,\qquad p^f,
\]

two local pairs

\[
(s,\rho)
\]

and

\[
(s',\rho')
\]

belong to the same diagonal unit orbit iff they have identical

\[
\boxed{
(a,b,m,r).
}
\]

### Necessity

A unit preserves \(p\)-adic valuations.

When both coordinates are nonzero, simultaneous multiplication cancels in the quotient

\[
\rho_0s_0^{-1},
\]

so \(r\) is invariant.

### Sufficiency

Assume the local data agree.

We seek a unit \(u\) satisfying

\[
us\equiv s'\pmod{p^e}
\]

and

\[
u\rho\equiv\rho'\pmod{p^f}.
\]

After dividing by the fixed powers \(p^a,p^b\), this becomes

\[
u\equiv s_0's_0^{-1}\pmod{p^{e-a}}
\]

and

\[
u\equiv\rho_0'\rho_0^{-1}\pmod{p^{f-b}}.
\]

These two unit congruences are compatible exactly on their overlap modulus

\[
p^m.
\]

Their compatibility condition is exactly equality of the relative ratios \(r\).

Hence a common unit exists.

Therefore the local invariant is complete.

---

## 6. Global theorem

For every prime

\[
p\mid n
\]

compute

\[
(a_p,b_p,m_p,r_p).
\]

Then:

\[
\boxed{
(s,\rho)\sim(s',\rho')
\text{ under }U(n)
}
\]

iff

\[
\boxed{
(a_p,b_p,m_p,r_p)
=
(a_p',b_p',m_p',r_p')
}
\]

for every prime \(p\mid n\).

Thus the old finite affine invariant

\[
\chi
=
\min_{u\in U(n)}
(us,\ u\rho)
\]

can be replaced exactly by the CRT signature

\[
\boxed{
\Psi(s,\rho)
=
\left\{
(a_p,b_p,m_p,r_p)
\right\}_{p\mid n}.
}
\]

There is no longer any need to enumerate \(U(n)\).

---

## 7. No exceptional 2-adic case

The proof uses only compatibility of unit congruences over nested powers

\[
p^k.
\]

It does not require cyclicity of \(U(p^e)\).

Therefore the theorem works unchanged for

\[
\boxed{p=2}.
\]

This is important because the PIFI family always has

\[
4\mid n.
\]

No special 2-adic branch is needed.

---

## 8. Previous affine-equivalence example

Recall the \(n=12\), \(d=3\) pairs

\[
(s,\rho)=(10,1)
\]

and

\[
(2,2).
\]

At \(p=2\), both have the same valuation data.

At \(p=3\),

\[
a=b=0.
\]

For the first pair,

\[
r=1\cdot 10^{-1}\equiv1\pmod3.
\]

For the second,

\[
r=2\cdot2^{-1}\equiv1\pmod3.
\]

So their CRT signatures coincide.

This recovers exactly the previous affine-gauge equivalence without searching for the unit \(u=5\).

---

## 9. Why gcd data failed

Compare instead

\[
(10,1)
\]

and

\[
(2,1)
\]

with \(n=12,d=3\).

The obvious scalar invariants coincide:

\[
\gcd(12,10)=\gcd(12,2)=2,
\]

and both \(\rho\)-coordinates are units modulo \(3\).

But at \(p=3\),

\[
r(10,1)=1,
\]

while

\[
r(2,1)=2.
\]

Therefore the CRT theorem distinguishes them immediately.

This identifies the precise information missed by a gcd-only taxonomy:

\[
\boxed{
\text{the relative unit ratio on the common prime-power layer}.
}
\]

---

## 10. A genuine higher prime-power witness

The relative ratio is not merely a mod-\(p\) sign.

Take

\[
n=16,
\qquad
d=8.
\]

Compare

\[
(s,\rho)=(2,2)
\]

and

\[
(2,6).
\]

At \(p=2\),

\[
e=4,\qquad f=3,
\]

and both pairs have

\[
a=b=1.
\]

Therefore

\[
m=\min(3,2)=2.
\]

The relative ratios are

\[
r_1=1\pmod4,
\]

and

\[
r_2=3\pmod4.
\]

Thus the pairs are inequivalent even though their valuation data are identical.

So the final invariant genuinely requires a unit ratio modulo

\[
p^m,
\]

not only valuations.

---

## 11. Generic exhaustive regression

The CRT theorem was checked independently against explicit unit-orbit enumeration for:

\[
n=2,\ldots,64,
\]

every divisor

\[
d\mid n,
\]

and every pair

\[
(s,\rho)\in\mathbb Z_n\times\mathbb Z_d.
\]

Total pairs:

\[
\boxed{146965}.
\]

Two directions were checked:

1. equal CRT signature \(\Rightarrow\) equal explicit \(U(n)\)-orbit;
2. equal explicit orbit \(\Rightarrow\) equal CRT signature.

Mismatches:

\[
\boxed0.
\]

So the CRT signature and the previous finite orbit are in exact bijection throughout the generic exhaustive test.

---

## 12. PIFI-family regression

For the actual split-annular PIFI family with

\[
q=2,\ldots,8,
\]

all admissible triples

\[
(\delta,c_{AB},c_{BC})
\]

were tested.

Total:

\[
\boxed{70574}
\]

triples.

The previous affine-orbit taxonomy gave

\[
\boxed{862}
\]

placement classes.

The new CRT taxonomy also gives

\[
\boxed{862}
\]

classes.

Moreover the map between them is one-to-one:

\[
\boxed{
\text{old affine class}
\longleftrightarrow
\text{CRT class}.
}
\]

Bijection mismatches:

\[
\boxed0.
\]

Thus the CRT theorem is an exact replacement, not a weaker approximation.

---

## 13. Extended census

The CRT classification was then extended through

\[
q=2,\ldots,12,
\]

that is

\[
n=8,\ldots,48.
\]

Total admissible wiring triples:

\[
\boxed{349294}.
\]

They collapse to

\[
\boxed{2665}
\]

CRT placement classes.

Per size:

\[
n=8:\quad 294\to19,
\]

\[
n=12:\quad1210\to92,
\]

\[
n=16:\quad3150\to56,
\]

\[
n=20:\quad6498\to116,
\]

\[
n=24:\quad11638\to305,
\]

\[
n=28:\quad18954\to140,
\]

\[
n=32:\quad28830\to134,
\]

\[
n=36:\quad41650\to468,
\]

\[
n=40:\quad57798\to379,
\]

\[
n=44:\quad77658\to188,
\]

\[
n=48:\quad101614\to768.
\]

So the prime-power taxonomy remains a strong compression at larger family sizes.

---

## 14. Final arithmetic form of placement

The affine placement theorem used

\[
\Theta
=
(n,d_{AB},d_{BC},[(s,\rho)]_{U(n)}).
\]

The CRT theorem now replaces the finite orbit by explicit local data:

\[
\boxed{
\Theta_{\rm CRT}
=
\left(
n,\,
d_{AB},\,
d_{BC},\,
\{(a_p,b_p,m_p,r_p)\}_{p\mid n}
\right).
}
\]

Equivalently, using the graph-level component invariants:

\[
\boxed{
\Theta_{\rm CRT}
=
\left(
n,\,
h_{AB},\,
h_{BC},\,
\epsilon_{BC},\,
\{(a_p,b_p,m_p,r_p)\}_{p\mid n}
\right).
}
\]

This is the maximal arithmetic compression reached in this branch.

---

## 15. What is irreducible

The classification separates into two layers:

### Valuation layer

\[
a_p,\qquad b_p
\]

records how deeply the two coordinates vanish at \(p\).

### Relative-unit layer

\[
r_p
\]

records their relative phase when both survive.

The earlier hope that valuations/gcd data alone might suffice is false.

The relative-unit ratio is irreducible in general.

So the exact endpoint is:

\[
\boxed{
\text{p-adic valuations}
+
\text{relative unit ratios}.
}
\]

---

## 16. Scientific significance

We have now replaced:

\[
\text{explicit search through }U(n)
\]

by

\[
\boxed{
\text{local prime-power invariants}
}
\]

and CRT reconstruction.

The complete placement chain is now

\[
(\delta,c_{AB},c_{BC})
\]

\[
\Downarrow
\]

\[
(s,d_{AB},d_{BC},\rho)
\]

\[
\Downarrow
\]

\[
\{(a_p,b_p,m_p,r_p)\}_{p\mid n}
\]

\[
\Downarrow
\]

\[
\text{component-labelled macro orbit}
\]

\[
\Downarrow
\]

\[
Q_{\rm comp}.
\]

At this point the placement classification is no longer computationally defined by an orbit search.

It is an explicit arithmetic theorem.

---

## 17. Claim boundary

This theorem completely classifies the diagonal affine placement orbit.

It does not yet prove that the entire graph-to-future chain has no implementation or derivation error outside the ranges already tested.

Therefore one final independent stage remains justified:

\[
\boxed{
\text{FINAL CLASSIFICATION / NECESSITY-SUFFICIENCY CONTROL}
}
\]

That stage should combine:

- the full graph generator;
- the macro transition theorem;
- the component-orbit predictor;
- the affine placement theorem;
- the CRT classifier;

and stress-test them against each other on larger and adversarial parameter sets.

After that, this branch should be frozen rather than extended with more wiring parameters.
