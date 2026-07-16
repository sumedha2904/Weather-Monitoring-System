from abc import ABC, abstractmethod

class SensorReader(ABC):

    @abstractmethod
    def connect(self):
        pass

    @abstractmethod
    def read(self):
        pass

    @abstractmethod
    def disconnect(self):
        pass