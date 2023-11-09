# every thread is a part of threading.Thread class
# Here threading is module and Thread is class
# Each program needs a thread to run and we call it main thread

import threading


# it returns the current thread which executing this program
current_thread = threading.current_thread()

print(current_thread)
print(current_thread.name)
print(current_thread.ident)           # return the unique id of the Thread
print(current_thread.is_alive())      # return True if Thread is running


