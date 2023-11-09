import threading
from time import sleep

def task():
    for i in range(5):
        sleep(0.5)
        print("hello")


timer = threading.Timer(10,task)
timer.start()


for i in range(5):
    sleep(0.5)
    print("hello everyone")