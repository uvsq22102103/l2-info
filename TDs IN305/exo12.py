
from tkinter.tix import Tree


def tri_selection(tab:list,p=0):
    tab[tab.index(min(tab))],tab[p] = tab[p],tab[tab.index(min(tab))]
    p += 1
    tri_selection()