"""
robot.py — Contient la classe RobotIntelligent.

Ce robot résout un anagramme en comparant les lettres triées
du mot mélangé avec celles des mots du dictionnaire.
Il trouve aussi les sous-mots valides formés à partir
des lettres disponibles.
"""


class Robot:
    """
    Robot solveur complet :
    - trouve les sous-mots valides,
    - trouve le mot final correspondant à l’anagramme.
    """

    @staticmethod
    def resoudre(mot_melange, banque_mots):
        """Retourne le mot original correspondant à l’anagramme."""
        melange_tri = "".join(sorted(mot_melange.lower()))

        for mot in banque_mots.words:
            if "".join(sorted(mot.lower())) == melange_tri:
                return mot

        return None

    @staticmethod
    def trouver_sous_mots(mot_melange, banque_sous_mots, difficulte="facile"):
        """Retourne les sous-mots valides formables avec les lettres disponibles."""
        mot_melange = mot_melange.lower()
        sous_mots_trouves = []

        longueur_min = 3 if difficulte != "facile" else 2

        for mot in banque_sous_mots.liste_mots:
            mot_courant = mot.lower()

            if len(mot_courant) < longueur_min or len(mot_courant) >= len(mot_melange):
                continue

            if all(mot_courant.count(lettre) <= mot_melange.count(lettre)
                   for lettre in set(mot_courant)):
                sous_mots_trouves.append(mot_courant)

        return sorted(set(sous_mots_trouves))
