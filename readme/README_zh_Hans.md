<p align="center">
  <img src="https://raw.githubusercontent.com/apixly-ai/dify-apixly-creative/apixly/docs/assets/cover.png" alt="Apixly Dify 创作指令：视角、打光、相机镜头观感免费预览" width="1200" />
</p>

# Apixly 创作指令：Dify 免费预览工具

在 Dify 插件运行环境中预览角度、打光与相机镜头观感提示词。无需 Apixly 账号或 API Key，不发起图片/视频生成；Dify 自身运行资源费用由宿主管理。

**启用所需组 → 选择预设或数值 → 免费查看 final_prompt → 确认后连接独立生成工具。** 三组默认全部关闭，没有有效指令时逐字保留原提示词。编辑模式会明确要求保留未请求修改的主体与场景细节。这是 AI 创作指令，并非精确物理相机或光照模拟。

## 使用四个小节点

1. 添加 **视角、打光、相机与镜头**，每张卡片只显示自己的控制项，默认全部关闭。
2. 启用所需组，选择预设和数值。打光明确选择“命名光向 / 明确坐标”，空坐标不会自动变成 0。
3. 将三张卡的 **settings** 输出接入 **组合提示词** 的对应输入，并连接原始提示词；参考图编辑使用 Edit 模式。
4. 免费运行，确认 `final_prompt`；只有 `success` 为真才进入独立生成或编辑节点。

节点外壳和控件由 Dify 原生提供；简短机身/镜头名称与八张内联打光色卡复用 Apixly Studio。原“预览创作提示词 · 免费”大面板工具保留，兼容已有流程。任何控制节点失败都会传递明确失败包，后续组合不会把它当作“关闭”后继续收费。

<img src="https://raw.githubusercontent.com/apixly-ai/dify-apixly-creative/apixly/docs/assets/free-preview-desktop.png" alt="真实 Dify 免费提示词预览：显式启用视角、黄金时刻打光和 Helios 镜头" width="1200" />

截图来自 Dify Community 1.17.1 的真实无 Key 运行，示例明确启用了三组控制，没有调用模型。已发布运行页也通过 [375px 视口检查](https://raw.githubusercontent.com/apixly-ai/dify-apixly-creative/apixly/docs/assets/free-preview-mobile.png)，工作流编辑器本身仍偏桌面布局。[素材来源与校验值](../docs/assets/provenance.json)。

需要生成时再安装独立 [Apixly Media](https://github.com/apixly-ai/dify-apixly)，媒体工具保持独立凭据，可使用 secret API Key 或 Apixly 账号授权。免费预览 DSL 只依赖本包；创作生图、编辑、视频 DSL 依赖两个精确版本的插件。在已验收的 Dify 守护进程中，每包保留一个工具提供商，因此拆包保持免费预览与媒体凭据边界独立。

[官网](https://apixly.ai/) · [控制台](https://platform.apixly.ai/) · [API Key](https://platform.apixly.ai/keys) · [模型与价格](https://platform.apixly.ai/models) · [文档](https://apixly.ai/docs) · [English](../README.md)。支持：support@apixly.ai。

编译器不访问外部 API，也不增加独立存储或遥测；Dify 宿主仍可能保存工作流输入和输出。详见[隐私说明](../PRIVACY.md)。Cloud 兼容性与 Marketplace 审核是独立验收项。

## 可导入工作流

| 工作流 | 插件 | 结果 |
| --- | --- | --- |
| [免费提示词预览](https://github.com/apixly-ai/dify-apixly/blob/apixly/examples/apixly-studio-preview-workflow.yml) | 仅本插件 | 最终提示词或安全错误；零生成 |
| [创作生图](https://github.com/apixly-ai/dify-apixly/blob/apixly/examples/apixly-studio-image-workflow.yml) | 本插件 + Apixly Media | 一次图片任务与文件 |
| [创作编辑](https://github.com/apixly-ai/dify-apixly/blob/apixly/examples/apixly-studio-edit-workflow.yml) | 本插件 + Apixly Media | 一次编辑任务与文件 |
| [创作视频](https://github.com/apixly-ai/dify-apixly/blob/apixly/examples/apixly-studio-video-workflow.yml) | 本插件 + Apixly Media | 一次视频任务与文件 |

新项目推荐四份 Studio 工作流，原八份媒体/创作工作流继续兼容。请安装工作流所引用的精确包。示例默认关闭全部控制组，只有显式启用才添加指令。打光预设复用 Apixly Studio 已有渐变色卡；相机镜头使用相同的简短名称。节点外壳与参数控件由 Dify 原生提供。
