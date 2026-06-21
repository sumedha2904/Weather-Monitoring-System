import csv
import json

class FileReader:

    def __init__(self):
        self.file_path = r"C:\Users\sumed\OneDrive\Documents\new 1.json"

    def read(self):

        raw_data = {}

        with open(self.file_path, "r") as file:
            raw_data = json.load(file)

        return raw_data