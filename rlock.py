# acquire and release multiple times
from threading import *
from time import sleep


# target method
def display_something(r_lock_obj, msg):

    # lock the critical section
    r_lock_obj.acquire()    
    r_lock_obj.acquire()
    print(r_lock_obj)

    for i in range(5):
        sleep(1)
        print(msg)

    # release the critical section
    r_lock_obj.release()
    r_lock_obj.release()


# initialise the lock object
r_lock_obj = RLock()

t1 = Thread(target=display_something, args=(r_lock_obj, "hel    o there 1"))
t2 = Thread(target=display_something, args=(r_lock_obj, "Hello there 2"))

t1.start()
t2.start()