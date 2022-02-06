from abc import ABCMeta, abstractmethod


class Print(metaclass=ABCMeta):
    @abstractmethod
    def printWeek(self) -> None:
        pass

    @abstractmethod
    def printStrong(self) -> None:
        pass
