# -*- coding: utf-8 -*-

import simple_draw as sd
import random

# На основе кода из lesson_004/05_snowfall.py
# сделать модуль snowfall.py в котором реализовать следующие функции


# В текущем модуле реализовать главный цикл падения снежинок,
# обращаясь ТОЛЬКО к функциям модуля snowfall


_point_x = []
_point_y = []
_count = []


#  создать_снежинки(N) - создает N снежинок
def create_snow(N):
    # глобальное переменное для доступа на всех функциях
    global _point_x, _point_y

    for i in range(N):
        _point_x.append(sd.random_number(50, 1000))

    for i in range(N):
        _point_y.append(sd.random_number(630, 650))


#  нарисовать_снежинки_цветом(color) - отрисовывает все снежинки цветом color
def draw_snow_color(color):
    sd.start_drawing()
    for i in range(len(_point_x)):
        center = sd.get_point(_point_x[i], _point_y[i])
        #  - отрисовка снежинки с цветом color
        sd.snowflake(center=center, length=50, color=color)
    sd.finish_drawing()


#  сдвинуть_снежинки() - сдвигает снежинки на один шаг
def move_snowflakes():
    for i in range(len(_point_x)):
        _point_y[i] = _point_y[i] - sd.random_number(10, 100)  # верт.скорость падения снега


#  номера_достигших_низа_экрана() - выдает список номеров снежинок, которые вышли за границу экрана
def screen_numbers_reached_down():
    global _count
    _count = []
    for i in range(len(_point_x)):
        if _point_y[i] < sd.random_number(80, 101):
            _count.append(i)
    return _count


#  удалить_снежинки(номера) - удаляет снежинки с номерами из списка
def delete_snowflakes(count):
    center = sd.get_point(_point_x[count], _point_y[count])
    sd.start_drawing()
    sd.snowflake(center=center, length=50, color=sd.background_color)
    sd.finish_drawing()
    del _point_x[count]
    del _point_y[count]

