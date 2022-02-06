from framework.product import Product
from functools import reduce
from operator import add
from unicodedata import east_asian_width
import copy


class UnderLinePen(Product):
    def __init__(self, ulchar: str) -> None:
        self.ulchar: str = ulchar

    def use(self, s: str) -> None:
        length: int = reduce(
            # 全角2文字、半角1文字とする
            add, [2 if east_asian_width(ch) in 'FWA' else 1 for ch in s]
        )

        print(f'"{s}"')
        print(self.ulchar, end='')
        for _ in range(length):
            print(self.ulchar, end='')
        print('')

    def createClone(self) -> Product:
        return copy.deepcopy(self)
