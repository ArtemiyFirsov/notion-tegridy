from Helpers.stdIOhelpers import disable_warnings
import logging

disable_warnings()
logging.basicConfig()
logging.getLogger().setLevel(logging.ERROR)

from Services.weather.NSUWeatherAPI import NSUWeatherAPI

try:
    result = NSUWeatherAPI().get_current_temperature()
    print(result)
except Exception as e:
    print("ERROR")
