import threading
import time

def debut(idx, locks, conds, mailbox):
    time.sleep(1)
    print(f"{threading.get_ident()} sended a mail.")
    mailbox[idx] = "Bonjour Obama"
    locks[idx].acquire()
    conds[idx].notify()
    locks[idx].release()

def transmission(idx, locks, conds, mailbox):
    locks[idx-1].acquire()
    conds[idx-1].wait()
    locks[idx-1].release()
    print(f"{threading.get_ident()} wake up.")
    mailbox[idx] = mailbox[idx-1]
    locks[idx].acquire()
    conds[idx].notify()
    locks[idx].release()

def fin(idx, locks, conds, mailbox):
    locks[idx].acquire()
    conds[idx].wait()
    locks[idx].release()
    print(f"{threading.get_ident()} receved a mail : {mailbox[idx-1]}")

n = 10

mailbox = [0] * (n+1)
locks = [threading.Lock() for i in range(n+1)]
conds = [threading.Condition(locks[i]) for i in range(n+1)]
threads = []
for idx in range(n):
    threads.append(threading.Thread(target=transmission, args=[idx+1, locks, conds, mailbox]))
threads.append(threading.Thread(target=debut, args=[0, locks, conds, mailbox]))
threads.append(threading.Thread(target=fin, args=[n, locks, conds, mailbox]))
for t in threads:
    t.start()

for t in threads:
    t.join()