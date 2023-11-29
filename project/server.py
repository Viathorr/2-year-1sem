import socket
import threading
import rsa

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
        self.public_keys = []

        self._public_key = None
        self._private_key = None

    def start(self):
        print('Server is listening...\n')
        self.__load_keys()
        self.server.listen()
        while True:
            client, address = self.server.accept()
            self.clients.append(client)

            client.send(rsa.PublicKey.save_pkcs1(self._public_key))
            client_public_key = rsa.PublicKey.load_pkcs1(client.recv(1024))
            self.public_keys.append(client_public_key)

            client.send(rsa.encrypt('NICK'.encode(FORMAT), client_public_key))
            nickname = rsa.decrypt(client.recv(1024), self._private_key).decode(FORMAT)
            print(nickname)
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
                msg = rsa.decrypt(client.recv(1024), self._private_key).decode(FORMAT)
                self._broadcast(msg)
            except socket.error:
                client_nickname = self.nicknames[self.clients.index(client)]
                client_public_key = self.public_keys[self.clients.index(client)]
                msg = f'{client_nickname} disconnected.\n\n'
                print(msg)
                self.clients.remove(client)
                self.nicknames.remove(client_nickname)
                self.public_keys.remove(client_public_key)
                self._broadcast(msg)
                info_msg = 'PARTICIPANTS'
                for nick in self.nicknames:
                    info_msg += f'\n{nick}'
                self._broadcast(info_msg)
                break
        client.close()

    def _broadcast(self, message):
        for client in self.clients:
            client_public_key = self.public_keys[self.clients.index(client)]
            client.send(rsa.encrypt(message.encode(FORMAT), client_public_key))

    def __load_keys(self):
        with open('keys/server_public_key.pem', 'rb') as p:
            self._public_key = rsa.PublicKey.load_pkcs1(p.read())
        with open('keys/server_private_key.pem', 'rb') as p:
            self._private_key = rsa.PrivateKey.load_pkcs1(p.read())


if __name__ == '__main__':
    server = Server()
    server.start()
