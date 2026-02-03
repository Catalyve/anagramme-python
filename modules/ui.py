"""
ui.py — Contient la classe UI.

Cette classe fournit une interface utilisateur en console :
- affiche les manches et les mots mélangés,
- récupère les réponses du joueur,
- affiche les résultats et le résumé final.
"""


class UI:
    """Interface utilisateur en console."""

    @staticmethod
    def afficher_bienvenue():
        """Affiche le message d'accueil du jeu (compatible tous systèmes)."""
        message = (
    """
        ╔═════════════════════════════════════════════════════════════════════════════════╗     
        ║                    ╔════════════════════════════════════════╗                   ║ 
        ║                    ║        >>  A N A G R A M M E  <<       ║                   ║
        ║                    ╚════════════════════════════════════════╝                   ║
        ║                                                                                 ║
        ║ Bienvenue dans Anagramme !                                                      ║
        ║                                                                                 ║
        ║ Règles :                                                                        ║
        ║ - Le mot est choisi puis mélangé, vous devez retrouver l'original.              ║
        ║   Vous disposez de trois essais.                                                ║
        ║ - En bonus pour les plus acharnés:                                              ║
        ║   Vous pouvez trouver d'autres mots à former avec les mêmes lettres.            ║
        ║   Cependant, interdiction aux sous-mots inférieurs à trois lettres              ║
        ║   en mode difficile.                                                            ║        
        ║                                                                                 ║
        ║ Points :                                                                        ║
        ║   longueur du mot × coef difficulté (facile ×1, moyen ×2,                       ║
        ║   difficile ×3)                                                                 ║
        ║   Chaque essai en plus retire 1 point.                                          ║ 
        ║   Une manche ratée ne rapporte aucun point.                                     ║
        ║   Pire, en mode difficile, on perd autant de points que la longueur             ║   
        ║   du mot.                                                                       ║
        ║ Amusez-vous bien !                                                              ║
        ╚═════════════════════════════════════════════════════════════════════════════════╝
    """
        )
        print(message)

    @staticmethod
    def afficher_manche(manche):
        """Affiche une nouvelle manche et son mot mélangé."""
        print("\nNouvelle manche !")
        print(f"Mot mélangé : {manche.mot_melange}")

    @staticmethod
    def demander_difficulte():
        """Demande au joueur de choisir la difficulté."""
        return int(input(
            "Choisissez la difficulté : Facile (1), Moyen (2) ou Difficile (3) ? "
        ))

    @staticmethod
    def demander_mode():
        """Demande au joueur de choisir la difficulté."""
        return int(input(
            "Choisissez le mode de jeu : Humain (1), Robot (2) ?  "
        ))

    @staticmethod
    def demander_proposition():
        """Demande une proposition au joueur."""
        return input("Votre proposition (mot original ou sous-mot) : ").strip()

    @staticmethod
    def afficher_resultat(correct, mot):
        """Affiche le résultat d'une tentative."""
        if correct:
            print(f"Bravo ! Le mot était bien : {mot}")
        else:
            print(f"Raté... Le mot était : {mot}")

    @staticmethod
    def afficher_sous_mot(mot, points):
        """Affiche le résultat d'un sous-mot proposé."""
        if points > 0:
            print(f"Sous-mot ou anagramme trouvé : {mot} (+{points} points)")
        else:
            print(f"Mot invalide : {mot}")

    @staticmethod
    def afficher_resume(tableau_scores):
        """Affiche le résumé final de la partie."""
        print("\n=== Fin de la partie ===")
        print(tableau_scores.resume())

    @staticmethod
    def demander_rejouer():
        """Demande au joueur s'il souhaite rejouer."""
        return input("Voulez-vous rejouer ? 'o'/'n' ").strip().lower()

    @staticmethod
    def afficher_message_fin():
        """Affiche le message de fin."""
        message_fin = ("""
               ╔═══════════════════════════════╗
               ║Merci d'avoir joué, à bientôt !║
               ╚═══════════════════════════════╝
        """)
        print(message_fin)
