import threading
import time

class mythread(threading.Thread):
    def run(self):
        for x in range(7):
            print("Hi from child")
a = mythread()
b = mythread()

a.start()
b.start()

a.join()
b.join()

print("Bye from",current_thread().getName())