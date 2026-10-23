"""Shared message adapters; entrypoint files each declare exactly one SDK Tool."""

from collections.abc import Generator
from typing import Any

from dify_plugin.entities.tool import ToolInvokeMessage

from apixly_creative.creative import CreativePromptError
from apixly_creative.settings import compose_settings, failed_settings, make_settings


def panel_messages(
    tool: Any, group: str, parameters: dict
) -> Generator[ToolInvokeMessage, None, None]:
    try:
        result = {**make_settings(group, parameters), "error_path": "", "error": ""}
    except CreativePromptError as error:
        result = {
            "success": False,
            "settings": failed_settings(group, error.path),
            "preview": "",
            "error_path": error.path,
            "error": str(error),
        }
    yield tool.create_json_message(result)
    for field, value in result.items():
        yield tool.create_variable_message(field, value)
    yield tool.create_text_message(
        result["preview"] or result["error"] or "Off or neutral: no creative instruction added."
    )


def compose_messages(tool: Any, parameters: dict) -> Generator[ToolInvokeMessage, None, None]:
    try:
        result = {
            "success": True,
            "result_state": "composed",
            "error_path": "",
            "error": "",
            **compose_settings(parameters),
        }
    except CreativePromptError as error:
        result = {
            "success": False,
            "result_state": "validation_error",
            "error_path": error.path,
            "error": str(error),
            "final_prompt": "",
            "sections": [],
            "applied_tools": [],
            "changed": False,
        }
    yield tool.create_text_message(result["final_prompt"] if result["success"] else result["error"])
    yield tool.create_json_message(result)
    for field, value in result.items():
        yield tool.create_variable_message(field, value)
