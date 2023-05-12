from random import shuffle

class JeuDeCartes():
    def __init__(self) -> None:
        couleurs = ["Coeur", "Carreau", "Trèfle", "Pique"]
        valeurs = [str(i) for i in range(2, 11)] + ["Valet", "Dame", "Roi", "As"]
        self.cartes = []
        for couleur in couleurs:
            for valeur in valeurs:
                self.cartes.append((couleur, valeur))
    
    def battre(self):
        shuffle(self.cartes)
    
    def tirer(self):
        try:
            return self.cartes.pop()
        except IndexError:
            return None
    
    def nomCarte(self, carte:tuple):
        if type(carte) == tuple:
            return carte[1] + " de " + carte[0]


player1 = JeuDeCartes()
score1 = 0
player2 = JeuDeCartes()
score2 = 0

player1.battre()
player2.battre()

while True:
    c1 = player1.tirer()
    c2 = player2.tirer()
    if c1 == None or c2 == None:
        print("fin de la partie !")
        break
    elif c1[1] > c2[1]:
        score1 += 1
    elif c1[1] < c2[1]:
        score2 += 1

print(f"player1 : {score1}\nplayer2 : {score2}")