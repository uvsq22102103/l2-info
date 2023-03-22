import os

rfd, wfd = os.pipe()
pid = os.fork()
if pid == 0: # Dans fils
    os.close(rfd)
    print("Child starting")
    w = os.fdopen(wfd,"w")
    w.write("Hello Boy")
    print("Child ending")
else: # Dans père
    os.close(wfd)
    print("Parent starting")
    r = os.fdopen(rfd)
    print(r.read())
    print("Parent ending")
    
