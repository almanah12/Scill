# -*- coding: utf-8 -*-

import simple_draw as sd
sd.resolution = [800, 800]


# def draw_bunches(start_point, angle1, angle2, angle3, length,):
#     if length < 5:
#         return
#     v1 = sd.get_vector(start_point=start_point, angle=angle1, length=length,)
#     v1.draw()
#     v2 = sd.get_vector(start_point=v1.end_point, angle=angle2, length=length*.75,)
#     v2.draw()
#     v3 = sd.get_vector(start_point=v1.end_point, angle=angle3, length=length*.75,)
#     v3.draw()
#     next_point = v1.end_point
#     next_angle1 = angle1 - sd.random_number(18, 42)
#     next_angle2 = angle2 - sd.random_number(18, 42)
#     next_angle3 = angle3 - sd.random_number(18, 42)
#     next_length = length*.75
#     draw_bunches(start_point=next_point, angle1=next_angle1, angle2=next_angle2, angle3=next_angle3, length=next_length,)
#     next_angle1 = angle1 + sd.random_number(18, 42)
#     next_angle2 = angle2 + sd.random_number(18, 42)
#     next_angle3 = angle3 + sd.random_number(18, 42)
#     next_length = length*.75
#     draw_bunches(start_point=next_point, angle1=next_angle1, angle2=next_angle2, angle3=next_angle3, length=next_length,)
#
#
# root_point = sd.get_point(300, 30)
# draw_bunches(start_point=root_point, angle1=90, angle2=120, angle3=60, length=100, )

def draw_bunches(start_point, angle1, length,):
    if length < 5:
        return
    v1 = sd.get_vector(start_point=start_point, angle=angle1, length=length,)
    v1.draw()

    next_point = v1.end_point
    next_angle1 = angle1 - sd.random_number(30-30*.4, 30+30*.4)
    next_length = length*.75
    draw_bunches(start_point=next_point, angle1=next_angle1, length=next_length,)
    next_point = v1.end_point
    next_angle1 = angle1 + sd.random_number(30-30*.4, 30+30*.4)
    next_length = length*.75
    draw_bunches(start_point=next_point, angle1=next_angle1, length=next_length,)



root_point = sd.get_point(300, 30)
draw_bunches(start_point=root_point, angle1=90, length=100, )



# 1) Написать функцию draw_branches, которая должна рисовать две ветви дерева из начальной точки
# Функция должна принимать параметры:
# - точка начала рисования,
# - угол рисования,
# - длина ветвей,
# Отклонение ветвей от угла рисования принять 30 градусов,

# 2) Сделать draw_branches рекурсивной
# - добавить проверку на длину ветвей, если длина меньше 10 - не рисовать
# - вызывать саму себя 2 раза из точек-концов нарисованных ветвей,
#   с параметром "угол рисования" равным углу только что нарисованной ветви,
#   и параметром "длинна ветвей" в 0.75 меньшей чем длина только что нарисованной ветви

# 3) первоначальный вызов:
# root_point = get_point(300, 30)
# draw_bunches(start_point=root_point, angle=90, length=100)

# Пригодятся функции
# sd.get_point()
# sd.get_vector()
# Возможный результат решения см lesson_004/results/exercise_04_fractal_01.jpg

# можно поиграть -шрифтами- цветами и углами отклонения



# 4) Усложненное задание (делать по желанию)
# - сделать рандомное отклонение угла ветвей в пределах 40% от 30-ти градусов
# - сделать рандомное отклонение длины ветвей в пределах 20% от коэффициента 0.75
# Возможный результат решения см lesson_004/results/exercise_04_fractal_02.jpg

# Пригодятся функции
#sd.random_number()

sd.pause()


