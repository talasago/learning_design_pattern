from book import Book


class BookShelf():
    def __init__(self) -> None:
        self.__books: list[Book] = []

    def getBookAt(self, index: int) -> Book:
        return self.__books[index]

    def appendBook(self, book: Book) -> None:
        self.__books.append(book)

    def getLength(self) -> int:
        return len(self.__books)

    def __iter__(self):
        return BookShelfIterator(self)


class BookShelfIterator():
    def __init__(self, bf: BookShelf):
        self.__index: int = 0
        self.bf: BookShelf = bf

    def __next__(self) -> Book:
        if self.__index >= self.bf.getLength():
            raise StopIteration

        book: Book = self.bf.getBookAt(self.__index)
        self.__index += 1

        return book
