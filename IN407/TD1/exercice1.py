maListe = [19,5,12,8,3,7,2,15]

def PlusGrandElement(l:list):
    m = l[0]
    for i in l[1:]:
        if i > m:
            m = i
    print(m)
    return m

PlusGrandElement(maListe)

def MoyenneElements(l:list):
    somme = 0
    nbr_val = 0
    for i in l:
        nbr_val += 1
        somme += i
    r = somme/nbr_val
    print(r)
    return r

MoyenneElements(maListe)

def PaireImpaire(l:list):
    l_paire = []
    l_impaire = []
    for i in l:
        if i%2 == 1:
            l_impaire.append(i)
        else:
            l_paire.append(i)
    print(f'Liste paire : {l_paire}\nListe impaire : {l_impaire}')
    return l_paire, l_impaire

def Combiner(l1:list,l2:list):
    t1, t2 = len(l1),len(l2)
    listR = []
    for i in range(min(t1,t2)):
        listR.append(l1[i])
        listR.append(l2[i])
    for i in range(min(t1,t2),max(t1,t2)):
        if t1 > t2:
            listR.append(l1[i])
        else:
            listR.append(l2[i])
    print(listR)
    return listR

l1,l2 = PaireImpaire(maListe)
listR = Combiner(l1,l2)
listR2 = [i for i in listR] # avec ce type de recopiage les liste ne sont pas reliées en mémoire.
print(f'\nlistR : {listR}\nlistR2 : {listR2}')
listR[0] = 0
print(f'\nlistR : {listR}\nlistR2 : {listR2}')