from threading import Event, Thread
from time import sleep


# create the event object
ev = Event()

def light_switch():
    while True:
        print("The light is Green")
        ev.set()            # flag to True
        sleep(5)
        print("The light is Red")
        ev.clear()           # flag to False
        sleep(5)



def message(): 
    ev.wait()            # wait until flag = True

    while ev.is_set():                # run till the flag is True
        print("You can go")
        sleep(0.5)
        # put it on wait each time it not goes to wait till the flag = True
        # once flag = False it starts waiting
        # we need it here because once ev.is_set() = false after first run 
        # the loop stops and this thread work is done 
        # we want call it in future
        ev.wait()                  
    



t1 = Thread(target=light_switch)
t2 = Thread(target=message)

t1.run()
t2.run()
