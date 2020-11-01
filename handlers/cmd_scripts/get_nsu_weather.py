import logging

logging.basicConfig()
logging.getLogger().setLevel(logging.ERROR)
logging.captureWarnings(True)

from Services.weather.NSUWeatherAPI import NSUWeatherAPI

try:
    result = NSUWeatherAPI().get_current_temperature()
    print(result)
except Exception as e:
    print("ERROR")
