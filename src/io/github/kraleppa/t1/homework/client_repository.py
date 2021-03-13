import threading


class ClientRepository:
    def __init__(self):
        self.connected_clients = []
        self.lock = threading.Lock()

    def add_client(self, client):
        with self.lock:
            self.connected_clients.append(client)
        print(self.connected_clients)

    def remove_client(self, client):
        if client in self.connected_clients:
            with self.lock:
                self.connected_clients.remove(client)
        print(self.connected_clients)
