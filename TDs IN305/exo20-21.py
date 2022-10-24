
def carré(n):
    if n == 0:
        return 0
    return carré(n-1)+(2*n)-1

def somme_entiers(n):
    if n == 0:
        return 0
    return somme_entiers(n-1)+n

def est_palindrome(mot):
    if len(mot) <= 1:
        return True
    elif mot[0] == mot[-1]:
        return est_palindrome(mot[1:-1])
    else :
        return False

print(carré(6))
print(somme_entiers(3))
print(est_palindrome("okooasaooko"))