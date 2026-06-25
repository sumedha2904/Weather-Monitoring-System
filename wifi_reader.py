import socket
import sensor_reader
import json
class WiFiReader(sensor_reader.SensorReader):

    def __init__(self):

        self.sock = None
        self.ip = "192.168.1.10"
        self.port = 8080

    def connect(self):

        self.sock = socket.socket(
            socket.AF_INET,
            socket.SOCK_STREAM
        )

        self.sock.connect(
            (self.ip, self.port)
        )

    def read(self):

        raw_data = self.sock.recv(1024)
        decoded_data = raw_data.decode()
        sensor_data = json.loads(decoded_data)
        return sensor_data

    def disconnect(self):

        self.sock.close()