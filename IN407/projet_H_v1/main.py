from fonctions import proportions, merger
from classes import ArbreB, Sommet

characters_proportions, characters = proportions("test.txt")
liste_arbres = [ArbreB(Sommet(e,v)) for v,e in characters_proportions]
arborescence = merger(liste_arbres)
#arborescence.show()
#arborescence.search(chr)
print(characters)