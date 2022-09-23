import string, random


def groupage(eleves:list,n):
    g = int(len(eleves)/n)+1 # doit être conditionnel
    groupes = []
    while len(eleves) >= g:
        groupes.append([])
        l = len(groupes)-1
        for i in range(g):
            e = random.choice(eleves)
            eleves.remove(e)
            groupes[l].append(e)
    groupes.append(eleves)
    return(groupes)
    



nb_etudiants = 15
etudiants = list(string.ascii_lowercase[:nb_etudiants])
print(etudiants)
print(groupage(etudiants,5))