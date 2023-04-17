import threading

def increment(value:list):
    for _ in range(10):
        lock.acquire()
        value[0] += 1
        lock.release()

if __name__ == "__main__":
    value = [0]
    lt = []
    n = 20
    lock = threading.Lock()
    for _ in range(n):
        lt.append(threading.Thread(target=increment, args=[value]))
    for t in lt:
        t.start()
    for t in lt:
        t.join()
    print(value[0])