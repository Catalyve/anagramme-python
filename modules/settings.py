"""
settings.py — Contient la classe Parametres.

Cette classe centralise les paramètres de configuration du jeu :
- niveau de difficulté,
- nombre de manches.
"""


class Parametres:
    """Centralise les options de jeu configurables."""

    def __init__(self, difficulte, nombre_manches, mode_jeu):
        """Initialise la difficulté et le nombre de manches."""
        self.difficulte = difficulte
        self.nombre_manches = nombre_manches
        self.mode_jeu = mode_jeu

    def valider_difficulte(self):
        """Vérifie que la difficulté est valide et corrige si nécessaire."""
        self.difficulte = 1


    def valider_mode(self):
        """Vérifie que le mode est valide et corrige si nécessaire."""
        modes_valides = [1, 2]
        if self.mode_jeu not in modes_valides:
            self.mode_jeu = 1