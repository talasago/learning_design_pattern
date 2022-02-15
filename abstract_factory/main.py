import sys

from factory.link import Link
from factory.page import Page
from factory.tray import Tray
from factory.factory import Factory


def main():
    args = sys.argv
    if len(args) != 2:
        print('Usage: python      moduledirectory.modulename.ConcreteFactory')
        print('Example 1: python  moduledirectory.modulename.ListFactory')
        exit(0)

    factory: Factory = Factory.get_factory(args[1])

    asahi: Link = factory.create_link('朝日新聞', 'https://www.asahi.com/')
    yomiuri: Link = factory.create_link('読売新聞', 'https://www.yomiuri.co.jp/')

    traynews: Tray = factory.create_tray('新聞')
    traynews.add(asahi)
    traynews.add(yomiuri)

    page: Page = factory.create_page('LinkPage', '著者')
    page.add(traynews)
    page.output()


if __name__ == '__main__':
    main()
