nombre = 10
suite_fibo = [0,1]


def suite_fibonacci(suite,n):
    if len(suite) < n:
        suite.append(suite[-1]+suite[-2])
        suite_fibonacci(suite,n)
    else:
        print("Suite de Fibonacci : ",suite,"\nU%d : %d" % (n ,suite[-1]))
        return(suite[-1])


def factorielle(n_objectif,n_actuel=1,total=1):
    if n_objectif > n_actuel:
        n_actuel += 1
        total *= n_actuel
        factorielle(n_objectif,n_actuel,total)
    else:
        print("Factoriel de %d est %d" % (n_objectif, total))
        return(total)


def diviseur_commun(a,b,nb=2,dc=[]):
    """a >= b"""
    if nb <= b:
        if a % nb == 0 and b % nb == 0:
            dc.append(nb)
        diviseur_commun(a,b,nb+1,dc)
    else:
        print("Plus Grand Diviseur Commun de %d et %d est %d" %(a,b,dc[-1]))
        return(dc[-1])


def pyramide_inversee(n,s):
    if n > 0:
        print(n*str(s))
        pyramide_inversee(n-1,s)


def calcul_xn(x,n,total=1):
    if n > 0:
        total *= x
        calcul_xn(x,n-1,total)
    else:
        print(total)
        return(total)


for i in range(nombre-1):
    suite_fibo.append(suite_fibo[-1]+suite_fibo[-2])
    assert suite_fibo[-1] >= suite_fibo[-2]
print("Suite de Fibonacci : ",suite_fibo,"\nU%d : %d" % (nombre ,suite_fibo[-1]))

while (nombre) >= len(suite_fibo):
    suite_fibo.append(suite_fibo[-1]+suite_fibo[-2])
    assert suite_fibo[-1] >= suite_fibo[-2]
print("Suite de Fibonacci : ",suite_fibo,"\nU%d : %d" % (nombre ,suite_fibo[-1]))

suite_fibonacci(suite_fibo,nombre)
factorielle(10)
diviseur_commun(852,366)
pyramide_inversee(5,"Jack")
calcul_xn(2,2)