from listfactory.list_page import ListPage
from listfactory.list_tray import ListTray
from factory.factory import Factory
from factory.link import Link
from factory.page import Page
from factory.tray import Tray
from listfactory.list_link import ListLink


class ListFactory(Factory):
    def create_link(self, caption: str, url: str) -> Link:
        return ListLink(caption, url)

    def create_tray(self, caption: str) -> Tray:
        return ListTray(caption)

    def create_page(self, title: str, author: str) -> Page:
        return ListPage(title, author)
