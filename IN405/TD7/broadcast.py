import os

childs = []

for _ in range(3):
    r,w = os.pipe()
    pid = os.fork()
    if pid == 0: #child
        os.close(w)
        r = os.fdopen(r)
        print(r.read())
        r.close()
        os._exit(0)
    else: #parent
        childs.append(pid)
        os.close(r)
        os.write(w,b"Mise a jour")
        os.close(w)

for pid in childs:
    os.waitpid(pid,0)

print("end")