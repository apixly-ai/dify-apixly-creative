# Community verification

Observed on 2026-10-23 using official Dify Community **1.17.1**, plugin daemon **0.6.10-local**, and SDK **0.10.2**. The local QA host used unmodified official images. These results establish the tested self-hosted path; they do not establish Dify Cloud compatibility or Marketplace approval.

## Tested scope

| Check | Observed result |
| --- | --- |
| Independent free installation | All five Creative Controls tools discovered; no media plugin, account or credential needed for the first preview |
| Two-package installation | Five free tools and five Apixly Media/catalog tools coexisted, with one provider per package |
| Combined example library | All 12 formal workflow DSLs imported successfully |
| Native editor persistence | All 53 tool panels in those workflows opened in Camofox; each snapshot matched the intended app/node, and saved original parameter types/values and variable bindings matched the imported graph |
| All controls off | Whitespace, newlines and a non-BMP character in the base prompt were preserved exactly; success End exposed only `final_prompt` |
| Native selector reset | Canon K35 was selected, then cleared to Unspecified in the actual Lens dropdown; the saved UI sentinel became an empty canonical lens, without adding a lens phrase |
| Native lighting swatches | All eight original inline Studio icons decoded at 24×24 in the new Lighting dropdown |
| Local Publish and running page | Actual native Publish and Run actions succeeded; stored inputs and final prompts matched the canonical compiler on desktop and at 375px |
| Credential and inference boundary | Both providers' saved credential lists were empty after the phase; no OAuth flow or media inference was submitted |

The free tools are **Viewpoint**, **Lighting**, **Camera & Lens**, **Compose prompt**, and the retained **Preview creative prompt · free** compatibility tool. The 12 workflows and 53 editor panels describe the combined free/media example library, not 12 free-only workflows or successful media generations.

## Controlled inputs in the real host

Seven additional local QA graph copies exercised the actual installed plugin and workflow engine. Inputs were deliberately selected for each case; the plugin runtime was not replaced by a mock:

1. Three enabled groups produced the byte-exact canonical generate prompt.
2. Edit mode produced the canonical prompt with the preservation guard applied once.
3. Explicit lighting coordinates `0 / 0` stayed numeric in the settings packet and matched canonical neutral-direction behavior.
4. Enabled coordinate mode with both coordinates blank produced a safe error End.
5. Enabled black lighting in the Studio image workflow produced a failed settings packet, then an error End; its media nodes were never executed.
6. Malformed settings JSON stopped at the error End.
7. A forged success packet with invalid settings was revalidated and stopped at the error End.

Errors named a safe field path without echoing the invalid value. A failed control could not be interpreted as an unconnected, disabled control. Adapter unit tests separately cover all five optional selector mappings; the native reset interaction specifically used Lens.

One early private QA run omitted the image workflow's required model form input and stopped before any node. A later run with complete inputs demonstrated the guard. An early readback window also elapsed before a native selector autosave; a later readback confirmed the selection without selecting it again. These were retained as QA observations; neither involved a model submission or a paid retry.

## Screenshots and platform limits

The README PNGs are unchanged captures from this five-tool candidate. The editor overview uses the formal defaults, with groups off. The published result demo is explicitly titled **all controls ON** and uses the three small cards and Compose. It displays only the final prompt, rather than internal settings/debug JSON. [Asset provenance](assets/provenance.json) records file hashes and sources.

The native running page fits a **375×900** viewport without horizontal overflow. Dify presents its mobile result in a bottom sheet. Its native Run button is 32px high, and the workflow editor remains desktop-oriented at that width. The plugin does not modify Dify's shell or widgets. These checks used a headless Firefox/Camofox viewport with humanization enabled; they do not establish iOS Safari, touch-event or soft-keyboard behavior.

Optional account-connected media workflows are documented separately in [Apixly Media QA](https://github.com/apixly-ai/dify-apixly/blob/apixly/docs/QA.md). Real image generation, single-reference camera-look editing and text-video files were delivered through that plugin using the outputs of these controls. Creative Controls itself still needs no account or API call; a free prompt preview alone does not establish a media result.

## Source and reproducibility

The tested runtime came from [source 8992436](https://github.com/apixly-ai/dify-apixly-creative/commit/89924367ec8edca0e03aee45a56c85cca4e1e8d9). Subsequent changes in this documentation batch affect only READMEs, QA notes and presentation images. The frozen compiler SHA256 is `f6ae30104545eb02bda94071dfaf2c37b732facf83926ffeb532f7d1fb12587c`.

The complete serial suites passed 29 companion tests and 107 media tests; Ruff lint, formatting and diff checks passed for both repositories before the native phase. The shared compiler fixtures include 169 valid and 24 invalid cases, with 1,000 source-language differential cases. These unit/differential checks complement the bounded native observations above.

Install the development requirements in a Python 3.12 virtual environment, then run:

```sh
.venv/bin/python -m unittest discover -s tests -v
```

The independent free-only qualification phase ended with its owned tab and Docker project stopped, the external port released and credentials read back empty. The later account/media phase used its own controlled connections. Local fixture app IDs and detailed receipts remain private for targeted cleanup. No customer content, key, signed media URL, private job/request ID or billing receipt is included in these assets. Files under `docs/**` stay outside `.difypkg`; public README images use absolute raw PNG URLs.

## Final distribution provenance

A final documentation-only package retains every Python, YAML, dependency and icon byte from the installed five-tool runtime. The final package is installed alongside Media, the twelve current DSLs and their 53 original tool-parameter bindings are read back, and a free native workflow sanity run returns the canonical prompt without inference. Media-package read-only task checks have their own result and retention scope. Release notes distinguish the paid-tested candidate from the final documentation package.
