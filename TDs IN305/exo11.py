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


def fusion(tab1,tab2):
    res = []
    i,j = 0,0
    while i < len(tab1) and j < len(tab2):
        if tab1[i] < tab2[j]:
            res.append(tab1[i])
            i+=1
        else:
            res.append(tab2[j])
            j+=1
    if i < j:
        res += tab1[i:j]
    else:
        res += tab2[j:i]
    return res


def trifusion(tab):
    n = len(tab)//2
    tab1, tab2 = tab[:n],tab[n:]
    trifusion(tab1)
    trifusion(tab2)
    fusion(tab1,tab2)
    return(tab)


def trirapide(tab):
    return(tab)


# initialisation d’un tableau de taille 10 avec des valeurs aléatoires pour vérifier la validité des algos de tris
tab_test=[random.randint(0,20)for i in range(10)]
est_trie(tab_test)
est_trie(triinsertion(tab_test.copy()))
est_trie(triinsertion_dicho(tab_test.copy()))
est_trie(tripermutation(tab_test.copy()))
est_trie(trifusion(tab_test.copy()))
est_trie(trirapide(tab_test.copy()))