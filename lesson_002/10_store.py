#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Есть словарь кодов товаров

goods = {
    'Лампа': '12345',
    'Стол': '23456',
    'Диван': '34567',
    'Стул': '45678',
}

# Есть словарь списков количества товаров на складе.

store = {
    '12345': [
        {'quantity': 27, 'price': 42},
    ],
    '23456': [
        {'quantity': 22, 'price': 510},
        {'quantity': 32, 'price': 520},
    ],
    '34567': [
        {'quantity': 2, 'price': 1200},
        {'quantity': 1, 'price': 1150},
    ],
    '45678': [
        {'quantity': 50, 'price': 100},
        {'quantity': 12, 'price': 95},
        {'quantity': 43, 'price': 97},
    ],
}

# Рассчитать на какую сумму лежит каждого товара на складе
# например для ламп

lamps_cost = store[goods['Лампа']][0]['quantity'] * store[goods['Лампа']][0]['price']
# или проще (/сложнее ?)
lamp_code = goods['Лампа']
lamps_item = store[lamp_code][0]
lamps_quantity = lamps_item['quantity']
lamps_price = lamps_item['price']
lamps_cost = lamps_quantity * lamps_price
print('Лампа -', lamps_quantity, 'шт, стоимость', lamps_cost, 'руб')

# Вывести стоимость каждого товара на складе: один раз распечать сколько всего столов, стульев и т.д. на складе
# Формат строки <товар> - <кол-во> шт, стоимость <общая стоимость> руб

# WARNING для знающих циклы: БЕЗ циклов. Да, с переменными; да, неэффективно; да, копипаста.
# Это задание на ручное вычисление - что бы потом понять как работают циклы и насколько с ними проще жить.
table_code = goods['Стол']
table_guantity1=store[table_code][0]['quantity']
table_guantity2=store[table_code][1]['quantity']
table_price1=store[table_code][0]['price']
table_price2=store[table_code][1]['price']
all_quantity_tables = table_guantity1 + table_guantity2
whole_cost_table = table_guantity1*table_price1+table_guantity2*table_price2
print('Tables: ',all_quantity_tables,'pieces, cost:',whole_cost_table)

code_sofa = goods['Диван']
quantity_sofa1 = store[code_sofa][0]['quantity']
quantity_sofa2 = store[code_sofa][1]['quantity']
price_sofa1 = store[code_sofa][0]['price']
price_sofa2 = store[code_sofa][1]['price']
all_quantity_sofas = quantity_sofa1+quantity_sofa2
whole_cost_sofas = quantity_sofa1*price_sofa1+quantity_sofa2*price_sofa2
print('Sofas: ',all_quantity_sofas,'pieces, whole cost:',whole_cost_sofas)


code_chair = goods['Стул']
chair_quantity1 = store[code_chair][0]['quantity']
chair_quantity2 = store[code_chair][1]['quantity']
chair_quantity3 = store[code_chair][2]['quantity']
chair_price1 = store[code_chair][0]['price']
chair_price2 = store[code_chair][1]['price']
chair_price3 = store[code_chair][2]['price']
all_quantity_chairs = chair_quantity1+chair_quantity2+chair_quantity3
whole_cost_chairs = chair_quantity1*chair_price1+chair_quantity2*chair_price2+chair_quantity3*chair_price3
print('Chairs:',all_quantity_chairs,'pieces, cost:',whole_cost_chairs)
print(chair_price1)

##########################################################################################
# ВНИМАНИЕ! После того как __ВСЯ__ домашняя работа сделана и запушена на сервер,         #
# нужно зайти в ЛМС (LMS - Learning Management System ) по адресу http://go.skillbox.ru  #
# и оформить попытку сдачи ДЗ! Без этого ДЗ не будет проверяться!                        #
# Как оформить попытку сдачи смотрите видео - https://youtu.be/qVpN0L-C3LU               #
##########################################################################################






