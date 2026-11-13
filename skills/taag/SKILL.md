---
name: taag
description: Create expressive, readable ASCII/ANSI text art for CLI apps, developer tools, terminal output, and software projects. Use when adding a banner, a FIGlet font, or a distinctive text flourish in Python code or a terminal workflow.
license: MIT
---

# TAAG text art for developer tools

Use TAAG to give a CLI, developer tool, project demo, or terminal output a recognizable visual touch. Match the font and size to the context: compact and readable for routine output, bold for a launch or demo, or playful when that suits the tool. Keep large banners out of routine help unless they are part of the product's identity.

Install the Python CLI after its package is published:

```sh
uv tool install taag
```

For a local source checkout, run `uv tool install --from . taag` from the repository root.

Render text, choose a font, list available fonts, or load a custom FIGfont:

```sh
taag render "Hello" --font "ANSI Shadow"
taag render "Hello" --font Isometric1 --color
taag fonts
taag render "Hello" --font-file ./custom.flf
```

Python API:

```python
from taag import list_fonts, render

print(list_fonts())
print(render("Hello", "ANSI Shadow"))
```

TAAG is inspired by Patrick Gillespie's [figlet.js](https://github.com/patorjk/figlet.js), which powers the [TAAG generator](https://patorjk.com/software/taag/). Bundled font files retain their upstream author and license notices. Use custom `.flf` fonts only when you have permission to use them.
