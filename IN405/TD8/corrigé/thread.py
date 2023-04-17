#!/usr/bin/python3

import queue
import random
import threading

def print_hello():
    print('Hello World!')

def print_number(a):
    print(a)

def gen_and_print(queue):
    rand_number = random.randint(1, 100)
    print(rand_number)
    queue.put(rand_number)

def print_avg(tab):
    print(sum(tab)/len(tab))

if __name__ == '__main__':
    rand_number = random.randint(1, 100)
    queue = queue.Queue()
    tab = [random.randint(1, 100) for _ in range(10)]

    tl = [
        threading.Thread(target=print_hello),
        threading.Thread(target=print_number, args=[rand_number]),
        threading.Thread(target=gen_and_print, args=[queue]),
        threading.Thread(target=print_avg, args=[tab])
    ]

    print("[PRT] Generated number: %d" % (rand_number))

    for t in tl:
        t.start()

    for t in tl:
        t.join()

    print("[PRT] Generated number by child: %d" % (queue.get()))