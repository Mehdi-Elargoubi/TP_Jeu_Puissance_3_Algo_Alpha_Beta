# Puissance3 - Projet d'IA pour un Jeu de Grille en Python

## Description
**Puissance3** est une implémentation d'un jeu de type Puissance 3, joué sur une grille de 5x5, avec une intelligence artificielle capable de jouer contre un humain en utilisant l'algorithme Alpha-Beta pour optimiser ses choix. L'objectif est d'aligner 3 pions pour gagner, en ligne ou en colonne.

Le projet est structuré en plusieurs classes :
- **Coup** : Représente un coup potentiel dans le jeu, comprenant une évaluation et une colonne cible.
- **Noeud** : Modélise un état du jeu, permettant d'évaluer des alignements et des configurations.
- **Puissance3** : Gère les règles du jeu et exécute l'algorithme Alpha-Beta pour optimiser le choix de l'IA.
- **Main** : Point d'entrée principal du programme, permettant de lancer une partie en mode interactif entre un joueur et l'IA.

## Prérequis
- Python 3.6 ou supérieur
- Bibliothèque `copy` (standard avec Python)

## Structure du Code
Le projet est divisé en plusieurs fichiers pour une meilleure organisation :
- **Coup.py** : Classe `Coup` qui représente les coups possibles.
- **Noeud.py** : Classe `Noeud` qui modélise un état de la grille.
- **Puissance3.py** : Classe `Puissance3` qui contient la logique du jeu et l'algorithme de recherche Alpha-Beta.
- **Main.py** : Contient la logique pour démarrer le jeu et interagir avec l'utilisateur, permettant de choisir le mode de jeu et de lancer l'IA.

## Installation
1. Clonez ce dépôt :
   ```bash
   git clone "https://github.com/Mehdi-Elargoubi/TP_Jeu_Puissance_3_Algo_Alpha_Beta.git"
   cd puissance3
   ```
2. Assurez-vous que Python est installé et à jour.

## Utilisation
Pour lancer le jeu ou tester les classes, créez un script Python et importez les classes. Voici un exemple d'initialisation :

```python
from Puissance3 import Puissance3

jeu = Puissance3()
# Utilisez les méthodes pour simuler des coups et évaluer la situation
```

## Documentation des Classes et Méthodes

### Classe `Coup`
Représente un coup possible, stockant une évaluation (`eval`) et une colonne (`colonne`).
- **Méthodes :**
  - `getEval()`: Retourne l'évaluation du coup.
  - `getColonne()`: Retourne la colonne cible pour placer le pion.

### Classe `Noeud`
Modélise un état du jeu dans la grille, incluant des méthodes pour évaluer les positions et alignements.
- **Attributs :**
  - `matrice` : Grille de jeu (5x5) représentant l'état actuel.
  - `max` : Booléen indiquant si le noeud représente le joueur maximisant (True) ou minimisant (False).
  - `h` : Score d’évaluation du noeud.
- **Méthodes :**
  - `getH()` : Retourne le score d’évaluation `h`.
  - `setH(h)` : Définit la valeur d’évaluation du noeud.
  - `getMatrice()` : Retourne la matrice de l’état actuel.
  - `isMax()` : Retourne `True` si le noeud est de type maximisant.
  - `toString()` : Affiche la matrice de jeu et les informations du noeud.
  - `troisPionsAlignesLigne(type_joueur)` : Retourne 1000 si le joueur `type_joueur` a trois pions alignés en ligne.
  - `troisPionsAlignesColonne(type_joueur)` : Retourne 1000 si le joueur a trois pions alignés en colonne.
  - `troisPionsPossiblesLigne(type_joueur)` : Calcule le score basé sur des configurations partiellement remplies en ligne.
  - `troisPionsPossiblesColonne(type_joueur)` : Calcule le score basé sur des configurations partiellement remplies en colonne.
  - `evaluer()` : Calcule l'évaluation finale d'un noeud, combinant les scores de différentes configurations.

### Classe `Puissance3`
Gère le déroulement du jeu et implémente l'algorithme Alpha-Beta pour prendre les meilleures décisions.
- **Attributs :**
  - `matriceJeu` : Grille de jeu initialisée à une matrice de 5x5 remplie de zéros (cases vides).
- **Méthodes :**
  - `getMatriceJeu()` : Retourne la matrice actuelle du jeu.
  - `jouer(typeJoueur, colonne, matrice)` : Place un pion pour `typeJoueur` dans `colonne` si possible, et retourne `True` si le coup est valide.
  - `estFinJeu(typeJoueur, matrice)` : Vérifie si le jeu est terminé, soit par victoire soit par grille pleine.
  - `copieMatrice(mSource)` : Crée une copie profonde de la matrice source.
  - `alpha_beta(noeud, alpha, beta, profondeur)` : Implémente l'algorithme Alpha-Beta pour déterminer le meilleur coup pour l'IA.

### Classe `Main`
Point d'entrée principal du programme, permettant de lancer une partie en mode interactif entre un joueur et l'IA.
- **Fonctionnalités :**
  - Initialise la grille de jeu et démarre une session interactive.
  - Permet à l'utilisateur de jouer contre l'IA, en lui demandant de sélectionner une colonne pour son pion.
  - Gère l'affichage de l'état du jeu et les messages de victoire ou de match nul.

## Algorithme Alpha-Beta
L'algorithme Alpha-Beta est utilisé pour réduire l'espace de recherche en évitant d'explorer des branches non nécessaires, ce qui accélère les décisions de l'IA :
- **Alpha** et **Beta** sont des valeurs limites qui permettent de couper certaines branches de l'arbre de recherche.
- La profondeur limite est définie dans le code pour réduire le temps de calcul.
- Si un état terminal (victoire ou grille pleine) est atteint, l’évaluation de ce noeud est utilisée pour influencer la décision.

### Exemple d'Utilisation de l'Algorithme Alpha-Beta
Voici un exemple simple pour tester la méthode `alpha_beta` :

```python
from Puissance3 import Puissance3
from Noeud import Noeud

# Initialiser le jeu et l'état initial
jeu = Puissance3()
matrice_initiale = jeu.getMatriceJeu()
noeud_initial = Noeud(True, matrice_initiale)  # True pour un nœud Max (IA)

# Exécuter l'algorithme Alpha-Beta
meilleur_coup = jeu.alpha_beta(noeud_initial, alpha=-float('inf'), beta=float('inf'), profondeur=3)
print("Meilleur coup :", meilleur_coup.getColonne())
```

## Auteurs
- EL MEHDI EL ARGOUBI

## Licence
Ce projet est sous licence MIT. Voir le fichier [LICENSE](LICENSE) pour plus d'informations.
