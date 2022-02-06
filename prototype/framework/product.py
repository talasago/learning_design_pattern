from __future__ import annotations # 自分自身のクラスを返せるようにする。
from abc import ABCMeta, abstractmethod

class Product(metaclass=ABCMeta):
    @abstractmethod
    def use(s: str) -> None:
        pass

    @abstractmethod
    def createClone() -> Product:
        pass
