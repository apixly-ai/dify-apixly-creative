import json
import unittest
from pathlib import Path
from unittest.mock import patch

import yaml
from dify_plugin import DifyPluginEnv
from dify_plugin.core.plugin_registration import PluginRegistration
from dify_plugin.entities.tool import ToolConfiguration

from tools.camera_lens import CameraLensTool
from tools.compose_prompt import ComposePromptTool
from tools.lighting import LightingTool
from tools.viewpoint import ViewpointTool


class StudioToolTests(unittest.TestCase):
    def invoke(self, tool_class, parameters):
        with patch("httpx.Client") as network:
            messages = list(tool_class.from_credentials({})._invoke(parameters))
            network.assert_not_called()
        return {
            message.message.variable_name: message.message.variable_value
            for message in messages
            if hasattr(message.message, "variable_name")
        }

    def test_one_credential_free_provider_has_four_studio_tools_and_legacy_tool(self):
        registration = PluginRegistration(DifyPluginEnv())
        self.assertEqual(set(registration.tools_mapping), {"apixly_creative"})
        provider, _, tools = registration.tools_mapping["apixly_creative"]
        self.assertEqual(provider.credentials_schema, [])
        self.assertEqual(
            set(tools),
            {"viewpoint", "lighting", "camera_lens", "compose_prompt", "compose_creative_prompt"},
        )

    def test_each_panel_has_only_its_own_small_typed_field_set(self):
        for name, count in [
            ("viewpoint", 5),
            ("lighting", 10),
            ("camera_lens", 5),
            ("compose_prompt", 5),
        ]:
            with self.subTest(tool=name):
                data = yaml.safe_load(Path(f"tools/{name}.yaml").read_text())
                config = ToolConfiguration.model_validate(data)
                self.assertEqual(len(config.parameters), count)
                if name != "compose_prompt":
                    enabled = next(p for p in config.parameters if p.name == "enabled")
                    self.assertIs(enabled.default, False)
                for field in data["parameters"]:
                    self.assertIn("en_US", field["label"])
                    self.assertIn("zh_Hans", field["label"])
        light = yaml.safe_load(Path("tools/lighting.yaml").read_text())
        fields = {field["name"]: field for field in light["parameters"]}
        self.assertEqual(fields["direction_mode"]["default"], "named")
        self.assertNotIn("default", fields["yaw"])
        self.assertNotIn("default", fields["pitch"])
        self.assertEqual(sum(bool(option.get("icon")) for option in fields["preset"]["options"]), 8)

    def test_default_settings_are_real_nonempty_packets_with_no_key_or_http(self):
        for tool_class, group in [
            (ViewpointTool, "angle"),
            (LightingTool, "lighting"),
            (CameraLensTool, "camera"),
        ]:
            with self.subTest(group=group):
                values = self.invoke(tool_class, {})
                packet = json.loads(values["settings"])
                self.assertTrue(values["success"])
                self.assertEqual(packet["tool"], group)
                self.assertIs(packet["settings"]["enabled"], False)

    def test_failed_lighting_packet_stops_compose_instead_of_becoming_off(self):
        light = self.invoke(LightingTool, {"enabled": True, "color": "#000"})
        self.assertFalse(light["success"])
        self.assertFalse(json.loads(light["settings"])["success"])
        result = self.invoke(
            ComposePromptTool, {"prompt": "A blue car.", "lighting_settings": light["settings"]}
        )
        self.assertFalse(result["success"])
        self.assertEqual(result["final_prompt"], "")
        self.assertEqual(result["error_path"], "tools.lighting")

    def test_typed_camera_output_wires_into_small_compose_and_keeps_edit_guard(self):
        camera = self.invoke(
            CameraLensTool,
            {"enabled": True, "lens": "helios-44-2", "focal": 85, "aperture": "f/1.4"},
        )
        result = self.invoke(
            ComposePromptTool,
            {"prompt": "Keep the same car.", "mode": "edit", "camera_settings": camera["settings"]},
        )
        self.assertTrue(result["success"])
        self.assertEqual(result["applied_tools"], ["camera"])
        self.assertIn("85mm", result["final_prompt"])
        self.assertEqual(result["final_prompt"].count("Preserve all subject and scene details"), 1)


if __name__ == "__main__":
    unittest.main()
