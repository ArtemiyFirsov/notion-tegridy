from abc import ABCMeta, abstractmethod
from typing import List


class BaseNotionAPI(metaclass=ABCMeta):
    @abstractmethod
    def add_todos(self, page_url: str, todos: List[str]):
        raise NotImplementedError()

    @abstractmethod
    def sort_todos(self, page_url: str):
        raise NotImplementedError()

    @abstractmethod
    def delete_todos_duplicates(self, page_url: str):
        raise NotImplementedError()
