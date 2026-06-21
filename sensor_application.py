from sensor_reader import FileReader
from sensor_data_parsing import SensorDataParser
from sensor_data_logger import DataLogger


class SensorApplication:

    def __init__(self):

        self.reader = FileReader()
        self.sensor_data_parser = SensorDataParser()
        self.logger = DataLogger()


    def run(self):

        raw_data = self.reader.read()

        sensor_readings = self.sensor_data_parser.parse(raw_data)

        for reading_id, sensor in sensor_readings.items():

            print(reading_id)
            sensor.display()

        self.logger.store_csv(sensor_readings)
        self.logger.store_json(sensor_readings)