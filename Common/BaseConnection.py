import socket


class BaseConnection:
    ip_address = ""
    port = 0
    local_socket = 0
    connection = 0
    foreign_address = 0

    def __init__(self, ip, port):
        self.ip_address = ip
        self.port = port
        self.local_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def close(self):
        self.local_socket.close()
        self.connection = 0
        self.foreign_address = 0

    @staticmethod
    def wait_for_bytes(receiving_socket):
        payload_length = int.from_bytes(receiving_socket.recv(4), byteorder='big', signed=False)
        total_received = bytes([])

        while len(total_received) < payload_length:
            data = receiving_socket.recv(8192)
            total_received += data

        return total_received

    @staticmethod
    def send_bytes(sending_socket, data):
        assert (type(data) == bytearray or type(data) == bytes)

        data_length = len(data)
        b_length = data_length.to_bytes(4, byteorder='big', signed=False)

        sending_socket.send(b_length)
        sending_socket.sendall(data)

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()
