from fonctions import proportions, merger
from classes import ArbreB, Sommet

characters_proportions = proportions("test.txt")
liste_arbres = [ArbreB(Sommet(e,v)) for v,e in characters_proportions]
print(characters_proportions)
arborescence = merger(liste_arbres)
#arborescence.show()
#arborescence.search(chr)
#arborescence.get_characters()
#arborescence.get_encode()