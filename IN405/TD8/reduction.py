import sys
import threading
from random import randint

def somme(id, a, b):
    total = 0
    for i in range(a, b):
        total += tab[i]
    res[id] = total

def moyenne(id, a, b):
    total = 0
    for i in range(a, b):
        total += tab[i]
    res[id] = total/(b-a)

def maximum(id, a, b):
    print(tab[a:b])
    res[id] = max(tab[a:b])

def minimum(id, a, b):
    res[id] = min(tab[a:b])


if __name__ == "__main__":
    
    OPCODE = {"+": somme,
              "/": moyenne,
              "M": maximum,
              "m": minimum}
    
    args = sys.argv[1::] # m n opcode
    m = int(args[0]) # nbr de thread
    n = int(args[1]) # taille du tableau
    opcode = args[2] # définit l'action à mener sur le tableau
    res = [0] * m # liste resultats
    lt = [] # liste thread
    tab = [randint(0,100) for _ in range(n)]
    offset = n // m
    reste = n % m
    for i in range(m):
        a = offset*i
        b = offset*(i+1) if i!=m-1 else offset*(i+1)+reste
        print(a,b)
        lt.append(threading.Thread(target=OPCODE[opcode], args=[i,a,b]))
    
    for thread in lt:
        thread.start()
    for thread in lt:
        thread.join()
    
    print(res)

    if opcode == "+":
        print(sum(res))
    elif opcode == "/":
        print(sum(res)/len(res))
    elif opcode == "M":
        print(max(res))
    elif opcode == "m":
        print(min(res))