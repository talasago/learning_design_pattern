from abc import ABCMeta, abstractmethod
from typing import final


class AbstractDisplay(metaclass=ABCMeta):
    @abstractmethod
    def open(self) -> None:
        pass

    @abstractmethod
    def print(self) -> None:
        pass

    @abstractmethod
    def close(self) -> None:
        pass

    @final
    def display(self) -> None:
        self.open()
        for _ in range(5):
            self.print()
        self.close()
