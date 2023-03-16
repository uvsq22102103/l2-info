#!/usr/bin/python3

import argparse
import csv
from random import randint
import sys

def fifo_routine(dataframe):
    """
    input: dataframe -- dictionary of process information
    output: total_time
    """
    total_time = 0
    for process in dataframe:
        print(f"{process['name']} started")
        total_time+=process["duration"]
    return total_time

def random_routine(dataframe):
    """
    input: dataframe -- dictionary of process information
    output: total_time
    """
    total_time = 0
    while (size := len(dataframe)) > 0:
        tirage = randint(0,size-1)
        print(f"{dataframe[tirage]['name']} started")
        total_time += dataframe[tirage]["duration"]
        del dataframe[tirage]
    return total_time

def priority_fifo_routine(dataframe:list):
    """
    input: dataframe -- dictionary of process information
    output: total_time
    """
    dataframe.sort(key= lambda x : x["priority"])
    total_time = 0
    for process in dataframe:
        print(f"{process['name']} started")
        total_time+=process["duration"]
    return total_time

def round_robin_routine(dataframe):
    """
    input: dataframe -- dictionary of process information
    output: total_time
    """
    total_time = 0
    while (size := len(dataframe)) > 0:
        offset = 0
        for i in range(size):
            i -= offset
            print(f"started {dataframe[i]}")
            dataframe[i]["duration"] -= 2
            total_time += 2
            if (duration := dataframe[i]["duration"]) <= 0:
                total_time += duration
                print(f"ended {dataframe[i]}")
                del dataframe[i]
                offset += 1
            print(f"time elapsed : {total_time}")
    return total_time

def supra_optimal_routine(dataframe):
    """
    input: dataframe -- dictionary of process information
    output: list of executed process for each time quantum
    """
    raise NotImplementedError

# DO NOT MODIFY THE PART BELOW

if __name__ == '__main__':
    NAME_TO_FUNC = {
        "fifo": fifo_routine,
        "random": random_routine,
        "priority": priority_fifo_routine,
        "quantum": round_robin_routine,
        "ultra": supra_optimal_routine
    }

    # Command line parsing, execute `./scheduler.py -h` for more information
    AP = argparse.ArgumentParser()
    AP.add_argument('algo', help='algorithm to use',
                    choices=NAME_TO_FUNC.keys())
    AP.add_argument('input', help='input file, in csv format')
    args = AP.parse_args(sys.argv[1::])

    process_list = []

    # Input file parsing
    with open(args.input, newline='') as csv_file:
        reader = csv.reader(csv_file, delimiter=';')
        # Each row is composed of 4 columns:
        # process name, start time, duration time and priority (lower is better)
        for row in reader:
            if row[0][0] == '#':
                continue
            # You can access to the start field of the 2nd item using:
            # process_list[1]['start']
            process_list.append({
                'name': row[0],
                'start': int(row[1]),
                'duration': int(row[2]),
                'priority': int(row[3]),
            })

    # Sort the list by start time
    process_list.sort(key=lambda x: x['start'])

    # Call the scheduling routine
    clock = NAME_TO_FUNC[args.algo](process_list)

    print("Total time for the given execution: %ds" % (clock))