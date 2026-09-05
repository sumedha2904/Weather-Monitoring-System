class SensorData:

    def __init__(self):
        self.__temperature = None
        self.__pressure = None
        self.__humidity = None

    def set_temperature(self, temperature):
        self.__temperature = temperature

    def get_temperature(self):
        return self.__temperature

    def set_pressure(self, pressure):
        self.__pressure = pressure

    def get_pressure(self):
        return self.__pressure

    def set_humidity(self, humidity):
        self.__humidity = humidity

    def get_humidity(self):
        return self.__humidity