mot = "tagada"

def occurence(chaine):
    dictionnaire = {}
    for i in chaine:
        dictionnaire[i] = 1
    print(dictionnaire)
    return(dictionnaire)


occurence(mot)