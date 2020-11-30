# -*- coding: utf-8 -*-

import simple_draw as sd

# Шаг 1: Реализовать падение снежинки через класс. Внести в методы:
#  - создание снежинки с нужными параметрами
#  - отработку изменений координат
#  - отрисовку
sd.resolution = [1000, 600]
N = 10
_count = []
list_flakes = []


class Snowflake:
    def __init__(self):
        self.x = sd.random_number(100, 900)
        self.y = sd.random_number(550, 570)
        self.length = sd.random_number(30, 70)

    def clear_previous_picture(self):
        sd.clear_screen()

    def draw(self):
        center = sd.get_point(self.x, self.y)
        sd.snowflake(center=center, length=self.length, color=sd.random_color() )

    def move(self):
        self.y -= sd.random_number(50, 150)

    def can_fall(self):
        return self.y >= 300


flake = Snowflake()

# while True:
#     flake.clear_previous_picture()
#     flake.move()
#     flake.draw()
#     if not flake.can_fall():
#         break
#     sd.sleep(0.1)
#     if sd.user_want_exit():
#         break

# шаг 2: создать снегопад - список объектов Снежинка в отдельном списке, обработку примерно так:


def get_flakes(count):
    for i in range(count):
        list_flakes.append(Snowflake())
    return list_flakes


def get_fallen_flakes():
    global _count
    _count = []
    for i in range(N):
        if list_flakes[i].y <= 50:
            _count.append(i)
    return _count


def append_flakes(count):
    for _ in range(count):
        list_flakes.append(Snowflake())
    return list_flakes


flakes = get_flakes(count=N)  # создать список снежинок

while True:
    flake.clear_previous_picture()
    for flake in flakes:
        flake.move()
        flake.draw()
        get_fallen_flakes()  # подчитать сколько снежинок уже упало

    fallen_flakes = get_fallen_flakes()
    if len(fallen_flakes):
        for i in get_fallen_flakes():
            del flakes[i]
            append_flakes(count=1)  # добавить еще сверху

    sd.sleep(0.5)
    if sd.user_want_exit():
        break

sd.pause()
