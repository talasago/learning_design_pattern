
from print import Print
from print_banner import PrintBanner


def main() -> None:
    p: Print = PrintBanner('Hello')
    p.printWeek()
    p.printStrong()


if __name__ == '__main__':
    main()
