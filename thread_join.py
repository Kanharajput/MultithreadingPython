# join method to let the below threads wait 
# until it completes it's execution

from threading import Thread


def uploading():
    for i in range(3):
        print("Uploading the video")

print("sak lak boom boom")

def notify():
    print("Send notification to all subs")


t1 = Thread(target=uploading)
t1.start()
t1.join()   # once it completed then other threads starts execution

t2 = Thread(target=notify)
t2.start()

print("Watching on MainThread")