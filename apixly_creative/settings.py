"""Keyless Studio panel packets; the frozen creative compiler remains authoritative."""

from __future__ import annotations

import json
from typing import Any

from apixly_creative.creative import CreativePromptError, compose_creative_prompt

PANEL_FIELDS = {
    "angle": {
        "enabled": "enabled",
        "preset": "preset",
        "yaw": "yaw",
        "pitch": "pitch",
        "shot": "shot",
        "show_prompt": "showPrompt",
    },
    "lighting": {
        "enabled": "enabled",
        "preset": "preset",
        "brightness": "brightness",
        "color": "color",
        "key_light": "keyLight",
        "yaw": "lightYaw",
        "pitch": "lightPitch",
        "rim_light": "rimLight",
        "smart_text": "smartText",
        "view": "view",
    },
    "camera": {
        "enabled": "enabled",
        "body": "body",
        "lens": "lens",
        "focal": "focal",
        "aperture": "aperture",
    },
}
PANEL_DEFAULTS = {
    "angle": {"enabled": False, "preset": "custom", "yaw": 0, "pitch": 0, "shot": "none"},
    "lighting": {
        "enabled": False,
        "preset": "",
        "brightness": 50,
        "color": "",
        "key_light": "",
        "rim_light": False,
        "smart_text": "",
    },
    "camera": {"enabled": False, "body": "", "lens": "", "aperture": ""},
}
PACKET_FIELDS = {
    "viewpoint_settings": "angle",
    "lighting_settings": "lighting",
    "camera_settings": "camera",
}


def _group(group: str) -> None:
    if group not in PANEL_FIELDS:
        raise CreativePromptError("settings", "unknown control group")


def failed_settings(group: str, error_path: str) -> str:
    """Failure is a nonempty packet so a connected failure cannot become 'off'."""
    _group(group)
    return json.dumps(
        {"version": 1, "tool": group, "success": False, "error_path": error_path},
        separators=(",", ":"),
    )


def make_settings(group: str, parameters: dict[str, Any]) -> dict[str, Any]:
    _group(group)
    if type(parameters) is not dict:
        raise CreativePromptError(f"tools.{group}", "settings must be an object")
    allowed = set(PANEL_FIELDS[group]) | ({"direction_mode"} if group == "lighting" else set())
    for field in parameters:
        if field not in allowed:
            safe = field if isinstance(field, str) and field.isidentifier() else "unknown_field"
            raise CreativePromptError(f"tools.{group}.{safe}", "unknown control input")
    values = {**PANEL_DEFAULTS[group], **parameters}
    settings = {}
    for field, canonical in PANEL_FIELDS[group].items():
        if field not in values:
            continue
        value = values[field]
        optional_selects = {
            "lighting": {"preset", "key_light"},
            "camera": {"body", "lens", "aperture"},
        }
        if field in optional_selects.get(group, set()) and value == "__none__":
            # Dify's native Select ignores an empty selection event. A nonempty
            # UI sentinel makes 'Unspecified' selectable; packets remain canonical.
            value = ""
        if (
            (group == "lighting" and field in {"yaw", "pitch"})
            or (group == "camera" and field == "focal")
        ) and value in (None, ""):
            continue
        settings[canonical] = value
    # Validate even inactive native widgets through the same contract. Their
    # values never become directions unless the explicit mode selects them.
    preview = compose_creative_prompt(
        {"prompt": "", "mode": "generate", "tools": {group: settings}}
    )
    if group == "lighting":
        mode = parameters.get("direction_mode", "named")
        if not isinstance(mode, str) or mode not in {"named", "coordinates"}:
            raise CreativePromptError(
                "tools.lighting.direction_mode", "choose named direction or coordinates"
            )
        if mode == "named":
            settings.pop("lightYaw", None)
            settings.pop("lightPitch", None)
        else:
            if settings.get("enabled") is True and not any(
                field in settings for field in ("lightYaw", "lightPitch")
            ):
                raise CreativePromptError(
                    "tools.lighting.direction_mode",
                    "enter at least one coordinate in coordinate mode",
                )
            settings.pop("keyLight", None)
        preview = compose_creative_prompt(
            {"prompt": "", "mode": "generate", "tools": {group: settings}}
        )
    packet = {"version": 1, "tool": group, "success": True, "settings": settings}
    return {
        "success": True,
        "settings": json.dumps(packet, ensure_ascii=False, separators=(",", ":"), allow_nan=False),
        "preview": "\n".join(section["text"] for section in preview["sections"]),
    }


def compose_settings(parameters: dict[str, Any]) -> dict[str, Any]:
    if type(parameters) is not dict:
        raise CreativePromptError("payload", "must be an object")
    if set(parameters) - {"prompt", "mode", *PACKET_FIELDS}:
        raise CreativePromptError("payload", "unknown compose input")
    groups = {}
    for field, group in PACKET_FIELDS.items():
        value = parameters.get(field)
        if value is None or value == "":
            continue
        path = f"tools.{group}"
        if (
            not isinstance(value, str)
            or len(value.encode("utf-16-le", errors="surrogatepass")) // 2 > 16000
        ):
            raise CreativePromptError(path, "connect the settings output from its control node")
        try:
            packet = json.loads(value)
        except ValueError:
            raise CreativePromptError(path, "settings packet is invalid") from None
        if (
            type(packet) is not dict
            or set(packet) - {"version", "tool", "success", "settings", "error_path"}
            or type(packet.get("version")) is not int
            or packet["version"] != 1
            or packet.get("tool") != group
        ):
            raise CreativePromptError(path, "settings packet does not match this control node")
        if packet.get("success") is not True:
            raise CreativePromptError(path, "fix this control node before continuing")
        groups[group] = packet.get("settings")
    # Never trust a prebuilt prompt or a packet's success flag as validation.
    # All groups are compiled together once, including the single edit guard.
    return compose_creative_prompt(
        {
            "prompt": parameters.get("prompt", ""),
            "mode": parameters.get("mode", "generate"),
            "tools": groups,
        }
    )
