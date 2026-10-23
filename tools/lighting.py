from dify_plugin import Tool

from tools import studio_helpers


class LightingTool(Tool):
    def _invoke(self, tool_parameters):
        yield from studio_helpers.panel_messages(self, "lighting", tool_parameters)
