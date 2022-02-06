from .product import Product

class Manager():
    __showcase: dict = {}
    def register(self, name: str, proto: Product) -> None:
        self.__showcase[name] = proto

    def create(self, protoname: str) -> Product:
        p: Product = self.__showcase.get(protoname)
        return p.createClone()
