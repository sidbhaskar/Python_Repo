import threading
import time

def countdown(n):
    while n>0:
        print(n)
        n -=1
        time.sleep(1)

thread1 = threading.Thread(target = countdown, args = (5,) )
thread2 = threading.Thread(target = countdown , args = (10,) )
thread3 = threading.Thread(target = countdown , args = (7,) )
thread1.start()
thread2.start()
thread3.start()
thread1.join()
thread2.join()
thread3.join()
