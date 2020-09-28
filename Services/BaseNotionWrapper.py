from abc import ABCMeta, abstractmethod
from typing import List


class BaseNotionAPI(metaclass=ABCMeta):
    @abstractmethod
    def add_todos(self, todos: List[str]):
        raise NotImplementedError()