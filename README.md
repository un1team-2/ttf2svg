## Dependencies
* fonttools (version 4.28.3) ```pip install fonttools==4.28.3```

## Example

```py
import ttf2svg

svg_symbols = ttf2svg.convert_font_to_svg('font.ttf')
print(len(svg_symbols))
```
