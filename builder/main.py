import sys
from director import Director
from html_builder import HtmlBuilder
from text_builder import TextBuilder


def main(args: list[str]) -> None:
    director: Director
    if args[1] == 'plain':
        text_builder: TextBuilder = TextBuilder()
        director = Director(text_builder)
        director.construct()
        print(text_builder.get_result())
    elif args[1] == 'html':
        html_builder: HtmlBuilder = HtmlBuilder()
        director = Director(html_builder)
        director.construct()
        print(f'{html_builder.get_result()}が作成されました。')
    else:
        usage()
        exit(0)


def usage() -> None:
    print('Usage: python plain        プレーンテキストで文書を作成')
    print('Usage: python html         HTMLファイルで文書を作成')
    pass


if __name__ == '__main__':
    args = sys.argv
    # print(args)
    # > ['main.py', 'plain']
    if len(args) != 2:
        usage()
        exit(0)
    main(args)
