from factory.tray import Tray


class ListTray(Tray):
    def __init__(self, caption: str) -> None:
        super().__init__(caption)

    def make_html(self) -> str:
        str_buf: list = []

        str_buf.append('<li>')
        str_buf.append(self._caption)
        str_buf.append('<ul>')
        for item in self._tray:
            str_buf.append(item.make_html())
        str_buf.append('</ul>')
        str_buf.append('</li>')
        return '\n'.join(str_buf)
