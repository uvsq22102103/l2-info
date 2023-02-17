matrixA = [[2,3],[8,9]]
matrixB = [[5,3],[7,2]]

def somme_matrice(mA:list[list],mB:list[list]) -> list[list]:
    resultat = []
    for i in range(len(mA)):
        resultat.append([])
        for j in range(len(mA[0])):
            resultat[i].append(mA[i][j]+mB[i][j])
    return resultat

def somme_matrice_comprehension(mA,mB):
    return [[mA[i][j]+mB[i][j] for j in range(len(mA[0]))] for i in range(len(mA))]

def paire_matrice_comprehension(mC):
    return[[0 if mC[i][j] % 2 else mC[i][j] for j in range(len(mC[0]))] for i in range(len(mC))]

print(somme_matrice(matrixA,matrixB))
matrixC = somme_matrice_comprehension(matrixA,matrixB)
print(matrixC)
print(paire_matrice_comprehension(matrixC))