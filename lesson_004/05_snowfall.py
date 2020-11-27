# -*- coding: utf-8 -*-

import simple_draw as sd
import random
sd.resolution = (1200, 700)


# На основе кода из практической части реализовать снегопад:
# - создать списки данных для отрисовки N снежинок
# - нарисовать падение этих N снежинок
# - создать список рандомных длинн лучей снежинок (от 10 до 100) и пусть все снежинки будут разные

N = 3

# Пригодятся функции
# sd.get_point()
# sd.snowflake()
# sd.sleep()
# sd.random_number()
# sd.user_want_exit()
point_x = [100, 250, 400]
# for i in range(N):
#     point_x.append(sd.random_number(50, 1000))


point_y = [600, 550, 610]
# for i in range(N):
#     point_y.append(sd.random_number(550, 600))

length_snowflakes = []
for i in range(N):
    length_snowflakes.append(sd.random_number(50, 100))

step_falloff_snowflakes = []
for i in range(N):
    step_falloff_snowflakes.append(sd.random_number(100, 150))

# Для рандомные отклонения вправо/влево при каждом шаге
# step_falloff_snowflakes_x = []
# for i in range(N):
#     step_falloff_snowflakes_x.append(sd.random_number(-20, 20))

while True:
    sd.start_drawing()
    for i in range(N):
        center = sd.get_point(point_x[i], point_y[i])
        #  - на старом месте снежинки отрисовать её же, но цветом sd.background_color
        sd.snowflake(center=center, length=length_snowflakes[i], color=sd.background_color)
        #  - сдвинуть снежинку
        shifted_snowflake_y = point_y[i] - step_falloff_snowflakes[i]
        shifted_point = sd.get_point(point_x[i], shifted_snowflake_y)
        #  - отрисовать её цветом sd.COLOR_WHITE на новом месте
        sd.snowflake(center=shifted_point, length=length_snowflakes[i], color=sd.COLOR_WHITE)
        #  Для сохр след. итерации
        point_y[i] -= step_falloff_snowflakes[i]
        #  Проверка достиг ли дна экрана
        if point_y[i] < sd.random_number(40, 60):
            center = sd.get_point(point_x[i], point_y[i])
            sd.snowflake(center=center, length=length_snowflakes[i], color=sd.background_color)
            point_y[i] = 550
            length_snowflakes[i] = sd.random_number(10, 40)


    sd.finish_drawing()

    sd.sleep(0.5)
    if sd.user_want_exit():
        break

sd.pause()

# подсказка! для ускорения отрисовки можно
#  - убрать clear_screen()
#  - в начале рисования всех снежинок вызвать sd.start_drawing()
#  - на старом месте снежинки отрисовать её же, но цветом sd.background_color
#  - сдвинуть снежинку
#  - отрисовать её цветом sd.COLOR_WHITE на новом месте
#  - после отрисовки всех снежинок, перед sleep(), вызвать sd.finish_drawing()


# 4) Усложненное задание (делать по желанию)
# - сделать рандомные отклонения вправо/влево при каждом шаге
# - сделать сугоб внизу экрана - если снежинка долетает до низа, оставлять её там,
#   и добавлять новую снежинку
# Результат решения см https://youtu.be/XBx0JtxHiLg


