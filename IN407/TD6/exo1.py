class Domino(object):
    def __init__(self,faceA:int,faceB:int):
        self.faceA = faceA
        self.faceB = faceB
    
    def affiche_points(self):
        print(f"Face A : {self.faceA}\nFace B : {self.faceB}")
    
    def valeur(self):
        return self.faceA + self.faceB

liste_dominos = []
for indice in range(7) :
    liste_dominos.append(Domino(6, indice))

total = 0
for domino in liste_dominos:
    total += domino.valeur()
    domino.affiche_points()
print(f"Total points : {total}")
