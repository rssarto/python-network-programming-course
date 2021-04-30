import threading
import time


# Defining the main function
def myfunction():
    "Function to be executed"
    print("Start a thread")
    time.sleep(3)
    print("End a thread")


# Define an empty list of threads
threads = []

for i in range(5):
    th = threading.Thread(target=myfunction)
    th.start()
    threads.append(th)

for th in threads:
    th.join()
