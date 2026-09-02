import sys

from PyQt6.QtWidgets import QApplication
from PyQt6.QtQml import QQmlApplicationEngine

from sensor_application import SensorApplication


app = QApplication(sys.argv)

engine = QQmlApplicationEngine()

backend = SensorApplication()

engine.rootContext().setContextProperty("backend", backend)

engine.load("weather_gui.qml")

if not engine.rootObjects():
    sys.exit(-1)

sys.exit(app.exec())