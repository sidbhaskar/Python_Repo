import threading
import time
def countdown(n):
    while n > 0:
        print(n)
        n -= 1
        time.sleep(1)
# Create two threads and start them
thread1 = threading.Thread(target=countdown, args=(5,))
thread2 = threading.Thread(target=countdown, args=(10,))
thread1.start()
thread2.start()
# Wait for both threads to finish
thread1.join()
thread2.join()
print("Done!")
