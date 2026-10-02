"""
Tests voor Begroeting en main.

Auteur:   Erik Borgers
Licentie: MIT - open source; zie https://opensource.org/license/mit
"""

from __future__ import annotations

import tomllib
from pathlib import Path

import pytest

import hello_claude_world
from hello_claude_world import VENSTERTITEL, Begroeting, __version__, main


def test_standaard_afzender_is_claude() -> None:
    assert Begroeting().tekst() == "Hello world from Claude"


def test_andere_afzender() -> None:
    assert Begroeting("Erik").tekst() == "Hello world from Erik"


def test_main_toont_begroeting(monkeypatch: pytest.MonkeyPatch) -> None:
    getoond: list[tuple[str, str]] = []
    monkeypatch.setattr(
        hello_claude_world, "toon_venster", lambda titel, tekst: getoond.append((titel, tekst))
    )
    main()
    assert getoond == [(VENSTERTITEL, "Hello world from Claude")]


def test_versie_komt_uit_pyproject() -> None:
    pyproject = Path(__file__).parents[1] / "pyproject.toml"
    verwacht = tomllib.loads(pyproject.read_text(encoding="utf-8"))["project"]["version"]
    assert __version__ == verwacht
