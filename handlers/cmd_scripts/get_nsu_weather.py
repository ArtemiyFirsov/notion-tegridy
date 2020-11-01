from Helpers.stdIOhelpers import disable_warnings
disable_warnings()

from Services.weather.NSUWeatherAPI import NSUWeatherAPI

try:
    result = NSUWeatherAPI().get_current_temperature()
    print(result)
except Exception as e:
    print("ERROR")
