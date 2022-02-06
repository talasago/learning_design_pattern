from framework.product import Product
from functools import reduce
from operator import add
from unicodedata import east_asian_width
import copy

class MessageBox(Product):
    def __init__(self, decochar: str) -> None:
        self.decochar :str = decochar

    def use(self, s: str) -> None:
        length :int = reduce(
            # 全角2文字、半角1文字とする
            add, [2 if east_asian_width(ch) in 'FWA' else 1 for ch in s]
        )

        for _ in range(length + 4):
            print(self.decochar, end='')
        print('')
        print(f'{self.decochar} {s} {self.decochar}')
        for _ in range(length + 4):
            print(self.decochar, end='')
        print('')

    def createClone(self) -> Product:
        try:
            p :Product = copy.copy(self) # 浅いコピー
        except:
            raise
        return p
