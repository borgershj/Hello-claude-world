"""
hello_claude_world - testproject voor de Python-werkplek.

Auteur:   Erik Borgers
Licentie: MIT - open source; zie https://opensource.org/license/mit
"""

from __future__ import annotations

import tkinter as tk
from importlib.metadata import version
from tkinter import messagebox

from hello_claude_world.begroeting import Begroeting

__version__ = version("hello-claude-world")
__all__ = ["VENSTERTITEL", "Begroeting", "main", "toon_venster"]

# TODO(afwijking): instelbare waarden in JSON - venstertitel en afzender staan voor dit testproject in de code
VENSTERTITEL = "Hello Claude World"


def toon_venster(titel: str, tekst: str) -> None:
    """
    Doel: toon een tekst in een venster met een OK-knop en wacht tot de gebruiker sluit.

    Parameters:
        titel: titel van het venster.
        tekst: tekst in het venster.
    Retourneert: niets.
    Exceptions: tk.TclError als er geen beeldscherm beschikbaar is.
    """
    root = tk.Tk()
    root.withdraw()
    messagebox.showinfo(titel, tekst, parent=root)
    root.destroy()


def main() -> None:
    """
    Doel: startpunt voor `uv run hello-claude-world` en `python -m hello_claude_world`.

    Parameters: geen.
    Retourneert: niets.
    Exceptions: tk.TclError als er geen beeldscherm beschikbaar is.
    """
    toon_venster(VENSTERTITEL, Begroeting().tekst())
