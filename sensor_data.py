class SensorData:
    def __init__(self, raw_data):
        self.raw_data = raw_data

    def display(self):
        print(self.raw_data)
        print("----------------")