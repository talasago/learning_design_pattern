from __future__ import annotations
from abc import ABCMeta, abstractmethod
from importlib import import_module

from factory.link import Link
from factory.page import Page
from factory.tray import Tray


class Factory(metaclass=ABCMeta):
    @classmethod
    def get_factory(cls, class_name: str) -> Factory:
        module, class_ = class_name.rsplit('.', 1)
        return getattr(import_module(module), class_)()

    @abstractmethod
    def create_link(self, caption: str, url: str) -> Link:
        pass

    @abstractmethod
    def create_tray(self, caption: str) -> Tray:
        pass

    @abstractmethod
    def create_page(self, title: str, author: str) -> Page:
        pass
