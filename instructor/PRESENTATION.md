# Build the branded companion

**Current learner deck:** [September 8 PowerPoint, 44 slides](../slides/Warner-CopilotStudio-Agents-2026-09-08.pptx).
Tim approved including this specific deck in Git for learner sharing on September 7. The supplied
template and private builds remain ignored. The existing deck was copied byte-for-byte from the
private build; this move did not revise or visually revalidate its contents.

The current [Python builder](build-deck.py) uses the repo-root O'Reilly template and writes to the
learner deck path above. The artifact-tool builder described below is an alternative build route.

The [manuscript](teaching-slides.json) and [builder](build-presentation.mjs) generate a 35-slide companion from the user-supplied O’Reilly PowerPoint template. Use the bundled presentation runtime, set PRESENTATION_SKILL_DIR, ARTIFACT_RUNTIME_PYTHON, and RUNTIME_NODE_MODULES, then supply the template path, task workspace, and a new revision name. The builder requires @oai/artifact-tool in its Node module resolution path.

The binary template and alternative PowerPoint outputs stay outside Git. Source layouts, theme, fonts, and brand artwork are reused. The alternative builder writes individual PNG previews and private validation records under work/. Its output goes to outputs/. Inspect every slide before delivery.

See the [coverage map](../docs/presentation-coverage.md) and [run of show](run-of-show.md). The instructor performs the demonstrations; all scheduled learner activities work without tenant access.
