class ArbreB():
    
    def __init__(self, sommet):
        self.content = {"racine" : sommet, "fg" : None, "fd" : None}
    
    def add_sommet(self, sommet):
        if self.content["fg"] == None:
            self.content["fg"] = sommet
        elif self.content["fd"] == None:
            self.content["fd"] == sommet
        else:
            raise IndexError

    def recherche_element(self,elem):
        pass
    
    def fusion(self,ArbreB): # surcharge opérateur ==> ArbreB + ArbreB
        pass

    def __add__(self,ArbreB):
        self.fusion(ArbreB)
    
    def décomposition(self): # surcharge opérateur ==> ArbreB / ArbreB
        pass