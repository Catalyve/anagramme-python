"""
round.py — Contient la classe Manche.

Cette classe représente une manche individuelle du jeu Anagramme :
- stocke le mot original et son anagramme,
- garde une trace des tentatives du joueur,
- met à jour l'état de la manche (en cours, gagnée, perdue).
"""


class Manche:
    """Représente une manche du jeu d’anagrammes."""

    def __init__(self, mot, generateur, parametres=None, essais_max=3):
        self.mot_original = mot
        self.mot_melange = generateur.melanger(mot)
        self.tentatives = []
        self.etat = "en cours"
        self.parametres = parametres
        self.essais_max = essais_max
        self.sous_mots_trouves = set()

    def verifier_tentative(self, proposition):
        """
        Vérifie si le mot original est trouvé.
        Retourne True si gagné, False sinon (et compte une tentative ratée).
        """
        if self.etat != "en cours":
            return False

        if proposition.lower() == self.mot_original:
            self.etat = "gagnée"
            return True

        self.tentatives.append(proposition)
        if len(self.tentatives) >= self.essais_max:
            self.etat = "perdue"
        return False

    def verifier_sous_mot(self, mot, banque_sous_mots):
        """Vérifie si un sous-mot est valide et renvoie son bonus (0 si invalide)."""
        mot = mot.lower()
        bonus = len(mot)

        longueur_min = 3 if self.parametres and self.parametres.difficulte != "facile" else 2
        if len(mot) < longueur_min:
            return 0

        if mot in self.sous_mots_trouves or mot == self.mot_original:
            return 0

        if mot not in banque_sous_mots.liste_mots:
            return 0

        for lettre in set(mot):
            if mot.count(lettre) > self.mot_melange.count(lettre):
                return 0

        self.sous_mots_trouves.add(mot)
        return bonus
