from random import randint

count_move = 0
_quess_number = 0


def quess_number_func():
    global _quess_number
    _quess_number = 0
    _quess_number = randint(1000, 10000)


def check_number():
    enter_number = input('Input the number:')
    print(_quess_number)
    global count_move
    cow = 0
    bulls = 0
    b = 0
    c = 0

    while True:
        for i in str(_quess_number):
            b += 1
            a = 0
            for k in str(enter_number):
                a += 1
                if i == k and b == a:
                    bulls += 1

        for i in str(_quess_number):
            c += 1
            a = 0
            for k in str(enter_number):
                a += 1
                if i == k and c != a:
                    cow += 1

        print({'bulls': bulls, 'cows': cow})
        break


    count_move += 1
    if enter_number == 'x':
        return 0
    elif bulls == 4:
        print('Move count:', count_move)
        answer = input('Want to play again?y/n')
        if answer == 'y':
            quess_number_func()
            check_number()
        elif answer == 'n':
            return 0
    elif bulls != 4:
        check_number()
    print(count_move)


















