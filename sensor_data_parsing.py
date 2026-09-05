from sensor_data import SensorData


class SensorDataParser:
    def parse(self, raw_data):

        temperature = float(raw_data.split('"bme_temperature":')[1].split(',')[0])
        humidity = float(raw_data.split('"humidity":')[1].split(',')[0])
        pressure = float(raw_data.split('"pressure":')[1].split(',')[0])

        sensor = SensorData()

        sensor.set_temperature(temperature)
        sensor.set_pressure(pressure)
        sensor.set_humidity(humidity)

        return sensor
