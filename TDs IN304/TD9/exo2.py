from exo1 import *


p1 = Pokemon("Ponita",50)
p2 = Pokemon("Roucoul",32)
p3 = Pokemon("Nosferapti",40)

atq_commune = Attaque("Charge",5,0,20)
p1.ajouter_attaque(atq_commune)
p2.ajouter_attaque(atq_commune)
p3.ajouter_attaque(atq_commune)
p1.ajouter_attaque(Attaque("Belier",10,0,3))
p2.ajouter_attaque(Attaque("Pic-pic",7,0,6))
p3.ajouter_attaque(Attaque("Onde de choc",6,0,12))
