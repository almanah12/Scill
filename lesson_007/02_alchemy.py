# -*- coding: utf-8 -*-

# Создать прототип игры Алхимия: при соединении двух элементов получается новый.
# Реализовать следующие элементы: Вода, Воздух, Огонь, Земля, Шторм, Пар, Грязь, Молния, Пыль, Лава.
# Каждый элемент организовать как отдельный класс.
# Таблица преобразований:
# Сложение элементов реализовывать через __add__
# Если результат не определен - то возвращать None
# Вывод элемента на консоль реализовывать через __str__

#   Вода + Воздух = Шторм
#   Вода + Огонь = Пар
#   Вода + Земля = Грязь
#   Воздух + Огонь = Молния
#   Воздух + Земля = Пыль
#   Огонь + Земля = Лава
# Примеры преобразований:
#   print(Water(), '+', Air(), '=', Water() + Air())
#   print(Fire(), '+', Air(), '=', Fire() + Air())


class Water:
    def __str__(self):
        return 'Water'

    def __add__(self, other):
        if isinstance(self, Water) and isinstance(other, Air):
            return Storm()


class Air:
    def __str__(self):
        return 'Air'

    def __add__(self, other):
        if Water() + Air():
            return Storm()


class Fire:
    def __str__(self):
        return 'Fire'

    def __add__(self, other):
        new_object = Air()


class Earth:
    def __str__(self):
        return 'Earth'

    def __add__(self, other):
        new_object = Air()


class Dust:
    pass


class Lava:
    pass


class Dirt:
    def __str__(self):
        return 'Dirt'


class Lightning:
    pass


class Steam:
    pass


class Storm:
    def __str__(self):
        return 'Storm'


print(Water(), '+', Air(), '=', Air() + Water())
print(Water(), '+', Earth(), '=', Water()+Earth())

# Усложненное задание (делать по желанию)
# Добавить еще элемент в игру.
# Придумать что будет при сложении существующих элементов с новым.
