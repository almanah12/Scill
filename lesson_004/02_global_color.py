# -*- coding: utf-8 -*-
import simple_draw as sd

sd.resolution = [800, 600]

print('Possible colors: ')
colors = ['0 : red', '1 : orange', '2 : yellow', '3 : green', '4 : cyan', '5 : blue', '6 : purple']
for i in range(len(colors)):
    print(colors[i])
number_user = 0
while number_user < 10:
    number_user = int(input('Enter the desire color >'))
    if number_user > 6 or number_user < 0:
        print('You entered incorrect number')
    else:
        break


# Добавить цвет в функции рисования геом. фигур. из упр lesson_004/01_shapes.py
# (код функций скопировать сюда и изменить)
# Запросить у пользователя цвет фигуры посредством выбора из существующих:
#   вывести список всех цветов с номерами и ждать ввода номера желаемого цвета.
# Потом нарисовать все фигуры этим цветом

# Пригодятся функции
# sd.get_point()
# sd.line()
# sd.get_vector()
# и константы COLOR_RED, COLOR_ORANGE, COLOR_YELLOW, COLOR_GREEN, COLOR_CYAN, COLOR_BLUE, COLOR_PURPLE
# Результат решения см lesson_004/results/exercise_02_global_color.jpg


sd.pause()
