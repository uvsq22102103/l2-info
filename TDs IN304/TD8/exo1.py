import random


def scenario1(p1,p2):
    p1.Attaque(p2)
    p1.Attaque(p2)
    p1.Afficher_pokemon()
    p2.Afficher_pokemon()
    if p2.pv > 0:
        p2.Attaque(p1)
        p2.Attaque(p1)
        p2.Attaque(p1)
        p1.Afficher_pokemon()
        p2.Afficher_pokemon()


def scenario2(p1,p2):
    while p1.pv > 0 and p2.pv > 0:
        p1.Attaque(p2)
        if p2.pv <= 0:
            break
        p2.Attaque(p1)
    p1.Afficher_pokemon()
    p2.Afficher_pokemon()
    if p1.pv <= 0:
        print(p2.nom+" à gagné le combat pokemon")
    else:
        print(p1.nom+" à gagné le combat pokemon")


class Pokemon:
    compteur = 0
    def __init__(self,nom,pv):
        self.nom = nom
        self.pv = pv
        self.attaques = []
        Pokemon.compteur += 1
    
    def ajouter_attaque(self,attaque):
        if attaque not in self.attaques and len(self.attaques) < 4:
            self.attaques.append(attaque)
    
    def soigner(self,pv):
        self.pv += pv
        for attaque in self.attaques:
            attaque.usages = 0
    
    def Afficher_pokemon(self):
        print(self.nom+" : %d pv"%self.pv)
        for i in self.attaques:
            i.Afficher_attaque()
    
    def Attaque(self,cible):
        print(self.nom+" attaque "+cible.nom)
        attaque = random.choice(self.attaques)
        if attaque.usages_max > attaque.usages:
            attaque.usages += 1
            cible.pv -= attaque.degats


class Attaque:
    def __init__(self,nom,degats,usages,usages_max):
        self.nom = nom
        self.degats = degats
        self.usages = usages
        self.usages_max = usages_max
    
    def Afficher_attaque(self):
        print(self.nom,"; %d Dégats;"%self.degats,"%d/%d Usage max."%(self.usages,self.usages_max))


pk1 = Pokemon("Harbok",35)
pk1.ajouter_attaque(Attaque("Charge",3,0,40))
pk1.ajouter_attaque(Attaque("Venin",7,0,20))
pk2 = Pokemon("Pikachu",32)
pk2.ajouter_attaque(Attaque("Vive attaque",4,0,10))
pk2.ajouter_attaque(Attaque("Eclair",10,0,10))
print("Il y a %d pokemons dans ce Monde"%Pokemon.compteur)

#scenario1(pk1,pk2)
#scenario2(pk1,pk2)