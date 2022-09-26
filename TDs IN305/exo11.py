import random, time


def recherche_pos(tab,elem,fin):
    for i in range(fin):
        if elem < tab[i]:
            return i
    return fin


def triinsertion(tab):
    for i in range(0,len(tab)):
        elem = tab[i]
        pos = recherche_pos(tab,elem,i)
        for j in range(i-1,pos-1,-1):
            tab[j+1] = tab[j]
        tab[pos] = elem
    return(tab)


def est_trie(tab):
    for i in range(len(tab)-1):
        if tab[i] > tab[i+1]:
            tri = False
            break
        else:
            tri = True
    if tri:
        print("tableau trié : ",tab)
    else:
        print("tableau pas trié : ",tab)


def recherche_pos_dicho(tab,elem,fin):
    debut = 0
    while debut != fin:
        milieu = (debut + fin)//2
        if tab[milieu] < elem:
            debut = milieu + 1
        else:
            fin = milieu 
    return fin 


def triinsertion_dicho(tab_test):
    #identique a triinsertion, avec une recherche de pose différente
    for i in range(1,len(tab_test)):
        pos = i
        elem = tab_test[i]
        pos = recherche_pos_dicho(tab_test,elem,i-1)
        for j in range(i-1,pos-1,-1):
                tab_test[j+1] = tab_test[j]
                tab_test[pos] = elem
    return tab_test


def tripermutation(tab):
    for tc in range(1,len(tab)+1):
        for i in range(len(tab)-1,tc-1,-1):
            if tab[i-1] > tab[i]:
                tab[i-1],tab[i] = tab[i],tab[i-1]
    return(tab)


def fusion(tab:list,p,q,r):
    res = tab.copy()
    i,k,j = p,p,q+1
    while i <= q and j <= r:
        if tab[i] < tab[j]:
            res[k] = tab[i]
            i+=1
        else:
            res[k] = tab[j]
            j+=1
        k+=1
    while i <= q:
        res[k] = tab[i]
        i+=1
        k+=1
    while j <= r:
        res[k] = tab[j]
        j+=1
        k+=1
    tab[:] = res.copy()


def trifusion(tab,p,r):
    if p < r :
        q = (p+r)//2
        trifusion(tab,p,q)
        trifusion(tab,q+1,r)
        fusion(tab,p,q,r)
    return(tab)


def partitionner(tab,p,r):
    i,j,pivot = p,r,tab[p]
    while i < j:
        while tab[i] < pivot:
            i+=1
        while tab[j] > pivot:
            j-=1
        if i < j:
            tab[i],tab[j] = tab[j],tab[i]
            i+=1
            j-=1
    return j


def trirapide(tab,p,r):
    if p < r:
        q = partitionner(tab,p,r)
        trirapide(tab,p,q)
        trirapide(tab,q+1,r)
    return(tab)


# initialisation d’un tableau de taille 10 avec des valeurs aléatoires pour vérifier la validité des algos de tris
tab_test=[random.randint(0,20)for i in range(10)]
est_trie(tab_test)
est_trie(triinsertion(tab_test.copy()))
est_trie(triinsertion_dicho(tab_test.copy()))
est_trie(tripermutation(tab_test.copy()))
est_trie(trifusion(tab_test.copy(),0,9))
est_trie(trirapide(tab_test.copy(),0,9))