from Helpers.stdIOhelpers import disable_warnings
disable_warnings()

from Services.weather.INPWeatherAPI import INPWeatherAPI


try:
    result = INPWeatherAPI().get_current_temperature()
    print(result)
except Exception as e:
    print("ERROR")
