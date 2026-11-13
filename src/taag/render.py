"""FIGlet rendering helpers backed by the bundled font files."""

from __future__ import annotations

from importlib.resources import as_file, files
from importlib.resources.abc import Traversable
from pathlib import Path

from pyfiglet import Figlet
from pyfiglet import FontNotFound

DEFAULT_FONT = "Standard"
_FONT_DIR = files("taag").joinpath("fonts")


def list_fonts() -> list[str]:
    """Return bundled FIGlet font names in alphabetical order."""
    return sorted(
        (item.name[:-4] for item in _FONT_DIR.iterdir() if item.name.endswith(".flf")),
        key=str.casefold,
    )


def _bundled_font(name: str) -> Traversable:
    match = next((font for font in list_fonts() if font.casefold() == name.casefold()), None)
    if match is None:
        available = ", ".join(list_fonts())
        raise ValueError(f"unknown font {name!r}; choose from: {available}")
    return _FONT_DIR.joinpath(f"{match}.flf")


def render(
    text: str,
    font: str = DEFAULT_FONT,
    *,
    font_file: str | Path | None = None,
    color: bool = False,
) -> str:
    """Render text using a bundled font or a caller-supplied FIGlet `.flf` file."""
    if not text or not text.strip():
        raise ValueError("text must not be empty")

    path: Path | Traversable = Path(font_file).expanduser() if font_file else _bundled_font(font)
    if font_file:
        if path.suffix.casefold() != ".flf":
            raise ValueError("custom fonts must be FIGlet .flf files")
        if not path.is_file():
            raise ValueError(f"font file not found: {path}")

    try:
        with as_file(path) as font_path:
            art = Figlet(font=str(font_path.with_suffix(""))).renderText(text).rstrip("\n")
    except FontNotFound as exc:
        raise ValueError(f"could not load FIGlet font: {path}") from exc
    return _rainbow(art) if color else art


def _rainbow(art: str) -> str:
    colors = (196, 202, 208, 214, 220, 226, 190, 154, 118, 82, 46, 51, 45, 39, 33, 27, 93, 129, 165, 201)
    output: list[str] = []
    color_index = 0
    for char in art:
        if char.isspace():
            output.append(char)
        else:
            color = colors[color_index % len(colors)]
            output.append(f"\033[38;5;{color}m{char}\033[0m")
            color_index += 1
    return "".join(output)
