# -*- coding: utf-8 -*-

# (определение функций)
import simple_draw

# Написать функцию отрисовки смайлика в произвольной точке экрана
# Форма рожицы-смайлика на ваше усмотрение
# Параметры функции: кордината X, координата Y, цвет.
# Вывести 10 смайликов в произвольных точках экрана.
def smailik(point):
    eye1 = simple_draw.get_point(point.x-7, point.y+7)
    eye2 = simple_draw.get_point(point.x + 7, point.y + 7)
    simple_draw.circle(center_position=eye1, radius=2, color=simple_draw.COLOR_GREEN, width=0)
    simple_draw.circle(center_position=eye2, radius=2, color=simple_draw.COLOR_GREEN, width=0)
    nose_point1 = simple_draw.get_point(point.x, point.y +10)
    nose_point2 = simple_draw.get_point(point.x, point.y - 5)
    simple_draw.line(nose_point1, nose_point2, width=2)
    mouth_point1 = simple_draw.get_point(point.x - 6, point.y - 7)
    mouth_point2 = simple_draw.get_point(point.x + 6, point.y - 7)
    simple_draw.line(mouth_point1, mouth_point2, width=2)

    simple_draw.circle(center_position=point, radius=20)

for _ in range(10):
    point = simple_draw.random_point()
    print(point)
    smailik(point)

# simple_draw.random_point().x +150
# point = simple_draw.random_point()
# print(simple_draw.get_point(point.x, point.y))
simple_draw.pause()
