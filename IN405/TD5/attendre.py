from os import waitpid, fork, getpid, _exit
from time import sleep
from random import randint

NUM_PROCESS = 10
childs = []

for i in range(NUM_PROCESS):
    pid = fork()
    if pid: # Parent
        childs.append(pid)
    else: # Child
        waiting = randint(0,10)
        sleep(waiting)
        print(f"PID {getpid()} finished after {waiting} sec!")
        _exit(0)

for child in childs:
    waitpid(child, 0)

print("End")