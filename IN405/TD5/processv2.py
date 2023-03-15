from os import getpid, getppid, fork, pipe, close, fdopen
from random import randint
r, w = pipe()
pid = fork() # au dessus du fork c'est uniquement exécuté en Parent. Ce qui fait de r et w des variables identiques dans P et C mais pas liées.
if pid > 0: # Running from Parent
    close(w)
    nbr = str(fdopen(r).read())
    print(f"PARENT\nSelf PID: {getpid()}\nParent PID: {getppid()}\nChild PID: {pid}\nNumber: {nbr}\n")
elif pid == 0: # Running from Child
    nbr = randint(0,100)
    close(r)
    w = fdopen(w,'w')
    w.write(str(nbr))
    w.close
    print(f"ENFANT\nSelf PID: {getpid()}\nParent PID: {getppid()}\nNumber: {nbr}\n")