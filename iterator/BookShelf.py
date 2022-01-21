from Book import Book

class BookShelf():
    def __init__(self, maxsize: int) -> None:
        self.__maxsize = maxsize
        self.__books: list[Book] = []
        self.__index :int = 0

    def getBookAt(self, index: int) -> Book:
        return self.__books[index]

    def appendBook(self, book: Book) -> None:
        # 最大数を検査
        if self.getLength() > self.__maxsize:
            raise IndexError

        self.__books.append(book)

    def getLength(self) -> int:
        return len(self.__books)

    def __iter__(self):
        return self

    def __next__(self) -> Book:
        if self.__index >= self.getLength():
            raise StopIteration

        book :Book = self.getBookAt(self.__index)
        self.__index += 1

        return book
