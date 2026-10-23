# Apixly 创作指令：Dify 免费预览工具

在 Dify 插件运行环境中预览角度、打光与相机镜头观感提示词。无需 Apixly 账号或 API Key，不发起图片/视频生成；Dify 自身运行资源费用由宿主管理。

**启用所需组 → 选择预设或数值 → 免费查看 final_prompt → 确认后连接独立生成工具。** 三组默认全部关闭，没有有效指令时逐字保留原提示词。编辑模式会明确要求保留未请求修改的主体与场景细节。这是 AI 创作指令，并非精确物理相机或光照模拟。

安装独立 `apixly_creative` 包后，选择 **Apixly Creative Controls → 预览创作提示词 · 免费** 即可，无需凭据。错误返回 `success: false`、`error_path` 与安全提示；后续收费节点必须检查 success 再执行。

需要生成时再安装独立 [Apixly Media](https://github.com/apixly-ai/dify-apixly)，媒体工具保持独立凭据，可使用 secret API Key 或 Apixly 账号授权。免费预览 DSL 只依赖本包；创作生图、编辑、视频 DSL 依赖两个精确版本的插件。在已验收的 Dify 守护进程中，每包保留一个工具提供商，因此拆包保持免费预览与媒体凭据边界独立。

[官网](https://apixly.ai/) · [控制台](https://platform.apixly.ai/) · [API Key](https://platform.apixly.ai/keys) · [模型与价格](https://platform.apixly.ai/models) · [文档](https://apixly.ai/docs) · [English](../README.md)。支持：support@apixly.ai。

编译器不访问外部 API，也不增加独立存储或遥测；Dify 宿主仍可能保存工作流输入和输出。详见[隐私说明](../PRIVACY.md)。Cloud 兼容性与 Marketplace 审核是独立验收项。

## 可导入工作流

| 工作流 | 插件 | 结果 |
| --- | --- | --- |
| [免费提示词预览](https://github.com/apixly-ai/dify-apixly/blob/apixly/examples/apixly-creative-preview-workflow.yml) | 仅本插件 | 最终提示词或安全错误；零生成 |
| [创作生图](https://github.com/apixly-ai/dify-apixly/blob/apixly/examples/apixly-creative-image-workflow.yml) | 本插件 + Apixly Media | 一次图片任务与文件 |
| [创作编辑](https://github.com/apixly-ai/dify-apixly/blob/apixly/examples/apixly-creative-edit-workflow.yml) | 本插件 + Apixly Media | 一次编辑任务与文件 |
| [创作视频](https://github.com/apixly-ai/dify-apixly/blob/apixly/examples/apixly-creative-video-workflow.yml) | 本插件 + Apixly Media | 一次视频任务与文件 |

请安装工作流所引用的精确包。示例默认关闭全部控制组，只有显式启用才添加指令。打光预设复用 Apixly Studio 已有渐变色卡；相机镜头使用相同的简短名称。节点外壳与参数控件由 Dify 原生提供。
