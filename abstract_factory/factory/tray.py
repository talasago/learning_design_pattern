from .item import Item


class Tray(Item):
    _tray: list = []

    def __init__(self, caption: str) -> None:
        super().__init__(caption)

    def add(self, item: Item) -> None:
        self._tray.append(item)
