class Book():
    def __init__(self, name) -> None:
        self.__name = name

    @property
    def name(self):
        pass

    @name.getter
    def name(self):
        return self.__name
