from typing import final
from display_impl import DisplayImpl


class Display():
    def __init__(self, impl: DisplayImpl) -> None:
        self.__impl: DisplayImpl = impl

    def open(self) -> None:
        self.__impl.rawOpen()

    def print(self) -> None:
        self.__impl.rawPrint()

    def close(self) -> None:
        self.__impl.rawClose()

    @final
    def display(self) -> None:
        self.open()
        self.print()
        self.close()
