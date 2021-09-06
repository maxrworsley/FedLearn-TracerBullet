from Common import BaseConnection


class ServerConnection(BaseConnection.BaseConnection):

    def connect(self):
        self.local_socket.connect((self.ip_address, self.port))

    def send_data(self, data):
        print(f'S= {data[:1].hex()}:{data[-1:].hex()} to server')
        self.send_bytes(self.local_socket, data)

    def receive_data(self):
        return self.wait_for_bytes(self.local_socket)

