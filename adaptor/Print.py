from abc import ABCMeta, abstractmethod

class Print(metaclass=ABCMeta):
    @abstractmethod
    def printWeek():
        pass

    @abstractmethod
    def printStrong():
        pass
