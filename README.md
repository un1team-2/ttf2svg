## Зависимости

* fonttools (version 4.28.3) ```pip install fonttools==4.28.3```
* beautifulSoup (version 4.10) ```pip install beautifulsoup==4.10```

## Пример

1. Скопируйте этот проект в вашу рабочую директорию

2. Специально для Алёны и Даши. Объект glyphs - то, что вам нужно, для каждого символа по списку

```py
import ttf2svg

glyphs = ttf2svg.get_glyphs('BebasNeue-Regular.ttf')
print("\n".join(glyphs))
```
__По идее, вы можете открывать шрифты любого типа__