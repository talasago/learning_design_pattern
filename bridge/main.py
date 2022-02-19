from count_display import CountDisplay
from display import Display
from string_display_impl import StringDisplayImpl


def main() -> None:
    d1: Display = Display(StringDisplayImpl('Hello, Japan.'))
    d2: Display = CountDisplay(StringDisplayImpl('Hello, Workd.'))
    d3: CountDisplay = CountDisplay(StringDisplayImpl('Hello, Univarse.'))
    d1.display()
    d2.display()
    d3.display()
    d3.multi_display(5)


if __name__ == '__main__':
    main()
