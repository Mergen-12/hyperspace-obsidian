# Hyperspace · an Obsidian theme

Deep space, bone-white text, one electric blue, and stars streaking past behind
the workspace. Square corners, thin borders, a typewriter interface (Share Tech
Mono) and a display face for titles (Orbitron). Dark by default; the light mode
is **Cryo**, ice white and blue.

Ported from the Hyperspace skin of Engram, a vault-map app built on OpenClio.

## What you get

- **Star warp.** A CSS-only starfield behind the workspace that keeps drifting
  outward; the editor panes are slightly translucent so it shows through.
  Freezes under the OS reduced-motion setting, or with a toggle.
- **Split-edge titles.** H1 and the inline note title carry a blue/white
  chromatic edge and, every few seconds, a one-frame jitter.
- **Typewriter chrome.** Tabs, folders, status bar, callout titles, table
  headers, tags and property keys in uppercase mono. `//` before every H3.
- **Hard-offset focus.** Inputs, modals and menus use a solid blue offset
  instead of a soft shadow.
- **JUMP // READY** badge in the status bar.
- Graph view, callouts, code, tables, blockquotes, checkboxes, embeds,
  properties and search all coloured to match.

Fonts are embedded in `theme.css` (both are SIL Open Font License), so the
theme makes no network requests.

## Options (Style Settings plugin)

With the community plugin *Style Settings* installed you can freeze the stars,
set how much the panes cover them, turn off the title effect, hide the badge,
and fall back to your own interface or heading font. Without the plugin every
effect is on.

## Install

Manual: copy `manifest.json` and `theme.css` into
`<your vault>/.obsidian/themes/Hyperspace/`, then pick **Hyperspace** under
Settings → Appearance → Themes.

## Develop

```
python3 build.py        # embeds src/fonts/*.woff2 and src/theme.src.css into theme.css
```

Edit `src/theme.src.css`, never `theme.css`.

## Publish (checklist)

Themes are submitted through the Obsidian community portal, not by pull
request (the old `obsidian-releases` repo no longer accepts them).

1. Push this repo to GitHub as a public repository.
2. Keep `manifest.json`, `README.md`, `LICENSE` and `screenshot.png` in the
   repo root. The portal reads `manifest.json` from the default branch.
3. Create a GitHub release whose tag is exactly the `version` in
   `manifest.json`, and attach `manifest.json` and `theme.css` as release
   assets (not just committed files).
4. Sign in at https://community.obsidian.md with your Obsidian account, link
   GitHub, and use "Add your theme". The portal reviews the entry
   automatically and lists anything to fix under Reviews.
5. To re-run a failed review: fix the repo, bump `version`, rebuild, and
   publish a new release with the new tag. The portal picks it up.

## License

MIT. Orbitron and Share Tech Mono are under the SIL Open Font License 1.1
(see `src/fonts/README.md`).

```
MIT License

Copyright (c) 2026 Mergen

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```
