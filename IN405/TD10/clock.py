import time, os

def clock():
    i = 0
    while i<10:
        t = time.gmtime()
        print(f"{t.tm_hour}:{t.tm_min}:{t.tm_sec}")
        time.sleep(5)
        i += 1


pid = os.fork()
if pid == 0:
    clock()