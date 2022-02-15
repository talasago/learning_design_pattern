from factory.page import Page


class ListPage(Page):
    def __init__(self, title: str, author: str) -> None:
        super().__init__(title, author)

    def make_html(self) -> str:
        str_buf: list = []

        str_buf.append('<html><head><title></title></head>')
        str_buf.append('<body>')
        str_buf.append(f'<h1>{self.title}</h1>')
        str_buf.append('<ul>')

        for item in self._content:
            str_buf.append(item.make_html())
        str_buf.append('</ul>')
        str_buf.append(f'<hr><adress>{self.author}</adress>')
        str_buf.append('</body></html>')
        return '\n'.join(str_buf)
