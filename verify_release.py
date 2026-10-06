#!/usr/bin/env python3
"""Fast consistency check for the frozen public v0.6 release."""

from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent


def load(name):
    return json.loads((ROOT / "results" / name).read_text(encoding="utf-8"))


split = load("pifi_3d_tn_split_annular_offset_v0_1.json")
refined = load("pifi_3d_refined_terminal_injectivity_v0_1.json")
orbit = load("pifi_3d_refined_quotient_component_orbit_v0_1.json")
affine = load("pifi_3d_component_placement_affine_gauge_v0_1.json")
crt = load("pifi_3d_crt_prime_power_placement_v0_1.json")
final = load("pifi_3d_final_classification_control_v0_1.json")
novelty = load("pifi_3d_specialist_novelty_literature_audit_v0_1.json")

assert "STRONG PASS" in split["status"]
assert "STRONG PASS" in refined["status"]
assert "STRONG PASS" in orbit["status"]
assert "STRONG PASS" in affine["status"]
assert "STRONG PASS" in crt["status"]
assert "FINAL CONTROL PASS" in final["status"]
assert "NOVELTY CANDIDATE" in novelty["status"]

pifi = final["anchors"]["original_PIFI"]
for sign in ("HT_plus", "HT_minus"):
    row = pifi[sign]
    assert row["Q_coarse"] == 52
    assert row["Q_refined"] == 52
    assert row["k_min"] == 13
    assert row["periods"] == [8, 12, 12, 20]

assert orbit["same_counts_different_Q_counterexample"]["case_A"]["Q_comp"] == 192
assert orbit["same_counts_different_Q_counterexample"]["case_B"]["Q_comp"] == 312
assert crt["regression"]["PIFI_family_bijection"]["bijection_mismatches"] == 0

main = (ROOT / "paper" / "main.tex").read_text(encoding="utf-8")
for needle in (
    r"s=2(\delta+c_{AB}+c_{BC})",
    r"Q=52",
    r"Q_{\rm comp}",
    r"\Theta_{\rm CRT}",
):
    assert needle in main, needle

print("PIFI-3D public release v0.6 frozen consistency: PASS")
