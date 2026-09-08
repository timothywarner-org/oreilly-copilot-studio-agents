# Contoso AI Fundamentals Coach icons

**Requirements verified September 7, 2026 against Microsoft Learn.**

## Upload-ready files

| File | Use | Verified export |
| --- | --- | --- |
| [agent-icon.png](agent-icon.png) | Copilot Studio agent avatar | 192 x 192 PNG, 11,684 bytes |
| [color.png](color.png) | Shared Teams and Microsoft 365 listing icon | 192 x 192 PNG, 11,684 bytes; opaque square background |
| [outline.png](outline.png) | Teams app bar / required app-package outline | 32 x 32 PNG, 1,156 bytes; white artwork with real alpha transparency |

![Color icon and enlarged outline preview](preview.png)

**Preview only:** The outline is enlarged six times on navy for inspection. Its actual file is 32 x 32
and transparent; the preview background is not embedded in it. The avatar and color file are identical.

## Verification performed

- Pixel dimensions, PNG format, and file sizes checked from the saved files.
- The full color canvas is opaque. Every pixel outside the central 120 x 120 area is exactly navy
  `#10243A`; the symbol bounds are x=38-153, y=44-147.
- The outline contains 438 fully transparent pixels. Every visible pixel has white RGB values;
  antialiasing uses alpha. It fills the width, with only the space needed to preserve its aspect ratio.
- The three network nodes and the open book remain recognizable at the 32-pixel size. Files were
  visually inspected after export.
- Solid-color contrast is **15.72:1** for white against navy and **8.64:1** for amber against navy.
  These measure the solid palette colors, not partially transparent edge pixels.
- File hashes and measured bounds are in [validation.json](validation.json).

The artwork was created with the built-in **ImageGen** tool. The user authorized **ImageMagick** for
exact-size exports, flat-color normalization, and real transparency after two generated outline
attempts produced painted checkerboards. [Export-Icons.ps1](Export-Icons.ps1) reproduces the final PNGs
from the preserved color master. The failed outline attempts are not shipped.

## Requirements by destination

| Destination | Required asset | Size and appearance | Source |
| --- | --- | --- | --- |
| Copilot Studio, standard harness | Agent avatar PNG | Maximum 192 x 192 pixels; less than 72 KB | [Create and delete agents](https://learn.microsoft.com/en-us/microsoft-copilot-studio/authoring-first-bot#edit-your-agents-basic-features) |
| Teams and Microsoft 365 store listings | Color PNG | Exactly 192 x 192; square, full-bleed background; symbol within the central 120 x 120 safe area; no baked-in rounded corners or border | [Design icons](https://learn.microsoft.com/en-us/microsoft-365/copilot/extensibility/agent-icon-management) |
| Teams app bar and Microsoft 365 app package | Outline PNG | Exactly 32 x 32; white symbol with transparent background; no added padding around the symbol | [App package icon requirements](https://learn.microsoft.com/en-us/microsoft-365/copilot/extensibility/agents-are-apps#app-icons) |

The same color icon serves the Teams and Microsoft 365 listings. There is no separate third store
logo required for this shared app package. The outline icon remains required for package validation
even where the Microsoft 365 Copilot interface only displays the color icon.

For this palette, use **`#10243A`** as the app's accent/background color where that setting is requested.

The new Copilot Studio experience separately documents a PNG limit of **100 KB or less**. This kit
targets the stricter standard-harness limit used by the live-build scaffold. See
[new-experience instructions](https://learn.microsoft.com/en-us/microsoft-copilot-studio/agents-experience/authoring-instructions).

## Design

One open book and three connected AI nodes represent the same agent across destinations. The palette
is navy, white, and amber. The shape carries the identity in grayscale; no meaning depends on color
alone. There is no official Microsoft logo, certification badge, exam number, or reward claim.

The final export uses a flat navy background. The store symbol stays within the central 120-pixel
safe area. The outline retains the same silhouette with transparent holes in the nodes and book.
The original [color master](source/color-master.png) is artwork for editing, not an upload-ready icon.
The [generation prompts](generation-prompts.md) record the built-in tool inputs.

## Where the icons are configured

For the standard-harness agent avatar, Microsoft's documented route is the agent icon in the top
bar, **Change icon**, select the PNG, and **Save**.

For channel listing details, open **Channels > Teams and Microsoft 365 Copilot > Edit details**.
For a downloaded app package, `color.png` and `outline.png` are the files referenced by its existing
manifest. These assets do not constitute an app package; keep the real Copilot Studio-generated
manifest and its actual identifiers.

Microsoft distinguishes channel listing branding from some direct-install avatar paths. Existing
installations or admin-approved listings may require reinstalling or resubmitting updated details.
See [customize the appearance for Teams and Microsoft 365 Copilot](https://learn.microsoft.com/en-us/microsoft-copilot-studio/publication-add-bot-to-microsoft-teams#customize-the-appearance-of-an-agent-for-teams-and-microsoft-365-copilot).

**Tenant evidence, September 7:** The avatar and Teams/Microsoft 365 channel art were configured.
After final publication, all three stored assets matched the approved kit bytes. The native channel
details editor regenerated icon assets when saved, so the approved files were reapplied and checked
after the last listing change. Recheck artwork after editing listing details. Installed appearance,
packaging validation, and store/admin approval remain **NOT RUN**.
