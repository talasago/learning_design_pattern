import random
from functools import reduce
from operator import add

from hand import Hand, HandValue
from strategy import Strategy


class ProbStrategy(Strategy):
    __prev_hand_value: int = HandValue.ROCK
    __current_hand_value: int = HandValue.ROCK
    __history: list[list[int]] = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]

    def __init__(self, seed: int) -> None:
        random.seed(seed)

    def next_hand(self) -> Hand:
        bet: int = random.randint(0, reduce(
            add, [self.__history[self.__current_hand_value][i] for i in range(2)])
        )

        hand_value: int = 0
        if bet < self.__history[self.__current_hand_value][HandValue.ROCK.value]:
            hand_value = HandValue.ROCK.value
        elif bet < self.__history[self.__current_hand_value][HandValue.ROCK.value] + \
                self.__history[self.__current_hand_value][HandValue.SCISSORS.value]:
            hand_value = HandValue.SCISSORS.value
        else:
            hand_value = HandValue.PAPER.value

        self.__prev_hand_value = self.__current_hand_value
        self.__current_hand_value = hand_value
        return Hand.get_hand(hand_value)

    def study(self, win: bool) -> None:
        if win:
            self.__history[self.__prev_hand_value][self.__current_hand_value] += 1
        else:
            self.__history[self.__prev_hand_value][(self.__current_hand_value + 1) % 3] += 1
            self.__history[self.__prev_hand_value][(self.__current_hand_value + 2) % 3] += 1
