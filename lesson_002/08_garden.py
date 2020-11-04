#!/usr/bin/env python
# -*- coding: utf-8 -*-

# в саду сорвали цветы
garden = ('ромашка', 'роза', 'одуванчик', 'ромашка', 'гладиолус', 'подсолнух', 'роза', )

# на лугу сорвали цветы
meadow = ('клевер', 'одуванчик', 'ромашка', 'клевер', 'мак', 'одуванчик', 'ромашка', )

# создайте множество цветов, произрастающих в саду и на лугу
# garden_set =
# meadow_set =
garden_set = set(garden)
print(garden_set)
meadow_set =set(meadow)
print(meadow_set)

# выведите на консоль все виды цветов
all_flowers = garden_set|meadow_set
print('All flowers:',all_flowers)
# выведите на консоль те, которые растут и там и там
# TODO здесь ваш код

# выведите на консоль те, которые растут в саду, но не растут на лугу
only_garden_flowers = garden_set - meadow_set
print('Flowers that only grow in the garden: ',only_garden_flowers)
# выведите на консоль те, которые растут на лугу, но не растут в саду
only_meadow_flowers =  meadow_set - garden_set
print('Flowers that only grow in the meadow: ',only_meadow_flowers)


