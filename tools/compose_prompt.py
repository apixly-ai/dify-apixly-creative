from dify_plugin import Tool

from tools import studio_helpers


class ComposePromptTool(Tool):
    def _invoke(self, tool_parameters):
        yield from studio_helpers.compose_messages(self, tool_parameters)
