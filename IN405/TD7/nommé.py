import os
path = "./mypipe"
os.mkfifo(path,0o666)
pid = os.fork()
if pid == 0: #child
    print("Child starting")
    with open(path,"w") as fifo:
        fifo.write("Hello world")
    print("Child ending")
else: #parent
    print("Parent starting")
    with open(path,"r") as fifo:
        print(fifo.read())
    print("Parent ending")
    os.unlink(path)