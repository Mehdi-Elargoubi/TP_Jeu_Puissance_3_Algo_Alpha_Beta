import copy
from Coup import Coup
from Noeud import Noeud


# class Puissance3:
#     WIDTH = 5
#     HEIGHT = 5

#     def __init__(self):
#         self.matriceJeu = [[0 for _ in range(self.WIDTH)] for _ in range(self.HEIGHT)]

#     def getMatriceJeu(self):
#         return self.matriceJeu

#     def jouer(self, typeJoueur, colonne, matrice):
#         for i in range(self.HEIGHT - 1, -1, -1):
#             if matrice[i][colonne] == 0:
#                 matrice[i][colonne] = typeJoueur
#                 return True
#         return False

#     def estFinJeu(self, typeJoueur, matrice):
#         noeud = Noeud(typeJoueur, matrice)
#         return noeud.troisPionsAlignesLigne(typeJoueur) == 1000 or noeud.troisPionsAlignesColonne(typeJoueur) == 1000

#     def copieMatrice(self, mSource):
#         return copy.deepcopy(mSource)

#     def alpha_beta(self, noeud, alpha, beta, profondeur):
#         if profondeur == 0 or self.estFinJeu(not noeud.isMax(), noeud.getMatrice()):
#             noeud.evaluer()
#             return Coup(noeud.getH(), -1)

#         bestColonne = -1

#         if noeud.isMax():
#             maxEval = -float('inf')
#             for col in range(self.WIDTH):
#                 matriceCopie = self.copieMatrice(noeud.getMatrice())
#                 if self.jouer(1, col, matriceCopie):
#                     successeur = Noeud(False, matriceCopie)
#                     coup = self.alpha_beta(successeur, alpha, beta, profondeur - 1)
#                     if coup.getEval() > maxEval:
#                         maxEval = coup.getEval()
#                         bestColonne = col
#                     alpha = max(alpha, coup.getEval())
#                     if beta <= alpha:
#                         break
#             return Coup(maxEval, bestColonne)
#         else:
#             minEval = float('inf')
#             for col in range(self.WIDTH):
#                 matriceCopie = self.copieMatrice(noeud.getMatrice())
#                 if self.jouer(2, col, matriceCopie):
#                     successeur = Noeud(True, matriceCopie)
#                     coup = self.alpha_beta(successeur, alpha, beta, profondeur - 1)
#                     if coup.getEval() < minEval:
#                         minEval = coup.getEval()
#                         bestColonne = col
#                     beta = min(beta, coup.getEval())
#                     if beta <= alpha:
#                         break
#             return Coup(minEval, bestColonne)


import copy
from Noeud import Noeud
from Coup import Coup

class Puissance3:
    WIDTH = 5
    HEIGHT = 5

    def __init__(self):
        """
        Initialise la matrice du jeu avec les dimensions spécifiées.
        """
        self.matriceJeu = [[0 for _ in range(self.WIDTH)] for _ in range(self.HEIGHT)]

    def getMatriceJeu(self):
        return self.matriceJeu

    def jouer(self, typeJoueur, colonne, matrice):
        """
        Place un pion pour le joueur spécifié dans la colonne donnée.
        Retourne True si le coup est valide, sinon False.
        """
        for i in range(self.HEIGHT - 1, -1, -1):
            if matrice[i][colonne] == 0:
                matrice[i][colonne] = typeJoueur
                return True
        return False

    def estFinJeu(self, typeJoueur, matrice):
        """
        Vérifie si la partie est terminée (si le joueur a gagné ou si la grille est pleine).
        """
        noeud = Noeud(typeJoueur, matrice)
        return noeud.troisPionsAlignesLigne(typeJoueur) == 1000 or noeud.troisPionsAlignesColonne(typeJoueur) == 1000

    def copieMatrice(self, mSource):
        return copy.deepcopy(mSource)

    def alpha_beta(self, noeud, alpha, beta, profondeur):
        """
        Implémente l'algorithme Alpha-Beta pour déterminer le meilleur coup pour l'IA.
        """
        if profondeur == 0 or self.estFinJeu(not noeud.isMax(), noeud.getMatrice()):
            noeud.evaluer()
            return Coup(noeud.getH(), -1)

        bestColonne = -1

        if noeud.isMax():
            maxEval = -float('inf')
            for col in range(self.WIDTH):
                matriceCopie = self.copieMatrice(noeud.getMatrice())
                if self.jouer(1, col, matriceCopie):
                    successeur = Noeud(False, matriceCopie)
                    coup = self.alpha_beta(successeur, alpha, beta, profondeur - 1)
                    if coup.getEval() > maxEval:
                        maxEval = coup.getEval()
                        bestColonne = col
                    alpha = max(alpha, coup.getEval())
                    if beta <= alpha:
                        break
            return Coup(maxEval, bestColonne)
        else:
            minEval = float('inf')
            for col in range(self.WIDTH):
                matriceCopie = self.copieMatrice(noeud.getMatrice())
                if self.jouer(2, col, matriceCopie):
                    successeur = Noeud(True, matriceCopie)
                    coup = self.alpha_beta(successeur, alpha, beta, profondeur - 1)
                    if coup.getEval() < minEval:
                        minEval = coup.getEval()
                        bestColonne = col
                    beta = min(beta, coup.getEval())
                    if beta <= alpha:
                        break
            return Coup(minEval, bestColonne)
