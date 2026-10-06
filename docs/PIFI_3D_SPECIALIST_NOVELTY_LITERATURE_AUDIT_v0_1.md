# PIFI-3D — SPECIALIST NOVELTY / LITERATURE AUDIT v0.1

**Date checked:** 2026-10-06  
**Branch:** \`agent/pifi-3d-specialist-novelty-audit-v01\`  
**Scope:** the frozen mathematical chain ending at \`PIFI_3D_FINAL_CLASSIFICATION_CONTROL_v0_1.md\`  
**Novelty verdict:** **FAMILY-SPECIFIC RESULT IS A CREDIBLE NOVELTY CANDIDATE; GENERAL MACHINERY IS PRIOR ART**

---

## 1. Executive verdict

The mathematical branch should remain frozen.

The targeted prior-art search did **not** locate a publication containing the same explicit family and the same theorem chain

\[
\mathcal T_{n;\delta,c_{AB},c_{BC}}
\longrightarrow
s=2(\delta+c_{AB}+c_{BC})
\longrightarrow
\mathcal A(q,s)
\longrightarrow
Q,k_{\min}
\]

together with

\[
\text{component-aware refinement}
\longrightarrow
\text{decorated macro-orbit formula}
\longrightarrow
\text{affine placement class}
\longrightarrow
\text{CRT prime-power classification}.
\]

That absence is **not a proof of novelty**.

The defensible current status is:

\[
\boxed{
\text{NOT LOCATED IN TARGETED PRIOR-ART PASS — NOT YET A GLOBAL NOVELTY CLAIM}.
}
\]

The strongest candidate contribution is not any one standard ingredient. It is the **explicit exactly-solvable routed rotation-system family and the complete arithmetic classification of its observation-dependent future quotients**.

---

## 2. What is clearly standard prior art

### 2.1 Darts and rotation systems

Encoding an embedded graph by darts/half-edges together with permutations describing edge reversal and cyclic order around vertices is classical combinatorial-map / rotation-system machinery.

A standard oriented combinatorial map is described by a finite dart set \(D\), an involution \(\alpha\), and a vertex rotation permutation \(\sigma\).

**Relevant source**

- *Three-dimensional maps and subgroup growth*, Manuscripta Mathematica, 2021/2022, DOI 10.1007/s00229-021-01321-7.

**Novelty boundary**

Do **not** claim novelty for:

- dart representations;
- vertex rotations;
- routing by permutations on darts;
- cycle decompositions of a dart permutation.

Our work may define a special routing rule on a special graph family, but the underlying representation is classical.

---

### 2.2 Voltage graphs, cyclic lifts and gcd/order phenomena

Voltage graphs and derived graph covers are classical.

For an oriented base cycle, its lift length is governed by the order of the net voltage. In cyclic voltage groups this immediately produces gcd/order formulas for numbers and lengths of lifted cycles.

A standard statement is that if a base cycle has length \(\ell\) and net voltage \(f\), then its lift has length controlled by \(\ell\) and the order of \(f\); equivalent formulations give the number of lifted components through the index/order of the generated subgroup.

**Relevant sources**

- Gross & Tucker, *Topological Graph Theory*, Wiley, 1987.
- Electronic Journal of Combinatorics, *Dynamic Cage Survey*, section on voltage graph lifts, 2013.
- Hubard, Mochán, Montero, *Voltage Operations on Maniplexes, Polytopes and Maps*, Combinatorica 43 (2023), 385–420, DOI 10.1007/s00493-023-00018-7.

**Novelty boundary**

Do **not** claim that gcd-controlled cyclic behavior itself is new.

Our candidate contribution is the **exact specialization and closed formulas for the particular PIFI-derived routing template**, not the existence of gcd phenomena in graph covers.

---

### 2.3 Future/follower equivalence and minimal finite-state presentations

Identifying states by indistinguishable future behavior is classical in automata theory and symbolic dynamics.

The Myhill–Nerode theorem identifies states with equal right/future languages and gives a canonical minimal deterministic automaton.

In symbolic dynamics, follower sets, Fischer covers, Krieger covers and future covers are standard tools for finite-state/sofic presentations.

**Relevant sources**

- Lind & Marcus, *An Introduction to Symbolic Dynamics and Coding*, Cambridge University Press, 2nd ed., 2021, DOI 10.1017/9781108899727.
- Rune Johansen, *On the Structure of Covers of Sofic Shifts*, Documenta Mathematica 16 (2011), 111–131, DOI 10.4171/DM/328.
- Klaus Thomsen, *On the future cover of a sofic shift*, arXiv:2512.01368 (2025).
- Standard Myhill–Nerode minimal-automaton theorem.

**Novelty boundary**

The phrases

\[
\text{future quotient}
\]

and

\[
\text{minimal future-state representation}
\]

should be translated in the paper into standard follower/right-language/Nerode terminology wherever possible.

Do **not** claim novelty for the abstract idea that future-equivalent states can be quotiented.

---

### 2.4 Observation maps, recoding and factors

Changing the observable alphabet while keeping an underlying finite-state dynamics is standard symbolic-dynamics/coding machinery.

Sliding block codes and factor maps explicitly formalize loss of information under recoding.

**Relevant source**

- Scholarpedia, *Symbolic dynamics*, sections on sliding block codes, factor maps, SFTs and sofic systems.

**Novelty boundary**

The general phenomenon

\[
\text{coarser observation}
\Rightarrow
\text{more state identifications}
\]

is not new.

The candidate contribution is the exact quantitative realization of this phenomenon in the present graph family, including explicit same-coarse/different-refined witnesses.

---

### 2.5 Primitive cyclic words / necklaces

Words modulo cyclic rotation and primitive cyclic words are standard necklace combinatorics.

**Relevant sources**

- standard necklace combinatorics;
- European Journal of Combinatorics 33 (2012), 1537–1546, DOI 10.1016/j.ejc.2012.03.016, on words and multisets of primitive necklaces.

**Novelty boundary**

Do **not** claim novelty for taking primitive roots of periodic words or quotienting words by cyclic rotation.

The candidate contribution is the **specific decorated \(C3/C6/C20\) macro-orbit decomposition and its exact state-count consequence**.

---

### 2.6 Affine permutations and cycle structures

Cycle structures of affine and coset-wise affine permutations over finite fields/groups are an established research subject.

**Relevant source**

- Alexander Bors & Qiang Wang, *Coset-wise affine functions and cycle types of complete mappings*, Finite Fields and Their Applications 83 (2022), 102088, DOI 10.1016/j.ffa.2022.102088.

**Novelty boundary**

Do **not** claim a new general theory of affine permutation cycles.

Our affine normal form is relevant as a reduction of this specific component-placement problem.

---

### 2.7 Finite abelian \(p\)-groups, chain rings and orbit classification

Orbit classification under automorphism/general-linear actions on finite abelian groups and finite chain rings is established.

**Relevant sources**

- Kunal Dutta & Amritanshu Prasad, *Degenerations and orbits in finite abelian groups*, Journal of Combinatorial Theory A 118 (2011), 1685–1694, DOI 10.1016/j.jcta.2011.02.002.
- Yonglin Cao, *Association Schemes and Directed Graphs Determined by Orbitals of General Linear Groups Over Finite Chain Rings*, Communications in Algebra 39 (2011), 220–236, DOI 10.1080/00927870903390652.
- Classical background: Birkhoff, *Subgroups of Abelian Groups*, Proc. London Math. Soc. (2) 38 (1935), 385–401.

**Novelty boundary**

The decomposition of a finite abelian problem prime by prime by CRT, and classification by valuations plus residual unit data, should be presented as an elementary specialization of standard \(p\)-primary orbit ideas unless a deeper literature audit establishes otherwise.

In particular, the theorem

\[
[(s,\rho)]_{U(n)}
\longleftrightarrow
\{(a_p,b_p,m_p,r_p)\}_{p\mid n}
\]

is useful and exact for this project, but should **not** currently be advertised as a new general orbit-classification theorem.

---

## 3. Claim-by-claim novelty matrix

| Project result | Prior-art risk | Current novelty status | Recommended paper wording |
|---|---:|---|---|
| Dart/rotation representation of the graph | Very high | Standard | Use standard rotation-system/combinatorial-map terminology |
| Deterministic routing permutation on darts | High | General mechanism standard | Define our special routing rule only |
| \(T_n\) family and exact counts \(V=7n-1,E=16n,|D|=32n\) | Low–medium | **Candidate family-specific contribution** | “For the family defined here, we prove…” |
| Reduction to \(L/R\) macro states and \(C3/C6/C20\) cores | Low–medium | **Candidate family-specific contribution** | Present as the principal structural lemma |
| \(s=2(\delta+c_{AB}+c_{BC})\) | Low | **Strong candidate specific theorem** | Claim for the defined family, not generally |
| Reduction to \(\mathcal A(q,s)\) | Low–medium | **Strong candidate specific theorem** | Main normal-form theorem |
| Coarse \(Q(q,s)\), \(k_{\min}(q,s)\), routing census | Low | **Strong candidate specific classification** | Central theorem package |
| Original slice \(Q=52\iff n\in\{8,12,24\}\) | Low | **Candidate corollary** | Emphasize it is a corollary of family classification |
| \(h_{AB},h_{BC}\) component formulas | Medium | Likely elementary specialization | Include as lemmas; avoid standalone novelty claim |
| Same coarse quotient / different graph microstructure | Medium | Mechanism standard, witnesses specific | “Explicit separation examples in this family” |
| Component-aware refined observation | High as concept | General concept standard | Novelty only in exact family result |
| Original PIFI \(52\to52\) under component refinement | Low | **Interesting family-specific robustness result** | Worth highlighting |
| \(Q_{\rm comp}=8+\sum|\operatorname{prim}(W)|\) decorated orbit formula | Medium | Primitive-word machinery standard; exact reduction specific | **Candidate contribution as exact reduction theorem** |
| Counterexample \(Q_{\rm comp}\ne F(n,s,h_{AB},h_{BC})\) | Low | **Candidate specific negative theorem** | Strong claim within defined family |
| Raw placement normal form \(\Pi_0=(n,s,d_{AB},d_{BC},\rho)\) | Low–medium | **Candidate family-specific reduction** | Present as normal-form lemma |
| Affine gauge \([(s,\rho)]_{U(n)}\) | Medium | Group action standard, reduction specific | Do not imply new affine-group theory |
| CRT tuple \((a_p,b_p,m_p,r_p)\) | High as general arithmetic | Likely standard/derivable machinery | Use as self-contained lemma supporting the family theorem |
| End-to-end graph \(\to\) macro \(\to\) observation \(\to\) CRT classification | Low | **Strongest novelty candidate as an integrated exact classification** | Main publication framing |

---

## 4. What targeted searches did NOT locate

The audit used broad and exact-phrase searches around combinations of:

- “routed rotation system”;
- “future quotient” + rotation systems;
- “component-labelled macro orbit”;
- \(Q=52\) + graph/sofic/future states;
- \(\gcd(q,6)\) + routing/graph dynamics;
- the project-specific \(C3/C6/C20\) macro-word structure;
- component-aware future quotient + affine placement;
- the exact combination \(s=2(\delta+c_{AB}+c_{BC})\).

No mathematically relevant source matching the complete project-specific theorem chain was located.

This is evidence only for the wording:

\[
\boxed{
\text{“not located in the targeted prior-art pass.”}
}
\]

It is **not** sufficient for:

\[
\boxed{
\text{“first ever”, “new theory”, or “proved novel”.}
}
\]

---

## 5. Strongest defensible novelty candidate

The strongest publication claim is the following package.

### Candidate core theorem package

Define the routed rotation-system family

\[
\mathcal T_{n;\delta,c_{AB},c_{BC}},
\qquad n=4q,
\]

with the frozen local rotation/routing rules.

Then:

1. the \(32n\)-dart dynamics admits an exact \(2n\)-state macro reduction;
2. all coarse routing is controlled by

\[
\boxed{
s=2(\delta+c_{AB}+c_{BC})\pmod n;
}
\]

3. the macro dynamics is conjugate/reducible to the canonical arithmetic system

\[
\boxed{\mathcal A(q,s);}
\]

4. its primitive future classes, state count \(Q\), resolving depth \(k_{\min}\), and cycle census admit exact arithmetic formulas;
5. a coarser observation can identify distinct graph microstructures;
6. component-aware refinement yields an exact decorated-periodic-orbit formula for \(Q_{\rm comp}\);
7. component placement reduces to a finite affine class and then to a prime-power CRT signature.

The novelty candidate is therefore the **complete solvability/classification of this explicit family**, not the generic ingredients.

---

## 6. The role of the original PIFI slice

The original PIFI wiring

\[
(\delta,c_{AB},c_{BC})=(1,1,1)
\]

has two particularly clean consequences inside the general classification.

### Coarse arithmetic exceptional set

For the original slice,

\[
s=6.
\]

The coarse theorem gives

\[
\boxed{
Q=52
\iff
n\in\{8,12,24\}.
}
\]

The \(n=12\) object is therefore special but not isolated.

### Robustness under component-aware refinement

At \(n=12\),

\[
h_{AB}=h_{BC}=1.
\]

Hence the exact component refinement adds no nontrivial annular component information, and

\[
\boxed{
Q_{\rm coarse}=Q_{\rm comp}=52.
}
\]

This is a useful negative/robustness result: the original \(52\) does not arise merely because the observation alphabet forgot nontrivial AB/BC component identities.

### Publication caution

The number \(52\) itself should not be marketed as a universal constant or as intrinsically physically significant.

Its value is meaningful **inside the precisely defined routed family and observation convention**.

---

## 7. Recommended standard terminology

To make the manuscript legible to specialists, replace or pair project vocabulary with established terminology.

| Project term | Recommended standard description |
|---|---|
| routed system | finite deterministic output system / permutation system on darts |
| rotation template | rotation system / combinatorial-map local rotation data |
| future quotient | follower/right-language quotient; Nerode-style output equivalence |
| future state | equivalence class of states with the same infinite output future |
| terminal observation | output labeling / observation map |
| refined terminal observation | refinement of the output alphabet / observation partition |
| component orbit | component-decorated periodic orbit |
| primitive terminal word | primitive cyclic output word / primitive necklace representative |
| macro frame | return section / induced state block |
| macro dynamics | induced/return permutation on frame-entry states |
| affine gauge | relabeling/conjugacy under an affine index action |
| CRT placement signature | prime-power invariant for the diagonal scalar-unit action |

The paper may keep the short project names \(C3,C6,C20,L,R\), but only after formal definitions.

---

## 8. Recommended publication framing

### Strong framing

> **An exactly solvable family of routed rotation systems with observation-dependent future quotients**

Possible subtitle:

> **Arithmetic macro reduction, information loss, component-decorated periodic orbits, and CRT placement classes**

This framing puts the contribution where the audit currently supports it:

- an explicit finite combinatorial family;
- an exact reduction;
- exact state/cycle formulas;
- an observation/refinement hierarchy;
- a complete arithmetic classification of the placement data.

### Weaker / risky framing to avoid

Avoid titles or abstracts suggesting:

- a new theory of symbolic dynamics;
- a new theory of graph coverings;
- a new general voltage-graph theorem;
- a new Myhill–Nerode theorem;
- a new general CRT theorem;
- a new classification of finite abelian group orbits;
- a physical law derived from \(52\), \(6\), or the PIFI geometry.

---

## 9. Suggested theorem hierarchy for a manuscript

A clean article should not reproduce the historical order of discovery.

Recommended logical order:

### Definition 1 — routed rotation-system family

Define

\[
\mathcal T_{n;\delta,c_{AB},c_{BC}}.
\]

### Lemma 2 — graph counts and degree data

\[
V=7n-1,\quad E=16n,\quad |D|=32n.
\]

### Theorem 3 — exact macro reduction

\[
\mathcal T_{n;\delta,c_{AB},c_{BC}}
\longrightarrow
\mathcal A(q,s),
\]

where

\[
s=2(\delta+c_{AB}+c_{BC}).
\]

### Theorem 4 — coarse future classification

Give \(g,m\), primitive words, \(Q\), \(k_{\min}\), and cycle census.

### Corollary 5 — original PIFI slice

\[
Q=52\iff n\in\{8,12,24\}.
\]

### Theorem 6 — microscopic annular invariants

Give \(h_{AB},h_{BC}\).

### Proposition 7 — coarse information loss

Give explicit same-coarse/different-microstructure witnesses.

### Theorem 8 — component-aware orbit formula

\[
Q_{\rm comp}
=
8+\sum|\operatorname{prim}(W)|.
\]

### Proposition 9 — component counts are insufficient

Use the \(192/312\) counterexample.

### Theorem 10 — affine placement normal form

\[
\Theta=(n,d_{AB},d_{BC},[(s,\rho)]_{U(n)}).
\]

### Lemma 11 — CRT prime-power description

Give \((a_p,b_p,m_p,r_p)\).

### Final theorem/corollary — complete computationally verified classification chain

State exactly which implications are equivalences and which are one-way.

---

## 10. Important final-control boundary

The final control established a subtle distinction that must survive into publication.

The CRT signature is necessary and sufficient for the **diagonal affine placement orbit**:

\[
\boxed{
\Psi=\Psi'
\iff
[(s,\rho)]_{U(n)}
=
[(s',\rho')]_{U(n)}.
}
\]

But the future language can be coarser.

The final control found cross-CRT future-language coincidences after component-label renaming.

Therefore do **not** state

\[
\text{same future language}
\iff
\text{same CRT placement class}.
\]

The defensible direction is

\[
\boxed{
\text{same CRT placement class}
\Rightarrow
\text{same component-colour future language}.
}
\]

This distinction materially improves the rigor of the final paper.

---

## 11. Prior-art bibliography used in this pass

1. Douglas Lind and Brian Marcus, *An Introduction to Symbolic Dynamics and Coding*, Cambridge University Press, 2nd ed., 2021. DOI: 10.1017/9781108899727.
2. Rune Johansen, *On the Structure of Covers of Sofic Shifts*, Documenta Mathematica 16 (2011), 111–131. DOI: 10.4171/DM/328.
3. Klaus Thomsen, *On the future cover of a sofic shift*, arXiv:2512.01368, 2025.
4. Isabel Hubard, Elías Mochán, Antonio Montero, *Voltage Operations on Maniplexes, Polytopes and Maps*, Combinatorica 43 (2023), 385–420. DOI: 10.1007/s00493-023-00018-7.
5. J. L. Gross and T. W. Tucker, *Topological Graph Theory*, Wiley, 1987.
6. *Dynamic Cage Survey*, Electronic Journal of Combinatorics, voltage graph lift section, 2013.
7. Alexander Bors and Qiang Wang, *Coset-wise affine functions and cycle types of complete mappings*, Finite Fields and Their Applications 83 (2022), 102088. DOI: 10.1016/j.ffa.2022.102088.
8. Kunal Dutta and Amritanshu Prasad, *Degenerations and orbits in finite abelian groups*, Journal of Combinatorial Theory A 118 (2011), 1685–1694. DOI: 10.1016/j.jcta.2011.02.002.
9. Yonglin Cao, *Association Schemes and Directed Graphs Determined by Orbitals of General Linear Groups Over Finite Chain Rings*, Communications in Algebra 39 (2011), 220–236. DOI: 10.1080/00927870903390652.
10. Garrett Birkhoff, *Subgroups of Abelian Groups*, Proceedings of the London Mathematical Society (2) 38 (1935), 385–401.
11. Standard necklace/primitive-word literature; see also European Journal of Combinatorics 33 (2012), 1537–1546, DOI: 10.1016/j.ejc.2012.03.016.
12. *Three-dimensional maps and subgroup growth*, Manuscripta Mathematica, DOI: 10.1007/s00229-021-01321-7.
13. Scholarpedia, *Symbolic dynamics*, for sliding-block codes and factor maps.

---

## 12. Search limitations

This audit is substantially stronger than a casual web search, but it is not a substitute for a complete bibliographic clearance.

Before wording a journal/arXiv abstract with an unqualified novelty claim, the following should still be done:

1. dedicated MathSciNet search;
2. dedicated zbMATH Open search;
3. Google Scholar cited-by / similarity search around:
   - voltage graph cycle classifications,
   - sofic follower/future covers,
   - rotation systems with deterministic straight-ahead/opposite-edge routing,
   - cyclic/affine permutation systems,
   - orbit classifications on \(\mathbb Z_n\times\mathbb Z_d\);
4. ideally, one external specialist read by a researcher in symbolic dynamics or topological graph theory.

Until then, use:

> **“We have not located this explicit classification in the targeted prior-art search.”**

not:

> **“This is the first such result.”**

---

## 13. Overall novelty assessment

### General mathematical machinery

\[
\boxed{\text{NOT NOVEL}}
\]

for:

- rotation systems/darts;
- voltage/lift ideas;
- gcd/order behavior in cyclic covers;
- future/follower/Nerode quotients;
- observation/factor maps;
- primitive cyclic words;
- affine finite permutations;
- CRT and \(p\)-primary orbit methods.

### Exact PIFI-derived routed family

\[
\boxed{\text{CREDIBLE NOVELTY CANDIDATE}}
\]

for the exact combination of:

- the defined \(\mathcal T_{n;\delta,c_{AB},c_{BC}}\) family;
- its \(2n\)-state macro reduction;
- the exact \(s\)-law;
- complete \(Q,k_{\min}\), routing-census formulas;
- explicit observation-dependent information-loss/refinement hierarchy;
- exact component-decorated orbit predictor;
- exact affine/CRT reduction of the placement data.

### Current confidence

\[
\boxed{\text{MODERATE-TO-STRONG AS A SPECIAL-FAMILY CLASSIFICATION}}
\]

provided that:

- the graph family is clearly motivated rather than artificially reverse-engineered;
- proofs are written independently of the verifier code;
- standard terminology is used;
- all general machinery is credited;
- novelty claims remain limited to the explicit family/classification.

---

## 14. Recommended next action

The mathematical branch itself should remain frozen.

The next stage is now publication-grade consolidation:

1. rewrite the theorem chain into one self-contained manuscript;
2. separate proofs from computational regression evidence;
3. add a prior-art/claim-boundary section using this audit;
4. make the final verifier executable from one clean public repository;
5. reproduce from a clean checkout;
6. freeze a public release/tag;
7. only after that decide whether to submit the manuscript to arXiv / a journal and whether a DOI release is warranted.

No further wiring parameter should be introduced before that consolidation.
