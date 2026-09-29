"""
begroeting - stelt de begroetingstekst samen.

Auteur:   Erik Borgers
Versie:   0.1.0
Licentie: Donateware - vrij te gebruiken en te verspreiden; een donatie wordt gewaardeerd.
"""

from __future__ import annotations


class Begroeting:
    """Maakt een begroeting namens een afzender."""

    def __init__(self, afzender: str = "Claude") -> None:
        self._afzender = afzender

    def tekst(self) -> str:
        """Geef de begroetingstekst terug."""
        return f"Hello world from {self._afzender}"
