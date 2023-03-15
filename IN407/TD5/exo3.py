liste_originale = ["gyuza","yivbs","bvhu","gyuza","gyuza","gyuza","gyuza","gyuza","bvhu"]

def frequence(liste):
    frequency = {}
    for i in liste:
        if not(i in frequency):
            frequency[i] = 1
        else :
            frequency[i] += 1
    return frequency

def supprime_doublons(liste):
    return list(frequence(liste).keys())

def garde_unique(liste):
    dico = frequence(liste)
    return [key for key in (dico) if (dico[key]) == 1]

print(frequence(liste_originale))
print(supprime_doublons(liste_originale))
print(garde_unique(liste_originale))