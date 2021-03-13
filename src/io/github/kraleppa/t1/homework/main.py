import sys
from server import Server

if len(sys.argv) == 3:
    IP_ADDRESS = str(sys.argv[1])
    PORT = int(sys.argv[2])
else:
    IP_ADDRESS = "127.0.0.1"
    PORT = 8080

server = Server(IP_ADDRESS, PORT)

