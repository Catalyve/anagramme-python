"""
scoreboard.py — Contient la classe TableauScore.

Cette classe gère le suivi des scores et statistiques de la partie :
- compte le nombre de manches jouées et gagnées,
- attribue des points en cas de réussite,
- applique des pénalités en cas d'échec,
- fournit un résumé de fin de partie.
"""

class TableauScore:
    """Gère le score et les statistiques de la partie."""

    def __init__(self):
        self.points = 0
        self.manches_jouees = 0
        self.manches_gagnees = 0

    def ajouter_succes(self, manche, difficulte=None):
        """Ajoute une manche réussie."""
        self.manches_jouees += 1
        self.manches_gagnees += 1

        coefficient = {"facile": 1, "moyen": 2, "difficile": 3}.get(difficulte, 2)
        points_de_base = len(manche.mot_original) * coefficient
        malus = len(manche.tentatives)

        self.points += max(1, points_de_base - malus)

    def ajouter_echec(self, manche, difficulte=None):
        """Ajoute une manche perdue (malus uniquement en difficile)."""
        self.manches_jouees += 1

        if difficulte == "difficile":
            self.points = max(0, self.points - len(manche.tentatives))

    def ajouter_sous_mot(self, points):
        """Ajoute les points obtenus pour un sous-mot valide."""
        self.points += points

    def resume(self):
        """Renvoie un résumé statistique de la partie."""
        return (
            f"Manches jouées : {self.manches_jouees} | "
            f"Gagnées : {self.manches_gagnees} | "
            f"Score : {self.points}"
        )
