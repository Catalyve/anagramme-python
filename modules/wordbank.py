"""
wordbank.py — Contient la classe BanqueMots.

Cette classe charge et gère la liste des mots utilisés pour
le jeu Anagramme :
- lit les mots depuis un fichier texte,
- fournit un mot aléatoire sans répétition,
- permet de réinitialiser les mots déjà utilisés.
"""

import random

class BanqueMots:
    """Gère la liste des mots utilisables pour le jeu d'anagrammes."""

    def __init__(self, chemin_fichier):
        """Initialise la banque de mots avec un fichier source."""
        self.chemin_fichier = chemin_fichier
        self.liste_mots = []
        self.mots_utilises = set()

    def charger(self):
        """Charge les mots valides depuis le fichier."""
        with open(self.chemin_fichier, "r", encoding="utf-8") as f:
            for ligne in f:
                mot = ligne.strip().lower()
                if 2 <= len(mot) <= 10 and mot.isalpha():
                    self.liste_mots.append(mot)

    def reinitialiser(self):
        """Réinitialise la liste des mots déjà utilisés."""
        self.mots_utilises.clear()

    def mot_aleatoire(self, difficulte=None):
        """
        Renvoie un mot aléatoire non encore utilisé,
        filtré selon la difficulté si nécessaire.
        """
        if len(self.mots_utilises) >= len(self.liste_mots):
            self.reinitialiser()

        if difficulte == "facile":
            candidats = [m for m in self.liste_mots if 4 <= len(m) <= 6]
        elif difficulte == "moyen":
            candidats = [m for m in self.liste_mots if 7 <= len(m) <= 8]
        elif difficulte == "difficile":
            candidats = [m for m in self.liste_mots if 9 <= len(m) <= 10]
        else:
            candidats = self.liste_mots

        mot = random.choice(candidats)
        while mot in self.mots_utilises:
            mot = random.choice(candidats)

        self.mots_utilises.add(mot)
        return mot
