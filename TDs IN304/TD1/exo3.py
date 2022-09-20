n = int(input("Nombre de valeurs :  "))
nombres = []
total = 0
for i in range(1,n+1):
    nombres.append(int(input("Valeur ")))
    total += nombres[-1]
#print("Max :",max(nombres),"Min :",min(nombres),"Moyenne :",round(total/n,2))

n = int(input("Factoriel de : "))
total = 1
for i in range(1,n+1):
    total *= i
total, i = 1, 1
while i <= n:
    total *=i
    i += 1
print("Factoriel is",total)

etoiles = ""
n = int(input("Taille du triangle:"))
for i in range (n):
    etoiles += "*"
    print(etoiles)

import random
nombres, paires = [], []
for i in range (100):
    nombres.append(random.randint(100,200))
    if not nombres[-1]%2 and len(paires) < 10:
        paires.append(nombres[-1])
print(paires)