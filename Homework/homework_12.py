# Написать декоратор к 2-м любым функциям, который бы считал и выводил время их выполнения.
# Подсказка:
# from datetime import datetime
# time = datetime.now()
from datetime import datetime


def new_decorator(n_func):
    def time():
        time_now = datetime.now()
        n_func()
        print("Lead time", datetime.now() - time_now)
    return time


@new_decorator
def compound():
    sentence_1 = [1, 2, 543, 'der', 'Sam']
    sentence_2 = [22, 'Far', 6]
    print(sentence_1 + sentence_2)


@new_decorator
def calcul():
    first_val = 23451
    second_val = 768542
    print("Answer is :", first_val + second_val)


compound()
print('-' * 50)
calcul()
