import random, string


def genere_nom():
    alphabet = string.ascii_lowercase
    nom = ""
    for i in range(6):
        nom += alphabet[random.randint(0,len(alphabet)-1)]
    return(nom)


def pokedex():
    dico = {}
    for i in range(6):
        dico[genere_nom()] = {"atk": random.randint(1,10),"def":random.randint(1,10)}
    return dico


def combat(x:tuple, y:tuple):
    xatq,xdef = x
    yatq,ydef = y
    while xdef > 0 and ydef > 0:
        ydef -= xatq
        if ydef > 0:
            xdef -= yatq
    return((xatq,xdef),(yatq,ydef))


p1 = pokedex()
p2 = pokedex()

while len(p1) > 0 and len(p2) > 0:
    pk1, pk2 = list(p1.keys())[0],list(p2.keys())[0]
    stat1, stat2 = combat((p1[pk1]["atk"],p1[pk1]["def"]),(p2[pk2]["atk"],p2[pk2]["def"]))
    if stat1[1] <= 0:
        del p1[pk1]
        p2[pk2]["def"] = stat2[1]
    elif stat2[1] <= 0:
        del p2[pk2]
        p1[pk1]["def"] = stat1[1]
if len(p1) == 0:
    print("Dresseur 2 à gagné")
elif len(p2) == 0:
    print("Dresseur 1 à gagné")