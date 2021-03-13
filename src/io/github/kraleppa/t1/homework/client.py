import socket
import sys
from threading import Thread
from image import image

working = True


def receiver_tcp():
    while working:
        message = str(tcp_client.recv(2048), 'utf-8')
        print(message)
    tcp_client.close()


def sender():
    global working
    while working:
        message = input()
        if message == '/quit':
            working = False
            print("Closing...")
            tcp_client.send(bytes(message, 'utf-8'))
            udp_client.sendto(bytes(message, 'utf-8'), (IP_ADDRESS, PORT))
        elif message == 'U':
            udp_client.sendto(bytes(image, 'utf-8'), (IP_ADDRESS, PORT))
        else:
            tcp_client.send(bytes(message, 'utf-8'))


def receiver_udp():
    while working:
        buff, address = udp_client.recvfrom(2048)
        print(str(buff, 'utf-8'))


if len(sys.argv) == 3:
    IP_ADDRESS = str(sys.argv[1])
    PORT = int(sys.argv[2])
else:
    IP_ADDRESS = "127.0.0.1"
    PORT = 8080

print("Podaj swój nick: ")
nick = input()

tcp_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcp_client.connect((IP_ADDRESS, PORT))
tcp_client.send(bytes(nick, 'utf-8'))

udp_client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
udp_client.sendto(bytes("Hello", 'utf-8'), (IP_ADDRESS, PORT))

Thread(target=sender).start()
Thread(target=receiver_tcp).start()
Thread(target=receiver_udp).start()

while working:
    pass

