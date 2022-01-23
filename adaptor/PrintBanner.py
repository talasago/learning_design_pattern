from Print import Print
from Banner import Banner

class PrintBanner(Print):
    def __init__(self, string: str) -> None:
        self.banner :Banner = Banner(string)

    def printWeek(self) -> None:
        self.banner.showWithParen()

    def printStrong(self) -> None:
        self.banner.showWithAster()
