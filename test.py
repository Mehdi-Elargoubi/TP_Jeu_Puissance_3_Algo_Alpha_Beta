class Noeud:
    def __init__(self, max, matrice):
        """
        Initialise un nœud avec la grille de jeu, le type de nœud (max ou min), et une valeur de score par défaut.

        :param max: bool - True si c'est un nœud de type max, False pour min
        :param matrice: list[list[int]] - La matrice représentant l'état du jeu
        """
        self.matrice = matrice  # Matrice de l'état de jeu
        self.max = max          # Booléen pour le type de nœud
        self.h = 0              # Score d'évaluation du nœud

    def getH(self):
        return self.h

    def setH(self, h):
        self.h = h

    def getMatrice(self):
        return self.matrice

    def isMax(self):
        return self.max

    def __str__(self):
        return f"Noeud(type={'MAX' if self.max else 'MIN'}, h={self.h})"

    def troisPionsAlignesLigne(self, type_joueur):
        score = 0
        for row in self.matrice:
            for i in range(len(row) - 2):
                if row[i] == row[i+1] == row[i+2] == type_joueur:
                    score += 1000
        return score

    def troisPionsAlignesColonne(self, type_joueur):
        score = 0
        for col in range(len(self.matrice[0])):
            for row in range(len(self.matrice) - 2):
                if self.matrice[row][col] == self.matrice[row+1][col] == self.matrice[row+2][col] == type_joueur:
                    score += 1000
        return score

    def troisPionsPossiblesLigne(self, type_joueur):
        score = 0
        for row in self.matrice:
            for i in range(len(row) - 2):
                if row[i] == type_joueur and row[i+1] == type_joueur and row[i+2] == 0:
                    score += 200
                elif row[i] == type_joueur and row[i+1] == 0 and row[i+2] == 0:
                    score += 30
        return score

    def troisPionsPossiblesColonne(self, type_joueur):
        score = 0
        for col in range(len(self.matrice[0])):
            for row in range(len(self.matrice) - 2):
                if self.matrice[row][col] == type_joueur and self.matrice[row+1][col] == type_joueur and self.matrice[row+2][col] == 0:
                    score += 200
                elif self.matrice[row][col] == type_joueur and self.matrice[row+1][col] == 0 and self.matrice[row+2][col] == 0:
                    score += 30
        return score

    def evaluer(self):
        self.h = (
            -1 * self.troisPionsAlignesLigne(False) + self.troisPionsAlignesLigne(True)
            -1 * self.troisPionsAlignesColonne(False) + self.troisPionsAlignesColonne(True)
            -1 * self.troisPionsPossiblesLigne(False) + self.troisPionsPossiblesLigne(True)
            -1 * self.troisPionsPossiblesColonne(False) + self.troisPionsPossiblesColonne(True)
        )

class Coup:
    def __init__(self, eval, colonne):
        self.eval = eval          # Score du coup
        self.colonne = colonne    # Colonne où jouer

    def getEval(self):
        return self.eval

    def getColonne(self):
        return self.colonne

    def __str__(self):
        return f"Coup(eval={self.eval}, colonne={self.colonne})"

class Puissance3:
    WIDTH = 5
    HEIGHT = 5

    def __init__(self):
        self.matriceJeu = [[0] * Puissance3.WIDTH for _ in range(Puissance3.HEIGHT)]

    def getMatriceJeu(self):
        return self.matriceJeu

    def jouer(self, type_joueur, colonne, matrice):
        for row in reversed(range(Puissance3.HEIGHT)):
            if matrice[row][colonne] == 0:
                matrice[row][colonne] = 1 if type_joueur else 2
                return True
        return False

    def estFinJeu(self, type_joueur, matrice):
        # Check for win conditions here or if grid is full
        pass  # Implementation of end-game condition check

    def copieMatrice(self, mSource, mDest):
        for i in range(Puissance3.HEIGHT):
            for j in range(Puissance3.WIDTH):
                mDest[i][j] = mSource[i][j]

    def alpha_beta(self, n, alpha, beta, profondeur):
        if profondeur == 0 or self.estFinJeu(not n.isMax(), n.getMatrice()):
            n.evaluer()
            return Coup(n.getH(), -1)

        bestj = -1
        if n.isMax():
            for j in range(Puissance3.WIDTH):
                new_matrice = [row[:] for row in n.getMatrice()]
                if self.jouer(True, j, new_matrice):
                    successeur = Noeud(False, new_matrice)
                    coup = self.alpha_beta(successeur, alpha, beta, profondeur - 1)
                    if coup.getEval() > alpha:
                        alpha = coup.getEval()
                        bestj = j
                    if alpha >= beta:
                        break
            return Coup(alpha, bestj)
        else:
            for j in range(Puissance3.WIDTH):
                new_matrice = [row[:] for row in n.getMatrice()]
                if self.jouer(False, j, new_matrice):
                    successeur = Noeud(True, new_matrice)
                    coup = self.alpha_beta(successeur, alpha, beta, profondeur - 1)
                    if coup.getEval() < beta:
                        beta = coup.getEval()
                        bestj = j
                    if beta <= alpha:
                        break
            return Coup(beta, bestj)





def main():
    jeu = Puissance3()
    matrice = jeu.getMatriceJeu()
    humain = True

    while True:
        if humain:
            colonne = int(input("Choisissez une colonne (0-4): "))
            if not jeu.jouer(1, colonne, matrice):
                print("Colonne pleine, choisissez une autre.")
                continue
        else:
            noeud = Noeud(True, matrice)
            coup = jeu.alpha_beta(noeud, float('-inf'), float('inf'), 4)
            jeu.jouer(2, coup.getColonne(), matrice)
            print(f"L'IA joue en colonne {coup.getColonne()}")

        for row in matrice:
            print(row)

        if jeu.estFinJeu(1, matrice):
            print("Le joueur gagne!")
            break
        elif jeu.estFinJeu(2, matrice):
            print("L'IA gagne!")
            break
        humain = not humain

main()
