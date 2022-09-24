import random


def tirage_entiers(dictionnaire):
    nb = random.randint(-5,5)
    if nb >= 0:
        dictionnaire["positif"].append(nb)
    else:
        dictionnaire["négatif"].append(nb)


def carre_cube(dictionnaire):
    carre = [i**2 for i in dictionnaire["positif"]]
    cube = [i**3 for i in dictionnaire["négatif"]]
    print(carre,cube)
    return([carre,cube])


dico = {
    "nom" : "toto",
    "prénom" : "titi",
    "adresse" : "guyancourt",
    "age" : 20
}
print(dico)
dico["age"] = 19
print(dico)
del dico["age"]
print(dico)
nom = dico.get("nom")
keys = dico.keys()
if "prénom" in keys:
    print("Clée 'prénom' présente")
if "age" in keys:
    print("Clée 'age' présente")
values = dico.values()
items = dico.items()
print(keys)
print(values)
print(items)
liste1 = [random.randint(0,10) for i in range(10)]
liste2 = [i for i in range(-10,0,1)]
entiers = {
    "positif":liste1,
    "négatif":liste2
}
print(liste1)
print(liste2)
print(entiers)
tirage_entiers(entiers)
print(entiers)
carre_cube(entiers)