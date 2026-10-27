<p align="center">
  <img src="https://raw.githubusercontent.com/apixly-ai/dify-apixly-creative/apixly/docs/assets/cover.png" alt="Apixly Creative Controls: viewpoint, lighting and camera-look prompt preview for Dify" width="1200" />
</p>

# Apixly Creative Controls for Dify: free prompt tools

Five free tools for viewpoint, lighting and camera-look prompts. Preview inside Dify's plugin runtime with **no Apixly account, API key or model request**. Dify's own runtime costs remain your operator's responsibility.

**[Install the free plugin from Dify Marketplace](https://marketplace.dify.ai/plugin/apixly-ai/apixly_creative)**

**[apixly.ai](https://apixly.ai/)** · **[platform.apixly.ai](https://platform.apixly.ai/)** · [Prices](https://platform.apixly.ai/models) · [API keys](https://platform.apixly.ai/keys) · [API docs](https://apixly.ai/docs)

## About this Apixly integration

**Apixly Creative Controls** (`apixly-ai/apixly_creative`) formats prompts and settings inside Dify. It does not call an AI model or act as an API/model provider. Its output can feed a generation tool you choose.

The separate [Apixly AI API platform](https://apixly.ai/) and [Apixly Media integration](https://github.com/apixly-ai/dify-apixly) are optional. For that path, use the [image API guide](https://apixly.ai/docs/images), [video task guide](https://apixly.ai/docs/video) and [console](https://platform.apixly.ai/). [Platform and pricing context](https://github.com/apixly-ai/dify-apixly/blob/apixly/docs/ABOUT_APIXLY.md) describes the wider service without changing this formatter's credential-free behavior.

## Build your prompt with four small nodes

1. Add **Viewpoint**, **Lighting**, and **Camera & Lens**. Each card contains only its own controls.
2. Enable the groups you need, then choose presets or values. Lighting offers **Named direction / Coordinates**; blank coordinates never become zero automatically.
3. Connect each **settings** output to its matching input on **Compose prompt**, along with your base prompt. Choose **Edit** to request preservation of existing subject and scene details.
4. Run the free preview and read `final_prompt`. Connect a generation tool only when `success` is true.

All groups default **off**. With no added instruction, the base prompt stays exactly unchanged. These are AI creative instructions, rather than a physical camera or light simulation. The original **Preview creative prompt · free** tool remains available for older workflows.

<img src="https://raw.githubusercontent.com/apixly-ai/dify-apixly-creative/apixly/docs/assets/studio-workflow-desktop.png" alt="Actual Dify editor: three compact control cards connect to Compose, a success check and a clean prompt result" width="1200" />

*Actual Community 1.17.1 editor, with controls off. Dify supplies the native cards and widgets.*

## Familiar Studio presets

Short camera/lens labels and eight inline lighting swatches reuse Apixly Studio's existing controls. Optional selectors include **Unspecified**, so a look can be removed again.

<img src="https://raw.githubusercontent.com/apixly-ai/dify-apixly-creative/apixly/docs/assets/lighting-swatches-desktop.png" alt="Actual native Lighting dropdown showing eight original Apixly Studio gradient swatches" width="1000" />

## See the result before generating

This explicitly enabled demo produced the final prompt without a Key or generation call. View the [desktop running page](https://raw.githubusercontent.com/apixly-ai/dify-apixly-creative/apixly/docs/assets/free-preview-desktop.png), or the actual 375px result below.

<p align="center">
  <img src="https://raw.githubusercontent.com/apixly-ai/dify-apixly-creative/apixly/docs/assets/free-preview-mobile.png" alt="Actual 375px Dify running-page result: only the composed prompt, without debug JSON" width="320" />
</p>

## Ready to import

| Workflow | Required plugins | Result |
| --- | --- | --- |
| [Free preview](https://github.com/apixly-ai/dify-apixly/blob/apixly/examples/apixly-studio-preview-workflow.yml) | Creative Controls | Prompt or safe validation message; no generation |
| [Creative image](https://github.com/apixly-ai/dify-apixly/blob/apixly/examples/apixly-studio-image-workflow.yml) | Creative Controls + Apixly Media | One image task and files |
| [Reference edit](https://github.com/apixly-ai/dify-apixly/blob/apixly/examples/apixly-studio-edit-workflow.yml) | Creative Controls + Apixly Media | One reference-edit task and files |
| [Creative video](https://github.com/apixly-ai/dify-apixly/blob/apixly/examples/apixly-studio-video-workflow.yml) | Creative Controls + Apixly Media | One video task and files |

The original eight workflows remain available. Install the exact packages referenced by your downloaded DSL. Invalid controls emit a failed settings packet; Compose stops and the examples route to a safe error before any media node.

Optional generation requires the separate [Apixly Media](https://github.com/apixly-ai/dify-apixly) plugin and its own credential. The plugin is free; API usage is charged to your Apixly account.

## FAQ

### Is an Apixly account or Key required for the free preview?

No. All five formatting tools run without an Apixly account, API key or generation request. Your Dify operator still supplies its own runtime resources.

### Must I install Apixly Media?

No. Use the composed prompt with any suitable generation tool. Apixly Media is needed only for the optional connected image/video workflows; its account credentials and API charges are separate. Check [current prices](https://platform.apixly.ai/models) before that optional step.

### What happens when controls are off or invalid?

All groups default off, preserving the base prompt exactly. Invalid settings produce a failure packet; Compose and the examples stop before a media submission. Connect generation only when `success` is true.

### Are camera and lighting controls a physical simulation?

No. They describe an intended visual look. How a generated image follows those instructions depends on the chosen model. The formatter itself only produces text and structured settings.

### Which package do the examples need?

The linked DSLs currently pin approved Creative Controls **0.1.0** and, where needed, Media **0.2.0** with their official signed checksums. Source documentation changes do not update those package identities or require a new Key.

## Verification and privacy

On Community 1.17.1, native checks covered five free tools alongside Apixly Media, 12 combined workflow imports, 53 editor panels with preserved bindings, and seven controlled-input cases in the real workflow engine. The local published preview ran on desktop and at 375px. These checks made no inference call. [QA scope and host limitations](https://github.com/apixly-ai/dify-apixly-creative/blob/apixly/docs/QA.md) · [Screenshot sources and hashes](https://github.com/apixly-ai/dify-apixly-creative/blob/apixly/docs/assets/provenance.json).

Creative compilation adds no external API, independent storage or telemetry. Dify may retain workflow inputs and outputs under workspace settings. Read [PRIVACY.md](PRIVACY.md). Cloud compatibility is unverified. Optional account-connected media workflows have their own [delivery and retention verification](https://github.com/apixly-ai/dify-apixly/blob/apixly/docs/QA.md); this formatter still requires no account or generation call.

[Website](https://apixly.ai/) · [Console](https://platform.apixly.ai/) · [Media API keys](https://platform.apixly.ai/keys) · [Models and prices](https://platform.apixly.ai/models) · [API docs](https://apixly.ai/docs) · [Chinese docs](readme/README_zh_Hans.md) · [Support](mailto:support@apixly.ai).
