"""Typer command line for TAAG."""

from __future__ import annotations

import typer
from rich.console import Console
from rich.table import Table
from typer.core import TyperCommand, TyperGroup

from taag import DEFAULT_FONT, __version__, list_fonts, render

WORDMARK = """████████╗ █████╗  █████╗  ██████╗
╚══██╔══╝██╔══██╗██╔══██╗██╔════╝
   ██║   ███████║███████║██║  ███╗
   ██║   ██╔══██║██╔══██║██║   ██║
   ██║   ██║  ██║██║  ██║╚██████╔╝
   ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝"""


class CleanHelpCommand(TyperCommand):
    def get_help_option(self, ctx: typer.Context):
        option = super().get_help_option(ctx)
        if option is not None:
            option.metavar = ""
        return option

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.command_class = CleanHelpCommand


class CleanHelpGroup(TyperGroup):
    def get_help_option(self, ctx: typer.Context):
        option = super().get_help_option(ctx)
        if option is not None:
            option.metavar = ""
        return option


app = typer.Typer(
    name="taag",
    help=f"```\n{WORDMARK}\n```\n\nRender text as FIGlet ASCII art.",
    no_args_is_help=True,
    add_completion=False,
    cls=CleanHelpGroup,
    invoke_without_command=True,
    rich_markup_mode="markdown",
    context_settings={"help_option_names": ["-h", "--help"]},
)
console = Console()
error_console = Console(stderr=True)


@app.callback()
def root_options(
    ctx: typer.Context,
    version: bool = typer.Option(
        False,
        "--version",
        "-V",
        is_eager=True,
        metavar="",
        show_default=False,
        help="Show the installed version.",
    ),
) -> None:
    if version:
        typer.echo(f"taag {__version__}")
        raise typer.Exit()
    if ctx.invoked_subcommand is None:
        typer.echo(ctx.get_help())
        raise typer.Exit()


@app.command("render", cls=CleanHelpCommand)
def render_command(
    text: str = typer.Argument(..., help="Text to render."),
    font: str = typer.Option(DEFAULT_FONT, "--font", "-f", help="Bundled FIGlet font."),
    font_file: str = typer.Option("", "--font-file", help="Path to a custom FIGlet .flf font."),
    color: bool = typer.Option(
        False,
        "--color",
        "-c",
        metavar="",
        show_default=False,
        help="Color the art with a rainbow.",
    ),
) -> None:
    """Render text using a bundled or custom FIGlet font."""
    try:
        typer.echo(render(text, font, font_file=font_file or None, color=color))
    except ValueError as exc:
        error_console.print(f"[red]error:[/red] {exc}")
        raise typer.Exit(code=1) from exc


@app.command("fonts", cls=CleanHelpCommand)
def fonts_command() -> None:
    """List bundled FIGlet fonts."""
    table = Table(title="Bundled FIGlet Fonts", title_justify="left", box=None, pad_edge=False)
    table.add_column("#", style="dim", justify="right")
    table.add_column("Font", style="cyan")
    for index, font in enumerate(list_fonts(), start=1):
        table.add_row(str(index), font)
    console.print(table)


def main() -> None:
    app()


if __name__ == "__main__":
    main()
