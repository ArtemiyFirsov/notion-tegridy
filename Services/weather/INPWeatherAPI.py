import re

import requests

from Services.weather.BaseWeatherAPI import BaseWeatherAPI, TempScale, celcius_to_fahrenheit


class INPWeatherAPI(BaseWeatherAPI):
    def get_current_temperature(self, scale: TempScale = TempScale.Celcius) -> float:
        r = requests.get("http://thermo.inp.nsk.su")
        r.encoding = 'utf-8'

        match = re.search("images/temp/temp\d+\.png", r.text)

        if not match:
            raise Exception("Weather data not available")

        temp = float(match.group(0).replace("images/temp/temp", "").replace(".png", ""))

        return temp if scale == TempScale.Celcius else celcius_to_fahrenheit(temp)
