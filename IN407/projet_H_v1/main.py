from fonctions import proportions, merger
from classes import ArbreB, Sommet

chr_p = proportions("test.txt")
liste_arbres = [ArbreB(Sommet(e,v)) for v,e in chr_p]
arborescence = merger(liste_arbres)
arborescence.show()
print(arborescence.search("t"))