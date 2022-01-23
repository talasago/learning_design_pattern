from AbstractDisplay import AbstractDisplay
from CharDisplay import CharDisplay
from StringDisplay import StringDisplay


def main() -> None:
    d1 :AbstractDisplay = CharDisplay('H')
    d2 :AbstractDisplay = StringDisplay('Hello, world!')
    d3 :AbstractDisplay = StringDisplay('こんにちは.')

    d1.display()
    d2.display()
    d3.display()

if __name__ == '__main__':
    main()
