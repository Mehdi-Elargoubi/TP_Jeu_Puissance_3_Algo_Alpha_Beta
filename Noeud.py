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
        score = 0
        for row in self.matrice:
            for col in range(len(row) - 2):
                count = sum(1 for k in range(3) if row[col + k] == type_joueur)
                empty = sum(1 for k in range(3) if row[col + k] == 0)
                if count == 2 and empty == 1:  # Deux pions et une case vide
                    score += 200
                elif count == 1 and empty == 2:  # Un pion et deux cases vides
                    score += 30
        return score
    
    def troisPionsPossiblesColonne(self, type_joueur):
        score = 0
        for col in range(len(self.matrice[0])):
            for row in range(len(self.matrice) - 2):
                count = sum(1 for k in range(3) if self.matrice[row + k][col] == type_joueur)
                empty = sum(1 for k in range(3) if self.matrice[row + k][col] == 0)
                if count == 2 and empty == 1:  # Deux pions et une case vide
                    score += 200
                elif count == 1 and empty == 2:  # Un pion et deux cases vides
                    score += 30
        return score

    def evaluer(self):
        # Calcule l'évaluation finale en combinant les évaluations positives et négatives
        self.h = (-1 * self.troisPionsAlignesLigne(2) + self.troisPionsAlignesLigne(1)
                  -1 * self.troisPionsAlignesColonne(2) + self.troisPionsAlignesColonne(1)
                  -1 * self.troisPionsPossiblesLigne(2) + self.troisPionsPossiblesLigne(1)
                  -1 * self.troisPionsPossiblesColonne(2) + self.troisPionsPossiblesColonne(1))

# Initialiser la matrice avec la situation de jeu intermédiaire
matrice_jeu = [
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0],
    [1, 2, 0, 2, 0]
]

# Créer une instance de Noeud en mode Max (par exemple)
noeud = Noeud(1, matrice_jeu)

# Appeler les méthodes de test et afficher les résultats
print("troisPionsAlignesLigne (joueur True):", noeud.troisPionsAlignesLigne(1))
print("troisPionsAlignesLigne (joueur False):", noeud.troisPionsAlignesLigne(2))
print("troisPionsAlignesColonne (joueur True):", noeud.troisPionsAlignesColonne(1))
print("troisPionsAlignesColonne (joueur False):", noeud.troisPionsAlignesColonne(2))
print("troisPionsPossiblesLigne (joueur True):", noeud.troisPionsPossiblesLigne(1))
print("troisPionsPossiblesLigne (joueur False):", noeud.troisPionsPossiblesLigne(2))
print("troisPionsPossiblesColonne (joueur True):", noeud.troisPionsPossiblesColonne(1))
print("troisPionsPossiblesColonne (joueur False):", noeud.troisPionsPossiblesColonne(2))

# Évaluer la situation actuelle et afficher le score d'évaluation
noeud.evaluer()
print("Évaluation du noeud:", noeud.h)