"""Regression tests for the public release's fail-closed JSON validation."""
from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

from run_all import validate_json


class TestCertificateValidation(unittest.TestCase):
    SCHEMA = "pifi.3d.component_placement_affine_gauge.v0.1"

    def run_case(self, payload: str) -> dict:
        with tempfile.TemporaryDirectory() as directory:
            out = Path(directory) / "certificate.json"
            out.write_text(payload, encoding="utf-8")
            return validate_json(out, self.SCHEMA)

    def test_valid(self) -> None:
        expected = {"schema": self.SCHEMA, "status": "STRONG PASS"}
        self.assertEqual(self.run_case(json.dumps(expected) + "\n"), expected)

    def test_old_literal_newline_bug(self) -> None:
        with self.assertRaises(json.JSONDecodeError):
            self.run_case(json.dumps({"schema": self.SCHEMA, "status": "STRONG PASS"}) + "\\n")

    def test_wrong_schema(self) -> None:
        with self.assertRaises(ValueError):
            self.run_case(json.dumps({"schema": "wrong", "status": "STRONG PASS"}))

    def test_non_pass(self) -> None:
        with self.assertRaises(ValueError):
            self.run_case(json.dumps({"schema": self.SCHEMA, "status": "FAIL"}))

    def test_truncated(self) -> None:
        with self.assertRaises(json.JSONDecodeError):
            self.run_case('{"schema":"x",')

    def test_missing(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            with self.assertRaises(FileNotFoundError):
                validate_json(Path(directory) / "missing.json", self.SCHEMA)


if __name__ == "__main__":
    unittest.main()
