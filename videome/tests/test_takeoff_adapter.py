import importlib.util
from pathlib import Path
import tempfile
import unittest

path = Path(__file__).resolve().parents[1] / "tools" / "takeoff_adapter.py"
spec = importlib.util.spec_from_file_location("takeoff_adapter", path)
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)

class TakeOffAdapterTests(unittest.TestCase):
    def test_missing_install(self):
        with tempfile.TemporaryDirectory() as d:
            with self.assertRaises(FileNotFoundError):
                mod.run(d, "doctor")
    def test_slug_rejection(self):
        with tempfile.TemporaryDirectory() as d:
            (Path(d) / "edit").write_text("#!/bin/sh\n")
            with self.assertRaises(ValueError):
                mod.run(d, "render", "../bad")
    def test_action_rejection(self):
        with tempfile.TemporaryDirectory() as d:
            (Path(d) / "edit").write_text("#!/bin/sh\n")
            with self.assertRaises(ValueError):
                mod.run(d, "install")
    def test_version_rejection(self):
        with tempfile.TemporaryDirectory() as d:
            (Path(d) / "edit").write_text("#!/bin/sh\n")
            with self.assertRaises(ValueError):
                mod.run(d, "render", "demo", "latest;rm")

if __name__ == "__main__":
    unittest.main()
