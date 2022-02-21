from abc import ABCMeta, abstractmethod
from hand import Hand


class Strategy(metaclass=ABCMeta):
    @abstractmethod
    def next_hand(self) -> Hand:
        pass

    @abstractmethod
    def study(self, win: bool) -> None:
        pass
