# -*- coding: utf-8 -*-

from termcolor import cprint
from random import randint

######################################################## Часть первая
#
# Создать модель жизни небольшой семьи.
#
# Каждый день участники жизни могут делать только одно действие.
# Все вместе они должны прожить год и не умереть.
#
# Муж может:
#   есть,
#   играть в WoT,
#   ходить на работу,
# Жена может:
#   есть,
#   покупать продукты,
#   покупать шубу,
#   убираться в доме,

# Все они живут в одном доме, дом характеризуется:
#   кол-во денег в тумбочке (в начале - 100)
#   кол-во еды в холодильнике (в начале - 50)
#   кол-во грязи (в начале - 0)
#
# У людей есть имя, степень сытости (в начале - 30) и степень счастья (в начале - 100).
#
# Любое действие, кроме "есть", приводит к уменьшению степени сытости на 10 пунктов
# Кушают взрослые максимум по 30 единиц еды, степень сытости растет на 1 пункт за 1 пункт еды.
# Степень сытости не должна падать ниже 0, иначе чел умрет от голода.
#
# -Деньги в тумбочку добавляет муж, после работы - 150 единиц за раз.
# Еда стоит 10 денег 10 единиц еды. Шуба стоит 350 единиц.
#
# Грязь добавляется каждый день по 5 пунктов, за одну уборку жена может убирать до 100 единиц грязи.
# Если в доме грязи больше 90 - у людей падает степень счастья каждый день на 10 пунктов,
# Степень счастья растет: у мужа от игры в WoT (на 20), у жены от покупки шубы (на 60, но шуба дорогая)
# Степень счастья не должна падать ниже количество грязь10, иначе чел умрает от депресии.
#
# Подвести итоги жизни за год: сколько было заработано денег, сколько сьедено еды, сколько куплено шуб.


class House:

    def __init__(self):
        self.amount_money = 100
        self.food_fridge = 50
        self.amount_dirt = 0
        self.cat_food = 30
        self.all_money = 0
        self.all_food_eat = 0
        self.all_coat_amount = 0

    def __str__(self):
        return 'In house amount of money {}, food in fridge {},amount of dirt {}, ' \
               'food to cat {}'.format(
                 self.amount_money, self.food_fridge, self.amount_dirt, self.cat_food)

    def act_dirt(self):
        self.amount_dirt += 5

    def all_result(self):
        cprint('In year all of money {}, total food eat {}, total bought coats {}'.format(
            self.all_money, self.all_food_eat, self.all_coat_amount), color='cyan')


class Human:
    def __init__(self, name):
        self.name = name
        self.fullness = 30
        self.happiness = 100
        self.house = None

    def __str__(self):
        return '{} fullness {}, happiness {}'.format(self.name, self.fullness, self.happiness)

    def eat(self):
        self.house.food_fridge -= 30
        self.fullness += 30
        self.house.all_food_eat += 30
        cprint('{} eat the food'.format(self.name), color='yellow')

    def in_house(self, house):
        self.house = house

    def pet_of_cat(self):
        self.fullness -= 10
        self.happiness += 5
        cprint('{} pet of cat'.format(self.name), color='yellow')
        
    def act(self):
        # crisis
        if self.fullness <= 0:
            cprint('{} dead of hunger'.format(self.name), color='red')
            return False
        elif self.happiness <= 10:
            cprint('{} dead of depression'.format(self.name), color='magenta')
            return False
        elif self.house.amount_money <= 0:
            cprint('NO Money'.format(self.name), color='magenta')
            return False

        # need eating
        if self.fullness <= 20:
            self.eat()
            return False

        # happiness --
        if self.house.amount_dirt >= 90:
            self.happiness -= 10

        return True


class Husband(Human):
    def act(self):
        if super().act():
            dice = randint(1, 7)
            if self.house.amount_money <= 100:
                self.work()
            elif self.happiness <= 20:
                self.gaming()
            elif dice == 1:
                self.eat()
            elif dice == 2:
                self.gaming()
            elif dice == 3:
                self.pet_of_cat()
            else:
                self.work()

    def work(self):
        self.house.amount_money += 150
        self.house.all_money += 150
        self.fullness -= 10
        cprint('{} go to work'.format(self.name), color='yellow')

    def gaming(self):
        self.fullness -= 10
        self.happiness += 30
        cprint('{} played WoT'.format(self.name), color='yellow')


class Wife(Human):
    def act(self):
        if super().act():
            dice = randint(1, 6)
            # crisis
            if self.house.food_fridge <= 60:
                self.shopping()
            elif self.house.amount_dirt >= 110:
                self.clean_house()
            # cat food to buy
            elif self.house.cat_food <= 20:
                self.buy_food_cat()
            # happy
            elif self.happiness <= 20:
                self.buy_fur_coat()
                self.house.all_coat_amount += 1
            # lotto
            elif dice == 1:
                self.shopping()
            elif dice == 2:
                self.eat()
            elif dice == 3 and self.house.amount_money > 450:
                self.buy_fur_coat()
            else:
                self.pet_of_cat()

    def shopping(self):
        self.fullness -= 10
        self.house.food_fridge += 50
        self.house.amount_money -= 50
        cprint('{} go to shop'.format(self.name), color='yellow')

    def buy_food_cat(self):
        self.house.cat_food += 50
        self.house.amount_money -= 50
        self.fullness -= 10
        cprint('{} bought food to cat'.format(self.name), color='yellow')

    def buy_fur_coat(self):
        self.fullness -= 10
        self.happiness += 60
        self.house.amount_money -= 350
        cprint('{} bought a coat'.format(self.name), color='yellow')

    def clean_house(self):
        self.fullness -= 10
        self.house.amount_dirt -= 100
        cprint('{} cleaned the house'.format(self.name), color='yellow')
#
# После реализации первой части надо в ветке мастер продолжить работу над семьей - добавить ребенка
#
# Ребенок может:
#   есть,
#   спать,
#
# отличия от взрослых - кушает максимум 10 единиц еды,
# степень счастья  - не меняется, всегда ==100 ;)


class Child(Human):
    def act(self):
        if self.fullness <= 10:
            self.eat()
        dice = randint(1, 2)
        if dice == 1:
            self.eat()
        else:
            self.sleep()

    def eat(self):
        self.house.food_fridge -= 10
        self.fullness += 10
        cprint('{} eat'.format(self.name), color='yellow')

    def sleep(self):
        self.fullness -= 10
        cprint('{} sleep'.format(self.name), color='yellow')


class Cat:
    """Cat"""

    def __init__(self, name, house):
        self.name = name
        self.fullness = 30
        self.house = house

    def __str__(self):
        return 'Cat {} fullness {}'.format(self.name, self.fullness)

    def act(self):
        if self.fullness <= 0:
            cprint('Cat {} dead of hunger'.format(self.name), color='red')
            return
        dice = randint(1, 3)
        if self.fullness <= 10:
            self.eat()
        elif dice == 1:
            self.eat()
        elif dice == 2:
            self.sleep()
        elif dice == 3:
            self.soil()

    def eat(self):
        self.house.cat_food -= 10
        self.fullness += 10
        cprint('Cat {} eat'.format(self.name), color='grey')

    def sleep(self):
        self.fullness -= 10
        cprint('Cat {} sleep'.format(self.name), color='grey')

    def soil(self):
        self.fullness -= 10
        self.house.amount_dirt += 5
        cprint('Cat {} soil'.format(self.name), color='grey')


home = House()
mike = Husband(name='Mike')
sara = Wife(name='Sara')
nick = Child(name='Nick')
black = Cat(name='Black', house=home)
mike.in_house(home)
sara.in_house(home)
nick.in_house(home)


for day in range(365):
    if day != 364:
        cprint('================== День {} =================='.format(day), color='red')
        mike.act()
        sara.act()
        nick.act()
        black.act()
        home.act_dirt()
        cprint(mike, color='cyan')
        cprint(sara, color='cyan')
        cprint(nick, color='cyan')
        cprint(black, color='cyan')
        cprint(home, color='cyan')
    else:
        cprint('================== День {} =================='.format(day), color='red')
        mike.act()
        sara.act()
        nick.act()
        black.act()
        home.act_dirt()
        cprint(mike, color='cyan')
        cprint(sara, color='cyan')
        cprint(nick, color='cyan')
        cprint(black, color='cyan')
        cprint(home, color='cyan')
        cprint(home.all_result(), color='cyan')


# TODO после реализации первой части - отдать на проверку учителю

######################################################## Часть вторая
#
# После подтверждения учителем первой части надо
# отщепить ветку develop и в ней начать добавлять котов в модель семьи
#
# Кот может:
#   есть,
#   спать,
#   драть обои
#
# Люди могут:
#   гладить кота (растет степень счастья на 5 пунктов)
#
# В доме добавляется:
#   еда для кота (в начале - 30)
#
# У кота есть имя и степень сытости (в начале - 30)
# Любое действие кота, кроме "есть", приводит к уменьшению степени сытости на 10 пунктов
# Еда для кота покупается за деньги: за 10 денег 10 еды.
# Кушает кот максимум по 10 единиц еды, степень сытости растет на 2 пункта за 1 пункт еды.
# Степень сытости не должна падать ниже 0, иначе кот умрет от голода.
#
# Если кот дерет обои, то грязи становится больше на 5 пунктов




######################################################## Часть вторая бис
#
# После реализации первой части надо в ветке мастер продолжить работу над семьей - добавить ребенка
#
# Ребенок может:
#   есть,
#   спать,
#
# отличия от взрослых - кушает максимум 10 единиц еды,
# степень счастья  - не меняется, всегда ==100 ;)


# TODO после реализации второй части - отдать на проверку учителем две ветки


######################################################## Часть третья
#
# после подтверждения учителем второй части (обоих веток)
# влить в мастер все коммиты из ветки develop и разрешить все конфликты
# отправить на проверку учителем.


# home = House()
# serge = Husband(name='Сережа')
# masha = Wife(name='Маша')
# kolya = Child(name='Коля')
# murzik = Cat(name='Мурзик')
#
# for day in range(365):
#     cprint('================== День {} =================='.format(day), color='red')
#     serge.act()
#     masha.act()
#     kolya.act()
#     murzik.act()
#     cprint(serge, color='cyan')
#     cprint(masha, color='cyan')
#     cprint(kolya, color='cyan')
#     cprint(murzik, color='cyan')


# Усложненное задание (делать по желанию)
#
# Сделать из семьи любителей котов - пусть котов будет 3, или даже 5-10.
# Коты должны выжить вместе с семьей!
#
# Определить максимальное число котов, которое может прокормить эта семья при значениях зарплаты от 50 до 400.
# Для сглаживание случайностей моделирование за год делать 3 раза, если 2 из 3х выжили - считаем что выжили.
#
# Дополнительно вносить некий хаос в жизнь семьи
# - N раз в год вдруг пропадает половина еды из холодильника (коты?)
# - K раз в год пропадает половина денег из тумбочки (муж? жена? коты?!?!)
# Промоделировать - как часто могут случаться фейлы что бы это не повлияло на жизнь героев?
#   (N от 1 до 5, K от 1 до 5 - нужно вычислит максимумы N и K при котором семья гарантированно выживает)
#
# в итоге должен получится приблизительно такой код экспериментов
# for food_incidents in range(6):
#   for money_incidents in range(6):
#       life = Simulation(money_incidents, food_incidents)
#       for salary in range(50, 401, 50):
#           max_cats = life.experiment(salary)
#           print(f'При зарплате {salary} максимально можно прокормить {max_cats} котов')

