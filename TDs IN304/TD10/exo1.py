class Titre:
    def __init__(self,titre:str):
        self.__titre = titre
    
    def getTitre(self):
        return(self.__titre)
    
    def Afficher(self):
        print(self.__titre)


class Annee:
    def __init__(self,annee:int):
        self.__annee = annee

    def getAnnee(self):
        return(self.__annee)
    
    def Afficher(self):
        print(self.__annee)


class CD(Titre,Annee):
    def __init__(self,titre:str,annee:int,nomArtiste:str,nbreTitres:int):
        self.__nomArtiste = nomArtiste
        self.__nbreTitres = nbreTitres
        Titre.__init__(self,titre)
        Annee.__init__(self,annee)

cd1 = CD("Feu de bois",2020,"Damso",11)