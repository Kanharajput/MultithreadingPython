# Built in methods
from threading import Thread, active_count, main_thread, enumerate

# target method executed by thread
def display_names():
    # want to print the details of mainThread 
    # here if we use current_thread()
    # so it print the details of t1 Thread
    print(main_thread())
    print(active_count())
    print("kanha tomar")


t1 = Thread(target=display_names)

print("This is printed by MainThread")

t1.start()

# details of all thread in a list
print(enumerate())

# printing the count of currently active Threads
# sometimes the Thread t1 got killed after completion of it's work
# so we got the count
print("no of threads :",active_count())

