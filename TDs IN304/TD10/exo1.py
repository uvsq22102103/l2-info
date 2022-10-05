
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
        print("CD :",self.__nomArtiste,Titre.getTitre(self),self.__nbreTitres,Annee.getAnnee(self))


class DVD(Titre,Annee):
    def __init__(self,titre:str,annee:int,realisateur:str):
        self.__real = realisateur
        Titre.__init__(self,titre)
        Annee.__init__(self,annee)
    
    def Afficher(self):
        print("DVD :",Titre.getTitre(self),self.__real,Annee.getAnnee(self))

    def getReal(self):
        return(self.__real)


class Collection():
    def __init__(self):
        self.collection = []
        print("\nUne collection a été créée\n")
    
    def Ajout(self,objet):
        if objet not in self.collection:
            self.collection.append(objet)
    
    def Afficher(self):
        print("Début collection<")
        for objet in self.collection:
            objet.Afficher()
        print(">Fin collection")
    
    def Rechercher_titre(self,titre:str):
        print("Recherche par titre : ")
        titres = [i.getTitre() for i in self.collection]
        try :
            self.collection[titres.index(titre)].Afficher()
        except ValueError:
            print("Le titre '"+titre+"' n'est pas dans la collection")

    def Rechercher_annee(self,annee:int):
        print("Recherche pour %d:"%annee)
        annees = [i.getAnnee() for i in self.collection]
        for i in range(len(annees)):
            if annees[i] == annee:
                self.collection[i].Afficher()
        print("Fin recherche")
    
    def Recherche_real_annee(self,real:str,annee:int):
        print("Recherche "+real+"/%d :"%annee)
        for i in self.collection:
            if isinstance(i, DVD):
                if i.getAnnee() == annee and i.getReal() == real:
                    i.Afficher()
        print("Fin recherche")


cd1 = CD("Feu de bois",2020,"Damso",11)
dvd1 = DVD("Intouchables",2012,"Patrick MURET")
cd1.Afficher()
dvd1.Afficher()
Armoire = Collection()
Armoire.Ajout(cd1)
Armoire.Ajout(dvd1)
Armoire.Afficher()
Armoire.Rechercher_titre(cd1.getTitre())
Armoire.Rechercher_titre("Adieu bientôt")
Armoire.Rechercher_annee(2020)
Armoire.Rechercher_annee(2012)
Armoire.Recherche_real_annee("Patrick MURET",2012)