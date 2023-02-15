from classes.sommet import Sommet

class ArbreB():
    
    def __init__(self, sommet:Sommet):
        self.content = {"racine" : sommet, "fg" : None, "fd" : None}
    
    def add_sommet(self, sommet:Sommet):
        if self.content["fg"] == None:
            self.content["fg"] = sommet
        elif self.content["fd"] == None:
            self.content["fd"] == sommet
        else:
            raise IndexError

    def recherche_element(self,elem):
        pass
    
    def fusion(self,abr):
        fg = self.content.copy()
        fd = abr.content.copy()
        self.content = {"racine" : Sommet(fg["racine"].etiquette + fd["racine"].etiquette),
                        "fg" : fg, "fd" : fd}
        return self

    def __add__(self,ArbreB):
        return self.fusion(ArbreB)
    
    def decomposition(self): # surcharge opérateur ==> ArbreB / ArbreB
        pass

    def _staged_merger(liste_abr:list):
        """Fusion par étages"""
        output = []
        while len(liste_abr) >= 2:
            output.append(liste_abr.pop(0) + liste_abr.pop(0))
        for i in liste_abr:
            output.append(i)
        return output
    
    def merger(liste_abr:list):
        """Prend une liste d'arbres en argument et fusionne le
        tout en un seul et même arbre."""
        while len(liste_abr) > 1:
            liste_abr = ArbreB._staged_merger(liste_abr)
        return liste_abr[0]
    
    def show(self):
        """Affiche le contenu de l'arbre dans le terminal"""
        current = self.content
        ArbreB._recurcive_show(current,0)
    
    def _recurcive_show(current,n):
        print(" "*10*n,(current["racine"].value, current["racine"].etiquette))
        n+=1
        if not current["racine"].is_leaf():
            ArbreB._recurcive_show(current["fg"],n)
            ArbreB._recurcive_show(current["fd"],n)
