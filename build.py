#!/usr/bin/env python3
"""Assemble theme.css: the two fonts as base64 @font-face rules, then src/theme.src.css."""
import base64, pathlib
root = pathlib.Path(__file__).parent
fonts = [("Orbitron", "500 700", "orbitron.woff2"), ("Share Tech Mono", "400", "share-tech-mono.woff2")]
out = ["/* Hyperspace for Obsidian. Built by build.py; edit src/theme.src.css, not this file. */\n"]
for family, weight, fname in fonts:
    b64 = base64.b64encode((root / "src" / "fonts" / fname).read_bytes()).decode()
    out.append(f'@font-face{{font-family:"{family}";font-style:normal;font-weight:{weight};font-display:swap;'
               f'src:url(data:font/woff2;base64,{b64}) format("woff2")}}\n')
out.append((root / "src" / "theme.src.css").read_text(encoding="utf-8"))
css = "".join(out)
(root / "theme.css").write_text(css, encoding="utf-8")
print(f"theme.css: {len(css)//1024} KB")
