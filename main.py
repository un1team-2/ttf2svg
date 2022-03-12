from . import fonts2svg
from . import scrap

def convert_font_to_svg(font: str) -> list:
    return fonts2svg.mainInMemory(['-c', '000000', font])

def get_glyphs(font: str) -> list:
    return scrap.get_svg_paths("\n".join(convert_font_to_svg(font)))
