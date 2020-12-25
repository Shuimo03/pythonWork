import time
import threading

def thread1(i):
    time.sleep(3)
    print('No. printrd by Thread1: %d' %i)

def thread2(i):
    print('No. printed by Thread2: %d' %i)

if __name__ == '__main__':
    t1 = threading.Thread(target=thread1,args=(10,))
    t2 = threading.Thread(target=thread2,args=(12,))

    #  start the threads
    t1.start()
    t2.start()

    t1.join()
    t2.join()
    