from abstract_display import AbstractDisplay
from char_display import CharDisplay
from string_display import StringDisplay


def main() -> None:
    d1: AbstractDisplay = CharDisplay('H')
    d2: AbstractDisplay = StringDisplay('Hello, world!')
    d3: AbstractDisplay = StringDisplay('こんにちは.')

    d1.display()
    d2.display()
    d3.display()


if __name__ == '__main__':
    main()
