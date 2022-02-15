from abc import ABCMeta, abstractmethod
from .item import Item


class Page(metaclass=ABCMeta):
    _content: list = []

    def __init__(self, title: str, author: str) -> None:
        self.title: str = title
        self.author: str = author

    def add(self, item: Item) -> None:
        self._content.append(item)

    def output(self) -> None:
        filename: str = f'{self.title}.html'
        with open(filename, mode='w') as f:
            f.write(self.make_html())
            print(f'{filename}を作成しました。')

    @abstractmethod
    def make_html(self) -> str:
        pass
