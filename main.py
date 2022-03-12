from ttf2svg import fonts2svg


def convert_font_to_svg(font: str) -> list:
    return fonts2svg.mainInMemory(['-c', '000000', font])
