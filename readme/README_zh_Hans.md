# Apixly 创作指令：Dify 免费预览工具

在 Dify 插件运行环境中预览角度、打光与相机镜头观感提示词。无需 Apixly 账号或 API Key，不发起图片/视频生成；Dify 自身运行资源费用由宿主管理。

**启用所需组 → 选择预设或数值 → 免费查看 final_prompt → 确认后连接独立生成工具。** 三组默认全部关闭，没有有效指令时逐字保留原提示词。编辑模式会明确要求保留未请求修改的主体与场景细节。这是 AI 创作指令，并非精确物理相机或光照模拟。

安装独立 `apixly_creative` 包后，选择 **Apixly Creative Controls → 预览创作提示词 · 免费** 即可，无需凭据。错误返回 `success: false`、`error_path` 与安全提示；后续收费节点必须检查 success 再执行。

需要生成时再安装独立 [Apixly Media](https://github.com/apixly-ai/dify-apixly)，其 API Key 仍为必需的 secret credential。免费预览 DSL 只依赖本包；创作生图、编辑、视频 DSL 依赖两个精确版本的插件。每个插件仅声明一个工具提供商，保持免费预览与 API 凭据边界独立。

[官网](https://apixly.ai/) · [控制台](https://platform.apixly.ai/) · [API Key](https://platform.apixly.ai/keys) · [模型与价格](https://platform.apixly.ai/models) · [文档](https://apixly.ai/docs) · [English](../README.md)。支持：support@apixly.ai。

编译器不访问外部 API，也不增加独立存储或遥测；Dify 宿主仍可能保存工作流输入和输出。详见[隐私说明](../PRIVACY.md)。Cloud 兼容性与 Marketplace 审核是独立验收项。
