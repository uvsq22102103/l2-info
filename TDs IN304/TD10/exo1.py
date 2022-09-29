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
    
    def Afficher(self):
        print(self.__nomArtiste+" : "+Titre.getTitre(self)+" ; %d titres ; sorti en %d"%(self.__nbreTitres,Annee.getAnnee(self)))


class DVD(Titre,Annee):
    def __init__(self,titre:str,annee:int,realisateur:str):
        self.__real = realisateur
        Titre.__init__(titre)
        Annee.__init__(annee)
    
    def Afficher(self):
        print("Nom : "+Titre.getTitre(self)+"; réalisateur "+self.__real+" ; Parution en %d"%Annee.getAnnee(self))


cd1 = CD("Feu de bois",2020,"Damso",11)
dvd1 = DVD("Intouchables",2012,"Patrick MURET")
dvd1.Afficher()
cd1.Afficher()