# PIFI-3D — REFINED TERMINAL OBSERVATION / QUOTIENT-INJECTIVITY THEOREM v0.1

**Date:** 2026-10-06  
**Branch:** `agent/pifi-3d-refined-terminal-injectivity-v01`  
**Verdict:** **STRONG PASS — COMPONENT-AWARE REFINEMENT RECOVERS LOST MICROSTRUCTURE**

## 1. Why this gate was necessary

The split annular theorem proved that the full labelled graph retains at least two independent microscopic invariants,

[
h_{AB},
qquad
h_{BC},
]

while the routed terminal future quotient sees only

[
s=2(delta+c_{AB}+c_{BC}).
]

Therefore distinct full graphs can have the same

[
Q,quad
k_{min},quad
	ext{primitive terminal periods},
]

and the same complete coarse routed future language.

The next question is no longer whether another wiring parameter exists.

The correct question is:

> what is the smallest natural refinement of the terminal observation that begins to recover the graph information erased by the coarse quotient?

---

## 2. The original coarse observation

The frozen terminal alphabet used up to this point is

[
oxed{
mathcal O_0(d)
=
(	ext{edge family},
deg(	ext{tail}),
deg(	ext{head}))
}
]

for every routed dart (d).

This observation knows whether the current edge belongs to

[
OA, AA, AB, AC, BC,
]

and it knows the endpoint degrees.

It does **not** know which connected component of an annular family the dart belongs to.

That omission is exactly where the previously proved microscopic information is lost.

---

## 3. Family-component structure

For AB,

[
oxed{
h_{AB}
=
gcd(n,c_{AB}).
}
]

The AB-only graph decomposes into (h_{AB}) annular components.

For BC, let

[
d_{BC}=gcd(n,c_{BC}).
]

After the two cardinal C-pair identifications,

[
oxed{
h_{BC}
=
egin{cases}
d_{BC},&d_{BC}mid n/2,\
d_{BC}-2,&d_{BC}
mid n/2.
end{cases}}
]

Thus every AB or BC dart belongs to a well-defined family component.

---

## 4. Natural refinement lattice

This gate freezes the following hierarchy.

### O0 — coarse

[
mathcal O_0
=
(	ext{family},deg u,deg v).
]

### O_AB — AB-aware only

Attach an exact canonical AB-component id only to AB darts.

### O_BC — BC-aware only

Attach an exact canonical BC-component id only to BC darts.

### O_bin — one-bit component refinement

For AB and BC, record only

[
oxed{
0	ext{-component}
quad	ext{versus}quad
	ext{nonzero component}.
}
]

This is the most obvious one-bit refinement.

### O_comp — exact component-aware observation

For AB darts, add their exact AB component id.

For BC darts, add their exact BC component id after the cardinal C identifications.

All OA, AA and AC tokens remain unchanged.

So the successful observation is

[
oxed{
mathcal O_{m comp}
=
mathcal O_0
+
	ext{family-component id on AB/BC only}.
}
]

---

## 5. Both family markers are necessary

An AB-only marker cannot recover (h_{BC}).

At (n=12),

[
(1,1,1)
]

and

[
(1,5,3)
]

have the same

[
h_{AB}=1
]

and the AB-aware future signatures remain identical, even though

[
h_{BC}=1
]

versus

[
h_{BC}=3.
]

Similarly, a BC-only marker cannot recover (h_{AB}).

The pair

[
(1,1,1)
]

and

[
(1,3,5)
]

has the same

[
h_{BC}=1,
]

but

[
h_{AB}=1
]

versus

[
h_{AB}=3.
]

Therefore:

[
oxed{
	ext{both annular families must contribute observation information}
}
]

if the goal is to recover both microscopic invariants.

---

## 6. One bit is not enough in general

The natural binary refinement

[
	ext{component zero/nonzero}
]

works for some small examples, including the four (n=12,s=6) witnesses.

But it fails globally.

At

[
n=16
]

compare

[
(delta,c_{AB},c_{BC})
=
(1,4,7)
]

and

[
(1,8,3).
]

Both have

[
s=8.
]

Their microscopic pairs are

[
(h_{AB},h_{BC})=(4,1)
]

and

[
(h_{AB},h_{BC})=(8,1).
]

Under the one-bit refinement both produce the same refined future signature, with

[
oxed{Q_{m bin}=116}
]

and

[
oxed{k_{min,m bin}=19}.
]

So:

[
oxed{
(4,1)
e(8,1)
}
]

but

[
oxed{
mathcal F_{m bin}(4,1)
=
mathcal F_{m bin}(8,1).
}
]

The one-bit component marker is therefore rejected as a general injective refinement.

With exact component labels the same two cases separate immediately:

[
oxed{
Q_{m comp}=128
}
]

versus

[
oxed{
Q_{m comp}=248.
}
]

---

## 7. Successful exact component-aware refinement

For fixed

[
(n,s),
]

define the complete refined future signature from all primitive periodic future classes under

[
mathcal O_{m comp}.
]

The injectivity test asks:

> can one refined future signature correspond to two different pairs
> ((h_{AB},h_{BC}))?

The exhaustive answer in the tested range is no.

For

[
q=2,ldots,6,
]

every admissible

[
(delta,c_{AB},c_{BC})
]

was checked.

Total:

[
oxed{22790}
]

full HT+ graph instances.

Number of refined future signatures shared by two different microscopic pairs at the same ((n,s)):

[
oxed0.
]

Thus in the entire tested range:

[
oxed{
mathcal O_{m comp}
	ext{ is injective with respect to }
(h_{AB},h_{BC})
	ext{ conditional on }(n,s).
}
]

This is the principal result of the gate.

---

## 8. Important nuance: the refined future can remember more than h_AB,h_BC

The converse is not true.

The same pair

[
(h_{AB},h_{BC})
]

can sometimes produce more than one refined future signature.

Across (q=2,ldots,6), this occurs in

[
296
]

fixed-((n,s,h_{AB},h_{BC})) classes.

Therefore

[
mathcal O_{m comp}
]

does not merely encode the two component counts.

It can retain finer phase-placement information inside the annular components.

Hence the proved statement is

[
oxed{
	ext{future signature}
Rightarrow
(h_{AB},h_{BC})
}
]

in the tested range,

not necessarily

[
(h_{AB},h_{BC})
Rightarrow
	ext{one unique future signature}.
]

---

## 9. How much observation information is being added?

Within the component-id strategy, an exact fixed-width component label requires

[
oxed{
b_{AB}
=
leftlceillog_2 h_{AB}ightceil
}
]

bits on AB tokens, with (0) bits when (h_{AB}=1).

Likewise,

[
oxed{
b_{BC}
=
leftlceillog_2 h_{BC}ightceil
}
]

bits on BC tokens.

No extra component field is needed on

[
OA, AA, AC.
]

Examples at (n=12,s=6):

[
(h_{AB},h_{BC})=(1,1)
]

requires

[
(0,0)
]

component bits;

[
(3,1)
]

requires

[
(2,0);
]

[
(1,3)
]

requires

[
(0,2);
]

[
(4,2)
]

requires

[
(2,1).
]

This is the exact fixed-width information needed to name the component ids themselves.

It is **not** claimed to be the globally minimal coding over every imaginable observation alphabet.

---

## 10. The n=12,s=6 witness family

All four split-annular templates below have identical coarse future data:

[
Q_0=52,
qquad
k_{min,0}=13.
]

### Original PIFI

[
(delta,c_{AB},c_{BC})=(1,1,1),
]

[
(h_{AB},h_{BC})=(1,1).
]

Under component-aware observation:

[
oxed{
Q_{m comp}=52.
}
]

Primitive periods:

[
8, 12, 12, 20.
]

### AB microstructure only

[
(1,3,5),
]

[
(h_{AB},h_{BC})=(3,1).
]

Then

[
oxed{
Q_{m comp}=96.
}
]

Primitive periods:

[
8, 12, 12, 20, 20, 24.
]

### BC microstructure only

[
(1,5,3),
]

[
(h_{AB},h_{BC})=(1,3).
]

Then

[
oxed{
Q_{m comp}=84.
}
]

Primitive periods:

[
8, 12, 12, 12, 20, 20.
]

### Both nontrivial

[
(1,4,4),
]

[
(h_{AB},h_{BC})=(4,2).
]

Then

[
oxed{
Q_{m comp}=184.
}
]

Primitive periods:

[
8, 12, 12, 12, 12, 20, 20, 20, 20, 24, 24.
]

All four retain

[
oxed{k_{min,m comp}=13}.
]

So the extra graph information appears primarily as additional distinguishable periodic future classes rather than a larger prefix depth in these witnesses.

---

## 11. The crucial result for the original 52-state PIFI quotient

At the original PIFI point,

[
(delta,c_{AB},c_{BC})=(1,1,1),
]

we have

[
oxed{
h_{AB}=h_{BC}=1.
}
]

That means both family-restricted annular graphs are already connected.

There is only one component id available in each family.

Therefore the successful component-aware refinement adds **no effective new symbol information** at the original PIFI point.

The result is exactly:

[
oxed{
Q_0=52
quadlongrightarrowquad
Q_{m comp}=52.
}
]

Also

[
oxed{
k_{min}=13
}
]

and

[
oxed{
(8,12,12,20)
}
]

remain unchanged.

This was verified for both HT+ and HT−.

---

## 12. What this means for the interpretation of 52

This gives a sharper answer than the initial hypothesis.

It is correct that the coarse observation forgets component microstructure **across the generalized family**.

For deformed templates, the same coarse

[
Q=52
]

can hide very different full graphs, and the refined quotient exposes them.

However:

[
oxed{
	ext{the original PIFI 52 is not created merely by forgetting nontrivial }
h_{AB},h_{BC}.
}
]

At the original point there is no nontrivial annular component information to forget:

[
h_{AB}=h_{BC}=1.
]

So the original 52-state result is more robust than the naive coarse-observation explanation.

---

## 13. Is 52 minimal?

There are two different meanings of "minimal".

### For the fixed coarse observation O0

The future quotient is built by identifying states with identical infinite observed futures.

Therefore its (52) classes are, by construction, the minimal future-equivalence representation for that fixed observation language.

In that precise sense:

[
oxed{
52	ext{ is minimal for }mathcal O_0.
}
]

### For all possible richer observations

No.

A richer alphabet changes the equivalence relation itself.

For generalized templates the component-aware quotient can be

[
84, 96, 128, 184, 248,ldots
]

while the coarse system can still show 52.

Thus 52 is not a universal minimal representation of the complete labelled graph.

### For original PIFI under the successful refinement

Unexpectedly,

[
oxed{
52	ext{ remains 52.}
}
]

So the original PIFI point is already component-trivial in AB and BC.

---

## 14. Chirality regression

For

[
q=2,ldots,8,
]

one representative of every class

[
(q,s,h_{AB},h_{BC})
]

was tested under the exact component-aware observation.

Number of representative classes:

[
1310.
]

Both HT+ and HT− were evaluated:

[
oxed{2620}
]

refined future computations.

Differences between HT+ and HT− in

[
Q_{m comp},
quad
	ext{primitive-period census},
quad
k_{min,m comp}
]

were:

[
oxed0.
]

No HT+ refined signature collision between distinct

[
(h_{AB},h_{BC})
]

was found in the representative set.

---

## 15. Scientific conclusion

The hierarchy is now:

[
	ext{full graph}
	o
(h_{AB},h_{BC},ldots)
	o
	ext{terminal observation}
	o
	ext{future quotient}.
]

Under the coarse observation,

[
oxed{
(delta,c_{AB},c_{BC})
	o
s
	o
Q
}
]

and component information is erased.

Under the refined observation,

[
oxed{
	ext{component identities}
	o
	ext{additional terminal distinctions}
	o
Q_{m comp},
}
]

and the pair

[
(h_{AB},h_{BC})
]

becomes recoverable in the exhaustive tested range.

So we have now explicitly demonstrated an **observation-resolution hierarchy**:

[
oxed{
	ext{same graph dynamics}
+
	ext{different observation resolution}
Rightarrow
	ext{different future quotient}.
}
]

---

## 16. Claim boundary

This gate proves a computational injectivity result over the tested family and an exact structural explanation of the component labels.

It does **not** yet provide a closed-form formula for

[
Q_{m comp}
]

in terms of

[
n, s, h_{AB}, h_{BC},
]

nor does it prove that exact component ids are the globally smallest possible observation coding.

The phrase "minimal refinement" should therefore be read as:

> the first successful refinement in the explicitly tested natural lattice
> (O_0	o O_{AB}/O_{BC}	o O_{m bin}	o O_{m comp}).

---

## 17. Next justified gate

The next useful step is not another observation experiment.

We now have enough evidence to attempt a theorem for the refined quotient itself:

[
oxed{
	ext{REFINED QUOTIENT CLOSED-FORM / COMPONENT-ORBIT GATE}
}
]

The goal is to derive, rather than enumerate,

[
Q_{m comp}
]

from the interaction of:

[
s,
qquad
h_{AB},
qquad
h_{BC},
]

and the placement of component labels along the (C3/C6/C20) macro word.

That will determine whether the refined state counts such as

[
52, 84, 96, 184, 248
]

belong to a second exact arithmetic classification analogous to the original

[
Q(n)
]

theorem.
