import importlib.util
from pathlib import Path
import tempfile
import unittest

MODULE = Path(__file__).resolve().parents[1] / "tools" / "editor_bridge.py"
spec = importlib.util.spec_from_file_location("editor_bridge", MODULE)
bridge = importlib.util.module_from_spec(spec)
spec.loader.exec_module(bridge)

class EditorBridgeTests(unittest.TestCase):
    def test_missing_vendors_not_render_ready(self):
        with tempfile.TemporaryDirectory() as d:
            report = bridge.inspect(d)
            self.assertFalse(report["ready_to_render"])
            self.assertFalse(report["takeoff"]["present"])
            self.assertEqual(report["videocut"]["operations_verified"], [])

    def test_vendor_presence_does_not_imply_compatibility(self):
        with tempfile.TemporaryDirectory() as d:
            (Path(d) / "claude-shortform-video-editor").mkdir()
            (Path(d) / "chengfeng-videocut-skills").mkdir()
            report = bridge.inspect(d)
            self.assertTrue(report["takeoff"]["present"])
            self.assertTrue(report["videocut"]["present"])
            self.assertFalse(report["takeoff"]["render_verified"])
            self.assertFalse(report["videocut"]["runtime_verified"])
            self.assertFalse(report["ready_to_render"])

    def test_missing_media_fails(self):
        self.assertFalse(bridge.verify_media("/nonexistent-videome-output.mp4")["ok"])

if __name__ == "__main__":
    unittest.main()
