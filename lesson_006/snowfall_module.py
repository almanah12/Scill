# -*- coding: utf-8 -*-

import simple_draw as sd
import random

# На основе кода из lesson_004/05_snowfall.py
# сделать модуль snowfall.py в котором реализовать следующие функции
#  создать_снежинки(N) - создает N снежинок
#  нарисовать_снежинки_цветом(color) - отрисовывает все снежинки цветом color
#  сдвинуть_снежинки() - сдвигает снежинки на один шаг
#  номера_достигших_низа_экрана() - выдает список номеров снежинок, которые вышли за границу экрана
#  удалить_снежинки(номера) - удаляет снежинки с номерами из списка
#
# В текущем модуле реализовать главный цикл падения снежинок,
# обращаясь ТОЛЬКО к функциям модуля snowfall

_point_x = []
_point_y = []


def create_snow(N):
    global _point_x
    for i in range(N):
        _point_x.append(sd.random_number(50, 1000))

    point_y = []
    for i in range(N):
        _point_y.append(sd.random_number(550, 600))


def draw_snow_color(color):
    sd.start_drawing()
    for i in range(len(_point_x)):
        center = sd.get_point(_point_x[i], _point_y[i])
        #  - на старом месте снежинки отрисовать её же, но цветом sd.background_color
        sd.snowflake(center=center, length=50, color=color)

        # #  - отрисовать её цветом sd.COLOR_WHITE на новом месте
        # sd.snowflake(center=shifted_point, length=length_snowflakes[i], color=sd.COLOR_WHITE)
        # #  Для сохр след. итерации
        # point_y[i] -= step_falloff_snowflakes[i]

    sd.finish_drawing()


def move_snowflakes():
    #  - сдвинуть снежинку
    for i in range(len(_point_x)):
        shifted_snowflake_y = _point_y[i] - 20
        shifted_point = sd.get_point(_point_x[i], shifted_snowflake_y)
        sd.snowflake(center=shifted_point, length=50, color=sd.COLOR_WHITE)

def screen_numbers_reached_down():
    pass


def delete_snowflakes(numbers):
    pass


