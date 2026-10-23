<p align="center">
  <img src="https://raw.githubusercontent.com/apixly-ai/dify-apixly-creative/apixly/docs/assets/cover.png" alt="Apixly Dify 创作指令：视角、打光、相机镜头观感免费预览" width="1200" />
</p>

# Apixly 创作指令：Dify 免费预览工具

五个免费工具，组合视角、打光与相机镜头观感提示词。**无需 Apixly 账号或 API Key，不调用模型**，在 Dify 插件运行环境中预览；Dify 自身资源费用由宿主管理。

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

## 验证与隐私

Community 1.17.1 原生验收覆盖五个免费工具与媒体插件共存、合计 12 份工作流导入、53 个编辑器面板的参数与绑定保存，以及真实工作流引擎中的七项受控输入用例。本地发布的免费预览已在桌面和 375px 视口实际运行，未发起推理。[QA 范围与宿主限制](https://github.com/apixly-ai/dify-apixly-creative/blob/apixly/docs/QA.md) · [截图来源与校验值](https://github.com/apixly-ai/dify-apixly-creative/blob/apixly/docs/assets/provenance.json)。

编译器不访问外部 API，不增加独立存储或遥测；Dify 宿主可能按工作区设置保存输入和输出。详见[隐私说明](../PRIVACY.md)。Cloud 兼容性未验证。可选账号连接媒体工作流有独立的[文件交付与保留期验收](https://github.com/apixly-ai/dify-apixly/blob/apixly/docs/QA.md)；本编译器仍无需账号或生成调用。

[官网](https://apixly.ai/) · [控制台](https://platform.apixly.ai/) · [媒体 API Key](https://platform.apixly.ai/keys) · [模型与价格](https://platform.apixly.ai/models) · [API 文档](https://apixly.ai/docs) · [English](../README.md)。支持：support@apixly.ai。
