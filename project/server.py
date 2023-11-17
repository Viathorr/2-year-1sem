import socket
import threading

PORT = 9090
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'


class Server:
    def __init__(self):
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind(ADDR)

        self.clients = []
        self.nicknames = []

    def start(self):
        print('Server is listening...\n')
        self.server.listen()
        while True:
            client, address = self.server.accept()
            self.clients.append(client)
            client.send('NICK'.encode(FORMAT))
            nickname = client.recv(1024).decode(FORMAT)
            self.nicknames.append(nickname)
            thread = threading.Thread(target=self._handle_client, args=(client,))
            thread.start()

    def _handle_client(self, client):
        print('New client has connected.')
        info_msg = 'PARTICIPANTS'
        for nick in self.nicknames:
            info_msg += f'\n{nick}'
        self._broadcast(info_msg)
        while True:
            try:
                msg = client.recv(1024).decode(FORMAT)
                self._broadcast(msg)
            except socket.error:
                client_nickname = self.nicknames[self.clients.index(client)]
                msg = f'{client_nickname} disconnected.\n\n'
                print(msg)
                self.clients.remove(client)
                self.nicknames.remove(client_nickname)
                self._broadcast(msg)
                info_msg = 'PARTICIPANTS'
                for nick in self.nicknames:
                    info_msg += f'\n{nick}'
                self._broadcast(info_msg)
                break
        client.close()

    def _broadcast(self, message):
        for client in self.clients:
            client.send(message.encode(FORMAT))


if __name__ == '__main__':
    server = Server()
    server.start()
