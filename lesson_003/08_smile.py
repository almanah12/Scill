# -*- coding: utf-8 -*-

# (определение функций)
import simple_draw

# Написать функцию отрисовки смайлика в произвольной точке экрана
# Форма рожицы-смайлика на ваше усмотрение
# Параметры функции: кордината X, координата Y, цвет.
# Вывести 10 смайликов в произвольных точках экрана.
def smailik(point, radius):
    #eyes
    eye1 = simple_draw.get_point(point.x-radius*.35, point.y+radius*.35)
    eye2 = simple_draw.get_point(point.x + radius*.35, point.y + radius*.35)
    simple_draw.circle(center_position=eye1, radius=radius*.1, color=simple_draw.COLOR_GREEN, width=0)
    simple_draw.circle(center_position=eye2, radius=radius*.1, color=simple_draw.COLOR_GREEN, width=0)
    #nose
    nose_point1 = simple_draw.get_point(point.x, point.y + radius*.5)
    nose_point2 = simple_draw.get_point(point.x, point.y - radius*.25)
    simple_draw.line(nose_point1, nose_point2, width=2)
    #mouth
    mouth_point1 = simple_draw.get_point(point.x - radius*.3, point.y - radius*.4)
    mouth_point2 = simple_draw.get_point(point.x + radius*.3, point.y - radius*.4)
    simple_draw.line(mouth_point1, mouth_point2, width=1)
    simple_draw.get_vector(start_point=mouth_point1, angle=150, length=radius*.25).draw()
    simple_draw.get_vector(start_point=mouth_point2, angle=30, length=radius * .25).draw()
    #full face
    simple_draw.circle(center_position=point, radius=radius)
    #body
    body_point1 = simple_draw.get_point(point.x, point.y - radius)
    body = simple_draw.get_vector(start_point=body_point1, angle=270, length=radius*2)
    body.draw()
    #legs
    simple_draw.get_vector(start_point=body.end_point, angle=240, length=radius*1.7).draw()
    simple_draw.get_vector(start_point=body.end_point, angle=300, length=radius*1.7).draw()
    #arms
    arm_point = simple_draw.get_point(point.x, point.y - radius*1.7)
    simple_draw.get_vector(start_point=arm_point, angle=140, length=radius*1.6).draw()
    simple_draw.get_vector(start_point=arm_point, angle=40, length=radius * 1.6).draw()

for _ in range(10):
    point = simple_draw.random_point()
    smailik(point=point, radius=30)

# simple_draw.random_point().x +150
# point = simple_draw.random_point()
# print(simple_draw.get_point(point.x, point.y))
simple_draw.pause()
