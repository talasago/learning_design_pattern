from unicodedata import east_asian_width
from functools import reduce
from operator import add
from display_impl import DisplayImpl


class StringDisplayImpl(DisplayImpl):
    def __init__(self, string: str) -> None:
        self.__str: str = string
        self.__width: int = reduce(
            # 全角2文字、半角1文字とする
            add, [2 if east_asian_width(ch) in 'FWA' else 1 for ch in string]
        )

    def rawOpen(self) -> None:
        self.__print_line()

    def rawPrint(self) -> None:
        print(f'|{self.__str}|')

    def rawClose(self) -> None:
        self.__print_line()

    def __print_line(self) -> None:
        print('+', end='')
        for _ in range(self.__width):
            print('-', end='')
        print('+')
