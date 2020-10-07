import re

import requests
from bs4 import BeautifulSoup

from Services.weather.BaseWeatherAPI import BaseWeatherAPI, TempScale, celcius_to_fahrenheit


class INPWeatherAPI(BaseWeatherAPI):
    def get_current_temperature(self, scale: TempScale = TempScale.Celcius) -> float:
        r = requests.get("http://thermo.inp.nsk.su")
        r.encoding = 'utf-8'

        soup = BeautifulSoup(r.text, 'html.parser')

        result = soup.find(id="temp_block")

        if not result:
            raise Exception("Weather data not available")

        results = list(result.children)

        if len(results) == 0:
            raise Exception("Weather data not available")

        temp = ""
        for res in results:
            try:
                src = res.get("src")
            except:
                continue

            if "-" in src:
                temp += "-"

            match = re.search(r"\d", res.get("src"))
            if not match:
                continue

            temp += match.group(0)

        temp = float(temp)

        return temp if scale == TempScale.Celcius else celcius_to_fahrenheit(temp)
