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

#_point = sd.snowflake(center=sd.get_point(0, 0),)

def create_snow(N):
    global _point
    point_x = []
    for i in range(N):
        point_x.append(sd.random_number(50, 1000))

    point_y = []
    for i in range(N):
        point_y.append(sd.random_number(550, 600))
    for i in range(N):
        center = sd.get_point(point_x[i], point_y[i])
        _point = sd.snowflake(center=center, length=sd.random_number(10, 100), factor_a=random.uniform(.5, .6),
                     factor_b= random.uniform(.3, .4), factor_c=sd.random_number(25, 35))


# def draw_snow_color(color):
#     _point = sd.snowflake(color=color)


def move_snowflakes():
    pass


def screen_numbers_reached_down():
    pass


def delete_snowflakes(numbers):
    pass


