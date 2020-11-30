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

_count = []


def create_snow(N):
    # глобальное переменное для доступа на всех функциях
    global _point_x, _point_y

    for i in range(N):
        _point_x.append(sd.random_number(50, 1000))

    for i in range(N):
        _point_y.append(sd.random_number(550, 600))


def draw_snow_color(color):
    sd.start_drawing()
    for i in range(len(_point_x)):
        center = sd.get_point(_point_x[i], _point_y[i])
        #  - отрисовка снежинки с цветом color
        sd.snowflake(center=center, length=50, color=color)

    sd.finish_drawing()


def move_snowflakes():
    # - сдвинуть снежинку
    for i in range(len(_point_x)):
        _point_y[i] = _point_y[i] - sd.random_number(10, 20)


def screen_numbers_reached_down():
    global _count
    for i in range(len(_point_x)):
        if _point_y[i] < sd.random_number(40, 60):
            _count.append(i)
    print(_count)
    return _count


def delete_snowflakes(count):
    for i in range(len(count)):
        center = sd.get_point(_point_x[count[i]], _point_y[count[i]])
        sd.start_drawing()
        sd.snowflake(center=center, length=50, color=sd.background_color)
        sd.finish_drawing()

        del _point_x[count[i]]
        del _point_y[count[i]]
