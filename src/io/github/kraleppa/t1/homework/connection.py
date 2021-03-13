import socket
from threading import Thread
import time


class Connection(Thread):
    def __init__(self):
        Thread.__init__(self)

    def run(self):
        print("Startuje")
        time.sleep(3)
        print("3 sekundy później :)")
