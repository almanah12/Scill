#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Создайте списки:

# моя семья (минимум 3 элемента, есть еще дедушки и бабушки, если что)
my_family = ['abay', 'ora', 'almas']


# список списков приблизителного роста членов вашей семьи
my_family_height = [
    # ['имя', рост],
    ['abay', 178],
    ['ora', 180],
    ['almas', 173],
]

# Выведите на консоль рост отца в формате
#   Рост отца - ХХ см
print('Heigh abay - '+ str(my_family_height[0][1])+'cm')
print('Heigh ora - '+ str(my_family_height[1][1])+'cm')
print('Heigh almas - '+ str(my_family_height[2][1])+'cm')
# Выведите на консоль общий рост вашей семьи как сумму ростов всех членов
#   The overall growth of my family - ХХ см
print('The overall growth of my family - '+ str(my_family_height[0][1]+my_family_height[1][1]+my_family_height[1][1])+'cm')
