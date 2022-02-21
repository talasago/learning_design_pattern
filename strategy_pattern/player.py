from strategy import Strategy
from hand import Hand


class Player:
    __wincount: int = 0
    __losecount: int = 0
    __gamecount: int = 0

    def __init__(self, name: str, strategy: Strategy) -> None:
        self.__name: str = name
        self.__strategy: Strategy = strategy

    def next_hand(self) -> Hand:
        return self.__strategy.next_hand()

    def win(self) -> None:
        self.__strategy.study(True)
        self.__wincount += 1
        self.__gamecount += 1

    def lose(self) -> None:
        self.__strategy.study(False)
        self.__losecount += 1
        self.__gamecount += 1

    def even(self) -> None:
        self.__gamecount += 1

    def __str__(self) -> str:
        return f'[{self.__name}:{self.__gamecount} games, ' + \
               f'{self.__wincount} win, {self.__losecount} lose]'
