def marquer(tab,x,h):
    tab[x] = h

def regle(tab,h):
    m = len(tab)
    if m == 1:
        return tab
    else:
        marquer(tab,int(m//2),h)
        return regle(tab[0:int(m/2)],h-1)+regle(tab[int(m/2):],h-1)

print(regle([0,0,0,0,0,0,0],10))