# -*- coding: utf-8 -*-

import simple_draw as sd
sd.resolution = [800, 800]


# def triangle(angles_point, angle=0, length=100):
#     v1 = sd.get_vector(start_point=angles_point, angle=angle, length=length)
#     v1.draw()
#
#     v2 = sd.get_vector(start_point=v1.end_point, angle=120 + angle, length=length)
#     v2.draw()
#
#     v3 = sd.get_vector(start_point=v2.end_point, angle=240 + angle, length=length)
#     v3.draw()
#
#
# point = sd.get_point(50, 50)
# triangle(angles_point=point, angle=0, length=200)
#
#
# def sguare(start_poin, angle=0, length=100):
#     v1 = sd.get_vector(start_point=start_poin, angle=angle, length=length)
#     v1.draw()
#
#     v2 = sd.get_vector(start_point=v1.end_point, angle=90 + angle, length=length)
#     v2.draw()
#
#     v3 = sd.get_vector(start_point=v2.end_point, angle=180 + angle, length=length)
#     v3.draw()
#
#     v4 = sd.get_vector(start_point=v3.end_point, angle=270 + angle, length=length)
#     v4.draw()
#
#
# point_square = sd.get_point(500, 100)
# sguare(start_poin=point_square, angle=0, length=100)
#
#
# def pentagon(start_poin, angle=0, length=100):
#     v1 = sd.get_vector(start_point=start_poin, angle=angle, length=length)
#     v1.draw()
#
#     v2 = sd.get_vector(start_point=v1.end_point, angle=72 + angle, length=length)
#     v2.draw()
#
#     v3 = sd.get_vector(start_point=v2.end_point, angle=144 + angle, length=length)
#     v3.draw()
#
#     v4 = sd.get_vector(start_point=v3.end_point, angle=216 + angle, length=length)
#     v4.draw()
#
#     v5 = sd.get_vector(start_point=v4.end_point, angle=288 + angle, length=length)
#     v5.draw()
# point_pentagon = sd.get_point(50, 500)
# pentagon(start_poin=point_pentagon, angle=0)
#
#
# def hexagon(start_poin, angle=0, length=100):
#     v1 = sd.get_vector(start_point=start_poin, angle=angle, length=length)
#     v1.draw()
#
#     v2 = sd.get_vector(start_point=v1.end_point, angle=60 + angle, length=length)
#     v2.draw()
#
#     v3 = sd.get_vector(start_point=v2.end_point, angle=120 + angle, length=length)
#     v3.draw()
#
#     v4 = sd.get_vector(start_point=v3.end_point, angle=180 + angle, length=length)
#     v4.draw()
#
#     v5 = sd.get_vector(start_point=v4.end_point, angle=240 + angle, length=length)
#     v5.draw()
#
#     v6 = sd.get_vector(start_point=v5.end_point, angle=301 + angle, length=length)
#     v6.draw()
#
#
# point_hexagon = sd.get_point(500, 500)
# hexagon(start_poin=point_hexagon, angle=0, length=100)


# Часть 1.
# Написать функции рисования равносторонних геометрических фигур:
# - треугольника
# - квадрата
# - пятиугольника
# - шестиугольника
# Все функции должны принимать 3 параметра:
# - точка начала рисования
# - угол наклона
# - длина стороны
#
# Использование копи-пасты - обязательно! Даже тем кто уже знает про её пагубность. Для тренировки.
# Как работает копипаста:
#   - одну функцию написали,
#   - копипастим её, меняем название, чуть подправляем код,
#   - копипастим её, меняем название, чуть подправляем код,
#   - и так далее.
# В итоге должен получиться ПОЧТИ одинаковый код в каждой функции

# Пригодятся функции
# sd.get_point()
# sd.get_vector()
# sd.line()
# Результат решения см lesson_004/results/exercise_01_shapes.jpg


def common_angles(start_poin, angle=0, length=100, side=1):
    for i in range(side):
        if i != side - 1:
            vec_general = sd.get_vector(start_point=start_poin, angle= 360*(i/side) + angle, length=length)
            start_poin = vec_general.end_point
            vec_general.draw()
        else:
            sd.line(start_point=start_poin, end_point=point_common)



point_common = sd.get_point(300, 300)
side_angles = 5
common_angles(start_poin=point_common, angle=15, length=300, side=side_angles)

# Часть 1-бис.
# Попробуйте прикинуть обьем работы, если нужно будет внести изменения в этот код.
# Скажем, связывать точки не линиями, а дугами. Или двойными линиями. Или рисовать круги в угловых точках. Или...
# А если таких функций не 4, а 44?

# Часть 2 (делается после зачета первой части)
#
# Надо сформировать функцию, параметризированную в местах где была "небольшая правка".
# Это называется "Выделить общую часть алгоритма в отдельную функцию"
# Потом надо изменить функции рисования конкретных фигур - вызывать общую функцию вместо "почти" одинакового кода.
#
# В итоге должно получиться:
#   - одна общая функция со множеством параметров,
#   - все функции отрисовки треугольника/квадрата/етс берут 3 параметра и внутри себя ВЫЗЫВАЮТ общую функцию.
#
# Не забудте в этой общей функции придумать, как устранить разрыв
#   в начальной/конечной точках рисуемой фигуры (если он есть)

# Часть 2-бис.
# А теперь - сколько надо работы что бы внести изменения в код? Выгода на лицо :)
# Поэтому среди программистов есть принцип D.R.Y. https://clck.ru/GEsA9
# Будьте ленивыми, не используйте копи-пасту!


sd.pause()
