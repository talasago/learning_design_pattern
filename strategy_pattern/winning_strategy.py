import random

from hand import Hand
from strategy import Strategy


class WinningStrategy(Strategy):
    __won: bool = False
    __prev_hand: Hand

    def __init__(self, seed: int) -> None:
        random.seed(seed)

    def next_hand(self) -> Hand:
        if not self.__won:
            self.__prev_hand = Hand.get_hand(random.randint(0, 2))
        return self.__prev_hand

    def study(self, win: bool) -> None:
        self.__won = win
