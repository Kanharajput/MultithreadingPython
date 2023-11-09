from threading import Thread, current_thread

# class having target function
class Example:
    # target function
    def func():

        for i in range(5):
            print(f"Hello from {current_thread().name}")



# instance of Example class
ex = Example()

# create a new thread
t1 = Thread(target=Example.func) 

# start the thread
t1.start()

for i in range(5):
    print("Hello from main Thread")
