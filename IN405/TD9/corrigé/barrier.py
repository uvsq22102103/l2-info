#!/usr/bin/python3

import argparse
from random import randint
import threading
import time

class MyBarrier:
    def __init__(self, num_threads):
        self.orig_num_threads = num_threads
        self.num_threads = num_threads
        self.lock = threading.Lock()
        self.cond = threading.Condition(self.lock)

    def reset(self):
        self.num_threads = self.orig_num_threads

def random_sleep_then_barrier(barrier):
    for _ in range(2):
        time.sleep(randint(1,5))
        print("%d is awakened" % (threading.get_ident()))
        barrier.lock.acquire()
        print("%d in the mutex" % (threading.get_ident()))
        barrier.num_threads -= 1
        if barrier.num_threads == 0:
            print("%d will notify them all" % (threading.get_ident()))
            barrier.reset()
            barrier.cond.notify_all()
        else:
            barrier.cond.wait()
            print("%d just notified" % (threading.get_ident()))
        barrier.lock.release()

if __name__ == '__main__':
    AP = argparse.ArgumentParser()
    AP.add_argument('nb_threads', type=int)
    args = AP.parse_args()

    b = MyBarrier(args.nb_threads)
    thread_list = [threading.Thread(target=random_sleep_then_barrier,
                                    args=[b]) for _ in range(args.nb_threads)]

    for elt in thread_list:
        elt.start()
    for elt in thread_list:
        elt.join()