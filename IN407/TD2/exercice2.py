from itertools import zip_longest

liste_noms = ["Aymeric", "Cyriac", "Elicopter", "Raphaëlo", "Ruben", "Ziak"]
liste_longueur = [len(i) for i in liste_noms]
print(liste_longueur)

def longest_nameV1(liste_longueur:list, liste_noms:list):
    r2 = [""]
    for i in range(len(liste_noms)):
        if liste_longueur[i] > len(r2[0]):
            r2 = [liste_noms[i]]
        elif liste_longueur[i] == len(r2[0]):
            r2.append(liste_noms[i])
    print(f"V1 : {r2}")

def longest_nameV2(liste_longueur:list, liste_noms:list):
    indices = [0]
    for i,j in enumerate(liste_longueur):
        if j > liste_longueur[indices[0]]:
            indices = [i]
        elif j == liste_longueur[indices[0]] and i != indices[0]:
            indices.append(i)
    print(f"V2 : {[liste_noms[i] for i in indices]}")

def longest_nameV3(liste_longueur:list, liste_noms:list):
    r = [(0,"")]
    for i in zip(liste_longueur,liste_noms):
        if i[0] > r[0][0]:
            r = [i]
        elif i[0] == r[0][0]:
            r.append(i)
    print(f"V3 : {[i[1] for i in r]}")


longest_nameV1(liste_longueur, liste_noms)
longest_nameV2(liste_longueur, liste_noms)
longest_nameV3(liste_longueur, liste_noms)

liste_noms = ["Cecilia", "Lise", "Marie"]
liste_longueur = [7, 4, 5]

longest_nameV1(liste_longueur, liste_noms)
longest_nameV2(liste_longueur, liste_noms)
longest_nameV3(liste_longueur, liste_noms)

liste_noms = ["Cecilia", "Lise", "Marie", "Rosaline"]
liste_longueur = [7, 4, 5]

for i,j in zip_longest(liste_noms,liste_longueur,fillvalue=None):
    if j == None:
        j = len(i)
    print(i,j)