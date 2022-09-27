import random

class Pokemon:
    def __init__(self,nom,pv):
        self.nom = nom
        self.pv = pv
        self.attaques = []
    
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
pk1.Afficher_pokemon()
pk2 = Pokemon("Pikachu",32)
pk2.ajouter_attaque(Attaque("Vive attaque",4,0,10))
pk2.ajouter_attaque(Attaque("Eclair",10,0,10))
pk2.Afficher_pokemon()
pk1.Attaque(pk2)
pk1.Afficher_pokemon()
pk2.Afficher_pokemon()
