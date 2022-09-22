carre_mag = [[1,8,11,14],[15,10,5,4],[6,3,16,9],[12,13,2,7]]
carre_pas_mag = [[10,8,11,14],[15,10,5,4],[6,3,16,9],[12,13,2,7]]


def affiche_carre(carre):
    for i in carre:
        print(i)


def test_lignes(carre):
    somme = 0
    for i in carre:
        somme += sum(i)
    if not somme % 4:
        print("Lignes magiques")
        return(somme//4)
    else:
        print("Lignes pas magiques")
        return(-1)


def test_colonne(carre):
    somme = 0
    for i in range(len(carre)):
        for j in range(len(carre)):
            somme += carre[j][i]

affiche_carre(carre_mag)
test_lignes(carre_pas_mag)