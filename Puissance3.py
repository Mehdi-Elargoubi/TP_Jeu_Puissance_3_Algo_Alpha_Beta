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

    # def estFinJeu(self, typeJoueur, matrice):
    #     """
    #     Vérifie si la partie est terminée (si le joueur a gagné ou si la grille est pleine).
    #     """
    #     noeud = Noeud(typeJoueur, matrice)
    #     return noeud.troisPionsAlignesLigne(typeJoueur) == 1000 or noeud.troisPionsAlignesColonne(typeJoueur) == 1000

    def estFinJeu(self, typeJoueur, matrice):
        """
        Vérifie si le jeu est terminé.
        :param typeJoueur: int, le joueur (1 pour l'IA, 2 pour l'humain) dont on vérifie la condition de victoire.
        :param matrice: list[list[int]], la grille de jeu actuelle.
        :return: bool, True si le jeu est terminé (victoire ou grille pleine), sinon False.
        """
        noeud = Noeud(typeJoueur, matrice)

        # Vérifie si le joueur a aligné 3 pions en ligne ou en colonne
        if (noeud.troisPionsAlignesLigne(typeJoueur) == 1000 
            or noeud.troisPionsAlignesColonne(typeJoueur) == 1000):
            return True  # Le joueur a gagné

        # Vérifie si la grille est pleine
        for row in matrice:
            if 0 in row:
                return False  # Au moins une case est vide, le jeu continue

        # Si aucune case vide n'est trouvée, la grille est pleine
        return True


    def copieMatrice(self, mSource):
        return copy.deepcopy(mSource)

    # def alpha_beta(self, noeud, alpha, beta, profondeur):
    #     """
    #     Implémente l'algorithme Alpha-Beta pour déterminer le meilleur coup pour l'IA.
    #     """
    #     if profondeur == 0 or self.estFinJeu(not noeud.isMax(), noeud.getMatrice()):
    #         noeud.evaluer()
    #         return Coup(noeud.getH(), -1)

    #     bestColonne = -1

    #     if noeud.isMax():
    #         maxEval = -float('inf')
    #         for col in range(self.WIDTH):
    #             matriceCopie = self.copieMatrice(noeud.getMatrice())
    #             if self.jouer(1, col, matriceCopie):
    #                 successeur = Noeud(False, matriceCopie)
    #                 coup = self.alpha_beta(successeur, alpha, beta, profondeur - 1)
    #                 if coup.getEval() > maxEval:
    #                     maxEval = coup.getEval()
    #                     bestColonne = col
    #                 alpha = max(alpha, coup.getEval())
    #                 if beta <= alpha:
    #                     break
    #         return Coup(maxEval, bestColonne)
    #     else:
    #         minEval = float('inf')
    #         for col in range(self.WIDTH):
    #             matriceCopie = self.copieMatrice(noeud.getMatrice())
    #             if self.jouer(2, col, matriceCopie):
    #                 successeur = Noeud(True, matriceCopie)
    #                 coup = self.alpha_beta(successeur, alpha, beta, profondeur - 1)
    #                 if coup.getEval() < minEval:
    #                     minEval = coup.getEval()
    #                     bestColonne = col
    #                 beta = min(beta, coup.getEval())
    #                 if beta <= alpha:
    #                     break
    #         return Coup(minEval, bestColonne)



    # def alpha_beta(self, noeud, alpha, beta, profondeur):
    #     """
    #     Implémente l'algorithme Alpha-Beta pour déterminer le meilleur coup pour l'IA.
    #     """
    #     # Condition d'arrêt : si la profondeur est atteinte ou si la partie est terminée
    #     if profondeur == 0 or self.estFinJeu(not noeud.isMax(), noeud.getMatrice()):
    #         noeud.evaluer()
    #         print(f"Evaluation du noeud : {noeud.getH()}")  # Debug pour l'évaluation
    #         return Coup(noeud.getH(), -1)  # -1 signifie aucun mouvement spécifique trouvé

    #     bestColonne = -1  # Réinitialisation de bestColonne

    #     if noeud.isMax():  # Nœud MAX
    #         maxEval = -float('inf')
    #         for col in range(self.WIDTH):
    #             matriceCopie = self.copieMatrice(noeud.getMatrice())
    #             if self.jouer(1, col, matriceCopie):  # Tente de jouer dans la colonne
    #                 successeur = Noeud(False, matriceCopie)
    #                 coup = self.alpha_beta(successeur, alpha, beta, profondeur - 1)
    #                 print(f"MAX - Colonne {col}, Evaluation: {coup.getEval()}")  # Debug

    #                 if coup.getEval() > maxEval:
    #                     maxEval = coup.getEval()
    #                     bestColonne = col  # Mise à jour de la meilleure colonne trouvée

    #                 alpha = max(alpha, coup.getEval())  # Mise à jour de alpha
    #                 if beta <= alpha:  # Coupure alpha-beta
    #                     break

    #         print(f"Meilleure colonne pour MAX: {bestColonne}, Evaluation: {maxEval}")  # Debug final MAX
    #         return Coup(maxEval, bestColonne)

    #     else:  # Nœud MIN
    #         minEval = float('inf')
    #         for col in range(self.WIDTH):
    #             matriceCopie = self.copieMatrice(noeud.getMatrice())
    #             if self.jouer(2, col, matriceCopie):  # Tente de jouer dans la colonne
    #                 successeur = Noeud(True, matriceCopie)
    #                 coup = self.alpha_beta(successeur, alpha, beta, profondeur - 1)
    #                 print(f"MIN - Colonne {col}, Evaluation: {coup.getEval()}")  # Debug

    #                 if coup.getEval() < minEval:
    #                     minEval = coup.getEval()
    #                     bestColonne = col  # Mise à jour de la meilleure colonne trouvée

    #                 beta = min(beta, coup.getEval())  # Mise à jour de beta
    #                 if beta <= alpha:  # Coupure alpha-beta
    #                     break

    #         print(f"Meilleure colonne pour MIN: {bestColonne}, Evaluation: {minEval}")  # Debug final MIN
    #         return Coup(minEval, bestColonne)


    # def alpha_beta(self, noeud, alpha, beta, profondeur):
    #     """
    #     Implémente l'algorithme Alpha-Beta pour déterminer le meilleur coup pour l'IA.
    #     :param noeud: Noeud, représentant l'état actuel du jeu (grille et type de joueur).
    #     :param alpha: int, valeur alpha pour l'élagage (meilleure évaluation maximale trouvée).
    #     :param beta: int, valeur beta pour l'élagage (meilleure évaluation minimale trouvée).
    #     :param profondeur: int, profondeur de recherche dans l'arbre des coups.
    #     :return: Coup, le meilleur coup avec son évaluation et la colonne où jouer.
    #     """
    #     # Condition d'arrêt de la récursion : profondeur maximale ou fin de jeu
    #     if profondeur == 0 or self.estFinJeu(not noeud.isMax(), noeud.getMatrice()):
    #         noeud.evaluer()  # Évaluation de l'état actuel
    #         return Coup(noeud.getH(), -1)  # Retourne l'évaluation et -1 si aucun coup n'est joué

    #     bestColonne = -1  # Par défaut, aucune colonne sélectionnée

    #     if noeud.isMax():  # Si le nœud est de type MAX (tour de l'IA)
    #         maxEval = -float('inf')  # Initialisation à l'infini négatif pour trouver la meilleure évaluation

    #         # Parcours de chaque colonne pour tester les coups possibles
    #         for col in range(self.WIDTH):
    #             matriceCopie = self.copieMatrice(noeud.getMatrice())
                
    #             if self.jouer(1, col, matriceCopie):  # Simule un coup de l'IA dans la colonne
    #                 successeur = Noeud(False, matriceCopie)  # Crée un nœud successeur pour le prochain tour du joueur MIN
    #                 coup = self.alpha_beta(successeur, alpha, beta, profondeur - 1)  # Récursion avec profondeur -1

    #                 # Mise à jour de la meilleure évaluation et de la colonne
    #                 if coup.getEval() > maxEval:
    #                     maxEval = coup.getEval()
    #                     bestColonne = col  # Colonne optimisée pour l'IA

    #                 alpha = max(alpha, coup.getEval())  # Mise à jour d'alpha pour l'élagage
    #                 if beta <= alpha:  # Coupure Alpha-Beta (aucune colonne meilleure trouvée)
    #                     break

    #         return Coup(maxEval, bestColonne)  # Retourne le coup optimal pour MAX

    #     else:  # Si le nœud est de type MIN (tour de l'adversaire)
    #         minEval = float('inf')  # Initialisation à l'infini positif pour trouver la pire évaluation

    #         # Parcours de chaque colonne pour tester les coups possibles
    #         for col in range(self.WIDTH):
    #             matriceCopie = self.copieMatrice(noeud.getMatrice())

    #             if self.jouer(2, col, matriceCopie):  # Simule un coup de l'adversaire dans la colonne
    #                 successeur = Noeud(True, matriceCopie)  # Crée un nœud successeur pour le prochain tour du joueur MAX
    #                 coup = self.alpha_beta(successeur, alpha, beta, profondeur - 1)  # Récursion avec profondeur -1

    #                 # Mise à jour de la pire évaluation et de la colonne
    #                 if coup.getEval() < minEval:
    #                     minEval = coup.getEval()
    #                     bestColonne = col  # Colonne optimisée pour l'adversaire

    #                 beta = min(beta, coup.getEval())  # Mise à jour de beta pour l'élagage
    #                 if beta <= alpha:  # Coupure Alpha-Beta (aucune colonne pire trouvée)
    #                     break

    #         return Coup(minEval, bestColonne)  # Retourne le coup optimal pour MIN


    def alpha_beta(self, noeud, alpha, beta, profondeur):
        if profondeur == 0 or self.estFinJeu(1 if noeud.isMax() else 2, noeud.getMatrice()):
            noeud.evaluer()
            return Coup(noeud.getH(), None)

        meilleurCoup = None
        if noeud.isMax():
            maxEval = -float('inf')
            for col in range(self.WIDTH):
                nouvelleMatrice = self.copieMatrice(noeud.getMatrice())
                if self.jouer(1, col, nouvelleMatrice):
                    enfantNoeud = Noeud(False, nouvelleMatrice)
                    coup = self.alpha_beta(enfantNoeud, alpha, beta, profondeur - 1)
                    if coup.getEval() > maxEval:
                        maxEval = coup.getEval()
                        meilleurCoup = Coup(maxEval, col)
                    alpha = max(alpha, coup.getEval())
                    if beta <= alpha:
                        break
            return meilleurCoup
        else:
            minEval = float('inf')
            for col in range(self.WIDTH):
                nouvelleMatrice = self.copieMatrice(noeud.getMatrice())
                if self.jouer(2, col, nouvelleMatrice):
                    enfantNoeud = Noeud(True, nouvelleMatrice)
                    coup = self.alpha_beta(enfantNoeud, alpha, beta, profondeur - 1)
                    if coup.getEval() < minEval:
                        minEval = coup.getEval()
                        meilleurCoup = Coup(minEval, col)
                    beta = min(beta, coup.getEval())
                    if beta <= alpha:
                        break
            return meilleurCoup
