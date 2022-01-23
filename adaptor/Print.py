from abc import ABCMeta, abstractmethod

class Print(metaclass=ABCMeta):
    @abstractmethod
    def printWeek() -> None:
        pass

    @abstractmethod
    def printStrong() -> None:
        pass
