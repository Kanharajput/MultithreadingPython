import threading

# by default it has Lock
con = threading.Condition() 

def take_temp():
    con.acquire()
    
    day_list = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

    # write in a file
    with open("temp_details.txt","w") as file:

        # take temp for this day
        for day in day_list:
            temp = input(f"temp on {day}: ")
            file.write(temp+"\n")

    con.notify_all()               # notify all that this thread work is done now they can proceed
    con.release()


def max_temp():
    con.acquire()
    con.wait(timeout=0)
    # get the data from the file
    with open("temp_details.txt", "r") as file:
        temp_data = file.readlines()
        max_temp = float(temp_data[0].strip('\n'))   # get the temp of one day

        for temp_str in temp_data[1:]:
            temp = float(temp_str.strip('\n'))
            if temp > max_temp:
                max_temp = temp

        print("Max temp is ", max_temp)
    con.release()


def avg_temp():
    con.acquire()
    con.wait(timeout=0)
    sum = 0
    # get the data from the file
    with open("temp_details.txt", "r") as file:
        temp_data = file.readlines()

        for temp_str in temp_data:
            temp = float(temp_str.strip('\n'))
            sum += temp

    avg = sum/7
    print("Avg temp is ", avg)
    con.release()


t1 = threading.Thread(target=take_temp)
t2 = threading.Thread(target=max_temp)
t3 = threading.Thread(target=avg_temp)

t1.run()
t2.run()
t3.run()