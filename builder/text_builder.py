from builder import Builder


class TextBuilder(Builder):
    __str_buf: list = []

    def make_title(self, title: str):
        self.__str_buf.append('===============================')
        self.__str_buf.append(f'『{title}』')
        self.__str_buf.append('')

    def make_string(self, str: str) -> None:
        self.__str_buf.append(f'■{str}')
        self.__str_buf.append('')

    def make_items(self, items: list[str]) -> None:
        for item in items:
            self.__str_buf.append(f'  ・{item}')
        self.__str_buf.append('')

    def close(self) -> None:
        self.__str_buf.append('===============================')

    def get_result(self) -> str:
        return '\n'.join(self.__str_buf)
