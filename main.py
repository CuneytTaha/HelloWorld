from threading import Thread
from time import sleep


def threadControl():
    counter = 0
    while True:
        counter += 1
        print(f"Thread {counter} second")
        sleep(1)


controlThread = Thread(target=threadControl)
controlThread.daemon = True
controlThread.start()


print("Main 1 second")
sleep(5)
print("Main 5 second")
sleep(5)
print("Main 10 second")
