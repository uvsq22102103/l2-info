def gen_entier(n:int):
    """Générateur de 1 à N non inclus"""
    for i in range(1,n):
        yield i

def gen_carre(liste:list[int]):
    """renvoi le carré des éléments de la liste"""
    for i in liste:
        yield i**2

def gen_negatif(liste:list[int]):
    for i in liste:
        yield -i

liste = [1,2,3,4,5,6,7,8,9]

for i in gen_entier(10):
    print(i)
for i in gen_carre(liste):
    print(i)
for i in gen_negatif(liste):
    print(i)