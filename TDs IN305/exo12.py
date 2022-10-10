# Complexité : O(n**2) pour itératif.
# Complexité : C(n,g) = n-g +1+C(n,g+1) à résoudre pour récursif.

def min_pos(tab,g,d):
    # O(n-g)
    pos = g
    m = tab[g]
    for i in range(g,d):
        if m > tab[i]:
            m = tab[i]
            pos = i
    return pos

def pos(tab,g,d):
    pos_min,pos_max = g,g
    mini,maxi = tab[g], tab[g]
    for i in range(g,d):
        if mini > tab[i]:
            mini = tab[i]
            pos_min = i
        elif maxi < tab[i]:
            maxi = tab[i]
            pos_max = i
    return pos_min,pos_max

def deplacer(tab,p,d):
    tab[p], tab[d] = tab[d], tab[p]

def tri_selection_Rs(tab,g=0):
    if len(tab[g:]) > 1:
        p = min_pos(tab,g,len(tab))
        deplacer(tab,p,g)
        tri_selection_Rs(tab,g+1)
    return tab

def tri_selection_Is(tab):
    for i in range(len(tab)):
        p = min_pos(tab,i,len(tab))
        deplacer(tab,p,i)
    return tab

def tri_selection_I(tab):
    g, d = 0, len(tab)-1
    while g < d:
        pos_min,pos_max = pos(tab,g,d)
        deplacer(tab,pos_min,g)
        deplacer(tab,pos_max,d)
        g += 1
        d -= 1
    return tab

def denombrement(tab):
    output = [0]*(max(tab)+1)
    for i in tab:
        output[i] += 1
    return output


l = [6,1,4,2,1,1,0,1,3,6,4]
#print("\nTri selection Récursif simple:",tri_selection_Rs(l.copy()))
#print("Tri selection Itératif simple:",tri_selection_Is(l.copy()))
#print("Tri selection Itératif MinMax:",tri_selection_I(l.copy()))
print(denombrement(l.copy()))