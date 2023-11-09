import threading
import time

def non_daemon_function():
    for i in range(5):
        print("Non-daemon thread is running...")
        time.sleep(1)

non_daemon_thread = threading.Thread(target=non_daemon_function)
non_daemon_thread.daemon = True
non_daemon_thread.start()

# non_daemon_thread.join()
print("Main program is exiting.")
