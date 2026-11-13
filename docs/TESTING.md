# Testing

Run the Python package and CLI checks from the repository root:

```sh
uv sync --all-extras
uv run pytest -q
uv run taag -h
uv run taag fonts
uv run taag render Hello --font "ANSI Shadow"
uv build
```

Tests cover bundled-font rendering, custom FIGlet font files, missing/empty input, rainbow output, and recursive help for the root and leaf commands.

GitHub Actions runs the same test and CLI smoke checks on pushes, pull requests, and manual dispatch. It also builds both wheel and source distributions with `uv build`.
