# TAAG

TAAG is a Python library and Typer command line for rendering text with bundled FIGlet fonts. It is inspired by Patrick Gillespie's [figlet.js](https://github.com/patorjk/figlet.js), which powers the [TAAG generator](https://patorjk.com/software/taag/). The bundled font files retain their original author and license notices.

## Install

```sh
uv tool install --from . taag
```

Run this command from a checkout of this repository.

## Use

```sh
taag -h
taag render "Hello" --font "ANSI Shadow"
taag render "Hello" -f Isometric1 --color
taag fonts
taag render "Hello" --font-file ./custom.flf
```

`taag render` supports bundled FIGlet fonts and caller-supplied `.flf` files. `--color` adds rainbow ANSI color. `taag fonts` lists the bundled font names. The default font is `Standard`.

## Python

```python
from taag import list_fonts, render

print(list_fonts())
print(render("Hello", "ANSI Shadow"))
```

## Development

```sh
uv sync --all-extras
uv run pytest -q
uv run taag render imail --font "ANSI Shadow"
```

The library and CLI are MIT licensed. The bundled FIGlet fonts retain their upstream licenses and attribution in each font file and [`FONT-LICENSE.txt`](FONT-LICENSE.txt).
