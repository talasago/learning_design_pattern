from abc import ABCMeta, abstractmethod


class Builder(metaclass=ABCMeta):
    @abstractmethod
    def make_title(self, title: str) -> None:
        pass

    @abstractmethod
    def make_string(self, str: str) -> None:
        pass

    @abstractmethod
    def make_items(self, items: list[str]) -> None:
        pass

    @abstractmethod
    def close(self) -> None:
        pass
