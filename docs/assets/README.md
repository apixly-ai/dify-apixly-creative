# Presentation assets

The cover is an explicitly illustrative diagram adapted from the official Apixly brand and existing Dify cover. It is not a screenshot. Camera, Zap and Aperture symbols reuse the Lucide family used by Apixly Studio; its license is included.

Four PNGs are byte-for-byte native Camofox captures from official Dify Community 1.17.1 / plugin daemon 0.6.10-local and the five-tool Creative Controls candidate:

- `studio-workflow-desktop.png`: actual three-card → Compose → success/error workflow, with the formal defaults off.
- `lighting-swatches-desktop.png`: actual small Lighting dropdown and eight decoded inline Studio gradient icons.
- `free-preview-desktop.png`: actual published local running page after a free Run, with the demo explicitly labeled all controls ON.
- `free-preview-mobile.png`: actual 375×900 result sheet after another free Run; only the final prompt is shown.

No capture was cropped, composited, redrawn or retouched. Browser rendering size in Markdown does not alter the PNG bytes. The prompt was composed inside Dify without a Key, account authorization or generation call. The [QA note](../QA.md) separates real installed-host behavior from controlled test inputs and records the native 32px Run button, desktop-oriented editor and viewport-only qualification limits.

No customer upload, credential, signed content link, private task/request ID or billing receipt is included. SHA256 values and public source descriptions are in `provenance.json`. Files under `docs/**` are repository assets excluded from `.difypkg`; README references use absolute public raw PNG URLs. Publishing the source assets is a release-owner step before distributing a newly documented package.
