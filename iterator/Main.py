from Book import Book
from BookShelf import BookShelf

def main():
    bs: BookShelf = BookShelf(4)
    bs.appendBook(Book("Javaで学ぶデザインパターン入門"))
    bs.appendBook(Book("実践Python3"))
    bs.appendBook(Book("リーダブルコード"))
    bs.appendBook(Book("ソフトウェアテストの教科書"))

    for book in iter(bs):
        print(book.name)

if __name__ == '__main__':
    main()
