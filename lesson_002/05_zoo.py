#!/usr/bin/env python
# -*- coding: utf-8 -*-

# есть список животных в зоопарке

zoo = ['lion', 'kangaroo', 'elephant', 'monkey', ]

# посадите медведя (bear) между львом и кенгуру
#  и выведите список на консоль
zoo.insert(1,'bear')
print(zoo)

# добавьте птиц из списка birds в последние клетки зоопарка
birds = ['rooster', 'ostrich', 'lark', ]
#  и выведите список на консоль
print(zoo+birds)
# уберите слона
#  и выведите список на консоль
zoo.pop(3)
print(zoo+birds)


# выведите на консоль в какой клетке сидит лев (lion) и жаворонок (lark).
# Номера при выводе должны быть понятны простому человеку, не программисту.
for link in enumerate(zoo):
    if 'lion' in link:
        print('the lark is in cage ' + str(link[0]+1))
for link in enumerate(birds):
    if 'lark' in link:
        print('the lark is in cage '+str(link[0]+1))
