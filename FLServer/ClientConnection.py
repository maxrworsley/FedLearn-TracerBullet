from Common import BaseConnection


class ClientConnection(BaseConnection.BaseConnection):

    def accept_local(self):
        self.local_socket.bind((self.ip_address, self.port))
        self.local_socket.listen(1)
        self.connection, self.foreign_address = self.local_socket.accept()

    def send_data(self, data):
        self.send_bytes(self.connection, data)

    def receive_data(self):
        return self.wait_for_bytes(self.connection)
