from __future__ import annotations

from pathlib import Path

import pytest

from taag import list_fonts, render


def test_fonts_and_ansi_shadow_render() -> None:
    assert "ANSI Shadow" in list_fonts()
    assert "██╔" in render("A", "ANSI Shadow")


def test_unknown_font_has_available_choices() -> None:
    with pytest.raises(ValueError, match="unknown font"):
        render("A", "not-a-font")


def test_empty_text_is_rejected() -> None:
    with pytest.raises(ValueError, match="must not be empty"):
        render("  ")


def test_custom_figlet_font(tmp_path: Path) -> None:
    font = Path(__file__).parents[1] / "src" / "taag" / "fonts" / "ANSI Shadow.flf"
    custom = tmp_path / "custom.flf"
    custom.write_bytes(font.read_bytes())
    assert "██╔" in render("A", font_file=custom)


def test_rainbow_uses_ansi_color() -> None:
    assert "\x1b[38;5;" in render("A", color=True)
