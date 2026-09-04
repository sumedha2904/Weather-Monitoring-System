import sensor_thresholds


class Alerter:

    def check(self, sensor):

        raw_data = sensor.raw_data

        temperature = float(raw_data.split('"Temperature":')[1].split(',')[0])

        humidity = float(raw_data.split('"Humidity":')[1].split(',')[0])

        pressure = float(raw_data.split('"Pressure":')[1].split('}')[0])

        if temperature < sensor_thresholds.TEMPERATURE_LOW:
            print("ALERT: Temperature is critically low")

        elif temperature > sensor_thresholds.TEMPERATURE_HIGH:
            print("ALERT: Temperature is critically high")

        if humidity < sensor_thresholds.HUMIDITY_LOW:
            print("ALERT: Humidity is critically low")

        elif humidity > sensor_thresholds.HUMIDITY_HIGH:
            print("ALERT: Humidity is critically high")

        if pressure < sensor_thresholds.PRESSURE_LOW:
            print("ALERT: Pressure is critically low")

        elif pressure > sensor_thresholds.PRESSURE_HIGH:
            print("ALERT: Pressure is critically high")
