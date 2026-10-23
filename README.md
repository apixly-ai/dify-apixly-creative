<p align="center">
  <img src="https://raw.githubusercontent.com/apixly-ai/dify-apixly-creative/apixly/docs/assets/cover.png" alt="Apixly Creative Controls for Dify: viewpoint, lighting and camera-look prompt preview" width="1200" />
</p>

# Apixly Creative Controls for Dify

Preview angle, lighting and camera-look instructions inside Dify's plugin runtime. This companion plugin needs no Apixly account or API key and makes no generation request. Dify workspace/runtime costs are controlled by your operator.

**Enable a group → choose its preset or values → preview `final_prompt` → connect a generation tool only when ready.** All three groups default off. When no instruction is added, the original prompt is preserved exactly. Edit mode asks the model to retain subject and scene details not requested to change. These are AI creative instructions, rather than physical camera or light simulation.

## Start with four small Studio nodes

1. Add **Viewpoint**, **Lighting**, and **Camera & Lens**. Each card has only its own controls; all groups default off.
2. Enable the groups you want. Lighting has an explicit **Named direction / Coordinates** mode; blank coordinates never become zero automatically.
3. Connect each card's **settings** output to its matching input on **Compose prompt**, and connect your base prompt. Use **Edit** mode when preserving an existing subject.
4. Run the free preview and inspect `final_prompt`. Connect a separate Generate/Edit tool only after `success` is true.

Dify supplies the native card shell and parameter widgets. Short camera/lens labels and eight inline lighting swatches reuse Apixly Studio's existing controls. The original **Preview creative prompt · free** tool remains available for older workflows.

Invalid controls return `success: false`, an `error_path` and a safe message. Keep any later paid node behind a success check. Numbers stay typed; no automatic model replacement or paid retry is introduced.

## See the prompt before generating

<img src="https://raw.githubusercontent.com/apixly-ai/dify-apixly-creative/apixly/docs/assets/free-preview-desktop.png" alt="Actual native Dify keyless preview: viewpoint, golden-hour lighting and Helios lens instructions" width="1200" />

This is an actual Dify Community 1.17.1 result from a deliberately enabled demo. The published running page also works at a [375px viewport](https://raw.githubusercontent.com/apixly-ai/dify-apixly-creative/apixly/docs/assets/free-preview-mobile.png). The workflow editor remains desktop-oriented. No model was called for this preview. [Asset sources and hashes](docs/assets/provenance.json).

## Optional media generation

Install [Apixly Media](https://github.com/apixly-ai/dify-apixly) separately to generate/edit images or create videos. That provider keeps its own media credential, using a manual secret API key or an authorized Apixly account connection. The creative preview workflow depends only on this free companion; creative image/edit/video workflows depend on both exact plugin packages. The tested Dify daemon retained one tool provider per plugin, so two independent packages preserve free preview and the media provider's credential boundary.

[Website](https://apixly.ai/) · [API console](https://platform.apixly.ai/) · [Create a key for media generation](https://platform.apixly.ai/keys) · [Models and prices](https://platform.apixly.ai/models) · [API documentation](https://apixly.ai/docs) · [Chinese documentation](readme/README_zh_Hans.md) · [Support](mailto:support@apixly.ai).

## Ready to import

| Workflow | Required plugins | Result |
| --- | --- | --- |
| [Free prompt preview](https://github.com/apixly-ai/dify-apixly/blob/apixly/examples/apixly-studio-preview-workflow.yml) | Creative Controls only | Prompt or a safe validation message; no generation |
| [Creative image](https://github.com/apixly-ai/dify-apixly/blob/apixly/examples/apixly-studio-image-workflow.yml) | Creative Controls + Apixly Media | One image task and files |
| [Creative reference edit](https://github.com/apixly-ai/dify-apixly/blob/apixly/examples/apixly-studio-edit-workflow.yml) | Creative Controls + Apixly Media | One reference-edit task and files |
| [Creative video](https://github.com/apixly-ai/dify-apixly/blob/apixly/examples/apixly-studio-video-workflow.yml) | Creative Controls + Apixly Media | One video task and files |

The four Studio workflows are recommended for new projects. The original eight media/creative workflows remain available for compatibility. Install the exact packages referenced by the downloaded workflow. All example control groups remain off until you explicitly enable them. Lighting presets reuse Apixly Studio's existing gradient swatches; camera and lens labels use the same familiar short names. Dify provides the native node shell and parameter widgets.

## Development

Python 3.12, `dify-plugin==0.10.2`. Install `requirements-dev.txt`, then run `.venv/bin/python -m unittest discover -s tests -v`. The canonical standard-library compiler follows Creative Controls contract 1.0.0 and is copied byte-for-byte across Python integrations. Shared fixtures cover 169 valid and 24 invalid cases, with additional Unicode and JavaScript-compatibility tests.

Creative compilation calls no external API and adds no independent telemetry or storage. Dify may retain workflow inputs and outputs according to workspace settings. Read [PRIVACY.md](PRIVACY.md). Cloud compatibility and Marketplace approval remain separate checks.
