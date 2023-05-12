#!/usr/bin/python3

import argparse
import threading

lock = threading.Lock()

def count(counter):
    for _ in range(10):
        lock.acquire()
        counter[0] += 1
        lock.release()

if __name__ == '__main__':
    AP = argparse.ArgumentParser()
    AP.add_argument('nb_threads', type=int)

    args = AP.parse_args()

    counter = [0]
    thread_list = [threading.Thread(target=count, args=[counter]) for _ in range(args.nb_threads)]

    for thread in thread_list:
        thread.start()
    for thread in thread_list:
        thread.join()

    print(counter[0])