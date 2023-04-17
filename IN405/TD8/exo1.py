import threading
from random import randint

##########
# Thread #

def tg_q2():
    print(entier)

def tg_q3():
    global entier
    entier = randint(0,100)

def tg_q4(liste):
    print(sum(liste)/len(liste))

########
# Main #

def q1():
    t1 = threading.Thread(target=lambda:print("Hello world"),args=[])
    t1.start()
    t1.join()

def q2():
    global entier
    entier = randint(0,100)
    t1 = threading.Thread(target=tg_q2,args=[])
    t1.start()
    t1.join()

def q3():
    t1 = t1 = threading.Thread(target=tg_q3,args=[])
    t1.start()
    t1.join()
    print(entier)

def q4(n:int):
    entiers = [randint(0,100) for i in range(n)]
    t1 = t1 = threading.Thread(target=tg_q4,args=[entiers])
    t1.start()
    t1.join()




#############
# Execution #

#q1()
#q2()
#q3()
#q4(n)