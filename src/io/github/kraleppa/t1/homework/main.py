import socket
import sys
from threading import Thread
import threading
import time
import logging


def thread_test():
    print("asdasd")
    time.sleep(2)
    print("asdasd2")
    return


if len(sys.argv) == 3:
    IP_ADDRESS = str(sys.argv[1])
    PORT = int(sys.argv[2])
else:
    IP_ADDRESS = "127.0.0.1"
    PORT = 8080

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind((IP_ADDRESS, PORT))
server.listen(100)

while True:
    conn, addr = server.accept()
    print(addr[0] + " connected")
    thread = Thread(target=thread_test)
    thread.start()
