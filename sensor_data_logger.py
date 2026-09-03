import os
import csv
import json
import xml.etree.ElementTree as ET
import sqlite3

class DataLogger:

    def __init__(self):
        self.json_path = "logger.json"
        self.csv_path = "logger.csv"
        self.xml_path = "logger.xml"
        self.sqlite_path = "logger.db"

    def store_json(self, sensor):
        with open(self.json_path, "a") as file:
            file.write(sensor.raw_data + "\n")

    def __store_csv(self):

        with open(self.json_path, "r") as json_file:
            for line in json_file:
                line = line.strip()

                if not line:
                    continue

        data = json.loads(line)
        file_exists = os.path.exists(self.csv_path)

        with open(self.csv_path, "a", newline="") as file:

            writer = csv.DictWriter(file,fieldnames=data.keys())

            if not file_exists:
                writer.writeheader()

            writer.writerow(data)
        pass

    def __store_xml(self):

        root = ET.Element("readings")

        with open(self.json_path, "r") as file:
            lines = file.readlines()

        for line in lines:
            line = line.strip()

            if not line:
                continue

            data = json.loads(line)
            reading = ET.SubElement(root, "reading")

            for key, value in data.items():
                element = ET.SubElement(reading, key)
                element.text = str(value)

        tree.write(self.xml_path)

        pass

    def __store_sqlite(self):

        with open(self.json_path, "r") as file:
            lines = file.readlines()

        for line in lines:
            line = line.strip()

            if not line:
                continue

            data = json.loads(line)

            connection = sqlite3.connect(self.sqlite_path)
            cursor = connection.cursor()
            columns = ", ".join(f'"{key} TEXT' for key in data.keys())

            cursor.execute(f"CREATE TABLE IF NOT EXISTS readings ({columns})")

        pass