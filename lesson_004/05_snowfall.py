# -*- coding: utf-8 -*-

import simple_draw as sd
import random
sd.resolution = (1200, 700)


# На основе кода из практической части реализовать снегопад:
# - создать списки данных для отрисовки N снежинок
# - нарисовать падение этих N снежинок
# - создать список рандомных длинн лучей снежинок (от 10 до 100) и пусть все снежинки будут разные

N = 20

# Пригодятся функции
# sd.get_point()
# sd.snowflake()
# sd.sleep()
# sd.random_number()
# sd.user_want_exit()
point_x = []
for i in range(N):
    point_x.append(sd.random_number(50, 1000))


point_y = []
for i in range(N):
    point_y.append(sd.random_number(550, 600))

while True:
    sd.clear_screen()
    for i in range(N):
        center = sd.get_point(point_x[i], point_y[i])
        sd.snowflake(center=center, length=sd.random_number(10, 100), factor_a=random.uniform(.5, .6), factor_b=random.uniform(.3, .4), factor_c=sd.random_number(25, 35))
        point_y[i] -= 50
        if  point_y[i]<50:
            break
        sd.sleep(0.1)
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


