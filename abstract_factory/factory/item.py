
from abc import ABCMeta, abstractmethod


class Item(metaclass=ABCMeta):
    def __init__(self, caption: str) -> None:
        self._caption: str = caption

    @abstractmethod
    def make_html(self) -> str:
        pass
