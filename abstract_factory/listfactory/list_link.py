from factory.link import Link


class ListLink(Link):
    def __init__(self, caption: str, url: str) -> None:
        super().__init__(caption, url)

    def make_html(self) -> str:
        return f'  <li><a href="{self._url}">{self._caption}</a></li>'
