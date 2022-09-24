mot = "tagada"
mots = ['eddard', 'catelyn', 'robb', 'sansa', 'arya', 'brandon', 'rickon', 'theon', 'rorbert', 'cersei', 'tywin',
'jaime', 'tyrion', 'shae', 'bronn', 'lancel', 'joffrey', 'sandor', 'varys', 'renly']

def occurence(chaine):
    dictionnaire = {}
    for i in chaine:
        if i in dictionnaire.keys():
            dictionnaire[i] += 1
        else:
            dictionnaire[i] = 1
    print(dictionnaire)
    return(dictionnaire)


def mots_position1(liste:list,let,pos):
    output = []
    for mot in liste:
        if let == mot[pos]:
            output.append(mot)
    liste.clear()
    for mot in output:
        liste.append(mot)


def mots_position2(liste:list,let,pos):
    output = [mot for mot in liste if let == mot[pos]]
    liste.clear()
    for mot in output:
        liste.append(mot)


def mots_position3(dico:dict,let,pos):
    return(dico[(pos,let)])


def dictionnaire_new(liste:list):
    dictionnaire = {}
    for mot in liste:
        for i in range(len(mot)):
            p_l = (i,mot[i])
            if p_l in dictionnaire.keys():
                dictionnaire[p_l].append(mot)
            else:
                dictionnaire[p_l] = [mot]
    return(dictionnaire)


#occurence(mot)
#print(mots)
#mots_position2(mots,"e",1)
#print(mots)
dico = dictionnaire_new(mots)
#print(dico)
recherche = mots_position3(dico,"a",1)
print(recherche)