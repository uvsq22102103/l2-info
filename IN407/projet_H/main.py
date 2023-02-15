from classes.arbreb import ArbreB
from classes.sommet import Sommet
from fonctions import *

chr_p = proportions("test.txt")
liste_arbres = [ArbreB(Sommet(e,v)) for v,e in chr_p]
for abr in liste_arbres:
    print(abr.content)
