from dify_plugin import Tool

from tools import studio_helpers


class CameraLensTool(Tool):
    def _invoke(self, tool_parameters):
        yield from studio_helpers.panel_messages(self, "camera", tool_parameters)
