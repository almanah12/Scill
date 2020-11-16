# -*- coding: utf-8 -*-

# (цикл for)
import simple_draw

# Нарисовать стену из кирпичей. Размер кирпича - 100х50
# Использовать вложенные циклы for


for k in range(12):
    for i in range(7):
        if k%2 == 0:
            simple_draw.rectangle(simple_draw.get_point(i*100, k*50), simple_draw.get_point(100 + i*100, 50 + k*50), width=1)
        elif k%2 != 0:
            simple_draw.rectangle(simple_draw.get_point(-50 + i*100, k*50), simple_draw.get_point(50 + i*100, 50 + k*50), width=1)


simple_draw.pause()
