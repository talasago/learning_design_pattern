from abc import ABCMeta, abstractclassmethod


class DisplayImpl(metaclass=ABCMeta):
    @abstractclassmethod
    def rawOpen(self) -> None:
        pass

    @abstractclassmethod
    def rawPrint(self) -> None:
        pass

    @abstractclassmethod
    def rawClose(self) -> None:
        pass
