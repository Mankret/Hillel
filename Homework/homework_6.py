# Сделать программу в виде функций в которой нужно будет угадывать число.
import random

name_player = input("Введите ваше имя: ")
print(f"Привет, {name_player}, давай сыграем в игру")


def game():
    ent_numb = 0
    rand_number = random.randint(1, 20)
    while rand_number != ent_numb:
        ent_numb = int(input(f"{name_player}, угадайте число от 1 до 20 : "))

        if ent_numb < rand_number:
            print("Число должно быть больше",)

        elif ent_numb > rand_number:

            print("Число должно быть меньше", )
    else:
        print(f"Правильно, {name_player} — это число = " + str(rand_number))


game()
