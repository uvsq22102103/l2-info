import threading, random

def search_negatif(data, i_start, i_stop, event:threading.Event):
    print(threading.get_ident(), "started")
    while i_start < i_stop and not event.is_set():
        if data[i_start] < 0:
            event.set()
            print(f"{data[i_start]} indice {i_start}")
        i_start += 1

nbr_threads = 15
taille_data = 10000
data = [random.randint(-1, 2000) for _ in range(taille_data)]
offset = taille_data // nbr_threads
reste = taille_data % nbr_threads
liste_threads = []
event = threading.Event()
for i in range(nbr_threads):
    if i == nbr_threads-1:
        liste_threads.append(threading.Thread(target=search_negatif, 
                                              args=[data, i*offset, ((i+1)*offset)+reste, event]))
    else:
        liste_threads.append(threading.Thread(target=search_negatif, 
                                              args=[data, i*offset, (i+1)*offset, event]))

for t in liste_threads:
    t.start()

for t in liste_threads:
    t.join()