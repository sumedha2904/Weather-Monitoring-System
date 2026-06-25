import json


class FileReader:

    def __init__(self):

        self.file_path = r"C:\Users\sumed\OneDrive\Documents\weather_monitoring\dummy_sensor_data.json"


    def read(self):

        with open(self.file_path, "r") as file:

            raw_data = json.load(file)

        return raw_data