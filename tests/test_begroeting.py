"""
Tests voor Begroeting en main.

Auteur:   Erik Borgers
Versie:   0.1.0
Licentie: Donateware - vrij te gebruiken en te verspreiden; een donatie wordt gewaardeerd.
"""
# TODO(afwijking): geen versie in header - bevat nog Versie: 0.1.0
# TODO(afwijking): header met open source statement - licentie is nog Donateware

from __future__ import annotations

import tomllib
from pathlib import Path

import pytest

from hello_claude_world import Begroeting, __version__, main


def test_standaard_afzender_is_claude() -> None:
    assert Begroeting().tekst() == "Hello world from Claude"


def test_andere_afzender() -> None:
    assert Begroeting("Erik").tekst() == "Hello world from Erik"


def test_main_print_begroeting(capsys: pytest.CaptureFixture[str]) -> None:
    main()
    assert capsys.readouterr().out.strip() == "Hello world from Claude"


def test_versie_komt_uit_pyproject() -> None:
    pyproject = Path(__file__).parents[1] / "pyproject.toml"
    verwacht = tomllib.loads(pyproject.read_text(encoding="utf-8"))["project"]["version"]
    assert __version__ == verwacht
