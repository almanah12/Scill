from random import randint

count_move = 0
_ques_number = 0


def quess_number_func():
    global _ques_number
    _ques_number = 0
    _ques_number = randint(1000, 10000)


def check_number(num):
    #enter_number = input('Input the number:')
    print(_ques_number)
    print(num)
    cow = 0
    bulls = 0
    b = 0
    c = 0

    while True:
        for i in str(_ques_number):
            b += 1
            a = 0
            for k in str(num):
                a += 1
                if i == k and b == a:
                    bulls += 1

        for i in str(_ques_number):
            c += 1
            a = 0
            for k in str(num):
                a += 1
                if i == k and c != a:
                    cow += 1

        print({'bulls': bulls, 'cows': cow})
        break
    #
    # count_move += 1
    # if num == 'x':
    #     return 0
    # elif bulls == 4:
    #     print('Move count:', count_move)
    #     answer = input('Want to play again?y/n')
    #     if answer == 'y':
    #         quess_number_func()
    #         check_number(num)
    #     elif answer == 'n':
    #         return 0
    # elif bulls != 4:
    #     check_number(num)
