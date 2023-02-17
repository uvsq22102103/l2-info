def fibon(n):
    liste = [0,1]
    for i in range(2,n+1):
        liste.append(liste[i-1]+liste[i-2])
    return liste[:n+1]

def fibonG_v1(n):
    for i in fibon(n):
        yield i

def fibonG_v2(n):
    a, b = 0, 1
    for i in range(2,n):
        c = a + b
        a = b
        b = c
        yield c

def fibon_recurcive(n:int,a=0,b=1):
    if n < 3:
        return [a+b]
    else:
        return [a+b]+fibon_recurcive(n-1,b,a+b)

def fibonnacci(n:int):
    return [0,1]+fibon_recurcive(n)

print(fibonnacci(10))
print(fibon(0))