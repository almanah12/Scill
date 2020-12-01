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
        elif isinstance(self, Water) and isinstance(other, Fire):
            return Steam()
        elif isinstance(self, Water) and isinstance(other, Earth):
            return Dirt()

    __radd__ = __add__


class Air:
    def __str__(self):
        return 'Air'

    def __add__(self, other):
        if isinstance(self, Air) and isinstance(other, Water):
            return Storm()
        elif isinstance(self, Air) and isinstance(other, Fire):
            return Lightning()
        elif isinstance(self, Air) and isinstance(other, Earth):
            return Dust()


class Fire:
    def __str__(self):
        return 'Fire'

    def __add__(self, other):
        if isinstance(self, Fire) and isinstance(other, Water):
            return Steam()
        elif isinstance(self, Fire) and isinstance(other, Air):
            return Lightning()
        elif isinstance(self, Fire) and isinstance(other, Earth):
            return Lava()


class Earth:
    def __str__(self):
        return 'Earth'

    def __add__(self, other):
        if isinstance(self, Earth) and isinstance(other, Water):
            return Dirt()
        elif isinstance(self, Earth) and isinstance(other, Fire):
            return Lava()
        elif isinstance(self, Earth) and isinstance(other, Air):
            return Dust()


class Dust:
    def __str__(self):
        return 'Dust'


class Lava:
    def __str__(self):
        return 'Lava'


class Dirt:
    def __str__(self):
        return 'Dirt'


class Lightning:
    def __str__(self):
        return 'Lightning'


class Steam:
    def __str__(self):
        return 'Steam'


class Storm:
    def __str__(self):
        return 'Storm'


print(Water(), '+', Air(), '=', Air() + Water())
print(Water(), '+', Fire(), '=', Water() + Fire())
print(Water(), '+', Fire(), '=', Earth() + Water())
print(Air(), '+', Fire(), '=', Air() + Fire())
print(Air(), '+', Earth(), '=', Air() + Earth())
print(Fire(), '+', Earth(), '=', Fire() + Earth())
# Усложненное задание (делать по желанию)
# Добавить еще элемент в игру.
# Придумать что будет при сложении существующих элементов с новым.
