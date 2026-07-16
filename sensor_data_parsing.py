from abc import ABC, abstractmethod
from sensor_data import SensorData
from sensor_schema import SCHEMA


class SensorDataParser(ABC):

    def validate(self, reading):

        for sensor_name, parameters in SCHEMA.items():
            for parameter in parameters:
                if parameter not in reading:
                    print(parameter, "missing")
                    reading[parameter] = ""

                elif reading[parameter] is None:
                    print(parameter, "is null")
                    reading[parameter] = ""

        return reading

    def create_sensor_object(self, reading):

        sensor = SensorData(**reading)
        return sensor

    @abstractmethod
    def parse(self, data):
        pass


class JSONParser(SensorDataParser):

    def parse(self, data):
        sensor_readings = {}
        for reading_id, reading in data.items():
            reading = self.validate(reading)
            sensor = self.create_sensor_object(reading)
            sensor_readings[reading_id] = sensor

        return sensor_readings