# hello-claude-world

Testproject om de Python-werkplek te controleren: uv, VS Code, pytest, GitHub en Claude Code.
Het programma print `Hello world from Claude`.

## Starten

| Waar | Hoe |
|---|---|
| PowerShell of Claude Code | `uv run hello-claude-world` |
| VS Code | F5 (startconfiguratie "Hello Claude World") |
| Zonder uv | `python -m venv .venv`, `.venv\Scripts\pip install -e .`, `python -m hello_claude_world` |

## Testen

```powershell
uv run pytest
uv run ruff check
```

## Licentie

Donateware: vrij te gebruiken en te verspreiden; een donatie wordt gewaardeerd.

Auteur: Erik Borgers
