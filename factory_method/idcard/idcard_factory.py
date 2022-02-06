from framework.factory import Factory
from framework.product import Product
from .idcard import IDCard


class IDCardFactory(Factory):
    __onwers = []

    def _createProduct(self, owner: str) -> Product:
        return IDCard(owner)

    def _registerProduct(self, product: Product) -> None:
        self.__onwers.append(product.getOwner())

    def getOnwer(self) -> list:
        return self.__onwers
