#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Есть словарь координат городов

sites = {
    'Moscow': (550, 370),
    'London': (510, 510),
    'Paris': (480, 480),
}

# Составим словарь словарей расстояний между ними
# расстояние на координатной сетке - корень из (x1 - x2) ** 2 + (y1 - y2) ** 2

distances = {'Moscow to London': (((sites['Moscow'][0]-sites['London'][0])**2+(sites['Moscow'][1]-sites['London'][1])**2)**1/2),
             'Moscow to Paris': (((550-480)**2+(370-480)**2)**1/2),
             'London to Paris': (((510-480)**2+(510-480)**2)**1/2),
             }

# TODO здесь заполнение словаря
print(sites['Moscow'][0])
print(sites)
print(distances)




