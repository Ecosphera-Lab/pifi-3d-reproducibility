# PIFI-3D — REFINED QUOTIENT CLOSED-FORM / COMPONENT-ORBIT THEOREM v0.1

**Date:** 2026-10-06  
**Branch:** \`agent/pifi-3d-refined-quotient-component-orbit-v01\`  
**Verdict:** **STRONG PASS — EXACT COMPONENT-ORBIT FORMULA**

## 1. Goal

The previous gate showed that the refined observation \(\mathcal O_{\rm comp}\) can distinguish graph microstructure hidden by the coarse \(52\)-state quotient.

The remaining problem was to stop computing \(Q_{\rm comp}\) by full graph enumeration and explain exactly why values such as

\[
52,\ 84,\ 96,\ 128,\ 184,\ 248,\ldots
\]

appear.

The answer is an exact component-orbit formula on the already derived \(2n\)-state macro system.

## 2. Split-annular data

For

\[
n=4q,
\]

the graph family is parameterized by

\[
(\delta,c_{AB},c_{BC}),
\]

and the routed macro shift is

\[
\boxed{
s=2(\delta+c_{AB}+c_{BC})\pmod n.
}
\]

The macro frame states are

\[
L_j,\qquad R_j,\qquad j\in\mathbb Z_n.
\]

Their affine transition permutation \(\sigma\) is exactly the one proved in the split-annular theorem.

The radial \(U\)-class remains independent and always contributes

\[
\boxed8
\]

future states.

## 3. Component maps

For AB define

\[
d_{AB}=\gcd(n,c_{AB})
\]

and the exact component map

\[
\boxed{
\alpha(i)=i\bmod d_{AB}.
}
\]

For BC define

\[
d_{BC}=\gcd(n,c_{BC}).
\]

Start with residues in \(\mathbb Z_{d_{BC}}\), then impose the two cardinal identifications induced by

\[
C_0\sim C_{n/2},
\qquad
C_q\sim C_{3q}.
\]

Let

\[
\boxed{\kappa(i)}
\]

be the canonical class of \(i\bmod d_{BC}\) in this quotient.

Thus the refined terminal observation on an AB or BC dart is determined arithmetically by \(\alpha\) or \(\kappa\).

## 4. Exact component placement inside one macro frame

For a frame entered at \(L_j\), the annular cell indices are

\[
\boxed{AB_L^{(1)}=j-c_{AB}},
\qquad
\boxed{AB_L^{(2)}=j-2c_{AB}-2\delta},
\]

and

\[
\boxed{BC_L^{(1)}=j-(s-c_{BC})},
\qquad
\boxed{BC_L^{(2)}=\text{destination frame index}}.
\]

For a frame entered at \(R_j\),

\[
\boxed{AB_R^{(1)}=j+c_{BC}},
\qquad
\boxed{AB_R^{(2)}=j+c_{BC}+c_{AB}+2\delta},
\]

while

\[
\boxed{BC_R^{(1)}=j+s-c_{BC}},
\qquad
\boxed{BC_R^{(2)}=\text{destination frame index}}.
\]

Applying \(\alpha\) to the AB indices and \(\kappa\) to the BC indices determines every component label in the refined terminal word.

## 5. Decorated frame words

The coarse routed system uses three non-radial frame types:

\[
C3,\qquad C6,\qquad C20,
\]

with terminal lengths

\[
12,\qquad12,\qquad20.
\]

For each macro state \(x=L_j\) or \(R_j\), define

\[
\boxed{\beta(x)}
\]

to be the corresponding \(C3\), \(C6\), or \(C20\) word decorated by the exact component labels from the index formulas above.

## 6. Exact component-orbit formula

Let \(\Omega\) be the set of cycles of the affine macro permutation \(\sigma\) on

\[
\{L_j,R_j:j\in\mathbb Z_n\}.
\]

For

\[
C=(x_0,x_1,\ldots,x_{\ell-1})\in\Omega,
\]

form

\[
\boxed{
W_C=
\beta(x_0)\beta(x_1)\cdots\beta(x_{\ell-1}).
}
\]

Let \(\operatorname{prim}(W_C)\) be its primitive periodic root.

Two macro cycles define the same refined future class exactly when these primitive decorated words agree up to cyclic rotation.

Let \(\mathcal P_{\rm comp}\) be the set of distinct cyclic classes of the primitive words. Then

\[
\boxed{
Q_{\rm comp}
=
8+
\sum_{[W]\in\mathcal P_{\rm comp}}
|W|.
}
\]

This is the exact closed component-orbit formula.

The full \(32n\)-dart routing permutation is no longer required to compute \(Q_{\rm comp}\).

## 7. Why the observed numbers appear

At the original PIFI point

\[
(\delta,c_{AB},c_{BC})=(1,1,1),
\]

all component labels are trivial. The distinct primitive periods are

\[
8,\ 12,\ 12,\ 20,
\]

hence

\[
\boxed{Q_{\rm comp}=8+12+12+20=52.}
\]

For

\[
n=12,\quad(1,5,3),
\]

the periods are

\[
8,\ 12,\ 12,\ 12,\ 20,\ 20,
\]

so

\[
\boxed{Q_{\rm comp}=84.}
\]

For

\[
n=12,\quad(1,3,5),
\]

the periods are

\[
8,\ 12,\ 12,\ 20,\ 20,\ 24,
\]

so

\[
\boxed{Q_{\rm comp}=96.}
\]

For

\[
n=12,\quad(1,4,4),
\]

the periods are

\[
8,\ 12,12,12,12,\ 20,20,20,20,\ 24,24,
\]

hence

\[
\boxed{
Q_{\rm comp}=8+4\cdot12+4\cdot20+2\cdot24=184.
}
\]

At \(n=16\),

\[
(1,4,7)\Rightarrow Q_{\rm comp}=128,
\]

while

\[
(1,8,3)\Rightarrow Q_{\rm comp}=248.
\]

Thus the previously empirical-looking numbers are exactly sums of primitive component-decorated macro-orbit periods.

## 8. Crucial negative theorem

A scalar formula of the form

\[
Q_{\rm comp}=F(n,s,h_{AB},h_{BC})
\]

does not exist for this refined observation.

At

\[
n=24
\]

the systems

\[
(\delta,c_{AB},c_{BC})=(1,7,6)
\]

and

\[
(1,5,8)
\]

both have

\[
\boxed{
s=4,\qquad h_{AB}=1,\qquad h_{BC}=6.
}
\]

But the first has periods

\[
8,\ 36,\ 60,\ 88
\]

and therefore

\[
\boxed{Q_{\rm comp}=192},
\]

whereas the second has

\[
8,\ 20,\ 20,\ 20,\ 20,\ 24,\ 24,\ 88,\ 88
\]

and therefore

\[
\boxed{Q_{\rm comp}=312}.
\]

Hence

\[
\boxed{
Q_{\rm comp}
\text{ is not determined by }
(n,s,h_{AB},h_{BC})
\text{ alone.}
}
\]

Component-label placement inside the \(C3/C6/C20\) frames is an essential invariant.

## 9. What the true refined invariant is

The coarse level is controlled by

\[
s=2(\delta+c_{AB}+c_{BC}),
\]

which fixes the affine macro orbit structure.

The refined level additionally requires the sampled component maps

\[
\alpha(i),\qquad\kappa(i)
\]

at the exact affine frame positions.

Therefore the correct invariant is

\[
\boxed{
\text{macro orbit}
+
\text{component-label placement}.
}
\]

The counts \(h_{AB}\) and \(h_{BC}\) alone retain too little information.

## 10. Regression

The arithmetic predictor was compared against the full graph component-aware future signature for every admissible triple with

\[
q=2,\ldots,4.
\]

Total:

\[
\boxed{4654/4654\text{ PASS}}.
\]

For every case, the following agreed exactly:

- complete cyclic primitive future signature;
- primitive-period multiset;
- \(Q_{\rm comp}\).

Mismatches:

\[
\boxed0.
\]

A larger arithmetic-only sweep over

\[
q=2,\ldots,8
\]

covered

\[
\boxed{70574}
\]

parameter triples and produced 31 distinct refined quotient sizes:

\[
52,\ 84,\ 96,\ 116,\ 128,\ 148,\ 160,\ 180,\ 184,\ 192,\ 212,\ 224,
\]

\[
244,\ 248,\ 256,\ 288,\ 312,\ 352,\ 360,\ 376,\ 416,\ 440,\ 480,\ 488,
\]

\[
504,\ 568,\ 616,\ 696,\ 744,\ 824,\ 872.
\]

Every value is generated by the same exact orbit-sum rule.

## 11. Scientific interpretation

The hierarchy is now

\[
\text{full graph}
\to
\text{affine macro permutation}
+
\text{component maps}
\to
\text{decorated macro orbits}
\to
Q_{\rm comp}.
\]

The computation has been reduced from the full \(32n\)-dart graph to only \(2n\) macro states plus fixed finite frame words.

More importantly, the theorem identifies exactly why the refined quotient grows: coarse cycles split when their component-decorated orbit words cease to be cyclically equivalent or cease to have the same primitive period.

## 12. Claim boundary

Here “closed-form” means an exact finite arithmetic orbit-sum formula with analytically specified transitions and component placements.

It is not a single gcd expression analogous to the coarse \(Q(n)\) theorem.

The \(n=24\) counterexample proves that any further scalar compression must introduce an additional invariant describing component placement, not merely \(h_{AB}\) and \(h_{BC}\).

## 13. Next justified gate

The natural continuation is

\[
\boxed{
\text{COMPONENT-PLACEMENT CLASSIFICATION / AFFINE-GAUGE GATE}
}
\]

to determine when two triples

\[
(\delta,c_{AB},c_{BC})
\]

produce equivalent component-labelled macro orbit systems.

If those placement types admit a finite arithmetic classification, the exact orbit-sum theorem may compress further into a small gcd/lcm taxonomy.
