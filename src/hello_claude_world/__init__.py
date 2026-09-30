"""
hello_claude_world - testproject voor de Python-werkplek.

Auteur:   Erik Borgers
Versie:   0.1.0
Licentie: Donateware - vrij te gebruiken en te verspreiden; een donatie wordt gewaardeerd.
"""
# TODO(afwijking): header met open source statement - licentie is nog Donateware

from __future__ import annotations

from hello_claude_world.begroeting import Begroeting

__version__ = "0.1.0"
__all__ = ["Begroeting", "main"]


def main() -> None:
    """Startpunt voor `uv run hello-claude-world` en `python -m hello_claude_world`."""
    print(Begroeting().tekst())
