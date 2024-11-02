from Puissance3 import Puissance3
from Noeud import Noeud

def main():
    jeu = Puissance3()
    noeud = Noeud(True, jeu.getMatriceJeu())
    profondeur = 4  # profondeur de recherche

    while True:
        # Tour de l'IA
        coup = jeu.alpha_beta(noeud, -float('inf'), float('inf'), profondeur)
        jeu.jouer(1, coup.getColonne(), jeu.getMatriceJeu())
        print("IA joue à la colonne:", coup.getColonne())
        
        # Affichage de la grille
        for ligne in jeu.getMatriceJeu():
            print(ligne)
        
        if jeu.estFinJeu(1, jeu.getMatriceJeu()):
            print("L'IA a gagné !")
            break

        # Tour du joueur humain
        col = int(input("Choisissez une colonne (0-4) : "))
        if jeu.jouer(2, col, jeu.getMatriceJeu()):
            for ligne in jeu.getMatriceJeu():
                print(ligne)
            if jeu.estFinJeu(2, jeu.getMatriceJeu()):
                print("Vous avez gagné !")
                break
        else:
            print("Colonne pleine, choisissez une autre colonne.")

if __name__ == "__main__":
    main()
