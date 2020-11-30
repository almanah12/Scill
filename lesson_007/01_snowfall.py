# -*- coding: utf-8 -*-

import simple_draw as sd

# Шаг 1: Реализовать падение снежинки через класс. Внести в методы:
#  - создание снежинки с нужными параметрами
#  - отработку изменений координат
#  - отрисовку
sd.resolution = [1000, 600]
N = 2

class Snowflake:
    def __init__(self):
        self.x = sd.random_number(100, 900)
        self.y = sd.random_number(550, 570)
        self.length = sd.random_number(30, 70)

    def clear_previous_picture(self):
        sd.clear_screen()

    def draw(self):
        center = sd.get_point(self.x, self.y)
        sd.snowflake(center=center, length=self.length,)

    def move(self):
        self.y -= 50

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
count = 0
list_flakes = []
def get_flakes(count):

    for i in range(count):
        list_flakes.append(Snowflake())
    return list_flakes


def get_fallen_flakes():
    global count

    if flake.y <= 50:
        count += 1
        if flake.y >= 50:
            count = 0
    return count


def append_flakes(count):
    for i in range(count):
        list_flakes.append(Snowflake())
    return list_flakes


flakes = get_flakes(count=N)  # создать список снежинок

while True:
    flake.clear_previous_picture()
    for flake in flakes:
        flake.move()
        flake.draw()
        fallen_flakes = get_fallen_flakes()  # подчитать сколько снежинок уже упало

    if fallen_flakes:
        append_flakes(count=fallen_flakes)  # добавить еще сверху

    sd.sleep(0.1)
    if sd.user_want_exit():
        break

sd.pause()
