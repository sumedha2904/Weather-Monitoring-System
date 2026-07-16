import json
from sensor_reader import SensorReader


class FileReader(SensorReader):

    def __init__(self):

        self.file_path = r"C:\Users\sumed\OneDrive\Documents\weather_monitoring\dummy_sensor_data.json"

    def connect(self):
        pass

    def read(self):

        with open(self.file_path, "r") as file:

            raw_data = json.load(file)

        return raw_data

    def disconnect(self):
        pass