import socket
import threading
import rsa

PORT = 5555
SERVER = '192.168.95.126'
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'


class ClientSocket:
    def __init__(self, parent):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self._parent = parent
        self._connected = False
        self._public_key = None
        self._private_key = None
        self._server_public_key = None
        self.participants = []

    def _generate_keys(self):
        self._public_key, self._private_key = rsa.newkeys(1024)

    def connect(self):
        try:
            self.socket.connect(ADDR)
            self._connected = True
            self._generate_keys()
            self._server_public_key = rsa.PublicKey.load_pkcs1(self.socket.recv(1024))
            self.socket.send(rsa.PublicKey.save_pkcs1(self._public_key))
            msg = rsa.decrypt(self.socket.recv(1024), self._private_key).decode(FORMAT)
            if msg == 'NICK':
                self.socket.send(rsa.encrypt(self._parent.master.user.name.encode(FORMAT), self._server_public_key))
            thread_receive = threading.Thread(target=self._receive)
            thread_receive.start()
            self._parent.open()
        except socket.error:
            raise Exception('Failed to connect to server! Try again.')

    def _receive(self):
        while True:
            try:
                msg = rsa.decrypt(self.socket.recv(1024), self._private_key).decode(FORMAT)
                if msg.startswith('PARTICIPANTS'):
                    print('in participants msg')
                    self.participants.clear()
                    lines = msg.split('\n')
                    for i in range(1, len(lines)):
                        nickname = lines[i]
                        self.participants.append(nickname)
                    self._parent.set_participants_label(f'Participants: {len(self.participants)}')
                else:
                    self._parent.add_message(msg)
            except socket.error:
                if self.socket.fileno() == -1:
                    break
                self.close()
                self._parent.deiconify_parent_root()
                self._parent.show_server_error()
                self._parent.destroy()
                break

    def send(self, message):
        self.socket.send(rsa.encrypt(message.encode(FORMAT), self._server_public_key))

    def close(self):
        self.socket.close()
