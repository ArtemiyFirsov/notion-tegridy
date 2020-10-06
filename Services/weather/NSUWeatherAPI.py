import re

import requests

from Services.weather.BaseWeatherAPI import BaseWeatherAPI, TempScale, celcius_to_fahrenheit


class NSUWeatherAPI(BaseWeatherAPI):
    def get_current_temperature(self, scale: TempScale = TempScale.Celcius) -> float:
        r = requests.get("http://weather.nsu.ru/loadata.php")
        r.encoding = 'utf-8'

        match = re.search(r"Температура около НГУ (?:-)\d+\.\d+", r.text)

        if not match:
            raise Exception("Weather data not available")

        temp = float(match.group(0).replace("Температура около НГУ ", ""))

        return temp if scale == TempScale.Celcius else celcius_to_fahrenheit(temp)
