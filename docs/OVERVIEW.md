# TAAG overview

TAAG is a Python package and Typer CLI for FIGlet text art. It ships nine bundled `.flf` fonts, lists them, renders text, accepts caller-provided `.flf` fonts, and can color output with rainbow ANSI escapes.

The project is inspired by Patrick Gillespie's [figlet.js](https://github.com/patorjk/figlet.js), which powers the [TAAG generator](https://patorjk.com/software/taag/). Bundled font files retain their upstream attribution and license notices.

## Interfaces

- CLI: `taag render TEXT` renders; `taag fonts` lists bundled fonts.
- Python: `taag.render(text, font="Standard", font_file=None, color=False)` and `taag.list_fonts()`.
- Installation: `uv tool install --force --from ~/dev/taag taag`.

GitHub Actions runs the Python test suite, a CLI rendering smoke check, and `uv build` on pushes and pull requests. Pushing a `v*` tag runs the same gates and attaches the built wheel and source archive to a GitHub Release.
