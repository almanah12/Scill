# -*- coding: utf-8 -*-

from random import randint

# Доработать практическую часть урока lesson_007/python_snippets/08_practice.py

# Необходимо создать класс кота. У кота есть аттрибуты - сытость и дом (в котором он живет).
# Кот живет с человеком в доме.
# Для кота дом характеризируется - миской для еды и грязью.
# Изначально в доме нет еды для кота и нет грязи.

# Доработать класс человека, добавив методы
#   подобрать кота - у кота появляется дом.
#   купить коту еды - кошачья еда в доме увеличивается на 50, деньги уменьшаются на 50.
#   убраться в доме - степень грязи в доме уменьшается на 100, сытость у человека уменьшается на 20.
# Увеличить кол-во зарабатываемых человеком денег до 150 (он выучил пайтон и устроился на хорошую работу :)

# Кот может есть, спать и драть обои - необходимо реализовать соответствующие методы.
# Когда кот спит - сытость уменьшается на 10
# Когда кот ест - сытость увеличивается на 20, кошачья еда в доме уменьшается на 10.
# Когда кот дерет обои - сытость уменьшается на 10, степень грязи в доме увеличивается на 5
# Если степень сытости < 0, кот умирает.
# Так же надо реализовать метод "действуй" для кота, в котором он принимает решение
# что будет делать сегодня

# Человеку и коту надо вместе прожить 365 дней.

# TODO здесь ваш код
from random import randint

# Реализуем модель человека.
# Человек может есть, работать, играть, ходить в магазин.
# У человека есть степень сытости, немного еды и денег.
# Если сытость < 0 единиц, человек умирает.
# Человеку надо прожить 365 дней.
from termcolor import cprint


class Man:

    def __init__(self):
        self.name = 'Ora'
        self.fullness = 50
        self.house = None

    def __str__(self):
        return 'Я - {}, сытость {}'.format(
            self.name, self.fullness)

    def eat(self):
        if self.house.man_food >= 10:
            cprint('{} поел'.format(self.name), color='yellow')
            self.fullness += 10
            self.house.man_food -= 10
        else:
            cprint('{} нет еды'.format(self.name), color='red')

    def work(self):
        cprint('{} сходил на работу'.format(self.name), color='blue')
        self.house.money += 150
        self.fullness -= 10

    def watch_MTV(self):
        cprint('{} смотрел MTV целый день'.format(self.name), color='green')
        self.fullness -= 10

    def shopping(self):
        if self.house.money >= 50:
            cprint('{} сходил в магазин за едой'.format(self.name), color='magenta')
            self.house.money -= 50
            self.house.man_food += 50
        else:
            cprint('{} деньги кончились!'.format(self.name), color='red')

    def man_go_to_the_house(self, house):
        self.house = house
        self.fullness -= 10
        cprint('{} Вьехал в дом'.format(self.name), color='cyan')

    # Cat methods
    def man_take_cat(self, house):
        self.house = house
        cprint('Кошка приютился в доме', color='cyan')

    def cat_buy_food(self):
        self.house.cat_food += 50
        self.house.money -= 50
        cprint('Ора купил еды для кошки', color='cyan')

    # --------
    def clean_house(self):
        self.house.dirt -= 100
        self.fullness -= 20
        cprint('Ора почистил дом', color='cyan')


    def act(self):
        if self.fullness <= 0:
            cprint('{} умер...'.format(self.name), color='red')
            return
        dice = randint(1, 6)
        if self.fullness <= 20:
            self.eat()
        elif self.house.man_food < 20:
            self.shopping()
        elif self.house.money < 50:
            self.work()
        elif self.house.cat_food < 20:
            self.cat_buy_food()
        elif self.house.dirt >= 100:
            self.clean_house()
        elif dice == 1:
            self.work()
        elif dice == 2:
            self.eat()
        else:
            self.watch_MTV()

# Необходимо создать класс кота. У кота есть аттрибуты - сытость и дом (в котором он живет).
# Кот живет с человеком в доме.
# Для кота дом характеризируется - миской для еды и грязью.
# Изначально в доме нет еды для кота и нет грязи.

# Доработать класс человека, добавив методы
#   подобрать кота - у кота появляется дом.
#   купить коту еды - кошачья еда в доме увеличивается на 50, деньги уменьшаются на 50.
#   убраться в доме - степень грязи в доме уменьшается на 100, сытость у человека уменьшается на 20.
# Увеличить кол-во зарабатываемых человеком денег до 150 (он выучил пайтон и устроился на хорошую работу :)

# Кот может есть, спать и драть обои - необходимо реализовать соответствующие методы.
# Когда кот спит - сытость уменьшается на 10
# Когда кот ест - сытость увеличивается на 20, кошачья еда в доме уменьшается на 10.
# Когда кот дерет обои - сытость уменьшается на 10, степень грязи в доме увеличивается на 5
# Если степень сытости < 0, кот умирает.
# Так же надо реализовать метод "действуй" для кота, в котором он принимает решение
# что будет делать сегодня


class Cat:
    def __init__(self):
        self.name = 'Муся'
        self.fulness = 50
        self.house = None

    def __str__(self):
        return 'Кошка {}, сытость {}'.format(self.name, self.fulness)

    def man_take_cat(self, house):
        self.house = house

    def eat(self):
        if self.house.cat_food >= 10:
            cprint('Кошка {} покушала'.format(self.name), color='grey')
            self.fulness += 20
            self.house.cat_food -= 10
        else:
            cprint('Для кошки {} нет еды'.format(self.name), color='grey')



    def sleep(self):
        cprint('Кошка {} поспала'.format(self.name), color='green')
        self.fulness -= 10

    def tears_wallpaper(self):
        cprint('Кошка {} нагадила'.format(self.name), color='red')
        self.fulness -= 10
        self.house.dirt += 20

    def act(self):
        if self.fulness <= 0:
            cprint('Кошка {} умерла'.format(self.name))
            return
        choice_act = randint(1, 4)
        if self.fulness < 20:
            self.eat()
        elif choice_act == 1:
            self.eat()
        elif choice_act == 2:
            self.sleep()
        else:
            self.tears_wallpaper()


class House:
    def __init__(self):
        self.man_food = 50
        self.money = 100
        self.cat_food = 0
        self.dirt = 0

    def __str__(self):
        return 'В доме человеческой еды осталось {}, еды для кошки осталось {}, денег осталось {},' \
               'уровень грязи {}'.format(self.man_food, self.cat_food, self.money, self.dirt)


citisen = Man()

cat = Cat()
my_sweet_home = House()
cat_welcome_home = House()



citisen.man_go_to_the_house(house=my_sweet_home)
citisen.man_take_cat(house=cat_welcome_home)
cat.man_take_cat(house=cat_welcome_home)

for day in range(1, 366):
    print('================ день {} =================='.format(day))

    citisen.act()
    cat.act()
    print('--- в конце дня ---')

    print(citisen)
    print(cat)

    print(cat_welcome_home)


# Усложненное задание (делать по желанию)
# Создать несколько (2-3) котов и подселить их в дом к человеку.
# Им всем вместе так же надо прожить 365 дней.

# (Можно определить критическое количество котов, которое может прокормить человек...)
