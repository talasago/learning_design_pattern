from AbstractDisplay import AbstractDisplay
from unicodedata import east_asian_width
from functools import reduce
from operator import add

class StringDisplay(AbstractDisplay):
    def __init__(self, string: str) -> None:
        self.string :str = string
        #self.width: int = self.__str_len(string)
        self.width: int = reduce(
            # 全角2文字、半角1文字とする
            add, [2 if east_asian_width(ch) in 'FWA' else 1 for ch in string]
        )

    def open(self) -> None:
        self.__printLine()

    def print(self) -> None:
        print(f'|{self.string}|')

    def close(self) -> None:
        self.__printLine()

    def __printLine(self) -> None:
        print('+', end='')
        for _ in range(self.width):
            print('-', end='')
        print('+')
