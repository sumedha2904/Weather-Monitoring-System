from sensor_data import SensorData
from sensor_schema import SCHEMA


class SensorDataParser:

    def parse(self, data):
        sensor_readings = {}
        for reading_id, reading in data.items():

            for sensor_name, parameters in SCHEMA.items():
                for parameter in parameters:

                    if parameter not in reading:
                        print(parameter, "missing")
                        reading[parameter] = ""

                    elif reading[parameter] is None:
                        print(parameter, "is null")
                        reading[parameter] = ""

            sensor = SensorData(**reading)
            sensor_readings[reading_id] = sensor

        return sensor_readings