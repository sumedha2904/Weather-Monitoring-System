import os


class DataLogger:

    def __init__(self):

        self.csv_path = "logger.csv"
        self.json_path = "logger.json"

    def store_csv(self, sensor):

        file_exists = os.path.exists(self.csv_path)

        with open(self.csv_path, "a") as file:

            if not file_exists:
                file.write("Reading\n")

            file.write(sensor.raw_data + "\n")

    def store_json(self, sensor):

        with open(self.json_path, "a") as file:

            file.write(sensor.raw_data + "\n")