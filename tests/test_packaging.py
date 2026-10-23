import unittest
from pathlib import Path

import yaml


class SingleProviderTests(unittest.TestCase):
    def test_independent_companion_has_one_provider_and_no_api_key(self):
        m = yaml.safe_load(Path("manifest.yaml").read_text())
        self.assertEqual(m["name"], "apixly_creative")
        self.assertEqual(m["version"], "0.1.0")
        self.assertEqual(m["plugins"]["tools"], ["provider/creative.yaml"])
        p = yaml.safe_load(Path("provider/creative.yaml").read_text())
        self.assertEqual(p["credentials_for_provider"], {})
