import hashlib
import json
import unittest
from pathlib import Path

from apixly_creative.creative import EDIT_GUARD, CreativePromptError, compose_creative_prompt
from apixly_creative.settings import compose_settings, failed_settings, make_settings


class StudioSettingsTests(unittest.TestCase):
    def test_disabled_panels_preserve_prompt_exactly_and_canonical_bytes_stay_frozen(self):
        values = {"prompt": " \ufeffA toy car.\n\n😀  ", "mode": "edit"}
        for tool, parameter in [
            ("angle", "viewpoint_settings"),
            ("lighting", "lighting_settings"),
            ("camera", "camera_settings"),
        ]:
            result = make_settings(tool, {})
            packet = json.loads(result["settings"])
            self.assertIs(packet["settings"]["enabled"], False)
            self.assertTrue(result["success"])
            values[parameter] = result["settings"]
        output = compose_settings(values)
        self.assertEqual(output["final_prompt"], values["prompt"])
        self.assertFalse(output["changed"])
        self.assertEqual(
            hashlib.sha256(Path("apixly_creative/creative.py").read_bytes()).hexdigest(),
            "f6ae30104545eb02bda94071dfaf2c37b732facf83926ffeb532f7d1fb12587c",
        )

    def test_three_panels_compose_once_with_exact_shared_contract_and_one_edit_guard(self):
        angle = make_settings(
            "angle", {"enabled": True, "preset": "front_high", "shot": "close_up"}
        )
        light = make_settings(
            "lighting",
            {
                "enabled": True,
                "preset": "goldenHour",
                "direction_mode": "named",
                "key_light": "left",
            },
        )
        camera = make_settings(
            "camera", {"enabled": True, "lens": "helios-44-2", "focal": 85, "aperture": "f/1.4"}
        )
        output = compose_settings(
            {
                "prompt": "Keep the exact red car.",
                "mode": "edit",
                "viewpoint_settings": angle["settings"],
                "lighting_settings": light["settings"],
                "camera_settings": camera["settings"],
            }
        )
        expected = compose_creative_prompt(
            {
                "prompt": "Keep the exact red car.",
                "mode": "edit",
                "tools": {
                    name: json.loads(result["settings"])["settings"]
                    for name, result in [("angle", angle), ("lighting", light), ("camera", camera)]
                },
            }
        )
        self.assertEqual(output, expected)
        self.assertEqual(output["final_prompt"].count(EDIT_GUARD), 1)

    def test_named_lighting_ignores_inactive_coordinate_widgets_and_coordinates_require_intent(
        self,
    ):
        named = make_settings(
            "lighting",
            {"enabled": True, "direction_mode": "named", "key_light": "left", "yaw": 0, "pitch": 0},
        )
        settings = json.loads(named["settings"])["settings"]
        self.assertNotIn("lightYaw", settings)
        self.assertNotIn("lightPitch", settings)
        self.assertIn("camera left", named["preview"])
        coords = make_settings(
            "lighting",
            {
                "enabled": True,
                "direction_mode": "coordinates",
                "yaw": 0,
                "pitch": None,
                "key_light": "left",
            },
        )
        settings = json.loads(coords["settings"])["settings"]
        self.assertEqual(settings["lightYaw"], 0)
        self.assertNotIn("lightPitch", settings)
        self.assertNotIn("keyLight", settings)
        with self.assertRaises(CreativePromptError) as raised:
            make_settings("lighting", {"enabled": True, "direction_mode": "coordinates"})
        self.assertEqual(raised.exception.path, "tools.lighting.direction_mode")
        disabled = make_settings("lighting", {"enabled": False, "direction_mode": "coordinates"})
        self.assertTrue(disabled["success"])

    def test_forged_packet_is_revalidated_and_cannot_supply_final_prompt(self):
        packet = json.loads(make_settings("angle", {"enabled": True})["settings"])
        packet["settings"]["final_prompt"] = "PRIVATE_INVALID_VALUE"
        with self.assertRaises(CreativePromptError) as raised:
            compose_settings({"prompt": "A car.", "viewpoint_settings": json.dumps(packet)})
        self.assertIn("tools.angle", raised.exception.path)
        self.assertNotIn("PRIVATE_INVALID_VALUE", str(raised.exception))
        packet["tool"] = "camera"
        with self.assertRaises(CreativePromptError):
            compose_settings({"prompt": "A car.", "viewpoint_settings": json.dumps(packet)})

    def test_failed_packet_never_looks_like_an_unconnected_disabled_panel(self):
        failed = failed_settings("lighting", "tools.lighting.color")
        self.assertTrue(failed)
        self.assertIs(json.loads(failed)["success"], False)
        with self.assertRaises(CreativePromptError) as raised:
            compose_settings({"prompt": "A car.", "lighting_settings": failed})
        self.assertEqual(raised.exception.path, "tools.lighting")
        self.assertEqual(compose_settings({"prompt": "A car."})["final_prompt"], "A car.")

    def test_native_unspecified_sentinel_maps_only_optional_selects_to_canonical_empty(self):
        camera = make_settings(
            "camera",
            {"enabled": True, "body": "__none__", "lens": "__none__", "aperture": "__none__"},
        )
        self.assertEqual(camera["preview"], "")
        self.assertEqual(
            json.loads(camera["settings"])["settings"],
            {"enabled": True, "body": "", "lens": "", "aperture": ""},
        )
        light = make_settings(
            "lighting",
            {
                "enabled": True,
                "preset": "__none__",
                "key_light": "__none__",
                "smart_text": "__none__",
            },
        )
        self.assertEqual(json.loads(light["settings"])["settings"]["preset"], "")
        self.assertEqual(json.loads(light["settings"])["settings"]["smartText"], "__none__")

    def test_invalid_inputs_have_safe_field_paths_without_echoing_values(self):
        for tool, parameters in [
            ("angle", {"yaw": float("nan")}),
            ("camera", {"focal": True}),
            ("lighting", {"enabled": True, "color": "#000"}),
            ("lighting", {"direction_mode": "PRIVATE_INVALID_VALUE"}),
            ("lighting", {"direction_mode": []}),
            ("angle", {"final_prompt": "PRIVATE_INVALID_VALUE"}),
        ]:
            with self.subTest(tool=tool), self.assertRaises(CreativePromptError) as raised:
                make_settings(tool, parameters)
            self.assertNotIn("PRIVATE_INVALID_VALUE", str(raised.exception))
        for value in [None, [], "private-invalid-value"]:
            with self.assertRaises(CreativePromptError):
                make_settings("angle", value)
        with self.assertRaises(CreativePromptError) as raised:
            compose_settings({"prompt": "A car.", "lighting_settings": "PRIVATE_INVALID_VALUE"})
        self.assertNotIn("PRIVATE_INVALID_VALUE", str(raised.exception))


if __name__ == "__main__":
    unittest.main()
