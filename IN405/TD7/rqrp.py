import os
from random import randint
from multiprocessing import Process, Pipe

def child(conn):
    msg = randint(0,100)
    conn.send(msg)
    #wait for response

if __name__ == "__main__":
    liste = []
    n = 3
    for i in range(n):
        parent_conn, child_conn = Pipe()
        liste.append((Process(target = child, args=[child_conn]),parent_conn))
    for (p,conn) in liste:
        p.start()
    for (p,conn) in liste:
        msg = conn.recv()
        print(msg)

