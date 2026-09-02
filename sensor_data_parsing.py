from abc import ABC, abstractmethod
from sensor_data import SensorData


class SensorDataParser(ABC):

    def validate(self, reading):
        if not reading:
            print("No sensor data received")
        return reading

    def create_sensor_object(self, reading):
        return SensorData(reading)

    @abstractmethod
    def parse(self, data):
        pass


class JSONParser(SensorDataParser):

    def parse(self, raw_data):
        raw_data = self.validate(raw_data)
        sensor = self.create_sensor_object(raw_data)
        return sensor