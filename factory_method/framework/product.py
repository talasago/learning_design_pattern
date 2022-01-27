from abc import ABCMeta, abstractmethod

class Product(metaclass=ABCMeta):
    @abstractmethod
    def use() -> None:
        pass
