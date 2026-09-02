import socket

from sensor_reader import SensorReader
from sensor_data_parsing import JSONParser


class WiFiReader(SensorReader):

    def __init__(self, ip="YOUR_IP", port=5000):

        self.ip = ip
        self.port = port

        self.sock = None
        self.buffer = ""

        # Create JSONParser instance
        self.parser = JSONParser()

    def connect(self):

        self.sock = socket.socket(
            socket.AF_INET,
            socket.SOCK_STREAM
        )

        self.sock.connect((self.ip, self.port))

        print("Connected to ESP32")

    def read(self):

        while True:

            chunk = self.sock.recv(1024)

            if not chunk:
                return None

            # Received bytes → string
            self.buffer += chunk.decode()

            if "\n" in self.buffer:

                line, self.buffer = self.buffer.split("\n", 1)

                if not line:
                    continue

                # Send JSON string to JSONParser
                return self.parser.parse(line)

    def disconnect(self):

        if self.sock:

            self.sock.close()
            self.sock = None

        print("Disconnected from ESP32")