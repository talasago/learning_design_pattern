class Banner():
    def __init__(self, string: str) -> None:
        self.string: str = string

    def showWithParen(self) -> None:
        print(f'({self.string})')

    def showWithAster(self) -> None:
        print(f'*{self.string}*')
