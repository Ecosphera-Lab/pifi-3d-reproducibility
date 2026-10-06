#!/usr/bin/env python3
"""Run the frozen PIFI-3D family classification reproduction chain."""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
OUT = ROOT / "reproduced"
OUT.mkdir(exist_ok=True)

COMMANDS = [
    [
        "tools/verify_pifi_3d_tn_split_annular_offset_v0_1.py",
        "--output", str(OUT / "split_annular.json"),
    ],
    [
        "tools/verify_pifi_3d_refined_terminal_injectivity_v0_1.py",
        "--output", str(OUT / "refined_terminal.json"),
    ],
    [
        "tools/verify_pifi_3d_refined_quotient_component_orbit_v0_1.py",
        "--output", str(OUT / "component_orbit.json"),
    ],
    [
        "tools/verify_pifi_3d_component_placement_affine_gauge_v0_1.py",
        "--output", str(OUT / "affine_gauge.json"),
    ],
    [
        "tools/verify_pifi_3d_crt_prime_power_placement_v0_1.py",
        "--output", str(OUT / "crt_prime_power.json"),
    ],
    [
        "tools/verify_pifi_3d_final_classification_control_v0_1.py",
        "--output", str(OUT / "final_control.json"),
    ],
]

for i, args in enumerate(COMMANDS, 1):
    cmd = [sys.executable, str(ROOT / args[0]), *args[1:]]
    print(f"\n[{i}/{len(COMMANDS)}] {' '.join(cmd)}", flush=True)
    subprocess.run(cmd, cwd=ROOT, check=True)

print("\nPIFI-3D v0.6 reproduction chain: PASS")
print("Outputs:", OUT)
