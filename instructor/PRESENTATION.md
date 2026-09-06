# Build the branded companion

The [manuscript](teaching-slides.json) and [builder](build-presentation.mjs) generate a 35-slide companion from the user-supplied O’Reilly PowerPoint template. Use the bundled presentation runtime, set PRESENTATION_SKILL_DIR, ARTIFACT_RUNTIME_PYTHON, and RUNTIME_NODE_MODULES, then supply the template path, task workspace, and a new revision name. The builder requires @oai/artifact-tool in its Node module resolution path.

Binary template and PowerPoint outputs stay outside Git. Source layouts, theme, fonts, and brand artwork are reused. The builder writes individual PNG previews and private validation records under work/. The output goes to outputs/. Inspect every slide before delivery.

See the [coverage map](../docs/presentation-coverage.md) and [run of show](run-of-show.md). The instructor performs the demonstrations; all scheduled learner activities work without tenant access.
