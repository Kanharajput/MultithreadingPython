from threading import Thread
from time import sleep

# inherit the Thread class
class MyClass(Thread):
    
    videos = ["Tech Burner", "Kapil Sharma", "TMKOC"]

    def __init__(self):
        Thread.__init__(self)

    def upload(self,vid):
        print(f"uplaoding video: {vid}")

    def check_copyrights(self):
        print("Checking copyrights")

    # override the run method
    def run(self):
        for vid in self.videos:
            self.upload(vid)
            sleep(1)
            self.check_copyrights()
            sleep(0.5)


if __name__ == "__main__":

    print("Watching on Main Thread")
    print("Uploading and Checking is on new created Thread\n")

    t1 = MyClass()
    t1.start()

    for i in ["Jadu ki Jhapi", "Travelling Desi", "Om shanti Om"]:
        print(f"Watching {i} in")
        sleep(2)