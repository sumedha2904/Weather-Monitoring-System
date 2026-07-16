SENSOR_THRESHOLDS = {
    "pt100_temperature": {
        "unit": "°C",
        "min_normal": -10,
        "max_normal": 45,
        "critical_low": 0,      # frost risk
        "critical_high": 40,    # heat warning
    },

    "humidity": {
        "unit": "%RH",
        "min_normal": 30,
        "max_normal": 70,
        "critical_low": 20,     # very dry
        "critical_high": 85,    # condensation/mold risk
    },

    "pressure": {
        "unit": "hPa",
        "min_normal": 1000,
        "max_normal": 1025,
        "critical_low": 990,    # storm system approaching
        "critical_high": 1030,  # stable/dry high-pressure
    },
}