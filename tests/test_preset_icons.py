import base64
import unittest
import xml.etree.ElementTree as ET
from pathlib import Path

import yaml
from dify_plugin.entities.tool import ToolConfiguration


class NativePresetIconTests(unittest.TestCase):
    def test_native_lighting_picker_reuses_all_eight_studixly_gradient_swatches(self):
        declaration = yaml.safe_load(Path("tools/compose_creative_prompt.yaml").read_text())
        config = ToolConfiguration.model_validate(declaration)
        options = next(
            parameter.options
            for parameter in config.parameters
            if parameter.name == "lighting_preset"
        )
        expected = {
            "overexposedFilm": ["#fef3c7", "#fffbeb", "#e2e8f0"],
            "blueBacklight": ["#0b1224", "#1670f0", "#7dd3fc"],
            "rembrandt": ["#b4530a", "#451a03", "#0c0a09"],
            "cyberpunk": ["#d946ef", "#0b1224", "#22d3ee"],
            "psychedelicSunset": ["#f97316", "#e11d48", "#a21caf"],
            "mysteriousDark": ["#1e293b", "#0f172a", "#020617"],
            "goldenHour": ["#fbbf24", "#f59e0b", "#b45309"],
            "nolanGray": ["#94a3b8", "#475569", "#1e293b"],
        }
        for option in options:
            if not option.value:
                continue
            with self.subTest(preset=option.value):
                self.assertTrue(
                    option.icon and option.icon.startswith("data:image/svg+xml;base64,")
                )
                svg = base64.b64decode(option.icon.split(",", 1)[1]).decode()
                image = ET.fromstring(svg)
                stops = image.findall(".//{http://www.w3.org/2000/svg}stop")
                self.assertEqual(
                    [stop.attrib["stop-color"] for stop in stops], expected[option.value]
                )
                self.assertNotIn("href=", svg)
                self.assertNotIn("script", svg)


if __name__ == "__main__":
    unittest.main()
