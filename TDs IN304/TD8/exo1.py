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



class Attaque:
    def __init__(self,nom,degats,usages,usage_max):
        self.nom = nom
        self.degats = degats
        self.usages = usages
        self.usages_max = usage_max


pk1 = Pokemon("Harbok",35)
pk1.ajouter_attaque(Attaque("Venin",7,0,20))
pk2 = Pokemon("Pikachu",32)
pk2.ajouter_attaque(Attaque("Eclair",10,0,10))
