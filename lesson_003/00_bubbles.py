# -*- coding: utf-8 -*-

import simple_draw as sd


sd.resolution = (1200, 600)

# Нарисовать пузырек - три вложенных окружностей с шагом 5 пикселей
point = sd.get_point(500, 500)
radius = 50

# Написать функцию рисования пузырька, принммающую 2 (или более) параметра: точка рисовании и шаг
def bbuble(point, step,color):
    radius = 5
    for _ in range(3):
        radius += step
        sd.circle(center_position=point, radius=radius, color= color)


# Нарисовать 10 пузырьков в ряд
# TODO здесь ваш код
#for x in range(100, 1100, 100):
#    point = sd.get_point(x, 100)
#    bbuble(point=point, step=5)
# Нарисовать три ряда по 10 пузырьков
# Нарисовать 100 пузырьков в произвольных местах экрана случайными цветами
# TODO здесь ваш код
for _ in range(100):
    point = sd.random_point()
    color = sd.random_color()
    bbuble(point=point, step=15, color=color)
sd.pause()


