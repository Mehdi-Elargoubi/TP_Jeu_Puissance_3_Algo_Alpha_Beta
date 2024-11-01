class Coup:
    def __init__(self, eval, colonne):
        self.eval = eval             # Évaluation de ce coup
        self.colonne = colonne       # Colonne pour placer le pion

    def getEval(self):
        return self.eval

    def getColonne(self):
        return self.colonne
