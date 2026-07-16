import socket
import json
import time
from sensor_reader import SensorReader


class ESP32S3Reader(SensorReader):

    def __init__(self, host="localhost", port=5000, data_path=None):

        self.host = host
        self.port = port
        self.data_path = r"C:\Users\sumed\OneDrive\Documents\weather_monitoring\dummy_sensor_data.json"
        self.server_socket = None
        self.client_socket = None

    def connect(self):

        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind((self.host, self.port))
        self.server_socket.listen()

        print("Server started...")
        print("Waiting for client...")

        self.client_socket, address = self.server_socket.accept()
        print("Connected:", address)

    def read(self):

        request = self.client_socket.recv(1024).decode()
        print("Client asked:", request)

        if request != "GET_WEATHER":
            self.client_socket.send("Unknown request\n".encode())
            return {}

        with open(self.data_path, "r") as file:
            data = json.load(file)

        readings_iter = iter(data.items())

        while True:
            try:
                reading_id, reading = next(readings_iter)
            except StopIteration:
                break

            message = json.dumps({reading_id: reading})
            self.client_socket.send((message + "\n").encode())
            print("Sent:", message)
            time.sleep(2)

        return data

    def disconnect(self):

        self.client_socket.close()
        self.server_socket.close()
