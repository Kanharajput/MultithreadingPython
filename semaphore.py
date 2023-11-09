from threading import *
from time import sleep


# target method
def display(s_object):

    # lock the section
    s_object.acquire()

    for i in range(2):
        print("Printing by Thread", current_thread().name)

        sleep(0.5)

    # unlock the section
    s_object.release()
    

# semaphore object without arguement works as RLock
# Here there threads can access the critical section simultaneously
s_object = Semaphore(3)
t1 = Thread(target=display, args=(s_object,), name="1")
t2 = Thread(target=display, args=(s_object,), name="2")
t3 = Thread(target=display, args=(s_object,), name="3")
t4 = Thread(target=display, args=(s_object,), name="4")
t5 = Thread(target=display, args=(s_object,), name="5")

t1.start()
t2.start()
t3.start()
t4.start()
t5.start()