import Coup
import Noeud


class Puissance3:
    WIDTH = 5
    HEIGHT = 5

    def __init__(self):
        # Initialise la matrice de jeu avec des zéros (cases vides)
        self.matriceJeu = [[0 for _ in range(self.WIDTH)] for _ in range(self.HEIGHT)]

    def getMatriceJeu(self):
        return self.matriceJeu

    def jouer(self, type_joueur, colonne, matrice):
        # Place un pion dans la colonne indiquée pour `type_joueur`
        for row in range(self.HEIGHT - 1, -1, -1):
            if matrice[row][colonne] == 0:
                matrice[row][colonne] = type_joueur
                return True
        return False

    def estFinJeu(self, type_joueur, matrice):
        # Vérifie si le jeu est fini (grille remplie ou alignement)
        node = Noeud(type_joueur == 1, matrice)
        return (node.troisPionsAlignesLigne(type_joueur) > 0 
               or node.troisPionsAlignesColonne(type_joueur) > 0)

    def copieMatrice(self, mSource):
        # Retourne une copie de la matrice
        return [row[:] for row in mSource]


    def alpha_beta(self, n, alpha, beta, profondeur):
        # Implémente l'algorithme Alpha-Beta
        if profondeur == 0 or self.estFinJeu(not n.isMax(), n.getMatrice()):
            n.evaluer()
            return Coup(n.getH(), -1)

        if n.isMax():
            best_eval = Coup(alpha, -1)
            for j in range(self.WIDTH):
                matrice_copie = self.copieMatrice(n.getMatrice())
                if self.jouer(1, j, matrice_copie):
                    successeur = Noeud(2, matrice_copie)
                    coup = self.alpha_beta(successeur, alpha, beta, profondeur - 1)
                    if coup.getEval() > alpha:
                        alpha = coup.getEval()
                        best_eval = Coup(alpha, j)
                    if alpha >= beta:
                        break
            return best_eval
        else:
            best_eval = Coup(beta, -1)
            for j in range(self.WIDTH):
                matrice_copie = self.copieMatrice(n.getMatrice())
                if self.jouer(2, j, matrice_copie):
                    successeur = Noeud(1, matrice_copie)
                    coup = self.alpha_beta(successeur, alpha, beta, profondeur - 1)
                    if coup.getEval() < beta:
                        beta = coup.getEval()
                        best_eval = Coup(beta, j)
                    if beta <= alpha:
                        break
            return best_eval
