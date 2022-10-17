# Ввести с клавиатуры целое число n.
# Получить сумму кубов всех целых чисел от 1 до n(включая n). Исключения составляют все числа кратные цифре 3.
# Реализовать в 2-х вариантах: используя цикл while и цикл for

number = int(input("Введите число: "))
csum = 0

for numb in range(number+1):
    if numb % 3 == 0:
        continue
    csum += numb**3
print(csum)

while number < 0:
    csum = range(number+1)
    if number % 3 == 0:
        csum += number**3
print(csum)

