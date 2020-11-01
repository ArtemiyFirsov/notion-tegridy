import logging

logging.basicConfig()
logging.getLogger().setLevel(logging.ERROR)
logging.captureWarnings(True)


from Services.weather.INPWeatherAPI import INPWeatherAPI


try:
    result = INPWeatherAPI().get_current_temperature()
    print(result)
except Exception as e:
    print("ERROR")
