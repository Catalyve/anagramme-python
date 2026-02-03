"""
main.py — Point d'entrée du jeu Anagramme.
"""

from modules.wordbank import BanqueMots
from modules.settings import Parametres
from modules.scoreboard import TableauScore
from modules.game import Jeu
from modules.ui import UI


def main():
    """Initialise les composants et lance la partie."""

    try:
        choix_difficulte = UI.demander_difficulte()
    except (TypeError, ValueError):
        print("Difficulté invalide, 'facile' sélectionnée par défaut.")
        difficulte = "facile"
        banque_mots = BanqueMots("data/list_common.txt")
    else:
        if choix_difficulte == 1:
            difficulte = "facile"
            banque_mots = BanqueMots("data/list_common.txt")

        elif choix_difficulte == 2:
            difficulte = "moyen"
            banque_mots = BanqueMots("data/list_less_common.txt")

        elif choix_difficulte == 3:
            difficulte = "difficile"
            banque_mots = BanqueMots("data/list_rare.txt")

        else:
            print("Difficulté invalide, 'facile' sélectionnée par défaut.")
            difficulte = "facile"
            banque_mots = BanqueMots("data/list_common.txt")

    banque_sous_mots = BanqueMots("data/subword.txt")

    nombre_manches = 0
    while nombre_manches <= 0:
        try:
            nombre_manches = int(input("Combien de manches ? "))
            if nombre_manches <= 0:
                print("Veuillez entrer un nombre strictement positif.")
        except ValueError:
            print("Veuillez entrer un nombre entier valide.")
    try:
        mode_jeu = UI.demander_mode()
    except (TypeError, ValueError):
        print("Mode invalide, 'Humain' sélectionné par défaut.")
        mode_jeu = 1

    parametres = Parametres(difficulte, nombre_manches, mode_jeu)
    parametres.valider_difficulte()
    parametres.valider_mode()

    tableau_scores = TableauScore()

    jeu = Jeu(banque_mots, banque_sous_mots, parametres, tableau_scores, mode=mode_jeu)
    jeu.demarrer()


if __name__ == "__main__":
    UI.afficher_bienvenue()
    main()

    while UI.demander_rejouer() == "o":
        main()

    UI.afficher_message_fin()
