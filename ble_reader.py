import sensor_reader
import json

class BLEReader(sensor_reader.SensorReader):

    def connect(self):

        print("Connecting ESP32-S3 through BLE")

    def read(self):
        #BLE receive logic
        raw_data = {}
        sensor_data = json.loads(raw_data)
        return sensor_data

    def disconnect(self):

        print("Disconnecting BLE")