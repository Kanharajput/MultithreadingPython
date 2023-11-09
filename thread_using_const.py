# import Thread class
from threading import Thread, current_thread

# create a func to execute it using the new Thread
def display_name(n,msg):

    print(current_thread())
    
    for i in range(n):  
        print(msg)


# create a Thread 
# args is a tuple
# t1 = Thread(target=display_name, args=(5,"hello kanha"))
t1 = Thread(target=display_name, kwargs={'n':5,'msg':"Hello Kanha"})

# start the thread
t1.start()

# this below code is executed by main thread

for i in range(5):
    print("Hello World")


# Output -> Try to run mulitple times then this pattern appers
"""Both run simultaneously that'swhy output is
<Thread(Thread-1 (display_name), started 140229125211712)>
Hello World
Hello Kanha
Hello Kanha
Hello World
Hello Kanha
Hello Kanha
Hello World
Hello Kanha
Hello World
Hello World"""