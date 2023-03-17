class Voiture():
    def __init__(self, marque:str="Ford", couleur:str="rouge"):
        self.marque = marque
        self.couleur = couleur
        self.pilote = "personne"
        self.vitesse = 0
    
    def choix_conducteur(self, nom:str):
        self.pilote = nom
    
    def accelerer(self, taux:int, durée:int):
        if self.pilote != "personne":
            if durée > 0:
                self.vitesse += taux*durée
            else:
                print("La conducteur est maboule")
        else:
            print("!Arrêt voiture!\nmotif : pas de conducteur au volant")
            self.vitesse = 0
    
    def affiche_tout(self):
        print(self.marque,self.couleur,self.pilote,self.vitesse)


auto1 = Voiture("Peugeot", "bleue")
auto2 = Voiture(couleur = "verte")
auto3 = Voiture("Mercedes")
auto1.choix_conducteur("Roméo")
auto2.choix_conducteur("Juliette")
auto2.accelerer(1.8, 12)
auto3.accelerer(1.9, 11)
auto2.affiche_tout()
auto3.affiche_tout()