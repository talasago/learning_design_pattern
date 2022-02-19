import io
from builder import Builder


class HtmlBuilder(Builder):
    def make_title(self, title: str):
        self.__file_name = f'{title}.html'
        self.__file: io.TextIOWrapper = io.open(self.__file_name, 'w',
                                                encoding='utf-8', newline='\n')
        self.__file.write(
            f'<html><head><title>{title}</title></head></body>\n')
        self.__file.write(f'<h1>{title}</h1>\n')

    def make_string(self, str: str) -> None:
        self.__file.write(f'<p>{str}</p>\n')

    def make_items(self, items: list[str]) -> None:
        self.__file.write('<ul>\n')
        for item in items:
            self.__file.write(f'<li>{item}</li>\n')
        self.__file.write('</ul>\n')

    def close(self) -> None:
        self.__file.write('</body></html>\n')
        self.__file.close()

    def get_result(self) -> str:
        return self.__file_name
