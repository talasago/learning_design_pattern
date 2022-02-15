from .item import Item


class Link(Item):
    def __init__(self, caption: str, url: str) -> None:
        super().__init__(caption)
        self._url = url
