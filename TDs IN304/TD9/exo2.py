from exo1 import *


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
        print("Le dresseur "+self.nom+" à %d xp et %d niv\nPokémons"%(self.xp,self.niveau))
        for pokemon in self.pokemons:
            pokemon.Afficher_pokemon()

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
#Afficher pokémons###############################
p1.Afficher_pokemon()
p2.Afficher_pokemon()
p3.Afficher_pokemon()
#Dresseurs################
d1 = Dresseur("Vaillant")
d2 = Dresseur("Papy sportif")
d1.Ajout_pokemon(p1)
d1.Ajout_pokemon(p2)
d1.Ajout_pokemon(p3)
d2.Ajout_pokemon(p1)
d2.Ajout_pokemon(p2)
d2.Ajout_pokemon(p3)
#Afficher dresseur########
d1.Afficher_dresseur()