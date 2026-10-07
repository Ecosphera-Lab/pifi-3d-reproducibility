# PIFI-3D v0.6 release notes

## Scope

This release freezes the family-classification branch described in the
manuscript:

**An Exactly Solvable Family of Routed Rotation Systems with
Observation-Dependent Future Quotients**

The release is intentionally narrower than the earlier geometry/voltage
research package.

## Mathematical chain

\[
\mathcal T_{n;\delta,c_{AB},c_{BC}}
\to
s=2(\delta+c_{AB}+c_{BC})
\to
\mathcal A(q,s)
\to
(Q,k_{\min},\text{cycle census})
\]

followed by

\[
\text{refined observation}
\to
\text{decorated macro orbits}
\to
\text{affine placement}
\to
\text{CRT prime-power classification}.
\]

## Frozen original PIFI anchor

\[
n=12,\qquad
(\delta,c_{AB},c_{BC})=(1,1,1),
\]

\[
Q_{\rm coarse}=Q_{\rm comp}=52,\qquad
k_{\min}=13,
\]

primitive periods:

\[
8,\ 12,\ 12,\ 20.
\]

## Main release change

The article has been rewritten in theorem order rather than research-history
order.  Standard machinery is explicitly separated from the family-specific
candidate contribution.

## Reproduction

\`\`\`bash
python run_all.py
\`\`\`

## Publication-priority wording

> Not located in the targeted prior-art pass; not yet a global novelty claim.

## v0.6 release quality gate (2026-10-07)

A final release review identified a literal `\\n` suffix in the affine-gauge
verifier's emitted JSON. The verifier output has been corrected, and
`run_all.py` now validates every fresh JSON result, failing on malformed
output or invalid schema/status. Regression tests reproduce the former failure.
This is a release-format fix, not a change to mathematical formulas.

The committed `SHA256SUMS` covers the tracked source tree except itself.
On a clean checkout, check it using `sha256sum -c SHA256SUMS`.
