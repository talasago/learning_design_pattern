from abstract_display import AbstractDisplay


class CharDisplay(AbstractDisplay):
    def __init__(self, ch: str) -> None:
        self.ch: str = ch

    def open(self) -> None:
        print('<<', end='')

    def print(self) -> None:
        print(self.ch, end='')

    def close(self) -> None:
        print('>>')
