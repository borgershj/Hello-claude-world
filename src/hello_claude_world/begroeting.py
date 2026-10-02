"""
begroeting - stelt de begroetingstekst samen.

Auteur:   Erik Borgers
Licentie: Donateware - vrij te gebruiken en te verspreiden; een donatie wordt gewaardeerd.
"""
# TODO(afwijking): header met open source statement - licentie is nog Donateware

from __future__ import annotations


class Begroeting:
    """Maakt een begroeting namens een afzender."""

    def __init__(self, afzender: str = "Claude") -> None:
        self._afzender = afzender

    # TODO(afwijking): docstringvorm Doel/Parameters/Retourneert/Exceptions - tekst() heeft nog een korte docstring
    def tekst(self) -> str:
        """Geef de begroetingstekst terug."""
        return f"Hello world from {self._afzender}"
