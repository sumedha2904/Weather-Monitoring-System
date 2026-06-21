class SensorData:

    def __init__(self, **data):

        for key, value in data.items():
            setattr(self, key, value)

    def get_data(self):
        return self.__dict__.keys(), self.__dict__.values()

    def display(self):

        for key, value in self.__dict__.items():
            print(key, ":", value)

        print("----------------")