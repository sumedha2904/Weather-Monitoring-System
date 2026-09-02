from PyQt6.QtCore import QObject, pyqtSignal, pyqtSlot, QTimer

from wifi_reader import WiFiReader
from sensor_data_logger import DataLogger

import json


class SensorApplication(QObject):

    reading_received = pyqtSignal(str)

    def __init__(self):

        super().__init__()

        self.reader = WiFiReader(
            ip="YOUR_IP",
            port=5000
        )

        self.logger = DataLogger()

        self.timer = QTimer()
        self.timer.timeout.connect(self.read_data)

        self.running = False

    @pyqtSlot()
    def connect_to_esp32(self):

        self.reader.connect()

        self.running = True

        self.timer.start(1)

    def read_data(self):

        if not self.running:
            return

        # WiFiReader returns SensorData object
        sensor = self.reader.read()

        if sensor is None:

            self.disconnect_from_esp32()
            return

        # Store reading
        self.logger.store_csv(sensor)
        self.logger.store_json(sensor)

        # Send reading to QML
        self.reading_received.emit(
            json.dumps(sensor.__dict__)
        )

    @pyqtSlot()
    def disconnect_from_esp32(self):

        self.running = False

        self.timer.stop()

        self.reader.disconnect()