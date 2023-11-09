# Another way to create Thread
from threading import Thread

# inherit class Thread
class MyClass(Thread):

    # method overriding 
    def run(self):
        for i in range(5):
            print("Hello Kanha")


t1 = MyClass()
t1.start()