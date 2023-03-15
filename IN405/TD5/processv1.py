from multiprocessing import Process, Pipe
from random import randint
from os import getpid, getppid

def hello(name:str, conn=None):
    print(name+f"\nSelf PID: {getpid()}\nParent PID: {getppid()}")
    if name == "ENFANT":
        nbr = randint(0,100)
        conn.send(nbr)
    elif name == "PARENT":
        print(f"Child PID: {child_pid}")
        nbr = conn.recv()
    print(f"Number: {nbr}\n")


if __name__ == "__main__":
    conn1, conn2 = Pipe(False)
    process = Process(target=hello,args=("ENFANT",conn2,))
    process.start()
    child_pid = process.pid
    process.join()
    hello("PARENT",conn1)
    conn1.close()
    conn2.close()