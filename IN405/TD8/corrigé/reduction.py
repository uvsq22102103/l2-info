#!/usr/bin/python3

import argparse
from random import randint
import sys
import threading

def reduction_sum(array, start, end, idx, res):
    tmp = 0
    for elt in array[start:end]:
        tmp += elt
    res[idx] = tmp

def reduction_avg(array, start, end, idx, res):
    raise NotImplementedError

def reduction_max(array, start, end, idx, res):
    raise NotImplementedError

def reduction_min(array, start, end, idx, res):
    raise NotImplementedError

AP = argparse.ArgumentParser()

AP.add_argument('num_threads', type=int)
AP.add_argument('array_size', type=int)
AP.add_argument('opcode', choices=['+', '/', 'M', 'm'])

OPCODE_TO_FUNC = {
    '+': reduction_sum,
    '/': reduction_avg,
    'M': reduction_max,
    'm': reduction_min,
}

args = AP.parse_args(sys.argv[1::])

array = [randint(1, 100) for _ in range(args.array_size)]
print(array)

res = args.num_threads * [0]
thread_list = [threading.Thread(target=OPCODE_TO_FUNC[args.opcode],
                                args=(array,
                                      round(i * args.array_size / args.num_threads),
                                      round((i + 1) * args.array_size / args.num_threads),
                                      i,
                                      res))
               for i in range(args.num_threads)]

for thread in thread_list:
    thread.start()
for thread in thread_list:
    thread.join()

print(sum(res))