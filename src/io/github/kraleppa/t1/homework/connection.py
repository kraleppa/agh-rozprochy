from threading import Thread


class Connection(Thread):
    def __init__(self, connection, address, client_repository):
        Thread.__init__(self)
        self.connection = connection
        self.address = address
        self.client_repository = client_repository
        self.nick = None

    def run(self):
        self.connection.send(bytes("Witajcie! Podaj swój nick: ", 'utf-8'))
        self.nick = str(self.connection.recv(2048), 'utf-8').strip()
        print(type(self.connection))

        while True:
            message = str(self.connection.recv(2048), 'utf-8')
            if message.strip() == "/quit":
                self.client_repository.remove_client(self)
                self.connection.close()
                return
            self.client_repository.broadcast(self, message)


