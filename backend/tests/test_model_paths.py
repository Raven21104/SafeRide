import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from app.core.config import settings


class ModelPathTests(unittest.TestCase):
    def test_default_model_paths_match_current_repo_files(self):
        repo_root = Path(__file__).resolve().parents[2]
        self.assertEqual(settings.object_model_path, repo_root / "models" / "yolo11s (1).pt")
        self.assertEqual(settings.helmet_model_path, repo_root / "models" / "helmet-v4-best.pt")
        self.assertEqual(settings.plate_model_path, repo_root / "models" / "license-plate-v4-best.pt")


if __name__ == "__main__":
    unittest.main()
