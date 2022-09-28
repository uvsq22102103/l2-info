import random

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
        self.pv_max = pv
        Pokemon.compteur += 1
    
    def ajouter_attaque(self,attaque):
        if attaque not in self.attaques and len(self.attaques) < 4:
            self.attaques.append(attaque)
    
    def soigner(self,pv):
        self.pv += pv
        for attaque in self.attaques:
            attaque.usages = 0
    
    def Afficher_pokemon(self):
        print(self.nom+" : %d/%d pv"%(self.pv,self.pv_max))
        for i in self.attaques:
            i.Afficher_attaque()
    
    def Attaque(self,cible):
        print(self.nom+" attaque "+cible.nom)
        attaque = random.choice(self.attaques)
        if attaque.usages_max > attaque.usages:
            attaque.usages += 1
            cible.pv -= attaque.degats
    
    def Soigner_pokemon(self):
        self.pv = self.pv_max
        for attaque in self.attaques:
            attaque.usages = 0
    
    def Scenario1(self,cible):
        self.Attaque(cible)
        self.Attaque(cible)
        self.Afficher_pokemon()
        cible.Afficher_pokemon()
        if cible.pv > 0:
            cible.Attaque(self)
            cible.Attaque(self)
            cible.Attaque(self)
            self.Afficher_pokemon()
            cible.Afficher_pokemon()
    
    def Scenario2(self,cible):
        while self.pv > 0 and cible.pv > 0:
            self.Attaque(cible)
            if cible.pv <= 0:
                break
            cible.Attaque(self)
        self.Afficher_pokemon()
        cible.Afficher_pokemon()
        if self.pv <= 0:
            print(cible.nom+" à gagné le combat pokemon")
            return(cible)
        else:
            print(self.nom+" à gagné le combat pokemon")
            return(self)



class Attaque:
    def __init__(self,nom,degats,usages_max):
        self.nom = nom
        self.degats = degats
        self.usages = 0
        self.usages_max = usages_max
    
    def Afficher_attaque(self):
        print("   >"+self.nom,"; %d Dégats;"%self.degats,"%d/%d Usage max."%(self.usages,self.usages_max))


#pk1.Scenario1(pk2)
#pk1.Scenario2(pk2)
