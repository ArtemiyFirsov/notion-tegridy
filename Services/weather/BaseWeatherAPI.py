from abc import ABCMeta, abstractmethod
from enum import Enum


class TempScale(Enum):
    Celcius = 0
    Fahrenheit = 1


def celcius_to_fahrenheit(value: float):
    return 9.0 / 5.0 * value + 32


class BaseWeatherAPI(metaclass=ABCMeta):
    @abstractmethod
    def get_current_temperature(self, scale: TempScale) -> float:
        raise NotImplementedError()