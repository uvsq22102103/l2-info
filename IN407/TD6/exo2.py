class CompteBancaire():
    def __init__(self, titulaire:str="Dupont", solde:int=1000):
        self.titulaire = titulaire
        self.solde = solde
    
    def depot(self, somme:int):
        self.solde += somme
    
    def retrait(self, somme:int):
        self.solde -= somme
    
    def affiche(self):
        print(f"Titulaire : {self.titulaire}\nSolde : {self.solde}")
