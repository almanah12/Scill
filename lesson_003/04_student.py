# -*- coding: utf-8 -*-

# (цикл while)

# Ежемесячная стипендия студента составляет educational_grant руб., а расходы на проживание превышают стипендию
# и составляют expenses руб. в месяц. Рост цен ежемесячно увеличивает расходы на 3%, кроме первого месяца
# Составьте программу расчета суммы денег, которую необходимо единовременно попросить у родителей,
# чтобы можно было прожить учебный год (10 месяцев), используя только эти деньги и стипендию.
# Формат вывода:
#   Студенту надо попросить ХХХ.ХХ рублей

educational_grant, expenses = 10000, 12000
summa_expenses = 0
i = 0
# TODO здесь ваш код
for i in range(10):
    if i == 0:
        summa_expenses += expenses
    else:
        summa_expenses += expenses + expenses * 0.03

sum_ask_parents = summa_expenses - educational_grant * 10
print('the amount to ask the parents:', sum_ask_parents)
