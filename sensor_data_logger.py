import csv
import json

class DataLogger:

    def __init__(self):
        self.csv_path = "logger.csv"
        self.json_path = "logger.json"

    def store_csv(self, sensor_readings):

        if not sensor_readings:
            print("No data available")
            return

        headers = []

        # collect sensor fields
        for sensor in sensor_readings.values():
            for key in sensor.__dict__.keys():
                if key not in headers:
                    headers.append(key)

        with open(self.csv_path, "w", newline="") as file:

            writer = csv.DictWriter(file, fieldnames=headers)

            writer.writeheader()

            for sensor in sensor_readings.values():
                writer.writerow(sensor.__dict__)

    def store_json(self, sensor_readings):
        data = {}

        for reading_id, sensor in sensor_readings.items():
            data[reading_id] = sensor.__dict__

        with open(self.json_path, "w") as file:
            json.dump(data, file, indent=4)
