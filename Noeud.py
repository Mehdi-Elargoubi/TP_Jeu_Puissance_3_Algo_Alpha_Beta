class Noeud:
    def __init__(self, max, matrice):
        self.matrice = matrice        # La grille du jeu
        self.max = max                # Booléen, True pour un nœud Max, False pour un nœud Min
        self.h = 0                    # Score d'évaluation du nœud

    def getH(self):
        return self.h

    def setH(self, h):
        self.h = h

    def getMatrice(self):
        return self.matrice

    def isMax(self):
        return self.max
    
    def toString(self):     # Affichage de la matrice
        matrice_str = "\n".join(["|".join(map(str, row)) for row in self.matrice])
        
        # Type du noeud (Max ou Min) et valeur d'évaluation
        type_noeud = "Max" if self.max else "Min"
        
        # Construction de la chaîne finale
        return f"Type de noeud: {type_noeud}\nValeur d'évaluation: {self.h}\nMatrice:\n{matrice_str}\n"
    
    
    def troisPionsAlignesLigne(self, type_joueur):
        # Retourne 1000 si le joueur a 3 pions alignés dans une ligne, sinon 0
        for row in self.matrice:
            for col in range(len(row) - 2):
                if row[col] == row[col + 1] == row[col + 2] == type_joueur:
                    return 1000
        return 0

    def troisPionsAlignesColonne(self, type_joueur):
        # Retourne 1000 si le joueur a 3 pions alignés dans une colonne, sinon 0
        for col in range(len(self.matrice[0])):
            for row in range(len(self.matrice) - 2):
                if (self.matrice[row][col] == self.matrice[row + 1][col] == self.matrice[row + 2][col] == type_joueur):
                    return 1000
        return 0

    def troisPionsPossiblesLigne(self, type_joueur):
        # Retourne un score pour les lignes avec des configurations favorables pour l'alignement
        score = 0
        for row in self.matrice:
            for col in range(len(row) - 2):
                # Deux pions et une case vide
                if row[col] == row[col + 1] == type_joueur and row[col + 2] == 0:
                    score += 200
                elif row[col] == type_joueur and row[col + 1] == row[col + 2] == 0:
                    score += 30
        return score

    def troisPionsPossiblesColonne(self, type_joueur):
        # Retourne un score pour les colonnes avec des configurations favorables pour l'alignement
        score = 0
        for col in range(len(self.matrice[0])):
            for row in range(len(self.matrice) - 2):
                # Deux pions et une case vide
                if (self.matrice[row][col] == self.matrice[row + 1][col] == type_joueur and self.matrice[row + 2][col] == 0):
                    score += 200
                elif self.matrice[row][col] == type_joueur and self.matrice[row + 1][col] == self.matrice[row + 2][col] == 0:
                    score += 30
        return score

    def evaluer(self):
        # Évalue la position du nœud pour déterminer si elle est favorable ou non
        self.h = (-1 * self.troisPionsAlignesLigne(False) + self.troisPionsAlignesLigne(True)
                  -1 * self.troisPionsAlignesColonne(False) + self.troisPionsAlignesColonne(True)
                  -1 * self.troisPionsPossiblesLigne(False) + self.troisPionsPossiblesLigne(True)
                  -1 * self.troisPionsPossiblesColonne(False) + self.troisPionsPossiblesColonne(True))
