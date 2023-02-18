class Sommet():

    def __init__(self, etiquette: int, value: int=None):
        self.etiquette = etiquette
        self.value = value

    def set_etiquette(self, new_etiquette):
        self.etiquette = new_etiquette

##############################################################################################

class ArbreB():
    
    def __init__(self, sommet:Sommet):
        self.content = {"r" : sommet, "fg" : None, "fd" : None}

    def fusion(self,abr):
        fg = self.content.copy()
        fd = abr.content.copy()
        self.content = {"r" : Sommet(fg["r"].etiquette + fd["r"].etiquette),
                        "fg" : fg, "fd" : fd}
        del abr
        return self

    def __add__(self,ArbreB):
        return self.fusion(ArbreB)
    
    def show(self,_n=None):
        """Affiche le contenu de l'arbre dans le terminal"""
        if type(self) == ArbreB:
            ArbreB.show(self.content,0)
        else:
            print(" "*7*_n,(self["r"].value, self["r"].etiquette))
            _n+=1
            if not self["r"].value != None:
                ArbreB.show(self["fd"],_n)
                ArbreB.show(self["fg"],_n)
    
    def search(self,elem:str):
        """Recherche un element ds un arbre en renvoi son chemin"""
        if type(self) == ArbreB: # 
            return ArbreB.search(self.content,elem)
        elif type(self) == dict:
            if self["r"].value == None: # if Sommet non feuille alors continuer
                g = ArbreB.search(self["fg"], elem)
                d = ArbreB.search(self["fd"], elem)
                if g == True:
                    return "0"
                elif d == True:
                    return "1"
                elif type(g) == str:
                    return "0"+g
                elif type(d) == str:
                    return "1"+d
            elif self["r"].value == elem: # if ce Sommet est la feuille recherchée
                return True
            else:
                return False


##############################################################################################
