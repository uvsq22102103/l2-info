#!/usr/bin/python3

import argparse
from random import randint
import threading
import time

def init_msg(idx, mailbox, locks, conds):
    time.sleep(1)
    value = randint(1, 100)
    print("%d was selected" % (value))
    mailbox[idx] = value
    locks[idx].acquire()
    conds[idx].notify()
    locks[idx].release()

def transfer_msg(idx, mailbox, locks, conds):
    locks[idx-1].acquire()
    conds[idx-1].wait()
    locks[idx-1].release()
    mailbox[idx] = mailbox[idx-1]
    locks[idx].acquire()
    conds[idx].notify()
    locks[idx].release()

def fini_msg(idx, mailbox, locks, conds):
    locks[idx-1].acquire()
    conds[idx-1].wait()
    locks[idx-1].release()
    print("%d I got" % (mailbox[idx-1]))

if __name__ == '__main__':
    n = 10

    locks = [threading.Lock() for _ in range(n + 1)]
    conds = [threading.Condition(locks[i]) for i in range(n + 1)]
    mailbox = (n + 1) * [0]
    thread_list = [threading.Thread(target=transfer_msg,
                                    args=[i+1, mailbox, locks, conds])
                   for i in range(n)]
    thread_list.append(threading.Thread(target=init_msg,
                                        args=[0, mailbox, locks, conds]))
    thread_list.append(threading.Thread(target=fini_msg,
                                        args=[n+1, mailbox, locks, conds]))

    for elt in thread_list:
        elt.start()
    for elt in thread_list:
        elt.join()