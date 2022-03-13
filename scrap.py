from . import fonts2svg
from bs4 import BeautifulSoup


def get_svg_paths(html):
    return [path.get('d') for path in BeautifulSoup(html, 'html.parser').find_all('path')]
