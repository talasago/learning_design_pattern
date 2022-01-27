from framework.product import Product

class IDCard(Product):
    def __init__(self, owner: str) -> None:
        print(f'{owner}のカードを作ります')
        self.owner: str = owner

    def use(self) -> None:
        print(f'{self.owner}のカードを使います')

    def getOwner(self) -> str:
        return self.owner
