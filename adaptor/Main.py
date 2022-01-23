
from Print import Print
from PrintBanner import PrintBanner

def main() -> None:
    p :Print = PrintBanner('Hello')
    p.printWeek()
    p.printStrong()

if __name__ == '__main__':
    main()
