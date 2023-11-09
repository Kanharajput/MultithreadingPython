import threading 

def custom_hook(args):
    print("Details about Exception")
    print(args[0])
    print(args[1])
    print(args[2])
    print(args[3])


# override the excepthook method of threading
# don't import excepthook from threading otherwise 
# if we assign it here it will be specified as variable
threading.excepthook = custom_hook

# target method
def display():
    print("Adding Kanha" + 5)      # raise an exception

t1 = threading.Thread(target=display)
t1.start()