import socket
import threading
import rsa
from typing import List
from client.gui.imediator import IMediator

PORT = 5555
SERVER = '192.168.95.126'
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'


class ClientSocket:
    """
    Class representing a client socket for connecting to a server and handling communication.

    Attributes:
        _socket (socket.socket): The client socket.
        _mediator (IMediator): The mediator that handles all needed events.
        _connected (bool): Indicates whether the client is connected to the server.
        _public_key (rsa.PublicKey): The client's public key.
        _private_key (rsa.PrivateKey): The client's private key.
        _server_public_key (rsa.PublicKey): The server's public key.
        _participants (list): A list of participants connected to the server.

    Methods:
        _generate_keys():
            Generates public and private keys for the client.

        connect():
            Connects the client socket to the server.

        _receive():
            Receives messages from the server.

        send(message: str):
            Sends a message to the server.

        close():
            Closes the client socket.
    """
    def __init__(self, mediator: IMediator) -> None:
        """
        Initialize a new ClientSocket object.

        Args:
            mediator(IMediator): Reference to the parent (gui component) object.
        """
        self._socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self._mediator = mediator
        self._connected = False
        self._public_key = None
        self._private_key = None
        self._server_public_key = None
        self._participants = []

    @property
    def participants(self) -> List[str]:
        return self._participants

    def _generate_keys(self) -> None:
        """
        Generates public and private keys for the client.
        """
        self._public_key, self._private_key = rsa.newkeys(1024)

    def connect(self) -> None:
        """
        Connects the client socket to the server.
        """
        try:
            self._socket.connect(ADDR)
            self._connected = True
            self._generate_keys()
            self._server_public_key = rsa.PublicKey.load_pkcs1(self._socket.recv(1024))
            self._socket.send(rsa.PublicKey.save_pkcs1(self._public_key))
            msg = rsa.decrypt(self._socket.recv(1024), self._private_key).decode(FORMAT)
            if msg == 'NICK':
                self._socket.send(rsa.encrypt(self._mediator.user.name.encode(FORMAT), self._server_public_key))
            thread_receive = threading.Thread(target=self._receive)
            thread_receive.start()
        except socket.error as err:
            print(err)
            raise Exception('Failed to connect to server! Try again.')

    def _receive(self) -> None:
        """
        Receives messages from the server.
        """
        while True:
            try:
                msg = rsa.decrypt(self._socket.recv(1024), self._private_key).decode(FORMAT)
                if msg.startswith('PARTICIPANTS'):
                    self._participants.clear()
                    lines = msg.split('\n')
                    for i in range(1, len(lines)):
                        nickname = lines[i]
                        self._participants.append(nickname)
                    self._mediator.change_participants_label(f'Participants: {len(self._participants)}')
                else:
                    self._mediator.display_msg(msg)
            except socket.error:
                if self._socket.fileno() == -1:
                    break
                self.close()
                self._mediator.handle_server_err()
                break

    def send(self, message) -> None:
        """
        Sends a message to the server.

        Args:
            message (str): The message to send.
        """
        self._socket.send(rsa.encrypt(message.encode(FORMAT), self._server_public_key))

    def close(self) -> None:
        """
        Closes the client socket.
        """
        self._socket.close()
