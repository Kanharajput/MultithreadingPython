from threading import *
from time import sleep


class Bus:
    def __init__(self, bus_name, avl_seats):
        self.bus_name = bus_name
        self.available_seats = avl_seats


    def book_seats(self, needed_seats):
        # this is critical section
        if self.available_seats >= needed_seats:
            print(f"{current_thread().name} Booking your seats")
            sleep(1)               # processing time

            print(f"{current_thread().name} seats booked")
            self.available_seats -= needed_seats

        else:
            print(f"Sorry! we don't enough seats")


b = Bus("Kanha Travels", 3)

t1 = Thread(target=b.book_seats, args=(2,))
t1.name = "Ram"
t2 = Thread(target=b.book_seats, args=(2,))
t2.name = "Shyam"

t1.start()
t2.start()

# Problem both got their seats booked 
# but we only have 3 seats available
# so this is know as race condition