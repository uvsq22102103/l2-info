import string, random, time
portefeuille = {"capital":100000}


def genere_titre():
    alphabet = string.ascii_lowercase
    lettres = ""
    for i in range(3):
        lettres += alphabet[random.randint(0,len(alphabet)-1)]
    return(lettres)


def genere_cours():
    return(random.uniform(0.0,500.0))


def achat(x):
    n,v = genere_titre(),genere_cours()
    if x*v <= portefeuille["capital"]:
        portefeuille[n] = {"nombre":x,"cours":v}
        portefeuille["capital"] -= x*v
    else:
        print("achat impossible, votre capital n'est pas suffisant")


def variation():
    for action in portefeuille.keys():
        if action != "capital":
            portefeuille[action]["cours"] *= random.uniform(0.5,2)


def valeur():
    total = 0
    for action in portefeuille.keys():
        if action != "capital":
            total += portefeuille[action]["nombre"]*portefeuille[action]["cours"]
    print(total)


for i in range(10):
    achat(1)

for i in range(30):
    valeur()
    variation()
    time.sleep(1)
