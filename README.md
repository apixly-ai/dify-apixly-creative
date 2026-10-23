<p align="center">
  <img src="https://raw.githubusercontent.com/apixly-ai/dify-apixly-creative/apixly/docs/assets/cover.png" alt="Apixly Creative Controls: viewpoint, lighting and camera-look prompt preview for Dify" width="1200" />
</p>

# Apixly Creative Controls for Dify

Five free tools for viewpoint, lighting and camera-look prompts. Preview inside Dify's plugin runtime with **no Apixly account, API key or model request**. Dify's own runtime costs remain your operator's responsibility.

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

## Verification and privacy

On Community 1.17.1, native checks covered five free tools alongside Apixly Media, 12 combined workflow imports, 53 editor panels with preserved bindings, and seven controlled-input cases in the real workflow engine. The local published preview ran on desktop and at 375px. These checks made no inference call. [QA scope and host limitations](https://github.com/apixly-ai/dify-apixly-creative/blob/apixly/docs/QA.md) · [Screenshot sources and hashes](https://github.com/apixly-ai/dify-apixly-creative/blob/apixly/docs/assets/provenance.json).

Creative compilation adds no external API, independent storage or telemetry. Dify may retain workflow inputs and outputs under workspace settings. Read [PRIVACY.md](PRIVACY.md). Cloud compatibility, live account authorization and new paid media quality are separate checks.

[Website](https://apixly.ai/) · [Console](https://platform.apixly.ai/) · [Media API keys](https://platform.apixly.ai/keys) · [Models and prices](https://platform.apixly.ai/models) · [API docs](https://apixly.ai/docs) · [Chinese docs](readme/README_zh_Hans.md) · [Support](mailto:support@apixly.ai).
