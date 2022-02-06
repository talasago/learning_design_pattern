from framework.factory import Factory
from framework.product import Product
from idcard.idcard_factory import IDCardFactory


def main() -> None:
    factory: Factory = IDCardFactory()
    card1: Product = factory.create('user1')
    card2: Product = factory.create('user2')
    card3: Product = factory.create('user3')
    card1.use()
    card2.use()
    card3.use()


if __name__ == '__main__':
    main()
