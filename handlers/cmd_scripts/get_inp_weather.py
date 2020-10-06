from Services.weather.INPWeatherAPI import INPWeatherAPI

try:
    result = INPWeatherAPI().get_current_temperature()
    print(result)
except:
    print("ERROR")
