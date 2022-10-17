# Написать программу, которая получит имя и возраст пользователя, проверяет возраст и выдаёт приветственное сообщение
# в зависимости от возраста: - меньше нуля или ноль или не число: “Ошибка, повторите ввод”; - больше нуля до 10 не
# включая: “Привет, шкет #Имя#”; - от 10 до 18 включая: “Как жизнь #Имя#?” - больше 18 и меньше 100: “Что желаете
# #Имя#?” - в противном случае: “#Имя#, вы лжете - в наше время столько не живут...” Программу необходимо завернуть в
# вечный цикл. После очередной отработки кода, спрашивать у пользователя "Желаете выйти? (Д/Y)". Если ответ будет
# буква "Д" или буква "Y" в любом регистре, то произвести выход из вечного цикла. В противном случае продолжить
# выполнение программы заново.

while True:

    name = input(" Введите ваше имя: ")
    age = input(" Введите ваш возраст: ")

    if not age.isdigit() or int(age) <= 0:
        print("Ошибка, повторите ввод")
        offer = input("Желаете выйти? (Д/Y): ")
        if offer.upper() in ('Д', 'Y'):
            break
        continue
    elif int(age) < 10:
        print(f"Привет, шкет {name}")
        offer = input("Желаете выйти? (Д/Y): ")
        if offer.upper() in ('Д', 'Y'):
            break
        continue
    elif int(age) <= 18:
        print(f"Как жизнь, {name}")
        offer = input("Желаете выйти? (Д/Y): ")
        if offer.upper() in ('Д', 'Y'):
            break
        continue
    elif int(age) < 100:
        print(f"Что желаете, {name}")
        offer = input("Желаете выйти? (Д/Y): ")
        if offer.upper() in ('Д', 'Y'):
            break
        continue
    elif int(age) > 100:
        print(f"{name}, вы лжете - в наше время столько не живут... ")
        offer = input("Желаете выйти? (Д/Y): ")
        if offer.upper() in ('Д', 'Y'):
            break
