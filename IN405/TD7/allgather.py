import os

childs = []
poeme = ["Bonjour", "Marmelade", "Au coin Dimitri"]

r,w = os.pipe()

for i in range(3):
    pid = os.fork()
    if pid == 0: #child
        os.close(r)
        os.write(w,f"[{os.getpid()}] : {poeme[i]} ".encode())
        os.close(w)
        os._exit(0)
    else: #parent
        childs.append(pid)

for pid in childs:
    os.waitpid(pid, 0)

os.close(w)
r = os.fdopen(r)
print(r.read())
r.close()