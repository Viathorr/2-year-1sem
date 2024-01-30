import socket
import threading
import rsa

PORT = 5555
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'


class Server:
    """
    Class representing a server for handling client connections and communication.

    Attributes:
        server (socket.socket): The server socket.
        clients (list): A list of clients' sockets.
        nicknames (list): A list of client nicknames.
        public_keys (list): A list of client public keys.
        _public_key (rsa.PublicKey): The server's public key.
        _private_key (rsa.PrivateKey): The server's private key.

    Methods:
        start():
            Starts the server and listens for incoming connections.

        _handle_client(client: socket.socket):
            Handles communication with a single client.

        _broadcast(message: str):
            Broadcasts a message to all connected clients.

        __load_keys():
            Loads the server's public and private keys.
    """
    def __init__(self) -> None:
        """
        Initialize a new Server object.
        """
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind(ADDR)

        self.clients = []
        self.nicknames = []
        self.public_keys = []

        self._public_key = None
        self._private_key = None

    def start(self) -> None:
        """
        Starts the server and listens for incoming connections.
        """
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

    def _handle_client(self, client: socket.socket) -> None:
        """
        Handles communication with a single client.

        Args:
            client (socket.socket): The client socket.
        """
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

    def _broadcast(self, message) -> None:
        """
        Broadcasts a message to all connected clients.

        Args:
            message (str): The message to broadcast.
        """
        for client in self.clients:
            client_public_key = self.public_keys[self.clients.index(client)]
            client.send(rsa.encrypt(message.encode(FORMAT), client_public_key))

    def __load_keys(self) -> None:
        """
        Loads the server's public and private keys.
        """
        with open('../keys/server_public_key.pem', 'rb') as p:
            self._public_key = rsa.PublicKey.load_pkcs1(p.read())
        with open('../keys/server_private_key.pem', 'rb') as p:
            self._private_key = rsa.PrivateKey.load_pkcs1(p.read())


if __name__ == '__main__':
    server = Server()
    server.start()
