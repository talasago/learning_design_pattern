from abc import ABCMeta, abstractmethod
from typing import final
from .product import Product


class Factory(metaclass=ABCMeta):
    @final
    def create(self, owner: str) -> Product:
        p: Product = self._createProduct(owner)
        self._registerProduct(p)
        return p

    @abstractmethod
    def _createProduct(self, owner: str) -> Product:
        pass

    @abstractmethod
    def _registerProduct(self, product: Product) -> None:
        pass
