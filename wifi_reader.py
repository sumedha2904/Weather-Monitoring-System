import socket
import json
from sensor_reader import SensorReader


class WiFiReader(SensorReader):

    def __init__(self, ip="localhost", port=5000):

        self.sock = None
        self.ip = ip
        self.port = port

    def connect(self):

        self.sock = socket.socket(
            socket.AF_INET,
            socket.SOCK_STREAM
        )

        self.sock.connect(
            (self.ip, self.port)
        )

    def read(self):

        self.sock.send("GET_WEATHER".encode())

        sensor_readings = {}
        buffer = ""

        while True:
            chunk = self.sock.recv(1024)

            if not chunk:
                break

            buffer += chunk.decode()

            while "\n" in buffer:
                line, buffer = buffer.split("\n", 1)

                if not line:
                    continue

                reading = json.loads(line)
                sensor_readings.update(reading)

        return sensor_readings

    def disconnect(self):

        self.sock.close()