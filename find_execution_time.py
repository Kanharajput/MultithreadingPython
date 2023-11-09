from threading import Thread
import time


def square(num):
    print(f"The square of {num} is: {num**2}")
    

def cube(num):
    print(f"The cube of {num} is: {num**3}")


t1 = Thread(target=square, args=(3,))
t2 = Thread(target=cube, args=(3,))

# save time when the execution starts
begin = time.time()

# start the threads
t1.start()
t2.start()

print("Time by using Threads: ", time.time() - begin)




# doing things normally
def square_normal(num):
    print(f"The square of {num} is: {num**2}")
    

def cube_normal(num):
    print(f"The cube of {num} is: {num**3}")


# begin time of execution
begin = time.time()
square_normal(3)    
cube_normal(3)

print("Time without Thread: ", time.time() - begin)