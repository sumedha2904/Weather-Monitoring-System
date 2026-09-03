import re

import sensor_thresholds

class Alerter:

    def check(self, sensor):
        raw_data = sensor.raw_data
        alerts = []

        temperature = re.search(r'"Temperature"\s*\s*(-?:\.\d+)', raw_data)
        pressure = re.search(r'"Pressure"\s*\s*(-?:\.\d+)', raw_data)
        humidity = re.search(r'"Humidity"\s*\s*(-?:\.\d+)', raw_data)

        if temperature:
            temperature = float(temperature.group(1))

            if temperature < TEMPERATURE_LOW:
                alerts.append("Temperature is critically low")

            elif temperature > TEMPERATURE_HIGH:
                alerts.append("Temperature is critically high")

        if humidity:
            humidity = float(humidity.group(1))

            if humidity < HUMIDITY_LOW:
                alerts.append("Humidity is critically low")

            elif humidity > HUMIDITY_HIGH:
                alerts.append("Humidity is critically high")

        if pressure:
            pressure = float(pressure.group(1))

            if pressure < PRESSURE_LOW:
                alerts.append("Pressure is critically low")

            elif pressure > PRESSURE_HIGH:
                alerts.append("Pressure is critically high")

        return alerts

