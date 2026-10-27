<p align="center">
  <img src="https://raw.githubusercontent.com/apixly-ai/dify-apixly-creative/apixly/docs/assets/cover.png" alt="Apixly Dify 创作指令：视角、打光、相机镜头观感免费预览" width="1200" />
</p>

# Apixly Creative Controls for Dify：免费提示词工具

五个免费工具，组合视角、打光与相机镜头观感提示词。**无需 Apixly 账号或 API Key，不调用模型**，在 Dify 插件运行环境中预览；Dify 自身资源费用由宿主管理。

**[从 Dify Marketplace 免费安装](https://marketplace.dify.ai/plugin/apixly-ai/apixly_creative)**

**[apixly.ai](https://apixly.ai/)** · **[platform.apixly.ai](https://platform.apixly.ai/)** · [价格](https://platform.apixly.ai/models) · [API Key](https://platform.apixly.ai/keys) · [文档](https://apixly.ai/docs)

## 关于这份 Apixly 集成

**Apixly Creative Controls**（`apixly-ai/apixly_creative`）在 Dify 中格式化提示词与设置，不调用 AI 模型，也不是 API 或模型提供商。输出可以交给自己选择的生成工具。

独立的 [Apixly AI API 平台](https://apixly.ai/)与 [Apixly Media 集成](https://github.com/apixly-ai/dify-apixly)均为可选。采用这条生成路径时，可查看[图片 API 指南](https://apixly.ai/docs/images)、[视频任务指南](https://apixly.ai/docs/video)和[控制台](https://platform.apixly.ai/)。[平台与价格说明](https://github.com/apixly-ai/dify-apixly/blob/apixly/docs/ABOUT_APIXLY_zh_Hans.md)介绍更广的平台服务，不改变本工具无需凭据的行为。

## 用四个小节点组织提示词

1. 添加 **视角、打光、相机与镜头**，每张卡片只保留自己的控制项。
2. 启用所需组，再选预设或数值。打光明确选择“命名光向 / 明确坐标”；空坐标不会自动变成 0。
3. 将各卡的 **settings** 输出接入 **组合提示词** 对应输入，并连接原始提示词。参考图编辑选 **Edit**，请求保留未修改的主体与场景细节。
4. 免费运行，先查看 `final_prompt`；只有 `success` 为真才连接生成工具。

三组默认全部**关闭**，没有附加指令时逐字保留原提示词。这是 AI 创作指令，并非精确物理相机或光照模拟。原“预览创作提示词 · 免费”工具继续兼容已有流程。

<img src="https://raw.githubusercontent.com/apixly-ai/dify-apixly-creative/apixly/docs/assets/studio-workflow-desktop.png" alt="真实 Dify 编辑器：三个小控制节点连接组合提示词、成功判断与清爽结果" width="1200" />

*真实 Community 1.17.1 编辑器，三组控制关闭；节点外壳与控件由 Dify 原生提供。*

## 复用熟悉的 Studio 预设

简短机身/镜头名称与八张内联打光色卡复用 Apixly Studio。可选下拉框提供“不指定”，选过的观感也能清除。

<img src="https://raw.githubusercontent.com/apixly-ai/dify-apixly-creative/apixly/docs/assets/lighting-swatches-desktop.png" alt="真实打光下拉框：八张原有 Apixly Studio 渐变色卡" width="1000" />

## 先看结果，再生成

此演示明确启用了三组控制，未配置 Key、未调用模型。查看[桌面运行页](https://raw.githubusercontent.com/apixly-ai/dify-apixly-creative/apixly/docs/assets/free-preview-desktop.png)，或下方真实 375px 结果。

<p align="center">
  <img src="https://raw.githubusercontent.com/apixly-ai/dify-apixly-creative/apixly/docs/assets/free-preview-mobile.png" alt="真实 375px Dify 运行页：只显示组合后的提示词，没有调试 JSON" width="320" />
</p>

## 可导入工作流

| 工作流 | 插件 | 结果 |
| --- | --- | --- |
| [免费预览](https://github.com/apixly-ai/dify-apixly/blob/apixly/examples/apixly-studio-preview-workflow.yml) | 仅本插件 | 最终提示词或安全错误，零生成 |
| [创作生图](https://github.com/apixly-ai/dify-apixly/blob/apixly/examples/apixly-studio-image-workflow.yml) | 本插件 + Apixly Media | 一次图片任务与文件 |
| [参考图编辑](https://github.com/apixly-ai/dify-apixly/blob/apixly/examples/apixly-studio-edit-workflow.yml) | 本插件 + Apixly Media | 一次编辑任务与文件 |
| [创作视频](https://github.com/apixly-ai/dify-apixly/blob/apixly/examples/apixly-studio-video-workflow.yml) | 本插件 + Apixly Media | 一次视频任务与文件 |

原八份工作流继续兼容。请安装所下载 DSL 引用的精确包。控制节点失败会输出明确失败包，组合节点随即停止；示例先进入安全错误分支，不执行媒体节点。

需要生成时再安装独立 [Apixly Media](https://github.com/apixly-ai/dify-apixly)，并配置其媒体凭据。插件免费，API 按自己的 Apixly 账号实际用量计费。

## 常见问题

### 免费预览需要 Apixly 账号或 Key 吗？

不需要。五个格式化工具都不要求 Apixly 账号、API Key 或生成请求；Dify 宿主仍需提供自己的运行资源。

### 必须安装 Apixly Media 吗？

不必。组合后的提示词可以交给合适的生成工具。只有可选的图片、视频联动流程才需要 Apixly Media；其账号凭据和 API 费用独立，采用前请查看[当前价格](https://platform.apixly.ai/models)。

### 关闭控制或输入无效设置会怎样？

所有组默认关闭，逐字保留原提示词。无效设置输出失败包，组合节点与示例在媒体提交前停止；仅在 `success` 为真时连接生成。

### 相机和打光控件是否进行物理模拟？

不是。这些控件描述期望的视觉观感，生成图片如何遵循它们取决于所选模型。本工具只输出文本与结构化设置。

### 示例依赖哪个版本？

链接的 DSL 当前固定已批准的 Creative Controls **0.1.0**，以及必要时的 Media **0.2.0**，使用官方签名校验值。源码文档更新不改变这些包身份，也不要求创建新 Key。

## 验证与隐私

Community 1.17.1 原生验收覆盖五个免费工具与媒体插件共存、合计 12 份工作流导入、53 个编辑器面板的参数与绑定保存，以及真实工作流引擎中的七项受控输入用例。本地发布的免费预览已在桌面和 375px 视口实际运行，未发起推理。[QA 范围与宿主限制](https://github.com/apixly-ai/dify-apixly-creative/blob/apixly/docs/QA.md) · [截图来源与校验值](https://github.com/apixly-ai/dify-apixly-creative/blob/apixly/docs/assets/provenance.json)。

编译器不访问外部 API，不增加独立存储或遥测；Dify 宿主可能按工作区设置保存输入和输出。详见[隐私说明](../PRIVACY.md)。Cloud 兼容性未验证。可选账号连接媒体工作流有独立的[文件交付与保留期验收](https://github.com/apixly-ai/dify-apixly/blob/apixly/docs/QA.md)；本编译器仍无需账号或生成调用。

[官网](https://apixly.ai/) · [控制台](https://platform.apixly.ai/) · [媒体 API Key](https://platform.apixly.ai/keys) · [模型与价格](https://platform.apixly.ai/models) · [API 文档](https://apixly.ai/docs) · [English](../README.md)。支持：support@apixly.ai。
