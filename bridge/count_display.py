from display import Display
from display_impl import DisplayImpl


class CountDisplay(Display):
    def __init__(self, impl: DisplayImpl) -> None:
        super().__init__(impl)

    def multi_display(self, times: int) -> None:
        self.open()
        for _ in range(times):
            self.print()
        self.close()
