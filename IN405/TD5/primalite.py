from math import sqrt
from os import getpid
from multiprocessing import Process

def test(n):
    i = 2
    while i <= sqrt(n):
        if n % i == 0:
            return False
        i += 1
    return True

def child_process(a,b):
    print(f"\nChild {getpid()} starting the following task : primalité [{a} ; {b}].\n")
    for i in range(a,b+1):
        print(f"{i} est primaire : {test(i)}")
    print(f"Child {getpid()} ending the following task : primalité [{a} ; {b}].\n")    


if __name__ == "__main__":
    childs = []
    nbr = int(input("Choisir un nombre : "))
    NUM_PROCESS = int(input("Nombre de processus : "))
    for i in range(2,nbr+1,nbr//NUM_PROCESS): # Répartition des tâches aux processus enfants
        a = i
        b = i-1+nbr//NUM_PROCESS if i-1+nbr//NUM_PROCESS < nbr else nbr
        p = Process(target=child_process,args=(a,b))
        p.start()
        childs.append(p)
    for p in childs:
        p.join()
    print(f"\nEND\n")