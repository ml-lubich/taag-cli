from __future__ import annotations

from typer.testing import CliRunner

from taag.cli import app

runner = CliRunner()


def test_root_and_leaf_help() -> None:
    for args in (["-h"], ["--help"], ["render", "-h"], ["fonts", "--help"]):
        result = runner.invoke(app, args)
        assert result.exit_code == 0, result.output


def test_render_command() -> None:
    result = runner.invoke(app, ["render", "A", "--font", "ANSI Shadow"])
    assert result.exit_code == 0
    assert "██" in result.output


def test_fonts_command() -> None:
    result = runner.invoke(app, ["fonts"])
    assert result.exit_code == 0
    assert "ANSI Shadow" in result.output


def test_invalid_font_is_clean_error() -> None:
    result = runner.invoke(app, ["render", "A", "--font", "nope"])
    assert result.exit_code == 1
    assert "error:" in result.output
