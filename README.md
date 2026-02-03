# Anagramme

**Anagramme** est un jeu développé en **Python**, jouable en **console**, dont le principe est de retrouver un mot à partir de ses lettres mélangées.
Le joueur peut également proposer des **sous-mots valides** afin de gagner des points bonus.

Le projet met l’accent sur une **architecture modulaire**, une **logique fiable**, et une **implémentation propre des règles du jeu**.

---

## Objectifs du projet

- Concevoir un jeu Python structuré et maintenable  
- Implémenter une logique robuste pour :
  - les anagrammes
  - les sous-mots  
- Développer un **résolveur d'anagrammes simple (SmartRobot)**  
- Mettre en place un **système de score équilibré**  
- Respecter les bonnes pratiques de programmation  

---

## Fonctionnalités principales

- Génération d’anagrammes garanties différentes du mot original  
- **Mode Humain**
  - 3 essais pour trouver le mot
  - Sous-mots autorisés pour obtenir des points bonus  
- **Mode Robot**
  - Détection automatique des sous-mots
  - Résolution systématique de l’anagramme finale  
- **3 niveaux de difficulté**
  - Facile / Moyen / Difficile (longueur des mots)  
- **Scoreboard**
  - Manches jouées
  - Manches gagnées
  - Score total
  - Pénalités en mode difficile  

---

## Fonctionnement du robot

Le robot (`SmartRobot`) fonctionne de manière déterministe :
- il compare les lettres triées du mot mélangé avec celles des mots du dictionnaire,
- il identifie tous les sous-mots possibles,
- il retrouve toujours le mot original.

---

## Architecture du projet

```
Project-1-anagramme/
│
├── data/
├── modules/
│   ├── game.py
│   ├── round.py
│   ├── robot.py
│   ├── scoreboard.py
│   ├── settings.py
│   ├── generator.py
│   ├── wordbank.py
│   └── ui.py
│
├── main.py
└── README.md
```

---

## Lancer le jeu

```bash
python main.py
```

---
## Évolutions possibles

- Interface graphique
- Sauvegarde des scores
- Classement des joueurs
- Nouveaux modes de jeu
---
## Licence

MIT License.
