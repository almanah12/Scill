# -*- coding: utf-8 -*-

import simple_draw as sd

sd.resolution = (1200, 600)
# познакомится с параметрами библиотечной функции рисования снежинки sd.snowflake()

# sd.snowflake(center=point_0, length=200, factor_a=0.5)

# реализовать падение одной снежинки
point_x = [100, 150, 200]
point_y = [500, 450, 500]
# y = 500
# x = 100
#
y2 = 450
x2 = 150

x3 = 200
y3 = 500
while True:
    sd.start_drawing()
    point2 = sd.get_point(x2, y2)
    sd.snowflake(center=point2, length=30, color=sd.background_color)
    yx = y2 - 10
    if yx < 50:
        break
    point2x = sd.get_point(x2, yx)
    sd.snowflake(center=point2x, length=30,)
    sd.finish_drawing()
    sd.sleep(.1)

    # for i in range(3):
    #     sd.start_drawing()
    #     point = sd.get_point(point_x[i], point_y[i])
    #     sd.snowflake(center=point,)
    #     sd.finish_drawing()
    #
    #     sd.start_drawing()
    #     sd.snowflake(center=point, length=50, color=sd.background_color)
    #     sd.finish_drawing()
    #     point_y[i] -= 10
    #     if point_y[i] < 50:
    #         break

    y2 -= 10
    if y2 < 50:
        break


    # sd.finish_drawing()
    # sd.start_drawing()
    # point3 = sd.get_point(x3, y3)
    # sd.snowflake(center=point3, length=150, color=sd.background_color)
    # sd.snowflake(center=point3, length=150)
    # y3 -= 20
    # if y3 < 50:
    #     break

    sd.sleep(.1)
    if sd.user_want_exit():
        break

# реализовать падение одной снежинки из произвольного места экрана

# реализовать падение одной снежинки с ветром - смещение в сторону


sd.pause()
