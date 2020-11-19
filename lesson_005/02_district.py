# -*- coding: utf-8 -*-

# Составить список всех живущих на районе и Вывести на консоль через запятую
# Формат вывода: На районе живут ...
# подсказка: для вывода элементов списка через запятую можно использовать функцию строки .join()
# https://docs.python.org/3/library/stdtypes.html#str.join

from central_street.house1 import room1 as cs_h1_r1
from central_street.house1 import room2 as cs_h1_r2
from central_street.house2 import room1 as cs_h2_r1
from central_street.house2 import room2 as cs_h2_r2
from soviet_street.house1 import room1 as ss_h1_r1
from soviet_street.house1 import room2 as ss_h1_r2
from soviet_street.house2 import room1 as ss_h2_r1
from soviet_street.house2 import room2 as ss_h2_r2

houses = [cs_h1_r1, cs_h1_r2, cs_h2_r1, cs_h2_r2, ss_h1_r1, ss_h1_r2, ss_h2_r1, ss_h2_r2]

print('Live in the district:')
for i in range(len(houses)):
    if i != len(houses) - 1 and bool(houses[i].folks):
        print(','.join(houses[i].folks), end=",")
    elif i == len(houses) - 1 and bool(houses[i].folks):
        print(','.join(houses[i].folks))

