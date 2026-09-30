# hello-claude-world

Testproject voor de Python-werkplek. Print `Hello world from Claude`.
De algemene werkafspraken staan in `C:\Users\erikb\Source\CLAUDE.md`; hier alleen wat specifiek is voor dit project.

## Commando's

- Omgeving bijwerken: `uv sync`
- Programma draaien: `uv run hello-claude-world`
- Tests: `uv run pytest`
- Lint en format: `uv run ruff check` en `uv run ruff format`
- Typecontrole: `uv run pyright`

## Structuur

- `src/hello_claude_world/begroeting.py` - class `Begroeting`, levert de tekst
- `src/hello_claude_world/__init__.py` - `main()`, het startpunt (ook `[project.scripts]`)
- `src/hello_claude_world/__main__.py` - maakt `python -m hello_claude_world` en F5 in VS Code mogelijk
- `tests/` - pytest-tests

## Projectregels

- Python-versie staat in `.python-version` (3.13); wijzig die niet zonder te overleggen.
- Dependencies alleen via `uv add` (runtime) of `uv add --dev` (ontwikkeling); nooit met pip in de `.venv`.
- Na elke codewijziging: `uv run pytest`, `uv run ruff check` en `uv run pyright` moeten slagen.

## Planning en afwijkingen

- Bord: GitHub Project `hello-claude-world` (kanban), gekoppeld aan repo `borgershj/hello-claude-world`.
- Openstaande afwijkingen staan als `# TODO(afwijking): ...` in de code; ik bekijk ze in Better Todo Tree.
- Bekende afwijking: de headers vermelden nog Donateware in plaats van een open source statement.
