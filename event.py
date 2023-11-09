from threading import Event, Thread

# create the object of Event
ev = Event()

# Event is used to communicate btw to only two threads

def display_thread1():
    for i in range(5):
        print("Printing by thread 1")
    
    # set make the internal flag = True
    # now second thread can run
    ev.set()


def display_thread2():
    # wait until flag val updated
    ev.wait()
    
    if ev.is_set():
        for i in range(5):
            print("Printing by thread 2")


t1 = Thread(target=display_thread1)
t2 = Thread(target=display_thread2)

t1.start()
t2.start()