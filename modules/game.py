"""
game.py — Gère le déroulement complet du jeu Anagramme.
"""

from modules.generator import GenerateurAnagramme
from modules.round import Manche
from modules.ui import UI
from modules.robot import Robot


class Jeu:
    """Orchestre le déroulement complet du jeu."""

    def __init__(self, banque_mots, banque_sous_mots, parametres, tableau_score, mode=1):
        self.banque_mots = banque_mots
        self.banque_sous_mots = banque_sous_mots
        self.parametres = parametres
        self.tableau_score = tableau_score
        self.manches_jouees = 0
        self.manche_actuelle = None
        self.mode = mode

    def demarrer(self):
        """Démarre la partie et gère la boucle des manches."""
        self.banque_sous_mots.charger()
        self.banque_mots.charger()

        self.tableau_score.manches_jouees = 0
        self.tableau_score.manches_gagnees = 0
        self.tableau_score.points = 0
        self.manches_jouees = 0

        for numero in range(1, self.parametres.nombre_manches + 1):
            print(f"\n===== Manche {numero}/{self.parametres.nombre_manches} =====")
            self.manches_jouees += 1

            if self.mode == 2:
                self.jouer_manche_robot()
            else:
                self.jouer_manche_humain()

        print(self.tableau_score.resume())

    def jouer_manche_robot(self):
        """Manche jouée par le robot."""
        mot = self.banque_mots.mot_aleatoire(self.parametres.difficulte)
        self.manche_actuelle = Manche(mot, GenerateurAnagramme(), self.parametres, essais_max=3)

        UI.afficher_manche(self.manche_actuelle)

        sous_mots = Robot.trouver_sous_mots(self.manche_actuelle.mot_melange, self.banque_sous_mots)

        for sm in sous_mots:
            bonus = self.manche_actuelle.verifier_sous_mot(sm, self.banque_sous_mots)
            if bonus > 0:
                self.tableau_score.ajouter_sous_mot(bonus)
                UI.afficher_sous_mot(sm, bonus)

        print(f"Robot propose le mot final : {self.manche_actuelle.mot_original}")
        self.manche_actuelle.statut = "gagné"
        self.tableau_score.ajouter_succes(self.manche_actuelle, self.parametres.difficulte)
        UI.afficher_resultat(True, self.manche_actuelle.mot_original)

    def jouer_manche_humain(self):
        """Manche jouée par un humain."""
        mot = self.banque_mots.mot_aleatoire(self.parametres.difficulte)
        self.manche_actuelle = Manche(mot, GenerateurAnagramme(), self.parametres, essais_max=3)

        UI.afficher_manche(self.manche_actuelle)

        erreurs_sous_mots = 0
        erreurs_anagrammes = 0
        max_erreurs = 3

        while self.manche_actuelle.etat == "en cours":
            proposition = UI.demander_proposition().strip().lower()

            if len(proposition) == len(self.manche_actuelle.mot_original):
                est_faux = self._gerer_anagramme(proposition)
                if est_faux:
                    erreurs_anagrammes += 1
                    if erreurs_anagrammes >= max_erreurs:
                        self._perdre_manche()
                        break

            else:
                est_faux = self._gerer_sous_mot(proposition)
                if est_faux:
                    erreurs_sous_mots += 1
                    if erreurs_sous_mots >= max_erreurs:
                        self._perdre_manche()
                        break

        if self.manche_actuelle.etat == "en cours":
            self._perdre_manche()

    def _gerer_anagramme(self, proposition):
        """Gère la vérification d'un mot complet (anagramme ou mot original)."""
        if proposition == self.manche_actuelle.mot_original:
            self.manche_actuelle.statut = "gagné"
            self.tableau_score.ajouter_succes(self.manche_actuelle, self.parametres.difficulte)
            UI.afficher_resultat(True, proposition)
            return False

        tri_prop = "".join(sorted(proposition))
        tri_ori = "".join(sorted(self.manche_actuelle.mot_original))

        est_valide = (
            tri_prop == tri_ori
            and (proposition in self.banque_mots.words or proposition in self.banque_sous_mots.words)
        )

        if est_valide:
            if proposition not in self.manche_actuelle.sous_mots_trouves:
                self.manche_actuelle.sous_mots_trouves.add(proposition)
                self.tableau_score.ajouter_sous_mot(len(proposition))
                UI.afficher_sous_mot(proposition, len(proposition))
            else:
                print("Mot déjà proposé.")
            return False

        print("Mauvaise anagramme.")
        return True

    def _gerer_sous_mot(self, proposition):
        """Gère la vérification d’un sous-mot."""
        bonus = self.manche_actuelle.verifier_sous_mot(proposition, self.banque_sous_mots)

        if bonus > 0:
            self.tableau_score.ajouter_sous_mot(bonus)
            UI.afficher_sous_mot(proposition, bonus)
            return False

        print("Mot invalide ou non formable.")
        return True

    def _perdre_manche(self):
        self.manche_actuelle.etat = "perdu"  # ← essentiel
        self.manche_actuelle.statut = "perdu"
        self.tableau_score.ajouter_echec(self.manche_actuelle, self.parametres.difficulte)
        UI.afficher_resultat(False, self.manche_actuelle.mot_original)

    def terminer(self):
        """Affiche simplement le score final."""
        print(self.tableau_score.resumer())
