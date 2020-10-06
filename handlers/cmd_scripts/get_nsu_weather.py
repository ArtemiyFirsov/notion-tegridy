from Helpers.Clear import clear
from Services.weather.NSUWeatherAPI import NSUWeatherAPI

try:
    result = NSUWeatherAPI().get_current_temperature()
    print(result)
except:
    print("ERROR")
