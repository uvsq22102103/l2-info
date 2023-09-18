import threading

total = [0]

def somme():
    lock.acquire()
    total[0] += 1
    lock.release()

n = int(input("Nombre de threads : "))

lock = threading.Lock()
threads = [threading.Thread(target=somme) for _ in range(n)]
for _ in threads:
    _.start()
for _ in threads:
    _.join()

print(total[0])