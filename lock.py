# always use lock in pairs
# first lock then release it
# don't do lock lock then release release 
from threading import *
from time import sleep


# target method
def display_something(lock_obj, msg):

    # lock the critical section
    lock_obj.acquire()
    print(lock_obj)

    for i in range(5):
        sleep(1)
        print(msg)

    # release the critical section
    lock_obj.release()


# initialise the lock object
lock_obj = Lock()

t1 = Thread(target=display_something, args=(lock_obj, "hello there 1"))
t2 = Thread(target=display_something, args=(lock_obj, "Hello there 2"))

t1.start()
t2.start()