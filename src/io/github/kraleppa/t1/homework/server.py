import socket
from connection import Connection


class Server:
    def __init__(self, address, port):
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.server.bind((address, port))
        self.server.listen(100)
        self.run()

    def run(self):
        while True:
            conn, addr = self.server.accept()
            print(addr[0] + " connected")
            thread = Connection()
            thread.start()
