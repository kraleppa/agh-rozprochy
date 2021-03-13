import socket
import sys
from threading import Thread

working = True


def sender():
    while working:
        message = str(socket.recv(2048), 'utf-8')
        print(message)
    socket.close()


def receiver():
    global working
    while working:
        message = input()
        if message == '/quit':
            working = False
            print("Closing...")
        socket.send(bytes(message, 'utf-8'))


if len(sys.argv) == 3:
    IP_ADDRESS = str(sys.argv[1])
    PORT = int(sys.argv[2])
else:
    IP_ADDRESS = "127.0.0.1"
    PORT = 8080

print("Podaj swój nick: ")
nick = input()

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.connect((IP_ADDRESS, PORT))
socket.send(bytes(nick, 'utf-8'))

Thread(target=sender).start()
Thread(target=receiver).start()

while working:
    pass
