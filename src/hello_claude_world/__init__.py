"""
hello_claude_world - testproject voor de Python-werkplek.

Auteur:   Erik Borgers
Versie:   0.1.0
Licentie: MIT - open source; zie https://opensource.org/license/mit
"""
# TODO(afwijking): geen versie in header - bevat nog Versie: 0.1.0

from __future__ import annotations

from importlib.metadata import version

from hello_claude_world.begroeting import Begroeting

__version__ = version("hello-claude-world")
__all__ = ["Begroeting", "main"]


def main() -> None:
    """Startpunt voor `uv run hello-claude-world` en `python -m hello_claude_world`."""
    print(Begroeting().tekst())
