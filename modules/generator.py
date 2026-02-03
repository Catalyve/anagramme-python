"""
generateur.py — Contient la classe GenerateurAnagramme.

Cette classe permet de générer une anagramme à partir d’un mot :
- mélange les lettres de façon aléatoire,
- garantit que le mot mélangé est différent du mot original.
"""

import random


class GenerateurAnagramme:
    """Mélange les lettres d’un mot pour générer une anagramme."""

    @staticmethod
    def melanger(mot):
        """Renvoie une version mélangée du mot donné."""
        lettres = list(mot)
        random.shuffle(lettres)
        anagramme = "".join(lettres)

        while anagramme == mot:
            random.shuffle(lettres)
            anagramme = "".join(lettres)

        return anagramme
