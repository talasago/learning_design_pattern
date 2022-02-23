from __future__ import annotations
from enum import Enum
from typing import Final


class HandValue(int, Enum):
    ROCK: Final[int] = 0
    SCISSORS: Final[int] = 1
    PAPER: Final[int] = 2


class FightResultValue(int, Enum):
    WIN: Final[int] = 1
    LOSE: Final[int] = -1
    DRAW: Final[int] = 0


class Hand:
    hands: list[Hand] = []

    def __init__(self, hand_value: int) -> None:
        self.__hand_value: int = hand_value

    @classmethod
    def get_hand(cls, hand_value: int) -> Hand:
        return cls.hands[hand_value]

    def is_stronger_than(self, h: Hand) -> bool:
        return self.__fight(h) == FightResultValue.WIN.value

    def is_weeker_than(self, h: Hand) -> bool:
        return self.__fight(h) == FightResultValue.LOSE.value

    def __fight(self, h: Hand) -> int:
        if self.__hand_value == h.__hand_value:
            return FightResultValue.DRAW.value
        elif (self.__hand_value + 1) % 3 == h.__hand_value:
            return FightResultValue.WIN.value
        else:
            return FightResultValue.LOSE.value


Hand.hands.append(Hand(HandValue.ROCK.value))
Hand.hands.append(Hand(HandValue.SCISSORS.value))
Hand.hands.append(Hand(HandValue.PAPER.value))
