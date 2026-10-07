#!/usr/bin/env python3
"""Reproduce and validate every frozen PIFI-3D v0.6 certificate.

A verifier returning exit code 0 is not sufficient: its newly emitted JSON
must also parse and carry the expected schema/status.
"""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
OUT = ROOT / "reproduced"
OUT.mkdir(exist_ok=True)

STAGES = [
    ("verify_pifi_3d_tn_split_annular_offset_v0_1.py",
     "split_annular.json", "pifi.3d.tn_split_annular_offset.v0.1"),
    ("verify_pifi_3d_refined_terminal_injectivity_v0_1.py",
     "refined_terminal.json", "pifi.3d.refined_terminal_injectivity.v0.1"),
    ("verify_pifi_3d_refined_quotient_component_orbit_v0_1.py",
     "component_orbit.json", "pifi.3d.refined_quotient_component_orbit.v0.1"),
    ("verify_pifi_3d_component_placement_affine_gauge_v0_1.py",
     "affine_gauge.json", "pifi.3d.component_placement_affine_gauge.v0.1"),
    ("verify_pifi_3d_crt_prime_power_placement_v0_1.py",
     "crt_prime_power.json", "pifi.3d.crt_prime_power_placement.v0.1"),
    ("verify_pifi_3d_final_classification_control_v0_1.py",
     "final_control.json", "pifi.3d.final_classification_control.v0.1"),
]


def validate_json(path: Path, schema: str) -> dict:
    """Reject missing, truncated, malformed, or wrong-stage JSON."""
    with path.open("r", encoding="utf-8") as fp:
        result = json.load(fp)  # catches trailing characters, including literal \\n
    if not isinstance(result, dict):
        raise ValueError(f"{path}: expected JSON object")
    if result.get("schema") != schema:
        raise ValueError(f"{path}: schema {result.get('schema')!r} != {schema!r}")
    if "PASS" not in str(result.get("status", "")):
        raise ValueError(f"{path}: no PASS in status: {result.get('status')!r}")
    return result


def main() -> None:
    for index, (script, filename, schema) in enumerate(STAGES, 1):
        output = OUT / filename
        output.unlink(missing_ok=True)
        command = [
            sys.executable,
            str(ROOT / "tools" / script),
            "--output",
            str(output),
        ]
        print(f"\\n[{index}/{len(STAGES)}] {script}", flush=True)
        subprocess.run(command, cwd=ROOT, check=True)
        result = validate_json(output, schema)
        print(f"Valid JSON: {filename}, {result['status']}", flush=True)

    print("\\nPIFI-3D v0.6 reproduction chain: PASS (all JSON verified)")
    print("Outputs:", OUT)


if __name__ == "__main__":
    main()
