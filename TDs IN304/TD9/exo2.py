from exo1 import *
import random


class Dresseur:
    def __init__(self,nom):
        self.nom = nom
        self.niveau = 0
        self.xp = 0
        self.pokemons = []
    
    def Ajout_pokemon(self,pokemon):
        if pokemon not in self.pokemons:
            self.pokemons.append(pokemon)
            print(pokemon.nom+" a été ajouté à l'équipe de "+self.nom)
        else:
            print(pokemon.nom+" fait déjà partie de votre équipe")
    
    def Afficher_dresseur(self):
        print("\nLe dresseur "+self.nom+" à %d xp et %d niv\nPokémons"%(self.xp,self.niveau))
        for pokemon in self.pokemons:
            pokemon.Afficher_pokemon()
    
    def Taverne(self):
        for pokemon in self.pokemons:
            pokemon.Soigner_pokemon()
        print("Le dresseur "+self.nom+" a fait un petit tour à la Taverne pour soigner ses pokémons")
    
    def Update(self):
        while self.xp >= 10:
            self.xp -= 10
            self.niveau += 1
            print("Le dresseur "+self.nom+" est maintenant au niveau %d"%self.niveau)
    
    def Defi_aleatoire(self,cible):
        self.Taverne()
        cible.Taverne()
        gagnant = random.choice(self.pokemons).Scenario2(random.choice(cible.pokemons))
        if gagnant in cible.pokemons:
            cible.xp +=1
            cible.Update()
            print("Le dresseur "+cible.nom+" a gagné")
            return(cible)
        elif gagnant in self.pokemons:
            self.xp +=1
            self.Update()
            print("Le dresseur "+self.nom+" a gagné")
            return(self)
    
    def Arene1(self,dresseur2):
        for i in range(100):
            self.Defi_aleatoire(dresseur2)
        score1,score2 = self.niveau+self.xp/10,dresseur2.niveau+dresseur2.xp/10
        self.Afficher_dresseur()
        dresseur2.Afficher_dresseur()
        if score1 > score2:
            print("\nLe dresseur "+self.nom+" à gagné Arène1 !")
            return(self)
        elif score1 < score2:
            print("\nLe dresseur "+dresseur2.nom+" à gagné Arène1 !")
            return(dresseur2)
        else:
            print("Egalité parfaite dans Arène1 !")


#Génération des pokémons#####
p1 = Pokemon("Ponita",50)
p2 = Pokemon("Roucoul",32)
p3 = Pokemon("Nosferapti",40)
#Attaque de base############################
p1.ajouter_attaque(Attaque("Charge",5,20))
p2.ajouter_attaque(Attaque("Charge",5,20))
p3.ajouter_attaque(Attaque("Charge",5,20))
#Attaques spéciales##############################
p1.ajouter_attaque(Attaque("Belier",10,3))
p1.ajouter_attaque(Attaque("Flammèche",12,8))
p2.ajouter_attaque(Attaque("Pic-pic",7,6))
p2.ajouter_attaque(Attaque("Crue-aile",11,8))
p3.ajouter_attaque(Attaque("Onde de choc",6,12))
p3.ajouter_attaque(Attaque("Vive-attaque",12,8))
#Dresseurs################
d1 = Dresseur("Vaillant")
d2 = Dresseur("Papy sportif")
d1.Ajout_pokemon(p1)
d1.Ajout_pokemon(p2)
d2.Ajout_pokemon(p3)
#Afficher dresseur########
d1.Afficher_dresseur()
d2.Afficher_dresseur()
#Combats###############
d1.Arene1(d2)